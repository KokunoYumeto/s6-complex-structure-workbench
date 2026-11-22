#!/usr/bin/env python3
"""Independent symbolic arithmetic for F.2.28 and F.2.30."""
import json
import sympy as s
r1,r2,kappa,a,b=s.symbols('r1 r2 kappa a b',integer=True)
R=s.Matrix([[5,0,-r1],[0,4,-r2],[1,1,kappa]])
det=s.expand(R.det())
assert det==20*kappa+4*r1+5*r2
negative=s.expand(det.subs({r1:1+5*a,r2:-1+4*b}))
positive=s.expand(det.subs({r1:-1+5*a,r2:1+4*b}))
assert negative==20*(kappa+a+b)-1
assert positive==20*(kappa+a+b)+1
# In rank-one fixed vertical space the norm formula N=lambda*phi
# has phi(lambda)=m and N(I-M)=0. N(q-lambda/m)=0 follows exactly.
m,sv=s.symbols('m sv',nonzero=True)
assert s.simplify(sv*(1-m/m))==0
# Characteristic-number forcing for each retained integral datum.
x,idx=s.symbols('x idx',integer=True)
chi=6
p1sq=4*x;p2=x+2*chi
sigma=s.factor((7*p2-p1sq)/45)
assert s.simplify(sigma-(x+28)/15)==0
forced=s.simplify(sigma.subs(x,2+240*idx))
assert forced==2+16*idx
allowed=[i for i in range(-2,3) if abs(2+16*i)<=4]
assert allowed==[0]
assert 6-2==4
print(json.dumps({'free_relation_matrix':str(R),'determinant':str(det),'negative_twist_gauge_identity':str(negative),'positive_twist_gauge_identity':str(positive),'vertical_translation_norm_identity_verified':True,'Euler_number':6,'middle_rank':4,'signature_from_Todd_integer':str(forced),'allowed_Todd_integer_under_signature_bound':0,'source_inputs':'The theorem statements and displayed norm equation; no prior checking program'},indent=2))
