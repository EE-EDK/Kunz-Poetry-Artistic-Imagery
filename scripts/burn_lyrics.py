"""Burn poem SRT onto a video (or stills + voice) with ffmpeg.

Usage:
  python scripts/burn_lyrics.py 01
  python scripts/burn_lyrics.py 01 --audio-only
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import paths  # noqa: E402


def find_poem(token: str) -> dict:
    catalog = json.loads(paths.CATALOG.read_text(encoding="utf-8"))
    token = token.strip().lower()
    for poem in catalog["poems"]:
        if poem["folder"].startswith(token.zfill(2) if token.isdigit() else token):
            return poem
        if str(poem["id"]) == token.lstrip("0") or f"{poem['id']:02d}" == token.zfill(2):
            return poem
    raise SystemExit(f"No poem matching {token!r}")


def first_file(folder: Path, suffixes: tuple[str, ...]) -> Path | None:
    if not folder.exists():
        return None
    hits = [
        p for p in folder.iterdir()
        if p.suffix.lower() in suffixes and "-lyrics" not in p.stem.lower()
    ]
    if not hits:
        return None
    # Prefer the latest take (v4 > v3 > FULL) by name, then newest mtime.
    hits.sort(key=lambda p: (p.name.lower(), p.stat().st_mtime), reverse=True)
    return hits[0]


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/burn_lyrics.py NN [--audio-only]", file=sys.stderr)
        return 1
    audio_only = "--audio-only" in sys.argv
    poem = find_poem(sys.argv[1])
    base = paths.POEMS / poem["folder"]
    srt = first_file(base / "timing", (".srt",))
    voice = first_file(base / "audio" / "elevenlabs", (".wav", ".mp3", ".m4a"))
    video = first_file(base / "video", (".mp4", ".mov", ".mkv"))
    if srt is None:
        print(f"No SRT in {base / 'timing'}", file=sys.stderr)
        return 1
    out = base / "video" / f"{poem['folder']}-lyrics.mp4"
    out.parent.mkdir(parents=True, exist_ok=True)

    # ffmpeg subtitles filter needs escaped path; copy SRT next to output to keep it simple.
    local_srt = out.with_suffix(".srt")
    local_srt.write_text(srt.read_text(encoding="utf-8"), encoding="utf-8")
    srt_filter = local_srt.name.replace("\\", "/").replace(":", "\\:")

    if video is not None and not audio_only:
        cmd = [
            paths.FFMPEG, "-y",
            "-i", str(video),
            "-vf", f"subtitles={srt_filter}:force_style='FontName=Arial,FontSize=28,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,Shadow=0,Alignment=2,MarginV=48'",
            "-c:a", "copy",
            str(out.name),
        ]
        cwd = str(out.parent)
    elif voice is not None:
        cmd = [
            paths.FFMPEG, "-y",
            "-f", "lavfi", "-i", "color=c=black:s=1920x1080:r=24",
            "-i", str(voice),
            "-vf", f"subtitles={srt_filter}:force_style='FontName=Georgia,FontSize=36,PrimaryColour=&H00FFFFFF,Outline=2,Alignment=2,MarginV=80'",
            "-shortest",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            str(out.name),
        ]
        cwd = str(out.parent)
    else:
        print("Need a video file or an elevenlabs voice track.", file=sys.stderr)
        return 1

    print(" ".join(cmd))
    result = subprocess.run(cmd, cwd=cwd)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
