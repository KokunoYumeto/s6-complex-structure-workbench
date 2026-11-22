"""Append human/model-authored notes only after the named page images were viewed."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("record")
ap.add_argument("manifest")
ap.add_argument("source")
ap.add_argument("--reader", default="root")
ap.add_argument("--paper", default="I")
ap.add_argument("--complete", action="store_true")
args = ap.parse_args()
manifest_path = Path(args.manifest)
manifest = json.loads(manifest_path.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(manifest["pdf"]) == manifest["pdf_sha256"]
record_path = Path(args.record)
record = json.loads(record_path.read_text()) if record_path.exists() else {
    "paper": args.paper,
    "reader": args.reader,
    "source_sha256": sha(args.source),
    "pdf_sha256": manifest["pdf_sha256"],
    "manifest_sha256": sha(manifest_path),
    "created_utc": now,
    "scope": "Actual complete rendered page images individually viewed and read. No mathematical check event is inferred.",
    "pages": [],
}
assert record["source_sha256"] == sha(args.source)
assert record["pdf_sha256"] == manifest["pdf_sha256"]
by_page = {row["page"]: row for row in manifest["rendered_pages"]}
already = {row["page"] for row in record["pages"]}
import sys
notes = json.load(sys.stdin)
for key, finding in notes.items():
    page = int(key)
    assert page not in already, ("duplicate reading", page)
    row = by_page[page]
    assert sha(row["image"]) == row["image_sha256"]
    assert isinstance(finding, str) and finding.strip()
    record["pages"].append({
        "page": page,
        "image_sha256": row["image_sha256"],
        "pdf_sha256": manifest["pdf_sha256"],
        "finding": finding,
    })
    already.add(page)
record["pages"].sort(key=lambda row: row["page"])
record["updated_utc"] = now
record["page_count"] = len(record["pages"])
if args.complete:
    record["all_assigned_changed_pages_read"] = True
    record["completed_utc"] = now
record_path.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"record": str(record_path), "pages_recorded": len(record["pages"]), "added": sorted(map(int, notes))}))
