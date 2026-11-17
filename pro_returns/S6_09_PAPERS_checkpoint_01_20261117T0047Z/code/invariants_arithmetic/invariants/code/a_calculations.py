"""Independent exact/local and high-precision computations for Part A.

Run from any directory. Numerical calculations use 100 decimal working digits.
Printed numerical agreement is corroboration, not an interval proof.
The nonvanishing proof is the exact geometric/modular argument in the paper.
"""
from pathlib import Path
import json
import mpmath as mp
import sympy as sp

OUT = Path(__file__).resolve().parents[1] / 'outputs'
OUT.mkdir(exist_ok=True)
lines = []
def say(x):
    lines.append(str(x))
    print(x, flush=True)

T, U, B, dt, du, db = sp.symbols('T U B dt du db')
Q = 6*du**2-dt*db
def differential(expr):
    return sum(sp.diff(expr,z)*dz for z,dz in [(T,dt),(U,du),(B,db)])
for name, transformed in [
    ('g1', ((T-1)/T,(1-U)/T,B+2-6*(1-U)**2/T)),
    ('g2', (-1/T,1+U/T,B-3-6*U**2/T)),
    ('g2_squared', (T,1-T-U,B+6*T+12*U-6)),
]:
    a,b,c=transformed
    target=Q if name=='g2_squared' else Q/T**2
    residual=sp.factor(6*differential(b)**2-differential(a)*differential(c)-target)
    assert residual==0
    say(f'covariance {name}: residual {residual}')

for m,a in [(3,2),(4,1),(9,6),(20,5)]:
    exponents={}
    for name,character in [('e0',0),('e1',a),('b0',0),('b1',-a),
                           ('e0b0',0),('e0b1',-a),('e1b0',a),('e1b1',0)]:
        exponents[name]=(-character)%m
    ordinary=a
    allowed=m-1
    twisted=min(r for r in range(-allowed,m) if (r-a)%m==0)
    assert twisted==a-m
    say(f'invariant lattice m={m}, a={a}: {exponents}; O((m-1)S) variable exponent {ordinary}->{twisted}')

x,y,z=sp.symbols('x y z')
v=sp.Matrix([y*z,x*z,x*y])
u=sp.Matrix([z,y,0]); vv=sp.Matrix([0,y,x])
test=sp.Matrix([[x*y,-x*z,y*z]])
assert test*u==sp.zeros(1,1) and test*vv==sp.zeros(1,1)
relations=[sp.Matrix([-x*z,-x*y,0]),sp.Matrix([y*z,0,-x*y]),sp.Matrix([0,y*z,x*z])]
assert relations==[-x*u,y*(u-vv),z*vv]
say('triple relative Omega^2 torsion presentation verified: x*u=0, y*(u-v)=0, z*v=0')

Cartan=sp.Matrix([[2,-1,0,0,0,0],[-1,2,-1,0,-1,0],
                  [0,-1,2,-1,0,0],[0,0,-1,2,0,0],
                  [0,-1,0,0,2,-1],[0,0,0,0,-1,2]])
assert Cartan.det()==3
assert Cartan.inv()[3,3]==Cartan.inv()[5,5]==sp.Rational(4,3)
say('E6 Cartan determinant = '+str(Cartan.det()))
say('E6 Cartan inverse = '+str(Cartan.inv()))
tt=sp.symbols('t')
AA=-3*tt**3*(tt-1); BB=2*tt**4*(tt-1)**2
P=(sp.Integer(0),sp.sqrt(2)*tt**2*(tt-1))
slope=AA/(2*P[1]); x2=sp.factor(slope**2); y2=sp.factor(-P[1]-slope*x2)
slope3=sp.factor((y2-P[1])/x2); x3=sp.factor(slope3**2-x2);y3=sp.factor(slope3*(P[0]-x3)-P[1])
assert sp.factor(y2**2-x2**3-AA*x2-BB)==0
assert sp.factor(y3**2-x3**3-AA*x3-BB)==0
assert sp.factor(x3-sp.Rational(16,81)*(tt-1)*(5*tt-32))==0
say('x(2P*) = '+str(x2));say('y(2P*) = '+str(y2))
say('x(3P*) = '+str(x3));say('x(3P*)(0) = '+str(x3.subs(tt,0)))

mp.mp.dps=100
I=mp.j
def sigma(n,k):
    return sum(d**k for d in range(1,n+1) if n%d==0)
def e4(tau,N=100):
    q=mp.exp(2*mp.pi*I*tau)
    return 1+240*sum(mp.mpf(sigma(n,3))*q**n for n in range(1,N+1))
def e6(tau,N=100):
    q=mp.exp(2*mp.pi*I*tau)
    return 1-504*sum(mp.mpf(sigma(n,5))*q**n for n in range(1,N+1))
Ei=mp.re(e4(I))
fourier=mp.sqrt(mp.mpf(2)/3)/(mp.pi*mp.root(Ei,4))
Kquad=mp.quad(lambda theta: 1/mp.sqrt(1-mp.sin(theta)**2/2),[0,mp.pi/4,mp.pi/2])
period=mp.sqrt(2)*Kquad/mp.root(3,4)
abel=mp.sqrt(2)/(3*period)
gamma=4*mp.sqrt(mp.pi)/(mp.power(3,mp.mpf(3)/4)*mp.gamma(mp.mpf(1)/4)**2)
hyper=mp.sqrt(6)/(3*mp.pi*mp.hyper([mp.mpf(1)/12,mp.mpf(5)/12],[1],1))
say('working decimal precision = 100')
say('mu_s_prime = i times the following positive number')
for name,val in [('E4 Fourier',fourier),('Abel-period quadrature',abel),('gamma',gamma),('Duke-Imamoglu hypergeometric',hyper)]:
    say(name+': '+mp.nstr(val,85))
say('Fourier vs quadrature absolute discrepancy: '+mp.nstr(abs(fourier-abel),5))
say('real period Omega_R: '+mp.nstr(period,85))
say('E4(i): '+mp.nstr(Ei,85))

# Independent Newton solutions of the Weierstrass Fourier expansion.
# For positive s, j(tau)=1728(1+s^4), tau=iy with y>1.
# The two local branches have the same limiting half period and opposite
# linear terms. Their difference removes the even terms.
def wp(zeta,tau,N=100):
    q=mp.exp(2*mp.pi*I*tau)
    return mp.pi**2/mp.sin(mp.pi*zeta)**2-mp.pi**2/3+8*mp.pi**2*sum(n*q**n/(1-q**n)*(1-mp.cos(2*mp.pi*n*zeta)) for n in range(1,N+1))
def wp_z(zeta,tau,N=100):
    q=mp.exp(2*mp.pi*I*tau)
    return -2*mp.pi**3*mp.cos(mp.pi*zeta)/mp.sin(mp.pi*zeta)**3+16*mp.pi**3*sum(n*n*q**n/(1-q**n)*mp.sin(2*mp.pi*n*zeta) for n in range(1,N+1))
for exponent in [5,10,15]:
    s=mp.mpf(10)**(-exponent)
    ratio=s*s/mp.sqrt(1+s**4)
    yy=mp.findroot(lambda yy:mp.re(e6(I*yy)/e4(I*yy)**mp.mpf('1.5'))-ratio,
                   (1+s*s/(mp.pi*mp.sqrt(Ei)),1+2*s*s/(mp.pi*mp.sqrt(Ei))),tol=mp.mpf('1e-95'))
    tau=I*yy
    middle=(1-tau)/2
    roots=[]
    for sign in [1,-1]:
        zz=middle+sign*I*fourier*s
        for it in range(12):
            step=wp(zz,tau)/wp_z(zz,tau)
            zz-=step
            if abs(step)<mp.mpf('1e-80'):break
        roots.append(zz)
    estimate=(roots[0]-roots[1])/(2*s)
    say(f'Newton s=1e-{exponent}: mu derivative estimate '+mp.nstr(estimate,70))
    say('  error vs scalar '+mp.nstr(abs(estimate-I*fourier),8)+'; max wp residual '+mp.nstr(max(abs(wp(r,tau)) for r in roots),8))

# Check the literal Duke--Imamoglu branch, rather than its derivative only.
for height in [mp.mpf('1.25'),mp.mpf('1.5')]:
    tau=I*height
    EE4=e4(tau);EE6=e6(tau)
    xx=EE6**2/EE4**3
    mu_hyper=(1-tau)/2+I*mp.sqrt(6)/(3*mp.pi)*mp.root(xx,4)*mp.hyper(
        [mp.mpf(1)/3,mp.mpf(2)/3,1],[mp.mpf(3)/4,mp.mpf(5)/4],xx)/mp.hyper(
        [mp.mpf(1)/12,mp.mpf(5)/12],[1],1-xx)
    zz=mp.mpf('0.5')-mp.mpf('0.4')*I
    for it in range(30):
        step=wp(zz,tau)/wp_z(zz,tau)
        zz-=step
        if abs(step)<mp.mpf('1e-90'):break
    say('literal DI branch tau='+mp.nstr(tau,5)+': '+mp.nstr(mu_hyper,75))
    say('  independent Newton disagreement '+mp.nstr(abs(mu_hyper-zz),8)+
        '; wp residual '+mp.nstr(abs(wp(mu_hyper,tau)),8))

rho=mp.exp(mp.pi*I/3)
E6rho=e6(rho)
qtheta=mp.exp(mp.pi*I*rho)
th2=mp.jtheta(2,0,qtheta);th3=mp.jtheta(3,0,qtheta);th4=mp.jtheta(4,0,qtheta)
E6theta=(th2**4+th3**4)*(th3**4+th4**4)*(th4**4-th2**4)/2
lam=3*mp.exp(5*mp.pi*I/6)/(2*mp.pi*mp.root(mp.re(E6rho),3))
lam2=3*mp.exp(5*mp.pi*I/6)/(2*mp.pi*mp.root(mp.re(E6theta),3))
coef=-3*I*lam/(2*mp.pi)
coef2=-3*I*lam2/(2*mp.pi)
say("order-three coordinate r^3=t, tau'(0) along unit-circle branch: "+mp.nstr(lam,80))
say('K_r/r^2 coefficient (Fourier): '+mp.nstr(coef,80))
say('K_r/r^2 coefficient (theta): '+mp.nstr(coef2,80))
say('order-three coefficient discrepancy: '+mp.nstr(abs(coef-coef2),5))
say('exact orders: ord_r K=2; ord_s K=0; coarse det(kappa0) orders (p0,p1,p2)=(0,1,1)')

(OUT/'a_calculations.txt').write_text('\n'.join(lines)+'\n')
(OUT/'a_numeric_values.json').write_text(json.dumps({'working_dps':100,'mu_prime_imaginary':mp.nstr(fourier,85),'period_real':mp.nstr(period,85),'order_three_K_coefficient_real':mp.nstr(mp.re(coef),85),'order_three_K_coefficient_imag':mp.nstr(mp.im(coef),85),'numerical_claim':'Numerical corroboration; nonvanishing proved analytically, not by numerical interval certification.'},indent=2)+'\n')
