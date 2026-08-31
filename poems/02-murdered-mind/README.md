# 02 — Murdered Mind

**Phase: active** (2026-08-30)

Current poem. Voice, timing, music bed, and Epidemic beds are in place.
Still missing: stills, picture/video, mix.

## In git

| Slot | File |
|------|------|
| Voice (current) | `audio/elevenlabs/02-murdered-mind-voice.wav` |
| Voice v1 | `audio/elevenlabs/02-murdered-mind-voice-v1.mp3` |
| Music | `audio/music/02-murdered-mind-music.wav` |
| Captions | `timing/02-murdered-mind.srt` (from the wav take) |
| Word clocks | `timing/02-murdered-mind.words.json` |
| Text | `poem.md` / `transcript.txt` |

Current wav span ~0.08–178.6 s. Alignment loss ~0.19.

## Local only (not in git)

Epidemic Sound cues in `audio/epidemic/`:

- `02-murdered-mind-es-ambience-drone-room-tone.wav`
- `02-murdered-mind-es-braam-classic-soft-brass-cs.wav`
- `02-murdered-mind-es-braam-massive-electronic-horn.wav`
- `02-murdered-mind-es-braam-straight-tone.wav`
- `02-murdered-mind-es-doors-dungeon-gate-latch.wav`
- `02-murdered-mind-es-fire-crackle-embers.wav`
- `02-murdered-mind-es-human-breath-male.wav`
- `02-murdered-mind-es-metal-friction-scraping.wav`
- `02-murdered-mind-es-voices-distant-screams.wav`

## Next

1. Pull/generate stills into `images/`.
2. Mix voice + music + epidemic → `audio/mix/`.
3. Picture cut into `video/`, then `python scripts/burn_lyrics.py 02`.
