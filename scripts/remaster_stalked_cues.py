"""Cut all eight poem-07 ES takes to the locked cue table. Reads sfx/alt/ masters."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import paths  # noqa: E402

SFX = ROOT / "poems" / "07-stalked-in-realms" / "audio" / "sfx"
ALT = SFX / "alt"

# dest, alt src, start, dur, copy
CUTS = [
    (
        "07-stalked-in-realms-es-01-room-0m00-0m43.wav",
        "07-stalked-in-realms-es-01-hotel-room-tone.wav",
        0.0,
        None,
        True,
    ),
    (
        "07-stalked-in-realms-es-02-sheet-0m00-0m03.wav",
        "07-stalked-in-realms-es-03-bed-sheet-cotton.wav",
        0.0,
        2.05,
        False,
    ),
    (
        "07-stalked-in-realms-es-03-breath-0m19-0m21.wav",
        "07-stalked-in-realms-es-07-gasp-female-01.wav",
        2.18,
        1.01,
        False,
    ),
    (
        "07-stalked-in-realms-es-04-shimmer-0m10-0m19.wav",
        "07-stalked-in-realms-es-06-shimmer-crystal.wav",
        0.0,
        8.30,
        False,
    ),
    (
        "07-stalked-in-realms-es-05-flinch-creak-0m19-0m21.wav",
        "07-stalked-in-realms-es-05-bed-creak.wav",
        0.0,
        None,
        True,
    ),
    (
        "07-stalked-in-realms-es-06-flinch-inhale-0m19-0m21.wav",
        "07-stalked-in-realms-es-08-gasp-female-03.wav",
        1.18,
        0.40,
        False,
    ),
    (
        "07-stalked-in-realms-es-07-hush-0m21-0m26.wav",
        "07-stalked-in-realms-es-02-empty-office-tone.wav",
        0.0,
        5.60,
        False,
    ),
    (
        "07-stalked-in-realms-es-08-settle-0m41-0m43.wav",
        "07-stalked-in-realms-es-04-bed-sit-soft.wav",
        0.0,
        1.70,
        False,
    ),
]

KEEP = {c[0] for c in CUTS}


def probe_duration(path: Path) -> float:
    r = subprocess.run(
        [paths.FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(r.stdout.strip())


def main() -> int:
    missing = 0
    for dest_name, src_name, start, dur, copy in CUTS:
        src = ALT / src_name
        dest = SFX / dest_name
        if not src.exists():
            print("MISSING", src_name)
            missing += 1
            continue
        cmd = [paths.FFMPEG, "-y", "-i", str(src)]
        if start:
            cmd += ["-ss", f"{start:.3f}"]
        if dur is not None:
            cmd += ["-t", f"{dur:.3f}"]
        cmd += ["-c", "copy"] if copy else ["-c:a", "pcm_s24le"]
        cmd += [str(dest)]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"wrote {dest_name}  {probe_duration(dest):.3f}s  {dest.stat().st_size} bytes")
    if missing:
        return 1
    for wav in SFX.glob("*.wav"):
        if wav.name not in KEEP:
            wav.unlink()
            print("removed", wav.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
