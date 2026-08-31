"""Single source of truth for project paths. Root-relative so the folder is portable."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SRC = ROOT / "src"
SCRIPTS = ROOT / "scripts"
TEXTS = ROOT / "texts"
POEMS = ROOT / "poems"
INBOX = ROOT / "inbox"
DOCS = ROOT / "docs"
DOCS_DEV = ROOT / "docs_dev"
OUTPUT = ROOT / "output"

CATALOG = SRC / "catalog.json"
POEMS_MD = TEXTS / "shadowshining-selected-poems.md"

AUDIO_SUBDIRS = ("elevenlabs", "music", "sfx", "epidemic", "mix")
POEM_SUBDIRS = ("audio", "timing", "images", "video", "inbox")

_ff_candidates = [
    Path.home() / "Downloads" / "ffmpeg-8.1.1-full_build" / "bin" / "ffmpeg.exe",
]
FFMPEG = shutil.which("ffmpeg") or next((str(c) for c in _ff_candidates if c.is_file()), "ffmpeg")

_fp_candidates = [
    Path.home() / "Downloads" / "ffmpeg-8.1.1-full_build" / "bin" / "ffprobe.exe",
]
FFPROBE = shutil.which("ffprobe") or next((str(c) for c in _fp_candidates if c.is_file()), "ffprobe")

_grok_candidates = [
    Path.home() / ".grok" / "bin" / "grok.exe",
    Path.home() / ".grok" / "bin" / "grok",
]
GROK = shutil.which("grok") or next((str(c) for c in _grok_candidates if c.is_file()), "grok")


def poem_dir(folder: str) -> Path:
    return POEMS / folder
