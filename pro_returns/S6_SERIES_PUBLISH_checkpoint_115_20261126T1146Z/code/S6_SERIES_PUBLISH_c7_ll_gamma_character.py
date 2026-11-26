#!/usr/bin/env python3
"""Exact finite-character arithmetic for the fresh LL characteristic trace.

Input is this lane's newly derived lattice data, never a historical catalogue.
The geometric trace and Gamma-to-P map are proved in the companion note.
This program proves the coefficient identities, all powers of the finite
action, both clutch matrices, and the resulting seven marked residues.
"""

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

import sympy as sp


BASE = Path(__file__).resolve().parent.parent
LANE = BASE / "agents/continuation7_iii_residual_two_primary"
INPUT = LANE / "S6_SERIES_PUBLISH_III_02LL_fresh_localization_data.json"
OUTPUT = LANE / "S6_SERIES_PUBLISH_III_02LL_fresh_gamma_data.json"
data = json.loads(INPUT.read_text())
z = sp.Symbol("z")


def cyc(values, c):
    """Represent a cyclic coefficient vector, without choosing complex roots."""
    result = [Fraction(0) for _ in range(c)]
    for exponent, value in values:
        result[exponent % c] += value
    return result


def mul(left, right):
    c = len(left)
    return cyc(((i + j, a * b) for i, a in enumerate(left)
                for j, b in enumerate(right)), c)


def polynomial(values):
    return sp.Poly(sum(sp.Rational(x.numerator, x.denominator) * z**i
                       for i, x in enumerate(values)), z, domain=sp.QQ)


def green(c):
    q = [Fraction(-r * (c - r), 2 * c) for r in range(c)]
    d = cyc([(0, 2), (1, -1), (-1, -1)], c)
    assert mul(d, q) == [Fraction(int(i == 0)) - Fraction(1, c)
                         for i in range(c)]
    return q


print("input", INPUT.relative_to(BASE), sha256(INPUT.read_bytes()).hexdigest())
results = []
for row in data["rows"]:
    c = row["c"]
    degree = row["cusp_degree"]
    char = row["cusp_character"]
    t = row["elliptic"]["t"]
    assert row["elliptic"]["character"] % c == 0
    assert row["elliptic"]["degree"] == -1
    assert gcd(t, c) == 1
    assert all(x["isotropy"] in (1, c) for x in row["rank_one"])
    assert sum(x["isotropy"] == c for x in row["rank_one"]) == 1
    assert all(gcd(w, c) == 1 for w in (-1, 1, -t, t))
    # The two other cusp edge slopes are units. Hence no lower-order power
    # acquires another fixed curve, point, or nonfree stratum.
    assert gcd(1 - c * row["cusp"]["kappa"], c) == 1

    q = green(c)
    first = cyc(((r + char, degree * value) for r, value in enumerate(q)), c)
    second = cyc(((r * t, value) for r, value in enumerate(q)), c)
    rational = [x - y for x, y in zip(first, second)]
    # Subtract its constant coefficient times the regular character.
    # This is the unique representative with constant coefficient zero.
    coefficients = [x - rational[0] for x in rational]
    assert all(x.denominator == 1 for x in coefficients)
    coefficients = [int(x) for x in coefficients]
    character = polynomial([Fraction(x) for x in coefficients])
    regular = sp.Poly(sum(z**r for r in range(c)), z, domain=sp.QQ)
    d1 = sp.Poly(2 - z - z**(c - 1), z)
    dt = sp.Poly(2 - z**t - z**((-t) % c), z)
    residual = d1 * dt * character - degree * sp.Poly(z**char, z) * dt + d1
    assert residual.rem(regular).is_zero
    for order in sp.divisors(c):
        if order > 1:
            assert residual.rem(sp.Poly(sp.cyclotomic_poly(order, z), z)).is_zero

    all_powers = []
    primitive = sp.Poly(sp.cyclotomic_poly(c, z), z, domain=sp.QQ)
    for j in range(1, c):
        value = sp.Poly(character.as_expr().subs(z, z**j), z).rem(primitive)
        order = c // gcd(c, j)
        all_powers.append({"power": j, "order": order,
                           "trace_in_Q_z_mod_Phi_c": str(value.as_expr())})

    # Sum all nonidentity evaluations using the exact root sum, not numerics.
    trace_sum = (c - 1) * coefficients[0] - sum(coefficients[1:])
    green_sum = degree * (Fraction(c*c - 1, 12)
                          - Fraction(char * (c - char), 2)) - Fraction(c*c - 1, 12)
    assert trace_sum == green_sum
    augmentation = sum(coefficients)
    assert (augmentation + trace_sum) % c == 0
    gamma = (-6 * augmentation) % c
    assert gamma in (0, c // 2)

    sign_maps = []
    for e in (-1, 1):
        # Coordinates are (gamma, beta). F is the framed two-handle boundary;
        # G is the stipulated ordinary shear; R gives the cap comparison.
        F = sp.Matrix([[1, 0], [e, 1]])
        G = sp.Matrix([[1, e], [0, 1]])
        R = sp.Matrix([[1, e], [-e, 0]])
        assert F * R == G
        assert R.det() == 1
        assert R.inv() * R == sp.eye(2)
        to_ints = lambda matrix: [[int(x) for x in line] for line in matrix.tolist()]
        sign_maps.append({"e": e, "F": to_ints(F), "G": to_ints(G),
                          "R": to_ints(R), "R_inverse": to_ints(R.inv())})

    record = {"OS": row["OS"], "zero": row["zero"], "a": row["a"],
              "c": c, "e": [-1, 1], "cusp_degree": degree,
              "cusp_character": char, "elliptic_normal_weight": t,
              "regular_quotient_coefficients": coefficients,
              "all_nonidentity_powers": all_powers,
              "trace_sum": int(trace_sum), "augmentation": augmentation,
              "index_mod_c": augmentation % c, "Gamma_c": gamma,
              "P_marked": gamma, "model": f"Z_{{{c},{int(gamma != 0)}}}",
              "clutch_maps": sign_maps}
    results.append(record)
    print(f"OS{row['OS']} zero={row['zero']} c={c} e=+/-1 "
          f"char={char} degree={degree} t={t}")
    print("  quotient coefficients", coefficients,
          "sum(nonidentity)", trace_sum, "augmentation", augmentation,
          "Gamma=P", gamma, record["model"])
    print("  every nonidentity power", all_powers)

assert len(results) == 7
OUTPUT.write_text(json.dumps({"input_sha256": sha256(INPUT.read_bytes()).hexdigest(),
                              "rows": results}, indent=2) + "\n")
print("PASS: exact Green inverse, all cyclotomic divisors, all nonidentity powers,")
print("both cap comparison matrices and inverses, all seven Gamma residues.")
print("data", OUTPUT.relative_to(BASE), sha256(OUTPUT.read_bytes()).hexdigest())
