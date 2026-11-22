#!/usr/bin/env python3
"""Bind the 21 actual full-image readings already recorded by the edits agent."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/i_cont_edits"
path = OUT / "S6_SERIES_PUBLISH_I_candidate14_reading_edits.json"
mirror = OUT / "S6_SERIES_PUBLISH_I_final_candidate14_reading_edits.json"
source_sha = "1f2d0d376f71e7843265976aeeb72cf8e1ff77aea176ff5dbb4e67446c25b36f"
pdf_sha = "1abe0fc16350045cd2ce0aae57ce377dcfe2400de0b0bf58ba7e559d360bcb37"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
record = json.loads(path.read_text())
manifest = json.loads((ROOT / "render/I_candidate14/manifest.json").read_text())
assert record["source_sha256"] == source_sha == sha(ROOT / "S6_SERIES_PUBLISH_I.tex")
assert record["pdf_sha256"] == pdf_sha == manifest["pdf_sha256"] == sha(Path(manifest["pdf"]))
assert [row["page"] for row in record["pages"]] == list(range(207, 228))
images = {row["page"]: row for row in manifest["rendered_pages"]}
for row in record["pages"]:
    image_row = images[row["page"]]
    assert row["image_sha256"] == image_row["image_sha256"] == sha(Path(image_row["image"]))
    row["image"] = image_row["image"]
    row["reading"] = "entire rendered page explicitly viewed and read"
    row["status"] = "clear"
record.update({"candidate": "I_candidate14", "assigned_pages": list(range(207, 228)),
               "actual_full_image_reading_count": 21,
               "all_assigned_changed_pages_read": True,
               "defects_found": [], "source_edits": 0, "check_events_added": 0,
               "record_identity": "I_candidate14_edits_pages207_227",
               "canonical_record": str(path.relative_to(ROOT)),
               "collector_mirror": str(mirror.relative_to(ROOT)),
               "mirror_scope": "The canonical file and collector-facing mirror contain the same single set of reading evidence; no second reading or independent check is counted.",
               "finalized_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()})
payload = json.dumps(record, indent=2) + "\n"
path.write_text(payload)
mirror.write_text(payload)
assert path.read_bytes() == mirror.read_bytes()
lines = ["# Paper I candidate14: complete changed-page reading, pages 207–227", "",
         "Reader: GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation edits agent, 21 November 2026.", "",
         f"Source SHA-256: `{source_sha}`.", "", f"PDF SHA-256: `{pdf_sha}`.", "",
         "All 21 assigned pages were individually opened as full rendered PNG images and read against the 25-type defect register. No new defect was found in these pages. No source edit or mathematical check event was created by this reading.", "",
         "The collector-facing JSON mirror contains this same reading evidence; it supplies no additional reading or independent check.", "",
         "| Page | Image SHA-256 | Reading finding |", "|---:|---|---|"]
for row in record["pages"]:
    finding = row["finding"].replace("|", "\\|").replace("\n", " ")
    lines.append(f"| {row['page']} | `{row['image_sha256']}` | {finding} |")
(OUT / "S6_SERIES_PUBLISH_I_candidate14_reading_edits.md").write_text("\n".join(lines) + "\n")
print(json.dumps({"pages_read": len(record["pages"]), "range": [207, 227],
                  "defects_found": 0, "check_events_added": 0,
                  "record": str(path.relative_to(ROOT)), "record_sha256": sha(path),
                  "collector_mirror": str(mirror.relative_to(ROOT))}, indent=2))
