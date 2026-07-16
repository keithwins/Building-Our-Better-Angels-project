#!/usr/bin/env python3
"""Build a browser-printable HTML edition of book-v0."""

from __future__ import annotations

import html
import importlib.util
import os
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"
BRIDGES = ROOT / "bridges"
BUILD_STAMP = os.environ.get("BUILD_STAMP", "260713")
PDF_NAME = f"building-our-better-angels-book-v0-{BUILD_STAMP}.pdf"
OUT = ROOT / "print" / f"building-our-better-angels-book-v0-{BUILD_STAMP}.html"
BUILD_TZ = ZoneInfo(os.environ.get("BUILD_TZ", "America/New_York"))

_READER_TONIGHT = (
    ROOT.parent / "reader-v0" / "tools" / "build-tonight-edition.py"
)
_spec = importlib.util.spec_from_file_location("build_tonight_edition", _READER_TONIGHT)
assert _spec and _spec.loader
tonight = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tonight)


def strip_fork_comments(text: str) -> str:
    return re.sub(r"^<!--.*?-->\s*\n?", "", text, flags=re.M | re.S)


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def load_piece(path: Path) -> tuple[str, str]:
    raw = strip_fork_comments(tonight.read(path))
    title = first_heading(raw)
    body = tonight.strip_first_h1(raw)
    return title, body


def header_label(built_at: datetime) -> str:
    stamp = built_at.strftime("%Y-%m-%d %H:%M %Z")
    return f"Building Our Better Angels · {PDF_NAME} · {stamp}"


def build() -> None:
    built_at = datetime.now(BUILD_TZ)
    running_header = header_label(built_at)
    sequence: list[tuple[str, Path, str]] = [
        ("title", SECTIONS / "00-title-and-status.md", "frontmatter"),
        ("why", SECTIONS / "01-why-we-are-here.md", "frontmatter"),
        ("name", SECTIONS / "03-the-name.md", "frontmatter"),
        ("map", SECTIONS / "04-a-map.md", "frontmatter"),
        ("prologue", SECTIONS / "10-prologue-the-door-in-the-fog.md", "prologue"),
        ("bridge-15", BRIDGES / "15-into-the-fog.md", "bridge"),
        ("fog", SECTIONS / "20-the-fog.md", "chapter"),
        ("bridge-25", BRIDGES / "25-into-the-wobbly-edge.md", "bridge"),
        ("edge", SECTIONS / "30-the-wobbly-edge.md", "chapter"),
        ("bridge-32", BRIDGES / "32-into-the-multitude.md", "bridge"),
        ("multitude", SECTIONS / "35-the-multitude.md", "chapter"),
        ("bridge-37", BRIDGES / "37-into-companionship.md", "bridge"),
        ("companionship", SECTIONS / "40-accountable-companionship.md", "chapter"),
        ("bridge-45", BRIDGES / "45-into-scores.md", "bridge"),
        ("scores", SECTIONS / "50-scores-not-leashes.md", "chapter"),
        ("bridge-55", BRIDGES / "55-into-trust.md", "bridge"),
        ("trust", SECTIONS / "60-trust-further-than-you-can-throw.md", "chapter"),
        ("bridge-65", BRIDGES / "65-into-memory.md", "bridge"),
        ("memory", SECTIONS / "70-memory-that-cannot-quietly-lie.md", "chapter"),
        ("bridge-75", BRIDGES / "75-into-the-mirror.md", "bridge"),
        ("mirror", SECTIONS / "80-the-lively-mirror.md", "chapter"),
        ("bridge-85", BRIDGES / "85-into-elderhood.md", "bridge"),
        ("elderhood", SECTIONS / "90-a-life-can-narrow-a-life-can-open.md", "chapter"),
        ("bridge-95", BRIDGES / "95-into-aflutter.md", "bridge"),
        ("aflutter", SECTIONS / "a0-asterism-aflutter.md", "chapter"),
        ("bridge-a5", BRIDGES / "a5-into-social-protocol.md", "bridge"),
        ("social", SECTIONS / "b0-the-social-protocol.md", "chapter"),
        ("bridge-b5", BRIDGES / "b5-into-collaborative-surface.md", "bridge"),
        ("surface", SECTIONS / "c0-the-collaborative-surface.md", "chapter"),
        ("bridge-d5", BRIDGES / "d5-toward-eclosion.md", "bridge"),
        ("eclosion", SECTIONS / "e0-eclosion.md", "backmatter"),
    ]

    pieces: list[tuple[str, str, str, str]] = []
    for section_id, path, classes in sequence:
        title, body = load_piece(path)
        pieces.append((section_id, title, body, classes))

    # Contents lists substantive stops; bridges stay in the flow but not the TOC.
    toc = "\n".join(
        f'<li><a href="#{section_id}">{html.escape(title)}</a></li>'
        for section_id, title, _, classes in pieces
        if classes != "bridge"
    )
    body_html = "\n\n".join(
        tonight.section(section_id, title, markdown, classes)
        for section_id, title, markdown, classes in pieces
    )

    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Building Our Better Angels: Book v0 {BUILD_STAMP}</title>
  <style>{tonight.css()}
.bridge {{
  margin-top: 2.4rem;
}}
.bridge > h1 {{
  font-size: 1.35rem;
  color: var(--accent);
  font-style: italic;
  font-weight: 400;
}}
.bridge .chapter-kicker::after {{
  content: " / bridge";
}}
.print-chrome {{
  display: none;
}}
@media screen {{
  .print-chrome {{
    display: block;
    margin: 0 auto 1rem;
    width: min(100%, 8.2in);
    padding: 0.55rem 0.72in 0;
    color: var(--muted);
    font-family: "Gill Sans", "Optima", "Avenir Next", sans-serif;
    font-size: 0.72rem;
    letter-spacing: 0.04em;
  }}
  .print-chrome .screen-footer {{
    margin-top: 0.35rem;
    opacity: 0.75;
  }}
}}
@media print {{
  .bridge {{
    break-before: avoid;
    break-inside: avoid;
    margin-top: 1.6rem;
  }}
  .bridge + .chapter {{
    break-before: page;
  }}

  /* Prefer @page margin boxes so every sheet carries identity + page number. */
  @page {{
    size: letter;
    margin: 0.92in 0.78in 0.95in;

    @top-center {{
      content: "{html.escape(running_header)}";
      color: #6c5a45;
      font-family: "Gill Sans", "Optima", "Avenir Next", sans-serif;
      font-size: 7.5pt;
      letter-spacing: 0.02em;
      vertical-align: bottom;
      padding-bottom: 0.22in;
    }}

    @bottom-center {{
      content: counter(page) " / " counter(pages);
      color: #6c5a45;
      font-family: "Gill Sans", "Optima", "Avenir Next", sans-serif;
      font-size: 9pt;
      vertical-align: top;
      padding-top: 0.18in;
    }}
  }}

  .title-page {{
    /* Title sheet keeps the chrome; later pages rely on margin boxes. */
  }}
}}
</style>
</head>
<body>
  <div class="print-chrome" aria-hidden="true">
    <div class="screen-header">{html.escape(running_header)}</div>
    <div class="screen-footer">Page numbers appear on the printed/PDF pages (n / total).</div>
  </div>
  <main class="book">
    <section class="title-page">
      <div class="eyebrow">Coffee-shop draft / book-v0 / {BUILD_STAMP}</div>
      <div>
        <h1>Building Our Better Angels</h1>
        <h2>Book v0</h2>
        <p class="motto">A forked reading sequence. Editable. Not the finished house.</p>
      </div>
      <div class="stamp">
        <span>Print duplex, mark freely, revise in sections/.</span>
        <span>Mara and the cedar box live later, in Asterism Aflutter.</span>
        <span>Built from docs/manuscript/book-v0.</span>
      </div>
    </section>

    <nav class="contents" aria-label="Contents">
      <h2>Contents</h2>
      <ol>
        {toc}
      </ol>
    </nav>

    <div class="reading-note">
      This is the working book fork: front matter, bridges, and chapter drafts in
      reading order. Some chapters still speak essay- or charter-voice; the print
      packet is for marking where invitation prose still needs to arrive.
    </div>

    {body_html}

    <footer class="colophon">
      Built by book-v0/tools/build-print-edition.py · stamp {BUILD_STAMP}
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
