#!/usr/bin/env python3
"""Check LF/control characters and convert every fresh L1 math fragment.

Syntax and MathML conversion only; no PDF build or page-reading credit.
"""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT/"agents/continuation7_iii_nonstar"
total = 0
for suffix in ("fresh_cap_rank", "fresh_graph_maps", "fresh_derivation"):
    path = FOLDER/f"S6_SERIES_PUBLISH_III_02L1_{suffix}.md"
    data = path.read_bytes()
    assert all(x >= 32 or x in (9,10) for x in data)
    source = data.decode("utf-8")
    assert source.endswith("\n")
    for left, right in ((r"\(",r"\)"),(r"\[",r"\]")):
        assert source.count(left) == source.count(right)
    displays = re.findall(r"\\\[(.*?)\\\]",source,re.S)
    inlines = re.findall(r"\\\((.*?)\\\)",source,re.S)
    fragments = displays+inlines
    clean = [re.sub(r"\\tag\{[^}]*\}","",f) for f in fragments]
    result = subprocess.run(
        ["pandoc","--from=markdown+tex_math_dollars","--to=html","--mathml"],
        input="\n\n".join("$$\n"+f.strip()+"\n$$" for f in clean),
        text=True,capture_output=True,check=False)
    assert result.returncode == 0, result.stderr
    assert not result.stderr.strip(), result.stderr
    assert len(re.findall(r"<math(?:\s|>)",result.stdout)) == len(fragments)
    total += len(fragments)
    print("PASS",suffix,len(displays),"display",len(inlines),
          "inline fragments; LF/control/delimiters and MathML conversion.")
print("PASS",total,"fragments; no PDF build or rendered-page credit.")
