# The Forest Disease — shot manifest (beats-first)

**This file supersedes `timing/TIMING-MAP-v3.md` and the shot table in
`HAND_OFF_LOCAL_GROK_CLI.md`.** Those two disagreed with each other and with
the keep folder, which is why every stitch attempt guessed differently.

One truth now lives in two places that cannot drift apart:

| Where | What it holds |
|---|---|
| `scripts/assemble_beats.py` → `SEQUENCE` | the executable manifest |
| this file | the same table for humans, plus why each window is what it is |

Picture lock **177.00 s** · 1280×720 · 24 fps · cross-fade **2.0 s** ·
audio `audio/mix/11-the-forest-disease-MIX-v2.wav` · subs `timing/lyrics.ass`

## Measured audio beats

Not taken from the map. Cross-correlated from the section cuts in
`audio/cuts/*.zip` against the mix, so these are where the sounds actually are.

| Clock | Event |
|---|---|
| 0:00.4 | whoosh |
| 0:24.6 | leaf tick |
| 0:50.0 | raven call |
| 0:52.0 | splash |
| 0:52.5 | bear growl |
| 1:39.3 | stick snap |
| 1:46.0 | wood squeak |

**The constraint that shapes the whole film:** the raven call and the splash
are 2.0 s apart. That is the fault in the v3 and v5 cuts, where the pond is
still on screen when you hear the bear enter the water. Shot 6 therefore hands
over at 0:50.5, so the dissolve runs 0:50.5–0:52.5: the raven calls on a clean
pond at 0:50.0, the bear is three quarters in at the splash on 0:52.0, and it
is clean on the growl at 0:52.5.

## Sequence

Every source is used **exactly once**, forward, from t=0. Twelve of the twenty
run their full length; eight are trimmed at the tail to land a beat.

| # | gen slot | source (video/videoset-keep) | clean on screen | out at | film s | file s | source s | state |
|---|---|---|---|---|---|---|---|---|
| 1 | s01 | 01-enter-aerial-snags | 0:00–0:08 | 0:08 | 8.0 | 10.0 | 10.04 | full |
| 2 | s02 | 02-s1-descent | 0:10–0:21 | 0:21 | 13.0 | 15.0 | 15.04 | full |
| 3 | s03 | 03-hoverA-moss-vault | 0:23–0:34 | 0:34 | 13.0 | 15.0 | 15.04 | full |
| 4 | s04 | 03c-hoverA-moss-goldwater | 0:36–0:40 | 0:40 | 6.0 | 8.0 | 10.04 | −2.0 |
| 5 | s05 | 04-s2-fires-log-rays | 0:42–0:45 | 0:45 | 5.0 | 7.0 | 10.04 | −3.0 |
| 6 | s06 | 04b-hoverB-raven-pond | 0:47–0:50.5 | 0:50.5 | 5.5 | 7.5 | 10.04 | −2.5 |
| 7 | s07 | 05-hoverB-bear-gold-pool | 0:52.5–1:03.5 | 1:03.5 | 13.0 | 15.0 | 15.04 | full |
| 8 | s08 | 05c-river-clean | 1:05.5–1:15 | 1:15 | 11.5 | 13.5 | 15.04 | −1.5 |
| 9 | s09 | 06-wind-valley-mist | 1:17–1:23 | 1:23 | 8.0 | 10.0 | 10.04 | full |
| 10 | s10 | 06b-wind-valley-river | 1:25–1:31 | 1:31 | 8.0 | 10.0 | 10.04 | full |
| 11 | s11 | 06c-spare-valley-clear | 1:33–1:36 | 1:36 | 5.0 | 7.0 | 10.04 | −3.0 |
| 12 | s12 | 07-bridge-approach | 1:38–1:40 | 1:40 | 4.0 | 6.0 | 10.04 | −4.0 |
| 13 | s13 | 08-bridge-under-arch | 1:42–1:53 | 1:53 | 13.0 | 15.0 | 15.04 | full |
| 14 | s14 | grok-c7714015 (elk bridge) | 1:55–2:06 | 2:06 | 13.0 | 15.0 | 15.04 | full |
| 15 | s15 | 03b-hoverA-moss-lighter | 2:08–2:10 | 2:10 | 4.0 | 6.0 | 10.04 | −4.0 |
| 16 | s16 | 10-dawn-gold | 2:12–2:23 | 2:23 | 13.0 | 15.0 | 15.04 | full |
| 17 | s17 | 09-hole-fog-trees | 2:25–2:31 | 2:31 | 8.0 | 10.0 | 10.04 | full |
| 18 | s18 | 00-spare-aerial-fog | 2:33–2:39 | 2:39 | 8.0 | 10.0 | 10.04 | full |
| 19 | s19 | 00-spare-aerial-ridge | 2:41–2:47 | 2:47 | 8.0 | 10.0 | 10.04 | full |
| 20 | s20 | 12-stare | 2:49–2:57 | 2:57 | 10.0 | 10.0 | 15.04 | −5.0 |

**How to read this.** `out at` is the moment the dissolve to the next shot
*begins*, which is what ffmpeg's xfade offset actually means. A shot is fully
clean from the previous shot's out plus 2.0 s until its own out; the 2.0 s
after its out are shared with the next shot. Getting this backwards is what
put the splash on the raven pond in the first build.

`film s` is screen time. `file s` is film + 2.0 s of cross-fade pad, except
the last shot which needs none. Sum of file lengths is 215.0 s; nineteen
cross-fades remove 38.0 s; picture lands at 177.00 s.

### Why the trimmed eight are trimmed

- **4 moss-goldwater** — hands over at 0:40 so the log-rays are clean by 0:42.
- **5 log-rays** — rays clean 0:42–0:45 under "blazing with fires".
- **6 raven** — clean 0:47–0:50.5 so the call at 0:50.0 plays on a clean pond
  and the dissolve to the bear runs 0:50.5–0:52.5.
- **8 river-clean** — hover C closes on 1:15 for "the wandering wind".
- **11 valley-clear** — closes the wind hold on 1:36.
- **12 bridge** — S4a is four seconds; the stick snap is at 1:39.3.
- **15 moss-lighter** — the Hole's darkest four seconds before dawn at 2:10.
- **20 stare** — the film ends at 2:57; the clip is longer than the ending.

### Not used

- `05b-river-HAS-FIGURE` — the map bans a body in the water. Reflection only.
- Two rejected generations, `68afeb32` (cartoon gold) and `2287fe0b`
  (hallucinated river), remain rejected.

## Elk bridge, shot 14

Also fixes a story hole. Shots 12 and 13 are the bridge and the falls from
below; shot 14 is the same bridge seen from the far side, so the camera has
drifted out from under the arch and looked back. The Hole window is scored to
a distant waterfall rumour and lake lap, which a still pond could not justify
and falls in frame can.

## Rule change recorded

The map allowed animals only at the raven pond and the bear pool. Shot 14 adds
a third: an elk standing on the bridge with a raven crossing, at 1:53–2:06.
Owner decision, 2026-09-07. It replaces a return to the dark moss water, which
would have been the third use of footage already spent on shot 3.

## Guards in the assembler

- A source used twice fails the run.
- `reverse`, `loop`, `tpad`, `setpts` in any filtergraph fails the run.
- A source shorter than its window is a hard error, never padded.
- Picture more than 0.25 s off the lock fails the run.

## Rebuild

```
python scripts/assemble_beats.py
```

Reads `gen/s01.mp4` … `gen/s20.mp4`. To swap a shot, drop a new clip over that
slot and rerun; nothing else changes. Output is `out/11-the-forest-disease-v4.mp4`
plus `out/beat-check/` frames at every beat clock and
`out/assemble-beats-report.json`.
