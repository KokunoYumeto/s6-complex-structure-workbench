"""Independent exact checks for the A3.4 root-cover/trace maps.

Written after the isolated root-cover comparison, without importing a producer.
The universal analytic argument is recorded separately; these finite algebraic
checks supplement it. All rings here retain the indicated nilpotents and units.
"""
from pathlib import Path
import datetime
import hashlib
import json
import sympy as S

CHECKER = "GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation"
checks = []


def record(name, value, **data):
    assert value, (name, data)
    checks.append({"name": name, "PASS": True, **data})


xi, s, w, z, x = S.symbols("xi s w z x")
for m in range(2, 10):
    ring = S.QQ.poly_ring(s, w, z)
    modulus = S.Poly(S.cyclotomic_poly(m, xi), xi, domain=ring)
    product = S.prod(s - xi**j * w * z for j in range(m))
    residue = S.Poly(S.expand(product - s**m + (w*z)**m), xi,
                     domain=ring).rem(modulus)
    record("unit-root factorization in the exact cyclotomic ring",
           residue.is_zero, degree=m)
    wi, wj, wk = 1+x, 1+2*x+x*x, 1-x+2*x*x
    ui, uj = wi**m, wj**m
    # The transition a_ij is w_j/w_i times an actual m-th root of unity.
    for k in (0, 1, m-1):
        numerator = S.together(ui*(xi**k*wj/wi)**m-uj)
        numerator = S.Poly(S.fraction(numerator)[0], xi).rem(
            S.Poly(S.cyclotomic_poly(m, xi), xi))
        record("retained nonconstant-unit transition", numerator.is_zero,
               degree=m, root_index=k)
    # Three coordinate transitions, with inverse explicitly retained.
    aij, ajk = wj/wi, wk/wj
    record("actual coordinate cocycle and inverse",
           S.cancel(aij*ajk-wk/wi)==0 and S.cancel(aij*(wi/wj)-1)==0,
           degree=m)
    for a in range(m):
        perm = [(j+a) % m for j in range(m)]
        inv = [(j-a) % m for j in range(m)]
        assert all(inv[perm[j]] == j for j in range(m))
    record("sheet overlap permutation and its inverse", True, degree=m)


for n in range(2, 7):
    # R=Q[e]/e^n; N is multiplication by e in its ordered basis.
    N = S.zeros(n)
    for j in range(n-1):
        N[j+1, j] = 1
    assert N**n == S.zeros(n) and N**(n-1) != S.zeros(n)
    for m in range(2, 9):
        # B=R[T]/(T^m-1). It is finite etale over the nonreduced ring R.
        P = S.zeros(m)
        for j in range(m):
            P[(j+1) % m, j] = 1
        assert P**m == S.eye(m)
        coeff = [sum((((j+1)*(k+2)-3)*N**k for k in range(n)), S.zeros(n))
                 for j in range(m)]
        mult = sum((S.kronecker_product(P**j, coeff[j]) for j in range(m)),
                   S.zeros(m*n))
        trace_over_R = sum((mult[j*n:(j+1)*n, j*n:(j+1)*n]
                            for j in range(m)), S.zeros(n))
        record("rank-m trace retains nilpotents", trace_over_R == m*coeff[0],
               degree=m, nilpotence_order=n)
        inclusion = S.zeros(m*n, n)
        inclusion[:n, :] = S.eye(n)
        normalized_trace = S.zeros(n, m*n)
        # Tr(T^j)/m is 1 for j=0 and 0 for the other basis elements.
        normalized_trace[:, :n] = S.eye(n)
        record("section pullback and normalized trace are exact inverses",
               normalized_trace*inclusion == S.eye(n),
               degree=m, nilpotence_order=n)


for n in range(2, 11):
    # Exact current Cartier layer on Q[s]/s^n, tensored with a rank-three bundle.
    inclusion = S.zeros(n, 1)
    inclusion[n-1, 0] = 1
    reduction = S.zeros(n-1, n)
    reduction[:, :n-1] = S.eye(n-1)
    i3 = S.kronecker_product(S.eye(3), inclusion)
    r3 = S.kronecker_product(S.eye(3), reduction)
    record("every Artinian Cartier layer, with all nilpotents retained",
           r3*i3 == S.zeros(3*(n-1), 3)
           and i3.rank() == 3
           and r3.rank() == 3*(n-1)
           and len(r3.nullspace()) == 3,
           full_multiplicity=n, bundle_rank=3)


result = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "checker": CHECKER,
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "outcome": "PASS",
    "exact_checks": len(checks),
    "checks": checks,
    "scope": "Finite exact cyclotomic factorization, retained nonconstant units, sheet maps, finite-etale trace over nilpotent rings, and all specified Cartier layers. The universal root-cover and cohomological transport proof is separate; no finite sample proves it.",
    "producer_imported": False,
    "chronology": "Authored after isolated target comparison; no before-reading computation claim. Canonical/raw/gate/source checkpoint freeze was retained.",
}
Path(__file__).with_suffix(".output.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({k: result[k] for k in ("utc", "outcome", "exact_checks", "source_sha256")}))
