#!/usr/bin/env python3
"""LH receiving-text syntax and identity check; no manuscript mutation/build."""
import ast
from hashlib import sha256
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_odd_weighted"
PREFIX = "S6_SERIES_PUBLISH_III_02LH_"


def body(name, environment):
    text = (LANE/(PREFIX+name)).read_text()
    start = text.index("\\begin{"+environment+"}")
    stop = text.index("\\end{"+environment+"}", start)+len("\\end{"+environment+"}")
    return text[start:stop]


old_statement = body("released_statement.tex", "theorem")
old_proof = body("released_proof.tex", "proof")
statement = body("receiving.tex", "theorem")
proof = body("receiving.tex", "proof")
for kind, old, new in (("statement", old_statement, statement),
                       ("proof", old_proof, proof)):
    for pattern, label in (
        (r"\\label\{([^}]+)\}", "labels"),
        (r"\\hypertarget\{([^}]+)\}", "targets"),
        (r"\\tag\{([^}]+)\}", "equation tags"),
    ):
        old_ids, new_ids = re.findall(pattern, old), re.findall(pattern, new)
        assert old_ids == new_ids, (kind, label, old_ids, new_ids)
        assert len(new_ids) == len(set(new_ids))
        print("PASS", kind, label, len(new_ids), "exact identities and order")
assert len(re.findall(r"\\label\{", statement+proof)) == 8
assert len(re.findall(r"\\tag\{", statement+proof)) == 7
assert r"\StatementRecord" not in statement+proof

for suffix in ("post_exposure_derivation.md", "receiving.tex"):
    path = LANE/(PREFIX+suffix)
    raw = path.read_bytes()
    assert raw.endswith(b"\n")
    assert all(x >= 32 or x in (9, 10) for x in raw)
    text = raw.decode()
    for left, right in ((r"\(", r"\)"), (r"\[", r"\]")):
        assert text.count(left) == text.count(right)
    fragments = re.findall(r"\\\[(.*?)\\\]", text, re.S)
    fragments += re.findall(r"\\\((.*?)\\\)", text, re.S)
    cleaned = []
    for f in fragments:
        f = re.sub(r"\\tag\{[^}]*\}", "", f)
        f = re.sub(r"\\hypertarget\{[^}]*\}\{\}", "", f)
        f = re.sub(r"\\label\{[^}]*\}", "", f)
        cleaned.append(f.strip())
    p = subprocess.run(
        ["pandoc", "--from=markdown+tex_math_dollars", "--to=html", "--mathml"],
        input="\n\n".join("$$\n"+f+"\n$$" for f in cleaned),
        text=True, capture_output=True,
    )
    assert p.returncode == 0 and not p.stderr.strip(), (suffix, p.stderr)
    assert len(re.findall(r"<math(?:\s|>)", p.stdout)) == len(fragments)
    print("PASS", suffix, "whole text LF/control/delimiter and math syntax",
          len(text.splitlines()), "lines", len(fragments), "fragments")
    print("SHA256", suffix, sha256(raw).hexdigest())

math = re.findall(r"\\\[(.*?)\\\]", statement+proof, re.S)
math += re.findall(r"\\\((.*?)\\\)", statement+proof, re.S)
for f in math:
    f = re.sub(r"\\(?:tag|label|hypertarget)\{[^}]*\}(?:\{\})?", "", f)
    assert not re.search(r"D(?!\.(?:OW|WP|[0-9]))", f), f
assert not re.search(r"\b(?:fresh|admitted|frozen|companion)\b", statement+proof)
assert not re.search(r"\.(?:py|json|tsv)|code/|agents/", statement+proof)
print("PASS single iterate notation and mathematical prose scope")

for stem in ("post_exposure_v1", "receiver_v1", "receiver_v2", "receiver_v3"):
    path = ROOT/"code"/("S6_SERIES_PUBLISH_c7_lh_"+stem+".py")
    raw = path.read_bytes()
    ast.parse(raw.decode())
    assert all(x >= 32 or x in (9, 10) for x in raw)
    out = path.with_suffix(".out").read_bytes()
    err = path.with_suffix(".err").read_bytes()
    assert not err, (stem, err.decode())
    print("PASS source syntax and complete streams", stem,
          "source", len(raw.splitlines()), "stdout", len(out.splitlines()),
          "stderr", len(err.splitlines()))

for suffix, expected in {
    "fresh_derivation.md": "23e7026ce52f00005d7d4248f33b4975900e3c64b9905a06b614ecde06cbf0d8",
    "fresh_local_maps.md": "71eb34b0e8735b77d34e3bfe7a48240b2acde421a0a2fdc8ea7b96bc4cc79ee0",
}.items():
    assert sha256((LANE/(PREFIX+suffix)).read_bytes()).hexdigest() == expected
print("PASS frozen fresh mathematical bytes unchanged")
print("SCOPE syntax and exact identities only; no canonical/PDF/build/unit/page/admission claim")
