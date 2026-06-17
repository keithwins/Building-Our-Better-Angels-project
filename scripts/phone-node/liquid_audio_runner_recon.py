import json
import os
import subprocess
import urllib.request
from datetime import datetime

REPOS = [
    "LiquidAI/LFM2.5-Audio-1.5B-GGUF",
    "LiquidAI/LFM2-Audio-1.5B-GGUF",
]

KEYWORDS = [
    "runner", "android", "arm64", "audio", "server", "cli",
    "vocoder", "speaker", "mtmd", "lfm2", "liquid"
]

def hf_tree(repo):
    url = f"https://huggingface.co/api/models/{repo}/tree/main?recursive=1"
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)

def shell(cmd):
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True, timeout=30)
        return out.strip()
    except Exception as e:
        return f"FAILED: {e}"

lines = []
lines.append("# Liquid Audio Runner Recon")
lines.append("")
lines.append(f"Created: {datetime.now().isoformat(timespec='seconds')}")
lines.append("")
lines.append("## Local binary")
lines.append("")
lines.append("```text")
lines.append(shell("~/bin/llama-server --version 2>&1"))
lines.append("```")
lines.append("")
lines.append("## Local server help: audio-related flags")
lines.append("")
lines.append("```text")
lines.append(shell("~/bin/llama-server --help 2>&1 | grep -Ei 'audio|vocoder|speaker|tts|mmproj|mtmd|hf-repo-v|hf-file-v|server|cli' | head -120"))
lines.append("```")
lines.append("")
lines.append("## Local llama.cpp liquid/audio files")
lines.append("")
lines.append("```text")
lines.append(shell("find ~/llama.cpp -iname '*liquid*' -o -iname '*audio*' -o -iname '*vocoder*' | head -100"))
lines.append("```")
lines.append("")

for repo in REPOS:
    lines.append(f"## Hugging Face file scan: {repo}")
    lines.append("")
    try:
        tree = hf_tree(repo)
        paths = []
        for item in tree:
            p = item.get("path", "")
            low = p.lower()
            if any(k in low for k in KEYWORDS):
                paths.append(p)
        if paths:
            lines.append("```text")
            lines.extend(paths[:200])
            lines.append("```")
        else:
            lines.append("No runner/audio-related paths found by keyword scan.")
    except Exception as e:
        lines.append(f"FAILED to scan repo: {e}")
    lines.append("")

report = "\n".join(lines)
out = "docs/wiki/session-records/2026-06-17-liquid-audio-runner-recon.md"
with open(out, "w", encoding="utf-8") as f:
    f.write(report)

print("LIQUID_AUDIO_RECON_WRITTEN")
print(out)
print()
print(report[-3000:])
