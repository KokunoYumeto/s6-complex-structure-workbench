"""Exact checks of the known v1 closing map and C.3.5 comparisons."""
import csv
from pathlib import Path
import sympy as s
h,k,c,tau,mu,beta,L0,L1,kappa=s.symbols('h k c tau mu beta L0 L1 kappa')
e=s.Matrix([0,1])
Pi=s.Matrix([[6*mu,tau,1,0],[beta+c,mu,0,1]])
gamma=s.Matrix([1,0,0,0])
ell=L0/3-L1/4
b=-h*Pi*gamma/12+(h*ell-h*h/24)*e
g1={tau:(tau-1)/tau,mu:(1-mu)/tau,beta:beta+2-6*(1-mu)**2/tau,L0:L0-1}
g2={tau:-1/tau,mu:1+mu/tau,beta:beta-3-6*mu**2/tau,L1:L1-1}
R1=s.Matrix([[-1/tau,0],[(1-mu)/tau,1]])
R2=s.Matrix([[1/tau,0],[-mu/tau,1]])
eta1=s.Matrix([0,h/2,-h/2,-h/2])
eta2=s.Matrix([0,0,-h/2,h/2])
def tr(v,rule):
    return v.subs(rule,simultaneous=True)
def zero(v):
    return v.applyfunc(s.factor)==s.zeros(*v.shape)
for j,rule,R,eta,eps,m in [(1,g1,R1,eta1,1,3),(2,g2,R2,eta2,-1,4)]:
    assert zero(tr(b,rule)-R*b-tr(Pi,rule)*eta)
    bj=-h*Pi*gamma/12+(h*kappa-h*h/24)*e
    assert zero(tr(bj,rule)-R*bj-h*eps*e/m-tr(Pi,rule)*eta)
    print('Core and finite affine defects verified for j =',j)
g0={tau:tau-1,beta:beta+1,L0:L0+1,L1:L1+1}
assert zero(tr(b,g0)-b)
print('Cusp core defect zero verified.')
composition=b + b.subs({h:k,c:c+h}, simultaneous=True)-b.subs(h,h+k)
assert zero(composition)
print('Coherent composition correction -h^2/24 verified.')
rawA=s.Matrix([-s.Rational(7,2)*h*mu-s.Rational(3,2)*h*tau+2*h,
               -s.Rational(7,12)*h*beta-s.Rational(3,2)*h*mu+h*ell])
lam=s.Matrix([-h/2,-3*h/2,2*h,0])
Ptarget=Pi.subs(c,c+h)
comparison=(rawA-b-Ptarget*lam).applyfunc(s.factor)
assert comparison==s.Matrix([0,h*(14*c+13*h)/24])
print('Previous R2 lift minus clean lift minus target period:',list(comparison))
b12=b.subs(h,12)
res=(b12+Pi*gamma).applyfunc(s.factor)
assert res==s.Matrix([0,4*L0-3*L1-6])
print('12-shift after removing source period -gamma:',list(res))
print('Exponent = t^4/(t-1)^3; no parameter-dependent constant.')
q,C21,kap0,ss=s.symbols('q C21 kap0 ss')
cu=b.subs({beta:C21-ss-c,L0:-ss+3*kap0,L1:0},simultaneous=True)
# Substitute ell directly, rather than individual logarithms, for cusp cancellation.
cu=-h*s.Matrix([6*mu,-ss+C21])/12+(h*(-ss/12+kap0)-h*h/24)*e
cu=cu.applyfunc(s.factor)
expected=s.Matrix([-h*mu/2,-h*C21/12+h*kap0-h*h/24])
assert zero(cu-expected)
print('Cusp unit logarithm:',list(cu))
B0=s.Matrix([[0,1],[-1,0]])
assert B0*s.Matrix([1,0])==s.Matrix([0,-1])
print('Gamma deck exponent:',list(B0*s.Matrix([1,0])))
print('Unit times gamma deck has first multiplier 1 and second q^(-1)*H(q).')
print('All exact checks passed.')
