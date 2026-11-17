#!/usr/bin/env python3
"""Apply root's reserved statement number without touching other exports."""
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[2]
for rel in ("notes/part3_whole_i1_shear.md", "code/part3_fourfold/whole_i1_shear.py"):
    p = ROOT / rel
    with (ROOT / "records/literature_fourfold.md").open("a") as log:
        log.write("\n- " + datetime.now(timezone.utc).isoformat()
                  + " — Opened own " + rel
                  + "; reason: root reserved P3K.24 for the reduced-III return; "
                  "material: renumber this independent shear proof P3K.25 only.\n")
    p.write_text(p.read_text().replace("P3K.24", "P3K.25"))
print("Renumbered the submitted whole-I1 shear statement P3K.25.")
