#!/usr/bin/env python3
"""Fresh symbolic exploration from the clean F2.16 definitions only.

Target proof and old producer are unopened. This is a working certificate;
the written derivation and final output will be frozen before exposure.
"""
import sympy as s
from itertools import combinations
from pathlib import Path
import json

v,t=s.symbols('v t'); q=v*v-v+1
A=s.zeros(5)
for j in range(5):A[(j+1)%5,j]=1
X=s.zeros(5,2);X[0,0]=1;X[2,1]=1;X[4,1]=v
Y=s.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
N=X*Y;C=(s.eye(5)+N)*A;B=A**4*(s.eye(5)-N)
P=s.eye(5);P[:,0]=s.ones(5,1)/q
Ap=s.simplify(P.inv()*A*P);Bp=s.simplify(P.inv()*B*P)
sigma=v*v+v-1;rho=-(v+1)*(v*v-2)/2
beta=s.Matrix([[sigma,sigma-v*rho,v*v*sigma+v*rho,rho,-v*sigma-rho]])
Ah=s.diag(1,Ap);Bh=s.diag(1,Bp);Bh[0,1:6]=beta
L=s.Matrix([[-2,3,-5,-1,5,-3],[0,2,-2,2,-2,2],[0,-4,0,0,4,-4],[0,0,0,-4,4,-4],[0,0,4,-4,4,-4],[0,0,0,-4,4,0]])/4
Av=s.simplify(L.inv()*Ah*L);Bv=s.simplify(L.inv()*Bh*L)
K=s.simplify(Bv*Av-s.eye(6))

if __name__=='__main__':
 print('YX',Y*X)
 print('N ones',list(map(s.factor,N*s.ones(5,1))))
 print('ones^t N',list(map(s.factor,(s.ones(1,5)*N))))
 print('C char',s.factor(C.charpoly(t).as_expr()))
 print('A prime',Ap)
 print('A_v',Av)
 print('B_v',Bv)
 print('K square',s.simplify(K*K))
 print('K',K)
 for aa in range(1,5):
  for bb in range(1,4):
   W=A**aa*C**bb
   tr=s.factor(s.trace(W)); dual=s.factor(s.trace(C**(4-bb)*A**(5-aa)))
   if tr!=dual or s.degree(tr,v)>0:print('word A^%d C^%d'%(aa,bb),'trace',tr,'inverse',dual,'difference',s.factor(tr-dual))
 print('Bhat order4',s.simplify(Bh**4-s.eye(6)))
 print('K maxrank',K.rank())
