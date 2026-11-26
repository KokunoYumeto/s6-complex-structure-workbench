#!/usr/bin/env python3
"""New LH integer maps. No target or historical program is imported."""
from itertools import combinations
from math import gcd
from sympy import Matrix, ZZ, eye, zeros
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

PAIRS = list(combinations(range(4), 2))


def integral(A):
    A = Matrix(A)
    assert all(x.q == 1 for x in A), A
    return A


def rows(A):
    return [[int(x) for x in row] for row in integral(A).tolist()]


def bezout(a, b):
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0-q*r1
        s0, s1 = s1, s0-q*s1
        t0, t1 = t1, t0-q*t1
    if r0 < 0:
        r0, s0, t0 = -r0, -s0, -t0
    assert a*s0+b*t0 == r0
    return r0, s0, t0


def bezout_vector(values):
    common, coeffs = 0, []
    for x in values:
        common, u, v = bezout(common, int(x))
        coeffs = [u*c for c in coeffs] + [v]
    assert sum(int(x)*c for x, c in zip(values, coeffs)) == common
    return common, Matrix(coeffs)


def exterior(A):
    return Matrix([[A.extract(I, J).det() for J in PAIRS] for I in PAIRS])


def wedge(x, y):
    return Matrix([x[i]*y[j]-x[j]*y[i] for i, j in PAIRS])


def smith(A):
    """Return verified integer equivalences D=U A V and both inverses."""
    A = integral(A)
    if not A.rows or not A.cols:
        return A, eye(A.rows), eye(A.cols), eye(A.rows), eye(A.cols), 0
    d, u, v = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    D, U, V = d.to_Matrix(), u.to_Matrix(), v.to_Matrix()
    assert U*A*V == D
    Ui, Vi = integral(U.inv()), integral(V.inv())
    assert U*Ui == eye(U.rows) and V*Vi == eye(V.rows)
    rank = sum(bool(D[i, i]) for i in range(min(D.shape)))
    ds = [abs(int(D[i, i])) for i in range(rank)]
    assert all(y % x == 0 for x, y in zip(ds, ds[1:]))
    return D, U, V, Ui, Vi, rank


def kernel(A):
    D, U, V, Ui, Vi, rank = smith(A)
    K, L = V[:, rank:], Vi[rank:, :]
    assert A*K == zeros(A.rows, K.cols) and L*K == eye(K.cols)
    return K, L


def saturated_image(A):
    D, U, V, Ui, Vi, rank = smith(A)
    B, L = Ui[:, :rank], U[:rank, :]
    Q, section = U[rank:, :], Ui[:, rank:]
    assert Q*A == zeros(Q.rows, A.cols)
    assert L*B == eye(rank) and Q*section == eye(Q.rows)
    assert B*L+section*Q == eye(A.rows)
    return B, L, Q, section


def image_basis(A):
    H = hermite_normal_form(integral(A))
    D, U, V, Ui, Vi, rank = smith(A)
    Z = U*H
    assert Z[rank:, :] == zeros(A.rows-rank, H.cols)
    pre = V[:, :rank]*Matrix.diag(*(1/D[i, i] for i in range(rank)))*Z[:rank, :]
    pre = integral(pre)
    assert A*pre == H
    return H, pre


def right_inverse(A):
    D, U, V, Ui, Vi, rank = smith(A)
    assert rank == A.rows and all(abs(D[i, i]) == 1 for i in range(rank))
    R = V[:, :rank]*Matrix.diag(*(1/D[i, i] for i in range(rank)))*U
    R = integral(R)
    assert A*R == eye(A.rows)
    return R


def invariants(A):
    D, U, V, Ui, Vi, rank = smith(A)
    return A.rows-rank, [abs(int(D[i, i])) for i in range(rank) if abs(D[i, i]) > 1]


def cycles(p):
    unseen, ans = set(range(len(p))), []
    while unseen:
        x, orbit = min(unseen), []
        while x in unseen:
            unseen.remove(x)
            orbit.append(x)
            x = p[x]
        assert x == orbit[0]
        ans.append(orbit)
    return ans


def permutation_power(p, k):
    out = [None]*len(p)
    for orbit in cycles(p):
        for j, x in enumerate(orbit):
            out[x] = orbit[(j+k) % len(orbit)]
    return out


def component_data(kind):
    """The admitted component graph and section permutation, not a target table."""
    if kind.startswith("I") and kind[1:].isdigit():
        n = int(kind[1:])
        return list(range(1, n))+[0], [1]*n
    if kind == "II":
        return [0], [1]
    if kind == "III":
        return [1, 0], [1, 1]
    if kind == "IV":
        return [1, 2, 0], [1, 1, 1]
    if kind == "III*":
        return [0, 4, 5, 6, 1, 2, 3, 7], [4, 3, 2, 1, 3, 2, 1, 2]
    if kind == "IV*":
        return [0, 3, 4, 5, 6, 1, 2], [3, 2, 1, 2, 1, 2, 1]
    assert kind.startswith("I") and kind.endswith("*")
    n = int(kind[1:-1])
    assert n % 2 == 1
    return [2, 3, 1, 0]+list(reversed(range(4, n+5))), [1]*4+[2]*(n+1)
