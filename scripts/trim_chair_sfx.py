"""File Downloads ES masters for poem 09. Long beds: voice + 5 s. One-shots: full."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import paths  # noqa: E402

DOWNLOADS = Path.home() / "Downloads"
SFX = ROOT / "poems" / "09-the-chair" / "audio" / "sfx"
VOICE_PLUS_PAD = 122.67 + 5.0

SFX_CUTS = [
    (
        "ES_Ambience, Room Tone, Stairwell 01 - Epidemic Sound.wav",
        "09-the-chair-es-01-stairwell-tone.wav",
        None,
    ),
    (
        "ES_Electricity, Buzz & Hum, Designed, Drone - Epidemic Sound.wav",
        "09-the-chair-es-02-electricity-drone.wav",
        None,
    ),
    (
        "ES_Human, Heartbeat, Designed, Evil Heartbeat, Fat Bass - Epidemic Sound.wav",
        "09-the-chair-es-03-heartbeat-evil.wav",
        None,
    ),
    (
        "ES_Designed, Vocal, Horror Whispers, Binaural, Reverberant, Voices - Epidemic Sound.wav",
        "09-the-chair-es-04-horror-whispers.wav",
        None,
    ),
    (
        "ES_Rocks, Crash & Debris, Falling, Heavy, Dusty - Epidemic Sound.wav",
        "09-the-chair-es-05-rocks-crash.wav",
        None,
    ),
    (
        "ES_Ice, Break, Thin, Crack Under Pressure - Epidemic Sound.wav",
        "09-the-chair-es-06-ice-crack.wav",
        None,
    ),
    (
        "ES_Swooshes, Whoosh, Low, Short 02 - Epidemic Sound.wav",
        "09-the-chair-es-07-whoosh-low.wav",
        None,
    ),
    (
        "ES_Swooshes, Whoosh, Wind, Soft 04 - Epidemic Sound.wav",
        "09-the-chair-es-08-whoosh-wind.wav",
        None,
    ),
    (
        "ES_Magic, Spell, Swell, Mystic, Light Pad, Chime 01 - Epidemic Sound.wav",
        "09-the-chair-es-09-mystic-chime.wav",
        None,
    ),
    (
        "ES_Dark Tunnels - Ethan Sloan.wav",
        "09-the-chair-es-dark-tunnels.wav",
        None,
    ),
    (
        "ES_Time Does Not Matter - Elm Lake.wav",
        "09-the-chair-es-time-does-not-matter.wav",
        VOICE_PLUS_PAD,
    ),
    (
        "ES_Air, Hiss, Thin, Long, Noise - Epidemic Sound.wav",
        "09-the-chair-es-air-hiss-thin.wav",
        None,
    ),
    (
        "ES_Wood, Friction, Creak, Old Wooden Furniture, Short, Dry 03 - Epidemic Sound.wav",
        "09-the-chair-es-wood-creak-dry.wav",
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


def cut_one(src_name: str, dest: Path, cap: float | None) -> bool:
    src = DOWNLOADS / src_name
    if not src.exists():
        print("MISSING", src_name)
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dur = probe_duration(src)
    t = min(float(cap), dur) if cap is not None else dur
    cmd = [paths.FFMPEG, "-y", "-i", str(src), "-t", f"{t:.3f}", "-c", "copy", str(dest)]
    print(f"src {dur:.2f}s -> {t:.2f}s  {dest.name}")
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  wrote {dest.stat().st_size} bytes  {probe_duration(dest):.3f}s")
    try:
        src.unlink()
        print("  removed Downloads original")
    except OSError as exc:
        print(f"  Downloads original left ({exc})")
    return True


def main() -> int:
    missing = 0
    for src_name, dest_name, cap in SFX_CUTS:
        if not cut_one(src_name, SFX / dest_name, cap):
            missing += 1
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
