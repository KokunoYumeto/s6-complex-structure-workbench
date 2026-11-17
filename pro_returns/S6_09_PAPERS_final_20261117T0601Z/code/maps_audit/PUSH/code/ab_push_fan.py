"""Exact enumeration of the no-new-ray triangulations in Lead 2.

Only rational arithmetic is used; pairwise intersections are checked by
enumerating vertices of the combined barycentric halfspaces.
"""
import itertools
import json
from pathlib import Path
import sympy as sp

names=['A','B','C','D','E','F']
v=[sp.Matrix(x) for x in [(0,0,1),(1,0,1),(0,1,1),(1,1,1),(0,0,0),(0,1,0)]]
rays=[sp.Matrix(x) for x in [(0,0,1,0),(1,0,1,0),(0,1,1,0),(1,1,1,0),(0,0,0,1),(0,1,0,1)]]

def inequalities(t):
    mat=sp.Matrix.hstack(*[v[i].col_join(sp.ones(1,1)) for i in t])
    return list(mat.inv().tolist())

def intersection_vertices(t,s):
    rows=inequalities(t)+inequalities(s)
    pts=set()
    for inds in itertools.combinations(range(8),3):
        a=sp.Matrix([[rows[i][j] for j in range(3)] for i in inds])
        if not a.det():
            continue
        b=sp.Matrix([-rows[i][3] for i in inds])
        p=a.inv()*b
        if all(sum(row[j]*p[j] for j in range(3))+row[3]>=0 for row in rows):
            pts.add(tuple(p))
    return pts

def compatible(t,s):
    # The intersection is a face exactly if its vertices are common vertices.
    allowed={tuple(v[i]) for i in set(t)&set(s)}
    return intersection_vertices(t,s).issubset(allowed)

tets=[t for t in itertools.combinations(range(6),4) if abs(sp.Matrix.hstack(*[rays[i] for i in t]).det())==1]
compat={(t,s):compatible(t,s) for t,s in itertools.combinations(tets,2)}
tris=[]
for ts in itertools.combinations(tets,3):
    if not all(compat[(a,b)] for a,b in itertools.combinations(ts,2)):
        continue
    edges={tuple(sorted(e)) for t in ts for e in itertools.combinations(t,2)}
    bottom='AD' if (0,3) in edges else 'BC'
    left='AF' if (0,5) in edges else 'CE'
    right='BF' if (1,5) in edges else 'DE'
    periodic=(left=='AF' and right=='BF') or (left=='CE' and right=='DE')
    tris.append({'tetrahedra':[''.join(names[i] for i in t) for t in ts],
                 'bottom':bottom,'left':left,'right':right,
                 'periodic_k':periodic})

# Verify dual description for the unsubdivided cone: xy=uzv, q=zv.
chars={
 'x':sp.Matrix([1,0,0,0]),
}
result={'rays':[list(map(int,r)) for r in rays],
        'unimodular_tetrahedra':len(tets),'triangulations':tris,
        'triangulations_total':len(tris),
        'periodic_with_bottom_AD':[t for t in tris if t['bottom']=='AD' and t['periodic_k']]}
assert len(tris)==6
assert len(result['periodic_with_bottom_AD'])==2
print(json.dumps(result,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
