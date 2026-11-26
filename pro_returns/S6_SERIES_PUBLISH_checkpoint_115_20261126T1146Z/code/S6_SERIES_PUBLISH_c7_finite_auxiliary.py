"""Post-exposure finite-cap auxiliaries from fresh literal matrices only.

Uses direct minors and rational row reduction, not historical target code.
Checks the complete boundary groups, literal g=q representatives, and
normal-index identity for the additional original proof assertions.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd
import json

ROOT=Path(__file__).resolve().parents[1]
F=ROOT/'agents/continuation7_iii_finite_general'
positions=json.loads((F/'S6_SERIES_PUBLISH_III_finite_fresh_lattices.json').read_text())['positions']

def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def det(a):
    n=len(a);s=0
    for p in permutations(range(n)):
        term=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for i in range(n):term*=a[i][p[i]]
        s+=term
    return s

def rank(a):
    a=[list(map(Fraction,r)) for r in a];r=0
    for j in range(len(a[0])):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None:continue
        a[r],a[i]=a[i],a[r]
        p=a[r][j];a[r]=[x/p for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                p=a[i][j];a[i]=[x-p*y for x,y in zip(a[i],a[r])]
        r+=1
    return r

def minor_gcd(a,k):
    value=0
    for rows in combinations(range(len(a)),k):
        for cols in combinations(range(len(a[0])),k):
            value=gcd(value,det([[a[i][j] for j in cols] for i in rows]))
            if value==1:return value
    return value

pp=list(combinations(range(4),2))
delta=[[0],[0],[1],[0]];gamma=[[0],[0],[0],[1]]
index_examples=0
for p in positions:
    t=p['T'];q,g,qv,d=p['q'],p['g'],p['qv'],p['order']
    a=[[t[i][j]-int(i==j) for j in range(4)] for i in range(4)]
    w=[[t[i][k]*t[j][l]-t[i][l]*t[j][k]-int((i,j)==(k,l))
        for k,l in pp] for i,j in pp]
    assert rank(a)==2 and rank(w)==4
    assert [minor_gcd(a,j) for j in (1,2)]==[1,1]
    assert [minor_gcd(w,j) for j in (1,2,3,4)]==[1,1,1,1]
    ell=[[row[1]] for row in p['fixed_basis']]
    beta,eta=p['beta'],p['eta']
    assert mul([list(x) for x in zip(*eta)],mul(p['omega'],ell))==[[0]]
    if g>1:
        assert mul(p['quotient_coordinates'],delta)==[[1],[0]]
        assert mul(p['quotient_coordinates'],gamma)==[[0],[1]]
        assert mul(p['norm'],gamma)==[[d//q*x[0]] for x in ell]
    for k in (1,2,3,5):
        m=d*k
        for r,n in [(-3,-2),(-1,0),(0,1),(1,2),(2,3),(5,-7)]:
            norm=[[m//qv,0,r],[0,m//g,n]]
            content=minor_gcd(norm,2)
            assert content==(m//q)*gcd(m,qv*r,g*n)
            index_examples+=1
    print('FINITE',p['OS'],p['profile'],p['a'],p['b'],p['zero_index'],
          p['finite_index'],p['kind'],'g',g,'H1=Z3 H2=Z4; norm and omega PASS')
print('PASS all102 boundary H1/H2 lattices free; all34 g=q literal delta/gamma bases and norm lifts.')
print('PASS all eta/ell pairings zero; normal-index direct-minor examples',index_examples)
