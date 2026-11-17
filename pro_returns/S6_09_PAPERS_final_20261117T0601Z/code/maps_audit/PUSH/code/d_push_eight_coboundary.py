#!/usr/bin/env python3
"""Exact characteristic pairing checks for the actual C.3.25 coboundary."""
from pathlib import Path
import json
import sympy as sp

p, k = sp.symbols("p k", integer=True)
Q = sp.Matrix([[k, 1], [1, 0]])
assert Q.det() == -1
Qi = Q.inv()
assert Qi == sp.Matrix([[0, 1], [1, -k]])
pvec = sp.Matrix([p+k, 3])
cvec = sp.Matrix([k, 1])
p_sq = sp.expand((pvec.T*Qi*pvec)[0])
pc_sq = sp.expand((pvec.T*Qi*cvec)[0])
c_four = sp.expand((cvec.T*Qi*cvec)[0])
assert p_sq == 6*p-3*k
assert pc_sq == p+k
assert c_four == k
mu = sp.factor(p_sq/sp.Integer(896)-pc_sq/sp.Integer(192)
               +c_four/sp.Integer(384))
assert sp.simplify(mu-(p-4*k)/672) == 0
# Euler sequence on CP2: c1=3H, c2=3H^2.
assert 3**2-2*3 == 3
actual = []
for sign in (-1, 1):
    sub = {p: -24*sign, k: -6*sign}
    assert mu.subs(sub) == 0
    actual.append({"common_cap_sign": sign,
                   "Q": [[int(v.subs(sub)) for v in row]
                         for row in Q.tolist()],
                   "p1_squared": int(p_sq.subs(sub)),
                   "p1_c_squared": int(pc_sq.subs(sub)),
                   "c_fourth": int(c_four.subs(sub)),
                   "signature": 0,
                   "mu": "0"})
# Independently calibrate the framing-only direction p=4k.
assert mu.subs(p, 4*k) == 0
result = {"statement": "C.3.25", "status": "PASS",
          "intersection_determinant": -1,
          "intersection_inverse": str(Qi),
          "p1_squared": str(p_sq), "p1_c_squared": str(pc_sq),
          "c_fourth": str(c_four), "spin_c_mu": str(mu),
          "actual_six_loop_cases": actual,
          "pure_framing_direction_mu": "0",
          "geometric_boundary_identification":
          "proved in the accompanying text, not inferred from this arithmetic"}
serialized = json.dumps(result, indent=2)
Path(__file__).with_suffix(".json").write_text(serialized+"\n")
print(serialized)
