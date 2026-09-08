> **Shot table superseded 2026-09-08** by [`SHOTS-MANIFEST.md`](SHOTS-MANIFEST.md).
> The HARD RULES, global prompt and story beats below still stand.
> The 18-shot table and UUID catalog are historical: eight of those UUIDs
> were never downloaded, and the film is now cut from the 20 clips in
> `video/videoset-keep` plus the elk bridge.

# THE FOREST DISEASE — LOCAL / GROK CLI HANDOFF
Generated for: kunz poems / eleven labs mp3 local folder
Picture lock: MIX-v2 = **177.00 s** | 1280×720 | 24 fps | 16:9
Soft xfades: **1.8–2.4 s** only (no hard cuts inside a shot)
Camera: floating consciousness — no footsteps, no solid spirit body
Animals OK only where map says (raven pond, bear). Else empty.

## HARD RULES (learned the hard way)
1. **NEVER loop, reverse, freeze, tpad, or setpts-stretch** to fill time.
2. If continuous video is short of the film window → **generate more** or report the gap. Do not pad.
3. Soft **xfade only** between shots (and multi-source within a shot).
4. Mux audio last: **MIX-v2.wav** (177s) + burn **lyrics.ass** (mix-aligned).
5. Photoreal: anchor image_to_video / reference_to_video on map stills + real PNW photo refs when possible.
6. No cartoon gold, no vanishing trees, no inventing rivers from canopy stills.
7. Spirit = reflection only (or none for clean river). Never a solid body.

## AUDIO / SUBS (put these in your local folder)
| File | Role |
|------|------|
| `11-the-forest-disease-MIX-v2.wav` (or .mp3) | Master audio **177.00 s** |
| `11-forest/lyrics.ass` | Poem subtitles, times locked to MIX-v2 |
| `timing/11-the-forest-disease.words.json` | Word-level alignment |
| `timing/11-the-forest-disease.alignment.json` | Alignment dump |
| `timing/11-the-forest-disease.srt` | SRT alt |
| `VIDEO-AI-MAP.md` | Full 18-shot creative map |

## GLOBAL PROMPT (prepend every generation)
```
Pacific Northwest temperate rainforest, Douglas fir hemlock cedar, moss, fern understory,
hyper-real documentary photography, soft fantasy bioluminescent moss only (not neon cartoon),
floating camera chest-to-canopy height, slow drift only, no people, no text, no hard cuts inside a shot.
Solid stable trees — no morphing, no vanishing trunks.
```

## 18-SHOT TIMELINE + RECOMMENDED CLIPS
| # | Shot | In–Out | Film s | Stills family | Recommended video UUID(s) | Notes |
|---|------|--------|--------|---------------|---------------------------|-------|
| 1 | Enter | 0:00–0:18 | 18 | 7ebae00a→50d1dd62 | 466e437e…, b044f7bf… | Enter wide mist drift |
| 2 | S1 body | 0:18–0:27 | 9 | 27a2bbc5→266fa333 | 4afa1909…, 75e7abd9… | S1 descent; leaf tick on 'rot' ~0:25 |
| 3 | Hover A | 0:27–0:40 | 13 | 266fa333→4665bd7a | e6876f29…, 9b1e51d7… | Moss tunnel glide |
| 4 | S2 fires | 0:40–0:48 | 8 | e94b302e→0d109f6d | 9553b496…, a6b390f9… | Rise vault → log god-rays |
| 5 | Hover B raven+bear | 0:48–1:02 | 14 | 8dd34a3e→981ffe5b | ad8a691d…, 9905dc94… | Raven pond THEN bear gold pool hold |
| 6 | S3a lie | 1:02–1:05 | 3 | 0d109f6d crop | a6b390f9… | Almost still branch settle on 'lie' |
| 7 | Hover C river | 1:05–1:15 | 10 | 34019923 / clean creek | 114fd9fb…, e3c9b0d8…, e62e0491… | River/creek ONLY — no body reflection (use clean regen) |
| 8 | S3b wind+hold | 1:15–1:36 | 21 | 34019923→7ebae00a | b9a7b2d1…, 01e94881… | Lift+gust then long high canopy float |
| 9 | S4a bridge | 1:36–1:40 | 4 | ae0f7005 | d87bae70… | Push to bridge; stick-snap |
| 10 | Hover D cathedral | 1:40–1:53 | 13 | ae0f7005→d07dbd83 | 296e7e40… | Under arch cathedral tiers |
| 11 | S4b silence | 1:53–1:58 | 5 | d07dbd83 hold | 296e7e40… | Almost stop under arch |
| 12 | Hole | 1:58–2:10 | 12 | 266fa333 dark | 9b1e51d7… | Dark mist lock 12s |
| 13 | S5 dawn | 2:10–2:19 | 9 | 0d109f6d→27a2bbc5 | a6b390f9…, b1089f90… | Dawn rise rays |
| 14 | Dawn hold | 2:19–2:32 | 13 | 27a2bbc5 / 7ebae00a | 471e0f61…, b1089f90… | High slow endless |
| 15 | S6a seen | 2:32–2:36 | 4 | 50d1dd62 | 2db6d767… | Almost none (LOCKED photoreal 2db6d767) |
| 16 | Hover E | 2:36–2:44 | 8 | 27a2bbc5 | ca4f9102… | Drift forest looks back |
| 17 | S6b stare | 2:44–2:48 | 4 | 7ebae00a | fa9098a1…, b395fb45… | Near stop stare |
| 18 | Stare out | 2:48–2:57 | 9 | 7ebae00a widest | 6cb1d782…, b395fb45… | Hold + slight darken; end 2:57 |

## FULL VIDEO UUID CATALOG (download these from chat/assets)
| UUID | Dur | Role | Status |
|------|-----|------|--------|
| `466e437e-dcd7-4972-9e90-f80e6243007f` | 10s | Enter lead | user |
| `b044f7bf-0c89-4dff-b157-fea201609eee` | 10s | Enter mid/end | user |
| `4afa1909-e97b-4ab3-b800-e42013121860` | 10s | S1 0:18–0:27 | user |
| `75e7abd9-ee04-4071-ab98-b30d7f6ba385` | 15s | S1 descent aisle→creek (new) | gen |
| `e6876f29-7e70-4a4a-8e57-4eb26306f7b9` | 10s | Hover A moss arch | user |
| `9b1e51d7-af70-4681-ad70-41f5dec9b467` | 15s | Tunnel / Hole | user |
| `9553b496-967e-4c9b-a698-4da264713445` | 10s | S2 rise | user |
| `a6b390f9-1e43-41f0-9a3b-30e16d4411b4` | 10s | LOG GOD-RAYS (4/6/13) | user✓ |
| `ad8a691d-00ba-4f97-ba0c-7649098a36fd` | 10s | RAVEN pond | user✓ |
| `9905dc94-a3b4-4a88-966b-d4987ba01a16` | 15s | BEAR gold pool | user✓ |
| `e3c9b0d8-dcf6-417d-b456-e355d358805f` | 10s | River + spirit reflection | user |
| `114fd9fb-410b-4945-a1a2-fd4e042bf27d` | 10s | Clean creek NO body (regen) | gen |
| `e62e0491-3586-4639-89c6-8ba16a7e2156` | 10s | ALT clean river text-pipe | alt |
| `2287fe0b-c9d0-4c00-91fa-028369bfe2e7` | 10s | REJECTED halluci river | REJECT |
| `b9a7b2d1-31e1-4aaf-b457-5d8f61437966` | 15s | Shot 8b high canopy gust | gen |
| `01e94881-7d4d-4aca-8e4c-3217dce04285` | 15s | Shot 8c wide mist float | gen |
| `d87bae70-4989-4ad2-b302-61314359aa6f` | 10s | Bridge approach | user |
| `296e7e40-344a-4da7-8051-a492476125c0` | 15s | Under arch 10–11 | user |
| `471e0f61-fa69-4760-b6ef-62e3b0446132` | 15s | Dawn hold 14 | gen |
| `b1089f90-8903-4763-8bab-5ac6e7ebb401` | 15s | Dawn gold 2:15–2:30 | gen |
| `2db6d767-5c13-41c8-8ea2-6bd999a10cd5` | 10s | Shot 15 LOCKED photoreal | LOCKED |
| `68afeb32-f838-4825-815b-997a43941598` | 10s | REJECTED cartoon gold | REJECT |
| `ca4f9102-9e3c-49ef-8f69-7ba956959857` | 10s | Hover E 16 | gen |
| `fa9098a1-e6ef-474a-9f85-3384530033a5` | 10s | S6b stare 17 | gen |
| `b395fb45-fee9-4171-819f-225b1cabab76` | 15s | Stare 2:45–2:57 (trim 12s) | gen |
| `6cb1d782-1d54-48f5-b1ff-25014c7715ce` | 10s | Stare out 18 | gen |

## KEY STILLS (for Grok CLI image→video if you regenerate)
| Still UUID / name | Use for |
|------------------|---------|
| `7ebae00a-9325-47e6-9f45-38221c471d5d` | Enter / 8c / 17–18 wide mist canopy |
| `50d1dd62-19f9-44a8-856f-4d9ce8af824b` | Enter closer gold / Shot 15 |
| `27a2bbc5-f50a-4a0a-97a9-ea9200f907ec` | High canopy 8b / 14 / 16 |
| `34019923-cd85-4f09-a2de-b58d0d0beba0` | River (may contain spirit — strip for clean) |
| `596d6615-6235-4c82-a67d-3190b773bf1f` | Creek aisle (S1 descent + clean river source) |
| `d1d5df95-6494-4acd-b72e-fa26e8cdf509` | Dawn gold corridor |
| `248d733a-e7c1-496a-b5c1-a83a49ac16b2` | Stare aerial gold mist |
| `10d24a71 / 39087e19 / 447641cf` | Real PNW photo refs for photoreal texture |

## ASSEMBLY MATH (batch mode, no loop)
```
X = 2.0   # soft xfade seconds (pick 1.8–2.4)
# For 18 sequential shots with film durations D1..D18 (sum=177):
#   Make shot file i length = Di + X  for i=1..17
#   Make shot file 18 length = D18
#   Then chain with xfade duration X:
#   output_duration = sum(Li) - 17*X = 177
# If continuous source < needed length: DO NOT stretch — generate more or shorten window.
```

## FFMPEG BATCH RECIPE (local)
```bash
# 1) Normalize one source (trim only, never loop)
ffmpeg -y -ss START -i SRC.mp4 -t LEN \
  -vf "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,setsar=1,fps=24,format=yuv420p" \
  -an -c:v libx264 -crf 18 -preset medium -r 24 shotNN.mp4

# 2) Soft xfade two clips (da = duration of A)
ffmpeg -y -i A.mp4 -i B.mp4 -filter_complex \
  "[0:v][1:v]xfade=transition=fade:duration=2.0:offset=OFFSET[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -preset medium out.mp4
# OFFSET = duration(A) - 2.0

# 3) Batches then join: A=shots1-6, B=7-12, C=13-18
# 4) Mux + burn ASS
ffmpeg -y -i picture.mp4 -i MIX-v2.wav -t 177 \
  -vf "ass=lyrics.ass" -c:v libx264 -crf 18 -c:a aac -b:a 192k -shortest \
  11-the-forest-disease-vN.mp4
# Do NOT use -movflags +faststart in this env (can corrupt); local usually OK.
```

## GROK CLI WORKFLOW (in your local folder)
```
Suggested folder layout:
  kunz-poems/eleven-labs-mp3/11-forest-disease/
    audio/MIX-v2.wav
    subs/lyrics.ass
    timing/words.json
    stills/          # export map stills + PNW refs
    clips/           # download UUIDs from above
    shots/           # normalized film-length pieces
    batches/
    out/
    VIDEO-AI-MAP.md
    HANDOFF.md       # this file

Grok CLI prompts per missing/regen clip:
  "Animate this still [file]. " + GLOBAL PROMPT + shot-specific motion from map.
  duration 10 or 15 only (engine limits). Trim in ffmpeg after.
  For photoreal: attach real PNW ref photos + still; say solid trees no morph.

Assemble with ffmpeg batch script (above), not by asking the model to
loop-fill. Prefer many short continuous clips soft-xfaded over one long fake.
```

## STORY BEATS THAT MUST NOT BE WRONG
| Beat | Clock | Must show |
|------|-------|-----------|
| Raven | ~0:48–0:55 | Raven at pond (`ad8a691d`) |
| Bear | ~0:52–1:02 | Bear overhead gold pool (`9905dc94`) |
| Log rays | 0:40–0:48 & dawn | `a6b390f9` |
| Clean river | 1:05–1:15 | Water only — **no body** (`114fd9fb` preferred) |
| Lie | 1:02–1:05 | Almost still |
| Bridge | 1:36+ | `d87bae70` / under arch `296e7e40` |
| Shot 15 | 2:32–2:36 | Photoreal canopy `2db6d767` LOCKED |
| End | 2:48–2:57 | High stare, slight darken, picture lock 2:57 |

## DELIVERABLE SPEC
```
11-the-forest-disease-vN.mp4
  1280×720, 24 fps, 177.00 s
  video: continuous soft-xfade motion only
  audio: MIX-v2
  subs: lyrics.ass burned (or soft-sub if you prefer)
```

## WHAT WAS FAILING IN-CHAT (so you avoid it)
- Long single ffmpeg jobs timing out mid-stitch
- Loop/setpts fill to fake length (you correctly banned this)
- Animating wrong still type (canopy still + 'river' prompt → hallucination)
- Cartoon gold / morphing without real PNW reference photos
- Recycling same B-roll across unrelated beats (broke raven/bear timing)

## QUICK START CHECKLIST
- [ ] Copy MIX-v2 + lyrics.ass + timing JSON into local 11-forest-disease/
- [ ] Download all non-REJECT video UUIDs into clips/
- [ ] Download stills listed above into stills/
- [ ] Confirm raven/bear/log/clean-river clips by eye
- [ ] Build shot files = film length (+ xfade pad), trim only
- [ ] Soft-xfade batches A/B/C → picture
- [ ] Mux audio + ASS → 177s master
- [ ] Spot-check clocks vs words.json for S1/raven/bear/lie/bridge/end
