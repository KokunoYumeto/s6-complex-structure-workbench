#!/usr/bin/env python3
"""Post-exposure 02KR receiving-map audit, continuation seven.

No earlier code or saved result matrix is imported. The literal constants
below are the matrices printed in the receiving proof. Determinantal
divisors are computed by enumerating minors using fraction-free integer
elimination, separately from the frozen fresh adjugate/Bezout program.
This is arithmetic review, not a new blind derivation or a geometric proof.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd
import sympy as sp


def determinant(rows):
    """Bareiss determinant, with exact divisions and pivot row swaps."""
    a = [list(map(int, r)) for r in rows]
    n = len(a)
    if not n:
        return 1
    sign, denominator = 1, 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = p * a[i][j] - a[i][k] * a[k][j]
                assert numerator % denominator == 0
                a[i][j] = numerator // denominator
            a[i][k] = 0
        denominator = p
    return sign * a[-1][-1]


def divisors(matrix):
    rows = matrix.tolist()
    ans = []
    for size in range(1, min(matrix.shape) + 1):
        d = 0
        for ri in combinations(range(matrix.rows), size):
            for ci in combinations(range(matrix.cols), size):
                d = gcd(d, determinant([[rows[i][j] for j in ci] for i in ri]))
        ans.append(d)
    return ans


def gaussian_inverse(matrix):
    n = matrix.rows
    a = [[Fraction(int(matrix[i, j])) for j in range(n)]
         + [Fraction(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if a[i][j])
        a[j], a[p] = a[p], a[j]
        factor = a[j][j]
        a[j] = [x / factor for x in a[j]]
        for i in range(n):
            if i != j:
                factor = a[i][j]
                a[i] = [x - factor * y for x, y in zip(a[i], a[j])]
    assert all(a[i][j] == (i == j) for i in range(n) for j in range(n))
    assert all(x.denominator == 1 for row in a for x in row[n:])
    return sp.Matrix([[int(x) for x in row[n:]] for row in a])


I4, I6 = sp.eye(4), sp.eye(6)
e = [I4[:, j] for j in range(4)]
f = [I6[:, j] for j in range(6)]
wedges = list(combinations(range(4), 2))


def exterior(t):
    return sp.Matrix([[t[i, k] * t[j, l] - t[i, l] * t[j, k]
                       for k, l in wedges] for i, j in wedges])


def sparse(rows, cols, mapping):
    mat = sp.zeros(rows, cols)
    for one_based, vals in mapping.items():
        mat[one_based - 1, :] = sp.Matrix([vals])
    return mat


parameters = [
    (1, 0, 0, 0, 0), (1, 0, 0, 0, 1), (1, 0, 0, 0, -1),
    (2, 0, 0, 1, 0), (4, 2, 0, 1, 0), (6, 2, 4, 1, 0),
    (6, 1, 2, 4, 0), (15, 3, 6, 5, 0), (18, 1, 5, 12, 0),
    (12, 4, 8, 3, 6), (12, 3, 6, 4, -6), (30, 5, 10, 6, 15),
    (8, 2, -4, 3, 1), (8, 2, -4, 3, -1), (21, -4, 9, 2, -7),
]

for kind, p in (('II', 4), ('IV', 12)):
    if kind == 'II':
        star = sp.Matrix([[-1, -3, 0, 1], [0, -1, 0, 1],
                          [-4, -8, 1, 3], [0, 0, 0, 1]])
        finite = sp.Matrix([[1, 1, 0, 0], [-1, 0, 0, 0],
                            [0, 0, 1, 0], [0, 0, 0, 1]])
        fixed_star = sp.Matrix.hstack(e[2], sp.Matrix([-1, 2, 0, 4]))
        fixed_finite = sp.Matrix.hstack(e[2], e[3])
        spec = sp.Matrix([[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]])
        basis = sp.Matrix.hstack(f[0], f[5], f[1], f[2], f[3], f[4])
        c = sparse(12, 3, {6: [-3, 0, 1], 8: [-8, 0, 3], 9: [-2, -1, 1]})
        z = sparse(18, 5, {9: [3, 0, -2, 0, 0], 10: [3, -1, 0, 1, 0],
                           11: [-2, 0, 1, 0, 0], 12: [-4, 2, -3, -3, 0],
                           15: [4, 0, -2, 0, -1]})
        multiplicity, expected_det = 1, -1
    else:
        star = sp.Matrix([[-1, -1, 0, -1], [0, -1, 0, 1],
                          [-12, -24, 1, 3], [0, 0, 0, 1]])
        finite = sp.Matrix([[-1, 1, 0, -2], [-1, 0, 0, 0],
                            [-24, 0, 1, -16], [0, 0, 0, 1]])
        fixed_star = sp.Matrix.hstack(e[2], sp.Matrix([-3, 2, 0, 4]))
        fixed_finite = sp.Matrix.hstack(e[2], sp.Matrix([-2, 2, 0, 3]))
        spec = sp.Matrix([[3, 0, -2, 0, -2, 0], [0, 0, -8, 0, -8, 1]])
        basis = sp.Matrix.hstack(f[0] + f[2] + 8 * f[5], f[5],
                                 sp.Matrix([2, 0, 3, 0, 0, 24]),
                                 sp.Matrix([0, 0, -1, 0, 1, 0]), f[1], f[3])
        c = sparse(12, 3, {5: [52, 88, -8], 6: [27, 34, -5],
                            8: [-72, -120, 11], 9: [-126, -189, 21],
                            12: [96, 144, -16]})
        z = sparse(18, 5, {8: [-43, 1, 20, 1, 30], 9: [3, 0, -2, 0, -2],
                           10: [43, -1, -20, -1, -30], 11: [2, 0, -1, 0, -2],
                           12: [-72, 2, 27, 1, 42], 15: [-4, 0, 2, 0, 3]})
        multiplicity, expected_det = 3, 1
    cusp = sp.Matrix([[0, 1, 0, -1], [-1, 2, 0, -1],
                      [-p, p, 1, 1-p], [0, 0, 0, 1]])
    omega = sp.Matrix([[p, 0, 0, 0, 0, -1]])
    assert star * finite * cusp == I4
    assert all(omega * exterior(t) == omega for t in (star, finite, cusp))
    assert divisors(finite - I4) == [1, 1, 0, 0]
    assert divisors(exterior(finite) - I6) == [1, 1, 1, 1, 0, 0]
    assert spec * basis == I6[:2, :]
    assert abs(determinant(basis.tolist())) == 1
    assert spec * (exterior(finite) - I6) == sp.zeros(2, 6)
    assert (p // multiplicity) * spec[:1, :] - spec[1:, :] == omega
    assert (finite - I4) * fixed_finite == sp.zeros(4, 2)
    assert gcd(*(determinant(fixed_finite.extract(rr, [0, 1]).tolist())
                 for rr in combinations(range(4), 2))) == 1
    h = sp.Matrix.hstack(sp.Matrix([1, 1, p, 0]), e[1], e[2], e[1] + e[3])
    hn = I4.copy(); hn[0, 1] = hn[2, 3] = 1
    assert determinant(h.tolist()) == 1 and cusp * h == h * hn
    assert gaussian_inverse(h) * h == I4

    def inclusion(i, mat):
        if i == 3:
            return -sp.Matrix.vstack(star * finite * mat, finite * mat, mat)
        blocks = [sp.zeros(4, mat.cols) for _ in range(3)]
        blocks[i] = mat
        return sp.Matrix.vstack(*blocks)

    d = sp.Matrix.hstack(sp.zeros(4), star - I4, finite - I4)
    b = sp.Matrix.hstack(inclusion(1, fixed_star), inclusion(2, fixed_finite),
                         inclusion(3, sp.Matrix.hstack(h[:, 0], e[2])))
    k = sp.Matrix.hstack(b, inclusion(0, sp.Matrix.hstack(e[0], e[1], e[3])))
    whole = sp.Matrix.hstack(k, c)
    assert determinant(whole.tolist()) == expected_det
    inv = gaussian_inverse(whole)
    ell = inv[:9, :]
    assert inv * whole == sp.eye(12) and whole * inv == sp.eye(12)
    assert d[:3, :] * c == sp.eye(3) and d * k == sp.zeros(4, 9)
    assert ell * k == sp.eye(9)
    project = sp.eye(12) - c * d[:3, :]
    assert k * ell * project == project
    graph = ell * inclusion(0, I4)
    assert graph[:, 2] == sp.Matrix([-1, 0, -1, 0, 0, -1, 0, 0, 0])
    assert graph[6:, :] == sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    b2 = sp.Matrix.hstack(sp.zeros(6), exterior(star) - I6, exterior(finite) - I6)
    ff = sp.Matrix.hstack(f[0] + p*f[5], f[1], f[2], f[3], f[4])
    assert b2 * z == ff
    assert abs(determinant(sp.Matrix.hstack(-f[5], ff).tolist())) == 1
    print(kind, 'literal finite specialization, all boundary Smith divisors, C/Z, complete graph inverse: PASS')

    m, a, bb, cc, n = sp.symbols('m a b c n', integer=True)
    r = sp.Matrix([[-p*bb, p*a, n, -cc, 0], [m, 0, 0, 0, a],
                   [0, m, 0, 0, bb], [0, 0, 0, m, n]])
    q = sp.Matrix([-a, -bb, -cc, -n, m])
    assert r*q == sp.zeros(4, 1)
    cof = sp.Matrix([(-1)**j * r[:, [i for i in range(5) if i != j]].det()
                     for j in range(5)])
    assert sp.simplify(cof - m*m*n*q) == sp.zeros(5, 1)
    full = sp.zeros(10, 11)
    full[1:7, :6] = sp.eye(6)
    full[0, 6:] = r[:1, :]
    full[1:, 6:10] = m*graph
    full[1:, 10] = graph*sp.Matrix([a, bb, cc, n])
    ordered = full[[1, 2, 3, 4, 5, 6, 0, 7, 8, 9], :]
    inverse_add = sp.eye(11); inverse_add[:6, 6:] = -ordered[:6, 6:]
    back_add = sp.eye(11); back_add[:6, 6:] = ordered[:6, 6:]
    assert inverse_add*back_add == sp.eye(11)
    assert ordered*inverse_add == sp.diag(sp.eye(6), r)
    print(kind, 'symbolic full transfer reduction and signed maximal-minor vector: PASS')
    for vals in parameters:
        mm, aa, bval, cval, nn = vals
        assert gcd(*vals) == 1
        value = r.subs(dict(zip((m, a, bb, cc, n), vals)))
        t = gcd(mm, nn, aa, bval)*gcd(mm, nn, p, cval)
        assert divisors(value) == [1, t, mm*t, mm*mm*abs(nn)]
    print(kind, len(parameters), 'determinantal-divisor specializations, including n=0 and n=+/-1: PASS')

g4 = sp.Matrix([[-n, 0, 0, 0], [m, 0, 0, -1],
                [0, 1, 0, -1], [0, 0, 1, -1]])
assert g4.det() == n
assert g4.subs(n, 0)*sp.Matrix([1, m, m, m]) == sp.zeros(4, 1)
assert g4[1:, 1:].det() == -1
print('Entire reduced H1 normal block: determinant n, unit minor -1, primitive zero-n kernel: PASS')
print('PASS: receiving constants and transfers checked; these computations carry no independent geometric closure credit.')
