# AGENTS.md — Shadowshining — Agent Startup Brief

> All AI agents read this first.

## Session Startup

1. `GROK.md` — Grok execution context
2. `AGENTS.md` — this brief
3. `CLAUDE.md` — layout, commands, conventions
4. `src/catalog.json` — which poems have audio / timing / video

Read only this project. Do not pull The Void is Crimson production data.

**Doc precedence:** `GROK.md` → `AGENTS.md` → `CLAUDE.md`

## Project Identity

*Shadowshining* is a 25-poem audiovisual set — **twenty-five independent
films in one repo**, not one production. Unit of work is one poem folder
under `poems/NN-slug/`. Shared scripts live in `scripts/`. Paths resolve from
`paths.py`. Public showing:
https://kunz-ai-hub.tailb1d0b7.ts.net/p/shadowshining-selected-poems/

## Downloads pull

If Ethan says **move image**, **pull image**, **retrieve**, **file**, **grab**,
or any close variant: the file is already on this PC, almost always in
`C:\Users\edk7c\Downloads` (KunzPrime) or `~/Downloads` (kunz-ai-hub), root,
last few minutes. Search there, assess,
rename to `NN-slug-brief-descriptor.ext`, catalog, and place under
`poems/NN-slug/<slot>/`. If the poem or slot is not obvious, **say so and
wait** — list the files found and ask. Do not guess. Full procedure:
`GROK.md` → Downloads pull.

## Red Lines

- No destructive deletes without explicit confirmation.
- No commits or pushes unless the user asks (END SESSION counts for its scope).
- Do not invent poem text. Canonical source is `texts/shadowshining-selected-poems.md`.
- Do not guess word timings. Use ElevenLabs forced alignment output.
- Do not mix two poems' media in one folder.
- Never print or commit `ELEVENLABS_API_KEY`.
- Do not archive a fresh Downloads pull into `Archive-Downloads/` while it
  belongs to this project.

## Git

This folder is its own repo (`Kunz-Poetry-Artistic-Imagery`, `main`). MASTER
gitignores `ai-video-photo/`, so never commit this tree from ENGINEERING-PROJECTS.

- Stage by explicit path. Confirm `.env` is untracked before every commit.
- Media goes through Git LFS (`.gitattributes`). Epidemic Sound cues in
  `audio/epidemic/` are local-only.
- No force-push / history rewrite without explicit approval.
- Full procedure: `GROK.md` → Git.

## Validation

Before claiming alignment or a lyric burn is done, confirm the files exist
under that poem's `timing/` or `video/` and print sizes / durations.

## Writing Voice

Voice policy: workspace `docs/writing/VOICE-POLICY.md`. Register B for
human-facing docs; Register C for this file, `GROK.md`, `CLAUDE.md`,
`GEMINI.md`, commits, and code.
