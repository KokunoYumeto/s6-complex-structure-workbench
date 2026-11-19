"""Independent exact arithmetic replay of UN24's finite fixed-point data.

Uses the integer trace recurrence, rather than the source's companion
matrices. This verifies the numerical table, not the geometric proof.
"""
from pathlib import Path
from fractions import Fraction
import json

rows=[]
for n,s in [(2,-2),(3,-1),(4,0),(6,1)]:
    tr=[2,s]
    for k in range(2,n+1):
        tr.append(s*tr[-1]-tr[-2])
    assert tr[n] == 2
    fixed={k:(2-tr[k])**2 for k in range(1,n)}
    strata={}
    singularities={}
    for d in range(n,1,-1):
        if n%d: continue
        strata[d]=fixed[n//d]-sum(v for e,v in strata.items() if e%d==0)
        orbit=Fraction(strata[d],n//d)
        assert orbit.denominator==1 and orbit>=0
        singularities[d-1]=int(orbit)
    e=Fraction(sum(fixed.values()),n)
    assert e.denominator==1
    exceptional=sum(a*c for a,c in singularities.items())
    assert e+exceptional==24
    rows.append(dict(order=n,trace=s,fixed=fixed,stabilizer_strata=strata,
                     A_chain_counts=singularities,quotient_euler=int(e),
                     exceptional_rank=exceptional,resolution_euler=24))
out=Path(__file__).resolve().parents[1]/'analysis/UN24_cyclic_counts.json'
out.write_text(json.dumps({'scope':'Exact arithmetic only; geometric quotient and resolution maps checked in the separate proof event.','method':'Integer trace recurrence t[k+1]=s*t[k]-t[k-1]; fixed-isogeny degree (2-t[k])^2; subgroup subtraction and exact orbit division.','rows':rows},indent=2)+'\n')
print(json.dumps(rows))
