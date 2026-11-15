"""Exact Bernstein certificate for the one-variable Cayley majorant."""
import sympy as s
from pathlib import Path
r,x=s.symbols('r x');sq=s.sqrt(3);r0=2-sq;cc=1-1/sq;k=s.Rational(72,5);kap=1+2/sq
U=1/sq+s.Rational(13,200)*k*r*r
V=1+s.Rational(7,50)*k*r*r
H=1+s.Rational(113,1000)*k*r*r
Den=(1+r)**2*(1+r/r0)**2
P=s.Poly(s.expand((1-U)**2*Den-V**2*(cc**2*H**2+4*kap*r*(cc+kap*r*r)*k*k*r**4*s.Rational(13,100)**2*Den)),r,extension=sq)
assert P.eval(0)==0
Q=s.Poly(P.as_expr()/r,r,extension=sq)
# Bernstein coefficients after r=r0*x, 0<=x<=1
n=Q.degree();coeff=[s.simplify(Q.nth(j)*r0**j) for j in range(n+1)]
bern=[s.simplify(sum(coeff[j]*s.Rational(s.binomial(i,j),s.binomial(n,j)) for j in range(i+1))) for i in range(n+1)]
print('degree',n)
print('power coefficients Q:')
for j in range(n+1):print(j,Q.nth(j))
print('Bernstein coefficients, exact and decimal:')
for j,b in enumerate(bern):print(j,b,s.N(b,25))
print('min',min(s.N(b,30) for b in bern))
