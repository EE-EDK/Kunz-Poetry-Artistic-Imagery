"""Beats-first assemble of poem 11 "The Forest Disease" to MIX-v2 (177.00 s).

Rules enforced by this script, not by convention:

  * every source is used EXACTLY ONCE, forward, from t=0
  * no reverse, loop, tpad, or setpts stretch -- the filter guard rejects them
  * a source shorter than its shot window is a hard error, never padded
  * shot windows are chosen so the measured audio beats land on picture

Sources are read from poems/11-the-forest-disease/gen/sNN.mp4 in order.

Measured beats in MIX-v2 (cross-correlated against audio/cuts/*.zip):

    0:00.4  whoosh          1:39.3  stick snap
    0:24.6  leaf tick       1:46.0  wood squeak
    0:50.0  raven call      voice windows per timing/lyrics.ass
    0:52.0  splash
    0:52.5  bear growl

The raven and the bear are 2.0 s apart, so the raven shot hands over at
0:50.5 and the bear dissolves in underneath the splash.

CROSS-FADE SEMANTICS, the thing that is easy to get wrong: a shot's film
seconds run up to the moment its dissolve BEGINS, not to the moment the next
shot is fully on. ffmpeg's xfade offset is the start of the dissolve. So a
shot is fully clean from (previous out + X) to its own out, and the X seconds
after its out are shared with the next shot. Windows below are set with that
in mind -- the bear's out is 0:50.5 + 13.0, and it is fully on at 0:52.5.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POEM = ROOT / "poems" / "11-the-forest-disease"
GEN = POEM / "gen"
SHOTS = POEM / "shots_beats"
BATCHES = POEM / "batches_beats"
OUT = POEM / "out"
TMP = SHOTS / "_parts"

FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"

X = 2.0
W, H, FPS = 1280, 720, 24
PICTURE_LOCK = 177.0
MASTER_NAME = "11-the-forest-disease-v4.mp4"

VF_NORM = (
    "scale=%d:%d:force_original_aspect_ratio=increase,"
    "crop=%d:%d,setsar=1,fps=%d,format=yuv420p" % (W, H, W, H, FPS)
)

BANNED = ("reverse", "loop", "tpad", "setpts", "boomerang")

# (gen slot, film seconds, tag, why this window)
SEQUENCE = [
    ("s01", 8.0, "enter", "open on aerial snags; whoosh 0:00.4"),
    ("s02", 13.0, "descent", "S1 voice from 0:18.06"),
    ("s03", 13.0, "moss-vault", "hover A; leaf tick 0:24.6"),
    ("s04", 6.0, "moss-goldwater", "gold builds toward 'fires'"),
    ("s05", 5.0, "log-rays", "rays clean 0:42-0:45 under 'blazing with fires'"),
    ("s06", 5.5, "raven", "raven clean 0:47-0:50.5; call 0:50.0; dissolve out on 0:50.5"),
    ("s07", 13.0, "bear", "bear 75% at splash 0:52.0, full on growl 0:52.5"),
    ("s08", 11.5, "river-clean", "hover C; water only, no body"),
    ("s09", 8.0, "wind-mist", "S3b 'wandering wind' 1:15-1:20.6"),
    ("s10", 8.0, "wind-river", "wind hold"),
    ("s11", 5.0, "valley-clear", "wind hold out"),
    ("s12", 4.0, "bridge", "S4a 1:36-1:39.9; stick snap 1:39.3"),
    ("s13", 13.0, "under-arch", "hover D; wood squeak 1:46.0"),
    ("s14", 13.0, "elk-bridge", "S4b 1:53-1:57.6 then the Hole"),
    ("s15", 4.0, "moss-lighter", "Hole tail, darkest point"),
    ("s16", 13.0, "dawn-gold", "S5 'meaning of dawn' 2:10-2:18.9"),
    ("s17", 8.0, "hole-fog-trees", "dawn hold"),
    ("s18", 8.0, "aerial-fog", "S6a 'nothing is seen' 2:32-2:35.7"),
    ("s19", 8.0, "aerial-ridge", "hover E, forest looks back"),
    ("s20", 10.0, "stare", "S6b 'stares at the breeze' 2:44-2:48.2; hold to 2:57"),
]

# Beat clocks to spot-check on the finished master.
BEATS = [
    (0.5, "whoosh"), (24.6, "leaf-tick"), (44.0, "fires"),
    (50.0, "raven-call"), (51.5, "dissolve"), (52.0, "splash"),
    (52.5, "growl"), (56.0, "bear"),
    (63.0, "lie"), (70.0, "river"), (78.0, "wind"),
    (99.3, "stick"), (106.0, "squeak"), (116.0, "elk"),
    (128.0, "hole"), (134.0, "dawn"), (153.0, "seen"),
    (166.0, "stare"), (176.5, "end"),
]


def guard(args):
    """Refuse any filtergraph that fakes duration."""
    for a in args:
        low = str(a).lower()
        if low.startswith("-") or "=" not in low and "," not in low:
            continue
        for bad in BANNED:
            if bad in low:
                raise RuntimeError("filter guard: %r appears in %r" % (bad, a))


def run(cmd, log=None):
    guard(cmd)
    print("+", Path(str(cmd[0])).name, " ".join(str(c) for c in cmd[1:6]), "...")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if log:
        log.write_text(proc.stdout + "\n" + proc.stderr, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError("ffmpeg failed (%s):\n%s" % (proc.returncode, (proc.stderr or proc.stdout or "")[-3000:]))


def probe_dur(path):
    out = subprocess.check_output(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nk=1:nw=1", str(path)], text=True)
    return float(out.strip())


def probe_wh(path):
    out = subprocess.check_output(
        [FFPROBE, "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height,r_frame_rate", "-of", "csv=p=0", str(path)], text=True)
    w, h, r = out.strip().split(",")
    return int(w), int(h), r


def norm_trim(src, dest, length):
    """Take `length` seconds from t=0. Never pads, never loops."""
    if dest.exists():
        dest.unlink()
    have = probe_dur(src)
    if have + 0.05 < length:
        raise RuntimeError(
            "SHORT SOURCE %s: have %.3fs, shot needs %.3fs. "
            "Generate more footage or shorten the window -- do not pad."
            % (src.name, have, length))
    run([FFMPEG, "-y", "-i", str(src), "-t", "%.3f" % length,
         "-vf", VF_NORM, "-an", "-c:v", "libx264", "-crf", "18",
         "-preset", "medium", "-r", str(FPS), "-pix_fmt", "yuv420p", str(dest)])
    got = probe_dur(dest)
    if got + 0.12 < length:
        raise RuntimeError("short encode %s: %.3f < %.3f" % (dest.name, got, length))
    return dest


def xfade_chain(clips, dest, x=X):
    if dest.exists():
        dest.unlink()
    if len(clips) == 1:
        shutil.copy2(clips[0], dest)
        return dest
    durs = [probe_dur(c) for c in clips]
    for c, d in zip(clips[:-1], durs[:-1]):
        if d <= x + 0.05:
            raise RuntimeError("clip %s dur %.3f too short to xfade %.2f" % (c.name, d, x))
    inputs = []
    for c in clips:
        inputs += ["-i", str(c)]
    filters, acc, offsets = [], 0.0, []
    for i, d in enumerate(durs[:-1]):
        acc += d
        offsets.append(acc - x * (i + 1))
    for i, off in enumerate(offsets):
        left = "[0:v]" if i == 0 else "[v%d]" % (i - 1)
        out = "[v%d]" % i if i < len(offsets) - 1 else "[vout]"
        filters.append("%s[%d:v]xfade=transition=fade:duration=%.3f:offset=%.4f%s"
                       % (left, i + 1, x, off, out))
    run([FFMPEG, "-y", *inputs, "-filter_complex", ";".join(filters),
         "-map", "[vout]", "-an", "-c:v", "libx264", "-crf", "18",
         "-preset", "medium", "-r", str(FPS), "-pix_fmt", "yuv420p", str(dest)])
    return dest


def main():
    films = [s[1] for s in SEQUENCE]
    if abs(sum(films) - PICTURE_LOCK) > 0.01:
        raise SystemExit("film sum %.2f != %.2f" % (sum(films), PICTURE_LOCK))

    slots = [s[0] for s in SEQUENCE]
    if len(set(slots)) != len(slots):
        raise SystemExit("a source is used more than once: %s" % slots)

    for d in (SHOTS, BATCHES, OUT, TMP):
        d.mkdir(parents=True, exist_ok=True)

    n = len(SEQUENCE)
    file_lens = [f + X for f in films[:-1]] + [films[-1]]

    shot_files = []
    for i, ((slot, film, tag, why), flen) in enumerate(zip(SEQUENCE, file_lens), start=1):
        src = GEN / ("%s.mp4" % slot)
        if not src.is_file():
            raise SystemExit("missing source %s" % src)
        dest = SHOTS / ("b%02d-%s.mp4" % (i, tag))
        norm_trim(src, dest, flen)
        have = probe_dur(src)
        whole = "FULL" if have - flen < 0.10 else "trim -%.2fs" % (have - flen)
        print("  %02d %-16s film %5.1fs  file %5.1fs  src %5.2fs  %s" % (i, tag, film, flen, have, whole))
        shot_files.append(dest)

    a = xfade_chain(shot_files[0:7], BATCHES / "A.mp4")
    b = xfade_chain(shot_files[7:14], BATCHES / "B.mp4")
    c = xfade_chain(shot_files[14:20], BATCHES / "C.mp4")
    for name, p in (("A", a), ("B", b), ("C", c)):
        print("batch %s %.3fs" % (name, probe_dur(p)))
    ab = xfade_chain([a, b], BATCHES / "AB.mp4")
    picture = xfade_chain([ab, c], BATCHES / "picture.mp4")
    pdur = probe_dur(picture)
    print("picture %.3fs" % pdur)
    if abs(pdur - PICTURE_LOCK) > 0.25:
        raise SystemExit("picture %.3f != %.2f" % (pdur, PICTURE_LOCK))

    mix = POEM / "audio" / "mix" / "11-the-forest-disease-MIX-v2.wav"
    ass = POEM / "timing" / "lyrics.ass"
    if not mix.is_file():
        raise SystemExit("missing %s" % mix)
    master = OUT / MASTER_NAME

    cmd = [FFMPEG, "-y", "-i", str(picture), "-i", str(mix), "-t", "%.2f" % PICTURE_LOCK]
    if ass.is_file():
        cmd += ["-vf", "ass='%s'" % ass.resolve().as_posix().replace(":", "\\:")]
        print("burning", ass.name)
    cmd += ["-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-shortest", str(master)]
    run(cmd, OUT / "mux-v4.log")

    check = OUT / "beat-check"
    check.mkdir(exist_ok=True)
    for t, name in BEATS:
        run([FFMPEG, "-y", "-ss", "%.2f" % t, "-i", str(master), "-frames:v", "1",
             str(check / ("t%06.1f-%s.jpg" % (t, name)))])

    w, h, r = probe_wh(master)
    md = probe_dur(master)
    report = {
        "master": str(master),
        "duration_s": md,
        "size_bytes": master.stat().st_size,
        "width": w, "height": h, "fps": r,
        "xfade_s": X,
        "sources_used": len(SEQUENCE),
        "sources_full_length": sum(
            1 for (slot, *_), fl in zip(SEQUENCE, file_lens)
            if probe_dur(GEN / ("%s.mp4" % slot)) - fl < 0.10),
        "shots": [
            {"n": i, "slot": slot, "tag": tag, "film_in": round(sum(films[:i - 1]), 2),
             "film_out": round(sum(films[:i]), 2), "film_s": film,
             "file_s": fl, "src_s": round(probe_dur(GEN / ("%s.mp4" % slot)), 3), "why": why}
            for i, ((slot, film, tag, why), fl) in enumerate(zip(SEQUENCE, file_lens), start=1)
        ],
        "beats_checked": [{"t": t, "name": nm} for t, nm in BEATS],
    }
    (OUT / "assemble-beats-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("MASTER %s  %.3fs  %dx%d @ %s  %s B" % (master, md, w, h, r, format(master.stat().st_size, ",")))
    print("full-length sources: %d of %d" % (report["sources_full_length"], len(SEQUENCE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
