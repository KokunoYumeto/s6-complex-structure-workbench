#!/usr/bin/env python3
"""Check the integrated numbered registry, inputs, citations and final build log.

This is an artifact-consistency check, not an independent proof of the
mathematics. Historical files under retained/ are intentionally excluded.
"""
from pathlib import Path
import csv, json, re, sys

root = Path(__file__).resolve().parents[1]
seen = set()
sources = []


def read_tree(path):
    path = path.resolve()
    if path in seen:
        return
    seen.add(path)
    text = path.read_text()
    sources.append((path, text))
    for relative in re.findall(r"\\input\{([^}]+)\}", text):
        target = root / relative
        if target.suffix != ".tex":
            target = target.with_suffix(".tex")
        assert target.is_file(), str(target)
        read_tree(target)


read_tree(root / "S6_02_PUSH_paper.tex")
statements = {}
for path, text in sources:
    for header in re.findall(
        r"\\begin\{(?:theorem|proposition|lemma|corollary|problem|remark|claim)\}\[([^]]+)\]",
        text,
    ):
        # A heading such as "Scope after E.2.6" refers to a statement;
        # it does not declare another numbered statement with that ID.
        match = re.match(r"\s*([A-E]\.\d+\.\d+)\b", header)
        if match:
            identity = match.group(1)
            assert identity not in statements, (identity, path)
            status = next((s for s in ("Open", "Refuted", "Known", "Proved") if s in header), None)
            assert status, (identity, header)
            statements[identity] = {"status": status, "source": str(path.relative_to(root))}

with (root / "S6_02_PUSH_results.csv").open(newline="") as stream:
    rows = list(csv.DictReader(stream))
registry = {row["id"]: row for row in rows}
assert len(registry) == len(rows)
missing_in_registry = sorted(set(statements) - set(registry))
not_integrated = sorted(set(registry) - set(statements))
status_mismatches = [
    {"id": identity, "paper": entry["status"], "registry": registry[identity]["status"]}
    for identity, entry in statements.items()
    if identity in registry and entry["status"] != registry[identity]["status"]
]

bib = (root / "S6_02_PUSH_references.bib").read_text()
entries = {}
for chunk in re.split(r"(?=@\w+\s*\{)", bib):
    match = re.match(r"@\w+\s*\{\s*([^,\s]+)", chunk)
    if match:
        entries[match.group(1)] = chunk
missing_open_status = [key for key, entry in entries.items() if not re.search(r"\bopened\b", entry, re.I)]
cited = set()
for _, text in sources:
    for keys in re.findall(r"\\(?:cite\w*|nocite)(?:\[[^]]*\])*\{([^}]+)\}", text):
        cited.update(keys.split(","))
missing_citations = sorted(cited - set(entries))

tag = sys.argv[1] if len(sys.argv) > 1 else "draft11"
logfile = root / "build_logs" / f"{tag}_4.txt"
log = logfile.read_text() if logfile.is_file() else ""
overfull = [float(x) for x in re.findall(r"Overfull \\[hv]box \(([0-9.]+)pt", log)]
unresolved = [line for line in log.splitlines()
              if "undefined" in line.lower() or "Rerun to get" in line or "rerunfilecheck Warning" in line]

result = {
    "integrated_tex_sources": len(sources), "numbered_statements": len(statements),
    "registry_rows": len(rows), "missing_in_registry": missing_in_registry,
    "registry_not_integrated": not_integrated, "status_mismatches": status_mismatches,
    "bibliography_entries": len(entries), "missing_opened_status": missing_open_status,
    "missing_citation_keys": missing_citations, "build_tag": tag,
    "final_log_present": logfile.is_file(), "final_overfull_pt": overfull,
    "unresolved_final_log_lines": unresolved,
    "scope": "Document integration and typesetting consistency; not mathematical validation.",
}
result["passed"] = not any([missing_in_registry, not_integrated, status_mismatches,
                            missing_open_status, missing_citations, unresolved,
                            any(value > 2 for value in overfull), not logfile.is_file()])
out = root / "code" / f"deliverable_audit_{tag}.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
sys.exit(0 if result["passed"] else 1)
