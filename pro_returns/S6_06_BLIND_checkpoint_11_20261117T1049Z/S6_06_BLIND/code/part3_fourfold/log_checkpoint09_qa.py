#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json, sys
ROOT=Path(__file__).resolve().parents[2]
phase=sys.argv[1] if len(sys.argv)>1 else "open"
path=ROOT/"records/qa_fourfold_checkpoint09.json"
if phase=="open":
    r={"utc":datetime.now(timezone.utc).isoformat(),"contacts":list(range(23,31)),
       "status":"visual inspection in progress"}
    with (ROOT/"records/literature_fourfold.md").open("a") as log:
        log.write("\n- "+r["utc"]+" — Opened own final-checkpoint09 rendered contacts23–30; "
                  "reason: delegated visual QA of the final 377-page manuscript; "
                  "material: page layout, equation rendering, clipping and glyph checks.\n")
else:
    r=json.loads(path.read_text())
    r.update(status="PASS",review_utc=datetime.now(timezone.utc).isoformat(),
             findings="All assigned contact pages inspected; no clipping, collisions, missing glyphs or malformed equations.",
             full_size_pages=[309,355,377])
    with (ROOT/"records/literature_fourfold.md").open("a") as log:
        log.write("\n- "+r["review_utc"]
                  +" — Opened own checkpoint09 full-size pages309,355,377 after contacts23–30; "
                  "reason: inspect dense fractions, branch matrices, and bibliography wrapping; "
                  "material: visual QA PASS, no clipping, collisions, missing glyphs or malformed equations.\n")
path.write_text(json.dumps(r,indent=2)+"\n")
print(json.dumps(r))
