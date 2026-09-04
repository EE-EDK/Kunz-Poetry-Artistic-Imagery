# The Chair — SFX work instruction

Mix **one track at a time** against the locked voice.

Local stems only (Epidemic license) — not in git.

Stack order: **ROOM**, then CHAIR, RUMBLE, HUMS, then the later one-shots.
Do **not** loop CHAIR, CRACK, or COLLAPSE. Leave the last line dry.

All tokens now have a stem.

## Locked voice

| Item | Value |
|---|---|
| File | `09-the-chair-voice-FINAL.mp3` |
| Length | **122.67 s** |
| First word | “An” **0.10–0.26** |
| Last line | “I am, so it is, so we are.” **1:57.76–2:02.50** |
| Clock | all times below are on this take |

Title is not spoken. Do not slip stems to a different voice render without rebuilding this sheet.

## How to think about it

- **ROOM** is one continuous clip from `0:00` to fade-out at `1:57.76`. Ride the percentages. Do not split it. The stairwell file is **120 s** — long enough; ROOM is already at 0 by then. `2:02.50–2:05.00` is empty air.
- **MUST** is not a new hit. Duck ROOM 5 dB (56%) under “It exists — it must — …”
- **VISION** and **BLOOM** are the same mystic-chime stem at two times. Do not loop it.
- If anything other than voice is audible on “I am, so it is, so we are.”, a clip is too late.

## Stems

| # | File | Length | Token | Use |
|---|---|---|---|---|
| 01 | `09-the-chair-es-01-room-0m00-2m05.wav` | 120.0 s | ROOM | One clip at 0:00. Ride the table. Out by 1:57.76. |
| 13 | `09-the-chair-es-13-chair-0m00-0m04.wav` | 1.05 s | CHAIR | Dry wooden furniture creak, one settle, no loop. 0:00.18–0:03.70. |
| 02 | `09-the-chair-es-02-rumble-0m05-0m12.wav` | 6.78 s | RUMBLE | Dark Tunnels SFX, first 6.78 s. 0:05.30–0:12.08. |
| 03 | `09-the-chair-es-03-hums-0m12-0m22.wav` | 10.26 s | HUMS | Electric drone. 0:12.14–0:22.40. |
| 12 | `09-the-chair-es-12-rot-0m24-0m37.wav` | 13.30 s | ROT | Thin air hiss. Place at 0:24.04 → ends 0:37.34. |
| 04 | `09-the-chair-es-04-collapse-0m39-0m42.wav` | 1.55 s | COLLAPSE | Low whoosh, one hit, no loop. 0:39.06–0:41.98. |
| 05 | `09-the-chair-es-05-cycle-0m43-0m53.wav` | 10.06 s | CYCLE | Heartbeat pulse. 0:43.34–0:53.40. |
| 06 | `09-the-chair-es-06-vision-0m55-1m02.wav` | 6.90 s | VISION | Mystic chime, first 6.90 s. 0:54.92–1:01.82. |
| 07 | `09-the-chair-es-07-layer-1m03-1m20.wav` | 16.26 s | LAYER | Time Does Not Matter SFX, first 16.26 s. 1:03.36–1:19.62. |
| 08 | `09-the-chair-es-08-whisper-1m21-1m26.wav` | 4.78 s | WHISPER | Horror whispers, hard out 1:26.04. |
| 09 | `09-the-chair-es-09-crack-1m28-1m31.wav` | 0.92 s | CRACK | Ice fracture, one hit, no loop. 1:27.92–1:31.22. |
| 10 | `09-the-chair-es-10-open-1m33-1m39.wav` | 2.16 s | OPEN | Soft wind whoosh. 1:32.94–1:39.36. |
| 11 | `09-the-chair-es-11-bloom-1m39-1m47.wav` | 7.32 s | BLOOM | Same chime as VISION. 1:39.40–1:46.72. |

Uncut masters (including unused rocks-crash, Dark Tunnels, Time Does Not Matter, air-hiss, wood-creak) stay in `alt/`. Mix from the numbered files. All of these are SFX.

---

## Session setup

Create 13 tracks, top to bottom:

1. Voice (locked)
2. ROOM
3. CHAIR
4. RUMBLE
5. HUMS
6. ROT
7. COLLAPSE
8. CYCLE
9. VISION
10. LAYER
11. WHISPER
12. CRACK
13. OPEN
14. BLOOM

All SFX under the voice. dB numbers are targets, not law. ROOM rides are **percent of body**.

---

## Step 1 — ROOM only

1. Put `es-01-room` on the ROOM track at **0:00.00**.
2. Fade in **0.6 s**.
3. Automate **this one clip**. Do not split it.
4. Fade to off **1:55.88–1:57.76**. After that the track is empty.

Body = 100%. Suggested body level **–22 dB** under the voice.

| From | To | Ride | Why |
|---|---|---|---|
| 0:00.00 | 0:22.40 | 100% | Opening through “beyond.” |
| 0:22.40 | 0:24.04 | hold 100% | Hole before rot |
| 0:24.04 | 0:37.34 | 80% | Under ROT |
| 0:37.34 | 0:39.06 | restore 100% | Before collapse |
| 0:39.06 | 0:43.34 | 100% | Collapse + hole |
| 0:43.34 | 0:53.40 | 71% | Under CYCLE |
| 0:53.40 | 0:54.92 | restore 100% | |
| 0:54.92 | 1:01.82 | 80% | Under VISION |
| 1:01.82 | 1:21.26 | 100% | Intention / layers — duck only if LAYER fights |
| 1:21.26 | 1:26.04 | 56% | Under WHISPER |
| 1:26.04 | 1:27.92 | restore 100% | |
| 1:27.92 | 1:31.22 | 80% | Under CRACK |
| 1:31.22 | 1:32.94 | restore 100% | |
| 1:32.94 | 1:39.36 | 71% | Under OPEN |
| 1:39.36 | 1:48.16 | 100% | Bloom, then hole |
| 1:48.16 | 1:55.88 | 56% | MUST — duck 5 dB, no new hit on the dashes |
| 1:55.88 | 1:57.76 | fade to 0 | |
| 1:57.76 | 2:02.50 | 0 | Last line dry |
| 2:02.50 | 2:05.00 | 0 | Empty air |

Solo Voice + ROOM once. The last line must be voice only.

---

## Step 2 — Add clips in this order

Drop each file at **Start**. Fade or trim so it is gone by **End**.

| Add | File | Start | End | Level | Under |
|---|---|---|---|---|---|
| CHAIR | `es-13` | 0:00.18 | 0:03.70 | –16 dB, one settle, **no loop** | “emptiness watches” through “All.” |
| RUMBLE | `es-02` | 0:05.30 | 0:12.08 | in 0.4 s, peak –14, thin by “insanity.” | “It stares…” through “insanity.” |
| HUMS | `es-03` | 0:12.14 | 0:22.40 | –15 under “light,” –13 on “hums,” –16 on “drones” | “Penetrating points…” through “beyond.” |
| ROT | `es-12` | 0:24.04 | 0:37.34 | in 0.5 s, peak –16 on “rot,” hold thin | “The beyond is known…” through “existence.” |
| COLLAPSE | `es-04` | 0:39.06 | 0:41.98 | –12 dB, short inward whoosh, **no loop** | “All collapses…” through “attention.” |
| CYCLE | `es-05` | 0:43.34 | 0:53.40 | –17 dB, slow two-tone pulse, out on “dead.” | “Attending…” through “the dead.” |
| VISION | `es-06` | 0:54.92 | 1:01.82 | –16 dB glassy pad, **out before “Intention”** | “Meaning is contained…” through “intent.” |
| LAYER | `es-07` | 1:03.36 | 1:19.62 | –16 dB, deepen after “not.” | “Intention settles…” through “reach.” |
| WHISPER | `es-08` | 1:21.26 | 1:26.04 | –14 dB, almost unintelligible, **hard out** | “Whispers feed…” through “construction.” |
| CRACK | `es-09` | 1:27.92 | 1:31.22 | –12 dB, one fracture, **no loop** | “Where is space if space is cracked?” |
| OPEN | `es-10` | 1:32.94 | 1:39.36 | in 0.3 s, peak –15 on “free?” | “And when…” through “are they free?” |
| BLOOM | `es-11` | 1:39.40 | 1:46.72 | –15 then lift **+3 dB** on “blooms” | “Determinism…” through “full.” |
| MUST | — | 1:48.16 | 1:55.88 | ROOM duck only | “It exists — it must — …” through “possibility.” |
| — | — | 1:57.76 | 2:02.50 | **nothing** | “I am, so it is, so we are.” |

---

## Step 3 — Check stacks

Legal combinations (Voice always in):

| Time | Playing |
|---|---|
| 0:00.00–0:00.18 | ROOM |
| 0:00.18–0:03.70 | ROOM + CHAIR |
| 0:05.30–0:12.08 | ROOM + RUMBLE |
| 0:12.14–0:22.40 | ROOM + HUMS |
| 0:24.04–0:37.34 | ROOM 80% + ROT |
| 0:39.06–0:41.98 | ROOM + COLLAPSE |
| 0:43.34–0:53.40 | ROOM 71% + CYCLE |
| 0:54.92–1:01.82 | ROOM 80% + VISION |
| 1:03.36–1:19.62 | ROOM + LAYER |
| 1:21.26–1:26.04 | ROOM 56% + WHISPER |
| 1:27.92–1:31.22 | ROOM 80% + CRACK |
| 1:32.94–1:39.36 | ROOM 71% + OPEN |
| 1:39.40–1:46.72 | ROOM + BLOOM |
| 1:48.16–1:55.88 | ROOM 56% only |
| 1:57.76–2:02.50 | Voice only |

VISION must be gone before “Intention” (1:03.36). WHISPER hard-out before CRACK. BLOOM gone before MUST.

---

## Step 4 — Pass / fail

- Last line is dry. No ROOM, no tail, no chime.
- CHAIR, CRACK, COLLAPSE fire once.
- WHISPER does not leak into “Where is space…”
- VISION does not leak into “Intention”
- MUST has no extra hit on the dashes — ROOM duck only

---

## Gaps vs the brief

| Token | Fit | Note |
|---|---|---|
| ROOM | closest on disk | Stairwell tone, 120 s. Empty hall, not a scored drone. |
| CHAIR | yes | Dry old-furniture creak, 1.05 s. One hit in a 3.52 s window. Do not loop. |
| RUMBLE | yes | First 6.78 s of Dark Tunnels. |
| HUMS | yes | Designed electric drone. |
| ROT | close | Thin long air hiss, 13.30 s. Quiet analog noise, not tape-peel. |
| COLLAPSE | close | Low short whoosh, 1.55 s (window is 2.92 s). Do not loop. |
| CYCLE | close | Designed heartbeat. Quiet it to –17 dB. |
| VISION | close | Mystic light-pad, same family as BLOOM. |
| LAYER | yes | First 16.26 s of Time Does Not Matter. |
| WHISPER | watch | Horror-whisper library — mute if words are intelligible. |
| CRACK | yes | Thin ice crack, one hit. |
| OPEN | close | Soft wind whoosh, 2.16 s in a 6.4 s window. One lift, then still. |
| BLOOM | close | Same chime as VISION; ride +3 dB on “blooms.” |

## Epidemic search / helper prompts

| Token | Prompt |
|---|---|
| ROOM | dark empty hall room tone low drone no melody no drums distant air 2 minutes |
| CHAIR | wooden chair creak settle once dry interior no crowd |
| RUMBLE | distant low rumble chaotic abyss sub bass no melody cinematic far |
| HUMS | monotone electrical drone matrix hum brutal indifferent no pulse mid scooped |
| ROT | tape decay dust fall fabric tear very quiet analog rot no music |
| COLLAPSE | inward whoosh pressure drop short 3 seconds no boom |
| CYCLE | slow two tone pulse living dead heartbeat very quiet no drums |
| VISION | thin glassy pad high overtone empty midrange no melody |
| LAYER | deep reverb swell morphing layers out of reach sparse drone |
| WHISPER | unintelligible whispers through cracks wall close dry no words |
| CRACK | ice glass crack single fracture space splitting short |
| OPEN | air opens after crack distant wind lift no melody |
| BLOOM | soft harmonic bloom after dissolve no choir no lyric |
