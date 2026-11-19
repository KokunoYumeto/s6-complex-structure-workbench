# Intake of S6_06_BLIND cp36 (Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026).
# An independent implementation of the two all-fan algorithms as stated in the results register:
# P3K.71 (the selected-cusp E7 source loop) and P3K.73 (the whole-zero I_1 scalar families and the original (3,4)
# family). Only the canonical representatives C = [[p,-r],[q,s]], p,r > 0, ps+rq = 1, and the vertical seeds T_n are
# used, so the run's "identical-fan maps" are not needed. Exact arithmetic; every division is checked to be exact.
# Usage: python -I -B fan_algorithms.py
from fractions import Fraction as Fr

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def inv(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert det in (1, -1)
    return [[A[1][1] * det, -A[0][1] * det], [-A[1][0] * det, A[0][0] * det]]
Q = {0: [[1, -1], [0, 1]], 1: [[1, 0], [-1, 1]]}

def factor(C):
    """C = T_n Q_{i_1} ... Q_{i_k} by the Euclidean subtraction on the first row (p, -r)."""
    word = []
    P = [row[:] for row in C]
    while not (P[0][0] == 1 and P[0][1] == 0):
        p, r = P[0][0], -P[0][1]
        assert p > 0 and r > 0
        if p > r:
            P = mul(P, inv(Q[1])); word.append(1)
        else:
            P = mul(P, inv(Q[0])); word.append(0)
    assert P[0] == [1, 0] and P[1][1] == 1
    return P[1][0], word[::-1]

def exact(x):
    assert x.denominator == 1, x
    return x

def run(C, kind, J=None, H=None, chi=None):
    n, word = factor(C)
    if kind == 'E7':
        V = [[18 * n * (n - 1), 6 - 12 * n, 12 * n - 6], [6 - 12 * n, 0, 0], [12 * n - 6, 0, 0]]
        d0 = [-12 - 18 * n * (n - 1), 12 * n - 12, -12 * n]
        S = Fr(-1 - 3 * n * (n - 1))
    else:
        J, H, chi = Fr(J), Fr(H), Fr(chi)
        V = [[2 * J - 6 * H + 6 * J * n * (n - 1), 2 * J * (1 - 2 * n), 2 * J * (2 * n - 1)],
             [2 * J * (1 - 2 * n), 2 * J, 0], [2 * J * (2 * n - 1), 0, 2 * J]]
        d0 = [2 * J + 6 * H - 24 * chi - 6 * J * n * (n - 1), 2 * J * (2 * n - 1), 2 * J * (1 - 2 * n)]
        S = H / 2 - chi - J * n * (n - 1) / 2
    V = [[Fr(x) for x in row] for row in V]; delta = [Fr(x) for x in d0]
    P = [[1, 0], [n, 1]]
    for i in word:
        a, b = V[i][i], delta[i]
        P = mul(P, Q[i])
        Pi = inv(P)
        if kind == 'E7':
            e1 = [[Pi[0][0] * P[0][0], Pi[0][0] * P[0][1]], [Pi[1][0] * P[0][0], Pi[1][0] * P[0][1]]]
            Bm = [[-6 * e1[j][k] for k in range(2)] for j in range(2)]
        else:
            e2 = [[Pi[0][1] * P[1][0], Pi[0][1] * P[1][1]], [Pi[1][1] * P[1][0], Pi[1][1] * P[1][1]]]
            Bm = [[2 * J * e2[j][k] for k in range(2)] for j in range(2)]
        l = [Bm[1][1] - Bm[1][0], Bm[0][0] - Bm[0][1], Bm[1][1]]
        x, y = Pi[0][1], Pi[1][1]
        w = [x, y, -x - y]
        d = [-x - 2 * y, -2 * x - y, x - y]
        assert all(wj != 0 for wj in w)
        if kind == 'E7':
            I = [-3 * w[j] + d[j] * (l[j] + 3) for j in range(3)]
            W = [-3 * w[j] - d[j] * (l[j] + 3) for j in range(3)]
        else:
            I = [J * w[j] + d[j] * (l[j] - J) for j in range(3)]
            W = [J * w[j] - d[j] * (l[j] - J) for j in range(3)]
        c = w[2] ** 2 * a - w[2] * I[2]
        e = w[2] * (2 * a - b) - W[2]
        V = [[exact(Fr(I[j], 1) / w[j] * (1 if j == k else 0) + Fr(c) / (w[j] * w[k])) for k in range(3)] for j in range(3)]
        delta = [exact(Fr(W[j] + e) / w[j]) for j in range(3)]
        S = S + (b - a) / (2 if kind == 'E7' else 4)
    return int(exact(S)) % 28, n, word

print('P3K.71 example P=[[2,-1],[-1,1]] (claimed class 1):', run([[2, -1], [-1, 1]], 'E7'))
orig = dict(J=2, H=Fr(1, 3), chi=Fr(1, 6))       # the original (3,4) family, K = L = 1, shorter loop
print('P3K.73 original family, P=[[1,-2],[0,1]] (claimed class 3):', run([[1, -2], [0, 1]], 'S', **orig))
print('P3K.73 original family, vertical T_2 (claimed 26):', run([[1, 0], [2, 1]], 'S', **orig) if False else
      (int(Fr(1, 3) / 2 - Fr(1, 6) - 2 * 2 * 1 / 2) % 28))
img_o, img_e, ok = set(), set(), True
for p in range(1, 13):
    for r in range(1, 13):
        for q in range(-12, 13):
            if (1 - r * q) % p == 0:
                s = (1 - r * q) // p
                C = [[p, -r], [q, s]]
                try:
                    img_o.add(run(C, 'S', **orig)[0]); img_e.add(run(C, 'E7')[0])
                except AssertionError:
                    ok = False
for n in range(-14, 15):
    img_o.add(int(Fr(1, 3) / 2 - Fr(1, 6) - n * (n - 1)) % 28); img_e.add((-1 - 3 * n * (n - 1)) % 28)
print('exact integrality on every fan tried:', ok)
print('original family: classes over the fans tried:', len(img_o), sorted(img_o))
print('E7 selected-cusp loop: classes over the fans tried:', len(img_e), sorted(img_e))
print('E7 vertical image {-1-3n(n-1)}:', sorted({(-1 - 3 * n * (n - 1)) % 28 for n in range(56)}))
print('period of -7-24j(j+1) mod 28:', min(t for t in range(1, 29) if all((-7 - 24 * j * (j + 1)) % 28 == (-7 - 24 * (j + t) * (j + t + 1)) % 28 for j in range(60))))
print('6a = b in Z/28: b odd has no solution', all((6 * a) % 28 != b for a in range(28) for b in range(1, 28, 2)),
      '; b = 2r has a in {5r, 5r+14}', all({a for a in range(28) if (6 * a) % 28 == (2 * r) % 28} == {(5 * r) % 28, (5 * r + 14) % 28} for r in range(14)))
print('P3K.69 flop rule 7A on 3,6,9,14 and on the OS47 class 4:', [(7 * x) % 28 for x in (3, 6, 9, 14, 4)])

# P3K.93 closed form on primitive vectors (x, y): I_a = 1-a-3(a-1)(S-1)-(2a+1)(S-1)(S-3)/4 mod 28, S = x^2+xy+y^2
from math import gcd
for a in (1, 2):
    img = set()
    for x in range(-40, 41):
        for y in range(-40, 41):
            if gcd(x, y) == 1:
                S = x * x + x * y + y * y
                v = Fr(1 - a - 3 * (a - 1) * (S - 1)) - Fr((2 * a + 1) * (S - 1) * (S - 3), 4)
                img.add(int(exact(v)) % 28)
    print('P3K.93 image for a=%d:' % a, sorted(img))
