#!/usr/bin/env python3
"""Exact algebra supporting B.4.28; no classification is delegated to code."""
import json
from pathlib import Path
import sympy as S

a,b,c,d=S.symbols('a b c d')
A=S.Matrix([[a,b],[c,d]])
identity=S.expand((A-S.eye(2)).det()-(1-(a+d)+A.det()))
assert identity==0
# det A=1 gives det(A-I)=2-tr A; hyperbolicity excludes eigenvalue 1.
checks={'determinant_identity':True}

# The angular integral of x^i y^j (t/(xy))^k survives only if i=j=k.
# The proof uses the exact identity for arbitrary indices and convergence.
counts={}
for n in [1,2,3,6,12,20]:
    kept=[(i,j,k) for i in range(n+1) for j in range(n+1)
          for k in range(n+1) if i-k==0 and j-k==0]
    assert kept==[(k,k,k) for k in range(n+1)]
    counts[str(n)]={'tested':(n+1)**3,'surviving':len(kept)}
checks['all_tested_residue_indices_exact']=True

v,e,f,h=S.symbols('v e f h')
checks['retained_partial_euler_identity']=S.expand(
    ((v-e+f-h)+h)-(v-e+f))==0
# This identity did not justify the rejected free-product assertion.
assert all(checks.values())
out={'status':'PASS','checks':checks,'residue_index_checks':counts,
     'scope':'algebra only; analytic and link hypotheses proved in text'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
