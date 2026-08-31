"""Create the 25-poem tree and file existing Downloads artifacts into it."""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import paths  # noqa: E402

POEMS_MD_CANDIDATES = [
    paths.POEMS_MD,
    ROOT / "shadowshining-selected-poems.md",
]

# Known incoming artifacts from the Downloads dump (source name -> dest under poem folder).
FILE_MAP = [
    ("1_A-tree-through-the-forrest.wav", "01-a-tree-through-the-forest", "audio/elevenlabs"),
    ("1_A-tree-through-the-forrest.alignment.json", "01-a-tree-through-the-forest", "timing"),
    ("1_A-tree-through-the-forrest.srt", "01-a-tree-through-the-forest", "timing"),
    ("01_A_Tree_Through_the_Forest_FULL.mp4", "01-a-tree-through-the-forest", "video"),
    ("01_A_Tree_Through_the_Forest_v3_smooth.mp4", "01-a-tree-through-the-forest", "video"),
    ("01_A_Tree_Through_the_Forest_v4_seamless.mp4", "01-a-tree-through-the-forest", "video"),
    ("01_A_Tree_Through_the_Forest_FINAL.mp4", "01-a-tree-through-the-forest", "video"),
    ("Murdered-Mind-voice.mp3", "02-murdered-mind", "audio/elevenlabs"),
    ("Murdered-Mind-voice.alignment.json", "02-murdered-mind", "timing"),
    ("Murdered-Mind-voice.srt", "02-murdered-mind", "timing"),
    ("Murdered-Mind-music.wav", "02-murdered-mind", "audio/music"),
    ("Apocolyte-voice.mp3", "03-apoclyte", "audio/elevenlabs"),
    ("Apocolyte-voice.alignment.json", "03-apoclyte", "timing"),
    ("Apocolyte-voice.srt", "03-apoclyte", "timing"),
]


def slugify(title: str) -> str:
    s = title.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def parse_poems(markdown: str) -> list[dict]:
    poems = []
    parts = re.split(r"^## ", markdown, flags=re.MULTILINE)
    n = 0
    for part in parts[1:]:
        lines = part.strip().splitlines()
        if not lines:
            continue
        n += 1
        title = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        body = re.sub(r"^---\s*$", "", body, flags=re.MULTILINE).strip()
        slug = slugify(title)
        folder = f"{n:02d}-{slug}"
        poems.append(
            {
                "id": n,
                "title": title,
                "slug": slug,
                "folder": folder,
                "transcript": f"{title}\n\n{body}".strip(),
            }
        )
    return poems


def spoken_words(alignment: dict) -> list[dict]:
    out = []
    for word in alignment.get("words") or []:
        text = (word.get("text") or "").strip()
        if not text:
            continue
        out.append(
            {
                "text": text,
                "start": word.get("start"),
                "end": word.get("end"),
                "loss": word.get("loss"),
            }
        )
    return out


def srt_timestamp(seconds: float) -> str:
    if seconds is None or seconds < 0:
        seconds = 0.0
    ms = int(round(float(seconds) * 1000))
    hours, ms = divmod(ms, 3_600_000)
    minutes, ms = divmod(ms, 60_000)
    secs, ms = divmod(ms, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"


def words_to_srt(words: list[dict], max_chars: int = 42) -> str:
    cues: list[str] = []
    idx = 1
    buf: list[dict] = []
    char_count = 0

    def flush() -> None:
        nonlocal idx, buf, char_count
        if not buf:
            return
        start = buf[0]["start"] or 0.0
        end = buf[-1]["end"] or start
        if end <= start:
            end = start + 0.05
        text = " ".join(w["text"] for w in buf).strip()
        if text:
            cues.append(f"{idx}\n{srt_timestamp(start)} --> {srt_timestamp(end)}\n{text}\n")
            idx += 1
        buf = []
        char_count = 0

    for word in words:
        token = word["text"]
        extra = len(token) + (1 if buf else 0)
        if buf and char_count + extra > max_chars:
            flush()
        buf.append(word)
        char_count += extra
        if token.endswith((".", "?", "!")):
            flush()
    flush()
    return "\n".join(cues) + ("\n" if cues else "")


def write_poem_md(poem: dict, dest: Path) -> None:
    body = poem["transcript"].split("\n\n", 1)
    title = poem["title"]
    rest = body[1] if len(body) > 1 else ""
    dest.write_text(
        f"# {title}\n\n*Shadowshining · {poem['id']:02d}*\n\n{rest}\n",
        encoding="utf-8",
    )


def ensure_tree(folder: str) -> Path:
    base = paths.POEMS / folder
    for sub in paths.POEM_SUBDIRS:
        (base / sub).mkdir(parents=True, exist_ok=True)
    for audio_sub in paths.AUDIO_SUBDIRS:
        (base / "audio" / audio_sub).mkdir(parents=True, exist_ok=True)
    return base


def move_if_exists(src: Path, dest_dir: Path) -> None:
    if not src.exists():
        return
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    if dest.exists() and dest.resolve() == src.resolve():
        return
    if dest.exists():
        print(f"  keep existing {dest}")
        return
    shutil.move(str(src), str(dest))
    print(f"  moved {src.name} -> {dest_dir.relative_to(ROOT)}")


def catalog_entry(poem: dict) -> dict:
    base = paths.POEMS / poem["folder"]

    def nonempty(rel: str) -> bool:
        p = base / rel
        if not p.exists():
            return False
        if p.is_file():
            return True
        return any(p.iterdir())

    return {
        "id": poem["id"],
        "title": poem["title"],
        "slug": poem["slug"],
        "folder": poem["folder"],
        "status": {
            "elevenlabs": nonempty("audio/elevenlabs"),
            "music": nonempty("audio/music"),
            "sfx": nonempty("audio/sfx"),
            "epidemic": nonempty("audio/epidemic"),
            "mix": nonempty("audio/mix"),
            "timing": nonempty("timing"),
            "images": nonempty("images"),
            "video": nonempty("video"),
        },
    }


def main() -> int:
    md_path = next((p for p in POEMS_MD_CANDIDATES if p.exists()), None)
    if md_path is None:
        print("Missing shadowshining-selected-poems.md", file=sys.stderr)
        return 1

    paths.SRC.mkdir(exist_ok=True)
    paths.SCRIPTS.mkdir(exist_ok=True)
    paths.TEXTS.mkdir(exist_ok=True)
    paths.POEMS.mkdir(exist_ok=True)
    paths.INBOX.mkdir(exist_ok=True)
    paths.DOCS.mkdir(exist_ok=True)
    paths.DOCS_DEV.mkdir(exist_ok=True)
    paths.OUTPUT.mkdir(exist_ok=True)
    (paths.INBOX / "elevenlabs").mkdir(exist_ok=True)
    (paths.INBOX / "music").mkdir(exist_ok=True)
    (paths.INBOX / "sfx").mkdir(exist_ok=True)
    (paths.INBOX / "epidemic").mkdir(exist_ok=True)
    (paths.INBOX / "images").mkdir(exist_ok=True)
    (paths.INBOX / "video").mkdir(exist_ok=True)
    (paths.INBOX / "README.md").write_text(
        "Drop new local artifacts here. File them into `poems/NN-slug/...` "
        "by poem — do not leave production media in this inbox.\n",
        encoding="utf-8",
    )

    if md_path.resolve() != paths.POEMS_MD.resolve():
        paths.POEMS_MD.parent.mkdir(parents=True, exist_ok=True)
        if not paths.POEMS_MD.exists():
            shutil.move(str(md_path), str(paths.POEMS_MD))

    poems = parse_poems(paths.POEMS_MD.read_text(encoding="utf-8"))
    if len(poems) != 25:
        print(f"WARNING: expected 25 poems, parsed {len(poems)}")

    for poem in poems:
        base = ensure_tree(poem["folder"])
        write_poem_md(poem, base / "poem.md")
        (base / "transcript.txt").write_text(poem["transcript"] + "\n", encoding="utf-8")

    for name, folder, rel in FILE_MAP:
        move_if_exists(ROOT / name, paths.POEMS / folder / rel)

    sfx_dir = ROOT / "Murdered-Mind-Sound-Effect"
    dest_epidemic = paths.POEMS / "02-murdered-mind" / "audio" / "epidemic"
    if sfx_dir.exists() and sfx_dir.is_dir():
        dest_epidemic.mkdir(parents=True, exist_ok=True)
        for wav in sfx_dir.glob("*"):
            if wav.name.lower() == "desktop.ini" or wav.suffix.lower() not in {".wav", ".mp3", ".flac", ".aiff"}:
                continue
            move_if_exists(wav, dest_epidemic)
        try:
            sfx_dir.rmdir()
        except OSError:
            pass

    # Compact spoken-word JSON + cleaned SRT next to each alignment dump.
    for alignment_path in paths.POEMS.glob("*/timing/*.alignment.json"):
        data = json.loads(alignment_path.read_text(encoding="utf-8"))
        spoken = spoken_words(data)
        words_path = alignment_path.with_name(alignment_path.name.replace(".alignment.json", ".words.json"))
        words_path.write_text(json.dumps(spoken, indent=2), encoding="utf-8")
        srt_path = alignment_path.with_suffix("").with_suffix(".srt")
        # *.alignment.json -> stem "foo.alignment"; with_suffix(".srt") = foo.alignment.srt
        srt_path = alignment_path.parent / (alignment_path.name.replace(".alignment.json", ".srt"))
        srt_path.write_text(words_to_srt(spoken), encoding="utf-8")

    catalog = {
        "collection": "Shadowshining",
        "subtitle": "Selected poems, 2009–2025",
        "poem_count": len(poems),
        "poems": [catalog_entry(p) for p in poems],
    }
    paths.CATALOG.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    print(f"catalog: {len(poems)} poems -> {paths.CATALOG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
