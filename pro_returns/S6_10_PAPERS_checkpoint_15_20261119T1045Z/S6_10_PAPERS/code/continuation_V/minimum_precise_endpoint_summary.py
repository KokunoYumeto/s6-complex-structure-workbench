"""Replay precise endpoints from the independently authored complete-domain run.

This export/replay is not a third independent numerical method.  No original
producer is read or imported.  The earlier coarse-string replay failure remains
preserved separately.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "code/continuation_V"
ctx.dps = 150
threshold_text = "-1.0945402503114027801162682630549457037"
threshold = arb(threshold_text)
specs = {
    "root": HERE / "endpoint_capture/root/minimum_root_regions.json",
    "cusp": HERE / "endpoint_capture/cusp/minimum_cusp_regions.json",
    "collar": HERE / "endpoint_capture/collar/minimum_collar.json",
}
data = {k: json.loads(p.read_text()) for k, p in specs.items()}
assert all(x["status"] == "PASS" for x in data.values())
leaves = {
    "infinity": data["root"]["root_regions"]["infinity"]["accepted"],
    "zero": data["root"]["root_regions"]["zero"]["accepted"],
    "cusp_annulus": data["cusp"]["annulus"]["accepted"],
    "collar": data["collar"]["accepted"],
}
numerators = {
    "infinity": -1094400523035,
    "zero": -1083329522544,
    "cusp_annulus": -1094402439774,
    "collar": -1092202452969,
}
out = {
    "time_utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS",
    "threshold_exact_decimal": threshold_text,
    "scope": "Exact endpoint capture and replay of strict inequalities from the already independently authored continuation programs. This is the same verified method with unrounded lower/upper endpoints retained, not a third independent numerical method. Original first-run outputs remain unchanged.",
    "regions": {},
    "inputs": {},
}
for name, items in leaves.items():
    values = [arb(x["h_lower"]) for x in items]
    bound = arb(numerators[name]) / 10**12
    assert all(x["above_common_exact_threshold"] for x in items)
    assert all(x > threshold for x in values)
    assert all(x > bound for x in values)
    assert bound > threshold
    out["regions"][name] = {
        "leaves": len(items),
        "all_recorded_predicates_pass": True,
        "all_recorded_precise_lower_endpoints_reparse_above_threshold": True,
        "uniform_lower_bound_exact_numerator": numerators[name],
        "uniform_lower_bound_exact_denominator": 10**12,
        "uniform_height_lower_bound": str(bound),
        "uniform_gap_over_threshold_lower": str((bound - threshold).lower()),
    }
for p in specs.values():
    out["inputs"][str(p.relative_to(ROOT))] = {
        "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        "precision_dps": 110,
    }
h = arb(json.loads((HERE / "infinity_and_splitting.json").read_text())["h_b_infinity"])
assert h < threshold
assert arb("-1.094540250311402780116268263054945703726") < h
assert h < arb("-1.094540250311402780116268263054945703725")
out["h_infinity_strictly_below_exact_threshold"] = True
out["printed_h_infinity_interval_verified"] = True
out["total_leaves"] = sum(len(x) for x in leaves.values())
assert out["total_leaves"] == 12911
target = HERE / "minimum_precise_endpoint_summary.json"
prior = HERE / "minimum_precise_endpoint_summary_initial.json"
if target.exists() and not prior.exists():
    prior.write_bytes(target.read_bytes())
target.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"status": out["status"], "leaves": out["total_leaves"], "regions": {k:v["leaves"] for k,v in out["regions"].items()}, "printed_interval": True}))
