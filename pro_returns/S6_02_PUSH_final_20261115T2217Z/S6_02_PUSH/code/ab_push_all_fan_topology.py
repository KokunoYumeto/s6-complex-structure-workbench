"""Exact checks of the general central-Euler and nearby-Euler formulas.

Tests every minimal bridge for n=1,2,12, eight point stars, and five
nonreduced conductor stars. The proof in A.4.7 handles every fan.
"""
from itertools import permutations
from pathlib import Path
import json

A=(0,0,1,0); B=(1,0,1,0); C=(0,1,1,0); D=(1,1,1,0)
E=(0,0,0,1); F=(0,1,0,1)
def determinant(cols):
    s=0
    for p in permutations(range(4)):
        x=1
        for i in range(4): x*=cols[p[i]][i]
        s+=(-1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1)*x
    return s

records=[]
def check(tag,n,fan,expected):
    assert all(abs(determinant(c))==1 for c in fan)
    rays={v for c in fan for v in c}
    top={(0,v[1]%(n*v[3]),0,v[3]) for v in rays if v[2]==0}
    K=len(top); T=len(fan)
    singles=[next(v[3] for v in c if v[3]) for c in fan if sum(v[3]>0 for v in c)==1]
    assert singles==[1,1] or sorted(singles)==[1,1]
    chi=11*K+T
    assert chi==expected
    rec=dict(tag=tag,n=n,pure_top_orbits=K,maximal_cones=T,
             central_Euler=chi,nearby_point_weights=singles,nearby_Euler=sum(singles))
    records.append(rec)
    print(rec)

for n in (1,2,12):
    rho=[(0,j,0,1) for j in range(n+1)]
    for k in range(n+1):
        fan=[(A,B,C,rho[k]),(B,C,D,rho[k])]
        fan += [(A,B,rho[i],rho[i+1]) for i in range(k)]
        fan += [(C,D,rho[i],rho[i+1]) for i in range(k,n)]
        check('bridge'+str(k),n,fan,12*n+2)

fan=[(A,B,C,E),(B,C,D,E),(C,D,E,F)]
previous=E
for m in range(9):
    if m:
        old=(A,B,C,previous)
        new=tuple(sum(v[i] for v in old) for i in range(4))
        fan.remove(old)
        fan += [old[:i]+(new,)+old[i+1:] for i in range(4)]
        previous=new
    check('point_stars'+str(m),1,fan,14+3*m)

fan=[(A,B,C,E),(B,C,D,E),(C,D,E,F)]
right=F
for m in range(6):
    if m:
        old=(C,D,E,right)
        new=tuple(E[i]+right[i] for i in range(4))
        assert new==(0,1,0,m+1)
        fan.remove(old)
        fan += [(C,D,E,new),(C,D,new,right)]
        right=new
    check('nonreduced_conductor_stars'+str(m),1,fan,14+12*m)

Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
print('ALL GENERAL EULER FORMULA CERTIFICATES PASSED:',len(records),'models')
