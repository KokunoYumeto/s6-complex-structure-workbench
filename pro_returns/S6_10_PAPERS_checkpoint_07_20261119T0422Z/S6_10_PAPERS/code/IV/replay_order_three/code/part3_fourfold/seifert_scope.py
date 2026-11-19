#!/usr/bin/env python3
"""Exact marked matrices for K16; no inference of source-cap existence."""
from pathlib import Path
import json
import math
import sympy as s

root = Path(__file__).resolve().parents[2]
m1,m2,n1,n2,b,k1,k2 = s.symbols('m1 m2 n1 n2 b k1 k2', integer=True)
R=s.Matrix([[m1,-n1],[-m2,-m2*b-n2]])
D=m1*m2*b+m2*n1+m1*n2
assert s.expand(R.det()+D)==0
assert s.expand(D.subs({n1:n1+m1*k1,n2:n2+m2*k2,b:b-k1-k2}, simultaneous=True)-D)==0
cases=[]
for a in range(1,13):
 for c in range(1,13):
  for j in range(a):
   if math.gcd(a,j)!=1: continue
   for ell in range(c):
    if math.gcd(c,ell)!=1: continue
    for beta in range(-2,2):
     detsum=a*c*beta+c*j+a*ell
     if abs(detsum)!=1: continue
     assert math.gcd(a,c)==1
     mu1=s.Matrix([a,-j]); mu2=s.Matrix([-c,-c*beta-ell])
     delta=int(s.Matrix.hstack(mu1,mu2).det())
     P=s.Matrix.hstack(mu1,delta*mu2)
     assert P.det()==1
     assert P.inv()*s.Matrix([0,1])==s.Matrix([delta*c,a])
     cases.append(dict(m1=a,m2=c,n1=j,n2=ell,b=beta,
                       determinant=detsum,meridian_matrix=[list(mu1),list(mu2)],
                       oriented_coordinate_matrix=[list(P.row(i)) for i in range(2)],
                       gamma_coordinates=[delta*c,a]))
data=dict(status='PASS',proof='P3K.16',
          relation_matrix=[[str(x) for x in R.row(i)] for i in range(2)],
          determinant=str(-D),
          exact_section_change='n_i -> n_i+m_i*k_i; b -> b-sum(k_i); C_i unchanged',
          certified_examples=cases,
          scope='These are exact base and meridian certificates; source, line and affine-cap existence are separate data retained in K15.')
(root/'code/part3_fourfold/seifert_scope.json').write_text(json.dumps(data,indent=2,default=int)+'\n')
print('PASS:',len(cases),'primitive sphere-base matrices and the symbolic determinant/section-change identities.')
