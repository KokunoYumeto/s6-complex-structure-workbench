#!/usr/bin/env python3
"""Independent polynomial check for the examples of cdp:st:D.1.15.

Written before opening the target construction; no prior code was reused.
"""
import itertools,json
import sympy as s
x,y,z,u=s.symbols('x y z u', real=True)
i=s.I
P=s.Matrix([[1,i,z,i*z],[-z,i*z,1,-i]])
J=s.diag(s.Matrix([[0,1],[-1,0]]),s.Matrix([[0,1],[-1,0]]))
isotropic=s.simplify(P*J*P.T)
assert isotropic==s.zeros(2)
Pxy=P.subs(z,x+i*y)
R=s.Matrix([[s.re(Pxy[r,c]) if part==0 else s.im(Pxy[r,c])
             for c in range(4)] for r,part in ((0,0),(0,1),(1,0),(1,1))])
det=s.factor(R.det())
assert det==-(1+x*x+y*y)**2
minors={str(cols):s.factor(P[:,list(cols)].det()) for cols in itertools.combinations(range(4),2)}
leading=P.applyfunc(lambda a:s.expand(a).coeff(z,1))
assert leading.rank()==2
print(json.dumps({'PJP_transpose':str(isotropic),'real_evaluation_matrix':str(R),
 'real_determinant':str(det),'complex_minors':{k:str(v) for k,v in minors.items()},
 'rank_at_infinity':leading.rank(),'coherent_quotient':'[v] -> P J v gives O(1)^2'},indent=2))
