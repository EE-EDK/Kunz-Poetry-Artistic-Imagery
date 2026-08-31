# CLAUDE.md — Shadowshining

## Commands

```
python scripts/bootstrap.py
python scripts/align_timings.py 01
python scripts/align_timings.py --all
python scripts/burn_lyrics.py 01
python scripts/burn_lyrics.py 01 --audio-only
```

Requires `ELEVENLABS_API_KEY` in `.env` for alignment. ffmpeg via `paths.FFMPEG`.

Git: independent repo `EE-EDK/Kunz-Poetry-Artistic-Imagery`, branch `main`.
Media is Git LFS (`git lfs pull` on a fresh clone — pointers are 134 bytes).
See `GROK.md` → Git. Never stage `.env`.

Live showing: https://kunz-ai-hub.tailb1d0b7.ts.net/p/shadowshining-selected-poems/
This repo is twenty-five independent films. Publishing a finished cut onto
kunzhub is `GROK.md` → Hub publish, not a step of `burn_lyrics.py`.

## Directory map

```
paths.py
src/catalog.json
texts/shadowshining-selected-poems.md
poems/NN-slug/
  poem.md
  transcript.txt
  audio/elevenlabs|music|sfx|epidemic|mix/
  timing/          # *.alignment.json *.words.json *.srt
  images/
  video/
  inbox/
inbox/             # unfiled drops
scripts/
docs/
docs_dev/
```

## Conventions

- Poem ids are 01–25, folders `NN-slug`.
- Forced alignment transcript is `transcript.txt` (title + body, no markdown).
- SRT is derived from spoken words only (whitespace tokens dropped).
- Epidemic Sound / library cues go in `audio/epidemic/`, not `sfx/`.
- Generated stills go in `images/`; do not overwrite voice or timing.
- Lyric video output: `video/NN-slug-lyrics.mp4`.

## Adding a new take

**From Downloads (usual path):** "move / pull / retrieve / grab / file" means
search `C:\Users\edk7c\Downloads` for files from the last ~10 minutes, rename
to `NN-slug-brief-descriptor.ext`, put them in the poem slot, refresh the
catalog. If the poem is unclear, stop and ask. See `GROK.md` → Downloads pull.

**Already in-tree:**

1. Drop the file in the poem folder (or `inbox/`).
2. Run `python scripts/align_timings.py NN` if it is a new voice take.
3. Refresh catalog: `python scripts/bootstrap.py` (moves known root dumps; safe
   on an already-scaffolded tree).
