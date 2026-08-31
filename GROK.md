# GROK.md — Shadowshining

## Project Identity

Twenty-five poem films from the *Shadowshining* collection. Each poem is its
own unit: ElevenLabs voice, timing, music, SFX, stills, lyric video. Lighter
than The Void is Crimson — no 540-shot bible, no continuity ledger.

Folder on disk: `ACTIVE-PROJECTS/ai-video-photo/Kunz-Poetry-Artistic-Imagery`
(cloned onto kunz-ai-hub 2026-08-31). On KunzPrime it has also lived under
the local name `Kunz-Poems-Eleven-Labs-MP3`.

This is **twenty-five independent poem-films in one repo**, not one production.
The public showing is
https://kunz-ai-hub.tailb1d0b7.ts.net/p/shadowshining-selected-poems/ .

Active poem: **03 Apoclyte** (`src/progress.json`). Poems **01** and **02**
have `*-final.mp4` in git; hub publish is on the other machine.

## Doc Precedence

`GROK.md` (this file) → `AGENTS.md` → `CLAUDE.md`. Do not import Void-is-Crimson
story data, locks, or scripts.

## Pipeline Commands

```
python scripts/bootstrap.py              # rebuild 25-poem tree + catalog.json
python scripts/align_timings.py 01       # forced alignment for one poem
python scripts/align_timings.py --all    # any poem that has a voice file
python scripts/burn_lyrics.py 01         # burn SRT onto video / lyric card
```

## Grok CLI

Still images and image→video for a poem run through the local Grok CLI on the
SuperGrok login (`$0`). Keep `XAI_API_KEY` **unset**. Save frames into that
poem's `images/` and clips into `video/`. Run generation from your own
PowerShell (pwsh 7), not via the agent terminal.

ElevenLabs is the exception: voice + forced alignment use `ELEVENLABS_API_KEY`
in `.env`.

## Downloads pull

Trigger phrases (any close variant): **move image**, **pull image**, **retrieve**,
**file the download**, **grab the still**, **pull the video**, **get that wav**.
These mean the artifact is already on this machine, usually a fresh browser or
CLI save into `C:\Users\edk7c\Downloads` (KunzPrime) or `~/Downloads`
(kunz-ai-hub).

**From kunz-ai-hub, pull KunzPrime Downloads with SCP.** Do not search the
hub first and stop. Username is `EthanK-admin` — **not** `edk7c` (that is
only the Windows profile folder). Hub `~/.ssh/id_ed25519` is already
authorized:

```
scp "EthanK-admin@100.118.229.4:C:/Users/edk7c/Downloads/<file>" ~/Downloads/
```

Do this immediately:

1. Search the **Downloads root** (not `Archive-Downloads/`) for files modified
   in the last few minutes. Default window: **10 minutes**. Skip
   `desktop.ini`, `*.crdownload`, `MOVED.txt`, and this project's leftover
   stub folder.
2. **Assess** each hit: type (still / video / voice / music / sfx / library),
   likely poem (filename, current conversation, content), and destination
   slot under `poems/NN-slug/`.
3. **Rename** to `NN-slug-brief-descriptor.ext` (ASCII, hyphens, no spaces).
   Keep a version suffix if it is a new take (`-v2`, `-v4`).
4. **Place** it in the matching slot (`images/`, `video/`,
   `audio/elevenlabs|music|sfx|epidemic|mix/`). Refresh `src/catalog.json`
   (`python scripts/bootstrap.py`).
5. If the poem, slot, or take identity is **not clear**, stop. List what you
   found (name, time, size, guessed type) and ask. Do not guess a poem.
   Ethan will fill in the missing fact.

This pull overrides a generic Downloads sweep: do not archive these files
into `Archive-Downloads/` while they belong to Shadowshining.

## Git

Independent repo — not MASTER. Remote `origin` is
`git@github.com:EE-EDK/Kunz-Poetry-Artistic-Imagery.git`, branch `main`.

- Never commit `.env` or the API key.
- Media (`mp4`, `wav`, `mp3`, stills) is Git LFS. Track new types in
  `.gitattributes` *before* `git add`.
- Epidemic Sound masters stay local (`**/audio/epidemic/` in `.gitignore`).
- Stage by path. Do not `git add -A` / `git add .` as a habit — confirm
  `git status` has no secrets and no stray Downloads dumps at the root.
- Commit messages: Register C, imperative subject.
- Push `main` only when asked. Never force-push or rewrite history without
  explicit approval.
- After filing a Downloads pull, commit the poem-folder files (LFS pointers
  for media, normal blobs for `timing/` JSON and SRT).

## Hub publish (kunz-ai-hub)

A finished cut is not live until the poem page on kunzhub plays it.

Live showing: `/p/shadowshining-selected-poems/`. Poem pages:
`/p/poems-by-ethank/<slug>.html`.

When a `poems/NN-slug/video/*-final.mp4` is ready:

1. `git lfs pull` if this clone only has the pointer.
2. Transcode a web copy into kunzhub
   `pages/public/poems-by-ethank/media/films/<slug>.mp4`
   (`ffmpeg -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart`).
   Force 4:2:0 — the Apoclyte 79s master is yuv444, which browsers will not play.
   Do not copy the LFS master — it is ~174MB / 12 Mbps; GitHub rejects blobs
   over 100MB and the web copy is gitignored in kunzhub.
3. Add `<slug>.html` to kunzhub `_build/films.json`.
4. `python3 apply_film.py` from that `_build/` directory.

The poem's top image (if it has one) becomes a playable poster. No
Facebook hero: put `poster` in the films.json spec and apply_film
inserts the cover after the meta line. Click fullscreens the cut. When
it ends, the reader returns to the 25-poem showing. Escape or leaving
fullscreen early stays on the poem.

New take = new web filename, or Caddy's 7-day `*.mp4` cache will keep the
old cut. Do not rebuild the 91 poem pages from `build_site.py`.

## Execution Notes

- `src/catalog.json` is regenerable via `scripts/bootstrap.py`.
- Never commit `.env`.
- File new media into `poems/NN-slug/...` or `inbox/`. Do not leave production
  assets at the project root.
- On-screen text must follow `timing/*.srt` / `timing/*.words.json`, not a
  guessed cadence.
