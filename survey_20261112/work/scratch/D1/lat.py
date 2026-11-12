# D1 sanity checks: lattice side. Exact integer arithmetic (coordinates scaled by 12).
from fractions import Fraction as Fr
from itertools import product, combinations
from collections import Counter
import math, time
import numpy as np
from flint import fmpz_mat

S = 12  # scale


def vec(blocks, d=(0, 0, 0, 0)):
    out = []
    for b in blocks:
        out += list(b)
    out += list(d)
    r = []
    for x in out:
        y = Fr(x) * S
        assert y.denominator == 1, x
        r.append(int(y))
    return tuple(r)


Z6 = (0,) * 6


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def sc(k, a):
    return tuple(k * x for x in a)


def ip(a, b):
    return Fr(sum(x * y for x, y in zip(a, b)), S * S)


lam = tuple(Fr(x, 6) for x in (5, -1, -1, -1, -1, -1))


def klam(k):
    return tuple(k * x for x in lam)


g = []
for i in range(4):
    for j in range(5):
        b = [Z6] * 4
        e = [0] * 6
        e[j] = 1
        e[j + 1] = -1
        b[i] = tuple(e)
        g.append(vec(b))
for d in [(1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1), (0, 0, 1, 1)]:
    g.append(vec([Z6] * 4, d))
vD = (1, 0, 0, 0)
sD = tuple(Fr(1, 2) for _ in range(4))
g.append(vec([klam(3)] * 4))  # g25
g.append(vec([klam(3), klam(3), Z6, Z6], vD))  # g26
g.append(vec([klam(3), Z6, klam(3), Z6], sD))  # g27
g.append(vec([klam(2), klam(2), klam(2), Z6]))  # g28
g.append(vec([klam(2), klam(4), Z6, klam(2)]))  # g29
assert len(g) == 29
rhoA = tuple(Fr(x, 2) for x in (5, 3, 1, -1, -3, -5))
rhoD = (3, 2, 1, 0)
rho = vec([rhoA] * 4, rhoD)
alpha = g[0]
assert ip(rho, rho) == 84 and ip(rho, alpha) == 1
H = [ip(rho, x) for x in g]
_v = tuple(Fr(a, 6) - b for a, b in zip(rho, alpha))
assert all(x.denominator == 1 for x in _v)
v = tuple(int(x) for x in _v)
assert ip(v, v) == 4


def basis(gens):
    M = fmpz_mat([list(x) for x in gens]).hnf()
    rows = [[int(M[i, j]) for j in range(M.ncols())] for i in range(M.nrows())]
    return [r for r in rows if any(r)]


def gram(B):
    n = len(B)
    return [[sum(x * y for x, y in zip(B[i], B[j])) for j in range(n)] for i in range(n)]


def det_true(B):
    G = fmpz_mat(gram(B))
    return Fr(int(G.det()), (S * S) ** len(B))


def is_even_integral(B):
    G = gram(B)
    n = len(B)
    return all(G[i][j] % (S * S) == 0 for i in range(n) for j in range(n)) and all(
        (G[i][i] // (S * S)) % 2 == 0 for i in range(n))


def member(B, x):
    return basis(B + [list(x)]) == basis(B)


def short_vectors(B, bound):
    M = fmpz_mat(B).lll()
    Bl = [[int(M[i, j]) for j in range(M.ncols())] for i in range(M.nrows())]
    n = len(Bl)
    G = np.array(gram(Bl), dtype=float) / (S * S)
    R = np.linalg.cholesky(G).T
    Rl = R.tolist()
    res = []
    x = [0] * n
    eps = 1e-7

    def rec(i, rem):
        c = 0.0
        row = Rl[i]
        for j in range(i + 1, n):
            c += row[j] * x[j]
        rii = row[i]
        center = -c / rii
        rad = math.sqrt(max(rem, 0.0) + eps) / rii
        lo = math.ceil(center - rad)
        hi = math.floor(center + rad)
        for xi in range(lo, hi + 1):
            x[i] = xi
            t = c + rii * xi
            nr = rem - t * t
            if nr < -eps:
                continue
            if i == 0:
                if any(x):
                    res.append(tuple(x))
            else:
                rec(i - 1, nr)
        x[i] = 0

    rec(n - 1, bound)
    out = set()
    for xs in res:
        w = tuple(sum(xs[k] * Bl[k][j] for k in range(n)) for j in range(len(Bl[0])))
        nrm = ip(w, w)
        if nrm > bound:
            continue
        mw = tuple(-t for t in w)
        out.add((max(w, mw), nrm))
    return out


def root_system(roots):
    R = list(roots)
    n = len(R)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if sum(a * b for a, b in zip(R[i], R[j])) != 0:
                adj[i].append(j)
                adj[j].append(i)
    seen = [False] * n
    comps = []
    for i in range(n):
        if seen[i]:
            continue
        st = [i]
        seen[i] = True
        c = []
        while st:
            k = st.pop()
            c.append(k)
            for m in adj[k]:
                if not seen[m]:
                    seen[m] = True
                    st.append(m)
        comps.append(c)
    desc = []
    for c in comps:
        rk = int(np.linalg.matrix_rank(np.array([R[k] for k in c], dtype=float)))
        nr = 2 * len(c)
        name = None
        if rk * (rk + 1) == nr:
            name = "A%d" % rk
        elif rk >= 4 and 2 * rk * (rk - 1) == nr:
            name = "D%d" % rk
        if (rk, nr) in [(6, 72), (7, 126), (8, 240)]:
            name = "E%d" % rk
        desc.append(name or "?(rank%d,%d)" % (rk, nr))
    return dict(Counter(desc))


def rmap(x):
    out = list(x)
    for i in range(4):
        for j in range(6):
            out[6 * i + j] = x[6 * i + (j - 2) % 6]
    return tuple(out)


def omega(t):
    return tuple(Fr(1 if j < t else 0) - Fr(t, 6) for j in range(6))


hgens = [sc(6, alpha)] + [sub(g[i], sc(int(H[i]), alpha)) for i in range(1, 29)]
bI = [sc(6, alpha)] + [sub(g[i], sc(int(H[i]), alpha)) for i in range(1, 28)] + [sub(sc(3, g[28]), sc(60, alpha))]
v3 = sc(3, v)
u_star = vec([omega(2), omega(4), Z6, omega(2)])
p_vec = sub(u_star, rmap(u_star))
q_vec = add(v, sub(rmap(u_star), rmap(v)))

if __name__ == "__main__":
    t0 = time.time()
    print("heights of glue lifts:", [str(h) for h in H[24:]])
    BR = basis(g[:24])
    print("det R_ES =", det_true(BR), "(expect 5184 = 6^4*4); sqrt =", math.isqrt(5184))
    BN = basis(g)
    print("rank N =", len(BN), "det N =", det_true(BN), "even integral:", is_even_integral(BN))
    sv = short_vectors(BN, 2)
    roots = [w for w, n in sv if n == 2]
    print("roots of N:", 2 * len(roots), root_system(roots))
    gens2 = [(1, 1, 1, 1, 0, 0), (1, 1, 0, 0, 1, 0), (1, 0, 1, 0, 0, 1)]
    C2 = set()
    for c in product(range(2), repeat=3):
        C2.add(tuple(sum(c[k] * gens2[k][m] for k in range(3)) % 2 for m in range(6)))
    C3 = set()
    for a, b in product(range(3), repeat=2):
        C3.add(((a + b) % 3, (a + 2 * b) % 3, a, b))
    mins = Counter()
    for u in C2:
        for z in C3:
            k = [(3 * u[i] + 2 * z[i]) % 6 for i in range(4)]
            m = sum(Fr(ki * (6 - ki), 6) for ki in k) + (1 if (u[4], u[5]) != (0, 0) else 0)
            mins[str(m)] += 1
    print("glue class minima:", dict(mins))
    BK = basis(hgens)
    print("det K =", det_true(BK), "(expect 36)")
    BL = basis(hgens + [v])
    print("det Lambda =", det_true(BL), "even integral:", is_even_integral(BL))
    svL = short_vectors(BL, 2)
    print("vectors of norm <=2 in Lambda (pairs):", len(svL), "time", round(time.time() - t0, 1))
    BL1 = basis([rmap(x) for x in BL])
    BL2 = basis([rmap(rmap(x)) for x in BL])
    print("L0==L1?", BL == BL1, "L0==L2?", BL == BL2, "L1==L2?", BL1 == BL2)
    for (a, b, nm) in [(BL, BL1, "01"), (BL1, BL2, "12"), (BL2, BL, "20")]:
        print(" det(L_%s sum) =" % nm, det_true(basis(a + b)))
    BI = basis(bI)
    BJ = basis(bI + [v3])
    print("det I =", det_true(BI), "det J =", det_true(BJ))

    def in_unimod(B, x):
        return all(ip(x, y).denominator == 1 for y in B)

    print("J in L0,L1,L2:", all(in_unimod(BL, x) for x in BJ), all(in_unimod(BL1, x) for x in BJ),
          all(in_unimod(BL2, x) for x in BJ))
    print("rJ == J:", basis([rmap(x) for x in BJ]) == BJ)
    BM = basis(BJ + [p_vec, q_vec])
    print("det M =", det_true(BM), "even integral:", is_even_integral(BM), "rM==M:",
          basis([rmap(x) for x in BM]) == BM)
    svM = short_vectors(BM, 2)
    rootsM = [w for w, n in svM if n == 2]
    print("roots of M:", 2 * len(rootsM), root_system(rootsM))
    print("det(M+N) =", det_true(basis(BM + BN)), "(index of M cap N in N is the inverse sqrt)")
    e = [u_star, v, rmap(u_star), rmap(v)]

    def comb(c):
        w = (0,) * 28
        for ci, ei in zip(c, e):
            w = add(w, sc(ci, ei))
        return w

    print("e_i in J^vee:", all(ip(x, y).denominator == 1 for x in e for y in BJ))
    iso = [c for c in product(range(3), repeat=4) if any(c) and ip(comb(c), comb(c)) % 2 == 0]
    iso_set = set(iso)
    print("number of nonzero isotropic vectors in J^vee/J:", len(iso))
    # compare with formula q_J = (2/3)(2ad+bc+bd)
    okf = all(((2 * a * d + b * c + b * d) % 3 == 0) == ((a, b, c, d) in iso_set)
              for (a, b, c, d) in product(range(3), repeat=4) if any((a, b, c, d)))
    print("isotropy agrees with formula (RF24):", okf)
    planes = set()
    for c1, c2 in combinations(iso, 2):
        span = frozenset(tuple((a_ * x + b_ * y) % 3 for x, y in zip(c1, c2))
                         for a_, b_ in product(range(3), repeat=2))
        if len(span) == 9 and all(s == (0, 0, 0, 0) or s in iso_set for s in span):
            planes.add(span)
    print("number of totally isotropic planes:", len(planes))
    for P in sorted(planes, key=lambda s: sorted(s)):
        nz = sorted(s for s in P if any(s))
        c1 = nz[0]
        c2 = next(s for s in nz if s not in (c1, tuple((2 * x) % 3 for x in c1)))
        BP = basis(BJ + [comb(c1), comb(c2)])
        dd = det_true(BP)
        ev = is_even_integral(BP)
        svP = short_vectors(BP, 2)
        rt = [w for w, n in svP if n == 2]
        rs = root_system(rt) if rt else {}
        rfix = basis([rmap(x) for x in BP]) == BP
        tag = "L0" if BP == BL else "L1" if BP == BL1 else "L2" if BP == BL2 else "M" if BP == BM else ""
        print(" plane", c1, c2, "det", dd, "even", ev, "roots", 2 * len(rt), rs, "r-stable", rfix, tag)
    print("total time", round(time.time() - t0, 1))
