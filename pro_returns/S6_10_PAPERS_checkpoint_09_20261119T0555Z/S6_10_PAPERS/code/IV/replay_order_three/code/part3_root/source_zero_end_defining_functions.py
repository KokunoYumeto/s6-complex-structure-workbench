"""Exact defining-function identities for the reduced source-zero lower arm."""
from pathlib import Path
from datetime import datetime,timezone
import json,sympy as s

root=Path(__file__).resolve().parents[2]
A,u,tau,b,c,H,x,y=s.symbols('A u tau b c H x y',positive=True)
checks=[]
def check(name,left,right):
    assert s.factor(left-right)==0,name
    checks.append(name)
ratio=(1-A)*(A+(1-A)*u)
check('full ratio from actual metric',(1-A)*(b+A*c)/(b+c),ratio.subs(u,b/(b+c)))
lower=(tau**2-A+A**2)/(1-A)**2
check('exact lower corner equation',ratio.subs(u,lower),tau**2)
check('lower angular derivative',s.diff(lower,A),(A+2*tau**2-1)/(1-A)**3)
check('lower initial value',lower.subs(A,0),tau**2)
Am=(1-s.sqrt(1-4*tau**2))/2
Ap=(1+s.sqrt(1-4*tau**2))/2
check('lower terminal value',lower.subs(A,Am),0)
check('upper zero-section corner',Ap*(1-Ap),tau**2)
check('separation of arm roots',Ap-Am,s.sqrt(1-4*tau**2))
check('charged metric equality',x*(x+y),x**2+x*y)
check('positive chamber b',H*(s.sqrt(x)*s.sqrt(y))**2/H,x*y)
check('charged metric scaling',(x**2+x*y)/x,x+y)
check('charged angular identity',1-(x*y)/(x*x+x*y),x/(x+y))
check('squared positive defining-factor identity',(x+y)**2*(1-y/(x+y)),x*(x+y))
for numerator,denominator in ((1,3),(1,4),(1,5),(2,5)):
    q=s.Rational(numerator,denominator)
    assert 0<q<s.Rational(1,2)
    a0=Am.subs(tau,q)
    assert s.simplify(a0<s.Rational(1,2)) is s.true
    assert s.simplify(a0+2*q*q-1<0) is s.true
    assert 1-q*q>s.Rational(3,4)
    checks.append(f'exact arm bounds tau={q}')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':len(checks),
     'identities':checks,'scope':'Actual reduced a2 product/radial defining-function comparison on the lower corner arm. No radial normalization of the source functions and no global source-zero return assignment.'}
(root/'code/part3_root/source_zero_end_defining_functions.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
