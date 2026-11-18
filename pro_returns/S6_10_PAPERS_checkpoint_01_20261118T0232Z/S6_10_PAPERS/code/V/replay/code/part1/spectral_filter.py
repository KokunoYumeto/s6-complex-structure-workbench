"""Complete finite-order characteristic-polynomial filter, P1B.2."""
from pathlib import Path
from itertools import product
from math import lcm
import json
import sympy as s

orders=(1,2,3,4,5,6,8,10,12)
degrees=(1,1,2,2,4,2,4,4,4)
x=s.symbols('x')
rows=[]
for exps in product(*(range(6//d+1) for d in degrees)):
    if exps[0]<1 or sum(a*b for a,b in zip(exps,degrees))!=6:
        continue
    polynomial=s.prod(s.cyclotomic_poly(n,x)**e for n,e in zip(orders,exps))
    order=lcm(*(n for n,e in zip(orders,exps) if e))
    compatible=exps[0]%2==0 and exps[1]%2==0
    rows.append({'exponents':list(exps),'polynomial':str(s.expand(polynomial)),
                 'linear_order':order,'complex_compatible':compatible})
assert len(rows)==38
assert sum(r['complex_compatible'] for r in rows)==19
assert sorted({r['linear_order'] for r in rows})==list(orders)
result={'status':'PASS','cyclotomic_indices':orders,'cyclotomic_degrees':degrees,
        'enumeration_bounds':[6//d for d in degrees],
        'total':len(rows),'complex_compatible':sum(r['complex_compatible'] for r in rows),
        'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
