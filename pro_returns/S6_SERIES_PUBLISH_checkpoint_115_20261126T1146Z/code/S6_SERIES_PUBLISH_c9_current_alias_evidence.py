#!/usr/bin/env python3
"""Retain exact observed alias records from the two actual current-kernel runs."""
from pathlib import Path
import hashlib
import json
import re

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
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
    start = 0
    result = []
    for i, char in enumerate(text):
        if char == "{":
            if depth == 0:
                start = i + 1
            depth += 1
        elif char == "}":
            depth -= 1
            assert depth >= 0
            if depth == 0:
                result.append(text[start:i])
    assert depth == 0
    return result


evidence = {}
for name, directory in [("exact_input", "aliases_latest"), ("plain_control", "aliases_plain_control")]:
    tex = ROOT / "agents/continuation9_current_tex" / directory / "S6_SERIES_PUBLISH_c9_display_aliases.tex"
    aux = tex.with_suffix(".aux").read_text()
    pdf = PdfReader(tex.with_suffix(".pdf"))
    records = {}
    for line in aux.splitlines():
        if line.startswith(r"\newlabel"):
            key, *value = groups(line[len(r"\newlabel"):])
            records[key] = "{" + "}{".join(value) + "}"
    targets = []
    for page in pdf.pages:
        for indirect in page.get("/Annots", []):
            annotation = indirect.get_object()
            action = annotation.get("/A", {})
            if action.get("/S") == "/GoTo":
                targets.append(str(action["/D"]))
            elif "/Dest" in annotation:
                targets.append(str(annotation["/Dest"]))
    checks = []
    for primary, alias in PAIRS:
        assert records[primary] == records[alias]
        assert records[primary + "@cref"] == records[alias + "@cref"]
        ordinary = groups(groups(records[primary])[0])
        cref = groups(groups(records[primary + "@cref"])[0])
        assert len(ordinary) == len(cref) == 5
        anchor = ordinary[3]
        assert anchor in pdf.named_destinations
        assert targets.count(anchor) == 3
        checks.append({"primary": primary, "alias": alias,
                       "ordinary_record_both": records[primary],
                       "cref_record_both": records[primary + "@cref"],
                       "destination_exists": True, "pdf_link_count": 3})
    diagnostic = {key: value for key, value in records.items() if "c9:" in key}
    if name == "exact_input":
        assert "c9:ordinary-after" not in records
        assert "[equation]{c9:ordinary-after}" in records
    else:
        for label, expected in [("c9:ordinary-before", "1.1"), ("c9:ordinary-after", "1.10"), ("c9:reset", "2.1")]:
            assert groups(groups(records[label])[0])[0] == expected
    issues = [line for line in tex.with_suffix(".log").read_text().splitlines()
              if re.search(r"undefined|Overfull|Missing character|LaTeX Font Warning|destination with the same identifier", line)]
    if name == "plain_control":
        assert issues == []
    evidence[name] = {"tex_sha256": hashlib.sha256(tex.read_bytes()).hexdigest(),
                      "aux_sha256": hashlib.sha256(tex.with_suffix(".aux").read_bytes()).hexdigest(),
                      "pdf_sha256": hashlib.sha256(tex.with_suffix(".pdf").read_bytes()).hexdigest(),
                      "kernel": "2026-11-01", "pairs": checks,
                      "diagnostic_records": diagnostic, "final_log_issues": issues}
path = ROOT / "code/S6_SERIES_PUBLISH_c9_current_alias_evidence.json"
path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", newline="\n")
print("Retained exact observed records:", path)
print("Exact input: 7 ordinary pairs, 7 five-field @cref pairs, 7 destinations, 21 links; optional-control failure preserved.")
print("Plain control: same 7 pairs/destinations and 21 links; three controls correct; final diagnostic list empty.")
