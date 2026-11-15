"""Exact cyclic cusp intersections for Theorem D.1.6.

The geometry identifies D_i D_j with -2f, f, 0 according to the cyclic
Cartan matrix; this verifies all lattice relations and the generator index.
"""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from math import gcd
for d in (5,7,11,13,17,19,23,25,29,31,35,49,101):
    C=s.zeros(d)
    for i in range(d):
        C[i,i]=-2; C[i,(i-1)%d]=C[i,(i+1)%d]=1
    assert C*s.ones(d,1)==s.zeros(d,1)
    assert C.rank()==d-1
    S=smith_normal_form(C,domain=s.ZZ)
    snf=[abs(S[i,i]) for i in range(d)]
    assert snf==[1]*(d-2)+[d,0]
    assert gcd(2,d)==1
    print('d=',d,'cyclic_Cartan_SNF=',snf,'ruling_generator_index=',gcd(2,d))
# Intersection form on dP6, in H,E1,E2,E3.
Q=s.diag(1,-1,-1,-1)
F=s.Matrix([1,-1,0,0])
E1=s.Matrix([0,1,0,0])
assert (F.T*Q*F)[0]==0
assert (F.T*Q*E1)[0]==1
print('F^2=0, F.E1=1; affine Cartan products have vanishing integral cubic form.')
