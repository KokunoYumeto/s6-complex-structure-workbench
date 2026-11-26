"""Universal contraction kernel and intersection form for a four-torus.

The proof chooses any nonzero coefficient of a rational 1-class as a0.
The columns below are actual wedge products of a basis of its kernel.
No Milnor-fibre geometry is inferred from these symbolic identities.
"""
from itertools import combinations
from sympy import Matrix, symbols, zeros, simplify, expand

alpha=Matrix(1,4,symbols('a0:4'))
a0,a1,a2,a3=list(alpha)
pairs=list(combinations(range(4),2))
e=[Matrix.eye(4)[:,i] for i in range(4)]
def wedge(v,w):
    return Matrix([expand(v[i]*w[j]-v[j]*w[i]) for i,j in pairs])
def sign(xs):
    return (-1)**sum(xs[i]>xs[j] for i in range(4) for j in range(i+1,4))
C=zeros(4,6)
J=zeros(6,6)
for k,(i,j) in enumerate(pairs):
    C[:,k]=alpha[i]*e[j]-alpha[j]*e[i]
    for l,(p,q) in enumerate(pairs):
        xs=(i,j,p,q)
        J[k,l]=sign(xs) if len(set(xs))==4 else 0
W=Matrix.hstack(*[a0*e[i]-alpha[i]*e[0] for i in (1,2,3)])
K=Matrix.hstack(*[wedge(W[:,i],W[:,j]) for i,j in combinations(range(3),2)])
assert alpha*W==zeros(1,3)
assert alpha*C==zeros(1,6)
assert (C*K).applyfunc(expand)==zeros(4,3)
assert (K.T*J*K).applyfunc(expand)==zeros(3,3)
assert simplify(C.extract([1,2,3],[0,1,2]).det()-a0**3)==0
assert simplify(K.extract([3,4,5],[0,1,2]).det()-a0**6)==0
print('wedge_basis =',pairs)
print('cap_matrix =',C.tolist())
print('intersection_matrix =',J.tolist())
print('kernel_wedge_columns =',K.tolist())
print('alpha_W = 0; alpha_C = 0; C_K = 0; K_transpose_J_K = 0')
print('cap_rank_minor = a0**3; kernel_rank_minor = a0**6')
print('For a0 != 0: rank C = 3, image K = kernel C, and the restricted intersection form is identically zero.')
print('Any nonzero alpha is covered by permuting a nonzero coefficient into position zero. Geometry and the orientation-preserving embedding are proved in the frozen derivation.')
