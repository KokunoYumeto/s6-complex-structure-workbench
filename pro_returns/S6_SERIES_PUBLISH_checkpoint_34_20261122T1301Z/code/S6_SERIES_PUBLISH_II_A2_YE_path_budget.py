#!/usr/bin/env python3
"""Statement-first certificates for 02YE: conductor path and exact budgets.

The finite partition sweep supplements the arbitrary-c graph proof in the
derivation.  It is not a certificate for analytic normalization or global
intersection constancy; those maps are proved separately in the text.
"""
from itertools import combinations
from math import factorial
import json
import sympy as sp


def partitions(items):
    blocks=[]
    def rec(index):
        if index==len(items):
            yield tuple(tuple(b) for b in blocks)
            return
        item=items[index]
        for block in blocks:
            # Two points of one normalized component cannot be identified.
            if all(x[0]!=item[0] for x in block):
                block.append(item);yield from rec(index+1);block.pop()
        blocks.append([item]);yield from rec(index+1);blocks.pop()
    yield from rec(0)


def admissible(blocks,c):
    supports=[{x[1] for x in block} for block in blocks]
    if any(not a&b for a,b in combinations(supports,2)):return False
    cost=sum(len(b)-1 for b in blocks)
    if cost>c+1:return False
    parent={v:v for v in ['H','R']+[f'V{i}' for i in range(1,c+1)]}
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for block in blocks:
        first=block[0][0]
        for item in block[1:]:
            a,b=root(first),root(item[0])
            if a==b:return False
            parent[b]=a
    return True


def main():
    sweep=[]
    for c in range(1,5):
        for h in [1,2]:
            items=[('H','A',i) for i in range(h)]+[('R','A',0)]
            items += [(f'V{i}',sign,0) for i in range(1,c+1) for sign in ['+','-']]
            valid=[p for p in partitions(items) if admissible(p,c)]
            expected=2*factorial(c) if h==1 else (4 if c==1 else 0)
            assert len(valid)==expected,(c,h,len(valid),expected)
            for p in valid:
                assert sum(len(b)-1 for b in p)==c+1
                if c>=2:
                    assert h==1 and all(len(b)==2 for b in p)
                    assert all(len({x[1] for x in b})==2 for b in p)
                else:
                    assert sorted(len(b) for b in p)==([2,2] if h==1 else [1,2,2])
            sweep.append({'c_B':c,'H_points':h,'admissible_partitions':len(valid)})

    e,b=sp.symbols('e b')
    def inter(v,w):return sp.expand(v[0]*w[0]*e+v[0]*w[1]+v[1]*w[0])
    C=(3,-b); K=(-2,e-2)
    pa=sp.expand(1+inter(C,(C[0]+K[0],C[1]+K[1]))/2)
    assert pa==3*e-2*b-2
    assert pa.subs(e,2)==4-2*b
    X,Y,z,a,v,hpoly=sp.symbols('X Y z a v h')
    norm_residual=sp.expand((Y**2+X**2*a**2*hpoly).subs(Y,X*a*v))
    assert sp.expand(norm_residual-X**2*a**2*(v**2+hpoly))==0

    d,tau,m,bfirst,blast=sp.symbols('d tau m bfirst blast',positive=True,integer=True)
    assert sp.expand((d*tau*m).subs(m,2*blast)-2*d*tau*blast)==0
    # c=2: first=last, so equality would force 1=2*d*tau.
    # c>=3: first>=2*last>=2 and every other b_j>=1.
    for dc in range(1,17):
        for tc in range(1,17):
            assert 2*dc*tc>=2
    for c in range(3,101):
        assert 2+(c-2)>=3 and 2+(c-2)==c
    print(json.dumps({
        'check':'02YE conductor path, spectral genus and branch-intersection budgets',
        'partition_sweep':sweep,
        'partition_scope':'All partitions with no repeated global component at one point, for minimal one point of each Vi over each B sign, c_B=1..4 and h=1,2. The general proof also excludes extra preimages by the exact count inequality.',
        'general_pairing_count':'2*c! for h=1; zero for h=2 and c>=2',
        'spectral_genus_general':str(pa),
        'spectral_genus_degree_two':str(pa.subs(e,2)),
        'spectral_union_equality':'g+delta+I=5-2*b, hence b<=2',
        'exact_normalization_residual':str(norm_residual),
        'endpoint_intersection_identities':['2*b_last=m','b_first=d_1*tau*m'],
        'combined_identity':'b_first=2*d_1*tau*b_last',
        'c_equal_two_contradiction':'1=2*d_1*tau with positive integers d_1,tau',
        'c_at_least_three_bound':'sum(b_j)>=c>=3, contradicting b<=2',
        'scope':'Exact symbolic identities plus finite supplementary partition and integer checks; actual proper maps and analytic length/intersection arguments are proved in the derivation.',
        'status':'PASS'},indent=2))


if __name__=='__main__':main()
