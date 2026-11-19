#!/usr/bin/env python3
"""Fresh exact checks of ARI C.2.1 and C.3.1--2.

Written from the frozen prereading derivation, without opening the programs
that produced the paper. Uses a differential polynomial vector field and
exact real polynomial identities, rather than fitted theta evaluations.
"""
import json
from pathlib import Path
import sympy as s

I, pi = s.I, s.pi
E, A, B, p, H, e = s.symbols('E A B p H e')
G, T, p0 = s.symbols('G T p0', nonzero=True)
delta, h, w = s.symbols('delta h w')
field = {
    E: I*(E**2-A/12)/(2*pi),
    A: I*(2*E*A-3*B)/pi,
    B: I*(3*E*B-A**2/6)/pi,
    p: I*(3*E*p/2+A**2/(12*p))/pi,
    H: I*p/(4*pi)+I*E*A/(6*pi*p),
}
def D(f, extra=None):
    v=field.copy()
    if extra:v.update(extra)
    return s.factor(sum(s.diff(f,x)*y for x,y in v.items()))
checks=[]
def check(name, got, expected=0):
    residual=s.simplify(s.factor(s.expand(got-expected)))
    assert residual == 0, (name,residual)
    checks.append({'name':name,'value':str(s.factor(got)),'expected':str(expected),'residual':'0'})

# Check the quoted Ramanujan equations by a separately generated q-series.
N=80
def series(k,m):
    return [1]+[m*sum(d**k for d in range(1,n+1) if n%d==0) for n in range(1,N+1)]
def mul(a,b):return [sum(a[j]*b[n-j] for j in range(n+1)) for n in range(N+1)]
qE2,qE4,qE6=series(1,-24),series(3,240),series(5,-504)
for label,seq,left,right,den in [
    ('E2',qE2,mul(qE2,qE2),qE4,12),
    ('E4',qE4,mul(qE2,qE4),qE6,3),
    ('E6',qE6,mul(qE2,qE6),mul(qE4,qE4),2)]:
    assert all(den*n*seq[n]==left[n]-right[n] for n in range(N+1))
    checks.append({'name':'Ramanujan '+label,'exact_coefficients_checked':N+1,'residuals':'all zero'})

check('nome relation',-w**2/s.Integer(48)**3,s.Rational(27,64)*(I*w/216)**2)
check('family versus continuation squared radii',s.Rational(216**2,48**3),s.Rational(27,64))
check('root cubic constraint preserved',D(p**2+B),3*I*E*(p**2+B)/pi)

# Implicit half-period root. This uses the cubic, without theta fitting.
ep=s.factor((field[A]*e+field[B])/(12*e**2-A))
sq={E:pi,A:G,B:0,e:0}
ep0=s.factor(ep.subs(sq))
epp0=s.factor(D(ep,{e:ep}).subs(sq))
Ap0=field[A].subs(sq)
check('square e prime',ep0,I*G/(6*pi))
check('square e double prime',epp0,-G/(2*pi))
check('square g2 prime',Ap0,2*I*G)
a=s.factor(G/(4*ep0))
b=s.factor((Ap0*a/4-epp0*a**2/2)/ep0)
check('delta h2 coefficient',a,-3*pi*I/2)
check('delta h4 coefficient',b,-9*pi**2*I/8)
aa=s.factor(1/a);bb=s.factor(-b/a**3)
check('inverse h2 delta coefficient',aa,2*I/(3*pi))
check('inverse h2 delta2 coefficient',bb,1/(3*pi))
check('square root correction',bb/(2*aa),-I/4)

Ep0=field[E].subs(sq)
Fhh_tau=-ep0-Ep0
Ftau_tau=I*ep0/(4*pi)
quartic=s.factor(G/48+Fhh_tau*a/2+Ftau_tau*a**2/2)
check('holomorphic quartic',quartic,-3*pi**2/8-5*G/192)
x,y,GG=s.symbols('x y GG',real=True)
z=x+I*y
realhol=s.re(-pi*z**2/2+quartic.subs(G,GG)*z**4).expand()
metric=-pi*y**2+pi*y**2*s.im(a*z**2).expand()
target=-pi*(x*x+y*y)/2+3*pi**2*(x*x+y*y)**2/8-3*pi**2*(x*x+y*y)*(x*x-y*y)/4-5*GG*s.re(z**4).expand()/192
check('complete square norm polynomial',realhol+metric,target)
# The inversion is expressed in independent real invariants r=|delta|,
# v=Im(delta), q=Re(delta^2); all retained total degrees are explicit.
r,v,q=s.symbols('r v q',real=True)
Ldelta=(-pi/2)*(2*r/(3*pi))*(1+v/2) + (3*pi**2/8)*(4*r**2/(9*pi**2)) - (3*pi**2/4)*(2*r/(3*pi))*(-2*v/(3*pi)) - (5*G/192)*(-4*q/(9*pi**2))
check('D_part square expansion',6*Ldelta/pi,-2*r/pi+(r*r+r*v)/pi+5*G*q/(72*pi**3))

# Smooth root at rho; differentiate the algebraic vector field exactly.
rho={E:pi/T,A:0,B:-p0**2,p:p0,H:2*pi*I/3}
mup=I*H/(2*pi)-I*A/(6*pi*p)
mu2=D(mup);mu3=D(mu2)
check('rho mu prime',mup.subs(rho),-s.Rational(1,3))
check('rho mu double prime',mu2.subs(rho),3*p0/(8*pi**2))
check('rho mu third derivative',mu3.subs(rho),9*I*p0/(16*pi**2*T))
A1=s.factor(field[A].subs(rho));A2=s.factor(D(field[A]).subs(rho));B1=s.factor(field[B].subs(rho))
check('rho g2 prime',A1,3*I*p0**2/pi)
check('rho g2 double prime',A2,-15*p0**2/(pi*T))
check('rho g3 prime',B1,-3*I*p0**2/T)
B0=-p0**2
t3=s.factor(A1**3/(-27*B0**2))
t4=s.factor(t3*(3*A2/(2*A1)-2*B1/B0))
check('t cubic coefficient',t3,I*p0**2/pi**3)
check('t quartic over cubic',t4/t3,3*I/(2*T))
K1=I*p0/(4*pi)
twodL=s.factor(I*K1**2/(4*pi)-I*K1*A1/(6*pi*p0))
check('2 dL harmonic quadratic',twodL,7*I*p0**2/(64*pi**3))
check('harmonic t coefficient',(twodL/3)/t3,s.Rational(7,192))
Pabs=s.symbols('Pabs',positive=True)
radial=-pi*(3*Pabs/(16*pi**2))**2/(2*T)
check('rho radial delta quartic',radial,-9*Pabs**2/(512*pi**3*T))
check('rho radial t coefficient',s.factor(radial*pi**4/Pabs**s.Rational(8,3)),-9*pi/(512*T*Pabs**s.Rational(2,3)))
check('D_part rho linear',6*s.Rational(7,192)/pi,7/(32*pi))
check('D_part rho radial',6*(-9*pi/(512*T*Pabs**s.Rational(2,3)))/pi,-27/(256*T*Pabs**s.Rational(2,3)))

# Exact CM lattice morphism used for H(mu0,rho).
rho0=(1+I*s.sqrt(3))/2
omega=rho0-1;mu0=(2-rho0)/3
check('CM order-three lattice map',s.expand(omega*mu0-mu0),rho0-1)
check('CM zeta solution',s.expand((1/omega-1)*(rho0+1)/3),-rho0)
check('CM logarithmic theta derivative',s.expand((rho0+1)/3-mu0),(2*rho0-1)/3)

out={'status':'PASS','method':'Exact SymPy differential-polynomial jets, real polynomial comparison and independently generated divisor q-series','sympy_version':s.__version__,'old_producing_code_read':False,'number_of_checks':len(checks),'checks':checks}
path=Path(__file__).with_suffix('.output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
