#!/usr/bin/env python3
"""Exact local repair function and equivariant relative pairings.

This does not identify the global doubled four-cycle or count gamma sheets.
"""
from pathlib import Path
import json
import sympy as s
R,A,B,eps,rho=s.symbols('R A B epsilon rho',positive=True)
h=1+R**2
f=(h*h*B+eps*R**2)/(h*h*A+eps)
assert s.simplify(s.diff(f,B)-h*h/(h*h*A+eps))==0
assert s.simplify(s.diff(f,A)+h*h*(h*h*B+eps*R**2)/(h*h*A+eps)**2)==0
assert s.simplify(f.subs({A:0,B:0}))==R**2
Q,U,V=s.symbols('Q U V',positive=True)
south=s.simplify(f.subs({R:1/Q,A:U*Q**2,B:V*Q**2}))
assert s.simplify(south-(((1+Q**2)**2*V+eps)/((1+Q**2)**2*U+eps*Q**2)))==0
u,v,c=s.symbols('u v c')
# c is any common background equivariant line class.
line_weights=[-v,0,u,u-v]
orientation=[1,-1,1,-1] # last point is the reversed old page.
x2=s.simplify(sum(sign*(c+w)**2/(u*v)
                 for sign,w in zip(orientation,line_weights)))
p1=s.simplify(sum(sign*(u*u+v*v)/(u*v) for sign in orientation))
assert x2==2
assert p1==0
assert s.simplify((12*x2-p1)/24)==1
data={
 'repair_function_rho_squared':str(f),
 'south_chart':str(south),
 'new_fixed_point_source_orientation_signs':[1,-1,1],
 'principal_circle_weights':['v','0','-u'],
 'Euler_line_equivariant_restrictions':['-v','0','u'],
 'old_principal_circle_weight':'v-u',
 'old_Euler_line_equivariant_restriction':'u-v',
 'closed_difference_orientation_signs':orientation,
 'relative_x_squared':2,'relative_p1':0,
 'local_graph_index_combination':1,
 'scope':'local compact page replacement with specified outer collar and actual circle line; no global angular-trace or gamma-sheet count is assigned',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: smooth local repair function, chart compatibility, relative x^2=2 and p1=0.')
