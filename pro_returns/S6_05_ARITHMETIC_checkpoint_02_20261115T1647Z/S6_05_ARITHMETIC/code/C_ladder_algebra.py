#!/usr/bin/env python3
"""Exact central division-polynomial normalization for the analytic ladder.

The output is algebraic data, not a numerical inequality certificate.
"""
from pathlib import Path
import json
import sympy as s
from Cspecial_division import psi,t

u=s.symbols('u')
out={}
for k in range(1,6):
    n=2**k
    print('starting n',n,flush=True)
    raw=s.cancel(psi(n)/(t**(2*(n*n-1)//3)*(t-1)**(n*n//4)))
    q=s.Poly(raw,t)
    c=q.eval(1)
    A=s.Poly(s.expand(q.as_expr().subs(t,1+u)/c),u)
    coeff=[A.nth(i) for i in range(A.degree()+1)]
    print('n',n,'degree',A.degree(),'central coefficient',c,flush=True)
    print('first coefficients',coeff[:8],flush=True)
    out[k]={'n':n,'c':str(c),'coefficients':[str(x) for x in coeff]}
    for r in [s.Rational(9,10),s.Rational(1,28),s.Rational(1,500),s.Rational(1,8000),s.Rational(1,128000)]:
        M=sum(abs(coeff[i])*r**(i-1) for i in range(1,len(coeff)))
        print('r',r,'majorant derivative',float(M),'lower',float(1-r*M),flush=True)
    Path(__file__).resolve().parent.parent.joinpath('records/C_ladder_polynomials.json').write_text(json.dumps(out,indent=2)+'\n')
