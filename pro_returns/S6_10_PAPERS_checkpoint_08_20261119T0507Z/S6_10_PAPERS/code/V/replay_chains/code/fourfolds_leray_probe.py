# Heuristic Betti-number count for torus fibrations over P^1 via Leray:
#   b_k = sum_{p+q=k} h^p(P^1; j_* Lambda^q V) + (skyscraper corrections K^q at the cusp)
# assuming E_2-degeneration and R^q f_* Q = j_* Lambda^q V (+) K^q.  Tested on X (should give S^6).
import itertools
from sympy import Matrix, eye, zeros, Rational

def ext_power(M, q):
    n = M.shape[0]
    idx = list(itertools.combinations(range(n), q))
    N = zeros(len(idx), len(idx))
    for a, I in enumerate(idx):
        for b, J in enumerate(idx):
            N[a, b] = M.extract(list(I), list(J)).det()
    return N

def inv_dim(mats):
    # dim of common fixed vectors
    n = mats[0].shape[0]
    stack = Matrix.vstack(*[m - eye(n) for m in mats])
    return n - stack.rank()

def betti(mono, Kcorr, name):
    # mono: list of local monodromy matrices on H_1 (product = I); cohomology rep = inverse transpose
    n = mono[0].shape[0]
    b = [0]*(n+3)
    for q in range(n+1):
        L = [ext_power(m.inv().T, q) for m in mono]
        Ld = [ext_power(m, q) for m in mono]
        rk = L[0].shape[0]
        h0 = inv_dim(L)
        h2 = inv_dim(Ld)            # coinvariants of L = invariants of dual
        chi = -(len(mono)-2)*rk + sum(inv_dim([m]) for m in L)
        h1 = h0 + h2 - chi
        K = Kcorr.get(q, 0)
        b[q] += h0 + K; b[q+1] += h1; b[q+2] += h2
        print(name, "q=%d rk=%d inv_local=%s h0,h1,h2=%d,%d,%d K=%d" % (q, rk, [inv_dim([m]) for m in L], h0, h1, h2, K))
    print(name, "Betti:", b, "chi =", sum((-1)**k*x for k, x in enumerate(b)))
    return b

A1 = Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
MF = Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
assert A1*A2*MF == eye(4)
betti([A1, A2, MF], {}, "X")

C1 = Matrix([[-1,-1],[1,0]]); C2 = Matrix([[0,1],[-1,0]]); C0 = Matrix([[1,1],[0,1]])
assert C1*C2*C0 == eye(2)
def dsum(A, B):
    M = zeros(A.shape[0]+B.shape[0], A.shape[0]+B.shape[0])
    M[:A.shape[0], :A.shape[0]] = A; M[A.shape[0]:, A.shape[0]:] = B
    return M
T1, T2, T0 = dsum(A1, C1), dsum(A2, C2), dsum(MF, C0)
assert T1*T2*T0 == eye(6)
print("--- fibre product Z, with K^4 = 1 at the cusp (Kuhn fibre: H^* = invariants + one extra class in degree 4)")
betti([T1, T2, T0], {4: 1}, "Z")
print("--- elliptic surface S_orb check (rank 2), K=0")
betti([C1, C2, C0], {}, "E")
