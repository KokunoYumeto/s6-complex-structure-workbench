"""Independent integral Seifert-form recurrence for the positive OS49 trace.

No earlier program is imported. Symbolic block identities establish all k;
small dense matrices independently check the recurrence's indexing and signs.
This computes the specified cochain. Geometry is recorded separately.
"""
import sympy as s
import sys
from sympy.polys.matrices import DomainMatrix
sys.stdout.reconfigure(line_buffering=True)

def det(a, b):
    return a[0]*b[1] - a[1]*b[0]

e1, e2 = s.Matrix([1, 0]), s.Matrix([0, 1])
A = s.Matrix([[0, -1], [1, -1]])
J = s.Matrix([[0, 1], [-1, 0]])
T = lambda v: s.eye(2) + v*v.T*J
gA = s.Matrix([0, -1])
v, ell = [], []
t = s.zeros(2, 1)
for j in range(3):
    next_t = t + A**j*gA
    vv = [A**j*e2, A**j*e1, A**(j+1)*e1, A**(j+1)*e1]
    ee = [-det(vv[0], t), -det(vv[1], t),
          1-det(vv[2], next_t), -det(vv[3], next_t)]
    v.extend(vv)
    ell.extend(ee)
    t = next_t
assert t == s.zeros(2, 1)
product = s.eye(2)
for vv in v:
    product = product*T(vv)
assert product == s.eye(2)
graph = [-ee + (i % 4 == 2) for i, ee in enumerate(ell)]
b = [2*aa for aa in graph]
print('Twelve actual ordered vectors:', [list(vv) for vv in v])
print('Physical line coefficients:', ell)
print('Positive-core graph coefficients:', graph)

f, g, l1, l2 = s.symbols('f g l1 l2', integer=True)
prefix = s.Matrix([f, g])
lam = s.Matrix([l1, l2])
block = []
for vv, bb in zip(v, b):
    xx = s.expand(-bb-lam.dot(vv)-det(vv, prefix))
    block.append(xx)
    prefix = s.simplify(prefix+xx*vv)
assert prefix == s.Matrix([f-6, g])
pair = s.expand(sum(xx*bb for xx, bb in zip(block, b)))
assert pair == 4-6*g-6*l1
print('General block dual coefficients:', block)
print('General block endpoint:', list(prefix), '; pairing:', pair)

j, k = s.symbols('j k', integer=True, nonnegative=True)
closed_block = [s.expand(xx.subs({f:-6*j,g:0,l1:1,l2:0})) for xx in block]
print('Closed dual block indexed from j=0:', closed_block)
print('After k blocks prefix=(-6k,0); append cap coefficient 6k.')
closed_pair = s.summation(pair.subs({g:0,l1:1}), (j,0,k-1))-6*k
assert s.expand(closed_pair+8*k) == 0
print('Exact all-k cochain pairing:', closed_pair)

for kk in (1,2,3):
    vectors = v*kk+[e1]
    N = len(vectors)
    V = s.Matrix.hstack(*vectors)
    U = s.zeros(N)
    for i in range(N):
        U[i,i] = -1 if i<N-1 else 0
        for j0 in range(i+1,N):
            U[i,j0] = det(vectors[i],vectors[j0])
    # Antisymmetric part is precisely the boundary intersection pairing.
    assert U-U.T == V.T*J*V
    xx = s.Matrix([a.subs(j,j0) for j0 in range(kk) for a in closed_block]+[6*kk])
    bb = s.Matrix(b*kk+[-1])
    assert V*xx == s.zeros(2,1)
    assert U.T*xx == bb+V.T*e1
    K = s.zeros(N,N-2)
    for col in range(N-2):
        row = col+2
        K[row,col] = 1
        K[0,col] = -vectors[row][1]
        K[1,col] = -vectors[row][0]
    Q = K.T*U*K
    assert Q == Q.T
    assert DomainMatrix.from_Matrix(Q).rank() == N-3
    R = s.Matrix([-1,1,0,0]*(3*kk)+[0])
    assert V*R == s.zeros(2,1)
    assert K.T*U*R == s.zeros(N-2,1)
    assert (bb.T*R)[0] == 0
    assert (bb.T*xx)[0] == (xx.T*U*xx)[0] == -8*kk
    print(f'Dense integral check k={kk}: kernel rank {N-2}, radical rank 1, square {-8*kk}.')
print('All symbolic and dense checks passed; geometric class identification remains a separate proof obligation.')
