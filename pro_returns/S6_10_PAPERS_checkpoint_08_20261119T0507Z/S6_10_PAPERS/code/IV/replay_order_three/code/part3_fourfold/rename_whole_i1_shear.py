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


# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    ['code/part3_fourfold/results_mapping.json'], ['notes/part3_whole_i1_shear.tex'], origin='code/part3_fourfold/rename_whole_i1_shear.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
