#!/usr/bin/env python3
"""Exact local fan and period conjugation for a nonvertical edge."""
from pathlib import Path
import json
import sympy as s
S=s.Matrix([[1,0],[-1,1]])
edges=[s.Matrix([0,1]),s.Matrix([1,0]),s.Matrix([1,-1])]
new=[S*v for v in edges]
assert new==[s.Matrix([0,1]),s.Matrix([1,-1]),s.Matrix([1,-2])]
assert S.det()==1
Z,V,q,alpha,g,lam,beta=s.symbols('Z V q alpha g lambda beta',nonzero=True)
def shear(z,v): return z,v/z
def inverse(z,v): return z,z*v
z,v=inverse(Z,V)
hnew=shear(q*z,alpha*v)
gnew=shear(g*z,q*lam*beta*v)
assert tuple(map(s.simplify,hnew))==(q*Z,alpha*V/q)
assert tuple(map(s.simplify,gnew))==(g*Z,q*lam*beta*V/g)
data={
 'shear':S.tolist(),
 'old_edges':[v.T.tolist()[0] for v in edges],
 'new_edges':[v.T.tolist()[0] for v in new],
 'torus_map':['Z','V/Z'],
 'conjugated_h':[str(s.simplify(z)) for z in hnew],
 'conjugated_gamma':[str(s.simplify(z)) for z in gnew],
 'scope':'exact local fan/period isomorphism; the actual outer identification with the original period group remains to be computed'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2,default=int)+'\n')
print('PASS: nonvertical fan flip and the complete conjugated period generators.')
