"""Outward-rounded constants for the local analytic proof at tau=i.
All estimates are proved by Cauchy, Rouche, and explicit Gaussian tails in
Statement C.2.4; this script evaluates their strict inequalities.
"""
import mpmath as m
v=m.iv;v.dps=60
pi=v.pi;T=v.mpf('0.9');Y=v.mpf('0.2');N=10
cosh=lambda x:(v.exp(x)+v.exp(-x))/2
A=[]
r=v.exp(-pi*T*(2*N+3)+2*pi*Y)
f=v.exp(-pi*T*(N+1)**2+2*pi*Y*(N+1))
tails=[f/(1-r),f*((N+1)/(1-r)+r/(1-r)**2),f*((N+1)**2/(1-r)+2*(N+1)*r/(1-r)**2+r*(1+r)/(1-r)**3)]
for k in range(3):A.append(sum(v.mpf(n)**k*v.exp(-pi*T*n*n)*cosh(2*pi*n*Y) for n in range(1,N+1))+tails[k])
a0=2*A[0];a1=4*pi*A[1];a2=8*pi*pi*A[2]
qr=v.exp(-2*pi*T)
MG=a2/(1-a0)+(a1/(1-a0))**2+pi*pi/3*(1+24*qr/(1-qr)**3)
MH=-v.ln(1-a0)+pi*v.mpf('1.1')/12+qr/(1-qr)**2
print('Uniform |G| bound',MG);print('Uniform |H| bound',MH)
assert MG.b<20;assert MH.b<v.mpf('.6')
q=v.exp(-2*pi)
E4=1+240*sum(v.mpf(n)**3*q**n/(1-q**n) for n in range(1,31))
# n^3 <= 31^3 * 2^(n-31) for n>=31, giving an elementary positive tail.
tail4=240*v.mpf(31)**3*q**31/((1-q)*(1-2*q))
E4+=v.mpf([0,tail4.b])
g2=4*pi**4/3*E4
q0=g2/4
# Independent differentiated theta-constant series for e2'(i), without a
# Ramanujan identity or reuse of the E4 value.
th2=2*sum(v.exp(-pi*(v.mpf(n)+v.mpf('.5'))**2) for n in range(21))
d2=2*pi*sum((v.mpf(n)+v.mpf('.5'))**2*v.exp(-pi*(v.mpf(n)+v.mpf('.5'))**2) for n in range(21))
th4=1+2*sum((-1)**n*v.exp(-pi*n*n) for n in range(1,21))
d4=2*pi*sum((-1)**n*n*n*v.exp(-pi*n*n) for n in range(1,21))
a=v.mpf('21.5');b=v.mpf(21)
e2=2*v.exp(-pi*a*a)/(1-v.exp(-44*pi));ed2=2*pi*a*a*v.exp(-pi*a*a)/(1-4*v.exp(-44*pi))
e4=2*v.exp(-pi*b*b)/(1-v.exp(-43*pi));ed4=2*pi*b*b*v.exp(-pi*b*b)/(1-4*v.exp(-43*pi))
th2+=v.mpf([0,e2.b]);d2+=v.mpf([0,ed2.b]);th4+=v.mpf([-e4.b,e4.b]);d4+=v.mpf([-ed4.b,ed4.b])
der=4*pi*pi/3*(th2**3*d2-th4**3*d4)
print('|Q(0,i)|',q0);print('|e2prime(i)| independent theta derivative',der)
print('Independent Eisenstein cross-check e2prime magnitude',g2/(6*pi))
assert q0.a>v.mpf('47.26');assert q0.b<v.mpf('47.30')
assert der.a>v.mpf('10.03');assert der.b<v.mpf('10.04')
eps=v.mpf('.00015');rh=v.mpf('.03');s=eps/v.mpf('.1');r2=(rh/v.mpf('.2'))**2
lower_boundary=(v.mpf('47.26')-500*r2/(1-r2))*rh*rh
variation=20*s/((1-s)*(1-r2))
print('Rouche lower',lower_boundary,'variation upper',variation)
assert lower_boundary.a>variation.b
Qerr=500*(r2+s/(1-s))/(1-r2)
Qlo=v.mpf('47.26')-Qerr;Qhi=v.mpf('47.30')+Qerr
elow=v.mpf('10.03')-2000*eps/(1-s);ehi=v.mpf('10.04')+2000*eps/(1-s)
rel=Qhi/elow;h2=ehi*eps/Qlo
print('Relation constant |tau-i|/|h|² upper',rel)
print('Root |h|² upper',h2)
assert rel.b<7;assert h2.b<v.mpf(1)/20000
coef=v.mpf('.6')*(70**2+25*70+25**2)/((1-s)*(1-v.mpf(25)/20000))+pi*7/(1-eps)
print('Quartic error coefficient',coef)
assert coef.b<5000
print('All local inequalities pass; norm²<2 except at tau=i.')
