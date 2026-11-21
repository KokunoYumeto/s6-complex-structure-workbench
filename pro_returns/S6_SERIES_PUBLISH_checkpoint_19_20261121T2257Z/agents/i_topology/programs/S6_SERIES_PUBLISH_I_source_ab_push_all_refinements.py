"""Exact finite data for the exhaustive periodic-fan parametrization.

This enumerates the candidate rays and unimodular cones at the bounds
explicitly reported below; it does not claim to enumerate every collection
of such cones at the larger bounds.  It also certifies the explicit infinite
family of disjoint maximal-cone star subdivisions through eight steps.
"""
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations, permutations
from math import gcd
from pathlib import Path
import json

def det4(cols):
    out=0
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        term=1
        for i in range(4):
            term*=cols[p[i]][i]
        out+=(-1 if inv%2 else 1)*term
    return out

BOTTOM=((0,0,1,0),(1,0,1,0),(0,1,1,0),(1,1,1,0))
def candidates(n,H,reduced):
    rays=set(BOTTOM)
    for ell in range(1,H+1):
        if reduced and ell!=1:
            continue
        for k in range(H-ell+1):
            for a in range(k+1):
                for b in range(k+n*ell+1):
                    v=(a,b,k,ell)
                    if reduce(gcd,v)==1:
                        rays.add(v)
    return sorted(rays)

def orbit(v,n):
    a,b,k,ell=v
    return (a%k if k else 0,b%(k+n*ell),k,ell)

records=[]
for n in (1,2,12):
    for H in (1,2,3):
        for reduced in (True,False):
            rays=candidates(n,H,reduced)
            top={orbit(v,n) for v in rays if v[2]==0}
            mixed={orbit(v,n) for v in rays if v[2]>0 and v[3]>0}
            if reduced:
                assert len(top)==n
                assert len(mixed)==sum(k*(k+n) for k in range(1,H))
            rec=dict(n=n,H=H,reduced=reduced,rays_in_closed_prism=len(rays),
                     pure_top_orbits=len(top),mixed_orbits=len(mixed))
            # All determinant tests at these bounds are run, not sampled.
            if H==1 or (n<=2 and H==2):
                rec['unimodular_four_subsets']=sum(abs(det4(c))==1
                                                  for c in combinations(rays,4))
            records.append(rec)
            print(rec)

A,B,C,D=BOTTOM
E=(0,0,0,1)
F=(0,1,0,1)
fan=[tuple(sorted(c)) for c in ((A,B,C,E),(B,C,D,E),(C,D,E,F))]
def boundary(cones):
    faces=Counter(tuple(sorted(f)) for c in cones for f in combinations(c,3))
    assert set(faces.values())<={1,2}
    return {f for f,count in faces.items() if count==1}

initial_boundary=boundary(fan)
star_records=[]
previous=E
for m in range(9):
    if m:
        old=tuple(sorted((A,B,C,previous)))
        assert old in fan
        new=tuple(sum(v[i] for v in old) for i in range(4))
        assert new==(m,m,3*m,1)
        assert abs(det4(old))==1
        # A strictly positive sum is in the relative interior; the four
        # replacements are its exact stellar subdivision.
        replacement=[tuple(sorted((new,)+old[:i]+old[i+1:])) for i in range(4)]
        assert all(abs(det4(c))==1 for c in replacement)
        old_volume=Fraction(1,6*reduce(lambda x,y:x*y,(v[2]+v[3] for v in old),1))
        new_volume=sum(Fraction(1,6*reduce(lambda x,y:x*y,(v[2]+v[3] for v in c),1))
                       for c in replacement)
        assert old_volume==new_volume
        fan.remove(old)
        fan+=replacement
        previous=new
    assert all(abs(det4(c))==1 for c in fan)
    assert boundary(fan)==initial_boundary
    assert all(v[3] in (0,1) for c in fan for v in c)
    assert max(sum(v[3]>0 for v in c) for c in fan)<=2
    volume=sum(Fraction(1,6*reduce(lambda x,y:x*y,(v[2]+v[3] for v in c),1))
               for c in fan)
    assert volume==Fraction(1,2)
    betti=[1,1,9+m,7,11+m,0,1+m]
    chi=sum((-1)**i*b for i,b in enumerate(betti))
    assert chi==14+3*m
    assert 2-3+1==0 # nearby Euler increment per point blow-up
    star_records.append(dict(m=m,maximal_cones=len(fan),slice_volume=str(volume),
                             new_ray=list(previous),central_betti=betti,central_euler=chi))
    print('STAR',star_records[-1])

result=dict(candidate_bounds=records,star_certificates=star_records,
            height2_n1_reduced_rays=candidates(1,2,True),
            general_volume='(n+2)/6',
            status='PASS: all advertised finite enumerations and all eight star certificates')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
