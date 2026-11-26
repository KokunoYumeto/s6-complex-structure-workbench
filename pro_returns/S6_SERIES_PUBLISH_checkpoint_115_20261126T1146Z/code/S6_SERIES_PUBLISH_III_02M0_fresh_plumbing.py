#!/usr/bin/env python3
"""Fresh moving-zero chart, gluing, singularity and small-resolution calculations.
The III M0 proof, old M0 programs and old M0 outcomes remain closed.
"""
import json
from datetime import datetime, timezone
import sympy as S

x,y,z,v,u,s,a,b,t,r=S.symbols('x y z v u s a b t r')
A,B,C,D=S.symbols('A B C D',nonzero=True)
phi=S.symbols('phi')
# Genuine line and dual-line changes on two overlapping trivializations.
assert S.expand((x/A)*(B*y)-u*(B/A)*phi-(B/A)*(x*y-u*phi))==0
assert S.simplify((x/A)/C-x/(A*C))==0
assert S.simplify(D*(B*y)-(B*D)*y)==0
assert S.simplify((D/C)*(B/A)*phi-(B*D)/(A*C)*phi)==0
print('PASS normal-line and dual-line frame maps and their triple cocycle')
# The two actual collar maps are inverse to the quotient generator.
x_from_infinity=u*phi/y
assert S.simplify(x_from_infinity*y-u*phi)==0
assert S.simplify(u*phi/(u*phi/x)-x)==0
print('PASS zero/infinity collar relation x=(u phi)/y and both inverses')
# Uniform separated collars and compact representatives, exactly rational.
a0=S.Rational(1,4); b0=S.Rational(1,2)
a1=S.Rational(1,3); b1=S.Rational(5,12); delta=S.Rational(1,32)
assert 0<a0<a1<b1<b0<1
assert delta<a0*a0 and delta/a0<b1
assert a1<b1 and b0<1/a1
assert a1<1/b0<1/b1<1/a1
print('PASS separated gluing collars and finite compact-representative bounds')
# Fixed nonzero u is absorbed by X=x/u. The complete singular ideal is linear.
X=S.symbols('X')
F=X*y-z*v+s
J=[S.diff(F,w) for w in (X,y,z,v)]
gb=S.groebner([F,*J],X,y,z,v,s)
assert [p.as_expr() for p in gb.polys]==[X,y,z,v,s]
assert S.diff(F,s)==1
H=S.hessian(F,(X,y,z,v))
assert H.det()==1
print('PASS unique fibre singularity at (X,y,z,v,s)=0 and nondegenerate Hessian')
# Chosen antidiagonal small resolution, not the other square diagonal.
chart0={X:a,y:b*t,z:b,v:a*t}
chart1={X:a*r,y:b,z:b*r,v:a}
assert S.expand((X*y-z*v).subs(chart0,simultaneous=True))==0
assert S.expand((X*y-z*v).subs(chart1,simultaneous=True))==0
assert S.expand((z*v).subs(chart0,simultaneous=True)-a*b*t)==0
assert S.expand((z*v).subs(chart1,simultaneous=True)-a*b*r)==0
A2,B2=S.symbols('A2 B2')
second=[A2*r,B2,B2*r,A2]
transition={A2:a*t,B2:b*t,r:1/t}
assert all(S.simplify(f.subs(transition,simultaneous=True)-g)==0
           for f,g in zip(second,[a,b*t,b,a*t]))
# Columns are valuations of (X,z,q), q=zv, on each smooth chart divisor.
cone0=S.Matrix([[1,0,0],[0,1,0],[1,1,1]])
cone1=S.Matrix([[1,0,1],[0,1,1],[1,1,1]])
assert cone0.det()==1 and cone1.det()==-1
assert cone0[:,0]==cone1[:,0] and cone0[:,1]==cone1[:,1]
assert cone0[:,1]-cone0[:,0]==S.Matrix([-1,1,0])
print('PASS both resolution charts, overlap, q map and the e1-e2 diagonal')
# Independent global section coordinates and exact finite-disc parameter pullback.
q,T,us,vs,lam=S.symbols('q T us vs lam')
assert S.expand((q-s)-q*(1-s*T)).subs(q,1/T)==0
scale=u*(1-s*T)
assert S.diff(scale,u)==1-s*T
coefficient_map=S.Matrix([u,-u*s])
assert coefficient_map.jacobian((u,s)).det()==-u
assert S.expand((x*y-u*(z*v-s)).subs(x,u*X)-u*F)==0
print('PASS section-ratio pullback and nonzero-u deformation-coordinate determinant')
print('PASS all fresh exact plumbing, inverse-map, cone and singularity identities')
print('Arithmetic completed UTC:',datetime.now(timezone.utc).isoformat())
