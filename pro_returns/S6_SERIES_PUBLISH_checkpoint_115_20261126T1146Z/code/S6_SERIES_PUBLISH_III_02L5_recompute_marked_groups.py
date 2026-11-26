#!/usr/bin/env python3
"""02L5: exact post-release recomputation from input-only marked data.

This program imports no historical code and reads no historical result file.
The method uses exact rational lift construction, primitive vanishing vectors,
a unimodular three-vector certificate, and the full presentation reduction
proved in the companion comparison. It does not infer a nonabelian group from
its abelianization. The original profiles do not supply analytic realizations.
"""

from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_02L5_original_inputs.json"
OUTPUT = ROOT / "agents/continuation4_iii_reductions/S6_SERIES_PUBLISH_III_02L5_marked_groups.json"


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def determinant(a):
    n = len(a)
    answer = 0
    for perm in permutations(range(n)):
        sign = (-1) ** sum(perm[i] > perm[j]
                           for i in range(n) for j in range(i + 1, n))
        term = sign
        for i in range(n):
            term *= a[i][perm[i]]
        answer += term
    return answer


def matrix_rank(a):
    for size in range(min(len(a), len(a[0])), 0, -1):
        for rows in combinations(range(len(a)), size):
            for cols in combinations(range(len(a[0])), size):
                if determinant([[a[i][j] for j in cols] for i in rows]):
                    return size
    return 0


def column(a, j):
    return [row[j] for row in a]


def minus_identity(a):
    return [[value - int(i == j) for j, value in enumerate(row)]
            for i, row in enumerate(a)]


def gcd_vector(v):
    answer = 0
    for x in v:
        answer = gcd(answer, abs(x))
    return answer


def rational_solution_rank_one(n, q):
    """Construct and verify one solution of N*x=q, using a nonzero entry."""
    assert matrix_rank(n) == 1
    for i in range(2):
        for j in range(2):
            if n[i][j]:
                x = [Fraction(0), Fraction(0)]
                x[j] = Fraction(q[i], n[i][j])
                if matvec(n, x) == q:
                    return x
    raise AssertionError("q is outside the rational image")


def inverse_unimodular_3(a):
    d = determinant(a)
    assert abs(d) == 1
    answer = []
    for i in range(3):
        row = []
        for j in range(3):
            minor = [[a[r][c] for c in range(3) if c != i]
                     for r in range(3) if r != j]
            row.append(((-1) ** (i + j) * determinant(minor)) // d)
        answer.append(row)
    assert multiply(a, answer) == identity(3)
    assert multiply(answer, a) == identity(3)
    return answer


def lift(a, cocycle, pscale, qscale, weight):
    n = minus_identity(a)
    assert determinant(a) == 1 and matrix_rank(n) == 1
    assert multiply(n, n) == [[0, 0], [0, 0]]
    p = [pscale * x for x in cocycle]
    q = [qscale * x for x in cocycle]
    row = multiply([[p[1], -p[0]]], a)[0]
    x = rational_solution_rank_one(n, q)
    # Independence of the chosen solution follows from row proportionality
    # to a nonzero row of N, so row kills ker(N).
    nr = next(r for r in n if any(r))
    pivot = next(j for j, value in enumerate(nr) if value)
    ratio = Fraction(row[pivot], nr[pivot])
    assert [ratio * y for y in nr] == row
    c = sum(row[j] * x[j] for j in range(2)) + weight
    assert c.denominator == 1
    m = [[a[0][0], a[0][1], 0, q[0]],
         [a[1][0], a[1][1], 0, q[1]],
         [row[0], row[1], 1, int(c)],
         [0, 0, 0, 1]]
    nn = minus_identity(m)
    assert determinant(m) == 1
    assert multiply(nn, nn) == [[0] * 4 for _ in range(4)]
    return m, {"x": [str(y) for y in x], "p": p, "q": q,
               "row": row, "c": int(c), "weight": weight}


def primitive_column_candidates(matrices):
    result = []
    for i, m in enumerate(matrices):
        n = minus_identity(m)
        for j in range(4):
            col = column(n, j)
            divisor = gcd_vector(col)
            if divisor:
                primitive = [x // divisor for x in col]
                assert gcd_vector(primitive) == 1
                assert [divisor * x for x in primitive] == col
                result.append({"fibre": i + 1, "column": j + 1,
                               "divisor": divisor, "vector": primitive})
    return result


def certify_first_three(matrices):
    # The fifth weight-one fibre gives e3 by an integral combination of
    # actual N5 columns. Search finite coefficients, ordered by their norm.
    n5 = minus_identity(matrices[4])
    e3 = [0, 0, 1, 0]
    choices = sorted(product((-1, 0, 1), repeat=4),
                     key=lambda x: (sum(abs(y) for y in x), x))
    coeff = next(list(x) for x in choices if matvec(n5, x) == e3)
    candidates = primitive_column_candidates(matrices[:4])
    for v, w in combinations(candidates, 2):
        columns = [v["vector"], w["vector"], e3]
        b = [[col[i] for col in columns] for i in range(3)]
        if abs(determinant(b)) == 1:
            inv = inverse_unimodular_3(b)
            full = [[col[i] for col in columns] for i in range(4)]
            assert multiply(full, inv) == [[1, 0, 0], [0, 1, 0],
                                          [0, 0, 1], [0, 0, 0]]
            return {"v": v, "w": w, "e3_fibre": 5,
                    "e3_column_coefficients": coeff,
                    "basis": full, "determinant": determinant(b),
                    "inverse_top_three": inv}
    raise AssertionError("no unimodular primitive vanishing certificate")


def main():
    raw = INPUT.read_bytes()
    data = json.loads(raw)
    profiles = {p["os_entry"]: p for p in data["profiles"]}
    results = []
    for case in data["cases"]:
        spec = case["input"]
        profile = profiles[spec["os_entry"]]
        pscale, = spec["P"]
        qscale, = spec["Q"]
        assert spec["coordinates"] == "ambient"
        assert profile["profile"] == spec["profile"] == "default"
        assert len(profile["section_cocycles"]) == 1
        cocycles = profile["section_cocycles"][0]
        weights = spec["linearization_divisor"]
        assert len(weights) == 6 and weights[-1] == 0
        assert weights[:5] == [0, 0, 0, 0, 1]
        assert Fraction(profile["height_matrix"][0][0]) * pscale * qscale == 1
        for comp in profile["component_maps"]:
            for modulus, row in zip(comp["moduli"], comp["rows"]):
                assert len(row) == 1 and (row[0] * pscale) % modulus == 0
        matrices, lifts = [], []
        elliptic_product = identity(2)
        for i, (a, cocycle) in enumerate(zip(profile["elliptic_matrices"], cocycles)):
            assert gcd_vector([x for row in minus_identity(a) for x in row]) == int(profile["kodaira_types"][i][1:])
            elliptic_product = multiply(elliptic_product, a)
            m, detail = lift(a, cocycle, pscale, qscale, weights[i])
            matrices.append(m)
            lifts.append(detail)
        assert elliptic_product == identity(2)
        matrices.append(identity(4))
        total = identity(4)
        for m in matrices:
            total = multiply(total, m)
            assert m[3] == [0, 0, 0, 1]
        assert total == identity(4)
        assert [matrix_rank(minus_identity(m)) for m in matrices] == [1, 1, 1, 1, 2, 0]
        certificate = certify_first_three(matrices)
        log_data = spec["log_data"]
        assert len(log_data) == 6 and log_data[:5] == [None] * 5
        theta = log_data[5]
        assert theta in ([0, 0, 0, 0], [0, 0, 0, 1])
        # The proved presentation elimination leaves exactly this one
        # relation on the surviving fourth fibre generator.
        relation = theta[3]
        group = "Z" if relation == 0 else "trivial"
        assert relation in (0, 1)
        results.append({
            "case": case["name"], "os_entry": spec["os_entry"],
            "profile_scope": profile["model_status"],
            "matrices": matrices, "lift_details": lifts,
            "ordered_product": total,
            "vanishing_lattice_certificate": certificate,
            "sum_primitive_vanishing_lattices": "Z e1 + Z e2 + Z e3",
            "quotient_map": [0, 0, 0, 1],
            "quotient_section": [0, 0, 0, 1],
            "smooth_clutch": theta,
            "full_marked_presentation_group": group,
            "surviving_generator": "a4",
            "remaining_relation": relation,
            "method": "full peripheral-generator elimination plus primitive unimodular basis; no Smith-form inference of a nonabelian group"
        })
    output = {
        "completed_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "input_file": str(INPUT.relative_to(ROOT)),
        "input_sha256": sha256(raw).hexdigest(),
        "historical_source_commit": data["source_commit"],
        "program_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "phase": "post-proof-release recomputation supporting one targeted 02L5 check",
        "scope": "exact full marked filling presentations; analytic database realizations are not supplied by these profiles",
        "results": results
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    for result in results:
        cert = result["vanishing_lattice_certificate"]
        print(result["case"] + ": " + result["full_marked_presentation_group"]
              + "; det=" + str(cert["determinant"])
              + "; v=" + str(cert["v"]["vector"])
              + "; w=" + str(cert["w"]["vector"])
              + "; e3 coefficients=" + str(cert["e3_column_coefficients"]))
    print("Completed " + output["completed_utc"])


if __name__ == "__main__":
    main()
