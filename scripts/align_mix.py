"""Force-align a poem's mix-FINAL.wav to transcript.spoken.txt.

Usage:
  python scripts/align_mix.py 07
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
from scripts.align_timings import find_poem, load_catalog, to_plain  # noqa: E402
from scripts.bootstrap import spoken_words, words_to_srt  # noqa: E402


def mix_file(poem: dict) -> Path | None:
    mix_dir = paths.POEMS / poem["folder"] / "audio" / "mix"
    if not mix_dir.exists():
        return None
    folder = poem["folder"]
    for name in (
        f"{folder}-mix-FINAL.wav",
        f"{folder}-mix-FINAL.mp3",
        f"{folder}-mix-final.wav",
        f"{folder}-mix-final.mp3",
    ):
        candidate = mix_dir / name
        if candidate.exists():
            return candidate
    return None


def stt_preview(client: ElevenLabs, audio_path: Path) -> None:
    with audio_path.open("rb") as handle:
        result = client.speech_to_text.convert(
            file=handle,
            model_id="scribe_v2",
            timestamps_granularity="word",
        )
    data = to_plain(result)
    words = [
        w
        for w in (data.get("words") or [])
        if (w.get("type") or "word") == "word" and (w.get("text") or "").strip()
    ]
    print(f"STT words={len(words)} text={data.get('text', '')[:120]!r}")
    for w in words[:8]:
        print(f"  first  {w.get('start'):6.3f}-{w.get('end'):6.3f}  {w.get('text')!r}")
    for w in words[-8:]:
        print(f"  last   {w.get('start'):6.3f}-{w.get('end'):6.3f}  {w.get('text')!r}")


def align_mix(client: ElevenLabs, poem: dict) -> None:
    audio_path = mix_file(poem)
    if audio_path is None:
        raise SystemExit(f"No mix-FINAL for {poem['folder']}")
    base = paths.POEMS / poem["folder"]
    spoken_path = base / "transcript.spoken.txt"
    transcript_path = spoken_path if spoken_path.exists() else base / "transcript.txt"
    transcript = transcript_path.read_text(encoding="utf-8").strip()
    print(
        f"Aligning {poem['folder']}  {audio_path.name} ({audio_path.stat().st_size} bytes)  "
        f"text={transcript_path.name}"
    )
    print("--- STT preview ---")
    stt_preview(client, audio_path)
    print("--- forced alignment ---")
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
    timing_dir = base / "timing"
    timing_dir.mkdir(parents=True, exist_ok=True)
    stem = poem["folder"]
    (timing_dir / f"{stem}.alignment.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )
    spoken = spoken_words(payload)
    (timing_dir / f"{stem}.words.json").write_text(
        json.dumps(spoken, indent=2), encoding="utf-8"
    )
    (timing_dir / f"{stem}.srt").write_text(words_to_srt(spoken), encoding="utf-8")
    first = spoken[0] if spoken else {}
    last = spoken[-1] if spoken else {}
    print(
        f"  loss={payload['loss']!r} spoken_words={len(spoken)} "
        f"first={first.get('text')!r} {first.get('start')}-{first.get('end')} "
        f"last={last.get('text')!r} {last.get('start')}-{last.get('end')} "
        f"cost={payload['headers']['character-cost']!r}"
    )


def main() -> int:
    load_dotenv(ROOT / ".env")
    api_key = os.getenv("ELEVENLABS_API_KEY") or os.getenv("XI_API_KEY")
    if not api_key:
        print("Missing ELEVENLABS_API_KEY in .env", file=sys.stderr)
        return 1
    if len(sys.argv) < 2:
        print("Usage: python scripts/align_mix.py NN", file=sys.stderr)
        return 1
    catalog = load_catalog()
    poem = find_poem(catalog, sys.argv[1])
    client = ElevenLabs(api_key=api_key)
    align_mix(client, poem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
