> **SUPERSEDED 2026-09-08.** The governing shot table is now
> [`SHOTS-MANIFEST.md`](../SHOTS-MANIFEST.md), executed by
> `scripts/assemble_beats.py`. This v3 plan named 24 clips that were never
> all downloaded, and its 10 s uniform grid put the raven pond on screen
> during the 0:52 splash. Kept as a historical record.

# The Forest Disease — TIMING-MAP v3 (reassessed)

**Master clock:** MIX-v2 = **177.00 s** (2:57)  
**Rules:** solid continuous photoreal only · no freeze · no reverse/ping-pong · no tpad · soft **2.5 s** xfades · ASS from mix words · mix untouched

## Why v3
v2 solid order was scrambled (duplicate wide aerials, contemplative clip twice, soft-hills mid-film, river/wind out of poem order).  
v3 re-orders 24 unique dynamic PNW clips to the reverse-build voice windows.

## Assembly math
- 24 × **10.00 s** solid continuous clips  
- soft **2.5 s** xfade between each  
- raw picture = `24×10 − 23×2.5` = **182.50 s**  
- trim tail **5.50 s** → **177.00 s** locked to MIX-v2  
- group stitch: 4 × 6 clips → each group **47.50 s**, then 3 × 2.5 s xfades between groups → 182.50 s

## Voice windows (mix-aligned, unchanged)

| Stem | Mix clock | Last word | Picture intent |
|------|-----------|-----------|----------------|
| Open | 0:00–0:18 | (no voice) | Wide establish, soft approach |
| **S1** | 0:18.06–0:27.00 | languish | High canopy intimacy / anguish |
| Hover A | 0:27–0:40 | — | Descent + wind builds |
| **S2** | 0:40.00–0:47.59 | fires | Close trunks, heavy wind |
| Hover B | 0:48–1:02 | — | River valley reveal |
| **S3a** | 1:02–1:04.36 | lie. | Denser pocket (branches lie) |
| Hover C | 1:05–1:15 | — | Approach shadow |
| **S3b** | 1:15–1:20.56 | wind | Heavy wind aerial |
| Wind hold | 1:21–1:36 | — | Long wind/music hold |
| **S4a** | 1:36–1:39.94 | was, | River valley classic |
| Hover D | 1:40–1:53 | — | Lower river approach |
| **S4b** | 1:53–1:57.64 | cause, | Valley edge |
| Hole | 1:58–2:10 | — | Deep fog void |
| **S5** | 2:10–2:18.88 | dawn, | Rise out of fog |
| Dawn hold | 2:19–2:32 | — | High pull-back |
| **S6a** | 2:32–2:35.66 | seen— | Wide aerial |
| Hover E | 2:36–2:44 | — | Mountains overview |
| **S6b** | 2:44–2:48.18 | breeze. | Contemplative soft wind |
| Stare | 2:48–2:57 | — | Final high stare |

## Picture sequence (24 unique solid continuous photoreal)

Film start ≈ clip_index × 7.5 s (because 10 − 2.5 xfade).  
After final trim of 5.5 s from 182.5 s raw, last frame lands at 177.00.

| # | Film start | End≈ (pre-trim) | Block | Role | Source asset (short) |
|---|------------|-----------------|-------|------|----------------------|
| 0 | 0:00.0 | 0:10.0 | Enter | Wide aerial fir canopy overview | 466e437e |
| 1 | 0:07.5 | 0:17.5 | Enter | Elevated aerial mist ridges | fca43ebc |
| 2 | 0:15.0 | 0:25.0 | Enter→S1 | Soft morning hills / mist | c8f4eb01 |
| 3 | 0:22.5 | 0:32.5 | **S1** | High canopy float (anguish) | b044f7bf |
| 4 | 0:30.0 | 0:40.0 | Hover A | Descent corridor + strong wind | 833d0066 |
| 5 | 0:37.5 | 0:47.5 | Hover A / S2 | Mid-canopy + wind | c7fbd6ee |
| 6 | 0:45.0 | 0:55.0 | **S2** | Close trunks + heavy wind (fires) | d91ddfed |
| 7 | 0:52.5 | 1:02.5 | Hover B | River valley + wind | 9b908d92 |
| 8 | 1:00.0 | 1:10.0 | Hover B / S3a | River elevated float | a36256af |
| 9 | 1:07.5 | 1:17.5 | Hover C / S3a | Denser pocket + wind | d27fda64 |
| 10 | 1:15.0 | 1:25.0 | **S3b** | Heavy wind aerial (wandering wind) | bb026aca |
| 11 | 1:22.5 | 1:32.5 | Wind hold | Lateral canopy float | 62940145 |
| 12 | 1:30.0 | 1:40.0 | Wind hold | Gorge approach | 45856292 |
| 13 | 1:37.5 | 1:47.5 | **S4a** | River valley classic (message) | 4afa1909 |
| 14 | 1:45.0 | 1:55.0 | Hover D | Toward river lower | 1ffd53be |
| 15 | 1:52.5 | 2:02.5 | **S4b** | Valley edge (words / silence) | d816a2ec |
| 16 | 2:00.0 | 2:10.0 | Hole | Hillside mist | cf5ae517 |
| 17 | 2:07.5 | 2:17.5 | Hole / S5 | Deep canopy fog | 17cc2a4e |
| 18 | 2:15.0 | 2:25.0 | **S5** | Rise out of fog (dawn) | c6bc172c |
| 19 | 2:22.5 | 2:32.5 | Dawn hold | High pull-back | 39417b4f |
| 20 | 2:30.0 | 2:40.0 | Dawn / S6a | Wide aerial | c28663e3 |
| 21 | 2:37.5 | 2:47.5 | Hover E | Mountains overview | 6756b943 |
| 22 | 2:45.0 | 2:55.0 | **S6** | Contemplative soft wind | ffea5969 |
| 23 | 2:52.5 | 3:02.5 | Stare | High stare (trim ends 2:57) | 8794adcf |

## Subtitle ASS (mix-aligned, unchanged)
Source: `11-forest/lyrics.ass` — poem text exact, times locked to MIX-v2 words.

## Deliverable
`11-the-forest-disease-v3.mp4` — 1280×720, 177.00 s, MIX-v2 audio, ASS burned, solid continuous motion only.
