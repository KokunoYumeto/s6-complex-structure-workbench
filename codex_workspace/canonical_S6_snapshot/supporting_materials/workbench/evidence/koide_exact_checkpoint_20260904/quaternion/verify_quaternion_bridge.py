#!/usr/bin/env python3
"""Exact arithmetic checks for the Koide quaternion bridge.

This script uses only fractions and integer arithmetic.  It checks the
multiplication table of the proposed order, its trace/norm formula, the
trace-zero coordinate lattice, the shell-to-unit identity on a sizeable
finite box, the order discriminant, and the Hilbert-symbol computations at
2 and 3.  The finiteness and spectral statements in the accompanying report
are proved there rather than inferred from finite computation.
"""

from fractions import Fraction as Q
from itertools import product, permutations

A = Q(18)
B = Q(-6)


def mul(x, y):
    """Multiply coordinates in (18,-6)_Q on the basis 1,I,J,K=IJ."""
    x0, x1, x2, x3 = x
    y0, y1, y2, y3 = y
    return (
        x0 * y0 + A * x1 * y1 + B * x2 * y2 - A * B * x3 * y3,
        x0 * y1 + x1 * y0 - B * x2 * y3 + B * x3 * y2,
        x0 * y2 + x2 * y0 + A * x1 * y3 - A * x3 * y1,
        x0 * y3 + x3 * y0 + x1 * y2 - x2 * y1,
    )


def conj(x):
    return (x[0], -x[1], -x[2], -x[3])


def trd(x):
    return 2 * x[0]


def nrd(x):
    return mul(x, conj(x))[0]


one = (Q(1), Q(0), Q(0), Q(0))
I = (Q(0), Q(1), Q(0), Q(0))
J = (Q(0), Q(0), Q(1), Q(0))
K = (Q(0), Q(0), Q(0), Q(1))
E = tuple((I[i] + J[i]) / 2 for i in range(4))
F0 = tuple((I[i] - J[i]) / 2 for i in range(4))
G = tuple(K[i] / 2 for i in range(4))
OBASIS = (one, E, F0, G)


def add(*xs):
    return tuple(sum((x[i] for x in xs), Q(0)) for i in range(4))


def scale(c, x):
    return tuple(Q(c) * z for z in x)


def ocoords(x):
    """Coordinates on 1,E,F0,G; valid over Q, integral exactly on O."""
    x0, xI, xJ, xK = x
    return (x0, xI + xJ, xI - xJ, 2 * xK)


def from_ocoords(r, s, t, u):
    return add(scale(r, one), scale(s, E), scale(t, F0), scale(u, G))


EXPECTED = {
    (1, 1): (3, 0, 0, 0),
    (1, 2): (6, 0, 0, -1),
    (2, 1): (6, 0, 0, 1),
    (2, 2): (3, 0, 0, 0),
    (3, 3): (27, 0, 0, 0),
    (1, 3): (0, 6, -3, 0),
    (3, 1): (0, -6, 3, 0),
    (2, 3): (0, 3, -6, 0),
    (3, 2): (0, -3, 6, 0),
}


def det_int(matrix):
    n = len(matrix)
    ans = 0
    for perm in permutations(range(n)):
        inv = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = 1
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        ans += (-1 if inv % 2 else 1) * term
    return ans


def hilbert_odd(alpha, u, beta, v, p):
    """Odd-p Hilbert symbol for  p^alpha*u, p^beta*v."""
    def legendre(x):
        x %= p
        value = pow(x, (p - 1) // 2, p)
        return -1 if value == p - 1 else value

    sign = -1 if (alpha * beta * ((p - 1) // 2)) % 2 else 1
    return sign * (legendre(u) ** beta) * (legendre(v) ** alpha)


def hilbert_two(alpha, u, beta, v):
    exponent = (
        ((u - 1) // 2) * ((v - 1) // 2)
        + alpha * ((v * v - 1) // 8)
        + beta * ((u * u - 1) // 8)
    )
    return -1 if exponent % 2 else 1


def main():
    assert mul(I, I) == scale(18, one)
    assert mul(J, J) == scale(-6, one)
    assert mul(I, J) == K
    assert mul(J, I) == scale(-1, K)
    assert mul(K, K) == scale(108, one)

    for i, j in product(range(4), repeat=2):
        coords = ocoords(mul(OBASIS[i], OBASIS[j]))
        assert all(c.denominator == 1 for c in coords)
        if (i, j) in EXPECTED:
            assert tuple(int(c) for c in coords) == EXPECTED[i, j]

    for r, s, t, u in product(range(-4, 5), repeat=4):
        x = from_ocoords(r, s, t, u)
        assert trd(x) == 2 * r
        assert nrd(x) == r * r - 3 * s * s - 12 * s * t - 3 * t * t - 27 * u * u
        assert ocoords(x) == (r, s, t, u)

    # Trace pairing discriminant on 1,E,F0,G.
    trace_pairing = [[trd(mul(x, y)) for y in OBASIS] for x in OBASIS]
    assert trace_pairing == [
        [2, 0, 0, 0],
        [0, 6, 12, 0],
        [0, 12, 6, 0],
        [0, 0, 0, 54],
    ]
    assert det_int(trace_pairing) == -11664

    checked = 0
    # A bounded replay sample; the identities themselves are polynomial and are
    # proved symbolically in the accompanying report.
    for a, q, n in product(range(-24, 25), range(-24, 25), range(-8, 9)):
        shell = a * a - 3 * q * q - 18 * n * n == -2
        parity = (a - q) % 2 == 0
        if shell:
            assert parity  # parity is automatic from the shell modulo 2
        if not parity:
            continue
        v = add(scale(Q(q, 2), I), scale(Q(a, 2), J), scale(Q(n, 2), K))
        gamma = add(scale(2, one), v)
        assert all(c.denominator == 1 for c in ocoords(gamma))
        assert trd(gamma) == 4
        assert nrd(gamma) == 4 + Q(3, 2) * (a * a - 3 * q * q - 18 * n * n)
        assert mul(v, v) == scale(-Q(3, 2) * (a * a - 3 * q * q - 18 * n * n), one)
        assert (nrd(gamma) == 1) == shell
        if shell:
            assert mul(gamma, add(scale(2, one), scale(-1, v))) == one
            # Frobenius norm in Q(sqrt(2)): store rational and sqrt(2)
            # coefficients separately and check the shell simplification
            # ||rho(gamma)||_F^2 = 14 + (7a+15 sqrt(2)n)^2/4.
            frob_rat = Q(8) + 9 * q * q + Q(37, 4) * a * a + Q(333, 2) * n * n
            frob_sqrt2 = Q(105, 2) * a * n
            simple_rat = Q(14) + Q(49, 4) * a * a + Q(225, 2) * n * n
            simple_sqrt2 = Q(105, 2) * a * n
            assert (frob_rat, frob_sqrt2) == (simple_rat, simple_sqrt2)
            checked += 1

    assert hilbert_two(1, 9, 1, -3) == -1
    assert hilbert_odd(2, 2, 1, -2, 3) == -1

    print("PASS")
    print(f"shell points checked in finite box: {checked}")
    print("trace-pairing determinant: -11664; reduced order discriminant: 108")
    print("Hilbert symbols: (18,-6)_2=-1, (18,-6)_3=-1")


if __name__ == "__main__":
    main()
