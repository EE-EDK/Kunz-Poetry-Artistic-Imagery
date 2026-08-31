"""Trim Downloads ES masters to cue length + 5s for poem 04."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import paths  # noqa: E402

DOWNLOADS = Path.home() / "Downloads"
DEST = ROOT / "poems" / "04-seeds-of-memory-from-death" / "audio" / "sfx"
PAD = 5.0

# cue_end - cue_start + PAD
CUTS = [
    {
        "src": "ES_Ambience, Insect, Cicada, Crickets, Summer, Day, Australia 01 - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-cicadas-summer-haze.wav",
        "cue": "0:00-0:12",
        "seconds": 12 + PAD,
        "idea": "Late-summer heat haze / cicadas",
    },
    {
        "src": "ES_Wind, Designed, Whispering Winds, Drones, Synthesized Nightmare - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-cooling-wind.wav",
        "cue": "0:07-0:12",
        "seconds": 5 + PAD,
        "idea": "Cooling wind, one pass",
    },
    {
        "src": "ES_Ice, Break, Walk On Thin Ice, Pressing, Crackle - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-frost-ice.wav",
        "cue": "0:15-0:20",
        "seconds": 5 + PAD,
        "idea": "Frost air / facial cold",
    },
    {
        "src": "ES_Footsteps, Human, Forest, Leaves, Branches, Dry - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-dry-leaves-underfoot.wav",
        "cue": "0:18-0:32",
        "seconds": 14 + PAD,
        "idea": "Dry leaves underfoot",
    },
    {
        "src": "ES_Rain, General, Tropical, Moderate Monsoon Rain, Balcony - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-rain.wav",
        "cue": "0:30-0:34",
        "seconds": 4 + PAD,
        "idea": "Rain (wet)",
    },
    {
        "src": "ES_Wind, Tonal, Wind At Bullet, Light Whistling, Light Wind On Bushes, Desert 01 - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-dry-hush.wav",
        "cue": "0:34-0:36",
        "seconds": 2 + PAD,
        "idea": "Dry hush",
    },
    {
        "src": "ES_Fire, Burning, Bonfire, Moderate Size, Close, Crackling - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-crackle.wav",
        "cue": "0:36-0:40",
        "seconds": 4 + PAD,
        "idea": "Far crackle (set ablaze)",
    },
    {
        "src": "ES_Bells, Large, Church, Distant, Reverberant, Distant Traffic, Distant Cowbells, Light Wind, Foliage 02 - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-distant-bells.wav",
        "cue": "0:38-0:46",
        "seconds": 8 + PAD,
        "idea": "Distant bells / faint organ",
    },
    {
        "src": "ES_Ambience, Insect, Insect Chorus, Texture, Night - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-night-insects.wav",
        "cue": "0:45-0:54",
        "seconds": 9 + PAD,
        "idea": "Night hush / insects cut off",
    },
    {
        "src": "ES_Ambience, Forest, Wind In Trees, Birds, Leaves Fall To Ground, Autumn - Epidemic Sound.wav",
        "dest": "04-seeds-of-memory-es-autumn-wind-leaf.wav",
        "cue": "0:52-1:04",
        "seconds": 12 + PAD,
        "idea": "Autumn wind + one leaf settling + hold",
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
    missing = []
    for cut in CUTS:
        src = DOWNLOADS / cut["src"]
        if not src.exists():
            missing.append(cut["src"])
            print(f"MISSING {cut['src']}")
            continue
        dest = DEST / cut["dest"]
        dur = probe_duration(src)
        t = min(cut["seconds"], dur)
        cmd = [
            paths.FFMPEG, "-y", "-i", str(src),
            "-t", f"{t:.3f}",
            "-c", "copy",
            str(dest),
        ]
        print(f"trim {cut['cue']} +{PAD:.0f}s -> {t:.1f}s  {cut['dest']}  (src {dur:.1f}s)")
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        out_dur = probe_duration(dest)
        print(f"  wrote {dest.name} {dest.stat().st_size} bytes  {out_dur:.3f}s")
        try:
            src.unlink()
            print("  removed Downloads original")
        except OSError as exc:
            print(f"  Downloads original left ({exc})")
    if missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
