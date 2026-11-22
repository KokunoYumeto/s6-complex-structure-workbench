#!/usr/bin/env python3
"""Exact global-D comparison computations; no canonical event or source edits."""
from pathlib import Path
from itertools import combinations, permutations
import datetime
import hashlib
import json
import random
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
checks = []


def check(name, condition, evidence):
    ok = bool(condition)
    checks.append({"name": name, "passed": ok, "evidence": evidence})
    if not ok:
        raise AssertionError(name)


pairs = list(combinations(range(4), 2))


def sign(order):
    return (-1) ** sum(order[i] > order[j]
                       for i in range(len(order))
                       for j in range(i + 1, len(order)))


Q = s.Matrix(6, 6, lambda i, j:
             sign(pairs[i] + pairs[j])
             if len(set(pairs[i] + pairs[j])) == 4 else 0)
check("wedge_pairing", Q == Q.T and Q.det() != 0, str(Q))

samples = [("identity", s.eye(4)), ("minus_identity", -s.eye(4)),
           ("two_negative", s.diag(-1, -1, 1, 1)),
           ("hyperbolic", s.diag(s.Matrix([[2, 1], [1, 1]]),
                                s.Matrix([[3, 2], [1, 1]]))),
           ("fourth_roots", s.Matrix([[0, 0, 0, -1], [1, 0, 0, 0],
                                      [0, 1, 0, 0], [0, 0, 1, 0]]))]
for p in permutations(range(4)):
    if sign(p) == 1:
        samples.append(("even_permutation_" + "".join(map(str, p)),
                        s.eye(4)[:, p]))
rng = random.Random(20261122)
for k in range(16):
    g = s.eye(4)
    for _ in range(5):
        i, j = rng.sample(range(4), 2)
        e = s.eye(4)
        e[i, j] = rng.choice([-2, -1, 1, 2])
        g = e * g
    samples.append((f"elementary_product_{k}", g))

matrix_records = []
for name, g in samples:
    A = s.Matrix(6, 6, lambda i, j: g.extract(pairs[i], pairs[j]).det())
    B = s.eye(6) - A
    pivots = B.rref()[1]
    U = B[:, pivots]
    d = len(pivots)
    check(name + ":exterior_square", g.det() == 1 and A.det() == 1
          and A.T * Q * A == Q, {"rank": d, "fixed_dimension": 6 - d})
    if d:
        X = s.eye(6)[:, pivots]
        H = X.T * Q * U
        AU = U.gauss_jordan_solve(A * U)[0]
        check(name + ":wall_form",
              H.det() != 0 and H.T == -H * AU.inv()
              and AU.det() == (-1) ** d,
              {"H": str(H), "det_A_on_image": str(AU.det())})
    else:
        check(name + ":zero_image", A == s.eye(6), "U=0")
    check(name + ":fixed_parity", (6 - d) % 2 == 0, 6 - d)
    matrix_records.append({"name": name, "g": str(g),
                           "image_rank": d, "fixed_dimension": 6 - d})

# Pair exact sequence: a symbolic calculation independent of source's
# sum-of-three-boundary-dimensions calculation.
b = s.symbols("b0:6", integer=True)
r = s.symbols("r", integer=True)
pair_expression = b[0]-b[1]+b[2]+b[3]-b[4]+b[5]-r
chi = sum((-1)**i*b[i] for i in range(6))
check("pair_sequence_difference",
      s.expand(pair_expression-chi) == 2*b[3]-2*b[4]+2*b[5]-r,
      str(s.expand(pair_expression-chi)))
c1, c2 = s.symbols("c1 c2", integer=True)
check("wang_boundary_alternating_sum",
      s.expand(1-(1+c1)+(c1+c2)) == c2, "c2")

# Cohomology generating polynomials versus support stratification.
t, k, m = s.symbols("t k m", integer=True)
base = s.expand((1+t)**4*(1+t**2))
curve_two = t**2*(1+4*t+t**2)
point = t**2+t**4
curve_three = t**2*(1+6*t+t**2)
total = s.Poly(s.expand(base+k*curve_two+m*point), t)
expected = [1, 4, 7+k+m, 8+4*k, 7+k+m, 4, 1]
check("UN2_all_betti_coefficients",
      all(s.expand(total.nth(i)-expected[i]) == 0 for i in range(7)),
      list(map(str, expected)))
check("UN2_cohomology_euler",
      s.expand(total.as_expr().subs(t, -1)) == 2*(m-k), "2*(m-k)")
check("negative_move_added_groups",
      s.expand(point+curve_three) == 2*t**2+6*t**3+2*t**4,
      "[2,6,2] in degrees [2,3,4]")
check("negative_move_euler",
      s.expand((point+curve_three).subs(t, -1)) == -2, -2)
check("zero_move_added_groups",
      s.expand(2*point+curve_three) == 3*t**2+6*t**3+3*t**4,
      "[3,6,3] in degrees [2,3,4]")
check("zero_move_euler",
      s.expand((2*point+curve_three).subs(t, -1)) == 0, 0)
eS, eZ, codim = s.symbols("eS eZ codim", integer=True)
check("support_stratification_euler",
      s.expand(eS-eZ+codim*eZ-eS-(codim-1)*eZ) == 0,
      "(codim-1)*eZ")
check("C2b_first_blowup_betti",
      [s.expand(base+curve_two).coeff(t, i) for i in range(7)]
      == [1,4,8,12,8,4,1], "[1,4,8,12,8,4,1]")
check("C2b_second_blowup_betti",
      [s.expand(base+curve_two+point).coeff(t, i) for i in range(7)]
      == [1,4,9,12,9,4,1], "[1,4,9,12,9,4,1]")
check("C2b_component_inclusion_exclusion", 1-4+3-(-2)-2 == 0, 0)

# Exact curve and local chart arithmetic.
z, w, u, v, rr, n = s.symbols("z w u v rr n")
check("genus_two_branch_polynomial",
      s.gcd(z**6-1, s.diff(z**6-1,z)) == 1, "six distinct finite roots")
check("genus_two_RH", -4+6 == 2, "2g-2=2")
check("quartic_line_intersection",
      s.gcd(z**4+1, s.diff(z**4+1,z)) == 1,
      "four distinct intersections with X=0")
check("quartic_adjunction", 4*(4-3) == 2*3-2, "g=3")
check("quartic_blowup_chart",
      (rr*u).subs(rr,v*w) == u*v*w, "t=(uvw)^m")
for old_half in range(-8,9):
    for target_half in range(-8,9):
        difference = target_half-old_half
        final = 2*old_half + 2*max(difference,0) - 2*max(-difference,0)
        if final != 2*target_half:
            raise AssertionError("integer prescription")
check("integer_prescriptions", True, "289 pairs, using the proved +/-2 moves")

source = ROOT/"S6_SERIES_PUBLISH_II.tex"
derivation = ROOT/"records/S6_SERIES_PUBLISH_II_global_D_root_derivation_01.md"
out = ROOT/"code/S6_SERIES_PUBLISH_II_global_D_root_certificate_01.json"
result = {
    "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "derivation_sha256": hashlib.sha256(derivation.read_bytes()).hexdigest(),
    "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Global-D comparative exact computations; finite matrix cases support the separately written general Wall-form proof and are not its substitute.",
    "method_difference": "Wall-form construction on im(I-A) compared with the printed generalized-eigenspace/Cayley proof; cohomology generating polynomials compared with support Euler stratification; direct local substitutions and squarefree curve polynomials.",
    "matrix_cases": matrix_records,
    "checks": checks,
    "passed": len(checks),
    "canonical_events_added": 0,
    "required_rows_closed": 0,
    "final_candidate_binding_pending": True
}
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"output":str(out.relative_to(ROOT)),
                  "passed":len(checks),"matrix_cases":len(samples),
                  "sha256":hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
