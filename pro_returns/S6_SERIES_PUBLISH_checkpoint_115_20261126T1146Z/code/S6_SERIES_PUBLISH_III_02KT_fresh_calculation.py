#!/usr/bin/env python3
"""Whole-fibre initial data from raw marked elliptic definitions.

No KT proof, completed-manifold catalogue, or historical KT program is
read.  The raw model data and the admitted Poincare lift are attributed
inputs; the component-divisor proof is developed in the companion file.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from functools import reduce
from collections import defaultdict
import json
import csv

HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation6_iii_d2'
RAW=json.loads((INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KY_raw_profiles.json').read_text())


def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def adj2(A):return [[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mv(A,v):return [dot(r,v) for r in A]
def mm(A,B):return [[dot(r,c) for c in zip(*B)] for r in A]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]


def bezout(a,b):
    r0,r1=a,b;s0,s1=1,0;t0,t1=0,1
    while r1:
        q=r0//r1;r0,r1=r1,r0-q*r1;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
    return (r0,s0,t0) if r0>=0 else (-r0,-s0,-t0)


def local(A,g,kind):
    N=[[A[i][j]-int(i==j) for j in range(2)] for i in range(2)]
    determinant=det2(N)
    if determinant:
        h=[F(x,determinant) for x in mv(adj2(N),g)]
        return dict(type=kind,solution=h,narrow_order=reduce(lambda a,b:a*b//gcd(a,b),(x.denominator for x in h),1))
    assert kind[0]=='I' and kind[1:].isdigit();n=int(kind[1:])
    u=next(list(c) for c in zip(*N) if any(c));d=reduce(gcd,map(abs,u));u=[x//d for x in u]
    if next(x for x in u if x)<0:u=[-x for x in u]
    j=next(j for j,x in enumerate(u) if x);k=F(g[j],u[j]);assert k.denominator==1
    assert [int(k)*x for x in u]==g
    d,x,y=bezout(*u);assert d==1;r=[-y,x]
    assert det2([[u[0],r[0]],[u[1],r[1]]])==1
    assert N==[[n*u[0]*(-u[1]),n*u[0]*u[0]],[n*u[1]*(-u[1]),n*u[1]*u[0]]]
    h=[F(k,n)*x for x in r]
    return dict(type=kind,solution=h,narrow_order=n//gcd(n,int(k)),u=u,kappa=int(k))


def lift(A,g,info,a,b,weight):
    ag=[-a*g[0],-a*g[1]]
    row=mm([ag],mm([[0,1],[-1,0]],A))[0]
    x=[b*z for z in info['solution']]
    centre=dot(row,x)+weight
    matrix=[A[0]+[0,b*g[0]],A[1]+[0,b*g[1]],row+[1,centre],[0,0,0,1]]
    assert all(F(v).denominator==1 for r in matrix for v in r)
    return [[int(v) for v in r] for r in matrix]


def product(ms):
    P=eye(4)
    for M in ms:P=mm(P,M)
    return P


def main():
    total_candidates=0;pairs=[];initial=[];os_pairs=defaultdict(set);profiles=[]
    for raw in RAW['rows']:
        h=F(raw['height_of_generator']);assert h.numerator==1;d=h.denominator
        As=raw['elliptic_matrices'];gs=raw['generator_section_cocycle'];kinds=raw['fibers']
        info=[local(A,g,k) for A,g,k in zip(As,gs,kinds)]
        candidates=[(a,d//a) for a in range(1,d+1) if d%a==0];total_candidates+=len(candidates)
        accepted=[];places=[j+1 for j,k in enumerate(kinds) if k[0]=='I' and k[1:].isdigit()]+['regular']
        for a,b in candidates:
            decisions=[dict(fiber=j+1,type=local_info['type'],narrow_order=local_info['narrow_order'],
                            P_narrow=a%local_info['narrow_order']==0,Q_narrow=b%local_info['narrow_order']==0)
                       for j,local_info in enumerate(info)]
            if any(not (v['P_narrow'] or v['Q_narrow']) for v in decisions):continue
            accepted.append((a,b));os_pairs[raw['OS']].add((a,b))
            pairs.append(dict(OS=raw['OS'],profile=raw['profile'],d=d,a=a,b=b,
                              component_tests=decisions,number_of_zero_markers=len(places)))
            for place in places:
                Ts=[lift(A,g,local_info,a,b,int(j+1==place))
                    for j,(A,g,local_info) in enumerate(zip(As,gs,info))]
                zero_type=kinds[place-1] if isinstance(place,int) else 'regular'
                if place=='regular':
                    Treg=eye(4);Treg[2][3]=1;Ts.append(Treg)
                assert product(Ts)==eye(4)
                assert all(T[3]==[0,0,0,1] and [T[i][2] for i in range(4)]==[0,0,1,0] for T in Ts)
                initial.append(dict(OS=raw['OS'],profile=raw['profile'],a=a,b=b,
                                    zero_fiber=place,zero_type=zero_type,matrices=Ts))
        profiles.append(dict(OS=raw['OS'],profile=raw['profile'],d=d,candidates=len(candidates),
                             accepted=len(accepted),zero_markers=len(places),initial_rows=len(accepted)*len(places)))
        print(raw['OS'],raw['profile'],'d',d,'candidates',len(candidates),'accepted',len(accepted),
              'zero markers',len(places),'initial rows',len(accepted)*len(places))
    for raw in RAW['rows']:
        accepted={(p['a'],p['b']) for p in pairs if (p['OS'],p['profile'])==(raw['OS'],raw['profile'])}
        assert accepted==os_pairs[raw['OS']]
    print('Candidate pairs:',total_candidates,'; accepted marked profile-pairs:',len(pairs),'; initial rows:',len(initial))
    for os,ps in sorted(os_pairs.items()):print('OS',os,'ordered pairs',sorted(ps))
    print('All full integer four-period tuples have product I, preserve delta and preserve chi.')
    print('No target proof or historical whole-fibre catalogue was read.')
    data=dict(method='Direct degree-zero component criterion and exact adjugate/unipotent component orders; freshly reconstructed integral Poincare lifts.',
              total_candidates=total_candidates,accepted_pairs=len(pairs),initial_rows=len(initial),
              profile_counts=profiles,ordered_pairs=pairs,rows=initial)
    (HERE/'S6_SERIES_PUBLISH_III_02KT_fresh_maps.json').write_text(json.dumps(data,indent=2)+'\n',newline='\n')
    with (HERE/'S6_SERIES_PUBLISH_III_02KT_fresh_pairs.tsv').open('w',newline='') as f:
        fields=['OS','profile','d','a','b','number_of_zero_markers','component_tests']
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader()
        for p in pairs:
            q=dict(p);q['component_tests']=json.dumps(q['component_tests'],separators=(',',':'));w.writerow(q)


if __name__=='__main__':main()
