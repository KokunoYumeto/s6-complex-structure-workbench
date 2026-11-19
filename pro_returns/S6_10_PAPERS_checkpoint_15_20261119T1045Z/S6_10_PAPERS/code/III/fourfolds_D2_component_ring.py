"""Exact divisor-ring certificates for the triangular Mumford cap (D.2.47).

All sublattices L of Z^2 of index at most12 are enumerated by their unique
column Hermite form [[a,b],[0,d]], a*d=index, 0<=b<a.  This gives127 cases.
The proof in the companion TeX applies to arbitrary finite index; the
finite computation checks all local/global conventions, including loops,
multiple edges, repeated labels on triangles and Cartier self-gluings.
"""
from pathlib import Path
from collections import defaultdict
from itertools import product
import json
import sympy as S

ROOT=Path(__file__).resolve().parent
RAYS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
Q=[[-int(i==j)+int((i-j)%6 in (1,5)) for j in range(6)] for i in range(6)]


def clean(p):
    return {m:c for m,c in sorted(p.items()) if c}


def add(p,monomial,coefficient):
    p[tuple(sorted(monomial))]+=coefficient


def run(a,b,d):
    vertices=list(product(range(a),range(d)))
    index={v:i for i,v in enumerate(vertices)}
    n=a*d
    def vertex(x,y):
        quotient,yy=divmod(y,d)
        return index[((x-quotient*b)%a,yy)]
    adjacent=[[vertex(x+rx,y+ry) for rx,ry in RAYS] for x,y in vertices]
    triples=[]
    local=defaultdict(int)
    for i in range(n):
        A=[[int(adjacent[i][r]==j)-int(i==j) for j in range(n)] for r in range(6)]
        T=[[sum(A[r][j]*Q[r][s]*A[s][k] for r in range(6) for s in range(6))
            for k in range(n)] for j in range(n)]
        triples.append(T)
        for j,k in product(range(n),repeat=2):
            add(local,(i,j,k),T[j][k])
    for i,j,k in product(range(n),repeat=3):
        assert triples[i][j][k]==triples[j][i][k]==triples[k][i][j]
    for j,k in product(range(n),repeat=2):
        assert sum(triples[i][j][k] for i in range(n))==0

    cell=defaultdict(int)
    edges=[];triangles=[]
    for i,(x,y) in enumerate(vertices):
        add(cell,(i,i,i),6)
        for rx,ry in RAYS[:3]:
            j=vertex(x+rx,y+ry);edges.append((i,j))
            add(cell,(i,i,j),-3);add(cell,(i,j,j),-3)
        u=vertex(x+1,y);v=vertex(x,y+1);w=vertex(x+1,y+1)
        triangles.extend(((i,u,v),(w,u,v)))
        add(cell,(i,u,v),6);add(cell,(w,u,v),6)
    assert len(edges)==3*n and len(triangles)==2*n
    assert clean(local)==clean(cell)
    # Direct all-integer trilinear products, not divided evaluations.
    sparse_triples=[]
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                if triples[i][j][k]:
                    sparse_triples.append(dict(indices=[i,j,k],intersection=triples[i][j][k]))
    if a==1 and b==0:assert not clean(cell)
    if (a,b,d)==(2,0,2):
        assert triples[0][0][0]==6
        assert triples[0][0][1]==-2
        assert triples[0][1][2]==2
    return dict(HNF=[[a,b],[0,d]],index=n,vertices=vertices,adjacent=adjacent,
                edges=edges,triangles=triangles,
                cubic=[dict(indices=list(m),coefficient=c) for m,c in clean(cell).items()],
                symmetric_integral_trilinear=sparse_triples,
                constant_vector_annihilates=True,
                c2_on_each_component=0,p1_on_each_component=0)


def main():
    # Smooth complete toric hexagon: six(-1)-curves, adjacent pairing1.
    for i in range(6):
        prev=RAYS[(i-1)%6];cur=RAYS[i];nxt=RAYS[(i+1)%6]
        assert cur==(prev[0]+nxt[0],prev[1]+nxt[1])
        assert cur[0]*nxt[1]-cur[1]*nxt[0]==1
    Ksquare=sum(sum(row) for row in Q)
    assert Ksquare==6
    surface_c2=6
    total_c2=surface_c2-Ksquare
    total_p1=2*Ksquare-2*surface_c2
    assert total_c2==total_p1==0
    x,y,z=S.symbols('x y z',nonzero=True)
    logarithmic_volume=S.Matrix([[1/x,0,0],[0,1/y,0],[y*z,x*z,x*y]])
    assert logarithmic_volume.det()==1

    records=[];counts={}
    for n in range(1,13):
        before=len(records)
        for a in range(1,n+1):
            if n%a:continue
            d=n//a
            for b in range(a):records.append(run(a,b,d))
        counts[n]=len(records)-before
        assert counts[n]==sum(a for a in range(1,n+1) if n%a==0)
        print('INDEX',n,'HNFs',counts[n],'all integral symmetry/cell/constant tests PASS',flush=True)
    assert len(records)==127
    four=next(r for r in records if r['HNF']==[[2,0],[0,2]])
    result=dict(scope=__doc__,hnf_count=127,counts_by_index=counts,
                rays=RAYS,boundary_intersection_matrix=Q,
                normalization_c1_square=Ksquare,normalization_c2=surface_c2,
                component_c2_pairing=total_c2,component_p1_pairing=total_p1,
                holomorphic_volume_local_coefficient=1,rows=records)
    (ROOT/'fourfolds_D2_component_ring.json').write_text(json.dumps(result,indent=2)+'\n')
    print('diag(2,2) nonzero cubic:',four['cubic'],flush=True)
    print('ALL127 HNFs index<=12 PASS; diag(1,d) vanishes for all tested1<=d<=12')


if __name__=='__main__':main()
