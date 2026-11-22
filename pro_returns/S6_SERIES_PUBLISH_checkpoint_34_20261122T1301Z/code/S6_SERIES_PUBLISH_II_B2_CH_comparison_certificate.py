#!/usr/bin/env python3
"""Postrelease 01CH comparison: the full strict-transform derivative."""
import json
import sympy as s

x,y,t,w = s.symbols('x y t w')
q=(w-t)*(w-1)*(w-2)
A=-(w-1)*(w-2)
P=s.expand(q+y*A)
root=t+y
F=(x-y*root)*(x-y)*(x-2*y)
unit=(root-1)*(root-2)
checks=[]
def check(name, expr, expected=0):
    value=s.factor(expr-expected)
    assert value==0,(name,value)
    checks.append({'name':name,'passed':True,'difference':str(value)})
check('Exact blowup of a cubic with higher normal term',F.subs(x,y*w),y**3*P)
check('Implicit root of the full strict transform',P.subs(w,root))
check('Derivative of full strict transform at its root',s.diff(P,w).subs(w,root),unit)
check('Factor residue on the smooth branch',((x-y)*(x-2*y)).subs(x,y*root),y**2*unit)
check('Derivative residue on the smooth branch',s.diff(F,x).subs(x,y*root),y**2*unit)
check('Restriction of the unit to H',unit.subs(y,0),s.diff(q,w).subs(w,t))
check('Full derivative minus cubic derivative',s.diff(P,w)-s.diff(q,w),-y*(2*w-3))
check('Nonconstant derivative correction on the root',s.diff(P,w).subs(w,root)-s.diff(q,w).subs(w,root),-y*(2*t+2*y-3))
check('The simple-root value at the origin',unit.subs({y:0,t:0}),2)
check('Nonzero off-H correction at a nearby rational point',(s.diff(P,w)-s.diff(q,w)).subs({w:root,t:0,y:s.Rational(1,10)}, simultaneous=True).subs({t:0,y:s.Rational(1,10)}),s.Rational(7,25))
# This polynomial is a local algebra check; no assertion is made that it is
# the fibre of a compact torus degeneration satisfying the global hypotheses.
print(json.dumps({'tag':'01CH','method':'An exact factored polynomial with a moving simple root tests the full strict-transform derivative and its restriction to H.','checks':checks,'exact_checks':len(checks),'all_passed':True,'interpretation':'The proof needs the nonzero cubic derivative on H. Away from H the unit is the derivative of q3+yA, with the displayed correction; the theorem and its domain are unchanged.'},indent=2))
