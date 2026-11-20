#!/usr/bin/env python3
"""Fresh Fraction Laurent verification; producer implementation is not imported."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import hashlib
import json
import math
import time

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'audit_sign/K111_T2_compact_ledger.json'
FAN = ROOT / 'audit_sign/K111_new_regular_common_fan.json'
OUTPUT = ROOT / 'code/outputs/K111_compact_owner_independent.json'
checks = 0


def require(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)


def poly_mul(a, b):
    c = defaultdict(F)
    for i, x in a.items():
        for j, y in b.items():
            c[i+j] += x*y
    return {i:x for i,x in c.items() if x}


def add(a, b, scale=1):
    for i,x in b.items():
        a[i] += scale*x


def inverse_product(w, a, multiplicities):
    """All Laurent coefficients through degree zero of product W_i^-m_i."""
    pole = sum(m for x,m in zip(w,multiplicities) if x == 0)
    coefficients = [F(1)] + [F(0)]*pole
    for x,y,m in zip(w,a,multiplicities):
        if x == 0:
            require(y != 0, ('identically zero weight',w,a))
            coefficients = [v/F(y)**m for v in coefficients]
            continue
        expansion = [F((-1)**k*math.comb(m+k-1,k)*y**k, x**(m+k))
                     for k in range(pole+1)]
        coefficients = [sum(coefficients[j]*expansion[k-j]
                            for j in range(k+1)) for k in range(pole+1)]
    return {k-pole:x for k,x in enumerate(coefficients) if x}


def nonpositive_product(a,b):
    return {i:x for i,x in poly_mul(a,b).items() if i<=0}


def contribution(w, a, degrees, alternative):
    # W=w+(w+2a)e, u=1+e in the second evaluation.
    slopes = [x+2*y for x,y in zip(w,a)] if alternative else list(a)
    u = {0:F(1),1:F(1)} if alternative else {0:F(1)}
    u3 = poly_mul(poly_mul(u,u),u)
    inv = inverse_product(w,slopes,[1]*len(w))
    Q = defaultdict(F)
    for x,y in zip(w,slopes):
        add(Q,{0:F(x*x),1:F(2*x*y),2:F(y*y)})
    if degrees is None:
        return ({i:-x for i,x in nonpositive_product(inv,u3).items()},
                {i:-x for i,x in nonpositive_product(inv,poly_mul(u,Q)).items()})
    S_over_W = defaultdict(F)
    T = defaultdict(F)
    for i,(x,y,d) in enumerate(zip(w,slopes,degrees)):
        add(T,{0:F(x*d),1:F(y*d)})
        if d:
            powers = [1]*len(w)
            powers[i] = 2
            add(S_over_W,inverse_product(w,slopes,powers),d)
    first = nonpositive_product(S_over_W,u3)
    second = defaultdict(F)
    add(second,nonpositive_product(S_over_W,poly_mul(u,Q)))
    add(second,nonpositive_product(inv,poly_mul(u,T)),-2)
    return first,dict(second)


def inverse(A):
    n=len(A)
    rows=[[F(x) for x in row]+[F(i==j) for j in range(n)]
          for i,row in enumerate(A)]
    for k in range(n):
        t=next(i for i in range(k,n) if rows[i][k])
        rows[k],rows[t]=rows[t],rows[k]
        v=rows[k][k]
        rows[k]=[x/v for x in rows[k]]
        for i in range(n):
            if i!=k:
                v=rows[i][k]
                rows[i]=[x-v*y for x,y in zip(rows[i],rows[k])]
    return [r[n:] for r in rows]


def mv(A,v):
    return [sum(x*y for x,y in zip(r,v)) for r in A]


def main():
    start=time.time()
    raw=INPUT.read_bytes()
    data=json.loads(raw)
    fan_raw=FAN.read_bytes()
    fan=json.loads(fan_raw)
    sums=[defaultdict(lambda:[defaultdict(F),defaultdict(F)]) for _ in range(2)]
    pieces=defaultdict(int)
    generic=0
    for item in data['generic_curve_clutches']:
        owner=item['physical_owner']
        face=fan['cones'][item['common_cone']]['rays']
        N=[list(r) for r in zip(*face)]
        invN=inverse(N)
        w=mv(invN,[1,0,0]); a=mv(invN,[0,1,0])
        physical_face=sorted(ray for ray,weight in zip(face,w) if weight)
        require(physical_face in [sorted(v) for v in data['physical_owners'][owner]['faces']],
                ('physical normal-face transport',owner))
        require(item['common_cone'] in data['physical_owners'][owner]['common_charts'],
                ('generic chart membership',owner))
        require(w==item['physical_weights'],('generic physical weights',owner))
        require(a==item['second_weights'],('generic second weights',owner))
        degrees=[F(0)]*3
        for endpoint,clutch in item['clutches'].items():
            c=mv(invN,mv(clutch['character_matrix'],clutch['transverse_ray']))
            require(c==clutch['coefficient_orders'],('generic coefficient',owner,endpoint))
            degrees=[x-y for x,y in zip(degrees,c)]
        require(degrees==item['degrees'],('generic degree',owner))
        # Convert the verified integral vectors before integer-power expansion.
        require(all(x.denominator==1 for x in w+a+degrees),('integrality',owner))
        w,a,degrees=map(lambda v:[int(x) for x in v],(w,a,degrees))
        for alt in (0,1):
            pair=contribution(w,a,degrees,alt)
            for j in (0,1): add(sums[alt][owner][j],pair[j])
        pieces[owner]+=1
        generic+=1
    corner=0
    for item in data['compact_corner_second_fixed_pieces']:
        owner=item['physical_owner']
        require(data['physical_owners'][owner]['kind'].startswith('compact'),
                ('corner compact owner',owner))
        for alt in (0,1):
            pair=contribution(item['physical_weights'],item['second_weights'],item['degrees'],alt)
            for j in (0,1): add(sums[alt][owner][j],pair[j])
        pieces[owner]+=1
        corner+=1
        if corner%10000==0:
            print('corner pieces',corner,'elapsed',round(time.time()-start,1),flush=True)
    require(set(sums[0])==set(data['physical_component_ledger']), 'owner set')
    totals=[F(0),F(0)]
    results={}
    maximum_pole=0
    for owner,saved in data['physical_component_ledger'].items():
        require(pieces[owner]==saved['second_fixed_pieces'],('piece count',owner))
        pair=[]
        for j in (0,1):
            for alt in (0,1):
                s=sums[alt][owner][j]
                maximum_pole=max(maximum_pole,max((-k for k in s if k<0),default=0))
                require(all(x==0 for k,x in s.items() if k<0),('uncancelled pole',owner,j,alt,dict(s)))
            c=sums[0][owner][j].get(0,F(0))
            require(c==sums[1][owner][j].get(0,F(0)),('alternative constant',owner,j))
            require(c==F(saved['pair'][j]),('stored constant',owner,j,c,saved['pair'][j]))
            totals[j]+=c
            pair.append(str(c))
        results[owner]={'pair':pair,'pieces':pieces[owner]}
    require(totals==list(map(F,data['compact_pair'])),'total compact pair')
    require(totals==[F(895),F(139)],'declared numerical pair')
    for piece in data['excluded_second_fixed_pieces']:
        require(data['physical_owners'][piece['physical_owner']]['kind']=='noncompact lower',
                ('excluded owner',piece['physical_owner']))
    out={'status':'PASS','checks':checks,'input':str(INPUT.relative_to(ROOT)),
         'input_sha256':hashlib.sha256(raw).hexdigest(),
         'ordered_common_fan_sha256':hashlib.sha256(fan_raw).hexdigest(),
         'method':'independent exact Fraction Laurent expansions for both physical-parameter substitutions; exact three-end generic matrix clutches',
         'generic_curves':generic,'compact_corner_pieces':corner,'compact_owners':len(results),
         'maximum_pole_order_cancelled':maximum_pole,'compact_pair':list(map(str,totals)),
         'scope':'Verifies every supplied compact-owner Laurent cancellation and contribution and all three-end generic weights/degrees. Owner classification, point/O extension and outer cap comparison retain their separate geometric proofs.',
         'elapsed_seconds':time.time()-start,'owners':results}
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='owners'},indent=2),flush=True)


if __name__=='__main__': main()
