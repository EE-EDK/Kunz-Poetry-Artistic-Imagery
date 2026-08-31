"""Force-align a poem's ElevenLabs voice track to its transcript.

Usage:
  python scripts/align_timings.py 01
  python scripts/align_timings.py 01 02 03
  python scripts/align_timings.py --all
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import paths  # noqa: E402
from scripts.bootstrap import spoken_words, words_to_srt  # noqa: E402


def load_catalog() -> dict:
    return json.loads(paths.CATALOG.read_text(encoding="utf-8"))


def find_poem(catalog: dict, token: str) -> dict:
    token = token.strip().lower().lstrip("0") or "0"
    for poem in catalog["poems"]:
        folder = poem["folder"]
        if folder == token or folder.startswith(token.zfill(2) + "-") or folder.startswith(token + "-"):
            return poem
        if str(poem["id"]) == token or f"{poem['id']:02d}" == token.zfill(2):
            return poem
        if poem["slug"] == token:
            return poem
    raise SystemExit(f"No poem matching {token!r}")


def voice_file(poem: dict) -> Path | None:
    audio_dir = paths.POEMS / poem["folder"] / "audio" / "elevenlabs"
    if not audio_dir.exists():
        return None
    folder = poem["folder"]
    for name in (
        f"{folder}-voice-FINAL.wav",
        f"{folder}-voice-FINAL.mp3",
        f"{folder}-voice-final.wav",
        f"{folder}-voice-final.mp3",
        f"{folder}-voice.wav",
        f"{folder}-voice.mp3",
    ):
        candidate = audio_dir / name
        if candidate.exists():
            return candidate
    for ext in (".wav", ".mp3", ".flac", ".m4a"):
        hits = sorted(
            p for p in audio_dir.glob(f"*{ext}")
            if "-v" not in p.stem.lower() and "-female" not in p.stem.lower()
        )
        if hits:
            return hits[0]
    return None


def to_plain(obj):
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    return obj


def align_poem(client: ElevenLabs, poem: dict) -> None:
    audio_path = voice_file(poem)
    if audio_path is None:
        print(f"Skip {poem['folder']}: no elevenlabs voice file")
        return
    transcript_path = paths.POEMS / poem["folder"] / "transcript.txt"
    transcript = transcript_path.read_text(encoding="utf-8").strip()
    print(f"Aligning {poem['folder']}  {audio_path.name} ({audio_path.stat().st_size} bytes)")
    with audio_path.open("rb") as handle:
        response = client.forced_alignment.with_raw_response.create(
            file=(audio_path.name, handle, "application/octet-stream"),
            text=transcript,
            request_options={"timeout_in_seconds": 300},
        )
    headers = {k.lower(): v for k, v in response.headers.items()}
    data = to_plain(response.data)
    words = [to_plain(w) for w in (data.get("words") or [])]
    characters = [to_plain(c) for c in (data.get("characters") or [])]
    payload = {
        "audio": audio_path.name,
        "transcript": transcript,
        "loss": data.get("loss"),
        "word_count": len(words),
        "character_count": len(characters),
        "headers": {
            "character-cost": headers.get("character-cost"),
            "request-id": headers.get("request-id"),
            "x-trace-id": headers.get("x-trace-id"),
        },
        "words": words,
        "characters": characters,
    }
    timing_dir = paths.POEMS / poem["folder"] / "timing"
    timing_dir.mkdir(parents=True, exist_ok=True)
    stem = poem["folder"]
    alignment_path = timing_dir / f"{stem}.alignment.json"
    words_path = timing_dir / f"{stem}.words.json"
    srt_path = timing_dir / f"{stem}.srt"
    alignment_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    spoken = spoken_words(payload)
    words_path.write_text(json.dumps(spoken, indent=2), encoding="utf-8")
    srt_path.write_text(words_to_srt(spoken), encoding="utf-8")
    print(
        f"  loss={payload['loss']!r} spoken_words={len(spoken)} "
        f"cost={payload['headers']['character-cost']!r} -> {timing_dir.relative_to(ROOT)}"
    )


def main() -> int:
    load_dotenv(ROOT / ".env")
    api_key = os.getenv("ELEVENLABS_API_KEY") or os.getenv("XI_API_KEY")
    if not api_key:
        print("Missing ELEVENLABS_API_KEY in .env", file=sys.stderr)
        return 1
    if not paths.CATALOG.exists():
        print("Run python scripts/bootstrap.py first.", file=sys.stderr)
        return 1

    catalog = load_catalog()
    args = sys.argv[1:]
    if not args or args == ["--all"]:
        targets = [p for p in catalog["poems"] if voice_file(p)]
    else:
        targets = [find_poem(catalog, a) for a in args]

    client = ElevenLabs(api_key=api_key)
    for poem in targets:
        align_poem(client, poem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
