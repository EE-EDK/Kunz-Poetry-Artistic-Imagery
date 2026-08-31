"""Trim Garden of Perspective ES downloads to max 30s and file as 01-10."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import paths  # noqa: E402

DOWNLOADS = Path.home() / "Downloads"
DEST = ROOT / "poems" / "05-the-garden-of-perspective" / "audio" / "sfx"
MAX_SEC = 30.0

CUTS = [
    ("ES_Ambience, Birdsong, Birds Chirping, Dawn, Lithuania, Quiet 01 - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-01-birdsong-dawn.wav"),
    ("ES_Birds, Songbird, Chirping, Close, Single 04 - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-02-songbird-chirp.wav"),
    ("ES_Ambience, Alpine, Mountain Valley, Forest Edge, Gentle Wind, Blowing Through Leaves & Branches 01 - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-03-alpine-forest-wind.wav"),
    ("ES_Movement, Insect, Many Bees Humming, Constant, Distant Birds, Light Wind, Mount Somma - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-04-bees-humming.wav"),
    ("ES_Vegetation, Leaves, Leaf, Dry, Rustling 01 - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-05-leaves-rustling.wav"),
    ("ES_Water, Drip, Reverberant Echo, Cave, Cavern - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-06-cave-drip-echo.wav"),
    ("ES_Water, Drip, Cave, Slovenia - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-07-cave-drip.wav"),
    ("ES_Wind, General, Desert, Close To Bushes, Wind Gusts, Twig Branch, Close - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-08-desert-wind-bushes.wav"),
    ("ES_Objects, Tape, Masking Tape, Peel Off Surface - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-09-tape-peel.wav"),
    ("ES_Dirt & Sand, Dust, Debris, Small, Tiny Drop 02 - Epidemic Sound.wav",
     "05-the-garden-of-perspective-es-10-dust-drop.wav"),
]


def probe_duration(path: Path) -> float:
    r = subprocess.run(
        [paths.FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(r.stdout.strip())


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    missing = 0
    for src_name, dest_name in CUTS:
        src = DOWNLOADS / src_name
        dest = DEST / dest_name
        if not src.exists():
            print("MISSING", src_name)
            missing += 1
            continue
        dur = probe_duration(src)
        t = min(MAX_SEC, dur)
        cmd = [paths.FFMPEG, "-y", "-i", str(src), "-t", f"{t:.3f}", "-c", "copy", str(dest)]
        print(f"src {dur:.1f}s -> {t:.1f}s  {dest_name}")
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  wrote {dest.stat().st_size} bytes  {probe_duration(dest):.3f}s")
        try:
            src.unlink()
            print("  removed Downloads original")
        except OSError as exc:
            print(f"  Downloads original left ({exc})")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
