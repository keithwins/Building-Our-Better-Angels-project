# Reader v0

**Title:** *Building Our Better Angels: An Invitation Reader*  
**Version:** `reader-v0`  
**Build stamp:** `260710`
**Audience:** Keith-copy, not trusted-reader copy  
**Status:** printable working packet

This directory holds the first coffee-shop reader packet for the book project.
It is meant to be printed, read with a pen, marked up, argued with, and revised.

It is not a finished manuscript and not a public/trusted-reader release.

## Edit in the Salon

**Editorial work on this reader lives on the Salon floor** — margin notes,
objections, partial rewrites, and revision claims hashed out in conversation,
scoped to the section you are reading.

1. Open the orientation web (with `salon-serve` — usually already on `:8080`).
2. In the sidebar, choose **Reader v0** → the section you are reading.
3. Use **✳ Salon** (bottom-right). `refs` carry the section path automatically.

The sharp line is not “conversation vs rewrite.” Rewriting happens in the
thread, in degrees. The line worth keeping is **do not silently patch section
files** without the Salon trail that led there. When a thread has settled enough
to capture, apply the change to the section file and rebuild.

Terminal equivalent:

```bash
salon-say -r Building-Our-Better-Angels-project/docs/manuscript/reader-v0/sections/03-field-notes.md "This paragraph is alive; that one is coy."
```

## Gates Before Trusted-Reader Copy

- ~~`oq-001`: public/private seam~~ — **CLOSED 2026-07-10:**
  [`docs/core/public-private-seam.md`](../../core/public-private-seam.md)
  (five classes; Keith-copy ungated; allowlist = invitation cut; self-facing
  pacing under Resonator).
- ~~`oq-009`: forgetting doctrine~~ — **CLOSED 2026-07-10:**
  [`docs/core/no-forgetting.md`](../../core/no-forgetting.md) (no forgetting;
  no crypto-shred; shrouding-as-forget retired).
- Multitude source lineage: locate and reconcile the richer April Drive seed
  before treating the Multitude chapter as public-ready prose.

**Trusted-reader edition (2026-07-11):** `sections-trusted/` holds the outside-reader
copy — prologue-first order, book voice, red-team fixes F1–F5, remaining gates
named in back matter. Keith-copy sections in `sections/` stay the working markup
lane.

## Keith-Copy Build

From this directory:

```bash
bash build-reader-v0.sh
```

Output:

```text
build/building-our-better-angels-invitation-reader-v0-260710.md
```

## Trusted-Reader Build

From this directory:

```bash
bash build-trusted-reader-v0.sh
python3 tools/build-trusted-edition.py
bash tools/build-trusted-pdf.sh
```

Outputs:

```text
build/building-our-better-angels-invitation-reader-trusted-v0-260711.md
print/building-our-better-angels-trusted-reader-v0-260711.html
print/building-our-better-angels-trusted-reader-v0-260711.pdf
```

The build script concatenates the local section sources plus the current
prologue seed. The generated file carries a date label for timeline orientation;
the repo path keeps the simpler `reader-v0` name so Git can do the detailed
history tracking.

## Tonight Edition (Keith-copy HTML)

For a more familiar book-like read of the Keith-copy, build the HTML print edition:

```bash
python3 tools/build-tonight-edition.py
```

Output:

```text
print/building-our-better-angels-tonight-reader-v0-260710.html
```

This edition is meant for tonight's read: title page, contents, generous
margins, browser-print styling, and rough gates moved into back matter.

## Red-Team Lane

Claude/CC opened `eph:score:20260707T003608Z-4247` to red-team this packet once
it exists on disk.

Recommended hostile readers:

- the skeptic;
- the person in the fog;
- the technical reader.

Expected findings should be anchored per section and graded as:

- blocks print;
- weakens;
- polish.
