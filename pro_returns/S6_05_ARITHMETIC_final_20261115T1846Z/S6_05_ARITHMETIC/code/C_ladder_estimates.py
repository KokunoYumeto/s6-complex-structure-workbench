#!/usr/bin/env python3
"""Explore scalar majorants for a proof with explicit analytic inequalities.
These floating evaluations are diagnostics, not certificates.
"""
import json
from pathlib import Path
import mpmath as m
from fractions import Fraction as F
m.mp.dps=60
p=m.pi
def supbound(a,b):
    f=lambda T:m.exp(p*T/12)*(1+2*m.exp(-p*T)/(1-m.exp(-3*p*T)))
    r=m.exp(-2*p*a)
    return max(f(a),f(b))*m.exp(r/(1-r)**2)
for a,b in [(m.sqrt(3)/2,1),(1,2),(m.sqrt(3)/2,m.mpf('1.4')),(m.sqrt(3)/2,m.mpf('1.1'))]:
    print('T interval',a,b,'supnorm bound',supbound(a,b))
data=json.loads(Path(__file__).resolve().parent.parent.joinpath('records/C_ladder_polynomials.json').read_text())
radii={1:F(9,10),2:F(1,28),3:F(1,500),4:F(1,8000),5:F(1,128000)}
for k in range(2,6):
    c=[F(x) for x in data[str(k)]['coefficients']]
    print('STEP',k)
    for r in [radii[k],radii[k-1]]:
        major=sum(abs(c[i])*r**i for i in range(1,len(c)))
        lower=1-major
        sup=m.mpf('1.5') if k==2 else m.mpf('1.43')
        target=(m.mpf(3)**(m.mpf(3)/4)/2**(k+1)*sup)**4
        val=m.mpf(lower.numerator)/lower.denominator*(m.mpf(r.numerator)/r.denominator)**m.mpf('.25')
        print('r',r,'lower',m.mpf(lower.numerator)/lower.denominator,'lhs',val,'rhs',target**m.mpf('.25'))
    # A single rational linear bound over the whole disc, rounded upward.
    r=radii[k-1]
    slope=sum(abs(c[i])*r**(i-1) for i in range(1,len(c)))
    bound=(slope.numerator+slope.denominator-1)//slope.denominator
    print('uniform linear slope bound',bound)
    # A more transparent coefficient estimate: first 4 coefficients plus
    # a geometric tail majorant with a displayed coefficient ratio.
    ratios=[abs(c[i+1]/c[i]) for i in range(4,len(c)-1) if c[i] and c[i+1]]
    print('tail ratio max (after degree4)',float(max(ratios)) if ratios else 0)
