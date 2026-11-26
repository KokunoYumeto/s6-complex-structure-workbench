#!/usr/bin/env python3
"""Validate the complete L9 receiver and post-exposure mathematical syntax.
No canonical, global or frozen fresh file is written.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_multiplicative"
BASE = "S6_SERIES_PUBLISH_III_02L9_"
receiver = (LANE/(BASE+"receiving.tex")).read_text()
old = "\n".join((LANE/(BASE+"released_"+kind+".tex")).read_text()
                for kind in ("statement","proof"))
for pattern in (r"\\label\{([^}]+)\}",r"\\hypertarget\{([^}]+)\}",r"\\tag\{([^}]+)\}"):
    assert Counter(re.findall(pattern, receiver)) == Counter(re.findall(pattern, old))
assert len(re.findall(r"\\label\{",receiver)) == 11
assert len(re.findall(r"\\tag\{",receiver)) == 10
assert r"\StatementRecord" not in receiver
assert not any(word in receiver for word in ("records/",".json",".py","certificate"))
stack = []
for kind,name in re.findall(r"\\(begin|end)\{([^}]+)\}",receiver):
    if kind == "begin":
        stack.append(name)
    else:
        assert stack and stack.pop() == name, (kind,name,stack)
assert not stack
print("PASS all eleven permanent labels/hypertargets and all ten equation tags preserved exactly.")
print("PASS one theorem and one proof, balanced TeX environments, and complete mathematical receiver content.")
assert receiver.count(r"\begin{theorem}") == receiver.count(r"\end{theorem}") == 1
assert receiver.count(r"\begin{proof}") == receiver.count(r"\end{proof}") == 1

data = json.loads((LANE/(BASE+"fresh_data.json")).read_text())
for row in data["profile_totals"]:
    label = r"\mathrm{default}" if row[1] == "default" else row[1]
    line = "&".join([str(row[0]), label, *map(str,row[2:])])+r"\\"
    assert receiver.count(line) == 1, line
assert "&172&120&495&1728" in receiver
print("PASS all 21 inline profile counts match the frozen complete enumeration.")

total = 0
for suffix in ("receiving.tex","post_exposure_derivation.md"):
    path = LANE/(BASE+suffix)
    raw = path.read_bytes()
    assert all(x>=32 or x in (9,10) for x in raw)
    assert raw.endswith(b"\n")
    source = raw.decode()
    for left,right in ((r"\(",r"\)"),(r"\[",r"\]")):
        assert source.count(left) == source.count(right)
    displays = re.findall(r"\\\[(.*?)\\\]",source,re.S)
    equations = re.findall(r"\\begin\{equation\}(.*?)\\end\{equation\}",source,re.S)
    rest = re.sub(r"\\\[.*?\\\]","",source,flags=re.S)
    rest = re.sub(r"\\begin\{equation\}.*?\\end\{equation\}","",rest,flags=re.S)
    inlines = re.findall(r"(?<!\\)\$(.*?)(?<!\\)\$",rest,re.S)
    inlines += re.findall(r"\\\((.*?)\\\)",rest,re.S)
    assert len(re.findall(r"(?<!\\)\$",rest)) % 2 == 0
    fragments = displays+equations+inlines
    clean = []
    for f in fragments:
        f = re.sub(r"\\tag\{[^}]*\}","",f)
        f = re.sub(r"\\label\{[^}]*\}","",f)
        f = re.sub(r"\\hypertarget\{[^}]*\}\{\}","",f)
        clean.append(f.strip())
    result = subprocess.run(["pandoc","--from=markdown+tex_math_dollars",
                             "--to=html","--mathml"],
        input="\n\n".join("$$\n"+f+"\n$$" for f in clean),
        text=True,capture_output=True,check=False)
    assert result.returncode == 0, result.stderr
    assert not result.stderr.strip(), result.stderr
    assert len(re.findall(r"<math(?:\s|>)",result.stdout)) == len(fragments)
    total += len(fragments)
    print("PASS",suffix,len(displays)+len(equations),"display and",len(inlines),
          "inline fragments; LF/control/delimiters and complete MathML conversion.")
assert sha256((LANE/(BASE+"fresh_derivation.md")).read_bytes()).hexdigest() == "e5f8cc59e98d20ffe7b845824c369083b7e5246762ba52423aeeca7ea016f920"
print("PASS",total,"math fragments; frozen fresh proof unchanged.")
print("SCOPE syntax only; no TeX build, PDF rendering, unit closure or page-reading claim.")
print("RECEIVER SHA256",sha256((LANE/(BASE+"receiving.tex")).read_bytes()).hexdigest())
