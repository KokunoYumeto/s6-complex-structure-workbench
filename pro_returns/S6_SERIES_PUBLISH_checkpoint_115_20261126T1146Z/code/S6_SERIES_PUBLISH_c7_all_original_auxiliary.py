#!/usr/bin/env python3
"""Focused post-exposure L7/L8 auxiliary verification.

Reads the raw fixture and this lane's frozen newly computed data only.
No historical target algorithm or output is read. Does not write frozen files.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd
from pathlib import Path
import hashlib
import json
import re
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/'agents/continuation7_iii_all_original'
RAW = ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
FRESH = LANE/'S6_SERIES_PUBLISH_III_all_original_fresh_data.json'
assert hashlib.sha256(FRESH.read_bytes()).hexdigest() == 'add1915f08f6819d648bcfa0a8dd196b3f368f204787f7bbe4d032346266f586'
profiles = json.loads(RAW.read_text())['rows']
frozen = json.loads(FRESH.read_text())
by_id = {r['id']: r for r in frozen['rows']}
J = S.Matrix([[0,1],[-1,0]])
PAIR = list(combinations(range(4),2))

def ints(M):
    assert all(x.q == 1 for x in M)
    return [[int(x) for x in M.row(i)] for i in range(M.rows)]

def wedge(T):
    return S.Matrix([[T[i,k]*T[j,l]-T[i,l]*T[j,k]
                      for k,l in PAIR] for i,j in PAIR])

def cycle(A,g):
    B=A-S.eye(2)
    col=next(B[:,j] for j in range(2) if any(B[:,j]))
    u=col/gcd(*[abs(int(x)) for x in col])
    if next(x for x in u if x)<0:
        u=-u
    C=u*u.T*J
    i,j=next((i,j) for i in range(2) for j in range(2) if C[i,j])
    n=B[i,j]/C[i,j]
    k=next(g[i]/u[i] for i in range(2) if u[i])
    assert B==n*C and g==k*u and n.q==k.q==1
    return int(n),u,int(k)

def intersection(kind,s):
    if kind=='II':
        return S.zeros(1)
    Q=-2*S.eye(s)
    if kind=='III':
        Q[0,1]=Q[1,0]=2
        return Q
    if kind=='IV':
        return S.ones(3)-3*S.eye(3)
    if kind=='III*':
        edges=[(0,2),(2,4),(4,6),(6,5),(5,3),(3,1),(6,7)]
    elif kind=='IV*':
        edges=[(j,j+3) for j in range(3)]+[(j+3,6) for j in range(3)]
    else:
        k=int(re.fullmatch(r'I(\d+)\*',kind).group(1))
        edges=[(0,4),(2,4),(1,k+4),(3,k+4)]+[(4+j,5+j) for j in range(k)]
    for i,j in edges:
        Q[i,j]=Q[j,i]=1
    return Q

natural=[]
count=Counter()
folds=[]
nonzero=[]
fan=[]
profile_counts=[]
for raw in profiles:
    here=Counter()
    N=len(raw['fibers'])
    for zero,kind in enumerate(raw['fibers']):
        if not re.fullmatch(r'I\d+',kind):
            continue
        n,u,k=cycle(S.Matrix(raw['elliptic_matrices'][zero]),S.Matrix(raw['generator_section_cocycle'][zero]))
        total=1/(Fraction(raw['height_of_generator'])*n)
        if total.denominator!=1:
            continue
        for a in range(1,total.numerator+1):
            if total.numerator%a:
                continue
            b=total.numerator//a
            if gcd(b*k,n)!=1:
                continue
            lhs=[int(j==a*k%n)-int(j==0)-int(j==(a-b)*k%n)+int(j==-b*k%n) for j in range(n)]
            rhs=[-2*int(j==0)+int(j==1%n)+int(j==-1%n) for j in range(n)]
            if lhs!=rhs:
                continue
            if any(a*c[0]%q and b*c[0]%q for i,d in enumerate(raw['component_coordinates']) if i!=zero
                   for q,c in zip(d['moduli'],d['rows'])):
                continue
            rid=f"{raw['OS']}:{raw['profile']}:z{zero+1}:a{a}:b{b}"
            row=by_id[rid]
            natural.append(rid)
            here['natural']+=1
            for i,(site,cc) in enumerate(zip(raw['fibers'],raw['component_coordinates'])):
                narrow=all(a*c[0]%q==0 for q,c in zip(cc['moduli'],cc['rows']))
                if narrow:
                    count['P_narrow_all_sites']+=1
                    if i!=zero:
                        count['P_narrow_unselected']+=1
                        here['zero_original_occurrences']+=1
                if i==zero or not re.fullmatch(r'I\d+',site) or not narrow:
                    continue
                ni,ui,ki=cycle(S.Matrix(raw['elliptic_matrices'][i]),S.Matrix(raw['generator_section_cocycle'][i]))
                assert gcd(b*ki,ni)==1
                pair=S.Matrix.hstack(S.Matrix(list(ui)+[0,0]),S.Matrix([0,0,1,0]))
                snf=smith_normal_form(pair,domain=S.ZZ)
                assert [abs(int(snf[j,j])) for j in range(2)]==[1,1]
                count['zero_multiplicative_transitive']+=1
            if b==1:
                C=S.Matrix([[n,k],[-a*k,S.Rational(1-a*k*k,n)]])
                assert C.det()==1
                coords=C.inv()*S.Matrix([0,1])
                edges=[S.Matrix([1,0]),S.Matrix([0,1]),S.Matrix([-1,1])]
                weights=[abs(int(S.det(S.Matrix.hstack(coords,e)))) for e in edges]
                data=dict(row=rid,nu=n,kappa=k,C=ints(C),delta_in_Jordan=list(map(int,coords)),edge_isotropy_orders=weights)
                fan.append(data)
                count['b1_fans']+=1
                if max(weights)>1:
                    count['b1_nonsemifree_initial_fans']+=1
            for d in row['original_additive']:
                i=d['site']-1
                if d['zero_Chern']:
                    mult=S.Matrix(d['multiplicities'])
                    Q=intersection(d['type'],len(mult))
                    assert Q*mult==S.zeros(len(mult),1)
                    assert Q.rank()==len(mult)-1
                    perm=d['plus_Q']
                    P=S.zeros(len(mult))
                    for j,p in enumerate(perm): P[p,j]=1
                    assert P.T*Q*P==Q
                    obs=d['orbits']; rho=len(obs)
                    I=S.zeros(len(mult),rho); R=S.zeros(len(mult),rho)
                    for j,ob in enumerate(obs):
                        R[ob[0],j]=1
                        for x in ob: I[x,j]=1
                    F=I.T*Q*R
                    W=S.Matrix(d['W'])
                    assert F.rank()==rho-1 and F*W==S.zeros(rho,1)
                    folds.append(dict(row=rid,site=i+1,type=d['type'],intersection=ints(Q),orbit_sum=ints(I),representatives=ints(R),folded=ints(F),W=list(map(int,W)),rank=rho-1))
                    count['zero_additive_occurrences']+=1
                else:
                    A=S.Matrix(raw['elliptic_matrices'][i]); g=S.Matrix(raw['generator_section_cocycle'][i])
                    z=b*(A-S.eye(2)).inv()*g
                    assert all(x.q==1 for x in z)
                    w=S.Matrix([[1,0,z[1],0,-z[0],0]])
                    K=S.eye(6)[:,1:]
                    K[0,1]=-z[1]; K[0,3]=z[0]
                    left=S.eye(6)[1:,:]
                    assert w*K==S.zeros(1,5) and left*K==S.eye(5)
                    omega=S.Matrix([[a,0,0,0,0,-b]])
                    values=omega*K
                    h=gcd(*map(int,values))
                    assert h==b//d['component_order']==d['h']
                    quotient=S.Matrix(d['fibre_quotient']); kernel=S.Matrix(d['fibre_kernel'])
                    assert quotient[0,:]==w
                    smith=d['boundary_fibre_smith']
                    BW=S.Matrix(smith['matrix']); U=S.Matrix(smith['U']); V=S.Matrix(smith['V'])
                    residue=K-kernel*(quotient[1,:]*K)
                    lift=V[:,:4]*U[:4,:]*residue
                    # D has four positive unit diagonal entries in frozen data.
                    assert BW*lift==residue
                    nonzero.append(dict(row=rid,site=i+1,type=d['type'],q=d['component_order'],z=list(map(int,z)),area=ints(w),kernel_basis=ints(K),kernel_inverse=ints(left),omega_values=ints(values),h=h,Wang_relation_lift=ints(lift)))
                    count['nonzero_additive_occurrences']+=1
                    here['nonzero_additive_occurrences']+=1
    profile_counts.append(dict(OS=raw['OS'],profile=raw['profile'],**dict(here)))

assert len(natural)==len(set(natural))==172 and set(natural)==set(by_id)
assert len(nonzero)==46
print('POST-EXPOSURE AUXILIARY CHECK; no historical target program/output read')
print('COUNTS',json.dumps(dict(count),sort_keys=True))
print('PROFILE COUNTS')
for p in profile_counts: print(json.dumps(p,sort_keys=True))
print('DISTINCT ZERO-CHERN ADDITIVE FOLDED MAPS')
distinct={}
for d in folds:
    key=(d['type'],tuple(tuple(x) for x in d['folded']))
    distinct[key]=d
for key,d in sorted(distinct.items()):
    print(d['type'],'F='+str(d['folded']),'W='+str(d['W']),'rank='+str(d['rank']))
print('ALL NONZERO-CHERN AREA/KERNEL OCCURRENCES')
for d in nonzero:
    print(d['row'],'site='+str(d['site']),d['type'],'z='+str(d['z']),'omega(K)='+str(d['omega_values'][0]),'h='+str(d['h']))
print('ALL b=1 INITIAL FANS WITH NONTRIVIAL FINITE ANGULAR ISOTROPY')
for d in fan:
    if max(d['edge_isotropy_orders'])>1: print(json.dumps(d,sort_keys=True))
print('PASS: raw natural rows, all multiplicative transitivity/pairs, folded intersection ranks, all 46 area kernels and exact Wang lifts; fresh data unchanged.')
result=dict(scope='Post-exposure auxiliary verification after full L7/L8 original read; no blind credit.',counts=dict(count),profiles=profile_counts,folded_maps=folds,nonzero_maps=nonzero,b1_fans=fan)
(LANE/'S6_SERIES_PUBLISH_III_all_original_auxiliary_data.json').write_text(json.dumps(result,indent=2)+'\n')
