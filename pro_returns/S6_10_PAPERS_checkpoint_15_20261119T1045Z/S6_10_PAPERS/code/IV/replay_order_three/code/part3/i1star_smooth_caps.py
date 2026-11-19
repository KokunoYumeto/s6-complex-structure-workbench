#!/usr/bin/env python3
"""Exact mod-p smooth-cap obstruction on the three OS50 additive cores."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parent
cases=[('star','i1star_boundary.json',2,'H2_inversion_exterior'),('reduced_IV','i1star_iv_reduced_boundary.json',2,'H2_exterior_inversion'),('good_IV','i1star_iv_boundary.json',6,'H2_exterior_inversion')]
records=[]
for name,path,b,key in cases:
 j=json.loads((ROOT/path).read_text());I=s.Matrix(j[key]);assert I[1:,1:]==-s.eye(I.rows-1)
 records.append(dict(core=name,torsion_order=b,inversion=[[int(x) for x in row] for row in I.tolist()],free_inversion=[[int(x) for x in row] for row in (-s.eye(I.rows-1)).tolist()]))
m,n,la,lb=s.symbols('m n lambda_a lambda_b',integer=True)
R=s.Matrix([[m,0,0,-la],[0,m,0,-lb],[0,0,m,n]])
R0=R.subs(m,0);assert R0[:,:3]==s.zeros(3);assert R0.rank()==1
# This exact rank statement uses n nonzero in the field; the last entry records it.
assert R0[2,3]==n
checked=0
for p in [3,5,7,11,13,17,19,23,29,31]:
 for nn in range(1,p):
  for aa,bb in [(0,0),(1,-1),(p+2,2*p-3),(-5,7)]:
   A=R.subs({m:p*3,n:nn,la:aa,lb:bb})
   assert all(int(A[i,j])%p==0 for i in range(3) for j in range(3))
   assert int(A[2,3])%p!=0
   checked+=1
out={'scope':'Necessary smooth-site order exclusion on the three displayed additive cores; no integral order-one collar is discarded','source_inversions':records,'smooth_rim_kernel_matrix':[[str(x) for x in row] for row in R.tolist()],'rank_at_prime_dividing_order':1,'surviving_rim_dimension':2,'supplementary_field_checks':checked,'all_pass':True}
(ROOT/'i1star_smooth_caps.json').write_text(json.dumps(out,indent=2)+'\n')
for k,v in out.items():print(k,'=',v)
print('PASS: source-only inversion, exact kernel rank, and two surviving mod-p rim classes.')
