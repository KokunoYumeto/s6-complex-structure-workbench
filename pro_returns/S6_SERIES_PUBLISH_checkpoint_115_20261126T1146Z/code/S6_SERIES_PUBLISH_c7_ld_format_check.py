#!/usr/bin/env python3
"""Readback, mathematical syntax, and exact inline-table checks for fresh LD.
No target original, global table, or canonical manuscript is read or written.
"""
from hashlib import sha256
from pathlib import Path
import ast
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_weighted_catalogue"
path=LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_derivation.md"
raw=path.read_bytes()
assert raw.endswith(b"\n")
assert all(x>=32 or x in (9,10) for x in raw)
source=raw.decode()
for left,right in ((r"\(",r"\)"),(r"\[",r"\]")):
    assert source.count(left)==source.count(right),(left,right)
displays=re.findall(r"\\\[(.*?)\\\]",source,re.S)
inlines=re.findall(r"\\\((.*?)\\\)",source,re.S)
assert not re.findall(r"(?<!\\)\$",source)
fragments=displays+inlines
clean=[re.sub(r"\\tag\{[^}]*\}","",f).strip() for f in fragments]
result=subprocess.run(["pandoc","--from=markdown+tex_math_dollars",
                       "--to=html","--mathml"],
    input="\n\n".join("$$\n"+f+"\n$$" for f in clean),
    text=True,capture_output=True,check=False)
assert result.returncode==0,result.stderr
assert not result.stderr.strip(),result.stderr
assert len(re.findall(r"<math(?:\s|>)",result.stdout))==len(fragments)
print("PASS LF/control bytes, balanced delimiters, and every mathematical fragment converted.")
print("MATH",len(displays),"display",len(inlines),"inline",len(fragments),"total")

patterns=json.loads((LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_patterns.json").read_text())
for row in patterns["profile_counts"]:
    cells=[row["OS"],row["profile"],row["rows"],row["nonzero_multiplicative"],
           row["patterns"],row["all_star_original"],row["individual_choices"]]
    text="| "+" | ".join(map(str,cells))+" |"
    assert source.count(text)==1,text
for row in patterns["extra_finite_star_families"]:
    cells=[*row["key"],"".join(row["choices"]),"".join(row["all_star_projection"])]
    text="|"+"|".join(map(str,cells))+"|"
    assert source.count(text)==1,text
assert len(patterns["patterns"])==495
assert sum(x["all_star_original"] for x in patterns["patterns"])==459
assert len(patterns["extra_finite_star_families"])==36
print("PASS all 21 complete inline profile rows and all 36 exact projection rows match the new data.")
global_data=json.loads((LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_global_data.json").read_text())
assert len(global_data["cases"])==4242
assert sum(c["e"]==0 for c in global_data["cases"])==2121
assert sum(c["e"]==1 for c in global_data["cases"])==2121
print("PASS retained complete global output has 4242 matrix/group cases, 2121 at each Euler value.")

for name,lines,output_lines in (("exterior",213,27),("finite",191,8),("catalogue",348,31)):
    stem=ROOT/"code"/("S6_SERIES_PUBLISH_c7_ld_"+name)
    code=stem.with_suffix(".py").read_text()
    ast.parse(code)
    assert len(code.splitlines())==lines
    out=stem.with_suffix(".out").read_text()
    assert len(out.splitlines())==output_lines
    assert stem.with_suffix(".err").read_bytes()==b""
    assert out.endswith("SCOPE LD original and historical weighted programs/outputs remain unopened.\n") if name=="catalogue" else "SCOPE" in out
    print("PASS",name,"complete source",lines,"lines; complete output",output_lines,"lines; error empty.")
print("SCOPE mathematical syntax and saved-data readback; no TeX/PDF build or page-reading credit.")
print("FRESH_SHA256",sha256(raw).hexdigest())
