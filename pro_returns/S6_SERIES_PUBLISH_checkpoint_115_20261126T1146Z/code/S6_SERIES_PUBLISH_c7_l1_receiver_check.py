#!/usr/bin/env python3
"""Insert the complete freshly derived table and validate the L1 receiver.

Reads only released L1 and its frozen new data. No historical program is
executed. MathML conversion is syntax checking, not a TeX/PDF/page check.
"""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_nonstar"
PREFIX = "S6_SERIES_PUBLISH_III_02L1_"
receiver = LANE/(PREFIX+"receiving.tex")
rows = list(csv.DictReader((LANE/(PREFIX+"fresh_sphere_patterns.csv")).open()))
data = json.loads((LANE/(PREFIX+"fresh_catalogue.json")).read_text())
assert len(rows) == len(data["sphere_patterns"]) == 59
keys = [(r["OS"],r["profile"],r["a"],r["b"],r["zero_index"]) for r in rows]
assert len(set(keys)) == 50
assert all(r["zero_component"] == "0" and r["c"] == "1" for r in rows)

def set_tex(raw):
    values = json.loads(raw)
    return r"\varnothing" if not values else r"\{"+",".join(map(str,values))+r"\}"

table = [r"\begingroup\small"]
for start in range(0,59,20):
    table += [r"\[",r"\begin{array}{c|rr|r|c|c}",
              r"\mathrm{profile}&a&b&\mathrm{zero\ place}&L&O\\ \hline"]
    for row in rows[start:start+20]:
        profile = row["OS"] + ("" if row["profile"] == "default" else "/"+row["profile"])
        table.append("&".join([profile,row["a"],row["b"],row["zero_index"],
                              set_tex(row["finite_indices"]),
                              set_tex(row["original_additive_indices"])])+r"\\")
        print("TABLE",row["pattern"],profile,"a",row["a"],"b",row["b"],
              "zero",row["zero_index"],"finite",row["finite_indices"],
              "original",row["original_additive_indices"])
    table += [r"\end{array}",r"\]"]
table += [r"\endgroup"]
table_text = "\n".join(table)
text = receiver.read_text()
marker = "%% L1_SPHERE_TABLE %%"
if marker in text:
    assert text.count(marker) == 1
    text = text.replace(marker,table_text)
    receiver.write_text(text)
else:
    assert text.count(table_text) == 1
counts = Counter(r["OS"]+("" if r["profile"]=="default" else "/"+r["profile"]) for r in rows)
expected = dict(zip(("43","43/II","45","45/II","47","47/II","47/III","49",
                     "49/II","49/III","55","55/II","56","56/II","56/III","56/IV"),
                    (3,1,4,4,4,4,4,3,1,2,4,4,5,6,5,5)))
assert dict(counts) == expected
additive_profiles = {r["OS"]+("" if r["profile"]=="default" else "/"+r["profile"])
                     for r in rows
                     if json.loads(r["finite_indices"]) or json.loads(r["original_additive_indices"])}
one_finite = {r["OS"]+("" if r["profile"]=="default" else "/"+r["profile"])
              for r in rows if len(json.loads(r["finite_indices"])) == 1}
assert len(additive_profiles) == 12 and additive_profiles <= one_finite
two_finite = [r for r in rows if len(json.loads(r["finite_indices"]))==2]
assert len(two_finite)==1
assert (two_finite[0]["OS"],two_finite[0]["profile"],two_finite[0]["a"],
        two_finite[0]["b"]) == ("49","III","1","6")
print("PASS complete inline table: 59 patterns, 50 initial rows, sixteen profile counts.")
print("PASS all twelve additive profiles have a one-finite infinite-order family; unique two-finite row verified.")

raw = receiver.read_bytes()
assert all(x >= 32 or x in (9,10) for x in raw)
assert raw.endswith(b"\n")
assert marker not in text
assert r"\StatementRecord" not in text
assert "records/" not in text and ".py" not in text and ".csv" not in text
labels = re.findall(r"\\label\{([^}]*)\}",text)
expected_labels = ["maps:src:D.2.26"]+["maps:eq:D.HY"+str(i) for i in range(1,8)]
assert Counter(labels)==Counter(expected_labels),labels
tags = re.findall(r"\\hypertarget\{tag-([^}]+)\}",text)
expected_tags = ["02L1","01ZN","01ZO","01ZP","01ZQ","01ZR","01ZS","01ZT"]
assert Counter(tags)==Counter(expected_tags),tags
eqtags = re.findall(r"\\tag\{([^}]+)\}",text)
assert Counter(eqtags)==Counter("D.HY"+str(i) for i in range(1,8))
stack=[]
for kind,name in re.findall(r"\\(begin|end)\{([^}]+)\}",text):
    if kind=="begin":
        stack.append(name)
    else:
        assert stack and stack.pop()==name,(kind,name,stack)
assert not stack
for left,right in ((r"\(",r"\)"),(r"\[",r"\]")):
    assert text.count(left)==text.count(right)
print("PASS all eight permanent labels and tags occur exactly once; all seven equation tags retained.")
print("PASS LF/control bytes, balanced environments/delimiters, and complete receiver content.")

displays=re.findall(r"\\\[(.*?)\\\]",text,re.S)
without_display=re.sub(r"\\\[.*?\\\]","",text,flags=re.S)
inlines=re.findall(r"(?<!\\)\$(.*?)(?<!\\)\$",without_display,re.S)
fragments=displays+inlines
clean=[]
for fragment in fragments:
    fragment=re.sub(r"\\tag\{[^}]*\}","",fragment)
    fragment=re.sub(r"\\label\{[^}]*\}","",fragment)
    fragment=re.sub(r"\\hypertarget\{[^}]*\}\{\}","",fragment)
    clean.append(fragment.strip())
result=subprocess.run(["pandoc","--from=markdown+tex_math_dollars","--to=html","--mathml"],
                      input="\n\n".join("$$\n"+f+"\n$$" for f in clean),
                      text=True,capture_output=True,check=False)
assert result.returncode==0,result.stderr
assert not result.stderr.strip(),result.stderr
assert len(re.findall(r"<math(?:\s|>)",result.stdout))==len(fragments)
print("PASS MathML conversion:",len(displays),"display and",len(inlines),"inline fragments.")
print("SCOPE syntax only; no TeX build, PDF render, or page-reading claim.")
print("RECEIVER SHA256",hashlib.sha256(raw).hexdigest())
