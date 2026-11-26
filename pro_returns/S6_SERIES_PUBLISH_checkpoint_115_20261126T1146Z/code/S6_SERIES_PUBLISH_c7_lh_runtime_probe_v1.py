#!/usr/bin/env python3
"""Bounded timing probe for the running new LH reversible integer routine."""
import json
from pathlib import Path
from time import perf_counter
from sympy import Matrix, eye, zeros
from S6_SERIES_PUBLISH_c7_lh_integral import invariants, kernel

ROOT = Path(__file__).resolve().parents[1]
path = ROOT/"agents/continuation7_iii_weighted_catalogue/S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json"
row = json.loads(path.read_text())["rows"][0]
A = Matrix(row["monodromies"][0])
S = Matrix.diag(1,1,1,1001)
A = S.inv()*A*S
F, inverse = kernel(A-eye(4))
start = perf_counter()
for i in range(10):
    v = F*Matrix([i+1,1])
    core = Matrix.hstack(Matrix.vstack(A-eye(4),zeros(1,4)),Matrix.vstack(-v,Matrix([16])))
    result = invariants(core)
elapsed = perf_counter()-start
print("PROBE ten exact five-generator core Smith computations:", elapsed, "seconds")
print("LAST_INVARIANTS", result)
print("SCOPE timing only; no mathematical completeness credit.")
