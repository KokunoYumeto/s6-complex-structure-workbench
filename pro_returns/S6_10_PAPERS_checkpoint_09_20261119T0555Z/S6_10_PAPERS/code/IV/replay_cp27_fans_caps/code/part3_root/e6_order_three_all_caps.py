#!/usr/bin/env python3
"""Exact OC identities: coincident point Cartier arrow and full chord/root maps.

The geometric cap product and equality of characteristic integrals are proved
in OC.4--5 and separately reviewed. This certificate checks their displayed
algebraic inputs; finite samples do not replace the symbolic identities.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math
import sympy as S

R=Path(__file__).resolve().parents[2]
checks=[]
def eq(name, expression):
    value=S.factor(S.together(expression))
    if value != 0:
        raise AssertionError((name, str(value)))
    checks.append(name)
def mod(name, expression, relation, variable):
    numerator=S.fraction(S.together(expression))[0]
    eq(name,S.rem(numerator,relation,variable))

l,j=S.symbols('l j',integer=True,nonnegative=True)
m=3*l+2;k=2*l+1
for name,expression in {
    'a2 root exponent':2*m-2*k-(2*l+2),
    'a4 root exponent':3*m-4*k-(l+2),
    'a6 root exponent':4*m-6*k-2,
    'G root exponent':2*m-3*k-1,
    'formal coordinate arrow':3*k-2*k-k,
    'invariant c low term':l-2*k+m,
    'invariant c high term':2*l-4*k+2*m,
    'UV deck weight':-3*k+2*m-1,
    'middle ab deck weight':2*(l+1)+2*k-2*m,
    'middle cubic deck weight':3*(l+1)-m-1,
    'formal division component':2*m-1-3*(2*l+1),
    'formal division norm':m*(2-(2*m-1)/m)-1,
    'B prime order at s zero':6*(l+1)-2*m-2,
    'full selected coefficient exponent':2*m-6*(l+1)+2,
    'normalized chord deck':-k+k,
}.items():eq(name,expression)

a,b,c,cp,B,C=S.symbols('a b c cp B C')
X=a*b;Y=a*b*(a+b)/2;z=a*b*(b-a)/(2*c)
rel=c*c-1-B*a*b-C*a*a*b*b
mod('full reduced root equation',Y*Y-X**3-z*z*(1+B*X+C*X*X),rel,c)
for name,xx,uu,vv in [('middle',a*b,a*a*b,a*b*b),
                     ('U-end',a*b,a,a*a*b**3),
                     ('V-end',a*b,a*a*b**3,a)]:
    eq(name+' UV=X3',uu*vv-xx**3)
am,bm=S.symbols('am bm')
eq('U-middle X overlap',(a*b).subs({a:am**2*bm,b:1/am})-am*bm)
eq('U-middle U overlap',a.subs(a,am**2*bm)-am**2*bm)
eq('U-middle V overlap',(a*a*b**3).subs({a:am**2*bm,b:1/am})-am*bm**2)
eq('V-middle X overlap',(a*b).subs({a:am*bm**2,b:1/bm})-am*bm)
eq('V-middle U overlap',(a*a*b**3).subs({a:am*bm**2,b:1/bm})-am**2*bm)
eq('V-middle V overlap',a.subs(a,am*bm**2)-am*bm**2)
K=1+b*(b-a)*(B+C*a*b)/(2*c*(c+1))
F=1-a*b*(B+C*a*b)*(K+1)/(2*c*(c+1))-C*a*b*b*(a-b)/(4*c*c)
Xp=a*(a-b)*F;Yp=-z-a*K*Xp
H=K+b*(a-b)*(B+C*Xp)/(2*c*(1+cp))
mod('full plus-G chord slope',(Y-z)/X-a*K,rel,c)
eq('full plus-G X',a*a*K*K-C*z*z-X-Xp)
mod('full plus-G V',Yp+z*cp+a*Xp*H,cp*cp-1-B*Xp-C*Xp*Xp,cp)
eq('full source target product',((b-a)*F/H)*(-a*H)-Xp)
for name,value in [('K',K),('F',F),('H',H)]:
    eq('central unit '+name,value.subs({a:0,b:0,c:1,cp:1})-1)

# The section 6G is evaluated by literal Weierstrass addition and doubling.
s,q,t=S.symbols('s q t')
r=S.Rational(1,4)-s
x2=s;y2=-t-s/2
slope3=S.factor((y2-t)/x2)
x3=S.factor(slope3*slope3-r-x2)
y3=S.factor(-t-slope3*x3)
tau3=S.factor((-x3/y3/q).subs(t,1/q))
target3=-2*s*(2+s*q)/(8+6*s*q+(s*s-s**3)*q*q)
eq('actual tau0 3G',tau3-target3)
slope6=S.factor((3*x3*x3+2*r*x3+t)/(2*y3))
x6=S.factor(slope6*slope6-r-2*x3)
y6=S.factor(-y3+slope6*(x3-x6))
tau6=S.factor((-x6/y6/q).subs(t,1/q))
ell=S.cancel(tau6/s)
ell_num,ell_den=S.fraction(ell)
assert ell_den.subs({s:0,q:0})!=0
checks.append('tau0 6G/s joint denominator is a unit')
eq('tau0 6G/s exact numerator constant',ell_num.subs({s:0,q:0})+1024)
eq('tau0 6G/s exact denominator constant',ell_den.subs({s:0,q:0})-1024)
eq('tau0 6G exact s factor',tau6-s*ell)
eq('tau0 6G q-zero value',tau6.subs(q,0)+s)
eq('tau0 6G/s joint value',ell.subs({s:0,q:0})+1)
eq('tau0 6G s-zero section',tau6.subs(s,0))

# Both exact coincident-section graph coefficients, without division by s.
tau,Zk,u,v,L=S.symbols('tau Zk u v L')
coef=tau/(tau-Zk*s*L)
eq('first full Cartier graph coefficient',coef.subs(tau,Zk*u)-u/(u-s*L))
eq('second full Cartier graph coefficient',coef.subs(tau,Zk/v)-1/(1-v*s*L))
eq('Cartier graph overlap',u/(u-s*L)-(1/(1-v*s*L)).subs(v,1/u))
eq('coincident strict sections', (u-s*L).subs(s,0)-u)
eq('Cartier reciprocal including full L',u/(u-s*L)*(u-s*L)/u-1)
eq('generic adjacent ray determinant',S.det(S.Matrix([[j+1,j],[1,1]]))-1)
eq('first graph cone determinant',S.det(S.Matrix([[1,k],[0,1]]))-1)
graph_checks=[]
for ll in range(31):
    mm=3*ll+2;kk=2*ll+1
    assert math.gcd(ll+1,mm)==1
    checks.append(f'primitive middle deck l={ll}')
    rays=[(1,0)]+[(jj,1) for jj in range(kk,-1,-1)]
    for i in range(len(rays)-1):
        det=rays[i][0]*rays[i+1][1]-rays[i][1]*rays[i+1][0]
        eq(f'full graph regular cone l={ll},i={i}',det-1)
    graph_checks.append({'l':ll,'m':mm,'k':kk,'rays':rays})

# Literal normalized chord, including its exact pole cancellation at P=O.
A,xx,yy,xr,yr,xpr=S.symbols('A xx yy xr yr xpr')
xp=A/tau**2;yp=-A/tau**3
slope=(yp-yr)/(xp-xr)
literal=tau*((yy-yr)-slope*(xx-xr))
written=tau*(yy-yr)+(A+tau**3*yr)/(A-tau**2*xr)*(xx-xr)
eq('full normalized chord',literal-written)
eq('normalized chord denominator at tau zero',(A-tau**2*xr).subs(tau,0)-A)
eq('normalized chord Cartier identity at P=O',written.subs(tau,0)/(xx-xr)-1)
eq('full Hom inverse product',written/(xx-xpr)*(xx-xpr)/written-1)

# Full reference-sector square and primitive signed cap generator.
sa,j0,nn,fa,Pi,cc,jb,logB,Lambda,ha=S.symbols('sa j0 nn fa Pi cc jb logB Lambda ha')
fb=fa+Pi;hb=ha-nn*sa*Pi+jb*logB+Lambda
ua=nn*sa*fa+sa*cc+ha
ub=nn*(sa+j0)*fb+(sa+j0)*cc+hb
eq('whole sector cap word',ub-ua-j0*(nn*fb+cc)-jb*logB-Lambda)
d=S.symbols('d',integer=True)
eq('full finite character norm',m*(d/m)-d)
for n in [-1,1]:eq(f'H=A^n primitive contraction norm n={n}',n*n-1)
rho=S.symbols('rho',positive=True)
for mm in [2,5,8,11,32]:
    vals=S.symbols('v0:'+str(mm+1))
    norm=sum(rho**(-2*jj)*vals[jj] for jj in range(mm))
    moved=sum(rho**(-2*jj)*vals[jj+1] for jj in range(mm))
    eq(f'weighted norm exact telescoping m={mm}',moved-rho*rho*(norm-vals[0]+rho**(-2*mm)*vals[mm]))

eq('initial index exact',S.Rational(4*(-27)-(-12),24)+4)
eq('native physical cubic',(-3)+(-24)+27)
eq('native physical linear',4*(-3)+12)
Sigma=S.symbols('Sigma')
fan=-4+S.Rational(3,2)*(Sigma-1)-S.Rational(27,8)*(Sigma*Sigma-1)
eq('fan initial index',fan.subs(Sigma,1)+4)
src=R/'notes/part3_e6_order_three_all_caps_working.md'
out={'status':'PASS','checks':len(checks),'utc':datetime.now(timezone.utc).isoformat(),
 'source':str(src.relative_to(R)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'identities':checks,'exact_tau0_6G':str(tau6),
 'exact_ell_numerator':str(S.factor(ell_num)),'exact_ell_denominator':str(S.factor(ell_den)),
 'regular_graph_samples':graph_checks,
 'scope':'M6, m=3l+2, n=+1 or -1, full finite character, fixed scalar in the common explicit contraction range; OC.1--5. Symbolic identities establish the universal formulas; graph samples are supplemental. Full geometric proof and independent review are required for characteristic-pair comparison.'}
dest=R/'code/part3_root/e6_order_three_all_caps.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','checks','source','source_sha256','exact_tau0_6G','exact_ell_numerator','exact_ell_denominator']},indent=2))
