# Reader v0

**Title:** *Building Our Better Angels: An Invitation Reader*  
**Version:** `reader-v0`  
**Build stamp:** `260707`  
**Audience:** Keith-copy, not trusted-reader copy  
**Status:** printable working packet

This directory holds the first coffee-shop reader packet for the book project.
It is meant to be printed, read with a pen, marked up, argued with, and revised.

It is not a finished manuscript and not a public/trusted-reader release.

## Build

From this directory:

```bash
bash build-reader-v0.sh
```

Output:

```text
build/building-our-better-angels-invitation-reader-v0-260707.md
```

The build script concatenates the local section sources plus the current
prologue seed. The generated file carries a date label for timeline orientation;
the repo path keeps the simpler `reader-v0` name so Git can do the detailed
history tracking.

## Tonight Edition

For a more familiar book-like read, build the HTML print edition:

```bash
python3 tools/build-tonight-edition.py
```

Output:

```text
print/building-our-better-angels-tonight-reader-v0-260707.html
```

This edition is meant for tonight's read: title page, contents, generous
margins, browser-print styling, and rough gates moved into back matter.

## Gates Before Trusted-Reader Copy

- `oq-001`: public/private seam for Walk, Fog stream, Drive, corpus, Salon,
  Asterisms, and GitHub.
- ~~`oq-009`: forgetting doctrine~~ — **CLOSED 2026-07-10:**
  [`docs/core/no-forgetting.md`](../../core/no-forgetting.md) (no forgetting;
  no crypto-shred; shrouding-as-forget retired).
- Multitude source lineage: locate and reconcile the richer April Drive seed
  before treating the Multitude chapter as public-ready prose.

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
