#!/usr/bin/env python3
"""Exact source equations at the remaining marked E7 u=0 puncture.
No completed-threefold return or finite-cap extension is inferred.
"""
import json
from pathlib import Path
import sympy as s
u,v,X,Y,T,x,y,t=s.symbols('u v X Y T x y t')
r=(1-2*u**3)/(3*u**2)
p=y*y-x**3-3*r*x*x-t*x-1
scaled=s.factor(u**6*p.subs({x:X/u**2,y:Y/u**3,t:T/u**4}))
expect=Y*Y-X**3-(1-2*u**3)*X*X-T*X-u**6
assert s.factor(scaled-expect)==0
P=X**3+(1-2*v)*X**2+T*X+v**2
assert s.factor(P.subs(T,v*v-2*v)-(X-v)**2*(X+1))==0
D=s.factor(s.discriminant(P,X))
Df=(-T+v*v-2*v)*(4*T*T-4*T*v-T+32*v**3-11*v*v+2*v)
assert s.factor(D-Df)==0
assert s.factor(D.subs(v,0)-T*T*(1-4*T))==0
assert P.subs({X:0,Y:v})==v*v
c=s.symbols('c')
Z=(1+c)/(1-c)
assert s.cancel(Z*(c*c-1)+4).subs(c,1)==0
result={'status':'PASS','checks':6,'source_equation':'Y^2=X^3+(1-2v)X^2+TX+v^2','section':'G=(0,v)','selected_node':'T_0=v^2-2v, X=v, Y=0','discriminant':str(D),'central_discriminant':'T^2(1-4T)','nodal_group_point':'Z_G=(1+sqrt(1+v))/(1-sqrt(1+v)); v Z_G -> -4','scope':'Exact source/chart identities only. No cap continuation, closed total family, or source-loop return class assigned.'}
pth=Path(__file__).with_suffix('.json');pth.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
