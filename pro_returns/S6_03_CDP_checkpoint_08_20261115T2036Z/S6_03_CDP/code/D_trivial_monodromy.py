"""Exact integral Mayer--Vietoris maps for Statement D.2.7.

The geometric maps are derived in the proof.  This program checks their
unimodularity, Smith normal forms, and the chosen elliptic-subtorus classes.
"""
from itertools import combinations
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

E = s.eye(4)
e = [E[:, i] for i in range(4)]
pairs = list(combinations(range(4), 2))


def wedge(v, w):
    return s.Matrix([v[i]*w[j]-v[j]*w[i] for i, j in pairs])


def quotient_by_primitive(v):
    """Integral quotient with kernel Zv, using a coordinate equal to +/-1."""
    pivot = next(i for i, a in enumerate(v) if abs(a) == 1)
    rows = []
    for j in range(len(v)):
        if j != pivot:
            row = s.zeros(1, len(v))
            row[0, j] = 1
            row[0, pivot] = -v[j]/v[pivot]
            rows.append(row)
    Q = s.Matrix.vstack(*rows)
    assert Q*v == s.zeros(len(v)-1, 1)
    return Q


v0 = e[0]
w = [e[2], e[1]+e[3], e[0]+e[3]]
partners = [e[3], -e[0]-e[2], e[1]-e[2]]
classes = [wedge(wi, ui) for wi, ui in zip(w, partners)]
W = s.Matrix.hstack(v0, *w)
assert abs(W.det()) == 1
print('ordered wedge basis:', [(i+1,j+1) for i,j in pairs])
print('columns (v0,w1,w2,w3):')
print(W)
print('determinant:', W.det())
print('columns [C1],[C2],[C3]:')
print(s.Matrix.hstack(*classes))

# Exterior base has mu1,mu2 and mu3=-mu1-mu2.  Its only nonzero
# clutching vector is c1=v0.  The signed MV maps are (j_M,-j_U).
mu = [s.Matrix([1,0]), s.Matrix([0,1]), s.Matrix([-1,-1])]
clutch = [v0, s.zeros(4,1), s.zeros(4,1)]
Q = [quotient_by_primitive(wi) for wi in w]
R = [quotient_by_primitive(ci) for ci in classes]

# H1(boundary)=direct sum of three copies of Lambda+Z*mu.
# H1(M)=Lambda+Z^2; H1(U_i)=Lambda/Z*w_i.
mv1 = s.zeros(15, 15)
for i in range(3):
    for j in range(4):
        mv1[:4,5*i+j] = e[j]
        mv1[6+3*i:9+3*i,5*i+j] = -Q[i]*e[j]
    mv1[:4,5*i+4] = clutch[i]
    mv1[4:6,5*i+4] = mu[i]
assert abs(mv1.det()) == 1
print('H1 signed MV matrix size:', mv1.shape)
print('H1 signed MV determinant:', mv1.det())
print('H1 signed MV Smith diagonal:', list(smith_normal_form(mv1, domain=s.ZZ).diagonal()))

# H2(M)=Lambda^2 Lambda + Lambda tensor Z^2 (dimension 14).
# H2(U_i)=Lambda^2 Lambda/Z[C_i] (dimension 5).
# H2(boundary_i)=Lambda^2 Lambda + Lambda*mu_i (dimension 10).
mv2 = s.zeros(29,30)
I6 = s.eye(6)
for i in range(3):
    for j in range(6):
        mv2[:6,10*i+j] = I6[:,j]
        mv2[14+5*i:19+5*i,10*i+j] = -R[i]*I6[:,j]
    for j in range(4):
        mv2[:6,10*i+6+j] = wedge(e[j],clutch[i])
        for k in range(2):
            mv2[6+4*k+j,10*i+6+j] = mu[i][k]
snf2 = list(smith_normal_form(mv2,domain=s.ZZ).diagonal())
assert len(snf2) == 29 and all(abs(a) == 1 for a in snf2)
print('H2 signed MV matrix size:', mv2.shape)
print('H2 signed MV rank:', mv2.rank())
print('H2 signed MV Smith diagonal:', snf2)

relations = s.Matrix.hstack(*[wedge(v0,ej) for ej in e],*classes)
snf_rel = list(smith_normal_form(relations,domain=s.ZZ).diagonal())
assert len(snf_rel) == 6 and all(abs(a) == 1 for a in snf_rel)
print('Final H2 relation matrix:')
print(relations)
print('Final H2 Smith diagonal:', snf_rel)
print('Verified: integral H1(Y)=H2(Y)=0; no torsion cokernel remains.')

# Integral and coherent comparison in D.2.8.
gamma = s.Matrix([1,1,0,-1])
assert all((gamma.T*wi)[0] == 0 for wi in w)
assert s.Matrix.hstack(*w).rank() == 3
period_projection = s.Matrix([[1,s.I,0,0],[0,0,1,s.I]])/2
for i, wi in enumerate(w):
    annihilator = s.Matrix.hstack(*wi.T.nullspace())
    assert annihilator.cols == 3
    assert (period_projection*annihilator).rank() == 2
print('Global integral section generator:', list(gamma))
print('All three local rank-three real annihilators have complex period rank two.')
print('Coherent splitting proved geometrically: R1 O = O^2, R2 O = O.')
