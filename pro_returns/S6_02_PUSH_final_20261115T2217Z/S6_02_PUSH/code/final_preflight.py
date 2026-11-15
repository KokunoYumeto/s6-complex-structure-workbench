#!/usr/bin/env python3
"""Verify the completed deliverable and every preserved checkpoint byte stream."""
from pathlib import Path
import collections, csv, datetime, hashlib, json, re, zipfile
import fitz

root = Path(__file__).resolve().parents[1]
tag = "draft34"
audit = json.loads((root/"code"/f"deliverable_audit_{tag}.json").read_text())
assert audit["passed"]
build = json.loads((root/"build_logs"/f"{tag}_summary.json").read_text())
assert len(build) == 4 and all(row["returncode"] == 0 and not row["overfull_pt"] for row in build)
qa = json.loads((root/"qa"/tag/"visual_inspection.json").read_text())
assert not qa["observed_issues"] and qa["compiler_overfull_boxes"] == 0
with (root/"S6_02_PUSH_results.csv").open(newline="") as stream:
    reader = csv.DictReader(stream)
    assert reader.fieldnames == ["id", "statement", "status", "where_proved", "depends_on",
                                 "item_of_the_prompt", "R_items_and_Leads_used", "notes"]
    rows = list(reader)
statuses = collections.Counter(row["status"] for row in rows)
assert len(rows) == 154 and statuses == {"Proved":137, "Refuted":9, "Known":8}
registry = {row["id"]: row for row in rows}
for identity in ["B.4.1", "B.5.1", "C.5.1"]:
    assert registry[identity]["status"] == "Refuted"
assert registry["B.4.33"]["status"] == "Proved"
report = (root/"S6_02_PUSH_report.md").read_text()
assert report.startswith("| Item |")
assert "There are no current Open rows." in report
assert "**236 pages**" in report and "**34 distinct pages**" in report
assert "481 explicitly retained changed checkpoint versions" in report
doc = fitz.open(root/"S6_02_PUSH_paper.pdf")
assert len(doc) == qa["pdf_pages"] == 236
assert "INCOMPLETE" not in doc[0].get_text()
for key, first, last in [("B433",109,113),("B430",98,103)]:
    assert set(range(first,last+1)).issubset(qa["visually_inspected_pages"]), key

history = []
checked = 0
for archive in sorted(root.parent.glob("S6_02_PUSH_checkpoint_*.zip")):
    number = archive.stem.rsplit("_",1)[1]
    count = 0
    with zipfile.ZipFile(archive) as old:
        assert old.testzip() is None
        for item in old.infolist():
            if item.is_dir():
                continue
            prefix = root.name + "/"
            assert item.filename.startswith(prefix)
            relative = Path(item.filename[len(prefix):])
            data = old.read(item)
            current = root / relative
            retained = root / "retained" / ("checkpoint_"+number) / relative
            assert (current.exists() and current.read_bytes() == data) or (
                    retained.exists() and retained.read_bytes() == data), (archive.name, str(relative))
            count += 1
    checked += count
    history.append({"archive":archive.name,"file_versions_verified":count,
                    "sha256":hashlib.sha256(archive.read_bytes()).hexdigest()})
assert len(history) == 9
pdfs = [str(path.relative_to(root)) for path in root.rglob("*.pdf")]
assert all(path == "S6_02_PUSH_paper.pdf" or (
    path.startswith("retained/checkpoint_") and path.endswith("/S6_02_PUSH_paper.pdf")) for path in pdfs)
for forbidden in ["background", "external_sources", "tex_runtime", "upload"]:
    assert not (root/forbidden).exists(), forbidden
record = {"verified_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "passed":True,"scope":"Artifact consistency, rendered-page record, exact retention and exclusion checks; not a formal proof checker.",
          "build":tag,"pdf_pages":len(doc),"statement_rows":len(rows),"statuses":dict(statuses),
          "bibliography_entries":audit["bibliography_entries"],"visual_pages":len(qa["visually_inspected_pages"]),
          "all_compiler_returncodes_zero":True,"overfull_boxes":0,"integration_passed":True,
          "checkpoint_archives":len(history),"checkpoint_file_versions_verified":checked,
          "checkpoint_integrity":history,
          "paper_sha256":hashlib.sha256((root/"S6_02_PUSH_paper.pdf").read_bytes()).hexdigest(),
          "retained_changed_versions":481,"external_inputs_and_scans_excluded":True}
(root/"code/final_preflight.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))
