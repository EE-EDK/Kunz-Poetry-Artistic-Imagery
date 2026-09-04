"""Cut poem-09 SFX to the locked cue table. Reads sfx/ masters (or sfx/alt/)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import paths  # noqa: E402

SFX = ROOT / "poems" / "09-the-chair" / "audio" / "sfx"
ALT = SFX / "alt"


def src_path(name: str) -> Path:
    here = SFX / name
    return here if here.exists() else ALT / name


# dest, src name, start, dur, copy
CUTS = [
    (
        "09-the-chair-es-01-room-0m00-2m05.wav",
        "09-the-chair-es-01-stairwell-tone.wav",
        0.0,
        None,
        True,
    ),
    (
        "09-the-chair-es-02-rumble-0m05-0m12.wav",
        "09-the-chair-es-dark-tunnels.wav",
        0.0,
        6.78,
        False,
    ),
    (
        "09-the-chair-es-03-hums-0m12-0m22.wav",
        "09-the-chair-es-02-electricity-drone.wav",
        0.0,
        10.26,
        False,
    ),
    (
        "09-the-chair-es-04-collapse-0m39-0m42.wav",
        "09-the-chair-es-07-whoosh-low.wav",
        0.0,
        None,
        True,
    ),
    (
        "09-the-chair-es-05-cycle-0m43-0m53.wav",
        "09-the-chair-es-03-heartbeat-evil.wav",
        0.0,
        10.06,
        False,
    ),
    (
        "09-the-chair-es-06-vision-0m55-1m02.wav",
        "09-the-chair-es-09-mystic-chime.wav",
        0.0,
        6.90,
        False,
    ),
    (
        "09-the-chair-es-07-layer-1m03-1m20.wav",
        "09-the-chair-es-time-does-not-matter.wav",
        0.0,
        16.26,
        False,
    ),
    (
        "09-the-chair-es-08-whisper-1m21-1m26.wav",
        "09-the-chair-es-04-horror-whispers.wav",
        0.0,
        4.78,
        False,
    ),
    (
        "09-the-chair-es-09-crack-1m28-1m31.wav",
        "09-the-chair-es-06-ice-crack.wav",
        0.0,
        None,
        True,
    ),
    (
        "09-the-chair-es-10-open-1m33-1m39.wav",
        "09-the-chair-es-08-whoosh-wind.wav",
        0.0,
        None,
        True,
    ),
    (
        "09-the-chair-es-11-bloom-1m39-1m47.wav",
        "09-the-chair-es-09-mystic-chime.wav",
        0.0,
        7.32,
        False,
    ),
    (
        "09-the-chair-es-12-rot-0m24-0m37.wav",
        "09-the-chair-es-air-hiss-thin.wav",
        0.0,
        13.30,
        False,
    ),
    (
        "09-the-chair-es-13-chair-0m00-0m04.wav",
        "09-the-chair-es-wood-creak-dry.wav",
        0.0,
        None,
        True,
    ),
]

OLD_SFX = [
    "09-the-chair-es-01-stairwell-tone.wav",
    "09-the-chair-es-02-electricity-drone.wav",
    "09-the-chair-es-03-heartbeat-evil.wav",
    "09-the-chair-es-04-horror-whispers.wav",
    "09-the-chair-es-05-rocks-crash.wav",
    "09-the-chair-es-06-ice-crack.wav",
    "09-the-chair-es-07-whoosh-low.wav",
    "09-the-chair-es-08-whoosh-wind.wav",
    "09-the-chair-es-09-mystic-chime.wav",
    "09-the-chair-es-air-hiss-thin.wav",
    "09-the-chair-es-wood-creak-dry.wav",
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
    ALT.mkdir(parents=True, exist_ok=True)
    missing = 0
    for dest_name, src_name, start, dur, copy in CUTS:
        dest = SFX / dest_name
        src = src_path(src_name)
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
    keep = {c[0] for c in CUTS}
    for name in OLD_SFX:
        src = SFX / name
        if src.exists() and name not in keep:
            dest = ALT / name
            if dest.exists():
                dest.unlink()
            src.rename(dest)
            print("alt", name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
