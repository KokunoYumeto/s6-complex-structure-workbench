#!/usr/bin/env python3
"""Exact A2 fan labels for the conductor and primitive gamma loop."""
from pathlib import Path
import json
import sympy as S

e1=S.Matrix([1,0]); e2=S.Matrix([0,1]); zero=S.zeros(2,1)
B=S.Matrix([[0,1],[-1,0]])
directions=[e1-e2,e1,e2,e2-e1,-e1,-e2]
def pts(values):
    return {tuple(map(int,v)) for v in values}
def L(v): return pts([v,v+e1,v+e2])
def U(v): return pts([v+e1,v+e2,v+e1+e2])
expected=[U(-e2),L(zero),U(-e1),L(-e1),U(-e1-e2),L(-e2)]
for i in range(6):
    assert pts([zero,directions[i],directions[(i+1)%6]])==expected[i]
gamma=S.Matrix([1,0]); u=S.Matrix([0,1])
a_label=B.inv()*e1
b_label=B.inv()*(e1-e2)
assert a_label==u and b_label==gamma+u
assert a_label-b_label==-gamma
assert B*gamma==-e2 and B*u==e1
assert B*e2==gamma
assert S.Matrix.hstack(a_label,b_label).det()==-1
data={
 'status':'PASS',
 'vertex_triangles':['U_-e2','L_0','U_-e1','L_-e1','U_-e1-e2','L_-e2'],
 'a_period':[int(x) for x in a_label],
 'b_period':[int(x) for x in b_label],
 'normalization_circle_period':[int(x) for x in a_label-b_label],
 'marking_determinant':-1,
 'period_order':['gamma','u'],
 'normal_line_degrees':[-1,-1],
 'tensor_normal_degree':-2,
 'scope':'finite marked fan computation; normal-bundle and immersion proof is in C.3.11',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
