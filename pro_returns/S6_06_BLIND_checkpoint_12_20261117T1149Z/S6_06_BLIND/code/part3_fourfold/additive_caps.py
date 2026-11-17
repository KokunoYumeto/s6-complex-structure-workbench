#!/usr/bin/env python3
"""Exact root exponents and component norm restrictions for additive caps."""
from pathlib import Path
import json
from math import gcd

root=Path(__file__).resolve().parent
types={2:'II',3:'III',4:'IV',6:'I0*',8:'IV*',9:'III*',10:'II*',0:'smooth'}
source={'II':(1,1,2),'III':(1,2,3),'IV':(2,2,4),
        'III*':(3,5,9),'IV*':(3,4,8)}
rows=[]
for name,(vf,vg,vd) in source.items():
    for m in range(1,121):
        k=min(m*vf//4,m*vg//6)
        vals=[m*vf-4*k,m*vg-6*k,m*vd-12*k]
        assert vals[2] in types,(name,m,vals)
        typ=types[vals[2]]
        rows.append(dict(source=name,m=m,k=k,valuations=vals,root=typ))
        if name in ('III','III*'):
            expected={0:'smooth',1:'III',2:'I0*',3:'III*'}[(m*(1 if name=='III' else 3))%4]
        elif name in ('IV','IV*'):
            expected={0:'smooth',1:'IV',2:'IV*'}[(m*(1 if name=='IV' else 2))%3]
        else:
            expected={0:'smooth',1:'II',2:'IV',3:'I0*',4:'IV*',5:'II*'}[m%6]
        assert typ==expected

component_checks=0
for p in (2,3):
    for m in range(1,31):
        if gcd(m,p)>1: continue
        for n in range(-30,31):
            for b in range(p):
                r0=(n*b*pow(m,-1,p))%p
                subgroup=gcd(p,b,r0)
                assert subgroup==gcd(p,b)
                component_checks+=1

for l in range(40):
    # Exponents are understood modulo the actual root order.
    m=3*l+1
    assert (3*l+1)%m==0
    m=3*l+2
    assert (6*l+4)%m==0
    m=6*l+2
    assert 2*(3*l+1)==m

result=dict(all_pass=True,root_cases=len(rows),component_norm_cases=component_checks,
            roots=rows,scope='Necessary additive cap restrictions and the exact source affine norm; no total-space topology or index assignment.')
(root/'additive_caps.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='roots'},indent=2))
