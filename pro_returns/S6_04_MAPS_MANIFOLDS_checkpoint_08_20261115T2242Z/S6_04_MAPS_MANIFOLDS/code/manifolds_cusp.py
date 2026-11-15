"""Exact algebra for the cyclic gamma-cover cusp; no floating-point input."""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
pvar=s.symbols('t')
# H,E1,E2,E3; classes of boundary curves in cyclic order.
C=[s.Matrix([0,1,0,0]),s.Matrix([1,-1,-1,0]),s.Matrix([0,0,1,0]),s.Matrix([1,0,-1,-1]),s.Matrix([0,0,0,1]),s.Matrix([1,-1,0,-1])]
J=s.diag(1,-1,-1,-1)
B=s.Matrix.vstack(*[((C[i]-[1,pvar,pvar][i]*C[i+3]).T*J) for i in range(3)])
mins=[s.factor(B[:,inds].det()) for inds in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]]
print('Degree-two normalization differential, rows in opposite boundary pairs:')
print(B)
print('Maximal minors:',mins)
print('At t=1 rank:',B.subs(pvar,1).rank())
print('Over Q(t) rank:',B.rank())
print('Kernel over Q(t):',B.nullspace())
print('Finite cyclic cover Smith data:')
for p in [1,2,3,5,7,11,13,17,19,23,25,29,31]:
    T=s.zeros(p)
    for i in range(p): T[(i+1)%p,i]=1
    BB=s.zeros(3*p,4*p)
    for i in range(3):
        for j in range(4):
            f=s.Poly(B[i,j],pvar)
            bb=s.zeros(p)
            for (k,),a in f.terms(): bb+=a*T**k
            BB[i*p:(i+1)*p,j*p:(j+1)*p]=bb
    S=smith_normal_form(BB,domain=ZZ)
    ds=[abs(S[i,i]) for i in range(min(S.shape)) if S[i,i]!=0]
    print({'p':p,'rank':len(ds),'kernel_rank':4*p-len(ds),'cokernel_free':3*p-len(ds),'torsion':[int(d) for d in ds if d!=1]})
print('Euler comparisons:')
for p in [1,5,7,11,13]:
    print({'p':p,'cover_euler':2*p,'connected_sum_S3xS3_euler':4-2*p,'minimum_b2':p-1})
# Intersections of the two adjacent boundary pairs meeting neighboring components.
Dp=C[1]+C[2]; Dm=C[4]+C[5]
print('Adjacent-pair intersection matrix:',s.Matrix.hstack(Dp,Dm).T*J*s.Matrix.hstack(Dp,Dm))
