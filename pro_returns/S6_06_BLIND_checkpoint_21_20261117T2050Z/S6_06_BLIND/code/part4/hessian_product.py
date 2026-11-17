"""Exact Morse Hessian in the actual product-Hessian exclusion P4R.15."""
from pathlib import Path
import json
import sympy as sp
x,y,z,a,b,c,v,epsilon=sp.symbols('x y z a b c v epsilon', nonzero=True)
m=sp.symbols('m',integer=True,positive=True)
h=v+(a*y*y+2*b*y*z+c*z*z)/2
f=x*x+h**m
H=sp.hessian(f,(x,y,z)).subs({x:0,y:0,z:0})
expected=sp.diag(2,1,1)
expected[1:3,1:3]=m*v**(m-1)*sp.Matrix([[a,b],[b,c]])
assert all(sp.simplify(t)==0 for t in H-expected)
det=sp.factor(H.det())
assert sp.simplify(det-2*m*m*v**(2*m-2)*(a*c-b*b))==0
moving=x*x+(y*z-epsilon)**m
movingH=sp.hessian(moving,(x,y,z)).subs({x:0,y:0,z:0})
assert movingH[0,0]==2
assert sp.simplify(movingH[1,2]-m*(-epsilon)**(m-1))==0
assert sp.simplify(movingH.det()+2*m*m*epsilon**(2*m-2))==0
out={'statement':'P4R.15','integer_parameter':'m>=2',
 'critical_value':'v^m','hessian':[[str(t) for t in row] for row in H.tolist()],
 'determinant':'2*m^2*v^(2m-2)*(a*c-b^2)',
 'moving_node':'x^2+(y*z-epsilon)^m','moving_node_value':'(-epsilon)^m',
 'moving_node_hessian_determinant':'-2*m^2*epsilon^(2m-2)',
 'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Product-Hessian Morse identities for arbitrary positive integer m: PASS')
print('General Hessian:',H)
print('General determinant:',det)
print('Moving-node determinant = -2*m^2*epsilon^(2m-2).')
