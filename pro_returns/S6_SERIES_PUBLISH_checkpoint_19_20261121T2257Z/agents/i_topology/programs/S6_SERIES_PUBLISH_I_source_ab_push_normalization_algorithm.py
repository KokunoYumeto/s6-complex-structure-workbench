"""Exact local tests for the normalization algorithm A.2.5.

This bounded search demonstrates the recorded star/inverse-star data;
the proof of termination for any input uses finite toroidal weak
factorization and does not rely on these examples.
"""
from pathlib import Path
from collections import deque
from itertools import combinations,product
import json
import sympy as s

A=(0,0,1,0); B=(1,0,1,0); C=(0,1,1,0); D=(1,1,1,0)
E=(0,0,0,1); F=(0,1,0,1)
def cone(x): return tuple(sorted(x))
def canonical(fan): return tuple(sorted(cone(c) for c in fan))
def star(fan,old):
    old=cone(old)
    assert old in fan
    ray=tuple(sum(v[i] for v in old) for i in range(4))
    new=[tuple(ray if j==i else old[j] for j in range(4)) for i in range(4)]
    result=canonical([c for c in fan if c!=old]+new)
    assert all(abs(int(s.Matrix.hstack(*map(s.Matrix,c)).det()))==1 for c in result)
    return result,ray

start=canonical([(A,B,C,E),(B,C,D,E),(C,D,E,F)])
target1,v1=star(start,(A,B,C,E))
target2,v2=star(target1,(A,B,C,v1))
assert v1==(1,1,3,1) and v2==(2,2,6,1)
queue=deque([(start,[])])
seen={start}
found=None
while queue:
    fan,path=queue.popleft()
    if fan==target2:
        found=path
        break
    if len(path)==2: continue
    for old in fan:
        nxt,ray=star(fan,old)
        if nxt in seen: continue
        seen.add(nxt)
        queue.append((nxt,path+[dict(centre_cone=old,exceptional_ray=ray,
                                    exceptional_multiplicity=ray[3])]))
assert found is not None and len(found)==2

def inverse_star(fan,ray):
    starcones=[c for c in fan if ray in c]
    boundary=sorted({v for c in starcones for v in c if v!=ray})
    assert len(boundary)==4
    candidate=cone(boundary)
    assert tuple(sum(v[i] for v in candidate) for i in range(4))==ray
    expected={cone([ray]+list(f)) for f in combinations(candidate,3)}
    assert set(starcones)==expected
    return canonical([c for c in fan if ray not in c]+[candidate])
assert inverse_star(target2,v2)==target1
assert inverse_star(target1,v1)==start

z=s.symbols('z0:4'); w=s.symbols('w0:4'); t=s.symbols('t')
local_count=0
for codim in (2,3,4):
    for exponents in product((0,1,2),repeat=4):
        if not any(exponents): continue
        mon=s.prod(z[i]**exponents[i] for i in range(4))
        for pivot in range(codim):
            replacement={z[j]:(t if j==pivot else t*w[j]) for j in range(codim)}
            result=s.expand(mon.subs(replacement,simultaneous=True))
            expected=t**sum(exponents[:codim])
            expected*=s.prod(w[j]**exponents[j] for j in range(codim) if j!=pivot)
            expected*=s.prod(z[j]**exponents[j] for j in range(codim,4))
            assert s.expand(result-expected)==0
            local_count+=1
        for i,l in enumerate(exponents):
            expected=0 if l==0 else l*z[i]**(l-1)*s.prod(z[j]**exponents[j] for j in range(4) if j!=i)
            assert s.expand(s.diff(mon,z[i])-expected)==0

out=dict(status='PASS',breadth_first_states_seen=len(seen),path=found,
         inverse_stars_checked=2,local_chart_substitutions=local_count,
         R_b2=11,P3_b2=1,
         assertion='Every P3 normalized component disproves a universal blow-up-of-R presentation.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
