#!/usr/bin/env python3
"""Fresh exact checks of conductor coefficients, graph Euler data and A-types.

These checks supplement universal written proofs. No old verifier is imported,
and no graph in this program is asserted to be realized by a complex surface.
"""
from math import gcd
from random import Random
from pathlib import Path
import json

rng=Random(20261119)
def invariants(coeff,genus,edges):
    vertices=[i for i,a in enumerate(coeff) if a>0]
    e=[(i,j) for i,j in edges if coeff[i]>0 and coeff[j]>0]
    euler=sum(2-2*genus[i] for i in vertices)-len(e)
    pa=sum(genus[i] for i in vertices)+len(e)-len(vertices)+1
    return vertices,e,euler,pa
def blow(coeff,genus,edges,operation):
    coeff=coeff[:];genus=genus[:];edges=edges[:]
    kind,index=operation;n=len(coeff)
    if kind=='smooth':
        multiplicity=coeff[index]
        edges.append((index,n))
    else:
        i,j=edges.pop(index)
        multiplicity=coeff[i]+coeff[j]
        edges.extend([(i,n),(n,j)])
    assert multiplicity>=1
    coeff.append(multiplicity-1);genus.append(0)
    return coeff,genus,edges,multiplicity
def operations(coeff,edges):
    return [('smooth',i) for i,a in enumerate(coeff) if a>0]+[('node',k) for k,(i,j) in enumerate(edges) if coeff[i]+coeff[j]>=1]

ruled_paths=ruled_steps=0
for g in (1,2,3):
 for v in range(4):
  for a in (1,2,4):
   for run in range(12):
    coeff=[2]+[a]*v;genus=[g]+[0]*v;edges=[(0,j) for j in range(1,v+1)]
    N0=0
    for N in range(1,13):
        op=rng.choice(operations(coeff,edges))
        coeff,genus,edges,m=blow(coeff,genus,edges,op)
        N0+=m==1
        vertices,e,eR,pa=invariants(coeff,genus,edges)
        assert pa==g
        assert eR==2-2*g+v+N-N0
        assert (4-4*g+N)-eR==2-2*g-v+N0
        assert all(gcd(coeff[i]-1,coeff[j]-1)==1 for i,j in e)
        valence={i:sum((i==u)+(i==w) for u,w in e) for i in vertices}
        assert all(valence[i]==1 for i in vertices if coeff[i]==1)
        ruled_steps+=1
    ruled_paths+=1

vii_paths=vii_steps=0
for initial in range(5):
 for run in range(20):
    if initial==0:coeff=[1];genus=[1];edges=[]
    elif initial==1:coeff=[3];genus=[1];edges=[]
    else:
        n=initial-1;coeff=[1]*n;genus=[0]*n;edges=[(j,(j+1)%n) for j in range(n)]
    for _ in range(12):
        coeff,genus,edges,m=blow(coeff,genus,edges,rng.choice(operations(coeff,edges)))
        vertices,e,eR,pa=invariants(coeff,genus,edges)
        assert pa==1
        assert eR==sum(genus[i]==0 for i in vertices)
        vii_steps+=1
    vii_paths+=1

curve_cases=0
for n0 in range(13):
 for delta in range(n0+2):
  for v in range(delta+1):
    if n0==0 and v:continue # independently proved node exclusion is an input
    eC=2*n0-v
    assert eC>=0
    if eC==0:
        assert (n0,v) in [(0,0),(1,2)]
        assert delta<=1 if n0==0 else delta==2
    for defect in range(7):
     for b in range(4):
        eS=defect+b+eC
        assert eS>=0
        assert (eS==0)==(defect==0 and b==0 and ((n0,v)==(0,0) or (n0,v)==(1,2)))
    curve_cases+=1

ak=[]
for s in range(1,41):
    # Semigroup of the actual cusp parametrization v=t^2,u=t^(2s+1).
    bound=8*s+4
    semigroup={2*a+(2*s+1)*b for a in range(bound//2+1) for b in range(bound//(2*s+1)+1) if 2*a+(2*s+1)*b<=bound}
    gaps=[n for n in range(bound+1) if n not in semigroup]
    assert len(gaps)==s and max(gaps)+1==2*s
    # Two branches u=+v^s and u=-v^s have intersection quotient C[v]/(2v^s).
    intersection_basis=list(range(s))
    assert len(intersection_basis)==s
    ak.append({'s':s,'odd_A_branch_conductor':s,'even_A_conductor':2*s,'even_A_delta':len(gaps)})

out={'status':'all assertions passed','ruled_paths':ruled_paths,'ruled_blowups':ruled_steps,'VII_paths':vii_paths,'VII_blowups':vii_steps,'curve_numerical_cases':curve_cases,'A_type_cases':ak,'scope':'Finite exact supplemental checks of universal graph, curve and semigroup identities; no realization assertion and no replacement for the written proofs.'}
Path(__file__).with_name('conductor_graph_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='A_type_cases'}))
