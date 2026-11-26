#!/usr/bin/env python3
"""Check every fresh L9 math fragment, LF endings and control characters.
Syntax and MathML conversion only; no PDF build or page-reading credit.
"""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
path = ROOT/"agents/continuation7_iii_multiplicative/S6_SERIES_PUBLISH_III_02L9_fresh_derivation.md"
data = path.read_bytes()
assert all(x >= 32 or x in (9, 10) for x in data)
source = data.decode("utf-8")
assert source.endswith("\n")
for left, right in ((r"\(", r"\)"), (r"\[", r"\]")):
    assert source.count(left) == source.count(right)
displays = re.findall(r"\\\[(.*?)\\\]", source, re.S)
inlines = re.findall(r"\\\((.*?)\\\)", source, re.S)
fragments = displays + inlines
clean = [re.sub(r"\\tag\{[^}]*\}", "", f) for f in fragments]
result = subprocess.run(
    ["pandoc", "--from=markdown+tex_math_dollars", "--to=html", "--mathml"],
    input="\n\n".join("$$\n"+f.strip()+"\n$$" for f in clean),
    text=True, capture_output=True, check=False)
assert result.returncode == 0, result.stderr
assert not result.stderr.strip(), result.stderr
assert len(re.findall(r"<math(?:\s|>)", result.stdout)) == len(fragments)
print("PASS", len(displays), "display and", len(inlines), "inline math fragments.")
print("PASS LF, control characters, balanced delimiters and complete MathML conversion.")
print("SCOPE syntax only; no PDF build or rendered-page credit.")
