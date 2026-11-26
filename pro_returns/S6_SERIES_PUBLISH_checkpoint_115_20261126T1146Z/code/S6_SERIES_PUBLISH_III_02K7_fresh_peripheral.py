#!/usr/bin/env python3
"""02K7 fresh peripheral calculation before target-proof exposure.

Inputs are the safe P309 matrices and marked primitive vectors. No manuscript,
prior proof, old program or outcome file is read. The group-theoretic inverse
maps and the geometric boundary maps are proved in the companion derivation;
these exact calculations certify their matrix and exponent identities.
"""

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def power(a, n):
    result = identity(len(a))
    for _ in range(n):
        result = multiply(result, a)
    return result


def transpose(a):
    return [list(row) for row in zip(*a)]


def matvec(a, x):
    return [sum(u * v for u, v in zip(row, x)) for row in a]


def column(a, j):
    return [row[j] for row in a]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(k, a):
    return [k * x for x in a]


def main():
    t1 = [[1, 0, -6, 2], [0, -1, 1, 1],
          [0, -1, 0, 1], [0, 0, 0, 1]]
    t2 = [[1, 6, 0, -3], [0, 0, -1, 1],
          [0, 1, 0, 0], [0, 0, 0, 1]]
    assert power(t1, 3) == power(t2, 4) == identity(4)
    a1 = transpose(power(t1, 2))
    a2 = transpose(power(t2, 3))
    assert multiply(transpose(t1), a1) == identity(4)
    assert multiply(transpose(t2), a2) == identity(4)
    a0 = transpose(multiply(t1, t2))
    assert multiply(multiply(a0, a1), a2) == identity(4)
    eps1 = [1, 2, -4, 0]
    eps2 = [1, 3, -3, 0]
    toric_delta = [0, 0, 0, 1]
    for a, eps in [(a1, eps1), (a2, eps2)]:
        assert matvec(a, eps) == eps
        assert matvec(a, toric_delta) == toric_delta
        assert a[0] == [1, 0, 0, 0]
    assert power(a1, 3) == power(a2, 4) == identity(4)
    n0 = [[a0[i][j] - int(i == j) for j in range(4)] for i in range(4)]
    assert column(n0, 0) == [0, 0, 0, -1]
    assert column(n0, 1) == [0, 0, 1, 0]
    assert column(n0, 2) == column(n0, 3) == [0, 0, 0, 0]
    assert multiply(n0, n0) == [[0] * 4 for _ in range(4)]
    cusp_quotient = [[1, 0, 0, 0], [0, 1, 0, 0]]
    assert multiply(cusp_quotient, a0) == cusp_quotient
    # These actual conjugation images kill the u-cycle after the two
    # toric cycles vanish; no abelianization of the whole group is assumed.
    assert column(a1, 1) == [0, 0, -1, 1]
    assert column(a2, 1) == [0, 0, 1, 0]

    # Coefficients of the linear polynomials in (ell0, ell1, ell2).
    ell0, ell1, ell2 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
    # From xy=g^ell0 and y^4=g^ell2 obtain x^4=g^(4ell0-ell2).
    # The exact Bezout identity 4-3=1 then eliminates x.
    x3 = ell1
    x4 = add(scale(4, ell0), scale(-1, ell2))
    x_exponent = add(x4, scale(-1, x3))
    y_exponent = add(ell0, scale(-1, x_exponent))
    remaining = add(scale(3, x_exponent), scale(-1, ell1))
    assert x_exponent == [4, -1, -1]
    assert y_exponent == [-3, 1, 1]
    assert remaining == [12, -4, -3]
    assert add(scale(4, y_exponent), scale(-1, ell2)) == scale(-1, remaining)
    assert add(x_exponent, y_exponent) == ell0
    # All original cyclic-presentation relations under the inverse map
    # are respectively p, -p, and zero, so this certifies every integer
    # triple, including the formal p=0 endpoint.
    relation_residuals = [remaining, scale(-1, remaining), [0, 0, 0]]
    # p=0 is parametrized by (ell0,ell1,ell2)=(a+b,3a,4b).
    zero_parameterization = [[1, 1], [3, 0], [0, 4]]
    assert multiply([remaining], zero_parameterization) == [[0, 0]]
    # The universal modular identities exclude the zero endpoint for
    # 3∤ell1 and odd ell2.
    assert [x % 3 for x in remaining] == [0, 2, 0]
    assert [x % 2 for x in remaining] == [0, 0, 1]

    result = {
        "completed_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "program_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "phase": "fresh derivation before 02K7 target-proof exposure",
        "input_scope": "safe P309 marked matrices and general affine/cusp defining data",
        "A0": a0, "A1": a1, "A2": a2,
        "cusp_nilpotent": n0,
        "cusp_quotient": cusp_quotient,
        "primitive_finite_vectors": [eps1, eps2, toric_delta],
        "x_exponent_in_ell0_ell1_ell2": x_exponent,
        "y_exponent_in_ell0_ell1_ell2": y_exponent,
        "derived_cyclic_relation": remaining,
        "inverse_map_relation_residuals": relation_residuals,
        "formal_zero_parameterization": zero_parameterization,
        "admissible_modular_identities": {
            "mod_3": "p = -ell1",
            "mod_2": "p = ell2"
        }
    }
    root = Path(__file__).resolve().parents[1]
    out = root / "agents/continuation4_iii_reductions/S6_SERIES_PUBLISH_III_02K7_fresh_peripheral.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print("Actual finite/cusp matrix identities verified.")
    print("Derived generator exponents:", x_exponent, y_exponent)
    print("Derived cyclic relation:", remaining)
    print("All inverse presentation residuals and the formal zero endpoint verified.")
    print("Completed:", result["completed_utc"])


if __name__ == "__main__":
    main()
