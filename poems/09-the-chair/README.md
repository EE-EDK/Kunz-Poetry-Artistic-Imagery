# 09 — The Chair

**Phase: picture-locked / final cut (continuous-motion rebuild)** (2026-09-04)

## In git / Drive

| Slot | File |
|------|------|
| Voice (current) | `audio/elevenlabs/09-the-chair-voice-FINAL.mp3` — **122.67 s** |
| Mix (current) | `audio/mix/09-the-chair-mix-FINAL.wav` — **122.68 s** (same clock) |
| Captions | `timing/09-the-chair.srt` |
| Alignment | `timing/09-the-chair.alignment.json` · `.words.json` |
| ASS | `timing/09-the-chair-lyrics.ass` (Georgia, fad, Default/Soft/Dark/Title) |
| Picture | `video/09-the-chair-final.mp4` (1080p, yuv420p, +faststart) |
| Web copy | `video/09-the-chair-web.mp4` (baseline, CRF 24, AAC 128k) |
| Working 720 | `video/09-the-chair-final-720.mp4` |
| Stills | `images/09-01-seat-of-all.jpg` … `09-10-i-am-dry.jpg` (+ hero base) |
| SFX map | `audio/sfx/CUE_MAP.md` |

## Clocks

Mix FINAL **122.68 s** = dry voice. Picture locked to mix. Last line dry.

## Visual grammar

- **Chair (locked):** well-crafted but very old generic wooden chair — four plain vertical spindles, rectangular back, flat worn seat, simple legs + stretchers, no arms, darkened thinned varnish, empty. Throne only by presence.
- Early: watching emptiness + matrix pin-pricks + first tears of oblivion
- Mid: rot dust + cycles + layers out of reach + collapse
- Late: cracked geometry → bloom → residual rim + softest after-bloom
- No faces, no ornate thrones, no banned symbols

## Edit notes (rebuild)

- 9 continuous-motion sources (10 s) stretched via setpts (no tpad freeze / no static holds)
- Soft 2.75 s xfades; single filter_complex chain
- Background always dynamic (dust, light crawl, rings, cracks, bloom); chair locked solid
- ASS burned; mix muxed as-is (no loudnorm)
- Duration final **≈122.65 s**

## Next

Hub published 2026-09-04 on kunz-ai-hub
(`09-the-chair-final.mp4`, 1080p). Poster is still 01
(`images/09-01-seat-of-all.jpg`). New take = new web filename
(`GROK.md` → Hub publish). Mix SFX still local. The 720p
`09-the-chair-final-720.mp4` and CRF web copy are the smaller
encodes; the hub serves the 1080p final.
