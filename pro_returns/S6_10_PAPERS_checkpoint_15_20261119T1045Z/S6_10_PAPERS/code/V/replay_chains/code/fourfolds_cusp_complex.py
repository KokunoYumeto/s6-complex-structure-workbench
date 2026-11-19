"""Exact integral normalization complex of the rank-three Kuhn cusp.

The bounded enumeration is complete: a tetrahedron containing 0 belongs to
one of the eight unit cubes with lower vertex in {-1,0}^3.  Its ordering is
one of the six permutations.  All chain matrices are integral.
"""
from itertools import product, permutations, combinations
from sympy import Matrix, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form
from pathlib import Path
import json

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
origin=(0,0,0)
unit=[(1,0,0),(0,1,0),(0,0,1)]
cones=set()
tetra=[]
for m in product((-1,0),repeat=3):
    for p in permutations(range(3)):
        verts=[m]
        for i in p: verts.append(add(verts[-1],unit[i]))
        if origin in verts:
            rays=tuple(sorted(v for v in verts if v!=origin))
            assert abs(Matrix.hstack(*map(Matrix,rays)).det())==1
            cones.add(rays)
for p in permutations(range(3)):
    verts=[origin]
    for i in p: verts.append(add(verts[-1],unit[i]))
    tetra.append(tuple(verts))
rays=sorted(set(v for c in cones for v in c))
edges=[v for v in product((0,1),repeat=3) if v!=origin]
triangles=sorted((origin,v,u) for v in edges for u in edges
                 if v!=u and all(a<=b for a,b in zip(v,u)))
assert len(cones)==24 and len(rays)==14 and len(triangles)==12
pic_rays=[v for v in rays if v not in unit]

stars={}
for v in edges:
    pairs=[tuple(w for w in c if w!=v) for c in cones if v in c]
    adjacent=sorted(set(w for pair in pairs for w in pair))
    bas=next(pair for pair in pairs
             if abs(Matrix.hstack(Matrix(v),*map(Matrix,pair)).det())==1)
    rem=[w for w in adjacent if w not in bas]
    stars[v]=(pairs,adjacent,bas,rem)
target=[(v,w) for v in edges for w in stars[v][3]]
assert len(target)==22

def global_coeff(v,j):
    return int(v==pic_rays[j])

D02=zeros(22,11)
for j in range(11):
    a=lambda v:global_coeff(v,j)
    for v in edges:
        _,_,bas,rem=stars[v]
        mat=Matrix([v,bas[0],bas[1]])
        mp=mat.inv()*Matrix([a(v),a(bas[0]),a(bas[1])])
        matn=Matrix([neg(v),sub(bas[0],v),sub(bas[1],v)])
        mn=matn.inv()*Matrix([a(neg(v)),a(sub(bas[0],v)),a(sub(bas[1],v))])
        for w in rem:
            val=a(w)-(Matrix(w).dot(mp))-a(sub(w,v))+Matrix(sub(w,v)).dot(mn)
            D02[target.index((v,w)),j]=val

def degree_row(v,w):
    pairs,adjacent,bas,rem=stars[v]
    ns=[p[1] if p[0]==w else p[0] for p in pairs if w in p]
    assert len(ns)==2
    coeff=Matrix.hstack(Matrix(w),Matrix(v)).gauss_jordan_solve(Matrix(add(*ns)))[0]
    b=coeff[0]
    row=zeros(1,22)
    for r,c in [(ns[0],1),(ns[1],1),(w,-b)]:
        if r in rem:row[0,target.index((v,r))]+=c
    return row

D12=zeros(12,22)
D10=zeros(12,7)
for i,(_,v,u) in enumerate(triangles):
    D12[i,:]=degree_row(sub(u,v),neg(v))-degree_row(u,v)+degree_row(v,u)
    D10[i,edges.index(sub(u,v))]+=1
    D10[i,edges.index(u)]-=1
    D10[i,edges.index(v)]+=1
assert D12*D02==zeros(12,11)

D20=zeros(6,12)
for i,verts in enumerate(tetra):
    for j in range(4):
        face=[v for k,v in enumerate(verts) if k!=j]
        first=face[0]
        normalized=tuple(sub(v,first) for v in face)
        D20[i,triangles.index(normalized)]+=(-1)**j
assert D20*D10==zeros(6,7)

# Degree-four restriction is dual to the span of paired divisor differences.
# Pic(E)=Z^14 / the three character relations.  Gauge coefficients of e_i to 0.
D04=zeros(7,11)
for i,v in enumerate(edges):
    co={r:int(r==v)-int(r==neg(v)) for r in rays}
    linear=Matrix([co[e] for e in unit])
    for j,r in enumerate(pic_rays):
        D04[i,j]=co[r]-Matrix(r).dot(linear)

def invariants(m):
    snf=smith_normal_form(m,domain=ZZ)
    return [abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]

data={name:{'shape':list(m.shape),'rank':m.rank(),'smith_nonzero':invariants(m),
            'matrix':[list(map(int,m.row(i))) for i in range(m.rows)]}
      for name,m in [('q0_d1',D10),('q0_d2',D20),('q2_d0',D02),
                    ('q2_d1',D12),('q4_d0',D04)]}
for name,item in data.items():
    print(name,'shape',item['shape'],'rank',item['rank'],'SNF',item['smith_nonzero'])
    assert all(x==1 for x in item['smith_nonzero'])
a,b,c=D02.rank(),D12.rank(),D04.rank()
betti=[1,7-D10.rank(),12-D10.rank()-D20.rank()+11-a,
       6-D20.rank()+22-a-b,12-b+11-c,7-c,1]
print('Kuhn quotient f-vector:',[1,7,12,6])
print('Central fibre integral Betti numbers:',betti)
print('Central fibre Euler characteristic:',sum((-1)**q*n for q,n in enumerate(betti)))
assert betti==[1,3,9,9,10,3,1]
data['betti']=list(map(int,betti))
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
