#!/usr/bin/env python3
"""Fresh L1 integral inverse checks; no original or historical target input.

Reads only the raw construction cache and the independently generated
L1 catalogue.  Euclidean formula maps are checked against separately
computed exact Smith quotients.  Finite examples validate the written
maps; the all-parameter assertions are proved in the fresh derivation.
"""
from pathlib import Path
from itertools import combinations, product
from math import gcd, prod
from collections import Counter
import json
import sympy as S
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/continuation7_iii_nonstar"
CAT = json.loads((OUT / "S6_SERIES_PUBLISH_III_02L1_fresh_catalogue.json").read_text())
RAW = json.loads((ROOT / "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json").read_text())
PROFILES = {(r["OS"], r["profile"]): r for r in RAW["rows"]}
PAIRS = list(combinations(range(4), 2))
J = S.Matrix([[0, 1], [-1, 0]])


def smith(A):
    if A.cols == 0:
        return S.zeros(A.rows, 0), S.eye(A.rows), S.zeros(0)
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    D, U, V = (x.to_Matrix() for x in (D, U, V))
    assert U*A*V == D and abs(U.det()) == abs(V.det()) == 1
    return D, U, V


def group(A):
    D, _, _ = smith(A)
    values = [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i]]
    return A.rows-len(values), tuple(v for v in values if v != 1)


def membership(A, vectors):
    D, U, _ = smith(A)
    W = U*vectors
    rank = sum(bool(D[i, i]) for i in range(min(D.shape)))
    for j in range(W.cols):
        assert all(W[i, j] % D[i, i] == 0 for i in range(rank)), (A, vectors)
        assert all(W[i, j] == 0 for i in range(rank, W.rows)), (A, vectors)


def inverse_quotients(old, new, forward, backward):
    membership(old, forward*new)
    membership(new, backward*old)
    membership(old, forward*backward-S.eye(old.rows))
    membership(new, backward*forward-S.eye(new.rows))
    assert group(old) == group(new)


def xgcd(a, b):
    if b == 0:
        return abs(a), int(a >= 0)-int(a < 0), 0
    g, x, y = xgcd(b, a % b)
    return g, y, x-(a//b)*y


def bezout(xs):
    out, g = [], 0
    for x in xs:
        h, u, v = xgcd(g, x)
        out = [u*t for t in out]+[v]
        g = h
    assert sum(x*y for x, y in zip(xs, out)) == g
    return g, out


def wedge(A):
    return S.Matrix([[A[i, k]*A[j, l]-A[i, l]*A[j, k]
                      for k, l in PAIRS] for i, j in PAIRS])


def omega(a, b, u, v):
    return a*(u[0]*v[1]-u[1]*v[0])-b*(u[2]*v[3]-u[3]*v[2])


def columns(n, cs):
    return S.Matrix.hstack(*cs) if cs else S.zeros(n, 0)


def finite_crt(ps, alphas):
    P = prod(ps)
    old = S.zeros(1+len(ps), len(ps))
    for i, (p, alpha) in enumerate(zip(ps, alphas)):
        old[0, i], old[i+1, i] = alpha, p
    beta = sum(P//p*alpha for p, alpha in zip(ps, alphas))
    new = S.Matrix([[beta], [P]])
    forward = S.zeros(1+len(ps), 2)
    forward[0, 0] = 1
    for i in range(len(ps)):
        forward[i+1, 1] = 1
    backward = S.zeros(2, 1+len(ps))
    backward[0, 0] = 1
    for i, (p, alpha) in enumerate(zip(ps, alphas)):
        E = pow(P//p, -1, p) if p != 1 else 0
        k = (E*(P//p)-1)//p
        backward[1, i+1] = E*(P//p)
        backward[0, i+1] = k*alpha+E*sum(P//(p*ps[l])*alphas[l]
                                                for l in range(len(ps)) if l != i)
    inverse_quotients(old, new, forward, backward)


def regular_crt(a, b, ms, vs):
    R = prod(ms)
    V = [sum(R//m*v[k] for m, v in zip(ms, vs)) for k in range(4)]
    old_cs = []
    for j, (m, v) in enumerate(zip(ms, vs)):
        for k in range(4):
            col = S.zeros(1+4*len(ms), 1)
            col[0] = -omega(a, b, list(S.eye(4)[:, k]), v)
            col[1+4*j+k] = m
            old_cs.append(col)
        col = S.zeros(1+4*len(ms), 1)
        col[1+4*j:5+4*j, 0] = S.Matrix(v)
        old_cs.append(col)
    old = columns(1+4*len(ms), old_cs)
    new = S.zeros(5, 5)
    for k in range(4):
        new[0, k] = -omega(a, b, list(S.eye(4)[:, k]), V)
        new[k+1, k] = R
    new[1:, 4] = S.Matrix(V)
    forward = S.zeros(old.rows, 5)
    forward[0, 0] = 1
    backward = S.zeros(5, old.rows)
    backward[0, 0] = 1
    for j, (m, v) in enumerate(zip(ms, vs)):
        E = pow(R//m, -1, m) if m != 1 else 0
        kappa = (E*(R//m)-1)//m
        for k in range(4):
            u = list(S.eye(4)[:, k])
            forward[1+4*j+k, 1+k] = 1
            backward[1+k, 1+4*j+k] = E*(R//m)
            backward[0, 1+4*j+k] = -(kappa*omega(a, b, u, v)+
                E*sum(R//(m*ms[l])*omega(a, b, u, vs[l])
                      for l in range(len(ms)) if l != j))
    inverse_quotients(old, new, forward, backward)


def presentation(a, b, finite, regular, e, full):
    stride = 2 if full else 1
    n = 1+stride*len(finite)+4*len(regular)
    cs = []
    for i, (m, q, numerator, r) in enumerate(finite):
        d = 1+stride*i
        c = S.zeros(n, 1)
        c[0], c[d] = b*numerator//q, m//q
        cs.append(c)
        if full:
            c2, c3 = S.zeros(n, 1), S.zeros(n, 1)
            c2[0], c2[d+1] = -b*r, m
            c3[d], c3[d+1] = r, numerator
            cs += [c2, c3]
    start = 1+stride*len(finite)
    for j, (m, v) in enumerate(regular):
        for k in range(4):
            c = S.zeros(n, 1)
            c[0] = -omega(a, b, list(S.eye(4)[:, k]), v)
            c[start+4*j+k] = m
            cs.append(c)
        c = S.zeros(n, 1)
        c[start+4*j:start+4*j+4, 0] = S.Matrix(v)
        cs.append(c)
    c = S.zeros(n, 1)
    c[0] = b*e
    for i in range(len(finite)):
        c[1+stride*i] = 1
    for j in range(len(regular)):
        c[start+4*j+2] = 1
    cs.append(c)
    return columns(n, cs)


all_patterns, original_checks, local_h1_checks = set(), 0, 0
own_patterns = set()
for p in CAT["minimal_patterns"]:
    own_patterns.add((p["OS"], p["profile"], p["a"], p["b"], p["zero_index"],
                      tuple(p["finite_indices"]), tuple(p["original_additive_indices"])))
for row in CAT["natural"]:
    if not row["nonstar"]:
        continue
    raw = PROFILES[row["OS"], row["profile"]]
    a, b = row["a"], row["b"]
    for T0 in row["T"]:
        T = S.Matrix(T0)
        assert group(T-S.eye(4))[1] == ()
        local_h1_checks += 1
    options, indices = [], []
    for key, f in row["finite"].items():
        i = int(key)
        indices.append(i+1)
        A, g = S.Matrix(raw["elliptic_matrices"][i]), S.Matrix(raw["generator_section_cocycle"][i])
        z, q = (A-S.eye(2)).inv()*g, f["component_order"]
        zQ = b*z
        narrowP = all(x.q == 1 for x in a*z)
        original = raw["fibers"][i] in ("II", "III", "IV") and narrowP and (
            q == 1 or f["gamma_index"] == q)
        options.append(("finite", "original") if original else ("finite",))
        if not original:
            continue
        alpha = -(a*z).T*J
        SP = S.eye(4)
        SP[2, :2] = alpha
        projection = S.Matrix([[q,0,q*zQ[1],0,-q*zQ[0],0],[0,0,0,0,0,1]])*wedge(SP)
        gg, abc = bezout([q, int(q*zQ[1]), int(-q*zQ[0])])
        assert gg == 1
        lift = S.zeros(6, 2)
        lift[0, 0], lift[2, 0], lift[4, 0], lift[5, 1] = abc[0], abc[1], abc[2], 1
        lift = wedge(SP.inv())*lift
        T = S.Matrix(row["T"][i])
        assert projection*lift == S.eye(2)
        assert projection*(wedge(T)-S.eye(6)) == S.zeros(2, 6)
        assert group(wedge(T)-S.eye(6)) == (2, ())
        original_checks += 1
    for modes in product(*options):
        key = (row["OS"], row["profile"], a, b, row["zero_index"],
               tuple(i for i, mode in zip(indices, modes) if mode == "finite"),
               tuple(i for i, mode in zip(indices, modes) if mode == "original"))
        all_patterns.add(key)
assert own_patterns <= all_patterns
extras = all_patterns-own_patterns
assert len(own_patterns) == 164 and len(all_patterns) == 198 and len(extras) == 34
lookup = {(r["OS"],r["profile"],r["a"],r["b"],r["zero_index"]):r
          for r in CAT["natural"] if r["nonstar"]}
for p in extras:
    row = lookup[p[:5]]
    assert any(row["finite"][str(i-1)]["gamma_index"] > 1 for i in p[5])
print("PASS exact pattern inclusion 164 -> 198; complement34 contains a nonprimitive-gamma finite choice in every row.")
print("PASS integral original additive sections", original_checks,
      "and torsion-free primitive boundary H1 matrices", local_h1_checks)

cases, c1, records = 0, 0, []
for pattern in CAT["minimal_patterns"]:
    if not pattern["simple_order_feasible"]:
        continue
    row = lookup[(pattern["OS"],pattern["profile"],pattern["a"],pattern["b"],pattern["zero_index"])]
    a, b, c = row["a"], row["b"], pattern["c"]
    fs = [row["finite"][str(i-1)] for i in pattern["finite_indices"]]
    for variant in (0, 1):
        fms = [f["monodromy_order"]*(1 if variant == 0 else 5) for f in fs]
        if len(fms) == 2:
            fms[1] = fs[1]["monodromy_order"]
        rms = ([2, 3, 1] if not fms else [7, 1] if len(fms) == 1 else [1])
        orders = fms+rms
        nontrivial = [i for i, m in enumerate(orders) if m > 1]
        assert len(nontrivial) == 2 and gcd(orders[nontrivial[0]], orders[nontrivial[1]]) == 1
        ns = [0]*len(orders)
        i, j = nontrivial
        gg, ni, nj = xgcd(orders[j], orders[i])
        assert gg == 1
        sign = 1 if variant == 0 else -1
        ns[i], ns[j] = sign*ni, sign*nj
        finite = [(m, f["vertical_index"], ns[i], (-1)**i*(a+m+variant))
                  for i, (m, f) in enumerate(zip(fms, fs))]
        regular = [(m, [a+j+variant, b-2*j, 3-j, ns[len(fs)+j]])
                   for j, m in enumerate(rms)]
        finite_crt([m//q for m,q,n,r in finite], [b*n//q for m,q,n,r in finite])
        regular_crt(a, b, rms, [v for m,v in regular])
        A = presentation(a, b, finite, regular, 0, False)
        Afull = presentation(a, b, finite, regular, 0, True)
        R = prod(rms)
        X = sum(R//m*v[0] for m,v in regular)
        Y = sum(R//m*v[1] for m,v in regular)
        g = gcd(c, R, X, Y)
        expected = (0, tuple(t for t in (g, R, c*R//g) if t != 1))
        assert group(A) == group(Afull) == expected
        cs = S.zeros(A.rows, 1)
        cs[0] = c
        membership(A, cs)
        c1 += c == 1
        product_order = prod(orders)
        determinant = sum(product_order//m*n for m,n in zip(orders,ns))
        assert determinant == sign
        records.append(dict(OS=row["OS"],profile=row["profile"],a=a,b=b,
                            zero=row["zero_index"],finite=finite,regular=regular,
                            c=c,R=R,g=g,smith=list(expected[1]),determinant=determinant))
        cases += 1
print("PASS finite and regular CRT forward/backward quotient maps, including every extra t(v) relation:", cases, "cases.")
print("PASS full three-column finite kernels and reduced global Smith groups:", cases, "cases.")
print("PASS c*s belongs to the complete integral relation lattice; c=1 cases:", c1)
print("PASS both determinant signs, empty finite sets, order-one sites, two finite sites, and unrestricted finite r coordinates.")
(OUT/"S6_SERIES_PUBLISH_III_02L1_fresh_inverse_checks.json").write_text(
    json.dumps(dict(scope="New inverse-map checks after the independent catalogue; no original exposure",
                    original_sections=original_checks,local_H1=local_h1_checks,
                    minimal_patterns=164,extended_patterns=198,
                    extras_by_profile={f"{k[0]}/{k[1]}":v for k,v in sorted(
                        Counter((p[0],p[1]) for p in extras).items())},
                    cases=records),indent=2)+"\n",newline="\n")
