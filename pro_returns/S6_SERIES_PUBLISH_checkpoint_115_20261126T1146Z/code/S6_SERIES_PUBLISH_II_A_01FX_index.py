#!/usr/bin/env python3
"""Fresh exact Chern-root expansion for cdp:st:D.1.12.

Authored from the statement and analytic index formula before target release.
No earlier checking program or target proof was read or reused.
"""
import json
import sympy as s

x1,x2,x3,t=s.symbols('x1 x2 x3 t')
td=s.Integer(1)
for x in (x1,x2,x3):
    td*=1+x*t/2+x*x*t*t/12
degree3=s.expand(td).coeff(t,3)
c1=x1+x2+x3
c2=x1*x2+x1*x3+x2*x3
assert s.expand(degree3-c1*c2/24)==0
g,e,a,length=s.symbols('g e a length')
leray=s.expand((1-g)-(e+2*(1-g))+(a+(1-g)+length))
assert leray==a-e+length
print(json.dumps({'todd_degree_three':str(s.factor(degree3)),
 'c1_c2_over_24_identity':True,'leray_index':str(leray),
 'meaning':'length>=0 and a-e>=0 force both zero when chi(Y,O_Y)=0'},indent=2))
