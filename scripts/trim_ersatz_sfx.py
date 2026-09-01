"""Trim Downloads ES masters for poem 06 (cue length + 5 s, HUM through tail)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import paths  # noqa: E402

DOWNLOADS = Path.home() / "Downloads"
DEST = ROOT / "poems" / "06-ersatz-machinations" / "audio" / "sfx"
PAD = 5.0

CUTS = [
    {
        "src": "ES_Ambience, Room Tone, Medium Sized Server Room - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-01-hum-0m00-1m33.wav",
        "seconds": 93.0 + PAD,
    },
    {
        "src": "ES_Robots, Movement, Startup, Large Robot - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-02-robot-on-0m00-0m15.wav",
        "seconds": 14.8 + PAD,
    },
    {
        "src": "ES_Scifi, Mechanism, Micro Bot, Robot, Servo Movement, Short, Variations 02 - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-03-servo-0m00-0m02.wav",
        "seconds": 2.22 + PAD,
    },
    {
        "src": "ES_Computers, Hard Drive, Vintage, Commodore, 64, 5, 25 Floppy Read - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-04-disc-0m03-0m06.wav",
        "seconds": 3.0 + PAD,
    },
    {
        "src": "ES_Air, Hiss, Steam Release, Machinery, Medium 02 - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-05-hiss-0m10-0m13.wav",
        "seconds": 3.3 + PAD,
    },
    {
        "src": "ES_User Interface, Data, Processing, Straight Telemetry, Garble, Data Readout 01 - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-06-swarm-0m26-0m34.wav",
        "seconds": 7.9 + PAD,
    },
    {
        "src": "ES_Electricity, Sparks, Short Complex Sparks, Designed 06 - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-07-spark-0m37-0m40.wav",
        "seconds": 2.6 + PAD,
    },
    {
        "src": "ES_Scifi, Mechanism, Micro Bot, Robot, Servo Movement, Complex, Short - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-08-joint-0m63-0m66.wav",
        "seconds": 2.3 + PAD,
    },
    {
        "src": "ES_Weapons, Armor, Medieval, Knight, Extra Heavy Metal, Movement, Walk, Distant - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-09-floor-0m84-0m92.wav",
        "seconds": 7.8 + PAD,
    },
    {
        "src": "ES_Vehicles, Military, Tank, T-72, Controls, Circuit Breaker - Epidemic Sound.wav",
        "dest": "06-ersatz-machinations-es-10-lock-0m93.wav",
        "seconds": 0.5 + PAD,
    },
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
    for cut in CUTS:
        src = DOWNLOADS / cut["src"]
        dest = DEST / cut["dest"]
        if not src.exists():
            print("MISSING", cut["src"])
            missing += 1
            continue
        dur = probe_duration(src)
        t = min(float(cut["seconds"]), dur)
        cmd = [paths.FFMPEG, "-y", "-i", str(src), "-t", f"{t:.3f}", "-c", "copy", str(dest)]
        print(f"src {dur:.2f}s -> {t:.2f}s  {cut['dest']}")
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
