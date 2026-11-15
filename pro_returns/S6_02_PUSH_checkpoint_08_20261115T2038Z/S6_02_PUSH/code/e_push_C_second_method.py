#!/usr/bin/env python3
"""Exact arithmetic audit for C.3.26--C.3.27; geometry is proved in the text."""
from pathlib import Path
from fractions import Fraction
import csv
import json
import sympy as sp

root = Path(__file__).resolve().parents[1]
p, k, r, lam = sp.symbols("p k r lambda", integer=True)
mu = (6*p-3*k)/sp.Integer(896) - (p+k)/sp.Integer(192) + k/sp.Integer(384)
index = (p-4*k)/sp.Integer(24)
assert sp.simplify(mu-index/28) == 0
assert sp.simplify(index.subs({p:p+4*r, k:k+r}, simultaneous=True)-index) == 0
assert sp.simplify(mu.subs(p,4*k+24*lam)-lam/28) == 0
six = -Fraction(126,896)+Fraction(30,192)-Fraction(6,384)
assert six == 0
kernel_six_mod28 = [n for n in range(28) if 6*n % 28 == 0]
assert kernel_six_mod28 == [0,14]
result = {
    "status": "PASS",
    "spin_c_conversion": str(sp.factor(mu)),
    "direct_integer": str(index),
    "framing_change": "(p,k) -> (p+4r,k+r) leaves lambda unchanged",
    "spin_index_congruence": "p=4k+24*lambda gives mu=lambda/28",
    "actual_six_loop_mu": str(six),
    "kernel_of_six_in_Z28": kernel_six_mod28,
    "scope": "Exact arithmetic only; annular and pair-of-pants bordisms, actual boundary identification, and normal-framing comparison are geometric proofs in C.3.25--C.3.27."
}
stem = Path(__file__).with_suffix("")
stem.with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
stem.with_suffix(".out").write_text(json.dumps(result, indent=2)+"\n")

columns = ["id","statement","status","where_proved","depends_on","item_of_the_prompt","R_items_and_Leads_used","notes"]
rows = {
    "C_index_additivity_results.csv": {
        "id": "C.3.26",
        "statement": "The actual surgery-cap index lambda=(p1*x-4*x^3)/24 is integral and additive under composition, and is independent of equivariant isotopies and fixed-tube normalizations, by direct characteristic bordisms and the vertical Euler identity on a sphere-bundle framing correction.",
        "status": "Proved",
        "where_proved": "sections/C_index_additivity.tex C.3.26",
        "depends_on": "geometric cap of C.3.14;actual bordism of C.3.20;spin Dirac index;Smale1959E;code/e_push_C_second_method.py",
        "item_of_the_prompt": "C.1;C.3;Lead 7",
        "R_items_and_Leads_used": "R6;R12;R13;Lead7",
        "notes": "No three-knot integer, Wall formula or Davis generator comparison is used. Individual cubic and Pontryagin pairings are additive for fixed-tube-relative maps; only their index combination is framing independent."
    },
    "C_independent_monodromy_value_results.csv": {
        "id": "C.3.27",
        "statement": "A second determination gives the actual one-loop monodromy zero: the direct characteristic index has lambda(six-loop)=0, integer additivity forces lambda(Phi)=0, and the actual eight-dimensional spin-c coboundary gives mu(Phi)=lambda(Phi)/28=0.",
        "status": "Proved",
        "where_proved": "sections/C_independent_monodromy_value.tex C.3.27",
        "depends_on": "C.1.1;C.1.2;C.3.5;C.3.6;C.3.10;C.3.18-C.3.22;C.3.25;C.3.26;code/e_push_C_second_method.py",
        "item_of_the_prompt": "C.1;C.3;Lead 6;Lead 7",
        "R_items_and_Leads_used": "R2;R6;R8;R12;R13;Lead6;Lead7",
        "notes": "Independent boundary-invariant and integer-before-mod28 arguments avoid C.3.23-C.3.24 and Wall-Davis. The actual annular representative and p,k geometry are shared inputs, explicitly disclosed. The specific analytic B.4 filling and its Chern data remain Open."
    }
}
for filename, row in rows.items():
    with (root/"sections"/filename).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerow(row)
print(json.dumps(result, indent=2))
