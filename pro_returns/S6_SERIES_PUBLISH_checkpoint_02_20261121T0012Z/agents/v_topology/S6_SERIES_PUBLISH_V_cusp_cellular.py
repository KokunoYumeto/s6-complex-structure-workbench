#!/usr/bin/env python3
"""Reconstruct the marked Kuhn cusp integral spectral sequence from cells.

All faces and incidences are generated directly from six unit-cube chains.
Integral quotient markings, kernels, homology and collapse images use full
Smith transformations. No prior program or saved certificate is imported.
"""
from itertools import combinations,permutations
from math import comb
import json
from datetime import datetime,timezone
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


def smith(A):
    if A.rows==0:
        return A,sp.eye(0),sp.eye(A.cols),0,[]
    if A.cols==0:
        return A,sp.eye(A.rows),sp.eye(0),0,[]
    d,u,v=smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(sp.ZZ))
    d,u,v=[z.to_Matrix() for z in (d,u,v)]
    assert d==u*A*v and abs(u.det())==abs(v.det())==1
    r=sum(d[i,i]!=0 for i in range(min(d.shape)))
    return d,u,v,r,[abs(int(d[i,i])) for i in range(r)]


def ext(A,k):
    rr=list(combinations(range(A.rows),k));cc=list(combinations(range(A.cols),k))
    return sp.Matrix(len(rr),len(cc),lambda i,j:A.extract(rr[i],cc[j]).det())


def canonical(vertices):
    vs=sorted(vertices)
    base=vs[0]
    return tuple(tuple(v[i]-base[i] for i in range(3)) for v in vs)


cells=[set() for _ in range(4)]
for perm in permutations(range(3)):
    vertices=[(0,0,0)];v=[0,0,0]
    for i in perm:
        v[i]=1;vertices.append(tuple(v))
    for dim in range(4):
        for face in combinations(vertices,dim+1):cells[dim].add(canonical(face))
cells=[sorted(c) for c in cells]
assert [len(c) for c in cells]==[1,7,12,6]

quot={};section={}
for dim,cs in enumerate(cells):
    for sigma in cs:
        L=sp.Matrix(3,dim,lambda i,j:sigma[j+1][i])
        dl,ul,vl,r,f=smith(L)
        assert r==dim and f==[1]*dim
        Q=ul[dim:,:];S=ul.inv()[:,dim:]
        assert Q*L==sp.zeros(3-dim,dim) and Q*S==sp.eye(3-dim)
        quot[sigma]=Q;section[sigma]=S

incidences=[]
for p in range(3):
    for it,tau in enumerate(cells[p+1]):
        for j in range(p+2):
            face=canonical(tau[:j]+tau[j+1:])
            isg=cells[p].index(face)
            incidences.append((p,it,isg,(-1)**j))
assert len(incidences)==74

D={}
for q in range(4):
    for p in range(4):
        indim=comb(3-p,q) if q<=3-p else 0
        outdim=comb(2-p,q) if p<3 and q<=2-p else 0
        inrank=len(cells[p])*indim
        outrank=len(cells[p+1])*outdim if p<3 else 0
        mat=sp.zeros(outrank,inrank)
        if p<3 and outdim:
            for pp,it,isg,sign in incidences:
                if pp!=p:continue
                tau=cells[p+1][it];sigma=cells[p][isg]
                block=sign*ext(quot[tau]*section[sigma],q)
                for i in range(outdim):
                    for j in range(indim):mat[it*outdim+i,isg*indim+j]+=block[i,j]
        D[p,q]=mat
    for p in range(3):assert D[p+1,q]*D[p,q]==sp.zeros(D[p+1,q].rows,D[p,q].cols)

hom={};table=[];images=[]
for q in range(4):
    row=[]
    for p in range(3,-1,-1):
        A=D[p,q];n=A.cols
        B=D[p-1,q] if p>0 else sp.zeros(n,0)
        da,ua,va,ra,fa=smith(A)
        binv=va.inv()*B
        assert binv[:ra,:]==sp.zeros(ra,B.cols)
        R=binv[ra:,:]
        dr,ur,vr,rr,fr=smith(R)
        assert all(z==1 for z in fr)
        rank=n-ra-rr
        row.append(rank)
        proj=ur[rr:,:]*va.inv()[ra:,:]
        hom[p,q]=(proj,rank)
        # Poincare-dual Alexander--Whitney cup cocycle for base cycles.
        d=3-p
        bs=list(combinations(range(3),d));angs=list(combinations(range(3),q))
        F=sp.zeros(n,len(bs)*len(angs))
        for isg,sigma in enumerate(cells[p]):
            qq=ext(quot[sigma],q)
            blocksize=qq.rows
            for jb,J in enumerate(bs):
                Jc=tuple(i for i in range(3) if i not in J)
                perm=J+Jc
                invs=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
                coefficient=(-1)**invs
                for r in range(1,p+1):coefficient*=sigma[r][Jc[r-1]]-sigma[r-1][Jc[r-1]]
                for ja,I in enumerate(angs):
                    col=jb*len(angs)+ja
                    for l in range(blocksize):F[isg*blocksize+l,col]=coefficient*qq[l,ja]
        assert A*F==sp.zeros(A.rows,F.cols)
        Hmap=proj*F
        df,uf,vf,rf,ff=smith(Hmap)
        assert all(z==1 for z in ff)
        expected_extra=int((d,q)==(2,2))
        assert rank-rf==expected_extra
        images.append({'base_degree':d,'angular_degree':q,'target_rank':rank,'image_rank':rf,'nonzero_smith_factors':ff,'cokernel_free_rank':rank-rf})
    table.append(row)
assert table==[[1,3,3,1],[0,6,8,3],[0,0,7,3],[0,0,0,1]]
betti=[0]*7;collapse=[0]*7
for item in images:
    k=item['base_degree']+item['angular_degree']
    if k<=6:
        betti[k]+=item['target_rank'];collapse[k]+=item['image_rank']
assert betti==[1,3,9,9,10,3,1]
assert collapse==[1,3,9,9,9,3,1]
U=sp.eye(6)+sp.zeros(3).row_join(sp.eye(3)).col_join(sp.zeros(3,6))
coinv=[comb(6,k)-(ext(U,k)-sp.eye(comb(6,k))).rank() for k in range(7)]
assert coinv==collapse
print(json.dumps({'computed_utc':datetime.now(timezone.utc).isoformat(),'cell_counts_by_dimension':[len(c) for c in cells],'codimension_one_incidences':len(incidences),'E2_ranks_rows_angular_cols_base':table,'all_E2_groups_free':True,'collapse_graded_maps':images,'central_fibre_betti':betti,'collapse_image_ranks':collapse,'monodromy_coinvariant_ranks':coinv,'only_collapse_cokernel':{'degree':4,'group':'Z'},'geometric_higher_differential_argument':'The base angular-identity section preserves E2_(3,0); all other possible higher arrows have zero source or target.'},indent=2))
