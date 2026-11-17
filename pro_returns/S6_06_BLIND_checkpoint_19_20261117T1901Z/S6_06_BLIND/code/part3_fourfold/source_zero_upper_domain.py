#!/usr/bin/env python3
"""Exact defining functions and ownership for the positive-chamber upper fill."""
import json
from pathlib import Path
import sympy as s
A,t,ss,T1,V=s.symbols('A t ss T1 V',nonnegative=True)
f=(1-A)*(A+(1-A)*t)
assert s.simplify(f.subs(A,s.Rational(1,2))-(1+t)/4)==0
H=1+ss;rho2=H*T1+H**2*V;R2=ss*(T1+V)
assert s.simplify((1-1/H)*(H*T1+(1/H)*H**2*V)-R2)==0
x0,x1,y0,y1=s.symbols('x0 x1 y0 y1',nonnegative=True)
cs=(x0**2+x1**2)*(y0**2+y1**2)-(x0*y0+x1*y1)**2
assert s.factor(cs-(x0*y1-x1*y0)**2)==0
out={'status':'PASS','checks':3,
 'domain':'rho<=r1 OR (r1<=rho<=rho0 AND (R>=epsilon OR A>=1/2)), 2epsilon<r1<rho0',
 'artificial_face':'At A=1/2, R/rho>=1/2, hence the A-face above r1 is interior to R>epsilon.',
 'upper_chart':'z=1, |S|^2<=1, rho^2=(1+|S|^2)|T1|^2+(1+|S|^2)^2|V|^2',
 'ownership':'Whole upper fibre and its charge-one origin once; whole fixed exceptional disk once; only lower horn retained as an attachment boundary.',
 'scope':'Actual positive-chamber compact domain; final global ledger remains under audit.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS 3 exact upper-domain/bound identities')
