#!/usr/bin/env python3
"""Whole owned LH fresh-note syntax and source readback; no target original."""
from hashlib import sha256
from pathlib import Path
import ast
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_odd_weighted"
for suffix in ("fresh_derivation.md", "fresh_local_maps.md", "fresh_source_scope.md", "attempt_record.md"):
    path = LANE/("S6_SERIES_PUBLISH_III_02LH_"+suffix)
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert all(x >= 32 or x in (9,10) for x in raw)
    text = raw.decode()
    for left, right in ((r"\(",r"\)"),(r"\[",r"\]")):
        assert text.count(left) == text.count(right), (suffix,left)
    fragments = re.findall(r"\\\[(.*?)\\\]",text,re.S)+re.findall(r"\\\((.*?)\\\)",text,re.S)
    cleaned = [re.sub(r"\\tag\{[^}]*\}","",f).strip() for f in fragments]
    p = subprocess.run(["pandoc","--from=markdown+tex_math_dollars","--to=html","--mathml"],
                       input="\n\n".join("$$\n"+f+"\n$$" for f in cleaned),
                       text=True,capture_output=True)
    assert p.returncode == 0 and not p.stderr.strip(), (suffix,p.stderr)
    assert len(re.findall(r"<math(?:\s|>)",p.stdout)) == len(fragments)
    print("PASS",suffix,"LINES",len(text.splitlines()),"MATH",len(fragments),"SHA256",sha256(raw).hexdigest())
for stem in (
    "integral", "exterior_local_v1", "exterior_local_v2", "exterior_local_v3",
    "component_denominators_v1", "runtime_probe_v1", "catalogue_v1",
):
    path = ROOT/"code"/("S6_SERIES_PUBLISH_c7_lh_"+stem+".py")
    source = path.read_text()
    ast.parse(source)
    assert "\r" not in source
    print("PASS complete source readback",stem,"LINES",len(source.splitlines()),"SHA256",sha256(source.encode()).hexdigest())
print("SCOPE whole fresh-note math syntax, LF/control bytes and source parsing; no manuscript, original, PDF or admission claim.")
