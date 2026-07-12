#!/usr/bin/env python3
"""Build a browser-printable trusted-reader HTML edition."""

from __future__ import annotations

import importlib.util
import os
import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections-trusted"
MANUSCRIPT = ROOT.parent
BUILD_STAMP = os.environ.get("BUILD_STAMP", "260711")
OUT = ROOT / "print" / f"building-our-better-angels-trusted-reader-v0-{BUILD_STAMP}.html"

_TONIGHT_PATH = ROOT / "tools" / "build-tonight-edition.py"
_spec = importlib.util.spec_from_file_location("build_tonight_edition", _TONIGHT_PATH)
assert _spec and _spec.loader
tonight = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tonight)


def build() -> None:
    sections = [
        (
            "prologue",
            "Prologue: The Door In The Fog",
            tonight.clean_prologue(tonight.read(MANUSCRIPT / "00-prologue-the-door-in-the-fog.md")),
            "prologue",
        ),
        (
            "note",
            "A Note on This Copy",
            tonight.strip_first_h1(tonight.read(SECTIONS / "01-a-note-on-this-copy.md")),
            "frontmatter",
        ),
        (
            "name",
            "Building Our Better Angels",
            tonight.strip_first_h1(tonight.read(SECTIONS / "02-the-name-better-angels.md")),
            "frontmatter",
        ),
        (
            "map",
            "A Map of the Book",
            tonight.strip_first_h1(tonight.read(SECTIONS / "03-chapter-spine.md")),
            "map",
        ),
        (
            "seeds",
            "From the Fog to the Door",
            tonight.strip_first_h1(tonight.read(SECTIONS / "04-from-the-fog-to-the-door.md")),
            "seeds",
        ),
        (
            "remaining",
            "Open Questions",
            tonight.strip_first_h1(tonight.read(SECTIONS / "05-remaining-questions.md")),
            "backmatter",
        ),
        (
            "appendix-g",
            "Appendix G: Source Notes",
            tonight.strip_first_h1(tonight.read(SECTIONS / "appendix-g-manuscript-lineage.md")),
            "backmatter",
        ),
    ]

    contents = "\n".join(
        f'<li><a href="#{section_id}">{html.escape(title)}</a></li>'
        for section_id, title, _, _ in sections
    )
    body = "\n\n".join(
        tonight.section(section_id, title, markdown, classes)
        for section_id, title, markdown, classes in sections
    )

    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Building Our Better Angels: Trusted Reader v0 {BUILD_STAMP}</title>
  <style>{tonight.css()}</style>
</head>
<body>
  <main class="book">
    <section class="title-page">
      <div class="eyebrow">Trusted-reader edition / reader-v0 / {BUILD_STAMP}</div>
      <div>
        <h1>Building Our Better Angels</h1>
        <h2>An Invitation Reader</h2>
        <p class="motto">A door in the fog; not the finished house.</p>
      </div>
      <div class="stamp">
        <span>Trusted-reader copy: read, mark, respond.</span>
        <span>Not a public release or finished manuscript.</span>
        <span>Built from docs/manuscript/reader-v0/sections-trusted/.</span>
      </div>
    </section>

    <nav class="contents" aria-label="Contents">
      <h2>Contents</h2>
      <ol>
        {contents}
      </ol>
    </nav>

    <div class="reading-note">
      This edition is prepared for a trusted outside reader: prologue first, book
      voice throughout, and honest naming of what is still unfinished.
    </div>

    {body}

    <footer class="colophon">
      Built by reader-v0/tools/build-trusted-edition.py from trusted-reader section sources.
    </footer>
  </main>
</body>
</html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(document, encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    build()
