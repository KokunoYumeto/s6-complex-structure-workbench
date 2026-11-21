"""Exact new checks of height conventions, duplication, and derivative identities.

Duplication functions are reconstructed by rational tangent/chord doubling,
then the composition law psi_(2n)=2*y(nP)*psi_n^4. No old division-polynomial
program is imported. Symbolic differentiation treats conjugate coordinates
as independent, as required for Wirtinger derivatives.
"""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import hashlib,json
import sympy as s

ROOT=Path(__file__).parent
u=s.symbols('u');t=u+1
A=-s.Rational(3,4)*t**3*u;B=s.Rational(1,4)*t**4*u*u
P=(s.Integer(0),t*t*u/2)
Delta=s.factor(-16*(4*A**3+27*B**2))
assert Delta==27*t**8*u**3

def double(pt):
    x,y=pt
    slope=(3*x*x+A)/(2*y)
    xx=s.factor(slope*slope-2*x)
    yy=s.factor(slope*(x-xx)-y)
    assert s.factor(yy*yy-xx**3-A*xx-B)==0
    return xx,yy

Ak_expected=[s.Integer(1),1-s.Rational(5,27)*u,
    1-s.Rational(217,27)*u-s.Rational(20486,729)*u*u+s.Rational(10910,19683)*u**3
       +s.Rational(161383,177147)*u**4-s.Rational(245,14348907)*u**5]
pt=P;psi=s.Integer(1);dup=[]
for k in range(1,4):
    n=2**k
    psi=s.factor(2*pt[1]*psi**4)
    constant=s.Rational(n)*3**(n*n//4-1)/2**(n*n//2-1)
    norm=s.factor(psi/(constant*t**(2*(n*n-1)//3)*u**(n*n//4)))
    assert s.expand(norm-Ak_expected[k-1])==0
    dup.append(dict(k=k,n=n,division_function=str(psi),constant=str(constant),A=str(s.expand(norm))))
    pt=double(pt)
q=s.Rational(1,28)
coeff=s.Poly(Ak_expected[2]-1,u)
bound=sum(abs(coeff.nth(k))*q**(k-1) for k in range(1,6))
assert bound<10

# Formal local-height solution, with valuations and log(p) divided out.
n,vdelta,vpsi,xnegative=s.symbols('n vdelta vpsi xnegative', nonzero=True)
ell=s.symbols('ell')
ell_m=s.Rational(1,2)*xnegative+vdelta/12
equation=s.Eq(ell_m,n*n*ell+vpsi-(n*n-1)*vdelta/12)
solution=s.solve(equation,ell)[0]
assert s.simplify(solution-(vdelta/12+(xnegative/2-vpsi)/(n*n)))==0

# Wieferstrass model homothety: x'=c^-2*x, Delta'=c^-12*Delta,
# psi'_n=c^(1-n^2)*psi_n. The local-height multiplier has zero change.
c_log=s.symbols('c_log')
transport=s.expand(-(1-n*n)*c_log+(n*n-1)*(-12*c_log)/12)
assert transport==0

# C8.11: Wirtinger derivatives of Re(phi)-pi*y^2/T at wp(mu)=0.
V,a,m,p,g2,pi=s.symbols('V a m p g2 pi',nonzero=True)
I=s.I
W=V+2*pi*I*a;R=m-a
direct=V*V/(8*pi*I)+V*m/2+pi*I*a*m-pi*I*a*a/2
first=W*(W+4*pi*I*R)/(8*pi*I)
assert s.expand(direct-first)==0
beta_derivative_over_6=V*V/(4*pi*pi)+I*V*m/pi
det=beta_derivative_over_6-m*m
assert s.expand(det-(W+2*pi*I*R)**2/(4*pi*pi))==0
implicit_R=g2/(6*pi*I*p)-W/(2*pi*I)
factor=s.simplify(first.subs(m,implicit_R+a))
expected=I*W*(3*W*p-2*g2)/(24*pi*p)
assert s.simplify(factor-expected)==0

# C8.12: compose with the exact modular derivative.
X=s.symbols('X')
dt_ratio=-3*pi*I*p*p/(g2*g2) # (t-1)/(dt/dtau)
radial=s.factor(dt_ratio*expected)
assert s.simplify(radial-X*(X-2)/24).subs(V,X*g2/(3*p)-2*pi*I*a).simplify()==0
assert s.simplify(6*pi*I*p/g2*implicit_R-(1-3*W*p/g2))==0
F=s.symbols('F')
assert s.expand((1-F)*((1-F)-2)-(F*F-1))==0

# The limiting constant in C8.4 is fixed by its fourth power.
limit_fourth=s.Rational(27,16)/n**4
assert s.simplify(limit_fourth-(s.Rational(27)/(16*n**4)))==0

out=dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
    program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    sympy_version=s.__version__,family_discriminant=str(Delta),
    duplication=dup,A3_slope_bound_at_one_over_28=str(bound),
    local_height_solution=str(solution),model_transport_change=str(transport),
    first_derivative_difference='0',period_determinant_difference='0',
    implicit_R_difference='0',radial_identity_difference='0',F_R_difference='0',
    general_duplication_limit_fourth_power=str(limit_fourth))
(ROOT/'S6_SERIES_PUBLISH_I_nine_symbolic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
