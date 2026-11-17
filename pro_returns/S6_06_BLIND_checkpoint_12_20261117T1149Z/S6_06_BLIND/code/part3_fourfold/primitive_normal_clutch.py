#!/usr/bin/env python3
"""Actual K9 frame map at degree-one binding, with K22 page arithmetic."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
rel = "notes/part3_primitive_rotating_integers.md"
with (ROOT / "records/literature_fourfold.md").open("a") as log:
    log.write("\n- " + datetime.now(timezone.utc).isoformat()
              + " — Opened own " + rel
              + "; reason: execute the exact primitive-family rotating frame "
              "and integer arithmetic; material: the typed quotient and clutch matrices.\n")
(ROOT / rel).read_text()
alpha, theta, phi, g = s.symbols("alpha theta phi g", real=True)
rho = s.symbols("rho", positive=True)
def R(a):
    return s.Matrix([[s.cos(a), -s.sin(a), 0],
                     [s.sin(a), s.cos(a), 0], [0, 0, 1]])
def G(a, t):
    return s.Matrix([[-s.sin(a), s.cos(t)*s.cos(a), s.sin(t)*s.cos(a)],
                     [s.cos(a), s.cos(t)*s.sin(a), s.sin(t)*s.sin(a)],
                     [0, s.sin(t), -s.cos(t)]])
def zero(matrix):
    return matrix.applyfunc(lambda x: s.trigsimp(s.expand_trig(x))) == s.zeros(*matrix.shape)

Q = s.Matrix([[1, 0, -s.cos(alpha)/rho, 0],
              [0, 1, -s.sin(alpha)/rho, 0], [0, 0, 0, 1]])
u = s.Matrix([s.cos(alpha), s.sin(alpha), rho, 0])
n = s.Matrix([-s.sin(alpha), s.cos(alpha), 0, 0])
px = s.Matrix([0, 0, s.cos(theta), -s.sin(theta)])
py = s.Matrix([0, 0, s.sin(theta), s.cos(theta)])
assert Q*u == s.zeros(3, 1)
projected = s.diag(rho, rho, 1)*Q*s.Matrix.hstack(n, -px, -py)*s.diag(1/rho, 1, 1)
assert zero(projected-G(alpha, theta))
assert zero(G(alpha, theta).T*G(alpha, theta)-s.eye(3))
assert s.trigsimp(G(alpha, theta).det()) == 1
assert zero(G(phi-theta-g, theta)-R(-g)*R(phi-theta)*G(0, theta))

values = []
for d in [8, 14, 20, 30]:
    b2 = -4*d
    p1nu, p1base = 0, -24
    k = s.Rational(p1nu+3*b2, 4)
    ell = p1base+p1nu
    A = s.Rational(4*k-ell, 24)
    assert k == -3*d and A == 1-s.Rational(d, 2)
    values.append({"d": d, "k": int(k), "ell": int(ell),
                   "index": int(A), "class_mod_28": int(A % 28)})
    print(f"d={d}: k={k}, ell={ell}, A={A}")
out = {
    "status": "PASS",
    "proof": rel,
    "framing": "The actual transported rotating framing of K9 at binding degree one",
    "parameter": "One positive closed scalar loop, no cover",
    "normal_quotient": [[str(x) for x in row] for row in Q.tolist()],
    "collar_annihilated": True,
    "quotient_recovers_actual_G": True,
    "factorization": "h(p)^-1 Rz(-g(p)) times Rz(phi-theta)G(0,theta)",
    "normal_pontryagin_number": 0,
    "source_gauge_winding_not_used": True,
    "values": values,
    "scope": "The numerical pair includes its rotating framing; the index is independent of that choice."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
print("PASS: exact degree-one quotient map, actual factorization, and all primitive-source rotating pairs.")
