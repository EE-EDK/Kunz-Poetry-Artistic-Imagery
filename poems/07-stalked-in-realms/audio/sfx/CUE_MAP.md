# Stalked in Realms — SFX work instruction

Mix **one track at a time** against the locked voice.

Local stems only (Epidemic license) — not in git.

All eight downloads are in the mix. **BREATH and FLINCH are one hit:**
the inhale and the creak stack on “We wake in dread.” Do not split them
across two moments.

## Locked voice

| Item | Value |
|---|---|
| File | `07-stalked-in-realms-voice-FINAL.mp3` |
| Length | **42.92 s** |
| First word | “Sleep” **0.36–0.76** |
| Last word | “leap.” **42.26–42.68** |
| Clock | all times below are on this take |

Title is not spoken. Do not slip stems to a different voice render without rebuilding this sheet.

## How to think about it

- **ROOM** is one continuous clip from `0:00` to `0:43`. Ride its volume.
- **HUSH** is the office tone under the wake stanza — thinner air, same night. If it reads as a different room, drop it and duck ROOM instead.
- **SHEET** is one stem, two placements. Same clip both times so the cycle matches.
- **SHIMMER** must be gone at **0:18.70**. Hard cut. It must not leak into the wake.
- **BREATH + FLINCH** are together at **0:18.80–0:20.50**. Three layers, one gesture: held inhale (gasp 01), snapped inhale (gasp 03), wooden creak. They land on “We wake in dread.” Not a separate fear-breath at 0:04.
- **SETTLE** is down-and-still. No bounce after “leap.”
- If anything other than dying ROOM is audible after **0:42.90**, a clip is too late.

## Stems

| # | File | Length | Token | Use |
|---|---|---|---|---|
| 01 | `07-stalked-in-realms-es-01-room-0m00-0m43.wav` | 47.96 s | ROOM | One clip, `0:00.00–0:43.00`. |
| 02 | `07-stalked-in-realms-es-02-sheet-0m00-0m03.wav` | 2.05 s | SHEET | Same file, two placements. First cotton gesture, then still. |
| 03 | `07-stalked-in-realms-es-03-breath-0m19-0m21.wav` | 1.01 s | BREATH | Held inhale. **Stacks with FLINCH** at 0:18.80. |
| 04 | `07-stalked-in-realms-es-04-shimmer-0m10-0m19.wav` | 8.30 s | SHIMMER | Place at 0:10.40 → ends 0:18.70. |
| 05 | `07-stalked-in-realms-es-05-flinch-creak-0m19-0m21.wav` | 0.92 s | FLINCH | Wooden creak. With BREATH + inhale, 0:18.80. |
| 06 | `07-stalked-in-realms-es-06-flinch-inhale-0m19-0m21.wav` | 0.40 s | FLINCH | Snapped inhale (gasp 03). With creak + BREATH. |
| 07 | `07-stalked-in-realms-es-07-hush-0m21-0m26.wav` | 5.60 s | HUSH | Office tone. Place at 0:20.80 → ends 0:26.40. |
| 08 | `07-stalked-in-realms-es-08-settle-0m41-0m43.wav` | 1.70 s | SETTLE | Sit/sink. Place at 0:41.20 → ends 0:42.90. |

Uncut masters stay in `alt/`. Mix from the numbered files only.

---

## Session setup

Create 9 tracks, top to bottom:

1. Voice (locked)
2. ROOM
3. SHEET
4. SHIMMER
5. BREATH
6. FLINCH creak
7. FLINCH inhale
8. HUSH
9. SETTLE

All SFX under the voice. Start conservative; the dB numbers are targets, not law.

---

## Step 1 — ROOM only

1. Put `es-01-room` on the ROOM track at **0:00.00**.
2. Let it run to **0:43.00**. Mute or trim the pad after that.
3. Automate **this one clip**. Do not split it.

| From | To | ROOM level | Why |
|---|---|---|---|
| 0:00.00 | 0:10.40 | –24 dB | Sleep / fear |
| 0:10.40 | 0:18.70 | –28 dB | Under SHIMMER |
| 0:18.70 | 0:20.80 | –24 dB | Wake / BREATH+FLINCH |
| 0:20.80 | 0:26.40 | –32 dB | Under HUSH (same space, thinner) |
| 0:26.40 | 0:41.20 | –24 dB | Recall / it will not pause |
| 0:41.20 | 0:42.90 | –28 dB | Under SETTLE / “the leap.” |
| 0:42.90 | 0:43.00 | fade to off | Stillness after the drop |

Solo Voice + ROOM once.

---

## Step 2 — Add clips in this order

Drop each file at **Start**. Fade or trim so it is gone by **End**.

| Add | File | Start | End | Level | Under |
|---|---|---|---|---|---|
| SHEET #1 | `es-02` | 0:00.30 | 0:03.40 | –18 dB | “Sleep is cruel when pain is near.” Gesture ~2.05 s; rest of the window is still. |
| SHIMMER | `es-04` | 0:10.40 | 0:18.70 | –20 dB, **hard out 0:18.70** | “In dreams of light…” through “without our sight.” |
| BREATH | `es-03` | 0:18.80 | 0:20.50 | –16 dB | With FLINCH. Held inhale on “We wake in dread.” |
| FLINCH creak | `es-05` | 0:18.80 | 0:20.50 | –12 dB | With BREATH. Attack ~50 ms in; land it on **wake** 19.14. |
| FLINCH inhale | `es-06` | 0:18.80 | 0:20.50 | –14 dB | With BREATH + creak. Snapped inhale, same hit. |
| HUSH | `es-07` | 0:20.80 | 0:26.40 | –28 dB | “We ache inside…” through “We stare ahead.” |
| SHEET #2 | `es-02` copy | 0:36.00 | 0:37.80 | –18 dB | “until we sleep.” Same clip as #1. |
| SETTLE | `es-08` | 0:41.20 | 0:42.90 | –16 dB | “we take the leap.” Down-and-still. Gone by 0:42.90. |

BREATH, FLINCH creak, and FLINCH inhale start on the **same** clock. They are one wake, not a sequence.

Do not put BREATH on “When gripped by fear” (0:04.30). That hole stays ROOM + voice.

SHEET #2 is a **copy of the same stem**.

---

## Step 3 — Check stacks

After every clip is in, these are the only legal combinations:

| Time | Should be playing |
|---|---|
| 0:00.00–0:00.30 | Voice + ROOM |
| 0:00.30–0:03.40 | Voice + ROOM + SHEET |
| 0:04.30–0:08.22 | Voice + ROOM | fear / “let darkness rule.” — no extra SFX |
| 0:10.40–0:18.70 | Voice + ducked ROOM + SHIMMER |
| 0:18.80–0:20.50 | Voice + ROOM + **BREATH + creak + snapped inhale** |
| 0:20.80–0:26.40 | Voice + ducked ROOM + HUSH |
| 0:36.00–0:37.80 | Voice + ROOM + SHEET |
| 0:41.20–0:42.90 | Voice + ROOM + SETTLE |
| 0:42.90–end | nothing (or ROOM dying) |

### Keep dry (ROOM only, no one-shots)

- 0:04.30–0:10.40 — “When gripped by fear, let darkness rule.”
- 0:26.40–0:36.00 — “Then we recall the lawless fact…”
- 0:37.80–0:41.20 — “It starts again the moment when”
- 0:42.90–end — after the leap

---

## Step 4 — Pass / fail

Play the mix once with Voice in front.

- All eight stems are audible at least once.
- BREATH and both FLINCH layers hit as **one** wake. If it reads as three events, pull them onto the same start and drop the loudest.
- SHIMMER is gone at 0:18.70. The wake stack does not start before that cut.
- HUSH is the same night, quieter — not a cut to an office. If it teleports, mute `es-07` and leave the ROOM duck.
- SHEET #1 and #2 are the same gesture.
- SETTLE has no bounce after “leap.”
- After 0:42.90 the bed is still.

---

## Source → token

| Download | Token |
|---|---|
| Quiet Hotel Room, Morning | ROOM |
| Empty Office, Deep, Quiet | HUSH |
| Bed, Sheet, Cotton 05 | SHEET |
| Bed, Sit Down, Soft | SETTLE |
| Bed, Wooden Frame, Creak 02 | FLINCH creak |
| Magic, Shimmer, Crystal Sphere | SHIMMER |
| Breath, Female 01, Gasp var 02 | BREATH (with FLINCH) |
| Breath, Female 03, Gasp var 03 | FLINCH inhale (with BREATH) |
