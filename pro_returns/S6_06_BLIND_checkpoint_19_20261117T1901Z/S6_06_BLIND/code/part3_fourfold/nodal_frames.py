#!/usr/bin/env python3
"""Exact algebra for the retained xy=q tangent-frame comparison."""
from pathlib import Path
import json
import sympy as s

root = Path(__file__).resolve().parent
x,y,xb,yb,t,z,v = s.symbols('x y xb yb t z v', nonzero=True)
rho2=x*xb+y*yb
G=s.Matrix([[x,yb],[-y,xb]])
Gstar=s.Matrix([[xb,-yb],[y,x]])
D=s.diag(t,1/t)
Gp=s.Matrix([[t*x,t*yb],[-y/t,xb/t]])
checks={
    'unitary_numerator':Gstar*G==s.eye(2)*rho2,
    'determinant_numerator':s.expand(G.det()-rho2)==0,
    'vertical_dq':s.Matrix([[y,x]])*s.Matrix([x,-y])==s.zeros(1,1),
    'horizontal_dq':s.expand((s.Matrix([[y,x]])*s.Matrix([yb,xb]))[0]-rho2)==0,
    'exact_equivariance':Gp==D*G,
    'preserves_q':s.simplify((t*x)*(y/t)-x*y)==0,
}
a,b,k=s.symbols('a b k',integer=True)
checks['opposite_weights_after_annular_shear']=s.simplify((a+k*b)+(-a-k*b))==0
result={'checks':checks,'all_pass':all(checks.values()),
        'matrix_numerator':s.sstr(G),'normal_parameter_matrix':s.sstr(D),
        'scope':'Exact local relative nodal frame only; global boundary-relative Pontryagin gluing is a separate check.'}
(root/'nodal_frames.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
assert result['all_pass']
