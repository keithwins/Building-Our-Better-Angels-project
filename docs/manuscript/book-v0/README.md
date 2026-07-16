# Book v0 — forked working draft

**Title:** *Building Our Better Angels*  
**Lane:** `book-v0`  
**Build stamp:** `260713`  
**Status:** scaffold for coffee-shop reading and free revision

This directory is a **forked reading sequence**, not the corpus.

Sections under `sections/` may be rewritten without concern for damaging
essays, charters, or mission docs. Corpus originals remain the provenance home
until an explicit later merge.

The trusted invitation reader
(`../reader-v0/sections-trusted/`) is the tone reference: inviting, non-recruiting,
clear, able to hold humor and seriousness together. It is also the freshest
record of how the project currently wants to sound.

## Opening posture

This draft does **not** begin by justifying a project or staging a philosophical
seminar about fog.

It begins because a response to *what now?* was required — in a moment where
older domination presses from one side, a new kind of intelligence enters from
another, and we remain misaligned and unevenly resourced. Reflexivity follows
from that attempt to help inside the weather, not the other way around.

## Layout

| Path | Role |
|---|---|
| `sections/` | Editable forked chapter copies + front/back matter |
| `bridges/` | Short connective tissue between chapters |
| `SOURCE_MAP.md` | What each section was forked from |
| `build/` | Generated concatenated Markdown |
| `print/` | Generated HTML (and PDF when a browser is available) |
| `tools/` | Print HTML/PDF builders |
| `build-book-v0.sh` | Reproducible Markdown assembly |

## Edit here, not the build

**Source of truth for prose:** `sections/` and `bridges/` only.

`build/building-our-better-angels-book-v0-*.md` and `print/*` are generated.
Editing them will be overwritten on the next rebuild, and stale editor buffers
of the Markdown build are how deleted editorial sections keep reappearing.

```bash
bash build-book-v0.sh
bash tools/build-print-pdf.sh
```

Open `print/building-our-better-angels-book-v0-*.html` in a browser for a
letter-sized print preview, or use the PDF the script writes beside it.
Suggested coffee-shop print: duplex, 2-up landscape ≈65% scale → ~20 sheets at
~80 pages.
