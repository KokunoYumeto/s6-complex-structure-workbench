"""Delta_{0,6} (boundary complex of M_{0,6}bar = space of phylogenetic trees on 6 leaves, link):
the cycle lattice Z_2 = ker(d_2) in C_2 = Z^{triangles} with the induced (standard) form;
its rank, evenness, determinant, discriminant group, short vectors; the S_6 character on it and its
decomposition into irreducibles (Murnaghan-Nakayama). Exact integer arithmetic throughout.
usage: python -B delta06_lattice.py"""
import itertools
import sys
from fractions import Fraction

sys.stdout.reconfigure(encoding="utf-8")
L = range(6)
# splits: side not containing leaf 0, size 2..4
S = [frozenset(c) for k in (2, 3, 4) for c in itertools.combinations(range(1, 6), k)]
idx = {s: i for i, s in enumerate(S)}


def comp(a, b):
    return a <= b or b <= a or not (a & b)


E = [(i, j) for i, j in itertools.combinations(range(len(S)), 2) if comp(S[i], S[j])]
T = [t for t in itertools.combinations(range(len(S)), 3) if all(comp(S[a], S[b]) for a, b in itertools.combinations(t, 2))]
eidx = {e: k for k, e in enumerate(E)}
print("vertices", len(S), "edges", len(E), "triangles", len(T))
# boundary d2: rows edges, cols triangles
d2 = [[0] * len(T) for _ in E]
for c, (i, j, k) in enumerate(T):
    d2[eidx[(j, k)]][c] += 1
    d2[eidx[(i, k)]][c] -= 1
    d2[eidx[(i, j)]][c] += 1


def int_kernel(A, n):
    """Z-basis of {x in Z^n : A x = 0} by unimodular column operations."""
    A = [row[:] for row in A]
    U = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # columns = basis
    m = len(A)
    piv = 0
    for r in range(m):
        # reduce columns piv..n-1 on row r to a single nonzero at column piv
        while True:
            nz = [c for c in range(piv, n) if A[r][c] != 0]
            if len(nz) <= 1:
                break
            c0 = min(nz, key=lambda c: abs(A[r][c]))
            for c in nz:
                if c == c0:
                    continue
                q = A[r][c] // A[r][c0]
                if q:
                    for rr in range(m):
                        A[rr][c] -= q * A[rr][c0]
                    for rr in range(n):
                        U[rr][c] -= q * U[rr][c0]
        nz = [c for c in range(piv, n) if A[r][c] != 0]
        if nz:
            c = nz[0]
            if c != piv:
                for rr in range(m):
                    A[rr][c], A[rr][piv] = A[rr][piv], A[rr][c]
                for rr in range(n):
                    U[rr][c], U[rr][piv] = U[rr][piv], U[rr][c]
            piv += 1
    return [[U[rr][c] for rr in range(n)] for c in range(piv, n)]  # list of kernel vectors


K = int_kernel(d2, len(T))
print("kernel rank", len(K))
assert all(sum(d2[r][c] * v[c] for c in range(len(T))) == 0 for v in K for r in range(len(E)))


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def lll(B, delta=Fraction(99, 100)):
    B = [b[:] for b in B]
    n = len(B)

    def gso(B):
        Bs, mu = [], [[Fraction(0)] * n for _ in range(n)]
        for i in range(n):
            v = [Fraction(x) for x in B[i]]
            for j in range(i):
                mu[i][j] = Fraction(dot(B[i], Bs[j][0])) if False else sum(Fraction(a) * b for a, b in zip(B[i], Bs[j])) / sum(b * b for b in Bs[j])
                v = [a - mu[i][j] * b for a, b in zip(v, Bs[j])]
            Bs.append(v)
        return Bs, mu
    Bs, mu = gso(B)
    k = 1
    while k < n:
        for j in range(k - 1, -1, -1):
            q = round(mu[k][j])
            if q:
                B[k] = [a - q * b for a, b in zip(B[k], B[j])]
                Bs, mu = gso(B)
        nk = sum(x * x for x in Bs[k]); nk1 = sum(x * x for x in Bs[k - 1])
        if nk >= (delta - mu[k][k - 1] ** 2) * nk1:
            k += 1
        else:
            B[k], B[k - 1] = B[k - 1], B[k]
            Bs, mu = gso(B)
            k = max(k - 1, 1)
    return B


G = [[dot(u, v) for v in K] for u in K]
print("Gram diagonal (norms of LLL basis):", sorted(G[i][i] for i in range(24)))
print("even:", all(G[i][i] % 2 == 0 for i in range(24)))


def det_bareiss(M):
    M = [r[:] for r in M]
    n = len(M)
    sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if M[i][k] != 0), None)
            if sw is None:
                return 0
            M[k], M[sw] = M[sw], M[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


dG = det_bareiss(G)
print("det Gram =", dG, "=", end=" ")
n_, f, fac = dG, 2, []
while f * f <= n_:
    while n_ % f == 0:
        fac.append(f); n_ //= f
    f += 1
if n_ > 1:
    fac.append(n_)
from collections import Counter
print(" * ".join("%d^%d" % (p, e) if e > 1 else str(p) for p, e in sorted(Counter(fac).items())))


def smith_diag(M):
    M = [r[:] for r in M]
    n = len(M)
    diag = []
    for t in range(n):
        # find nonzero pivot with minimal abs in submatrix
        while True:
            entries = [(abs(M[i][j]), i, j) for i in range(t, n) for j in range(t, n) if M[i][j] != 0]
            if not entries:
                return diag + [0] * (n - t)
            _, i, j = min(entries)
            M[t], M[i] = M[i], M[t]
            for r in M:
                r[t], r[j] = r[j], r[t]
            p = M[t][t]
            done = True
            for i in range(t + 1, n):
                q = M[i][t] // p
                if q:
                    M[i] = [a - q * b for a, b in zip(M[i], M[t])]
                if M[i][t] != 0:
                    done = False
            for j in range(t + 1, n):
                q = M[t][j] // p
                if q:
                    for r in M:
                        r[j] -= q * r[t]
                if M[t][j] != 0:
                    done = False
            if done:
                bad = [(i, j) for i in range(t + 1, n) for j in range(t + 1, n) if M[i][j] % p != 0]
                if bad:
                    i, j = bad[0]
                    M[t] = [a + b for a, b in zip(M[t], M[i])]
                    continue
                diag.append(abs(p))
                break
    return diag


sd = smith_diag(G)
print("discriminant group invariants (Smith, >1):", [d for d in sd if d != 1])
# S_6 action
def act(p, s):
    img = frozenset(p[x] for x in s)
    return img if 0 not in img else frozenset(range(6)) - img


def tri_perm(p):
    """signed permutation of triangles"""
    out = []
    for (i, j, k) in T:
        vs = [idx[act(p, S[i])], idx[act(p, S[j])], idx[act(p, S[k])]]
        order = sorted(range(3), key=lambda a: vs[a])
        # sign of permutation 'order'
        sgn = 1
        o = order[:]
        for a in range(3):
            for b in range(a + 1, 3):
                if o[a] > o[b]:
                    sgn = -sgn
        out.append((T.index(tuple(sorted(vs))), sgn))
    return out


Ginv = None
# exact rational inverse of G
from fractions import Fraction as Fr
n = 24
Aug = [[Fr(G[i][j]) for j in range(n)] + [Fr(1 if i == j else 0) for j in range(n)] for i in range(n)]
for c in range(n):
    p = next(r for r in range(c, n) if Aug[r][c] != 0)
    Aug[c], Aug[p] = Aug[p], Aug[c]
    pv = Aug[c][c]
    Aug[c] = [x / pv for x in Aug[c]]
    for r in range(n):
        if r != c and Aug[r][c] != 0:
            f_ = Aug[r][c]
            Aug[r] = [a - f_ * b for a, b in zip(Aug[r], Aug[c])]
Ginv = [row[n:] for row in Aug]


def trace_on_kernel(p):
    tp = tri_perm(p)
    PK = []
    for v in K:
        w = [0] * len(T)
        for c, (c2, s) in enumerate(tp):
            w[c2] += s * v[c]
        PK.append(w)
    # R = Ginv * (K^T PK): R[i][j] = coefficient of K_i in PK_j
    M = [[dot(K[i], PK[j]) for j in range(24)] for i in range(24)]
    tr = sum(sum(Ginv[i][k] * M[k][i] for k in range(24)) for i in range(24))
    return tr


def perm_from_cycles(cyc):
    p = list(range(6))
    for c in cyc:
        for a, b in zip(c, c[1:] + c[:1]):
            p[a] = b
    return p


classes = {"1^6": [], "2": [(0, 1)], "2^2": [(0, 1), (2, 3)], "2^3": [(0, 1), (2, 3), (4, 5)], "3": [(0, 1, 2)],
           "3.2": [(0, 1, 2), (3, 4)], "3^2": [(0, 1, 2), (3, 4, 5)], "4": [(0, 1, 2, 3)], "4.2": [(0, 1, 2, 3), (4, 5)],
           "5": [(0, 1, 2, 3, 4)], "6": [(0, 1, 2, 3, 4, 5)]}
sizes = {"1^6": 1, "2": 15, "2^2": 45, "2^3": 15, "3": 40, "3.2": 120, "3^2": 40, "4": 90, "4.2": 90, "5": 144, "6": 120}
chi = {}
for name, cyc in classes.items():
    chi[name] = trace_on_kernel(perm_from_cycles(cyc))
print("character of S_6 on H_2:", {k: str(v) for k, v in chi.items()})
# Murnaghan-Nakayama
def partitions(n, m=None):
    m = m or n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def mn(lam, mu):
    """chi^lam(mu) via Murnaghan-Nakayama with beta-sets"""
    if not mu:
        return 1
    r, rest = mu[0], mu[1:]
    n = len(lam)
    beta = [lam[i] + (n - 1 - i) for i in range(n)]
    total = 0
    for i, b in enumerate(beta):
        nb = b - r
        if nb < 0 or nb in beta:
            continue
        height = sum(1 for x in beta if nb < x < b)
        newbeta = sorted([x for x in beta if x != b] + [nb], reverse=True)
        newlam = [newbeta[j] - (n - 1 - j) for j in range(n)]
        newlam = tuple(x for x in newlam if x > 0)
        total += (-1) ** height * mn(newlam, rest)
    return total


ctype = {"1^6": (1, 1, 1, 1, 1, 1), "2": (2, 1, 1, 1, 1), "2^2": (2, 2, 1, 1), "2^3": (2, 2, 2), "3": (3, 1, 1, 1),
         "3.2": (3, 2, 1), "3^2": (3, 3), "4": (4, 1, 1), "4.2": (4, 2), "5": (5, 1), "6": (6,)}
dec = {}
for lam in partitions(6):
    m = sum(Fr(sizes[c]) * chi[c] * mn(lam, ctype[c]) for c in classes) / 720
    if m:
        dec[lam] = m
print("decomposition into S_6 irreducibles (partition: multiplicity):", {str(k): str(v) for k, v in dec.items()})
