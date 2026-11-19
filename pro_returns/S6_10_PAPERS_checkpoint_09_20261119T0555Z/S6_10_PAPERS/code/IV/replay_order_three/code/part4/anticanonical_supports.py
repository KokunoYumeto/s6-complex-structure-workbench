#!/usr/bin/env python3
"""Exact checks for the complete minimal rational-surface case split in P4.21.

The geometric completeness proof is in notes/part4_ruled_extension.md.
A point records every local branch, including repeated component indices.
The finite blowup check covers reduced normal-crossing initial cases through
four blowups; arbitrary depth is established by the coefficient formula.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def invariants(genera, coefficients, points):
    c=len(genera)
    graph_rank=sum(len(p)-1 for p in points)-c+1
    assert graph_rank>=0
    e=2*c-2*sum(genera)-sum(len(p)-1 for p in points)
    group=('1' if graph_rank==0 else 'Z' if graph_rank==1 else f'F{graph_rank}') if not any(genera) else 'Z^2' if sum(genera)==1 and graph_rank==0 else 'other'
    return dict(components=c, graph_rank=graph_rank, euler=e, pi1=group,
                reduced=all(x==1 for x in coefficients),
                all_normalizations_rational=not any(genera))

models=[]
def add(name, genera, coefficients, points, nc):
    inv=invariants(genera,coefficients,points)
    assert inv['pi1'] in ('1','Z','Z^2')
    if inv['pi1']!='1':
        assert inv['reduced'] and nc
    else:
        assert inv['all_normalizations_rational']
    models.append(dict(name=name,genera=genera,coefficients=coefficients,
                       branch_points=points,normal_crossings=nc,**inv))

add('P2: smooth cubic',[1],[1],[],True)
add('P2: nodal cubic',[0],[1],[[0,0]],True)
add('P2: cuspidal cubic',[0],[1],[],False)
add('P2: transverse conic and line',[0,0],[1,1],[[0,1],[0,1]],True)
add('P2: tangent conic and line',[0,0],[1,1],[[0,1]],False)
add('P2: triangle',[0,0,0],[1,1,1],[[0,1],[1,2],[2,0]],True)
add('P2: concurrent three lines',[0,0,0],[1,1,1],[[0,1,2]],False)
add('P2: double line and line',[0,0],[2,1],[[0,1]],True)
add('P2: triple line',[0],[3],[],True)
add('Fe: two sections, two transverse intersections',[0,0],[1,1],[[0,1],[0,1]],True)
add('Fe: two tangent sections',[0,0],[1,1],[[0,1]],False)
add('Fe: two sections and fibre, three distinct points',[0,0,0],[1,1,1],[[0,1],[0,2],[1,2]],True)
add('Fe: two sections and fibre, common point',[0,0,0],[1,1,1],[[0,1,2]],False)
add('Fe: two disjoint sections and double fibre',[0,0,0],[1,1,2],[[0,2],[1,2]],True)
add('Fe: two disjoint sections and two fibres',[0,0,0,0],[1,1,1,1],[[0,2],[1,2],[0,3],[1,3]],True)
add('Fe: smooth elliptic bisection',[1],[1],[],True)
add('Fe: nodal bisection',[0],[1],[[0,0]],True)
add('Fe: cuspidal bisection',[0],[1],[],False)
add('Fe: rational bisection and transverse fibre',[0,0],[1,1],[[0,1],[0,1]],True)
add('Fe: rational bisection and tangent fibre',[0,0],[1,1],[[0,1]],False)
# Double-section family: geometry permits arbitrary effective vertical weights.
for v in range(0,5):
    for a in range(1,5):
        add(f'Fe: double section with {v} fibres of weight {a}',
            [0]*(v+1),[2]+[a]*v,[[0,j] for j in range(1,v+1)],True)

checks=0
for model in models:
    if model['pi1']=='1':
        continue
    initial=(tuple(model['genera']),tuple(model['coefficients']),
             tuple(tuple(p) for p in model['branch_points']))
    layer={initial}
    for depth in range(5):
        following=set()
        for gs,cs,ps in layer:
            inv=invariants(gs,cs,ps)
            assert inv['pi1']==model['pi1'] and all(c==1 for c in cs)
            checks+=1
            # Smooth coefficient-one centres add no conductor component.
            following.add((gs,cs,ps))
            # Each node blowup inserts one coefficient-one exceptional P1.
            for idx,p in enumerate(ps):
                assert len(p)==2
                i,j=p; e=len(gs)
                c_new=cs[i]+cs[j]-1
                points=ps[:idx]+ps[idx+1:]+((i,e),(j,e))
                following.add((gs+(0,),cs+(c_new,),tuple(sorted(points))))
        layer=following

result=dict(minimal_models_checked=len(models),
            arbitrary_double_section_family_sample_bounds={'vertical_fibres':[0,4],'common_weight':[1,4]},
            reduced_nc_blowup_depth_bound=4,
            reduced_nc_blowup_states_checked=checks,
            nontrivial_pi1_always_reduced_nc=True,
            simply_connected_case_has_only_rational_normalizations=True,
            models=models)
(ROOT/'anticanonical_supports.json').write_text(json.dumps(result,indent=2)+'\n')
print('Complete minimal-surface case split: 20 named incidence types, plus bounded double-section samples.')
print(f'Model instances checked: {len(models)}')
print(f'Reduced-NC blowup states through depth 4 checked: {checks}')
print('Every nontrivial pi1 case is reduced NC with group Z or Z^2.')
print('Every other case has pi1=1 and only rational normalized components.')
print('All exact integer assertions passed.')
