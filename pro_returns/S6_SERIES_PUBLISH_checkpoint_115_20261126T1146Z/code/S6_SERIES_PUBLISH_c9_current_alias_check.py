#!/usr/bin/env python3
"""Independently check the seven supplied alias displays on current LaTeX.

The input MWE is copied byte-for-byte from the root's existing test. The
--plain-control variant then replaces the sole optional-type diagnostic
label by its ordinary public-interface form and checks the exact inverse.
The manuscript and its records are not modified. Retained outputs give
actual compiler passes, complete aux-record comparisons and PDF link checks.
"""
from pathlib import Path
import hashlib
import re
import subprocess
import sys

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "agents/continuation9_tex_runtime/aliases/S6_SERIES_PUBLISH_c9_display_aliases.tex"
PLAIN_CONTROL = "--plain-control" in sys.argv
WORK = ROOT / ("agents/continuation9_current_tex/aliases_plain_control" if PLAIN_CONTROL else "agents/continuation9_current_tex/aliases_latest")
WORK.mkdir(parents=True, exist_ok=True)
TEX = WORK / INPUT.name
TEX.write_bytes(INPUT.read_bytes())
assert TEX.read_bytes() == INPUT.read_bytes()
if PLAIN_CONTROL:
    old = r"\label[equation]{c9:ordinary-after}"
    new = r"\label{c9:ordinary-after}"
    original = TEX.read_text()
    assert original.count(old) == 1
    revised = original.replace(old, new)
    assert revised.replace(new, old) == original
    TEX.write_text(revised, newline="\n")
WRAPPER = ROOT / "code/S6_SERIES_PUBLISH_c9_current_pdflatex.py"
PAIRS = [
    ("wb:h24:ret:eq:M", "maps:eq:B.3.2"),
    ("wb:h24:ret:eq:derivative-on-M", "maps:eq:B.3.3"),
    ("wb:h24:ret:eq:normal-u", "maps:eq:B.3.4"),
    ("maps:eq:D.OF1", "maps:eq:D.OL1"),
    ("maps:eq:D.OF11", "maps:eq:D.OL2"),
    ("maps:eq:D.OF16", "maps:eq:D.OL12"),
    ("maps:eq:D.OF18", "maps:eq:D.OL3"),
]


def groups(text):
    depth = 0
    start = None
    out = []
    for i, ch in enumerate(text):
        if ch == "{":
            if depth == 0:
                start = i + 1
            depth += 1
        elif ch == "}":
            depth -= 1
            assert depth >= 0
            if depth == 0:
                out.append(text[start:i])
    assert depth == 0
    return out


print("MWE source SHA-256", hashlib.sha256(TEX.read_bytes()).hexdigest(), flush=True)
last = None
for n in range(1, 5):
    result = subprocess.run([sys.executable, str(WRAPPER), "-interaction=nonstopmode", "-halt-on-error", TEX.name], cwd=WORK, capture_output=True, text=True)
    prefix = ROOT / f"code/S6_SERIES_PUBLISH_c9_current_alias_{'plain' if PLAIN_CONTROL else 'latest'}_pass{n:02d}"
    prefix.with_suffix(".out").write_text(result.stdout, newline="\n")
    prefix.with_suffix(".err").write_text(result.stderr, newline="\n")
    log = TEX.with_suffix(".log").read_text() if TEX.with_suffix(".log").exists() else ""
    prefix.with_suffix(".log").write_text(log, newline="\n")
    print("pass", n, "exit", result.returncode, flush=True)
    assert result.returncode == 0, result.stdout[-6000:]
    assert "LaTeX2e <2026-11-01>" in log
    aux = TEX.with_suffix(".aux").read_text()
    unresolved = [line for line in log.splitlines() if "undefined" in line or "Rerun to get" in line or "Rerun LaTeX" in line]
    if aux == last:
        print("Stable auxiliary data; unresolved diagnostics:", unresolved, flush=True)
        break
    last = aux
else:
    raise AssertionError("The supplied alias MWE did not converge in four passes")

records = dict(re.findall(r"^\\newlabel\{([^{}]+)\}(.*)$", aux, re.M))
pdf = PdfReader(TEX.with_suffix(".pdf"))
destinations = pdf.named_destinations
link_targets = []
for page in pdf.pages:
    for indirect in page.get("/Annots", []):
        annotation = indirect.get_object()
        action = annotation.get("/A", {})
        if action.get("/S") == "/GoTo":
            link_targets.append(str(action["/D"]))
        elif "/Dest" in annotation:
            link_targets.append(str(annotation["/Dest"]))
for primary, alias in PAIRS:
    assert records[primary] == records[alias], (primary, alias)
    assert records[primary + "@cref"] == records[alias + "@cref"], (primary, alias)
    fields = groups(groups(records[primary])[0])
    assert len(fields) == 5, fields
    anchor = fields[3]
    assert anchor in destinations, anchor
    assert link_targets.count(anchor) >= 3, (anchor, link_targets.count(anchor))
    print(primary, "=", alias, records[primary], "PDF links", link_targets.count(anchor), flush=True)
for label, number in [("c9:ordinary-before", "1.1"), ("c9:ordinary-after", "1.10"), ("c9:reset", "2.1")]:
    actual = groups(groups(records[label])[0])[0]
    assert actual == number, (label, actual, number)
    print("ordinary/reset", label, actual, flush=True)
tags = re.findall(r"\\hypertarget\{(tag-[^{}]+)\}", TEX.read_text())
assert len(tags) == len(set(tags))
assert all(tag in destinations for tag in tags)
print("Every explicit tag destination exists:", len(tags), flush=True)
issues = [line for line in log.splitlines() if any(term in line for term in ("Overfull", "Missing character", "LaTeX Font Warning", "undefined", "destination with the same identifier"))]
print("Final log issues:", issues, flush=True)
assert not any("Missing character" in line or "Font Warning" in line or "undefined" in line or "destination with" in line for line in issues)
print("PDF pages", len(pdf.pages), "SHA-256", hashlib.sha256(TEX.with_suffix(".pdf").read_bytes()).hexdigest(), flush=True)
print("PASS: all seven full ordinary and cleveref records, all seven PDF destinations/link triples, ordinary labels and section reset.", flush=True)
subprocess.run(["pdftoppm", "-r", "90", "-png", str(TEX.with_suffix(".pdf")), str(WORK / "page")], check=True)
print("Rendered pages:", ", ".join(path.name for path in sorted(WORK.glob("page-*.png"))), flush=True)
