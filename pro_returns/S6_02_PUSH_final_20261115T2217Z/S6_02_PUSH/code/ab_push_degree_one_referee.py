"""Independent exact checks of boundary_d's B.4.21 multiplicity repair."""
import json
from pathlib import Path
import sympy as S

u,v,s,u1,v1,s1,e=S.symbols('u v s u1 v1 s1 e')
for j,m in enumerate(range(12,0,-2)):
    old=s**(2*j)*(u*v-s**m)
    schart=S.expand(old.subs({u:s*u1,v:s*v1}, simultaneous=True))
    expected=s**(2*j+2)*(u1*v1-s**(m-2))
    assert S.expand(schart-expected)==0
    uchart=old.subs({v:u*v1,s:u*s1}, simultaneous=True)
    assert S.expand(uchart-u**(2*j+2)*s1**(2*j)*(v1-u**(m-2)*s1**m))==0
z=[2*min(i,12-i) for i in range(12)]
b=[12-a for a in z]
deg=[-(-2*z[i]+z[(i-1)%12]+z[(i+1)%12]) for i in range(12)]
assert deg==[-4,0,0,0,0,0,4,0,0,0,0,0]
assert sum(b)==72
assert all(z[i]+b[i]==12 for i in range(12))
assert all(b[i]+b[(i+1)%12]>0 for i in range(12))
record={'status':'PASS','point_exponents':list(range(12,0,-2)),
        'normal_correction':z,'curve_blowups':b,'count':sum(b),
        'normal_degrees':deg}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print('All six point-chart total-transform identities: PASS')
print('Normal correction:',z)
print('Normal degrees:',deg)
print('Curve blow-up counts:',b,'total',sum(b))
print('Final exponents all12; every adjacent pair has a positive correction: PASS')
print('ALL EXACT CHECKS PASSED')
