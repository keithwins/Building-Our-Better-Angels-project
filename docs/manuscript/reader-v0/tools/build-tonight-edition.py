#!/usr/bin/env python3
"""Build a browser-printable, book-like HTML reading copy for tonight."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT.parent
OUT = ROOT / "print" / "building-our-better-angels-tonight-reader-v0-260707.html"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_source_notes(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    skipping = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("_Source refs:") or stripped.startswith("_Reader-v0 source note:"):
            skipping = True
            if stripped.endswith("._"):
                skipping = False
            continue
        if skipping:
            if stripped.endswith("._"):
                skipping = False
            continue
        out.append(line)
    return "\n".join(out).strip() + "\n"


def strip_first_h1(text: str) -> str:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[:idx] + lines[idx + 1 :]).strip() + "\n"
    return text.strip() + "\n"


def clean_prologue(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    skipped_meta = False
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if idx == 0 and line.startswith("# "):
            idx += 1
            continue
        if not skipped_meta and line.startswith("**Status:**"):
            while idx < len(lines) and lines[idx].strip() != "---":
                idx += 1
            if idx < len(lines) and lines[idx].strip() == "---":
                idx += 1
            skipped_meta = True
            continue
        out.append(line)
        idx += 1
    return "\n".join(out).strip() + "\n"


def inline(text: str) -> str:
    code_spans: list[str] = []

    def stash_code(match: re.Match[str]) -> str:
        code_spans.append(html.escape(match.group(1)))
        return f"@@CODE{len(code_spans) - 1}@@"

    text = re.sub(r"`([^`]+)`", stash_code, text)
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"_([^_\n]+)_", r"<em>\1</em>", escaped)
    for idx, code in enumerate(code_spans):
        escaped = escaped.replace(f"@@CODE{idx}@@", f"<code>{code}</code>")
    return escaped


def is_table_separator(line: str) -> bool:
    return bool(re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", line))


def parse_table(lines: list[str], idx: int) -> tuple[str, int]:
    headers = [cell.strip() for cell in lines[idx].strip().strip("|").split("|")]
    idx += 2
    rows: list[list[str]] = []
    while idx < len(lines) and "|" in lines[idx] and lines[idx].strip():
        rows.append([cell.strip() for cell in lines[idx].strip().strip("|").split("|")])
        idx += 1

    head = "".join(f"<th>{inline(cell)}</th>" for cell in headers)
    body = []
    for row in rows:
        body.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in row) + "</tr>")
    table = "<table><thead><tr>" + head + "</tr></thead><tbody>" + "".join(body) + "</tbody></table>"
    return table, idx


def render_markdown(text: str) -> str:
    lines = text.splitlines()
    idx = 0
    out: list[str] = []

    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()

        if not stripped or stripped.startswith("<!--"):
            idx += 1
            continue

        if stripped == "---":
            out.append("<hr>")
            idx += 1
            continue

        if re.match(r"^#{1,6}\s+", line):
            level = len(line) - len(line.lstrip("#"))
            title = line[level:].strip()
            out.append(f"<h{level}>{inline(title)}</h{level}>")
            idx += 1
            continue

        if idx + 1 < len(lines) and "|" in line and is_table_separator(lines[idx + 1]):
            table, idx = parse_table(lines, idx)
            out.append(table)
            continue

        if stripped.startswith(">"):
            quote_lines = []
            while idx < len(lines) and lines[idx].strip().startswith(">"):
                quote_lines.append(lines[idx].strip()[1:].strip())
                idx += 1
            out.append("<blockquote><p>" + inline(" ".join(quote_lines)) + "</p></blockquote>")
            continue

        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while idx < len(lines) and re.match(r"^\s*[-*]\s+", lines[idx]):
                item = re.sub(r"^\s*[-*]\s+", "", lines[idx]).strip()
                idx += 1
                while idx < len(lines):
                    continuation = lines[idx]
                    if not continuation.strip():
                        idx += 1
                        break
                    if re.match(r"^\s*[-*]\s+", continuation) or re.match(r"^\s*\d+\.\s+", continuation):
                        break
                    if continuation.startswith(" ") or continuation.startswith("\t"):
                        item += " " + continuation.strip()
                        idx += 1
                        continue
                    break
                items.append(item)
            out.append("<ul>" + "".join(f"<li>{inline(item)}</li>" for item in items) + "</ul>")
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while idx < len(lines) and re.match(r"^\s*\d+\.\s+", lines[idx]):
                item = re.sub(r"^\s*\d+\.\s+", "", lines[idx]).strip()
                idx += 1
                while idx < len(lines):
                    continuation = lines[idx]
                    if not continuation.strip():
                        idx += 1
                        break
                    if re.match(r"^\s*[-*]\s+", continuation) or re.match(r"^\s*\d+\.\s+", continuation):
                        break
                    if continuation.startswith(" ") or continuation.startswith("\t"):
                        item += " " + continuation.strip()
                        idx += 1
                        continue
                    break
                items.append(item)
            out.append("<ol>" + "".join(f"<li>{inline(item)}</li>" for item in items) + "</ol>")
            continue

        para = [stripped]
        idx += 1
        while idx < len(lines):
            next_line = lines[idx]
            next_stripped = next_line.strip()
            if not next_stripped:
                idx += 1
                break
            if (
                next_stripped == "---"
                or next_stripped.startswith(">")
                or re.match(r"^#{1,6}\s+", next_line)
                or re.match(r"^\s*[-*]\s+", next_line)
                or re.match(r"^\s*\d+\.\s+", next_line)
                or (idx + 1 < len(lines) and "|" in next_line and is_table_separator(lines[idx + 1]))
            ):
                break
            para.append(next_stripped)
            idx += 1
        out.append("<p>" + inline(" ".join(para)) + "</p>")

    return "\n".join(out)


def section(section_id: str, title: str, markdown: str, classes: str = "") -> str:
    return f"""
<section id="{section_id}" class="chapter {classes}">
  <div class="chapter-kicker">Building Our Better Angels</div>
  <h1>{html.escape(title)}</h1>
  {render_markdown(markdown)}
</section>
""".strip()


def css() -> str:
    return """
:root {
  --paper: #f8f0df;
  --paper-deep: #efe1c5;
  --ink: #241a12;
  --muted: #6c5a45;
  --faint: #9a876d;
  --rule: #d7c3a1;
  --accent: #8f3d1f;
  --accent-soft: #b46336;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  color: var(--ink);
  background:
    radial-gradient(circle at 10% 0%, rgba(180, 99, 54, 0.14), transparent 28rem),
    linear-gradient(135deg, #d9c49c 0%, #efe2c7 42%, #c7d0bd 100%);
  font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Georgia, serif;
  font-size: 18px;
  line-height: 1.58;
}

.book {
  width: min(100%, 8.2in);
  margin: 2rem auto;
  padding: 0.72in;
  background:
    linear-gradient(90deg, rgba(95, 65, 36, 0.045), transparent 1.2rem),
    var(--paper);
  box-shadow: 0 2rem 4rem rgba(52, 34, 16, 0.28);
}

.title-page {
  min-height: 8.6in;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid var(--rule);
  padding: 0.72in 0.62in;
  background:
    radial-gradient(circle at 90% 8%, rgba(143, 61, 31, 0.13), transparent 11rem),
    linear-gradient(180deg, rgba(255, 255, 255, 0.34), transparent 45%);
}

.eyebrow,
.chapter-kicker,
.colophon {
  color: var(--muted);
  font-family: "Gill Sans", "Optima", "Avenir Next", sans-serif;
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.title-page h1 {
  max-width: 5.7in;
  margin: 1.7in 0 0;
  font-size: clamp(3.4rem, 9vw, 5.7rem);
  line-height: 0.92;
  letter-spacing: -0.055em;
}

.title-page h2 {
  margin: 1.2rem 0 0;
  color: var(--accent);
  font-size: 1.35rem;
  font-style: italic;
  font-weight: 400;
}

.title-page .motto {
  max-width: 4.4in;
  margin: 2rem 0 0;
  color: var(--muted);
  font-size: 1.15rem;
  font-style: italic;
}

.title-page .stamp {
  display: grid;
  gap: 0.28rem;
  color: var(--muted);
  font-size: 0.88rem;
}

.contents {
  margin: 3rem 0 4rem;
  padding: 1.4rem 1.5rem;
  border-top: 2px solid var(--ink);
  border-bottom: 1px solid var(--rule);
}

.contents h2 {
  margin: 0 0 1rem;
  color: var(--accent);
  font-family: "Gill Sans", "Optima", "Avenir Next", sans-serif;
  font-size: 0.82rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}

.contents ol {
  margin: 0;
  padding-left: 1.3rem;
}

.contents li { margin: 0.35rem 0; }
.contents a { color: var(--ink); text-decoration: none; }

.chapter {
  margin: 4.5rem 0 0;
}

.chapter > h1 {
  margin: 0.18rem 0 1.45rem;
  font-size: clamp(2rem, 5vw, 3.15rem);
  line-height: 1.03;
  letter-spacing: -0.035em;
}

.chapter h2 {
  margin: 2rem 0 0.65rem;
  color: var(--accent);
  font-family: "Gill Sans", "Optima", "Avenir Next", sans-serif;
  font-size: 0.92rem;
  letter-spacing: 0.13em;
  text-transform: uppercase;
}

.chapter h3 {
  margin: 1.6rem 0 0.45rem;
  color: var(--accent-soft);
  font-size: 1.15rem;
}

p {
  margin: 0 0 0.88rem;
}

.prologue p:first-of-type::first-letter {
  float: left;
  padding: 0.04em 0.08em 0 0;
  color: var(--accent);
  font-size: 4.8rem;
  line-height: 0.78;
}

blockquote {
  margin: 1.35rem 0;
  padding: 0.25rem 0 0.25rem 1.15rem;
  border-left: 3px solid var(--accent);
  color: #3b2a1d;
  font-size: 1.13rem;
  font-style: italic;
}

blockquote p { margin: 0; }

ul, ol {
  margin: 0.4rem 0 1rem 1.15rem;
  padding-left: 1rem;
}

li { margin: 0.32rem 0; }

code {
  padding: 0.08em 0.22em;
  border-radius: 0.2em;
  background: rgba(75, 48, 25, 0.09);
  color: #3f2415;
  font-family: "Input Mono", "Cascadia Mono", "Courier New", monospace;
  font-size: 0.86em;
}

hr {
  width: 35%;
  margin: 2.2rem auto;
  border: 0;
  border-top: 1px solid var(--rule);
}

table {
  width: 100%;
  margin: 1rem 0 1.3rem;
  border-collapse: collapse;
  font-size: 0.84rem;
  line-height: 1.35;
}

th, td {
  padding: 0.42rem 0.48rem;
  border-bottom: 1px solid var(--rule);
  vertical-align: top;
}

th {
  color: var(--accent);
  font-family: "Gill Sans", "Optima", "Avenir Next", sans-serif;
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-align: left;
  text-transform: uppercase;
}

.backmatter {
  color: #3d3025;
  font-size: 0.94rem;
}

.backmatter .chapter-kicker::after {
  content: " / back matter";
}

.reading-note {
  margin: 2.4rem 0;
  padding: 1.1rem 1.25rem;
  border-left: 4px solid var(--accent);
  background: rgba(255, 255, 255, 0.28);
  color: var(--muted);
  font-size: 0.97rem;
}

a { color: var(--accent); }

@media print {
  @page {
    size: letter;
    margin: 0.72in 0.78in 0.82in;
  }

  body {
    background: white;
    font-size: 11.2pt;
  }

  .book {
    width: auto;
    margin: 0;
    padding: 0;
    background: white;
    box-shadow: none;
  }

  .title-page {
    min-height: 9.05in;
    break-after: page;
  }

  .contents {
    break-after: page;
  }

  .chapter {
    break-before: page;
    margin-top: 0;
  }

  .chapter > h1 {
    break-after: avoid;
  }

  h1, h2, h3, blockquote, table {
    break-inside: avoid;
  }
}
"""


def build() -> None:
    sections = [
        (
            "note",
            "A Note on This Copy",
            strip_first_h1(strip_source_notes(read(ROOT / "sections" / "01-how-to-read.md"))),
            "frontmatter",
        ),
        (
            "prologue",
            "Prologue: The Door In The Fog",
            clean_prologue(read(MANUSCRIPT / "00-prologue-the-door-in-the-fog.md")),
            "prologue",
        ),
        (
            "map",
            "A Map of the Book",
            strip_first_h1(strip_source_notes(read(ROOT / "sections" / "02-chapter-spine.md"))),
            "map",
        ),
        (
            "field-notes",
            "First Field Notes",
            strip_first_h1(strip_source_notes(read(ROOT / "sections" / "03-field-notes.md"))),
            "field-notes",
        ),
        (
            "open-gates",
            "Open Gates",
            strip_first_h1(strip_source_notes(read(ROOT / "sections" / "04-open-gates.md"))),
            "backmatter",
        ),
        (
            "appendix-g",
            "Appendix G: Manuscript Lineage Ledger",
            strip_first_h1(read(ROOT / "sections" / "appendix-g-manuscript-lineage.md")),
            "backmatter",
        ),
    ]

    contents = "\n".join(
        f'<li><a href="#{section_id}">{html.escape(title)}</a></li>'
        for section_id, title, _, _ in sections
    )
    body = "\n\n".join(section(section_id, title, markdown, classes) for section_id, title, markdown, classes in sections)

    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Building Our Better Angels: Tonight Reader v0 260707</title>
  <style>{css()}</style>
</head>
<body>
  <main class="book">
    <section class="title-page">
      <div class="eyebrow">Tonight reading copy / reader-v0 / 260707</div>
      <div>
        <h1>Building Our Better Angels</h1>
        <h2>An Invitation Reader</h2>
        <p class="motto">A door in the fog; not the finished house.</p>
      </div>
      <div class="stamp">
        <span>Keith-copy: print, read, mark, revise.</span>
        <span>Not a trusted-reader release.</span>
        <span>Built from docs/manuscript/reader-v0.</span>
      </div>
    </section>

    <nav class="contents" aria-label="Contents">
      <h2>Contents</h2>
      <ol>
        {contents}
      </ol>
    </nav>

    <div class="reading-note">
      This edition is intentionally book-like rather than final: generous margins,
      a familiar reading rhythm, rough gates moved to the back, and enough source
      lineage to stay honest without making the first pass feel like repo work.
    </div>

    {body}

    <footer class="colophon">
      Built by reader-v0/tools/build-tonight-edition.py from local manuscript sources.
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
