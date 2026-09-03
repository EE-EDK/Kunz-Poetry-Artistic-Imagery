"""Trim Downloads ES masters for poem 07. Long beds: voice + 5 s. One-shots: full."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import paths  # noqa: E402

DOWNLOADS = Path.home() / "Downloads"
DEST = ROOT / "poems" / "07-stalked-in-realms" / "audio" / "sfx"
VOICE_PLUS_PAD = 42.92 + 5.0

CUTS = [
    (
        "ES_Ambience, Room Tone, Quiet Hotel Room, Morning - Epidemic Sound.wav",
        "07-stalked-in-realms-es-01-hotel-room-tone.wav",
        VOICE_PLUS_PAD,
    ),
    (
        "ES_Ambience, Room Tone, Empty Office, Deep, Quiet, 2ch - Epidemic Sound.wav",
        "07-stalked-in-realms-es-02-empty-office-tone.wav",
        VOICE_PLUS_PAD,
    ),
    (
        "ES_Cloth, Movement, Bed, Sheet, Cotton 05 - Epidemic Sound.wav",
        "07-stalked-in-realms-es-03-bed-sheet-cotton.wav",
        None,
    ),
    (
        "ES_Objects, Furniture, Bed, Sit Down, Soft - Epidemic Sound.wav",
        "07-stalked-in-realms-es-04-bed-sit-soft.wav",
        None,
    ),
    (
        "ES_Bed, Person Sits On Wooden Frame, Creak 02 - Epidemic Sound.wav",
        "07-stalked-in-realms-es-05-bed-creak.wav",
        None,
    ),
    (
        "ES_Magic, Shimmer, Crystal Sphere, Glassy, Slowly Evolving Tone - Epidemic Sound.wav",
        "07-stalked-in-realms-es-06-shimmer-crystal.wav",
        VOICE_PLUS_PAD,
    ),
    (
        "ES_Human, Breath, Female 01, Gasp, Shocked, Inhale, Variations 02 - Epidemic Sound.wav",
        "07-stalked-in-realms-es-07-gasp-female-01.wav",
        None,
    ),
    (
        "ES_Human, Breath, Female 03, Gasp, Shocked, Inhale, Variations 03 - Epidemic Sound.wav",
        "07-stalked-in-realms-es-08-gasp-female-03.wav",
        None,
    ),
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
    for src_name, dest_name, cap in CUTS:
        src = DOWNLOADS / src_name
        dest = DEST / dest_name
        if not src.exists():
            print("MISSING", src_name)
            missing += 1
            continue
        dur = probe_duration(src)
        t = min(float(cap), dur) if cap is not None else dur
        cmd = [paths.FFMPEG, "-y", "-i", str(src), "-t", f"{t:.3f}", "-c", "copy", str(dest)]
        print(f"src {dur:.2f}s -> {t:.2f}s  {dest_name}")
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
