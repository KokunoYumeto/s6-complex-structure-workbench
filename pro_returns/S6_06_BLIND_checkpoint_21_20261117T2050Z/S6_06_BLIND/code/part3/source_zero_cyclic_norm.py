#!/usr/bin/env python3
"""Exact exponents for continued chosen-sheet maps; no finite action asserted."""
from fractions import Fraction
from pathlib import Path
import json

root=Path(__file__).resolve().parents[2]
rows=[]
checks=0
def mod1(x):
    return x-x.numerator//x.denominator
for p in range(1,25):
    for n in (-1,1):
        for branch,m in [('good',4*p),('reduced',4*p-1)]:
            s=m*(m-1)//2
            w=(n,-n) if branch=='good' else (-n*(m-1)//2,-n)
            orders=[j for j in range(1,m+1) if all(j*x % m==0 for x in w)]
            assert orders==[m],(branch,m,n,w,orders)
            checks+=1
            for node in ('q1','q2'):
                if branch=='good':
                    source=Fraction((-1 if node=='q1' else 1)*n,m)
                    line=-source
                    expect=(Fraction(1,2),Fraction(1,2))
                else:
                    source=Fraction(n*(m-1 if node=='q1' else m+1),2*m)
                    line=Fraction(n if node=='q1' else -n,m)
                    expect=(Fraction(0),Fraction(0))
                actual=(mod1(s*source),mod1(s*line))
                assert actual==expect,(p,n,branch,node,actual)
                checks+=2
                rows.append({'p':p,'m':m,'n':n,'branch':branch,'node':node,
                             'one_step_exponents':[str(source),str(line)],
                             'cyclic_residual_exponents':[str(x) for x in actual]})
out={'status':'PASS','checks':checks,
     'scope':'Successive chosen-sheet continuation only; no closed root-sheet action or central attachment asserted.',
     'good_residual':'(Z,V) -> (-Z,-V)',
     'reduced_residual':'identity',
     'direct_root_quotient_I_boundary_multiplicity':'m, because all component orbits have length m and generic inertia is trivial',
     'rows':rows}
path=root/'code/part3/source_zero_cyclic_norm.json'
path.write_text(json.dumps(out,indent=2)+'\n')
message=f'PASS: {checks} exact cyclic-exponent checks; good residual (-1,-1), reduced residual identity.\nChosen-sheet continuation only; root-sheet action and attachment remain unassembled.\n'
(root/'code/part3/source_zero_cyclic_norm.out').write_text(message)
print(message,end='')
