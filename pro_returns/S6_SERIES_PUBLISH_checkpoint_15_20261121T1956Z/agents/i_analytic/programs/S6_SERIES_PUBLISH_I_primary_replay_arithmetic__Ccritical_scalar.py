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
lo=s.Rational('1.73205080756887729352744634150587236694280525381038')
hi=s.Rational('1.73205080756887729352744634150587236694280525381039')
assert lo*lo<3<hi*hi
lowers=[169,175,181,187,192,197,202,205,207,207,204,197,184,160,118]
for i,(v,L) in enumerate(zip(bern,lowers)):
 pol=s.Poly(v,sq);aa=pol.nth(0);bb=pol.nth(1)
 certified=aa+bb*(lo if bb>=0 else hi)
 assert certified>s.Rational(L,100)
print('Exact lower bounds: ',lowers,' divided by 100')
print('ALL EXACT BERNSTEIN COMPARISONS PASSED')
import json
Path(__file__).resolve().parents[1].joinpath('records/Ccritical_scalar.json').write_text(json.dumps({'degree':n,'bernstein':[str(v) for v in bern],'rational_lower_numerators':lowers,'rational_lower_denominator':100},indent=2)+'\n')
