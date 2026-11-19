#!/usr/bin/env python3
"""Exact one-step cusp deck of the partial origin; no geometric descent assumed."""
from pathlib import Path
import json
import sympy as sp
s,v,mu,C=sp.symbols('s v mu C')
def F(a,b):
    return sp.Matrix([mu*(a+12*b)/2,
        C*(a+12*b)/12-(a+12*b)**2/24+6*b])
gamma=sp.Matrix([6*mu,C-s-12*v])
delta=sp.Matrix([0,1])
one=sp.simplify(F(s+1,v)-F(s,v))
twelve=sp.simplify(F(s+12,v)-F(s,v))
assert sp.simplify(one-gamma/12+delta/24)==sp.zeros(2,1)
assert sp.simplify(twelve-gamma+6*delta)==sp.zeros(2,1)
data={
    'one_step':'F(s+1,v)-F(s,v)=gamma(s,v)/12-delta/24',
    'twelve_steps':'F(s+12,v)-F(s,v)=gamma(s,v)-6delta',
    'q':'Q^12',
    'free_reduced_Q_divisor_quotient_multiplicity':12,
    'actual_reduced_cusp_multiplicity':1,
    'proper_bimeromorphic_map_over_q_from_all_multiplicity_12_divisors':False,
    'proof':'A strict transform of a multiplicity-one target divisor has the same divisorial valuation of q, hence order one.'
}
out=Path(__file__).resolve().parent
(out/'outer_descent.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
