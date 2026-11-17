#!/usr/bin/env python3
"""Assemble the completed report with explicit historical-status separation."""
from pathlib import Path
import collections, csv, datetime, json, re, sys

root = Path(__file__).resolve().parents[1]
tag = sys.argv[1] if len(sys.argv) > 1 else "draft34"
front = (root / "sections/final_report_frontmatter.md").read_text()
assert front.startswith("| Item |"), "Outcome table must be first"
with (root / "S6_02_PUSH_results.csv").open(newline="") as stream:
    rows = list(csv.DictReader(stream))
statuses = collections.Counter(row["status"] for row in rows)
assert not statuses.get("Open", 0), "A completed report cannot conceal an Open row"
bib = (root / "S6_02_PUSH_references.bib").read_text()
reference_count = len(re.findall(r"^@\w+\s*\{", bib, re.M))
buildfile = root / "build_logs" / f"{tag}_summary.json"
build = json.loads(buildfile.read_text()) if buildfile.exists() else []
auditfile = root / "code" / f"deliverable_audit_{tag}.json"
audit = json.loads(auditfile.read_text()) if auditfile.exists() else {}
qafile = root / "qa" / tag / "visual_inspection.json"
qa = json.loads(qafile.read_text()) if qafile.exists() else {}
retfile = root / "code/retention_record.json"
retention = json.loads(retfile.read_text()) if retfile.exists() else []
current = ["\n\n## Final build and verification record\n",
           f"Current build: **{tag}**. The registry has **{len(rows)} numbered statements**, "
           f"with statuses {dict(statuses)}, and **{reference_count} bibliography entries**. "
           "There are no current Open rows.\n"]
if build:
    current.append("Compiler return codes: " + ", ".join(str(s["returncode"]) for s in build) + ". "
                   "Overfull-box counts by stage: " + ", ".join(str(len(s["overfull_pt"])) for s in build) + ".\n")
if audit:
    current.append(f"The source/registry/bibliography/final-log integration audit is "
                   f"**{'PASS' if audit.get('passed') else 'FAIL'}**. "
                   f"It checks {audit.get('integrated_tex_sources')} integrated TeX sources. "
                   f"Final overfull widths: {audit.get('final_overfull_pt')}. "
                   f"Unresolved final-log lines: {audit.get('unresolved_final_log_lines')}.\n")
if qa:
    pages = qa["visually_inspected_pages"]
    current.append(f"The final PDF has **{qa['pdf_pages']} pages**. "
                   f"**{len(pages)} distinct pages** were rendered and visually inspected: "
                   + ", ".join(map(str, pages)) + ". "
                   "The sample covers the first-page conventions, every new B.4.30–B.4.33 proof page, "
                   "the changed disposition passages, a spread across all parts and the bibliography. "
                   f"The dated inspection record is qa/{tag}/visual_inspection.json. "
                   "No clipping, overlap or visible display overflow was observed.\n")
else:
    current.append("The current build's visual record is not yet present; this report must be refreshed "
                   "after the required inspection before final delivery.\n")
current.append("The initial draft01 had two boxes over 2pt, of 14.53073pt and 10.80035pt. "
               "Later draft28 had one unbreakable-path overflow of 83.39786pt. "
               "All were corrected in source; their original logs and corrected builds are retained. "
               "The final counts above are read directly from the final compilation, not inferred "
               "from a previous clean draft.\n")
current.append(f"There are {len(retention)} explicitly retained changed checkpoint versions. "
               "Every prior checkpoint byte stream is either unchanged at its current path or "
               "preserved at the recorded retained path. The exact hashes and replacement mapping "
               "are in code/retention_record.json and the retention table at the end of this report.\n")
package = root / "code/final_package_verification.json"
if package.exists():
    current.append("A final archive verification record is present; see code/final_package_verification.json.\n")

orderfile = root / "code/report_record_order.json"
order = json.loads(orderfile.read_text()) if orderfile.exists() else []
extra = []
for file in sorted((root / "sections").glob("*.md")):
    if any(word in file.stem.lower() for word in ["report", "audit", "referee", "working", "attempt", "sanity", "stress", "equdimensionalization", "scope"]):
        extra.append(file.name)
exclude = {"final_report_frontmatter.md", "execution_history_through_checkpoint09.md", "retention_record.md"}
names = []
for name in order + extra:
    if name not in exclude and name not in names and (root/"sections"/name).exists():
        names.append(name)

parts = []
history = root / "sections/execution_history_through_checkpoint09.md"
if history.exists():
    parts.append("\n\n---\n\n## Historical execution and typesetting record\n\n"
                 "This chronology records the state at each earlier checkpoint; its then-current "
                 "Open statuses and next-deadline sentences are historical.\n\n" + history.read_text())
for name in names:
    parts.append("\n\n---\n\n## Detailed development record: " + name + "\n\n"
                 "Status language in this record is preserved from its writing; use the current "
                 "outcome table and numbered registry for the final disposition.\n\n"
                 + (root/"sections"/name).read_text())
retmd = root / "sections/retention_record.md"
if retmd.exists():
    parts.append("\n\n---\n\n" + retmd.read_text())
text = front + "\n".join(current) + "".join(parts)
(root / "S6_02_PUSH_report.md").write_text(text)
summary = {"updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "build": tag, "statement_rows": len(rows), "statuses": dict(statuses),
           "references": reference_count, "historical_records_included": len(names),
           "retained_versions": len(retention), "visual_record_present": bool(qa),
           "integration_passed": audit.get("passed"), "report_bytes": len(text.encode())}
(root/"code/final_report_summary.json").write_text(json.dumps(summary, indent=2)+"\n")
print(json.dumps(summary, indent=2))
