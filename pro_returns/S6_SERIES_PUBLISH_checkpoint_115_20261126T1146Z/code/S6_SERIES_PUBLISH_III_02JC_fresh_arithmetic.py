#!/usr/bin/env python3
"""Fresh integral checks for III 02JC, written before target-proof release.

Method: exterior minors, explicit integral image/kernel bases, and actual
normal-circle tubes in Mayer--Vietoris. No old cellular program is imported.
Only Python's standard library is used. All emitted text has LF endings.
"""
from fractions import Fraction
from itertools import combinations


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return list(map(list, zip(*a)))


def mul(a, b):
    return [[sum(x*y for x, y in zip(row, column))
             for column in zip(*b)] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def sub(a, b):
    return [[x-y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def columns(*vectors):
    return transpose(vectors)


def column(a, j):
    return [row[j] for row in a]


def mv(a, x):
    return [sum(u*v for u, v in zip(row, x)) for row in a]


def power(a, n):
    result = eye(len(a))
    for _ in range(n):
        result = mul(result, a)
    return result


def determinant(a):
    """Bareiss elimination with integer division, including row pivots."""
    b = [list(row) for row in a]
    n, sign, previous = len(b), 1, 1
    for k in range(n-1):
        pivot = next((i for i in range(k, n) if b[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            sign = -sign
        value = b[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = b[i][j]*value-b[i][k]*b[k][j]
                assert numerator % previous == 0
                b[i][j] = numerator // previous
        for i in range(k+1, n):
            b[i][k] = 0
        previous = value
    return sign*b[-1][-1]


def inverse(a):
    n = len(a)
    b = [[Fraction(x) for x in row+unit]
         for row, unit in zip(a, eye(n))]
    for j in range(n):
        k = next(i for i in range(j, n) if b[i][j])
        b[j], b[k] = b[k], b[j]
        pivot = b[j][j]
        b[j] = [x/pivot for x in b[j]]
        for i in range(n):
            if i != j:
                c = b[i][j]
                b[i] = [x-c*y for x, y in zip(b[i], b[j])]
    result = [row[n:] for row in b]
    assert mul(a, result) == eye(n)
    return [[int(x) if x.denominator == 1 else x for x in row]
            for row in result]


PAIRS = list(combinations(range(4), 2))


def wedge2(a):
    return [[a[i][k]*a[j][l]-a[i][l]*a[j][k]
             for k, l in PAIRS] for i, j in PAIRS]


def wedge(x, y):
    return [x[i]*y[j]-x[j]*y[i] for i, j in PAIRS]


def show(name, a):
    print(name + ':')
    for row in a:
        print('  ' + ' '.join(str(x) for x in row))


def check(name, predicate):
    assert predicate, name
    print('PASS ' + name)


A1 = [[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
A2 = [[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
v1, v2 = [1,2,-4,0], [-1,-3,3,0]
G = [[-2,1,0,1],[-6,0,-1,0],[0,-1,0,0],[-1,0,0,0]]
Gi = inverse(G)
V0, V1 = mul(mul(G, A1), Gi), mul(mul(G, A2), Gi)
M0 = inverse(mul(A1, A2))
U0, U1 = [0,2,2,1], [0,3,3,1]
D, A, B, E = [column(eye(4), j) for j in range(4)]
w0, w1 = mv(G, v1), mv(G, v2)

check('G determinant -1 and integral inverse',
      determinant(G) == -1 and all(isinstance(x, int) for row in Gi for x in row))
show('G inverse', Gi)
show('G A1 G^-1', V0)
show('G A2 G^-1', V1)
show('M0=(A1 A2)^-1', M0)
check('given cusp shear', M0 == [[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
check('finite orders', power(A1, 3) == eye(4) and power(A2, 4) == eye(4))
check('fixed affine vectors', mv(A1, v1) == v1 and mv(A2, v2) == v2)
check('exact signed vector transport', w0 == [-x for x in U0]
      and w1 == [x-y for x, y in zip(U1, D)])
print('transported vectors:', w0, w1)

E0, E1 = sub(wedge2(V0), eye(6)), sub(wedge2(V1), eye(6))
R2 = [r+s for r, s in zip(E0, E1)]
xi = [0,0,-6,1,0,0]
check('invariant exterior functional', mv(transpose(R2), xi) == [0]*12)

# Construct five image vectors by integer combinations of exterior columns.
s1, s2 = column(E0, 3), column(E1, 3)
rA = [2*x-y for x, y in zip(s1, column(E0, 5))]
rB = [-x-4*y-2*z for x, y, z in zip(column(E0, 4), s1, s2)]
rC = [x-3*y-6*z for x, y, z in zip(column(E1, 5), s1, s2)]
s5 = [x-y for x, y in zip(rB, rC)]
s6 = [x-y for x, y in zip(rA, s5)]
s36 = [x-y+z for x, y, z in zip(rC, s5, s6)]
image_basis = columns(s1, s2, s36, s5, s6)
expected = columns([1,0,0,0,0,0], [0,1,0,0,0,0],
                   [0,0,1,6,0,0], [0,0,0,0,1,0], [0,0,0,0,0,1])
check('five explicit integral exterior image generators', image_basis == expected)
with_s = [row+[int(i == 3)] for i, row in enumerate(image_basis)]
check('exterior image plus A wedge B is a unimodular basis', abs(determinant(with_s)) == 1)
show('exterior image basis', image_basis)

D1 = [r+s for r, s in zip(sub(V0, eye(4)), sub(V1, eye(4)))]
D3 = D1[:3]
pivot_cols = (1,2,6)
pivot = [[row[j] for j in pivot_cols] for row in D3]
check('D1 image is exactly Z<D,A,B>', D1[3] == [0]*8 and abs(determinant(pivot)) == 1)
ellD = [-x for x in mv(V1, D)] + [-x for x in D]
ellA = [-x for x in mv(V1, A)] + [-x for x in A]
J = columns(D+[0]*4, U0+[0]*4, [0]*4+U1, ellD, ellA)
R = [[1,0,0,0,-1,0,0,0],
     [0,0,0,1,0,0,0,0],
     [0,0,0,0,0,0,0,1],
     [0,0,0,0,-1,0,0,0],
     [0,0,0,0,0,-1,0,3]]
check('five columns lie in ker D1', mul(D1, J) == [[0]*5 for _ in range(4)])
check('integral kernel coordinate left inverse', mul(R, J) == eye(5))
remainder = sub(eye(8), mul(J, R))
S = mul([[row[j] for j in pivot_cols] for row in remainder], inverse(pivot))
check('integral kernel completeness I-JR=S D3', remainder == mul(S, D3))
show('kernel basis J', J)
show('kernel completeness factor S', S)
check('peripheral relations', ellD == [-1,0,0,0,-1,0,0,0]
      and ellA == [0,0,1,0,0,-1,0,0])

C = [[0,1,0,0],[0,0,-1,0],[-1,-1,1,1]]
check('honeycomb H2 mixed-cycle surjectivity over Z',
      determinant([row[:3] for row in C]) == 1)
check('mixed-cycle kernel g wedge w + u wedge delta', mv(C, [1,0,0,1]) == [0,0,0])
show('honeycomb mixed-cycle map', C)

def norm(v, m):
    result = [[0]*4 for _ in range(4)]
    for j in range(m):
        result = add(result, power(v, j))
    return result


N0, N1 = norm(V0, 3), norm(V1, 4)
show('finite norm N0', N0)
show('finite norm N1', N1)
check('norm columns used by tubes',
      mv(N0, A) == [-x for x in D]
      and mv(N1, A) == [-2*x for x in D]
      and mv(N0, E) == [3*x for x in U0]
      and mv(N1, E) == [4*x for x in U1])


def xi_pair(x, y):
    return sum(a*b for a, b in zip(xi, wedge(x, y)))


def tube(end, cut, omega):
    edge_vector = cut+[0]*4 if end == 0 else [0]*4+cut
    check('tube cut is a core cycle', mv(D1, edge_vector) == [0]*4)
    return [omega]+mv(R, edge_vector)[:3]


ta0 = tube(0, mv(N0, A), -xi_pair(A, w0))
tg0 = tube(0, w0, 0)
ta1 = tube(1, mv(N1, A), -xi_pair(A, w1))
tg1 = tube(1, w1, 0)
finite = columns(ta0, [-x for x in tg0], ta1, tg1)
expected_finite = [[2,0,-3,0],[-1,0,2,1],[0,1,0,0],[0,0,0,1]]
check('actual four finite tube columns', finite == expected_finite)
check('finite tube map determinant -1', determinant(finite) == -1)
finite_inverse = inverse(finite)
check('finite tube inverse integral', all(isinstance(x, int) for row in finite_inverse for x in row))
show('finite tube matrix', finite)
show('integral finite tube inverse', finite_inverse)

counts = [5,20,45,56,42,17,3]
chi = sum((-1)**i*c for i, c in enumerate(counts))
check('Euler characteristic from granted cells', chi == 2)
print('ALL FRESH INTEGRAL ARITHMETIC CHECKS PASSED')
