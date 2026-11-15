#!/usr/bin/env python3
"""Exact weighted-line counts used in the degree-one Leray argument.

The geometric direct-image and degeneration theorems are proved/cited in
sections/B_hodge_obstruction.tex; this program certifies only the finite counts.
"""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]

def monomials(degree, weights=(3, 4)):
    if degree < 0:
        return []
    a, b = weights
    return [(i, j) for i in range(degree // a + 1)
            for j in range(degree // b + 1) if a*i + b*j == degree]

record = {
    "weighted_curve": "P(3,4)",
    "canonical_degree": -7,
    "H0_O": monomials(0),
    "H0_O_minus1": monomials(-1),
    "H1_O_by_Serre_duality": monomials(-7),
    "H1_X_O_from_Leray": len(monomials(0)) + len(monomials(-1)),
    "b1_S6": 0,
    "hypothetical_E1_degeneration_impossible": True,
}
assert record["H1_X_O_from_Leray"] == 1
assert not record["H1_O_by_Serre_duality"]
assert record["H1_X_O_from_Leray"] > record["b1_S6"]
(root/"code"/"b_hodge_obstruction.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
print("PASS: the cited E1-degeneration conclusion contradicts the exact degree-one counts.")
