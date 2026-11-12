# D1 sanity check: cubic value groups V_F(N), V_F(Lambda), V_F(J), V_F(M), and dependence on the
# choice of the isometry L (assignment of coordinates to octonion units).
from fractions import Fraction as Fr
from itertools import combinations
import sys, time, random
from flint import fmpz_mat
import sympy as sp
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lat
from lat import g, H, alpha, v, sc, sub, add, hgens, bI, v3, p_vec, q_vec

# ---- Z[sqrt2, sqrt3] arithmetic on 4-tuples (1, r2, r3, r6)
def fmul(x, y):
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return (a0*b0 + 2*a1*b1 + 3*a2*b2 + 6*a3*b3,
            a0*b1 + a1*b0 + 3*(a2*b3 + a3*b2),
            a0*b2 + a2*b0 + 2*(a1*b3 + a3*b1),
            a0*b3 + a3*b0 + a1*b2 + a2*b1)

# ---- quaternion and Cayley-Dickson tables
def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3,
            a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1,
            a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qconj(a): return (a[0], -a[1], -a[2], -a[3])
def omul(x, y):
    a, b = x[:4], x[4:]
    c, d = y[:4], y[4:]
    # (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c))
    p1 = qmul(a, c); p2 = qmul(qconj(d), b)
    p3 = qmul(d, a); p4 = qmul(b, qconj(c))
    return tuple(p1[i] - p2[i] for i in range(4)) + tuple(p3[i] + p4[i] for i in range(4))
def unit(i):
    e = [0]*8; e[i] = 1; return tuple(e)
TAB = {}
for i in range(8):
    for j in range(8):
        pr = omul(unit(i), unit(j))
        k = [t for t in range(8) if pr[t] != 0]
        assert len(k) == 1
        TAB[(i, j)] = (k[0], pr[k[0]])
# Re((u_i u_j) u_k) nonzero iff u_i u_j = +-u_k^{-1}: u_k^2 = -1 for k>0, +1 for k=0
TRI = []
for i in range(8):
    for j in range(8):
        k, s = TAB[(i, j)]
        TRI.append((i, j, k, s * (1 if k == 0 else -1)))
# check the seven positive triples of the file: phi(u_i,u_j,u_k)=<u_i x u_j,u_k> = 1
for (i, j, k) in [(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]:
    assert TAB[(i, j)] == (k, 1), (i, j, k, TAB[(i, j)])

def Lmap(X, tperm=None, bperm=None, bsign=None):
    """X: scaled (x12) integer vector of length 28. Returns 72*L(X): three octonions with entries in Z[r2,r3].
    tperm: permutation of the 8 t-channels -> unit index; bperm: permutation of the 8 b-coordinates -> unit index."""
    tperm = tperm or list(range(8)); bperm = bperm or list(range(8)); bsign = bsign or [1]*8
    q = [[(0, 0, 0, 0)]*8 for _ in range(3)]
    q = [[list((0, 0, 0, 0)) for _ in range(8)] for _ in range(3)]
    for i in range(4):
        blk = X[6*i:6*i+6]
        for p in range(2):
            tot = blk[p] + blk[p+2] + blk[p+4]
            a = tperm[2*i + p]
            for j in range(3):
                q[j][a][0] += 6*blk[p + 2*j] - 2*tot      # 72 * t
    for a in range(8):
        tgt = bperm[a]
        if a < 4:
            blk = X[6*a:6*a+6]
            s = sum((-1)**j * blk[j] for j in range(6))
            for j in range(3):
                q[j][tgt][1] += bsign[a] * s               # 72 * sqrt2 s/6 with s=S/12 -> sqrt2*S
        else:
            dk = X[24 + a - 4]
            for j in range(3):
                q[j][tgt][2] += bsign[a] * 2 * dk          # 72 * sqrt3 d/3 -> 2 sqrt3 * D
    return [[tuple(c) for c in oc] for oc in q]

def F72(X, **kw):
    q1, q2, q3 = Lmap(X, **kw)
    tot = [0, 0, 0, 0]
    for (i, j, k, s) in TRI:
        a = q1[i]; b = q2[j]
        if not any(a) or not any(b): continue
        c = q3[k]
        if not any(c): continue
        t = fmul(fmul(a, b), c)
        for m in range(4): tot[m] += s * t[m]
    return tuple(tot)   # = 72^3 * F(X)

def value_group(gens, **kw):
    vals = []
    m = len(gens)
    f1 = [F72(b, **kw) for b in gens]
    vals += f1
    for i, j in combinations(range(m), 2):
        vals.append(F72(add(gens[i], gens[j]), **kw))
        vals.append(F72(sub(gens[i], gens[j]), **kw))
    for i, j, k in combinations(range(m), 3):
        vals.append(F72(add(add(gens[i], gens[j]), gens[k]), **kw))
    rows = [list(w) for w in set(vals) if any(w)]
    M = fmpz_mat(rows).hnf()
    B = [[int(M[i, j]) for j in range(4)] for i in range(M.nrows())]
    B = [r for r in B if any(r)]
    return B   # integer basis; true values = B / 72^3

D = 72**3
def show(B):
    return [[str(Fr(x, D)) for x in r] for r in B]
def contains(Bbig, Bsmall):
    M1 = fmpz_mat(Bbig + Bsmall).hnf()
    b1 = [[int(M1[i, j]) for j in range(4)] for i in range(M1.nrows())]
    return [r for r in b1 if any(r)] == Bbig
def quotient(Bbig, Bsmall):
    """elementary divisors of Bbig/Bsmall when Bsmall subset Bbig of equal rank"""
    A = sp.Matrix(Bbig).T
    cols = []
    for r in Bsmall:
        sol = (A.T * A).inv() * A.T * sp.Matrix(r)
        cols.append([int(x) for x in sol])
    C = fmpz_mat(cols)
    Sn = C.snf()
    return [int(Sn[i, i]) for i in range(min(Sn.nrows(), Sn.ncols()))]

if __name__ == "__main__":
    t0 = time.time()
    gN = list(g)
    gL = hgens + [v]
    gJ = bI + [v3]
    gM = gJ + [p_vec, q_vec]
    # spot values from the file
    print("72^3 F(alpha) =", F72(alpha), " expected (-4+2r2)/27 ->", (-4*D//27, 2*D//27, 0, 0))
    print("72^3 F(v) =", F72(v), " expected 14/27 - 7r2/24 - r3/27 ->", (14*D//27, -7*D//24, -D//27, 0))
    print("F(p), F(q):", [str(Fr(x, D)) for x in F72(p_vec)], [str(Fr(x, D)) for x in F72(q_vec)])
    VN = value_group(gN); print("V_F(N) basis:", show(VN), round(time.time()-t0, 1))
    VL = value_group(gL); print("V_F(Lambda) basis:", show(VL), round(time.time()-t0, 1))
    VJ = value_group(gJ); print("V_F(J) basis:", show(VJ))
    VM = value_group(gM); print("V_F(M) basis:", show(VM), round(time.time()-t0, 1))
    print("N in J:", contains(VJ, VN), quotient(VJ, VN), " J in L:", contains(VL, VJ), quotient(VL, VJ),
          " J==M:", VJ == VM, " N in L:", contains(VL, VN), quotient(VL, VN))
    # ---- choice dependence: other coordinate-to-unit assignments of the same type
    random.seed(1)
    tests = [("swap b-units 3,4 (alpha_4 <-> d_1)", dict(bperm=[0,1,2,4,3,5,6,7])),
             ("swap t-units 3,4", dict(tperm=[0,1,2,4,3,5,6,7])),
             ("swap both 3,4 (frame permutation, not an automorphism)", dict(tperm=[0,1,2,4,3,5,6,7], bperm=[0,1,2,4,3,5,6,7])),
             ("swap both 1,2 (frame permutation i<->j)", dict(tperm=[0,2,1,3,4,5,6,7], bperm=[0,2,1,3,4,5,6,7])),
             ("b: alphas to units 4..7, d to units 0..3", dict(bperm=[4,5,6,7,0,1,2,3])),
             ("sign of d_1 flipped", dict(bsign=[1,1,1,1,-1,1,1,1])),
             ("sign of alpha_1 flipped", dict(bsign=[-1,1,1,1,1,1,1,1]))]
    for _ in range(3):
        tp = list(range(8)); bp = list(range(8)); random.shuffle(tp); random.shuffle(bp)
        tests.append(("random tperm %s bperm %s" % (tp, bp), dict(tperm=tp, bperm=bp)))
    for name, kw in tests:
        A = value_group(gN, **kw); Bv = value_group(gL, **kw)
        inc = contains(Bv, A)
        qd = quotient(Bv, A) if inc and len(A) == len(Bv) else None
        print("CHOICE:", name)
        print("   V(N) =", show(A))
        print("   V(L) =", show(Bv))
        print("   V(N) subset V(L):", inc, " elementary divisors of V(L)/V(N):", qd, round(time.time()-t0, 1))
