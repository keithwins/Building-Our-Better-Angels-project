#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_STAMP="${BUILD_STAMP:-260711}"
HTML="$ROOT/print/building-our-better-angels-trusted-reader-v0-${BUILD_STAMP}.html"
PDF="$ROOT/print/building-our-better-angels-trusted-reader-v0-${BUILD_STAMP}.pdf"

python3 "$ROOT/tools/build-trusted-edition.py"

if command -v chromium >/dev/null 2>&1; then
  chromium --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PDF" "file://$HTML"
elif command -v google-chrome >/dev/null 2>&1; then
  google-chrome --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PDF" "file://$HTML"
elif [[ -x "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe" ]]; then
  HTML_WIN="$(wslpath -w "$HTML")"
  PDF_WIN="$(wslpath -w "$PDF")"
  "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe" \
    --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PDF_WIN" "$HTML_WIN"
elif [[ -x "/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" ]]; then
  HTML_WIN="$(wslpath -w "$HTML")"
  PDF_WIN="$(wslpath -w "$PDF")"
  "/mnt/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" \
    --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PDF_WIN" "$HTML_WIN"
else
  printf 'No supported headless browser found for PDF rendering.\n' >&2
  exit 1
fi

printf 'wrote %s\n' "$PDF"
