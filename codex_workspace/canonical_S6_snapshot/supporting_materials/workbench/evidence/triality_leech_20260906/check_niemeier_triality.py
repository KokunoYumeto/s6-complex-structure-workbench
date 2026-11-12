"""Exact checks of the displayed rank-24 map and exterior-algebra tensor."""
import itertools
import json
import sympy as s


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


def iszero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)


sqrt = s.sqrt
L = s.zeros(24, 28)
for a in range(8):
    i, p = divmod(a, 2)
    for j in range(3):
        row = 8*j+a
        L[row, 6*i+p+2*j] += 1
        for h in range(3):
            L[row, 6*i+p+2*h] -= s.Rational(1, 3)
        if a < 4:
            for k in range(6):
                L[row, 6*a+k] += (-1)**k/sqrt(18)
        else:
            L[row, 24+a-4] += 1/sqrt(3)
P = s.diag(*([s.eye(6)-s.ones(6)/6]*4+[s.eye(4)]))
check(iszero(L*L.T-s.eye(24)), 'L L^T')
check(iszero(L.T*L-P), 'L^T L = constraint projector')
r = s.zeros(28)
for i in range(4):
    for j in range(6):
        r[6*i+(j+2)%6, 6*i+j] = 1
for k in range(4):
    r[24+k, 24+k] = 1
c = s.zeros(24)
for j in range(3):
    for a in range(8):
        c[8*((j+1)%3)+a, 8*j+a] = 1
check(iszero(L*r-c*L), 'C3 intertwining')
check(r**3 == s.eye(28), 'residue order')

binary = []
for u in itertools.product(range(2), repeat=4):
    if sum(u)%2 == 0:
        binary.append((u, ((u[1]+u[3])%2, (u[2]+u[3])%2)))
glue = set()
for u, y in binary:
    for a, b in itertools.product(range(3), repeat=2):
        z = (a+b, a+2*b, a, b)
        glue.add((tuple((3*u[i]+2*z[i])%6 for i in range(4)), y))
check(len(glue) == 72, 'glue order')
v = s.Matrix([1, 0, 0, 0])
sp = s.ones(4, 1)/2
sm = s.Matrix([-1, 1, 1, 1])/2
drep = {(0,0): s.zeros(4,1), (1,0):v, (0,1):sp, (1,1):sm}
lam = s.Matrix([5,-1,-1,-1,-1,-1])/6
for k, y in glue:
    X = s.Matrix.vstack(*[ki*lam for ki in k], drep[y])
    check(iszero(L.T*L*X-X), 'glue round trip')
    delta = r*X-X
    check(all(x.is_Integer for x in delta), 'residue glue difference integral')
    check(all(sum(delta[6*i:6*i+6]) == 0 for i in range(4)), 'augmentation')
    check(all(x == 0 for x in delta[24:]), 'D fixed')

# Exterior basis e_I, in bit-mask order.
dim = 16
a_ops, b_ops = [], []
for i in range(4):
    a, b = s.zeros(dim), s.zeros(dim)
    for I in range(dim):
        sign = (-1)**((I & ((1<<i)-1)).bit_count())
        if not I & (1<<i):
            a[I | (1<<i), I] = sign
        else:
            b[I ^ (1<<i), I] = sign
    a_ops.append(a)
    b_ops.append(b)
C = [a+b for a,b in zip(a_ops,b_ops)]
D = [s.I*(b-a) for a,b in zip(a_ops,b_ops)]
cliff = [op for pair in zip(C,D) for op in pair]
for i in range(8):
    for j in range(8):
        check(cliff[i]*cliff[j]+cliff[j]*cliff[i]
              == 2*int(i == j)*s.eye(dim), 'Clifford relation')
B = s.zeros(dim)
for I in range(dim):
    k = I.bit_count()
    indices = [i for i in range(4) if I & (1<<i)]
    concat_sign = (-1)**sum(i-r for r,i in enumerate(indices))
    B[I, 15^I] = (-1)**(k*(k-1)//2)*concat_sign
check(B == B.T and B*B == s.eye(16), 'B symmetric involution')
for op in cliff:
    check(op.T*B == B*op, 'Clifford B-adjoint')
    check(B*op.conjugate() == op*B, 'real structure compatibility')
K = [C[i]*D[i]/2 for i in range(4)]
nonzero = 0
for i, direction, I, J in itertools.product(range(4), (1,-1), range(16), range(16)):
    if I.bit_count()%2 or J.bit_count()%2 != 1:
        continue
    op = sqrt(2)*(a_ops[i] if direction == 1 else b_ops[i])
    coefficient = (op.T*B)[I,J]
    total_weight = [s.Rational(int(bool(I & (1<<h)))+int(bool(J & (1<<h)))-1)
                    + direction*int(i == h) for h in range(4)]
    if coefficient:
        nonzero += 1
        check(all(x == 0 for x in total_weight), 'zero total weight')
        check(coefficient in (sqrt(2), -sqrt(2)), 'exact coupling factor')
    else:
        check(any(x != 0 for x in total_weight), 'no missing zero-weight coupling')
check(nonzero == 32, '32 couplings')

print(json.dumps({'status':'PASS', 'map_shape':[24,28],
                  'glue_classes_round_tripped':len(glue),
                  'clifford_anticommutators':64,
                  'nonzero_weight_couplings':nonzero,
                  'weight_coupling_coefficients':['sqrt(2)','-sqrt(2)']}, indent=2))
