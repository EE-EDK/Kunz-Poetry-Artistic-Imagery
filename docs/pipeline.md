# Pipeline

One poem at a time. Text is already in the folder. Everything else is a file
you either generate here or pull from a local export.

```
transcript.txt
    → ElevenLabs voice          → audio/elevenlabs/
    → forced alignment          → timing/*.json + *.srt
music / epidemic / sfx          → audio/{music,epidemic,sfx}/ → mix/
poem text → stills (Grok CLI)   → images/
stills or existing mp4 + SRT    → video/NN-slug-lyrics.mp4
```

On-screen words are a subtitle burn from `timing/*.srt`. They are not a
separate script. If the SRT is wrong, re-align; do not nudge timestamps by
hand unless a single cue is visibly off after a listening pass.
