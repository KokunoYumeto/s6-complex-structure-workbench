#!/usr/bin/env python3
"""Parse every mathematical fragment in the two new receivers.

This is syntax/render-conversion validation, not a TeX build or page review.
"""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "agents/continuation7_iii_original_caps"
total = 0
for tag in ("02KV", "02KW"):
    path = FOLDER / f"S6_SERIES_PUBLISH_III_{tag}_receiving.tex"
    source = path.read_text()
    displays = re.findall(r"\\\[(.*?)\\\]", source, flags=re.S)
    inlines = re.findall(r"(?<!\\)\$(?!\$)(.*?)(?<!\\)\$", source, flags=re.S)
    fragments = displays + inlines
    clean = []
    for fragment in fragments:
        fragment = re.sub(r"\\hypertarget\{[^}]*\}\{\}", "", fragment)
        fragment = re.sub(r"\\(?:label|tag)\{[^}]*\}", "", fragment)
        clean.append("$$\n" + fragment.strip() + "\n$$")
    result = subprocess.run(
        ["pandoc", "--from=markdown+tex_math_dollars", "--to=html", "--mathml"],
        input="\n\n".join(clean), text=True, capture_output=True, check=False)
    assert result.returncode == 0, (tag, result.stderr)
    assert not result.stderr.strip(), (tag, result.stderr)
    assert len(re.findall(r"<math(?:\s|>)", result.stdout)) == len(fragments)
    total += len(fragments)
    print(f"PASS {tag}: {len(displays)} display and {len(inlines)} inline fragments converted to MathML without warnings.")
print(f"PASS {total} mathematical fragments; no TeX build or rendered-page credit claimed.")
