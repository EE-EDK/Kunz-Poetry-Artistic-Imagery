# Hub publish — twenty-five films, one showing

This repo is **25 independent poem-films**. The public page is
https://kunz-ai-hub.tailb1d0b7.ts.net/p/shadowshining-selected-poems/

When a `*FINAL*.mp4` is ready, publish it onto kunzhub (do not leave it
only in this tree):

1. Transcode a web copy into
   `Self-Host/sites/kunzhub/pages/public/poems-by-ethank/media/films/<slug>.mp4`
2. Add the poem html file to that page's `_build/films.json`
3. Run `python3 apply_film.py`

That replaces the poem's top image (if there is one) with a still that
looks ready to play. Click → fullscreen. Ended → back to the 25-poem
page. Early exit stays on the poem.

Masters stay Git LFS here. Web copies are gitignored on kunzhub. New
take = new filename (Caddy caches mp4 for a week). Full procedure:
`GROK.md` → Hub publish.
