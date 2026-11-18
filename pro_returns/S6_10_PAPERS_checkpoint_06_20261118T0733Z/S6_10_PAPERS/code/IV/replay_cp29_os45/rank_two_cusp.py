#!/usr/bin/env python3
"""Full integral rank-two Kuhn cusp and product-to-quotient collapse."""
from itertools import combinations, permutations
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ

r=2
def normalize(vertices):
    vertices=tuple(sorted(vertices,key=lambda v:(sum(v),v)))
    first=vertices[0]
    return tuple(tuple(v[i]-first[i] for i in range(r)) for v in vertices)
cells=[set() for _ in range(r+1)]
for perm in permutations(range(r)):
    vertex=[0]*r;simplex=[tuple(vertex)]
    for i in perm:vertex[i]=1;simplex.append(tuple(vertex))
    for p in range(r+1):
        for face in combinations(simplex,p+1):cells[p].add(normalize(face))
cells=[sorted(c) for c in cells]
assert [len(c) for c in cells]==[1,3,2]
Q={};S={}
for p in range(r+1):
    for i,c in enumerate(cells[p]):
        tangent=s.Matrix.hstack(*[s.Matrix(v) for v in c[1:]]) if p else s.zeros(r,0)
        for js in combinations(range(r),r-p):
            mat=tangent.row_join(s.eye(r)[:,list(js)])
            if abs(mat.det())==1:break
        else:raise AssertionError(c)
        Q[p,i]=mat.inv()[p:,:];S[p,i]=mat[:,p:]
def wedge(m,q):
    rows=list(combinations(range(m.rows),q));cols=list(combinations(range(m.cols),q))
    return s.Matrix(len(rows),len(cols),lambda i,j:m.extract(rows[i],cols[j]).det())
def snf(m):
    if min(m.shape)==0:return s.zeros(*m.shape),s.eye(m.rows),s.eye(m.cols)
    d,u,v=smith_normal_decomp(DomainMatrix.from_Matrix(m).convert_to(ZZ))
    d,u,v=d.to_Matrix(),u.to_Matrix(),v.to_Matrix()
    assert u*m*v==d and abs(u.det())==abs(v.det())==1
    return d,u,v
def presentation(a,b):
    assert a*b==s.zeros(a.rows,b.cols)
    d,u,v=snf(a);rank=a.rank();K=v[:,rank:]
    rel=(v.inv()*b)[rank:,:]
    rd,ru,rv=snf(rel);rr=rel.rank()
    assert all(abs(rd[i,i])==1 for i in range(rr))
    Z=K*ru.inv()[:,rr:];Pi=ru[rr:,:]*v.inv()[rank:,:]
    assert Pi*Z==s.eye(Z.cols)
    return Z,Pi
D={};result={'cells':cells,'quotients':{},'incidences':[],
             'differentials':{},'homology':{},'collapse':[]}
for p in range(r+1):
    for i,c in enumerate(cells[p]):
        result['quotients'][f'{p}.{i}']={'projection':Q[p,i].tolist(),'section':S[p,i].tolist()}
betti=[0]*(2*r+1)
for q in range(r+1):
    dims={p:int(len(cells[p])*s.binomial(r-p,q)) for p in range(r+1)}
    for p in range(r):
        matrix=s.zeros(dims[p+1],dims[p])
        dw=int(s.binomial(r-p-1,q));sw=int(s.binomial(r-p,q))
        for j,coface in enumerate(cells[p+1]):
            for k in range(p+2):
                face=normalize(coface[:k]+coface[k+1:]);i=cells[p].index(face)
                proj=Q[p+1,j]*S[p,i]
                matrix[j*dw:(j+1)*dw,i*sw:(i+1)*sw]+=(-1)**k*wedge(proj,q)
                if q==0:result['incidences'].append({'face':[p,i],'coface':[p+1,j],'omit':k,'sign':(-1)**k,'projection':proj.tolist()})
        D[p,q]=matrix
        sd,su,sv=snf(matrix)
        result['differentials'][f'{p},{q}']={'matrix':matrix.tolist(),'shape':list(matrix.shape),
                                          'Smith':sd.tolist(),'left':su.tolist(),'right':sv.tolist()}
    for p in range(r+1):
        a=D[p,q] if p<r else s.zeros(0,dims[p])
        b=D[p-1,q] if p else s.zeros(dims[p],0)
        Z,Pi=presentation(a,b)
        degree=r-p+q;betti[degree]+=Z.cols
        result['homology'][f'{p},{q}']={'degree':degree,'free':Z.cols,'torsion':[],
                                       'cycle_basis':Z.tolist(),'projection':Pi.tolist()}
assert betti==[1,2,4,2,1]

for q in range(r+1):
    sourceD={p:s.kronecker_product(D[p,0],s.eye(s.binomial(r,q))) for p in range(r)}
    collapse={p:s.diag(*[wedge(Q[p,i],q) for i in range(len(cells[p]))]) for p in range(r+1)}
    for p in range(r):assert D[p,q]*collapse[p]==collapse[p+1]*sourceD[p]
    for p in range(r+1):
        ns=int(len(cells[p])*s.binomial(r,q));nt=int(len(cells[p])*s.binomial(r-p,q))
        sa=sourceD[p] if p<r else s.zeros(0,ns)
        sb=sourceD[p-1] if p else s.zeros(ns,0)
        ta=D[p,q] if p<r else s.zeros(0,nt)
        tb=D[p-1,q] if p else s.zeros(nt,0)
        sz,spi=presentation(sa,sb);tz,tpi=presentation(ta,tb)
        H=tpi*collapse[p]*sz;hd,hu,hv=snf(H)
        assert H.rank()==H.rows
        assert all(abs(hd[i,i])==1 for i in range(H.rank()))
        result['collapse'].append({'p':p,'q':q,'degree':r-p+q,
                                  'chain_map':collapse[p].tolist(),
                                  'homology_map':H.tolist(),'shape':list(H.shape),
                                  'Smith':hd.tolist(),'left':hu.tolist(),'right':hv.tolist(),
                                  'cokernel_free':0,'cokernel_torsion':[]})
result['betti']=betti
result['higher_differentials']='None: the only possible d2 source at base degree2/fibre degree0 has target base degree0/fibre degree1 equal0.'
result['specialization']='Dual of the surjective primitive collapse; equal to the full integral invariant lattice in every degree.'
result['geometric_model']='The dual moment-polytope/angular-torus model and actual blowup-collapse comparison of P1.11, with r=2 and G=3I_2-11^t.'
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(result,indent=2,default=int)+'\n')
print('Cells',list(map(len,cells)),'incidences',len(result['incidences']))
print('Homology',betti,'all free')
for row in result['collapse']:
    print('collapse p,q,degree',row['p'],row['q'],row['degree'],'matrix',row['homology_map'],'onto with unit Smith factors')
print('Every differential, lattice quotient, collapse matrix and Smith transformation saved:',path)
