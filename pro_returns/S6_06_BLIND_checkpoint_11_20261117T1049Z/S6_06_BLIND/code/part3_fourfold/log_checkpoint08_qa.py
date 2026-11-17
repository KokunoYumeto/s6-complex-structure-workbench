#!/usr/bin/env python3
"""Record the read-only checkpoint08 pages assigned by root."""
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[2]
with (ROOT / "records/literature_fourfold.md").open("a") as log:
    for number in range(18, 23):
        path = f"records/render_checkpoint08/contact_{number}.png"
        log.write("\n- " + datetime.now(timezone.utc).isoformat()
                  + " — Opened current-team " + path
                  + "; reason: root-assigned visual QA of frozen build34; "
                  "material: check clipping, collisions, missing symbols, and equations only.\n")
    for number in [295, 299, 305, 317]:
        path = f"records/render_checkpoint08/page_{number:03d}.png"
        log.write("\n- " + datetime.now(timezone.utc).isoformat()
                  + " — Opened current-team " + path
                  + "; reason: full-size inspection of dense equations, table, and bibliography "
                  "after contact-sheet QA; material: visual layout only.\n")
print("Logged checkpoint08 contact sheets 18–22 for read-only visual QA.")
