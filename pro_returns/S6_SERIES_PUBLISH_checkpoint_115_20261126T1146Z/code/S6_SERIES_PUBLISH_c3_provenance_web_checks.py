#!/usr/bin/env python3
"""Retrieve link/authorship metadata without retaining remote source content."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import urllib.request

root = Path(__file__).resolve().parents[1]
rows = []
for key, url in [
    ("records_II", "https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-ii"),
    ("authorship", "https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/bc08b5278bcad2beb70b6862c5722f1b9f636db6/README.md")]:
    req = urllib.request.Request(url, headers={"User-Agent":"publication-source-verification/1.0"})
    with urllib.request.urlopen(req, timeout=45) as reply:
        data, status, final = reply.read(), reply.status, reply.url
    source_text = data.decode("utf-8")
    checks = ({"paper_ii_anchor":"user-content-paper-ii" in source_text}
              if key == "records_II" else
              {"sol_named":"GPT-5.6 Sol" in source_text,
               "astra_named":"GPT-6 Astra" in source_text,
               "ultra_named":"ultra" in source_text})
    rows.append(dict(key=key, url=url, date_utc=datetime.now(timezone.utc).isoformat(),
        http_status=status, final_url=final, bytes=len(data),
        sha256=hashlib.sha256(data).hexdigest(), checks=str(checks)))
out = root / "agents" / "continuation3_provenance" / "S6_SERIES_PUBLISH_c3_provenance_web_metadata.tsv"
with out.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
summary = json.dumps(rows, indent=2) + "\n"
(root / "code" / "S6_SERIES_PUBLISH_c3_provenance_web_checks.out").write_text(summary)
print(summary)
