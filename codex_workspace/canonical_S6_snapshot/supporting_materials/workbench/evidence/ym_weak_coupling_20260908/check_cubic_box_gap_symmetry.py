"""Exact finite matrix symmetry checks; no continuum certificate."""
from itertools import permutations, product
from pathlib import Path
import json
import sympy as S

pairs = [(0, 1), (0, 2), (1, 2)]
checks = []


def record(name, passed):
    if not passed:
        raise AssertionError(name)
    checks.append({"name": name, "passed": True, "exact": True})


representations = []
for perm in permutations(range(3)):
    for signs in product((-1, 1), repeat=3):
        exterior = S.zeros(3)
        for col, (i, j) in enumerate(pairs):
            a, b = perm[i], perm[j]
            row = pairs.index(tuple(sorted((a, b))))
            exterior[row, col] = signs[i]*signs[j]*(1 if a < b else -1)
        rep = S.zeros(6)
        for col in range(3):
            row = next(i for i in range(3) if exterior[i, col])
            rep[row, col] = 1
        for col, (i, j) in enumerate(pairs, 3):
            ri = next(k for k in range(3) if exterior[k, i])
            rj = next(k for k in range(3) if exterior[k, j])
            row = 3 + pairs.index(tuple(sorted((ri, rj))))
            rep[row, col] = exterior[ri, i]*exterior[rj, j]
        record(f"orthogonal_{len(representations)}", rep.T*rep == S.eye(6))
        representations.append(rep)

d, o, c = S.symbols("d o c", real=True)
K = S.diag(d, d, d, c, c, c)
for i, j in permutations(range(3), 2):
    K[i, j] = o
for i, rep in enumerate(representations):
    record(f"commutes_{i}", K*rep == rep*K)

# Converse: solve every commutator on all 21 symmetric matrix variables.
variables = S.symbols("k0:21")
general, idx = S.zeros(6), 0
for i in range(6):
    for j in range(i, 6):
        general[i, j] = general[j, i] = variables[idx]
        idx += 1
equations = set()
for rep in representations:
    for entry in general*rep-rep*general:
        if entry:
            equations.add(entry)
A, b = S.linear_eq_to_matrix(sorted(equations, key=str), variables)
record("symmetric_commutant_dimension_exactly_three", 21-A.rank() == 3)
lam = S.Symbol("lambda")
record("full_characteristic_polynomial",
       S.expand(K.charpoly(lam).as_expr()
                -(lam-d-2*o)*(lam-d+o)**2*(lam-c)**3) == 0)
record("invariant_scalar_vector",
       K*S.Matrix([1, 1, 1, 0, 0, 0])
       == (d+2*o)*S.Matrix([1, 1, 1, 0, 0, 0]))

result = {
    "passed": True, "count": len(checks), "checks": checks,
    "scope": "All 48 signed coordinate permutations, their exact exterior-square "
             "and six-state actions, and full real-symmetric commutant. "
             "The nonlinear graph-operator correspondence is proved in the "
             "companion text, not certified by these matrix checks."
}
dest = Path(__file__).with_name("CUBIC_BOX_GAP_SYMMETRY_CHECKS.json")
dest.write_text(json.dumps(result, indent=2)+"\n", encoding="utf8")
print(json.dumps({"passed": True, "count": len(checks), "output": str(dest)}))
