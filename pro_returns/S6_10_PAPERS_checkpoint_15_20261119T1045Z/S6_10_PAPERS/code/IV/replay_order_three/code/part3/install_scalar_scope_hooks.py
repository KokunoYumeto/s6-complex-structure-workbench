#!/usr/bin/env python3
"""Install reproducible scope flags on the historical scalar generators.

All originals and the exact appended footer are retained. This does not run
the historical proof exporters or modify their mathematical derivations.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
MARKER = "# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION"
CONFIG = {
 "code/part3/canonical_scalar_catalogue.py": (["code/part3/canonical_scalar_catalogue.json"], []),
 "code/part3/os49_full_framing.py": (["code/part3/os49_full_framing.json"], []),
 "code/part3/liu_rollenske_parameter.py": (["code/part3/liu_rollenske_parameter.json"], []),
 "code/part3/fixed_source_cap_loops.py": (["code/part3/fixed_source_cap_loops.json"], []),
 "code/part3/moving_order_one_sites.py": (["code/part3/moving_order_one_sites.json"], []),
 "code/part3/os49_cap_loops.py": (["code/part3/os49_cap_loops.json"], []),
 "code/part3/export_os49_full_framing.py": (["code/part3/os49_full_framing_results_mapping.json"], ["notes/part3_os49_full_framing.tex"]),
 "code/part3/export_liu_rollenske_parameter.py": (["code/part3/liu_rollenske_parameter_results_mapping.json"], ["notes/part3_liu_rollenske_parameter.tex"]),
 "code/part3/export_fixed_source_cap_loops.py": (["code/part3/results_mapping.json"], ["notes/part3_fixed_source_cap_loops.tex"]),
 "code/part3/export_moving_order_one_sites.py": (["code/part3/results_mapping.json"], ["notes/part3_moving_order_one_sites.tex"]),
 "code/part3/export_os49_cap_loops.py": (["code/part3/results_mapping.json"], ["notes/part3_os49_cap_loops.tex"]),
 "code/part3_fourfold/cox_flop.py": (["code/part3_fourfold/cox_flop.json"], []),
 "code/part3_fourfold/whole_i1_shear.py": (["code/part3_fourfold/whole_i1_shear.json"], []),
 "code/part3_fourfold/common_exterior_meridians.py": (["code/part3_fourfold/common_exterior_meridians.json"], []),
 "code/part3_fourfold/common_exterior_frame_recurrence.py": (["code/part3_fourfold/common_exterior_frame_recurrence.json"], []),
 "code/part3_fourfold/original_cox_descent_universal.py": (["code/part3_fourfold/original_cox_descent_universal.json"], []),
 "code/part3_fourfold/weighted_shorter_loop.py": (["code/part3_fourfold/weighted_shorter_loop.json"], []),
 "code/part3_fourfold/os49_shorter_loop.py": (["code/part3_fourfold/os49_shorter_loop.json"], []),
 "code/part3_fourfold/finalize_flop.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_fourfold.tex"]),
 "code/part3_fourfold/export_trace_tex.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_fourfold.tex"]),
 "code/part3_fourfold/export_whole_i1_shear.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_whole_i1_shear.tex"]),
 "code/part3_fourfold/rename_whole_i1_shear.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_whole_i1_shear.tex"]),
 "code/part3_fourfold/export_common_exterior_meridians.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_common_exterior_meridians.tex"]),
 "code/part3_fourfold/export_common_exterior_frame_recurrence.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_common_exterior_frame_recurrence.tex"]),
 "code/part3_fourfold/export_original_cox_descent.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_original_cox_descent.tex"]),
 "code/part3_fourfold/export_weighted_shorter_loop.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_weighted_shorter_loop.tex"]),
 "code/part3_fourfold/export_os49_shorter_loop.py": (["code/part3_fourfold/results_mapping.json"], ["notes/part3_os49_shorter_loop.tex"]),
}

stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
archive = ROOT / "records/attempts/scalar_fan_dependency_correction" / stamp
changes = []
for rel, (json_paths, tex_paths) in CONFIG.items():
    p = ROOT / rel
    if not p.exists():
        raise FileNotFoundError(p)
    old = p.read_text()
    if MARKER in old:
        continue
    footer = "\n\n" + MARKER + "\n" + f'''\
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    {json_paths!r}, {tex_paths!r}, origin={rel!r})
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
'''
    backup = archive / rel
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_text(old)
    new = old + footer
    compile(new, rel, "exec")
    p.write_text(new)
    changes.append({
        "file": rel, "original": str(backup.relative_to(ROOT)),
        "before_sha256": hashlib.sha256(old.encode()).hexdigest(),
        "after_sha256": hashlib.sha256(new.encode()).hexdigest(),
        "operation": "append scope-only postprocessor",
        "old_footer": None, "new_footer": footer,
        "mathematical_code_changed": False,
    })
if changes:
    (archive / "generator_changes.json").write_text(json.dumps({
        "utc": datetime.now(timezone.utc).isoformat(),
        "main_input_modified": False,
        "generators_executed": False,
        "changes": changes,
    }, indent=2) + "\n")
print("Installed and syntax-checked", len(changes), "scope hooks; mathematical generator bodies unchanged.")
