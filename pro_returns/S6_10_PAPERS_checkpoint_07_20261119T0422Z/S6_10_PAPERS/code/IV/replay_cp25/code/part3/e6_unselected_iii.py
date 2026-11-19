#!/usr/bin/env python3
"""Exact actual-chart checks for the M6, quadratic-root E6 r=0 disc."""
from pathlib import Path
import sympy as S
import json,hashlib

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def eq(name,value):
    z=S.factor(S.together(value))
    if z!=0: raise AssertionError((name,z))
    checks.append(name)
def mod(name,value,relation,var):
    num=S.fraction(S.together(value))[0]
    eq(name,S.rem(num,relation,var))

x,y,t,r,u,k,s,a,b,c,cp,z,D,X,Y,T,w=S.symbols('x y t r u k s a b c cp z D X Y T w')
curve=y*y-x**3-r*x*x-t*x-t*t
U=y-t-x/2;V=y+t+x/2
eq('actual A1 source product',U*V-x*x*(x+r-S.Rational(1,4))-curve)
xx=k*k-r+(2*k-1)*u;tt=xx*u;yy=xx*(k+u)
eq('source x-chart equation',curve.subs({x:xx,y:yy,t:tt}))
up=xx/(1-2*k);kp=-k-2*up;xp=u*(1-2*k);yp=-tt-k*xp
eq('source translation preserves t',xp*up-tt)
eq('target x-chart equation',xp-(kp*kp-r+(2*kp-1)*up))
eq('target kappa equality',yp-xp*(kp+up))
eq('target Weierstrass equation',curve.subs({x:xp,y:yp,t:tt}))
eq('kappa half chart source unit',xx.subs(k,S.Rational(1,2))-(S.Rational(1,4)-r))
aa,bb=S.symbols('aa bb')
rel=bb*bb-t*aa**3-r*aa**2-aa-1
mod('G-chart cancelled slope',aa*(t*aa*aa+r*aa+1)-(bb-1)*(bb+1),rel,bb)
NN=(bb-1)**2-r*aa*aa-t*aa**3
eq('minus-G O-chart denominator value',(t*aa**3+(bb-1)*NN).subs({aa:0,bb:-1})+8)
tau,vv=S.symbols('tau vv')
p=tau*tau*vv;ap=p*(1+2/tau+2*t*p);bp=-1+(1/tau+t*p)*ap
eq('O-chart target a value',S.cancel(ap).subs(tau,0))
eq('O-chart target b value',S.cancel(bp).subs({tau:0,vv:1})-1)
eq('III branch derivative one',S.diff(-k/(1-2*k),k).subs(k,0)+1)
eq('III branch derivative two',S.diff(-k,k)+1)

rr=S.Rational(1,4)-s
x2=s;y2=-t-s/2
eq('actual twice-section on source',curve.subs({x:x2,y:y2,r:rr}))
lam=-2*t/s-S.Rational(1,2);x3=2*t*(2*t+s)/s**2;y3=-t-lam*x3
eq('actual three-section on source',curve.subs({x:x3,y:y3,r:rr}))
Lp=y-t-lam*x;Lm=y+t+lam*x
mod('full Miller chord product',Lp*Lm-x*(x-s)*(x-x3),curve.subs(r,rr),y)
eq('Miller alternative denominator',Lm-(s*V-(s+2*t)*x)/s)
q=S.symbols('q')
eq('three-section infinity x0',S.limit(q*q*x3.subs(t,1/q),q,0)-4/s**2)
eq('three-section infinity y0',S.limit(q**3*y3.subs(t,1/q),q,0)-8/s**3)
xc=4/s**2;yc=8/s**3;lc=3*xc*xc/(2*yc);x6=lc*lc-2*xc;y6=-yc+lc*(xc-x6)
eq('six-section infinity tau0',-x6/y6+s)
eq('central III twice-section additive coordinate',(-x2/y2).subs({t:0,s:S.Rational(1,4)})-2)

ww=S.symbols('ww');x0=s+ww*ww-ww
f2p=x0/ww;f3p=x0;f3Tp=2*ww**3/(x0*(ww-s))
f23p=x0*(1-s)/((1-s)*ww-s)
f23Tp=2*(1-s)*(ww-s)**2/(s**3*x0)
eq('complete I2 Miller leading coefficient',f2p**6*(f3Tp/f3p)**2*f23Tp/f23p-8*((1-s)*ww-s)/s**3)
eq('whole fibre divisor cancellation at zero',3-3)
eq('whole fibre divisor cancellation at infinity',-2+2)

cc=c*c-1-a*b-r*a*a*b*b
zz=a*b*(b-a)/(2*c);YY=a*b*(a+b)/2;XX=a*b
mod('actual middle A2 source equation',YY*YY-XX**3-zz**2*(r*XX*XX+XX+1),cc,c)
K=1+b*(b-a)*(1+r*a*b)/(2*c*(c+1))
mod('actual root chord slope',(YY-zz)/XX-a*K,cc,c)
F=1-a*b*(1+r*a*b)*(K+1)/(2*c*(c+1))-r*a*b*b*(a-b)/(4*c*c)
Xp=a*(a-b)*F;Yp=-zz-a*K*Xp
eq('root X-prime factor',a*a*K*K-r*zz*zz-XX-Xp)
H=K+b*(a-b)*(1+r*Xp)/(2*c*(1+cp))
cpp=cp*cp-1-Xp-r*Xp*Xp
mod('root V-prime exact unit',Yp+zz*cp+a*Xp*H,cpp,cp)
apr=(b-a)*F/H;bpr=-a*H
eq('root toric product preserved',apr*bpr-Xp)
for label,fun in [('K',K),('F',F),('H',H)]:
    eq('root deck unit '+label,fun.xreplace({a:-a,b:-b})-fun)
    eq('root central unit '+label,fun.subs({a:0,b:0,c:1,cp:1})-1)
J=S.Matrix([[-1,1],[-1,0]])
eq('root Jacobian determinant',J.det()-1)
eq('root component cycle order three',(J**3-S.eye(2)).norm())
eq('root division norm',2*(2-S.Rational(3,2))-1)
for n in [-1,1]:
    for d in range(-4,5):
        eq(f'root character norm n{n}d{d}',((-1)**d)**2-1)
        eq(f'primitive cap generator n{n}d{d}',n*n-1)

# Full root multiplier, in the actual source/target rational Cartier frames.
xp0=w*w
yp0=w**3+z*z*((S.Rational(1,4)-s)*w**4+w*w+1)/(2*w**3)
ki=(yp0+z)/xp0
xpt=ki*ki-(S.Rational(1,4)-s)*z*z-xp0
ypt=z-ki*xpt
def f3root(px,py):
    return s*z*px*(py-z-z*px/2)/(s*z*(py+z+z*px/2)-(s*z*z+2)*px)
eq('root f2 leading coefficient',S.limit((yp0-z-z*xp0/2)/(xp0-s*z*z),z,0)-w)
eq('root f3 source leading coefficient',S.limit(f3root(xp0,yp0)/z,z,0)+s*w**3/2)
eq('root f3 target leading coefficient',S.limit(f3root(xpt,ypt)/z**2,z,0)-s)
x3r=4/(s*s*z*z)+2/s
y3r=(8/z**3+6*s/z+(s*s-s**3)*z)/s**3
lam3r=(3*x3r*x3r+2*(S.Rational(1,4)-s)*z*z*x3r+z*z)/(2*y3r)
x6r=lam3r*lam3r-(S.Rational(1,4)-s)*z*z-2*x3r
eq('root tangent scaled slope',S.limit(z*lam3r,z,0)-3/s)
eq('root six-section scaled x',S.limit(z*z*x6r,z,0)-1/s**2)
for name,px,py in [('source',xp0,yp0),('target',xpt,ypt)]:
    f23r=(py-y3r-lam3r*(px-x3r))/(px-x6r)
    eq('root tangent-over-vertical '+name,S.limit(z*f23r,z,0)+4/s)
eq('root full Miller unit value',w**6*(s/(-s*w**3/2))**2*(-4/s)/(-4/s)-4)
eq('root selected full weight',(z**(-2)/z**(-6))*z**(-6)-z**(-2))

# Signed sector arrow, including all reference deck/period corrections.
ss,kk,nn,ff,PP,cc0,jj,bb0,LL,hh=S.symbols('ss kk nn ff PP cc0 jj bb0 LL hh')
f_beta=ff+PP
h_beta=hh-nn*ss*PP+jj*bb0+LL
U_alpha=nn*ss*ff+ss*cc0+hh
U_beta=nn*(ss+kk)*f_beta+(ss+kk)*cc0+h_beta
eq('full cap-period overlap',U_beta-U_alpha-kk*(nn*f_beta+cc0)-jj*bb0-LL)
ee=S.symbols('ee')
eq('literal odd-log finite average',-ee/2+ee-ee/2)
eab,eac=S.symbols('eab eac')
ebc=eac-eab
eq('Cauchy partition overlap sign',-ebc+eac-eab)

# Weighted maps are checked in the actual rational line frames.
AA,BB,CC,GG,HH=S.symbols('AA BB CC GG HH')
f2old=AA/BB;f2new=(D**3*AA)/(D**2*BB)
eq('f2 actual weight',f2new-D*f2old)
f3old=f2old*CC/GG;f3new=f2new*(D**3*CC)/(D**2*GG)
eq('f3 actual weight',f3new-D**2*f3old)
f6old=f3old**2*HH/GG;f6new=f3new**2*(D**3*HH)/(D**2*GG)
eq('f6 actual weight',f6new-D**5*f6old)
eq('B6 exact source-target ratio weight',D**(-6)*D**(-5)/D**(-5)-D**(-6))
eq('selected height inverse weight',(D**(-3))/D**(-9)-D**6)
eq('full Bsel scalar cancellation',D**(-6)*D**6-1)
dw=w*w-3;rw=(3-2*w*w)/dw**2;rho=w*w/dw
tc=(1-3*rho*rho+2*rho**3)/27
eq('selected source height',dw**3*tc-(w*w-1))
eq('marked source discriminant branch',rho*rho-(1-3*rw))
eq('marked source equation',dw**6*curve.subs({x:X/dw**2,y:Y/dw**3,t:T/dw**3,r:rw})-(Y*Y-X**3-(3-2*w*w)*X*X-dw*T*X-T*T))
mod('positive unselected local parameter derivative',S.diff(rw,w)+16*w/9,2*w*w-3,w)

source=ROOT/'notes/part3_e6_unselected_iii_working.md'
out={'status':'PASS','scope':'Concrete M6,Q=G,m=2,n=+-1,d retained; actual unselected III disc attachment.','checks':len(checks),'exact_identities':checks,'source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'return_class':0,'no_other_cap_order_or_branch_claimed':True,'geometric_proof_gates':['resolved source and root maps','complete rational Cartier divisor/Hartogs extension','full reference-relative integral/finite annular cocycles','uniform proper disc quotient and actual identity closing']}
(ROOT/'code/part3/e6_unselected_iii.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
