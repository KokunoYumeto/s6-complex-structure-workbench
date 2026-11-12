"""Exact native open-face coefficients, norms, shifts, and residual checks.

Standard-library arithmetic only. All graph vectors are stored after
multiplication by 12; every reported norm removes exactly that factor.
No floating eigenvalues, external packages, writes, or Lean processes.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(*ps):
    out = [F(0)] * max(map(len, ps))
    for p in ps:
        for i, x in enumerate(p):
            out[i] += x
    return trim(out)


def scale(p, c):
    return trim([c * x for x in p])


def mul(*ps):
    out = (F(1),)
    for p in ps:
        vals = [F(0)] * (len(out) + len(p) - 1)
        for i, x in enumerate(out):
            for j, y in enumerate(p):
                vals[i + j] += x * y
        out = trim(vals)
    return out


def power(p, n):
    return mul(*([p] * n))


def compose(p, q):
    return add(*(scale(power(q, i), x) for i, x in enumerate(p)))


def value(p, x):
    out = F(0)
    for c in reversed(p):
        out = out * x + c
    return out


def same(p, q):
    assert trim(p) == trim(q), (p, q)


# Exact polynomial identities in L, not numerical fitting.
ell = (F(0), F(1))
one = (F(1),)
minus_one = add(ell, (-1,))
P2 = scale(mul(ell, add(ell, one), add(scale(ell, 2), one)), F(1, 6))
P4 = scale(mul(ell, add(ell, one), add(scale(ell, 2), one),
               add(scale(power(ell, 2), 3), scale(ell, 3), (-1,))), F(1, 30))
for deg, poly in ((2, P2), (4, P4)):
    assert value(poly, 0) == 0
    same(add(poly, scale(compose(poly, minus_one), -1)), power(ell, deg))

s0 = scale(ell, 2)
s1 = scale(ell, -1)
s2 = scale(mul(ell, add(scale(power(ell, 2), 2), one)), F(1, 3))
s3 = scale(power(ell, 3), -1)
s4 = scale(mul(ell, add(scale(power(ell, 4), 6),
                         scale(power(ell, 2), 10), (-1,))), F(1, 15))
same(s2, add(power(ell, 2), scale(compose(P2, minus_one), 2)))
same(s4, add(power(ell, 4), scale(compose(P4, minus_one), 2)))

fsq = scale(mul(ell, add(scale(power(ell, 4), 4), one)), F(1, 40))
dsq = scale(mul(ell, add(scale(power(ell, 2), 4), (-1,))), F(1, 24))
same(fsq, add(scale(s4, F(1, 4)), scale(s3, F(1, 2)),
              scale(s2, F(1, 2)), scale(s1, F(1, 4)), scale(s0, F(1, 16))))
same(dsq, add(scale(s2, F(1, 4)), scale(s1, F(1, 4)), scale(s0, F(1, 16))))

mp = scale(ell, 2)
AA = add(scale(power(ell, 7), F(4, 5)), scale(power(ell, 6), F(6, 5)),
         scale(power(ell, 5), F(2, 3)), scale(power(ell, 3), F(1, 30)),
         scale(power(ell, 2), F(1, 20)))
BB = add(scale(power(ell, 7), F(4, 5)), scale(power(ell, 5), F(4, 3)),
         scale(power(ell, 3), F(-2, 15)))
RR = add(scale(power(ell, 6), F(6, 5)), scale(power(ell, 5), F(2, 3)),
         scale(power(ell, 3), F(-1, 6)), scale(power(ell, 2), F(1, 20)))
CC = add(scale(power(ell, 5), F(-2, 3)), scale(power(ell, 3), F(1, 6)))
same(AA, add(mul(mp, add(mp, one), fsq),
             scale(mul(power(mp, 2), add(s4, power(ell, 4))), F(1, 4))))
same(BB, scale(mul(power(mp, 2), s4), F(1, 2)))
same(RR, add(mul(power(mp, 2), dsq), mul(mp, fsq),
             scale(mul(power(mp, 2), power(ell, 4)), F(1, 4))))
same(CC, mul(power(mp, 2), add(scale(s3, F(1, 4)), scale(s2, F(1, 8)))))
same(AA, add(BB, scale(CC, 2), RR))

interior_diff = scale(add(scale(power(ell, 3), 8),
                          scale(power(ell, 2), -12), scale(ell, 10), (-3,)), F(1, 12))
same(interior_diff,
     add(s2, s1, scale(s0, F(1, 4)),
         scale(power(add(ell, (F(-1, 2),)), 2), -1)))
D2p = mul(power(mp, 2),
          add(scale(add(power(ell, 4), power(minus_one, 4)), F(1, 4)),
              interior_diff))
Dsum = add(scale(power(ell, 6), F(14, 5)), scale(power(ell, 5), F(-4, 3)),
           scale(power(ell, 4), F(10, 3)), scale(power(ell, 3), F(-2, 3)),
           scale(power(ell, 2), F(-2, 15)))
same(Dsum, add(mul(mp, s4), D2p))
assert AA[-1] == BB[-1] == F(4, 5)
assert len(RR) == 7 and len(Dsum) == 7
print("All polynomial identities and finite-sum telescoping identities passed.")


def shifted(n, i, k=1):
    r = list(n)
    r[i] += k
    return tuple(r)


def edges(p):
    n, i, j = p
    return ((n, i), (shifted(n, i), j), (shifted(n, j), i), (n, j))


planes = tuple(combinations(range(3), 2))


def bulk_neighbors(p):
    n, i, j = p
    out = []
    for k in (i, j):
        for sign in (-1, 1):
            out.append((shifted(n, k, sign), i, j))
    for k, l in planes:
        if (i, j) == (k, l):
            continue
        source_transverse = next(iter({i, j} - {k, l}))
        target_transverse = next(iter({k, l} - {i, j}))
        for a, b in product((0, 1), repeat=2):
            base = shifted(shifted(n, source_transverse, a), target_transverse, -b)
            out.append((base, k, l))
    assert len(out) == len(set(out)) == 12
    return out


def dot(x, y):
    return F(sum(x[p] * y[p] for p in x), 144)


def q_apply(x, adj):
    return {p: len(adj[p]) * x[p] + sum(x[q] for q in adj[p]) for p in x}


rows = []
for L in range(2, 7):
    m = 2 * L
    faces = [(n, i, j) for n in product(range(-L, L + 1), repeat=3)
             for i, j in planes if n[i] < L and n[j] < L]
    face_set = set(faces)
    stars = defaultdict(list)
    for p in faces:
        for e in edges(p):
            stars[e].append(p)
    adj = {p: set() for p in faces}
    pairs = set()
    for star in stars.values():
        for p, q in combinations(star, 2):
            pair = frozenset((p, q))
            assert pair not in pairs
            pairs.add(pair)
            adj[p].add(q)
            adj[q].add(p)
    assert len(faces) == 12 * L * L * (2 * L + 1)
    assert len(pairs) == 144 * L**3 - 12 * L

    def in_cube(n):
        return all(-L <= t < L for t in n)

    def g2(n):
        return n[1] ** 2 if in_cube(n) else 0  # Exactly twice g_L.

    a12, b12, r12, u24, u12 = {}, {}, {}, {}, {}
    for p in faces:
        n, i, j = p
        t = n[1]
        alpha = (i, j)
        a12[p] = 3 * (2 * t * t + 2 * t + 1) if alpha == (0, 1) else (
            6 * t * t if alpha == (0, 2) else 0)
        # The original Gamma Casimir map, checked independently by edges.
        assert a12[p] == 3 * sum(base[1] ** 2 for base, direction in edges(p)
                                 if direction == 0)
        b12[p] = 6 * g2(n) if alpha in ((0, 1), (0, 2)) else 0
        r12[p] = a12[p] - b12[p]
        if in_cube(n) and alpha == (0, 1):
            expected = 6 * t + 3
        elif alpha == (0, 1) and n[2] == L:
            expected = 3 * (2 * t * t + 2 * t + 1)
        elif alpha == (0, 2) and n[1] == L:
            expected = 6 * L * L
        else:
            expected = 0
        assert r12[p] == expected
        u24[p] = 4 * g2(n)
        u12[p] = (2 if alpha != (1, 2) else -4) * g2(n)
        assert u24[p] + u12[p] == b12[p]

        assert adj[p] == (set(bulk_neighbors(p)) & face_set)
        normal = 3 - i - j
        beta = lambda t: int(t == -L) + int(t == L - 1)
        deficit = beta(n[i]) + beta(n[j]) + 4 * int(n[normal] in (-L, L))
        assert 12 - len(adj[p]) == deficit
        for q in bulk_neighbors(p):
            assert len(set(edges(p)) & set(edges(q))) == 1

    A, B, R, C = dot(a12, a12), dot(b12, b12), dot(r12, r12), dot(b12, r12)
    assert (A, B, R, C) == tuple(value(poly, L) for poly in (AA, BB, RR, CC))
    assert A == B + 2 * C + R and C < 0
    assert dot(u24, u12) == 0
    assert dot(u24, u24) == F(2, 3) * B
    assert dot(u12, u12) == F(1, 3) * B
    assert A >= F(4, 5) * L**7
    interval = range(-L, L)
    assert tuple(sum(F(t) ** k for t in interval) for k in range(5)) == tuple(
        value(poly, L) for poly in (s0, s1, s2, s3, s4))

    box_nearby = tuple(product(range(-L - 1, L + 1), repeat=3))
    D = [F(sum((g2(shifted(n, i)) - g2(n)) ** 2 for n in box_nearby), 4)
         for i in range(3)]
    assert D[0] == D[2] == F(m, 2) * value(s4, L)
    assert D[1] == value(D2p, L)
    assert sum(D) == value(Dsum, L)
    assert sum(F(2 * t + 1, 2) ** 2 for t in range(-L, L - 1)) == value(interior_diff, L)
    for i, j in combinations(range(3), 2):
        delta = F(sum((g2(shifted(shifted(n, i), j, -1)) - g2(n)) ** 2
                      for n in box_nearby), 4)
        assert delta <= 2 * (D[i] + D[j])

    resnorms = {}
    for eigenvalue, vector, vnorm2 in ((24, u24, F(4, 3)), (12, u12, F(2, 3))):
        def extended_u(p):
            n, i, j = p
            factor = 4 if eigenvalue == 24 else (2 if (i, j) != (1, 2) else -4)
            return factor * g2(n)

        bulk_res = {}
        for n in box_nearby:
            for i, j in planes:
                p = (n, i, j)
                bulk_res[p] = ((12 - eigenvalue) * extended_u(p)
                               + sum(extended_u(q) for q in bulk_neighbors(p)))
        bulk_norm = F(sum(x*x for x in bulk_res.values()), 144)
        assert bulk_norm <= 72 * vnorm2 * sum(D)
        boundary_vec = {p: (12 - len(adj[p])) * vector[p] for p in faces}
        E = dot(boundary_vec, boundary_vec)
        E_formula = F(0)
        for p in faces:
            n, i, j = p
            if not in_cube(n):
                continue
            normal = 3 - i - j
            bracket = beta(n[i]) + beta(n[j]) + 4 * int(n[normal] == -L)
            E_formula += F(bracket * bracket * vector[p] * vector[p], 144)
        assert E == E_formula
        assert E <= 45 * m*m * L**4 * vnorm2
        qvec = q_apply(vector, adj)
        residual = {p: qvec[p] - eigenvalue * vector[p] for p in faces}
        for p in faces:
            assert residual[p] == bulk_res[p] - boundary_vec[p]
        residual_norm = dot(residual, residual)
        assert residual_norm <= 2 * bulk_norm + 2 * E
        assert residual_norm <= 2 * vnorm2 * (72 * sum(D) + 45 * m*m * L**4)
        resnorms[eigenvalue] = residual_norm

    qa = q_apply(a12, adj)
    qform = dot(a12, qa)
    qsecond = dot(qa, qa)
    assert qform == F(sum((a12[p] + a12[q]) ** 2
                         for p, q in (tuple(pair) for pair in pairs)), 144)
    deficit_form = F(sum((a12[p] - a12[q]) ** 2
                         for p, q in (tuple(pair) for pair in pairs))
                     + 2 * sum((12-len(adj[p])) * a12[p] ** 2 for p in faces), 144)
    assert 24 * A - qform == deficit_form >= 0
    assert qsecond * A >= qform * qform
    Fmean = F(7, 15) - qform / (21 * A)
    rows.append((L, len(faces), A, qform/A, Fmean))
    print(f"L={L}: {len(faces)} faces; A={A}; all native entries, exact boundary "
          "and bulk residual identities passed.")

# Exact endpoint pushforward and the limiting first two moments.
v24, v12 = (F(2, 3),)*3, (F(1, 3), F(1, 3), F(-2, 3))
for vv, lam in ((v24, 24), (v12, 12)):
    assert tuple(12 * x + 4 * sum(vv) for x in vv) == tuple(lam * x for x in vv)
assert sum(x*y for x, y in zip(v24, v12)) == 0
phi = lambda q: F(7, 15) - F(q, 21)
assert (phi(24), phi(12)) == (F(-71, 105), F(-11, 105))
weights = ((F(2, 3), 24), (F(1, 3), 12))
qmean = sum(w*q for w, q in weights)
qsecond = sum(w*q*q for w, q in weights)
fmean = sum(w*phi(q) for w, q in weights)
fvar = sum(w*(phi(q)-fmean)**2 for w, q in weights)
assert (qmean, qsecond, qsecond-qmean*qmean, fmean, fvar) == (
    20, 432, 32, F(-17, 35), F(32, 441))
assert (F(4, 5)*F(2, 3), F(4, 5)*F(1, 3)) == (F(8, 15), F(4, 15))
print("Exact affine spectral pushforward, limiting weights, means, and variances passed.")
print("Finite native graph means (exact rational diagnostics, not eigenvalue fits):")
for L, count, A, qmean, fmean in rows:
    print(f"  L={L}: <Q>/A={qmean}; <F>/A={fmean}")
print("PASS: the companion all-L proof retains native amplitude and every open boundary.")
