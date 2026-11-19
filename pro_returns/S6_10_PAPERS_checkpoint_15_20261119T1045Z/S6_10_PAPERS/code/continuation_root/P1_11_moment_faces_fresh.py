"""Exact character-set and face checks; P1.11 target proof remains unread."""
from pathlib import Path
from itertools import product, combinations, permutations
from functools import reduce
from math import gcd
import sympy as s
import json, datetime, hashlib
P=Path(__file__).resolve().parents[2]
G=4*s.eye(3)-s.ones(3)
normals=[s.Matrix(v) for v in product((0,1),repeat=3) if any(v)]
normals += [-v for v in normals]
b=[(v.T*G*v)[0] for v in normals] # inequalities for 2P
vertices=set()
unimodular_active=[]
for inds in combinations(range(14),3):
    Q=s.Matrix.vstack(*[normals[i].T for i in inds])
    if not Q.det(): continue
    v=Q.inv()*s.Matrix([b[i] for i in inds])
    if all((n.T*v)[0]<=c for n,c in zip(normals,b)):
        assert all(x.q==1 for x in v)
        vertices.add(tuple(int(x) for x in v))
        assert abs(Q.det())==1
        unimodular_active.append({'normals':inds,'det':int(Q.det())})
assert len(vertices)==24
pts={v for v in product(range(-3,4),repeat=3)
     if all(sum(int(n[j])*v[j] for j in range(3))<=int(c)
            for n,c in zip(normals,b))}
assert vertices<=pts

zero=(0,0,0);simplices=set()
for base in product((-1,0),repeat=3):
    for order in permutations(range(3)):
        v=list(base);vv=[tuple(v)]
        for i in order:
            v=v.copy();v[i]+=1;vv.append(tuple(v))
        if zero in vv:simplices.add(tuple(sorted(vv)))
assert len(simplices)==24
faces={}
for simplex in simplices:
    for k in range(1,5):
        for sigma in combinations(simplex,k):
            if zero in sigma: faces[sigma]=None
counts={str(k):sum(len(sig)==k+1 for sig in faces) for k in range(4)}
assert counts=={'0':1,'1':14,'2':36,'3':24}
face_records=[]
for sigma in sorted(faces):
    common=pts.copy()
    for v in sigma:
        shift=2*G*s.Matrix(v)
        shifted={tuple(p[j]+int(shift[j]) for j in range(3)) for p in pts}
        common &= shifted
    assert common
    other=[v for v in sigma if v!=zero]
    eq={p for p in pts if all(sum(v[j]*p[j] for j in range(3))==
                                  int((s.Matrix(v).T*G*s.Matrix(v))[0])
                                  for v in other)}
    assert common==eq
    # Actual fan ray limits minimize the characters -m, so select the
    # maximum face of m. This fixes the geometric sign of the presentation.
    outward=tuple(sum(v[j] for v in other) for j in range(3))
    height=max(sum(outward[j]*m[j] for j in range(3)) for m in pts)
    upper={m for m in pts if sum(outward[j]*m[j] for j in range(3))==height}
    assert upper==common
    m0=min(common)
    for m in common:
        for v in sigma:
            assert sum((m[j]-m0[j])*v[j] for j in range(3))==0
    if other:
        K=s.Matrix.hstack(*[s.Matrix(v) for v in other])
        rank=K.rank();minors=[]
        for rows in combinations(range(3),rank):
            for cols in combinations(range(K.cols),rank):
                minors.append(abs(int(K.extract(rows,cols).det())))
        assert reduce(gcd,minors)==1
    else:rank=0
    D=s.Matrix.hstack(*[s.Matrix([m[j]-m0[j] for j in range(3)]) for m in common])
    assert D.rank()==3-rank
    face_records.append({'simplex':sigma,'dimension':3-rank,
                         'common_character_count':len(common),
                         'character_origin':m0,'same_monomial_ratios':True})

a0,a1,a2,k,n0,n1,n2,v0,v1,v2=s.symbols('a0 a1 a2 k n0 n1 n2 v0 v1 v2')
a=s.Matrix([a0,a1,a2]);nu=s.Matrix([n0,n1,n2]);v=s.Matrix([v0,v1,v2])
assert all(s.expand(t)==0 for t in a+k*nu-k*(v+nu)-(a-k*v))
# Shared monomial weights are independent positive symbols. Translation of all
# exponent labels cancels in their ratios and translates the mean by G nu.
weights=s.symbols('w0:4',positive=True)
ms=[s.Matrix(u) for u in list(sorted(vertices))[:4]]
den=sum(weights)
mu=sum((w*m for w,m in zip(weights,ms)),s.zeros(3,1))/(2*den)
mut=sum((w*(m+2*G*nu) for w,m in zip(weights,ms)),s.zeros(3,1))/(2*den)
assert all(s.simplify(t)==0 for t in mut-mu-G*nu)
out={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':'new independent SymPy exact facet enumeration and common-character-set comparison; no producing program read',
 'G':[[int(x) for x in row] for row in G.tolist()],'det_G':int(G.det()),'dilated_vertices':sorted(vertices),
 'dilated_lattice_points':len(pts),'face_counts':counts,
 'unimodular_vertex_checks':len(unimodular_active),'face_checks':len(face_records),
 'faces':face_records,'deck_marking_identity':True,'universal_moment_translation_identity':True,
 'status':'passed'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['faces','dilated_vertices']},indent=2))
