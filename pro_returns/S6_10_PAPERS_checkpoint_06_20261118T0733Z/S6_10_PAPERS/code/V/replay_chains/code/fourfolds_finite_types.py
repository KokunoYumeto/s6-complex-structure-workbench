"""Complete characteristic-polynomial filter for finite linear monodromy.

A free affine action needs a nonzero 1-eigenspace.  Thus a cyclotomic factor
has degree at most five.  The full set with phi(n)<=5 is the nine n below;
the elementary bound phi(n)>=sqrt(n/2) bounds n by 50, so enumeration to 50
is a proved sufficient bound for this preliminary filter.  This is NOT an
integral-conjugacy classification of tuples or of affine lifts.
"""
from itertools import product, combinations
from math import lcm
from sympy import totient, cyclotomic_poly, symbols, expand
from pathlib import Path
import json
x=symbols('x')
orders=[n for n in range(1,51) if totient(n)<=5]
assert orders==[1,2,3,4,5,6,8,10,12]
deg={n:int(totient(n)) for n in orders}
rows=[]
for powers in product(*[range(6//deg[n]+1) for n in orders]):
    mult=dict(zip(orders,powers))
    if mult[1]==0 or sum(mult[n]*deg[n] for n in orders)!=6:continue
    linear_order=lcm(*[n for n in orders if mult[n]])
    hol=mult[1]%2==0 and mult[2]%2==0
    roots=[]
    from math import gcd
    for n in orders:
        for k in range(1,n+1):
            if gcd(k,n)==1:roots += [(k*linear_order//n)%linear_order]*mult[n]
    dims=[sum(sum(c)%linear_order==0 for c in combinations(roots,q)) for q in range(7)]
    poly=expand(__import__('functools').reduce(lambda a,n:a*cyclotomic_poly(n,x)**mult[n],orders,1))
    rows.append({'multiplicities':mult,'order':linear_order,'holomorphic_possible':hol,
                 'fixed_exterior_ranks':dims,'polynomial':str(poly)})
print('Possible linear orders:', sorted(set(r['order'] for r in rows)))
print('All degree-six cyclotomic types with a 1-eigenvalue:',len(rows))
hol=[r for r in rows if r['holomorphic_possible']]
print('Types commuting with a complex structure:',len(hol))
for r in hol:
    factors=' '.join('Phi(%d)^%d'%(n,m) for n,m in r['multiplicities'].items() if m)
    print(factors,'order',r['order'],'fixed exterior ranks',r['fixed_exterior_ranks'])
print('Necessary (k; finite fixed ranks; dual-global rank) for b1=b2=0:')
for k in (2,3):
    for rs in combinations(range(2,7,2),k):
        pass
    for rs in product((2,4,6),repeat=k):
        if tuple(sorted(rs))!=rs:continue
        dual=sum(rs)+3-1-6*(k-1)
        if 0<=dual<=min(3,*rs):print(k,rs,dual)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
