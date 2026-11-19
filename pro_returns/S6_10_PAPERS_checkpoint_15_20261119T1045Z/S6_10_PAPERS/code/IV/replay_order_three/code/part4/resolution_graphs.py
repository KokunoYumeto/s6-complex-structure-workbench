"""Exact checks for the resolution-conductor Euler identities of P4R.8.

The proof is the displayed symbolic identity, valid without a search bound.
The finite enumeration is an additional check, not an exhaustion of surfaces.
"""
from pathlib import Path
import json
import sympy as s

c,r,g,b,h=s.symbols('c r g b h', integer=True)
e=c+h-2*g-b
lower=c+r-2*g-1
assert s.expand(e-lower-(1-(b+r-h)))==0
assert s.expand(lower+1-((c-g)+(r-g)))==0
bound=14
count=0
negative=[]
for R in range(1,bound+1):
    for C in range(1,bound+1):
        for G in range(min(C,R)+1):
            for H in range(1,min(C,R)+1):
                for B in range(max(0,1-R+H)+1):
                    if B+R-H>1:
                        continue
                    count+=1
                    E=C+H-2*G-B
                    if E<0:
                        assert C==R==G and B+R-H==1 and E==-1
                        negative.append([C,R,G,H,B,E])
record={
    'statement':'P4R.8',
    'identities':[
        'e(C)-(c+r-2g-1)=1-(b+r-s)',
        '(c+r-2g-1)+1=(c-g)+(r-g)'],
    'constraints':'c>=g; r>=g; b+r-s<=1; all variables integral',
    'negative_conclusion':'e(C)<0 forces c=r=g, b+r-s=1, e(C)=-1',
    'finite_check_bound':bound,
    'finite_check_cases':count,
    'negative_cases':negative,
    'geometric_exclusion':'P4R.8 proves C locally unibranch in the forced negative case; then b=0, s=c=g and e(C)=0.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='negative_cases'},indent=2))
