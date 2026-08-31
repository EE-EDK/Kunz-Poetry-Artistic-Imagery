# 02 — Murdered Mind

**Phase: active** (2026-08-30)

Current poem. Voice, timing, music bed, and Epidemic beds are in place.
Still missing: stills, picture/video, mix.

## In git

| Slot | File |
|------|------|
| Voice | `audio/elevenlabs/02-murdered-mind-voice.mp3` |
| Music | `audio/music/02-murdered-mind-music.wav` |
| Captions | `timing/02-murdered-mind.srt` |
| Word clocks | `timing/02-murdered-mind.words.json` |
| Text | `poem.md` / `transcript.txt` |

Voice span ~0.08–176.2 s. Alignment loss ~0.17.

## Local only (not in git)

Epidemic Sound cues in `audio/epidemic/`:

- `02-murdered-mind-es-ambience-drone-room-tone.wav`
- `02-murdered-mind-es-doors-dungeon-gate-latch.wav`
- `02-murdered-mind-es-fire-crackle-embers.wav`
- `02-murdered-mind-es-human-breath-male.wav`
- `02-murdered-mind-es-metal-friction-scraping.wav`
- `02-murdered-mind-es-voices-distant-screams.wav`

## Next

1. Pull/generate stills into `images/`.
2. Mix voice + music + epidemic → `audio/mix/`.
3. Picture cut into `video/`, then `python scripts/burn_lyrics.py 02`.
