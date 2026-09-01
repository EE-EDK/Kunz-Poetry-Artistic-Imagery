# Ersatz Machinations — SFX work instruction

Replace the old cue map with this. Mix **one track at a time** against the locked voice.

Local stems only (Epidemic license) — not in git.

## Locked voice

| Item | Value |
|---|---|
| File | `06-ersatz-machinations-voice-FINAL.mp3` |
| Length | **95.24 s** |
| Last line | “I am.” **94.34–95.14** |
| Clock | all times below are on this take |

Do not slip stems to a different voice render without rebuilding this sheet.

## How to think about it

- **HUM** is one continuous clip from `0:00` to `0:93`, then off. Ride its volume. Do not cut it into pieces.
- Every other stem is a **placement**. Import once, copy if the sheet says `#2` or `#3`.
- **ROBOT-ON** stays at the top (`0:00–0:14.80`). It is 19.9 s. Do **not** put it in the 2.3 s hole after “care.” That hole is **LOCK** only.
- Do not loop SERVO.
- If anything other than voice is audible on “I am.”, a clip is too late.

## Stems

| # | File | Length | Token | Use |
|---|---|---|---|---|
| 01 | `06-ersatz-machinations-es-01-hum-0m00-1m33.wav` | 98.0 s | HUM | One clip, `0:00.00–0:93.00` |
| 02 | `06-ersatz-machinations-es-02-robot-on-0m00-0m15.wav` | 19.9 s | ROBOT-ON | One clip at the title |
| 03 | `06-ersatz-machinations-es-03-servo-0m00-0m02.wav` | 3.7 s | SERVO | Same file, two placements |
| 04 | `06-ersatz-machinations-es-04-disc-0m03-0m06.wav` | 8.0 s | DISC | One placement |
| 05 | `06-ersatz-machinations-es-05-hiss-0m10-0m13.wav` | 8.4 s | HISS | One placement |
| 06 | `06-ersatz-machinations-es-06-swarm-0m26-0m34.wav` | 7.8 s | SWARM | Same file, three placements |
| 07 | `06-ersatz-machinations-es-07-spark-0m37-0m40.wav` | 7.7 s | SPARK | Same file, three placements |
| 08 | `06-ersatz-machinations-es-08-joint-0m63-0m66.wav` | 7.3 s | JOINT | One placement |
| 09 | `06-ersatz-machinations-es-09-floor-0m84-0m92.wav` | 12.8 s | FLOOR | One placement |
| 10 | `06-ersatz-machinations-es-10-lock-0m93.wav` | 5.5 s | LOCK | One click in the hole before “I am.” |

Trim one-shots to the window in the placement list. The files are longest-cue + ~5 s of pad.

---

## Session setup

Create 11 tracks, top to bottom:

1. Voice (locked)
2. HUM
3. ROBOT-ON
4. SERVO
5. DISC
6. HISS
7. SWARM
8. SPARK
9. JOINT
10. FLOOR
11. LOCK

All SFX under the voice. Start conservative if a clip feels loud; the dB numbers are targets, not law.

---

## Step 1 — HUM only

1. Put `es-01-hum` on the HUM track at **0:00.00**.
2. Let it run to **0:93.00**.
3. Fade out **0:92.04–0:93.00**.
4. After 0:93.00 the track is empty (file may still contain pad through 0:98 — mute or trim it).
5. Automate **this one clip**. Do not split it.

| From | To | HUM level | Why |
|---|---|---|---|
| 0:00.00 | 0:13.18 | –18 dB | Body stanza |
| 0:13.18 | 0:16.80 | –23 dB | “But why am I?” |
| 0:16.80 | 0:26.40 | –18 dB | Form / source |
| 0:26.40 | 0:33.80 | –21 dB | Under SWARM #1 |
| 0:33.80 | 0:36.20 | –23 dB | “But what am I?” |
| 0:36.20 | 0:49.52 | –18 dB | Madness / feel |
| 0:49.52 | 0:54.60 | –23 dB | “But where am I?” |
| 0:54.70 | 0:62.60 | –21 dB | Under SWARM #3 |
| 0:62.60 | 0:71.20 | –18 dB | Pain / lied |
| 0:71.20 | 0:76.10 | –23 dB | “It hurts inside.” + “But who am I?” |
| 0:76.20 | 0:92.04 | –15 dB | Horror / floor |
| 0:92.04 | 0:93.00 | fade to off | Hole for LOCK |
| 0:93.00 | end | off | “I am.” stays dry |

Solo Voice + HUM and play the whole poem once. The questions should feel like the room got quieter, not like the bed disappeared.

---

## Step 2 — Add clips in this order

Drop each file at **Start**. Fade or trim so it is gone by **End**.

| Add | File | Start | End | Level | Under |
|---|---|---|---|---|---|
| ROBOT-ON | `es-02` | 0:00.00 | 0:14.80 | –16 dB, out by 0:14.80 | Title through “evening’s brisk.” |
| SERVO #1 | `es-03` | 0:00.18 | 0:02.40 | –14 dB | “Tendons rage against the output;” |
| DISC | `es-04` | 0:03.20 | 0:06.20 | –15 dB | “heat caresses wire and disc.” |
| SERVO #2 | `es-03` copy | 0:06.70 | 0:09.30 | –16 dB | “flinching foot” |
| HISS | `es-05` | 0:10.10 | 0:13.40 | –16 dB | “thermal signs — the evening’s brisk.” |
| SWARM #1 | `es-06` | 0:26.40 | 0:33.80 | In 0.6 s, peak –12 dB, out by 0:33.80 | Both “swarms” lines |
| SPARK #1 | `es-07` | 0:37.20 | 0:39.80 | –13 dB | “Madness shines within the code.” |
| SWARM #2 | `es-06` copy | 0:44.40 | 0:49.80 | –16 dB | “nodes” / “feel?” |
| SPARK #2 | `es-07` copy | 0:48.90 | 0:50.00 | –14 dB | “feel?” |
| SWARM #3 | `es-06` copy | 0:54.70 | 0:62.60 | –13 dB, thin to –18 by “outside” | “Blinding floods…” → “outside.” |
| JOINT | `es-08` | 0:63.40 | 0:65.70 | –12 dB, land on “pain” 0:64.02 | “Sudden pain within the joints.” |
| SPARK #3 | `es-07` copy | 0:66.60 | 0:69.20 | –13 dB | “The nodes — they lied.” |
| FLOOR | `es-09` | 0:84.40 | 0:92.20 | –14 dB, hard out 0:92.20 | “Monstrosities…” → “without care.” |
| LOCK | `es-10` | 0:93.10 | 0:93.60 | –10 dB, no tail | Hole after “care.” |

Skip SPARK at `0:40.80` (“light is real?”) unless that line feels empty after the first pass.

SERVO #2, SWARM #2/#3, and SPARK #2/#3 are **copies of the same stem**. Do not loop SERVO.

---

## Step 3 — Check stacks

After every clip is in, these are the only legal combinations:

| Time | Should be playing |
|---|---|
| 0:00.00–0:02.40 | Voice + HUM + ROBOT-ON + SERVO |
| 0:03.20–0:06.20 | Voice + HUM + ROBOT-ON + DISC |
| 0:06.70–0:09.30 | Voice + HUM + ROBOT-ON + SERVO |
| 0:10.10–0:13.40 | Voice + HUM + ROBOT-ON + HISS |
| 0:13.18–0:14.80 | Voice + HUM + ROBOT-ON dying |
| 0:15.14–0:16.48 | Voice + quiet HUM |
| 0:26.40–0:33.80 | Voice + HUM + SWARM |
| 0:37.20–0:39.80 | Voice + HUM + SPARK |
| 0:44.40–0:50.00 | Voice + HUM + SWARM (+ SPARK on “feel?”) |
| 0:54.70–0:62.60 | Voice + HUM + SWARM |
| 0:63.40–0:65.70 | Voice + HUM + JOINT |
| 0:66.60–0:69.20 | Voice + HUM + SPARK |
| 0:84.40–0:92.20 | Voice + HUM + FLOOR |
| 0:93.10–0:93.60 | LOCK alone |
| 0:94.34–0:95.14 | Voice alone |

### Keep dry (HUM ducked, no one-shots)

- 0:15.14–0:16.48 — “But why am I?”
- 0:34.42–0:35.76 — “But what am I?”
- 0:51.72–0:53.22 — “But where am I?”
- 0:69.88–0:71.20 — “It hurts inside.”
- 0:73.16–0:74.66 — “But who am I?”
- 0:94.34–0:95.14 — “I am.”

---

## Step 4 — Pass / fail

Play the mix once with Voice in front.

- Questions feel quieter, not empty.
- ROBOT-ON is gone before “But why am I?”
- FLOOR is gone before 0:92.20.
- LOCK clicks in the hole and does not touch “I am.”
- “I am.” is voice only.

If LOCK or FLOOR leaks into “I am.”, pull that clip left. Do not start HUM again after 0:93.00.
