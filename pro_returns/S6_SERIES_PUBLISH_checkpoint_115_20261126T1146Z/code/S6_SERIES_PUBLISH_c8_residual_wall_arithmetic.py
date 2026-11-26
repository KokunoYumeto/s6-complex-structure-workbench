#!/usr/bin/env python3
"""Exact wall-map arithmetic and the eleven residual-total comparisons.

The three computation blocks are retained literally from the successful
publication calculations. This standalone mathematical source performs
those same assertions without the surrounding manuscript-edit operations.
Its creation does not constitute a new execution or independent check.
"""
from math import gcd
import sympy as sp
import sympy as S

M=sp.Matrix([[1,0,0],[-1,-1,1],[0,1,0]])
Mi=sp.Matrix([[1,0,0],[0,0,1],[1,1,1]])
assert M*Mi==Mi*M==sp.eye(3)
assert M*sp.ones(3,1)==sp.Matrix([1,-1,1])
row=sp.Matrix([[1,8,56]])
assert row*M==sp.Matrix([[-7,48,8]])
assert sum(row*M)==1-8+56==49
print('WALL_MAP',str(M.tolist()),'INVERSE',str(Mi.tolist()),'BOTH_COMPOSITES_IDENTITY')
print('OS45_II_ZERO2_ACTUAL_DEGREES',list(row*M),'OLD_INDIVIDUAL_DEGREES',[1,-8,56],'COMMON_SUM',49)

aa,bb,kk=sp.symbols('a b k',integer=True)
K11=aa;K12=aa*bb*kk;K22=aa*bb**2*kk**2-bb
assert sp.expand((K11-K12)+(K22-K12)+K12-(K11-K12+K22))==0
rows=[('45II2O',8,24,4,0,1),('45II2F',8,40,4,0,1),('45II3O',8,-32,0,0,1),('45II3F',8,-16,0,0,1),
 ('55II3O',4,72,0,0,1),('55II3F',4,80,0,0,1),('55base2',20,352,4,8,5),('55base3',20,-68,14,8,5),
 ('55base4',20,352,4,8,5),('55II20O',20,352,4,8,5),('55II20F',20,392,4,8,5)]
for name,b,K,P,lam,order in rows:
 assert K%2==0 and (-K//2)%b==P and -K%b==lam and b//gcd(K,b)==order
 print('UNCHANGED_TOTAL',name,'b',b,'K',K,'P',P,'lambda',lam,'critical_order',order)

m,e,r=S.symbols('m e r',integer=True)
for sigma in (-1,1):
    n=m*e+sigma
    A=S.Matrix([[sigma,0,0],[0,0,-sigma*e],[0,0,sigma],[-sigma*m,1,-sigma*r]])
    B=S.Matrix([[sigma,-r,-e*r,0],[m,0,r,1],[0,m,n,0]])
    v=S.Matrix([r,n,-m,0])
    assert S.simplify(B*A-S.eye(3))==S.zeros(3)
    assert S.simplify(A*B-S.eye(4)+sigma*v*S.Matrix([[0,1,e,0]]))==S.zeros(4)
    assert S.expand((S.Matrix([[0,1,e,0]])*v)[0])==sigma
    print('PRESENTATION_MAP sigma',sigma,'BA=I3; AB=I4-sigma*(r,n,-m,0)^t*(0,1,e,0) PASS')
