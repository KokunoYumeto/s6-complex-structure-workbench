"""Exact division-polynomial evaluation at the elliptic section P.

Every non-special zero of a displayed primitive factor is a potential
regular-fibre resonance in the nonintegral Picard jump locus.
"""
from pathlib import Path
import sympy as S
import json
ROOT=Path(__file__).resolve().parents[1]
t=S.symbols('t')
A=-3*t**3*(t-1)
B=2*t**4*(t-1)**2
y=S.sqrt(2)*t**2*(t-1)
psi={0:S.Integer(0),1:S.Integer(1),2:2*y,
     3:-A**2,4:4*y*(-8*B**2-A**3)}
def f(n):
    if n in psi:return psi[n]
    if n%2:
        m=(n-1)//2
        ans=f(m+2)*f(m)**3-f(m-1)*f(m+1)**3
    else:
        m=n//2
        ans=f(m)/(2*y)*(f(m+2)*f(m-1)**2-f(m-2)*f(m+1)**2)
    psi[n]=S.factor(ans)
    return psi[n]
out={}
for n in range(2,13):
    value=S.factor(f(n))
    poly=S.Poly(value/S.sqrt(2) if n%2==0 else value,t)
    unit,fac=S.factor_list(poly.as_expr(),t)
    regular=S.Integer(1)
    for factor,power in fac:
        if S.degree(factor,t)>0 and factor not in [t,t-1]:regular*=factor**power
    regular=S.Poly(regular,t).monic().as_expr()
    out[str(n)]={'psi_n_at_P':str(value),'regular_factor_monic':str(regular),
                 'regular_factor_degree':S.degree(regular,t)}
    print(n,S.factor(regular))
(ROOT/'outputs/d_division_polynomials.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
