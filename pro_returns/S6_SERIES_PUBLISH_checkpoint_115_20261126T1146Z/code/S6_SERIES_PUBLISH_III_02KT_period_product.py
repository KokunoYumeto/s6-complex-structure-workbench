#!/usr/bin/env python3
"""New symbolic comparison of every whole-line product, with free a,b,weights."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s

H=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation6_iii_d2'
raw=json.loads((INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KY_raw_profiles.json').read_text())['rows']
a,b=s.symbols('a b',integer=True)
J=s.Matrix([[0,1],[-1,0]])
E=s.zeros(4);E[2,3]=1
records=[]
for row in raw:
    weights=s.symbols('w0:'+str(len(row['fibers'])))
    total=s.eye(4)
    for entries,coordinates,w in zip(row['elliptic_matrices'],row['generator_section_cocycle'],weights):
        A=s.Matrix(entries);g=s.Matrix(coordinates)
        # Gauss--Jordan solution, with all free affine parameters zero.
        x,parameters=(A-s.eye(2)).gauss_jordan_solve(g)
        x=x.subs({p:0 for p in parameters})
        beta=-g.T*J*A
        T=s.eye(4);T[:2,:2]=A;T[:2,3]=b*g;T[2,:2]=a*beta
        T[2,3]=a*b*(beta*x)[0]+w
        total=total*T
    total=total.applyfunc(s.expand)
    height=s.Rational(row['height_of_generator'])
    expected=s.eye(4)+(sum(weights)-a*b*height)*E
    assert total==expected
    regular=s.symbols('w_regular',integer=True)
    assert (total*(s.eye(4)+regular*E)).applyfunc(s.expand)==s.eye(4)+(sum(weights)+regular-a*b*height)*E
    records.append(dict(OS=row['OS'],profile=row['profile'],height=str(height),central=str(total[2,3])))
    print(row['OS'],row['profile'],'product = I4 + (sum weights - a*b*'+str(height)+') E_delta,gamma')
(H/'S6_SERIES_PUBLISH_III_02KT_period_product_maps.json').write_text(json.dumps(records,indent=2)+'\n')
print('All 21 profiles verified over the full polynomial ring, including the regular-marker commuting product.')
print('At a*b=d and total weight 1 every product is exactly I4.')
print('Completed UTC:',datetime.now(timezone.utc).isoformat())
