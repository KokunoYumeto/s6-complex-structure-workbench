"""Exact Fraction verification of the derived Albert flag-chart formulas.

This is an independent coefficient check, not a replacement for STAGED.tex.
No external libraries and no file reads/writes are used by this script.
"""

from fractions import Fraction as F
from math import factorial


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def scale(a, x):
    return tuple(a * b for b in x)


def conj(x):
    return (x[0],) + tuple(-a for a in x[1:])


def mul(x, y):
    if len(x) == 1:
        return (x[0] * y[0],)
    h = len(x) // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return add(mul(a, c), neg(mul(conj(d), b))) + add(
        mul(d, a), mul(b, conj(c))
    )


O0 = (F(0),) * 8


def scalar(a):
    return (F(a),) + (F(0),) * 7


def to_matrix(x):
    q1, q2, q3 = x[3:11], x[11:19], x[19:27]
    return [
        [scalar(x[0]), q3, conj(q2)],
        [conj(q3), scalar(x[1]), q1],
        [q2, conj(q1), scalar(x[2])],
    ]


def from_matrix(x):
    assert all(x[i][i][j] == 0 for i in range(3) for j in range(1, 8))
    assert all(x[i][j] == conj(x[j][i]) for i in range(3) for j in range(3))
    return (x[0][0][0], x[1][1][0], x[2][2][0]) + x[1][2] + x[2][0] + x[0][1]


def jordan(x, y):
    a, b = to_matrix(x), to_matrix(y)
    c = []
    for i in range(3):
        row = []
        for j in range(3):
            value = O0
            for k in range(3):
                value = add(value, add(mul(a[i][k], b[k][j]), mul(b[i][k], a[k][j])))
            row.append(scale(F(1, 2), value))
        c.append(row)
    return from_matrix(c)


V0 = (F(0),) * 27
BASIS = [tuple(F(i == j) for i in range(27)) for j in range(27)]
UNIT = add(add(BASIS[0], BASIS[1]), BASIS[2])
WEIGHTS = (2, -2, 0) + (-1,) * 8 + (1,) * 8 + (0,) * 8
METRIC = (1,) * 3 + (2,) * 24


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matvec(a, v):
    return tuple(sum(x * y for x, y in zip(row, v)) for row in a)


def matadd(a, b):
    return [list(add(x, y)) for x, y in zip(a, b)]


def matscale(t, a):
    return [list(scale(t, row)) for row in a]


def comm(a, b):
    return matadd(matmul(a, b), matscale(-1, matmul(b, a)))


def inner(i, octonion):
    return (F(0),) * (3 + 8 * i) + octonion + (F(0),) * (16 - 8 * i)


def nu(i, octonion):
    u = inner(i, octonion)
    columns = [jordan(u, e) for e in BASIS]
    left = list(zip(*columns))
    rho = (1, 1, 2)[i]
    ans = [
        [F(1, 2) * (1 + F(WEIGHTS[r] - WEIGHTS[c], rho)) * left[r][c] for c in range(27)]
        for r in range(27)
    ]
    assert all((WEIGHTS[r] - WEIGHTS[c] - rho) * ans[r][c] == 0 for r in range(27) for c in range(27))
    assert matvec(ans, UNIT) == scale(F(1, 2), u)
    return ans


def adjoint(a):
    return [[a[j][i] * F(METRIC[j], METRIC[i]) for j in range(27)] for i in range(27)]


def exponential_apply(z, v):
    ans = v
    term = v
    for k in range(1, 6):
        term = matvec(z, term)
        if k == 5:
            assert term == V0
        else:
            ans = add(ans, scale(F(1, factorial(k)), term))
    return ans


def check(q):
    roots = [nu(i, q[i]) for i in range(3)]
    z = matadd(matadd(roots[0], roots[1]), roots[2])
    zstar = adjoint(z)
    # Check the full endomorphism nilpotence, not only the two used vectors.
    for basis in BASIS:
        v = basis
        for _ in range(5):
            v = matvec(z, v)
        assert v == V0
    a0 = exponential_apply(z, BASIS[1])
    b0 = exponential_apply(matscale(-1, zstar), BASIS[0])
    ta, tb = sum(a0[:3]), sum(b0[:3])
    assert ta > 0 and tb > 0
    a, b = scale(1 / ta, a0), scale(1 / tb, b0)
    assert jordan(a, a) == a
    assert jordan(b, b) == b
    assert jordan(a, b) == V0
    assert a0[1] == b0[0] == 1
    q1 = scale(2 / a[1], a[3:11])
    q2 = scale(-2 / b[0], b[11:19])
    q3 = add(scale(2 / a[1], a[19:27]), scale(F(-1, 4), conj(mul(q1, q2))))
    assert (q1, q2, q3) == q
    bracket = comm(roots[0], roots[1])
    assert bracket == nu(2, scale(F(-1, 2), conj(mul(q[0], q[1]))))
    print('PASS: complete operators, fifth power, positive traces, primitive orthogonal idempotents, exact inverse, bracket; traces =', ta, tb)


if __name__ == '__main__':
    for raw in [
        ((1, 0, 0, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 0, 0, 0), (3, 0, 0, 0, 0, 0, 0, 0)),
        ((0, 1, 2, 0, 1, 0, -1, 1), (1, 0, -1, 2, 0, 1, 1, 0), (-1, 2, 1, 0, -2, 1, 0, 1)),
        ((1, -2, 3, -1, 2, 0, 1, -1), (2, 1, 0, -2, 1, 3, -1, 2), (0, -1, 2, 3, 1, -2, 1, -3)),
    ]:
        check(tuple(tuple(F(x) for x in v) for v in raw))
