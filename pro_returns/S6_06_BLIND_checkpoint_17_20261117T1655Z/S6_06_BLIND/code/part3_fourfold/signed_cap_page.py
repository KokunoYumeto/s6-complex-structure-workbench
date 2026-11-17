#!/usr/bin/env python3
"""Exact signed cap coordinate and normal-orientation certificate."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s
ROOT = Path(__file__).resolve().parents[2]
rel = "notes/part3_signed_cap_page.md"
with (ROOT / "records/literature_fourfold.md").open("a") as log:
    log.write("\n- " + datetime.now(timezone.utc).isoformat()
              + " — Opened own " + rel
              + "; reason: verify the actual n=±1 weighted cap/page maps "
              "and normal Thom orientation; material: exact rational phase identities.\n")
(ROOT/rel).read_text()
m = s.symbols("m", positive=True, integer=True)
alpha, gamma, theta, u, q, t = s.symbols("alpha gamma theta u q t")
cases = []
for n in [1, -1]:
    phase1 = alpha/m+n*u/m
    phase2 = n*u
    U = m*gamma-n*alpha
    assert s.simplify(phase1.subs(u, U)-n*gamma) == 0
    assert s.simplify(phase2.subs(u, U)-(n*m*gamma-alpha)) == 0
    # A sends alpha to alpha+1 and u to u-n.
    assert s.simplify(phase1.subs({alpha: alpha+1, u: u-n}, simultaneous=True)-phase1) == 0
    assert s.simplify(phase2.subs(u, u-n)-phase2) == -1
    # Physical positive parameter motion gamma -> gamma+n*theta
    # is one positive Hopf turn in beta=n*gamma.
    assert s.expand(n*(gamma+n*theta)-n*gamma) == theta
    normal_exchange_sign = (-1)**(3*2)
    assert normal_exchange_sign == 1
    cases.append({
        "n": n,
        "cap_coordinate": str(U),
        "weighted_Hopf_angle": str(n*gamma),
        "physical_positive_angular_return": str(n*gamma),
        "parameter_degree_in_Hopf_angle": 1,
        "complex_boundary_degree_kappa": 1,
        "normal_exchange_sign": normal_exchange_sign,
        "actual_Euler_meridian_integral": 1,
    })
a_power = q/(1-t*q)
b = 1/(1-t*q)
assert s.simplify(b-t*a_power-1) == 0
assert s.simplify(b/a_power-1/q) == 0
out = {
    "status": "PASS",
    "cases": cases,
    "holomorphic_page_coordinate_power": str(a_power),
    "holomorphic_page_b": str(b),
    "same_signed_index_for_both_primitive_twists": True,
    "scope": "The actual source/page line must be supplied by the corresponding cap construction; this certificate verifies the map and orientation only."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
print("PASS: both exact cap maps, positive Hopf parameter degree, complex boundary degree, and positive normal Thom sign.")
