"""Exact finite polynomial checks; not a continuum or spectral certificate."""
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json
import sympy as S

CHECKS = []


def check(name, expression):
    residual = S.expand(expression)
    if residual != 0:
        residual = S.factor(residual)
    if residual != 0:
        raise AssertionError((name, str(residual)))
    CHECKS.append({"name": name, "exact": True, "passed": True})


def expectation(expr, variables, covariance):
    @lru_cache(None)
    def moment(indices):
        if not indices:
            return S.Integer(1)
        if len(indices) % 2:
            return S.Integer(0)
        first, rest = indices[0], indices[1:]
        return sum(covariance[first, rest[k]]
                   * moment(rest[:k] + rest[k + 1:])
                   for k in range(len(rest)))
    answer = 0
    for powers, coefficient in S.Poly(S.expand(expr), *variables).terms():
        indices = tuple(i for i, power in enumerate(powers)
                        for unused in range(power))
        answer += coefficient * moment(indices)
    return S.expand(answer)


def vectors(prefix, count):
    return [S.Matrix(S.symbols(f"{prefix}{i}_0:3")) for i in range(count)]


def quartic_word(v):
    q = sum(w.dot(w)**2 / 192 for w in v)
    for i, j in combinations(range(4), 2):
        q += (v[i].dot(v[i]) + v[j].dot(v[j])) * v[i].dot(v[j]) / 48
        q += v[i].dot(v[i]) * v[j].dot(v[j]) / 32
    for i, j, k in combinations(range(4), 3):
        q += (v[i].dot(v[i]) * v[j].dot(v[k])
              + v[j].dot(v[j]) * v[i].dot(v[k])
              + v[k].dot(v[k]) * v[i].dot(v[j])) / 16
    q += (v[0].dot(v[1]) * v[2].dot(v[3])
          - v[0].dot(v[2]) * v[1].dot(v[3])
          + v[0].dot(v[3]) * v[1].dot(v[2])) / 8
    return -q


# The complete ordered SU(2) face word, with four arbitrary vector letters.
v = vectors("v", 4)
pauli = [S.Matrix([[0, 1], [1, 0]]),
         S.Matrix([[0, -S.I], [S.I, 0]]),
         S.diag(1, -1)]
T = [-S.I * sigma / 2 for sigma in pauli]
V = [sum((w[c] * T[c] for c in range(3)), S.zeros(2)) for w in v]
powers = [[S.eye(2)] for unused in range(4)]
for i in range(4):
    for n in range(1, 5):
        powers[i].append((powers[i][-1] * V[i]).applyfunc(S.expand))
for degree in (2, 3, 4):
    trace = 0
    for ns in product(range(degree + 1), repeat=4):
        if sum(ns) != degree:
            continue
        mat = S.eye(2)
        for i, n in enumerate(ns):
            mat = mat * powers[i][n] / S.factorial(n)
        trace += S.trace(mat)
    if degree == 2:
        total = sum(v, S.zeros(3, 1))
        formula = total.dot(total) / 4
    elif degree == 3:
        formula = sum(v[i].dot(v[j].cross(v[k])) / 4
                      for i, j, k in combinations(range(4), 3))
    else:
        formula = quartic_word(v)
    check(f"ordered_face_degree_{degree}", -trace - formula)

# Complete Wick contraction of the four-letter quartic polynomial.
m = S.Matrix(4, 4, lambda i, j: S.Symbol(f"m{min(i,j)}{max(i,j)}"))
cov = S.Matrix(12, 12, lambda i, j: m[i // 3, j // 3]
               if i % 3 == j % 3 else 0)
variables = [entry for w in v for entry in w]
actual = expectation(quartic_word(v), variables, cov)
claimed = S.Rational(15, 192) * sum(m[i, i]**2 for i in range(4))
for i, j in combinations(range(4), 2):
    claimed += S.Rational(15, 48) * (m[i, i] + m[j, j]) * m[i, j]
    claimed += (9 * m[i, i] * m[j, j] + 6 * m[i, j]**2) / 32
for i, j, k in combinations(range(4), 3):
    claimed += (9 * (m[i, i] * m[j, k] + m[j, j] * m[i, k]
                    + m[k, k] * m[i, j])
                + 6 * (m[i, j] * m[i, k] + m[i, j] * m[j, k]
                       + m[i, k] * m[j, k])) / 16
claimed += (9 * m[0, 1] * m[2, 3] - 3 * m[0, 2] * m[1, 3]
            + 9 * m[0, 3] * m[1, 2]) / 8
check("ordered_face_quartic_full_symbolic_covariance", actual + claimed)

# Generic A1 contraction: no assumed incidence, metric or coordinate values.
x, p = vectors("x", 3), vectors("p", 3)
s, t = S.symbols("s0:3"), S.symbols("t0:3")
A1 = S.zeros(9)
for c, d, b, q in product(range(3), repeat=4):
    A1[3*c+b, 3*d+q] = sum(
        S.LeviCivita(e, b, q) * (s[c]*t[d]*x[c][e]
                                  - t[c]*s[d]*x[d][e]) / 2
        for e in range(3))
pv = S.Matrix([entry for w in p for entry in w])
rhs = sum(s[c] * t[d] * x[c].dot(p[c].cross(p[d]))
          for c, d in product(range(3), repeat=2))
check("A1_exact_determinant_contraction", (pv.T*A1*pv)[0] - rhs)
xv = [entry for w in x for entry in w]
for j in range(9):
    check(f"A1_divergence_column_{j}",
          sum(S.diff(A1[i, j], xv[i]) for i in range(9)))

# Direct Wick evaluation of each A2 chord-pair tensor on an exact positive
# rational covariance. This tests contraction arithmetic, not graph spectra.
B = S.Matrix([[3, 1, 0], [1, 4, 1], [0, 1, 5]])
assert all(B[:k, :k].det() > 0 for k in range(1, 4))
M = B.inv() / 2
p = [sum((B[c, d] * x[d] for d in range(3)), S.zeros(3, 1))
     for c in range(3)]
cov = S.kronecker_product(M, S.eye(3))
for c, d in product(range(3), repeat=2):
    raw_s = (p[c].dot(p[d]) * x[c].dot(x[d])
             - p[c].dot(x[d]) * p[d].dot(x[c])) / 4
    rhs_s = S.Rational(3, 4) * B[c, d] * M[c, d] \
        - S.Rational(3, 8) * int(c == d)
    check(f"A2_s_pair_{c}_{d}", expectation(raw_s, xv, cov) - rhs_s)
    raw_t = (p[c].dot(x[c]) * p[d].dot(x[c])
             + p[c].dot(x[d]) * p[d].dot(x[d])
             - (x[c].dot(x[c]) + x[d].dot(x[d])) * p[c].dot(p[d])) / 12
    rhs_t = (int(c == d) - B[c, d] * (M[c, c] + M[d, d])) / 4
    check(f"A2_t_pair_{c}_{d}", expectation(raw_t, xv, cov) - rhs_t)

# All coefficients and factors in the three-distinct-mode spectral inverse.
z = vectors("z", 4)
sig = S.symbols("sigma0:4", positive=True)
a = S.Symbol("a", positive=True)
det = z[0].dot(z[1].cross(z[2]))
conjugated = sum(-2*S.diff(det, z[i][c], 2)/a
                 + sig[i]*z[i][c]*S.diff(det, z[i][c])/a
                 for i, c in product(range(4), range(3)))
check("cubic_singlet_exact_excitation",
      conjugated - (sig[0]+sig[1]+sig[2])*det/a)
zv = [entry for w in z for entry in w]
cov = S.diag(*[2/sig[i] for i in range(4) for c in range(3)])
norm = expectation(det**2, zv, cov)
check("cubic_singlet_raw_norm_48", norm - 48/(sig[0]*sig[1]*sig[2]))
check("different_spatial_triples_orthogonal",
      expectation(det*z[0].dot(z[1].cross(z[3])), zv, cov))
check("cubic_singlet_vacuum_orthogonal", expectation(det, zv, cov))
theta = S.Symbol("Theta", real=True)
check("reduced_inverse_energy_coefficient",
      theta**2 * norm * a/(sig[0]+sig[1]+sig[2])
      - 48*a*theta**2/(sig[0]*sig[1]*sig[2]*(sig[0]+sig[1]+sig[2])))

# The entire six-dimensional lowest physical cluster.
sigma = S.Symbol("sigma_star", positive=True)
cluster = []
for i in range(3):
    cluster.append(sigma/(2*S.sqrt(6))*(z[i].dot(z[i])-6/sigma))
for i, j in combinations(range(3), 2):
    cluster.append(sigma/(2*S.sqrt(3))*z[i].dot(z[j]))
cov_low = S.diag(*([2/sigma]*9 + [2/sig[3]]*3))
for i, Pi in enumerate(cluster):
    check(f"physical_cluster_centered_{i}", expectation(Pi, zv, cov_low))
    opPi = sum(-2*S.diff(Pi, z[j][c], 2)/a
               + sigma*z[j][c]*S.diff(Pi, z[j][c])/a
               for j, c in product(range(3), range(3)))
    check(f"physical_cluster_excitation_{i}", opPi-2*sigma*Pi/a)
    for j, Pj in enumerate(cluster):
        check(f"physical_cluster_gram_{i}_{j}",
              expectation(Pi*Pj, zv, cov_low)-int(i == j))

result = {
    "scope": "Exact finite polynomial and Gaussian contraction identities only. "
             "No continuum limit or interacting mass-gap certificate.",
    "passed": True,
    "count": len(CHECKS),
    "checks": CHECKS,
    "rational_covariance_fixture_B": [list(B.row(i)) for i in range(3)]
}
path = Path(__file__).with_name("CUBIC_SINGLET_VACUUM_ENERGY_CHECKS.json")
path.write_text(json.dumps(result, indent=2, default=str)+"\n", encoding="utf-8")
print(json.dumps({"passed": True, "count": len(CHECKS), "output": str(path)}))
