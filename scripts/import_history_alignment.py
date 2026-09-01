"""Import native ElevenLabs TTS alignments from a history item.

Usage:
  python scripts/import_history_alignment.py 05 0EMTyGb2YqIHgCwMys4C
  python scripts/import_history_alignment.py 05 0EMTyGb2YqIHgCwMys4C --audio
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import paths  # noqa: E402
from scripts.align_timings import find_poem, load_catalog, to_plain  # noqa: E402
from scripts.bootstrap import spoken_words, words_to_srt  # noqa: E402

TAG = re.compile(r"\[[^\]]*\]")


def absolute_end(start: float, end_field: float) -> float:
    """History items store duration in character_end_times_seconds, not abs end."""
    if end_field >= start:
        return end_field
    return start + end_field


def strip_tags(text: str) -> str:
    cleaned = TAG.sub("", text)
    cleaned = re.sub(r"[ \t]*\n[ \t]*", "\n", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = re.sub(r" {2,}", " ", cleaned)
    return cleaned.strip() + "\n"


def chars_to_entries(block: dict) -> list[dict]:
    chars = block.get("characters") or []
    starts = block.get("character_start_times_seconds") or []
    ends = block.get("character_end_times_seconds") or []
    if not (len(chars) == len(starts) == len(ends)):
        raise SystemExit(
            f"alignment length mismatch chars={len(chars)} starts={len(starts)} ends={len(ends)}"
        )
    out = []
    i = 0
    n = len(chars)
    in_tag = False
    while i < n:
        ch = chars[i]
        start = float(starts[i])
        end = absolute_end(start, float(ends[i]))
        if ch == "[":
            in_tag = True
        out.append(
            {
                "text": ch,
                "start": start,
                "end": end,
                "tag": in_tag,
            }
        )
        if ch == "]":
            in_tag = False
        i += 1
    return out


def words_from_chars(entries: list[dict]) -> list[dict]:
    words: list[dict] = []
    buf: list[dict] = []

    def flush() -> None:
        if not buf:
            return
        text = "".join(e["text"] for e in buf).strip()
        if text:
            words.append(
                {
                    "text": text,
                    "start": buf[0]["start"],
                    "end": buf[-1]["end"],
                }
            )
        buf.clear()

    for entry in entries:
        if entry["tag"]:
            flush()
            continue
        if entry["text"].isspace():
            flush()
            continue
        buf.append(entry)
    flush()
    return words


def demote_final(audio_dir: Path, folder: str) -> None:
    for ext in (".wav", ".mp3"):
        current = audio_dir / f"{folder}-voice-FINAL{ext}"
        if not current.exists():
            continue
        n = 2
        while True:
            dest = audio_dir / f"{folder}-voice-v{n}{ext}"
            if not dest.exists():
                current.rename(dest)
                print(f"  demoted {current.name} -> {dest.name}")
                break
            n += 1


def write_audio(client: ElevenLabs, history_id: str, dest: Path) -> None:
    chunks = []
    for chunk in client.history.get_audio(
        history_id, request_options={"timeout_in_seconds": 180}
    ):
        chunks.append(chunk if isinstance(chunk, (bytes, bytearray)) else bytes(chunk))
    dest.write_bytes(b"".join(chunks))
    print(f"  audio {dest.name} ({dest.stat().st_size} bytes)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("poem")
    parser.add_argument("history_item_id")
    parser.add_argument(
        "--audio",
        action="store_true",
        help="Download history audio and make it the poem FINAL (demote current FINAL).",
    )
    args = parser.parse_args()

    load_dotenv(ROOT / ".env")
    api_key = os.getenv("ELEVENLABS_API_KEY") or os.getenv("XI_API_KEY")
    if not api_key:
        print("Missing ELEVENLABS_API_KEY in .env", file=sys.stderr)
        return 1

    catalog = load_catalog()
    poem = find_poem(catalog, args.poem)
    folder = poem["folder"]
    base = paths.POEMS / folder
    timing_dir = base / "timing"
    audio_dir = base / "audio" / "elevenlabs"
    timing_dir.mkdir(parents=True, exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)

    client = ElevenLabs(api_key=api_key)
    item = client.history.get(args.history_item_id, request_options={"timeout_in_seconds": 120})
    data = to_plain(item)
    alignments = data.get("alignments") or {}
    block = alignments.get("alignment") or alignments.get("normalized_alignment")
    if not block:
        print(f"History item {args.history_item_id} has no alignments", file=sys.stderr)
        return 1

    entries = chars_to_entries(block)
    tagged_text = "".join(e["text"] for e in entries)
    spoken_text = strip_tags(tagged_text)
    words = words_from_chars(entries)
    characters = [
        {"text": e["text"], "start": e["start"], "end": e["end"], "tag": e["tag"]}
        for e in entries
    ]
    audio_name = f"{folder}-voice-FINAL.mp3"
    payload = {
        "audio": audio_name,
        "history_item_id": args.history_item_id,
        "request_id": data.get("request_id"),
        "model_id": data.get("model_id"),
        "source": "elevenlabs-history",
        "transcript": spoken_text.strip(),
        "transcript_tts": tagged_text,
        "loss": None,
        "word_count": len(words),
        "character_count": len(characters),
        "words": words,
        "characters": characters,
    }

    stem = folder
    alignment_path = timing_dir / f"{stem}.alignment.json"
    words_path = timing_dir / f"{stem}.words.json"
    srt_path = timing_dir / f"{stem}.srt"
    alignment_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    spoken = spoken_words(payload)
    words_path.write_text(json.dumps(spoken, indent=2), encoding="utf-8")
    srt_path.write_text(words_to_srt(spoken), encoding="utf-8")
    (base / "transcript.spoken.txt").write_text(spoken_text, encoding="utf-8")
    (base / "transcript.tts.txt").write_text(tagged_text if tagged_text.endswith("\n") else tagged_text + "\n", encoding="utf-8")

    last = spoken[-1] if spoken else {}
    print(
        f"Imported {args.history_item_id} -> {timing_dir.relative_to(ROOT)}  "
        f"words={len(spoken)} last={last.get('text')!r} {last.get('start')}–{last.get('end')}"
    )

    if args.audio:
        demote_final(audio_dir, folder)
        write_audio(client, args.history_item_id, audio_dir / audio_name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
