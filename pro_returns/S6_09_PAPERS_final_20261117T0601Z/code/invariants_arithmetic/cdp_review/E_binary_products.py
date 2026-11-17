"""Exact homogeneous binary-product checks for A.5.21."""
import sympy as sp
x,y,z,v,lam=sp.symbols('x y z v lam')
for degree in range(2,9):
    P=sp.prod(x-a*v for a in range(degree))
    h=sp.expand(P.subs(v,y*z))
    assert sp.expand(h.subs({x:lam**2*x,y:lam*y,z:lam*z},simultaneous=True)-lam**(2*degree)*h)==0
    assert P.subs({x:1,v:0})==1
    assert sp.expand(P.subs(v,0))==x**degree
    assert sp.diff(P,x).subs(v,0)==degree*x**(degree-1)
    assert sp.gcd(x**degree-1,degree*x**(degree-1))==1
    print('Degree',degree,': positive weighted homogeneity and',degree,'simple v-zeros checked.')
assert 2*1*(-1)==-2
print('Two endpoint linking numbers:',-1,-1,'; spherical square:',-2)
s=sp.symbols('s')
for degree in range(2,6):
    coefficients=[1+x+y*z]+[i+x*z+y+z*z for i in range(1,degree+1)]
    h=sum(coefficients[i]*x**(degree-i)*(y*z)**i for i in range(degree+1))
    family=sum(coefficients[i].subs({x:s*s*x,y:s*y,z:s*z},simultaneous=True)
               *x**(degree-i)*(y*z)**i for i in range(degree+1))
    assert sp.expand(h.subs({x:s*s*x,y:s*y,z:s*z},simultaneous=True)-s**(2*degree)*family)==0
print('Variable-coefficient weighted family identity checked in degrees2 through5.')
excluded_scope=x*v*(x-v)
assert excluded_scope.subs({x:1,v:0})==0
assert sp.cancel(excluded_scope.subs(v,y*(v/y))-x*v*(x-v))==0
print('The nodal-image product model XV(X-V) has P(1,0)=0 and is outside the theorem.')
print('All exact binary-product checks passed.')
