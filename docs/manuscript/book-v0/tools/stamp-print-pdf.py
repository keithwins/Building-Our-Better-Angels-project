#!/usr/bin/env python3
"""Stamp identity header + page numbers onto a Chrome-printed book-v0 PDF."""

from __future__ import annotations

import os
import sys
from datetime import datetime
from io import BytesIO
from pathlib import Path
from zoneinfo import ZoneInfo

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import Color
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
BUILD_STAMP = os.environ.get("BUILD_STAMP") or datetime.now().strftime("%y%m%d")
BUILD_TZ = ZoneInfo(os.environ.get("BUILD_TZ", "America/New_York"))
PDF_NAME = f"building-our-better-angels-book-v0-{BUILD_STAMP}.pdf"
PDF_PATH = ROOT / "print" / PDF_NAME
INK = Color(0.424, 0.353, 0.271)  # ~#6c5a45


def header_label(built_at: datetime, pdf_name: str) -> str:
    return (
        f"Building Our Better Angels · {pdf_name} · "
        f"{built_at.strftime('%Y-%m-%d %H:%M %Z')}"
    )


def overlay_page(width: float, height: float, header: str, page_label: str) -> BytesIO:
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(width, height))
    c.setFillColor(INK)
    c.setFont("Helvetica", 7.5)
    # Keep the identity line inside the top margin, slightly inset.
    c.drawCentredString(width / 2.0, height - 36, header)
    c.setFont("Helvetica", 9)
    c.drawCentredString(width / 2.0, 28, page_label)
    # Hairline rules so the chrome reads as print furniture, not body text.
    c.setStrokeColor(INK)
    c.setLineWidth(0.4)
    c.setStrokeAlpha(0.35)
    c.line(54, height - 42, width - 54, height - 42)
    c.line(54, 40, width - 54, 40)
    c.save()
    buf.seek(0)
    return buf


def stamp(path: Path, built_at: datetime | None = None) -> None:
    if not path.is_file():
        raise SystemExit(f"missing pdf: {path}")
    built_at = built_at or datetime.now(BUILD_TZ)
    header = header_label(built_at, path.name)
    reader = PdfReader(str(path))
    writer = PdfWriter()
    total = len(reader.pages)
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        stamp_pdf = PdfReader(overlay_page(width, height, header, f"{index} / {total}"))
        page.merge_page(stamp_pdf.pages[0])
        writer.add_page(page)
    tmp = path.with_suffix(".stamped.pdf")
    with tmp.open("wb") as fh:
        writer.write(fh)
    tmp.replace(path)
    print(f"stamped {path} ({total} pages)")
    print(f"header: {header}")


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else PDF_PATH
    stamp(target)
