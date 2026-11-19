#!/usr/bin/env python3
"""New exact normalization-incidence graph and Euler checks for RAT.3.

No previous graph code or producer is imported. All maps are the graph deletion
and edge-incidence operations described in the frozen geometric derivation.
"""
from collections import Counter
from itertools import combinations_with_replacement, product
from pathlib import Path
import json


def components(vertices, edges):
    adjacency={v:set() for v in vertices}
    for x,y in edges:
        if x in adjacency and y in adjacency:
            adjacency[x].add(y)
            adjacency[y].add(x)
    out=[]
    while adjacency:
        start=next(iter(adjacency))
        reached={start}
        todo=[start]
        while todo:
            x=todo.pop()
            for y in adjacency[x]:
                if y not in reached:
                    reached.add(y)
                    todo.append(y)
        for v in reached:
            del adjacency[v]
        out.append(reached)
    return out


def main():
    graph_count=0
    kept_edge_count=0
    beta_counts={0:0,1:0}
    extremal=[]
    for n in range(1,5):
        for q in range(1,4):
            vertices=list(range(n+q))
            types=[(i,n+j) for i in range(n) for j in range(q)]
            for beta in (0,1):
                num_edges=n+q-1+beta
                for ids in combinations_with_replacement(range(len(types)),num_edges):
                    counts=Counter(ids)
                    if max(counts.values())>2:
                        continue
                    edges=[types[i] for i in ids]
                    degree=Counter(x for edge in edges for x in edge)
                    if any(degree[n+j]<2 for j in range(q)):
                        continue
                    if len(components(vertices,edges))!=1:
                        continue
                    assert len(edges)-len(vertices)+1==beta
                    graph_count+=1
                    beta_counts[beta]+=1
                    remaining=components(vertices[1:],edges)
                    retained=[cc for cc in remaining if cc & set(range(1,n))]
                    c=len(retained)
                    relevant=set().union(*retained) if retained else set()
                    a=sum(1 for x,y in edges if x==0 and y in relevant)
                    assert c<=n-1
                    assert a-c<=beta
                    eG=2*n-sum(degree[n+j]-1 for j in range(q))
                    assert eG==n+1-beta
                    assert eG>=a
                    for k in range(a+1):
                        assert eG>=k
                        kept_edge_count+=1
                    if eG==a and len(extremal)<8:
                        extremal.append({'curves':n,'singular_points':q,
                                         'edges':edges,'beta':beta,'a':a,'eG':eG})
    arithmetic=0
    for r,N0,rdom in product(range(9),range(9),range(3)):
        if rdom>r:
            continue
        k=max(0,r-N0-rdom)
        # The least allowed e(G)=k is sufficient for the exact Euler bound.
        eS=2-r+N0+k
        assert eS>=2-rdom>=0
        arithmetic+=1
    conductor_cases=0
    for intrinsic in range(3):
        for number in range(4):
            for intersections in product(range(1,4),repeat=number):
                if intrinsic+sum(intersections)==2:
                    assert number<=2
                    conductor_cases+=1
    result={'status':'PASS','method':'New integral bipartite multigraph enumeration, exact vertex deletion and branch-edge counting',
            'connected_incidence_graphs':graph_count,'graphs_by_cycle_rank':beta_counts,
            'retained_edge_subcounts':kept_edge_count,'Euler_integer_cases':arithmetic,
            'coefficient_two_branch_cases':conductor_cases,'sharp_graph_examples':extremal,
            'scope':'Finite graph certificate and scalar arithmetic. Actual normalization, residue and ruling-fibre maps are proved in028_RAT3_before_read.md.'}
    Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='sharp_graph_examples'},indent=2))


if __name__=='__main__':
    main()
