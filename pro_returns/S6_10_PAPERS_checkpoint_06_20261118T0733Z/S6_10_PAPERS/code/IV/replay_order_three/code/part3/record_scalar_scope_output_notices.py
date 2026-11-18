#!/usr/bin/env python3
"""Preserve and annotate previously captured scalar arithmetic output."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from scalar_dependency_scope import ROOT, CERTIFICATES, NOTICE

stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
archive = ROOT / "records/attempts/scalar_fan_dependency_correction" / stamp
changes = []
marker = "POST-CHECKPOINT15 FIELD-SCOPE NOTICE"
for rel in [*CERTIFICATES, "code/part3/canonical_scalar_catalogue.json"]:
    p = (ROOT / rel).with_suffix(".out")
    if not p.exists():
        continue
    old = p.read_text()
    if marker in old:
        continue
    footer = ("\n\n" + marker + "\n" + NOTICE
              + "\nThe current JSON sibling carries the exact field scopes. "
                "The output above is preserved prior arithmetic, not a new "
                "promotion of an all-fan return formula.\n")
    backup = archive / p.relative_to(ROOT)
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_text(old)
    p.write_text(old + footer)
    changes.append({
        "file": str(p.relative_to(ROOT)), "original": str(backup.relative_to(ROOT)),
        "before_sha256": hashlib.sha256(old.encode()).hexdigest(),
        "after_sha256": hashlib.sha256((old+footer).encode()).hexdigest(),
        "old_footer": None, "new_footer": footer,
    })
if changes:
    (archive / "captured_output_changes.json").write_text(json.dumps({
        "utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Annotations only; every prior arithmetic output byte retained",
        "changes": changes,
    }, indent=2) + "\n")
print("Preserved and annotated", len(changes), "captured arithmetic outputs.")
