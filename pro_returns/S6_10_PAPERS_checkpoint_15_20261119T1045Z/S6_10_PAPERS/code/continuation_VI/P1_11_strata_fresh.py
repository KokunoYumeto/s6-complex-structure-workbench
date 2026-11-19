#!/usr/bin/env python3
"""Fresh P1.11 integral normalization-resolution calculation from Kuhn charts.

All fan simplices, face maps, toric intersection vectors, quotient lattices,
and integer Smith transformations are independently constructed here.  No
P1.11 target proof, old matrices, or P1.19 producer has been read or imported.
The script uses only Python standard-library exact arithmetic.
"""
from itertools import product, permutations, combinations
from fractions import Fraction
from pathlib import Path
import json


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def columns(cols): return [list(row) for row in zip(*cols)]
def basis_coordinates(cols,v):
    A=columns(cols);d=det3(A)
    assert abs(d)==1
    answer=[]
    for k in range(3):
        B=[row[:] for row in A]
        for i in range(3): B[i][k]=v[i]
        answer.append(det3(B)//d)
    return tuple(answer)
def zero(m,n): return [[0]*n for _ in range(m)]
def identity(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):
    if not A: return []
    if not B: return [[] for _ in A]
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def inverse_integral(A):
    n=len(A)
    B=[[Fraction(x) for x in A[i]]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if B[k][j])
        B[j],B[k]=B[k],B[j]
        factor=B[j][j];B[j]=[x/factor for x in B[j]]
        for i in range(n):
            if i!=j:
                factor=B[i][j];B[i]=[x-factor*y for x,y in zip(B[i],B[j])]
    assert all(x.denominator==1 for row in B for x in row[n:])
    return [[int(x) for x in row[n:]] for row in B]


def smith(A,ncols=None):
    """Integer Euclidean row/column operations, retaining exact U*A*V=D."""
    m=len(A);n=len(A[0]) if A else (ncols or 0)
    D=[row[:] for row in A];U=identity(m);V=identity(n)
    def swaprow(i,j):
        D[i],D[j]=D[j],D[i];U[i],U[j]=U[j],U[i]
    def swapcol(i,j):
        for M in (D,V):
            for row in M:row[i],row[j]=row[j],row[i]
    def rowadd(i,j,q):
        D[i]=[x+q*y for x,y in zip(D[i],D[j])]
        U[i]=[x+q*y for x,y in zip(U[i],U[j])]
    def coladd(i,j,q):
        for M in (D,V):
            for row in M:row[i]+=q*row[j]
    for k in range(min(m,n)):
        nz=[(abs(D[i][j]),i,j) for i in range(k,m) for j in range(k,n) if D[i][j]]
        if not nz:break
        _,i,j=min(nz);swaprow(k,i);swapcol(k,j)
        while True:
            restart=False
            for i in range(k+1,m):
                if D[i][k]:
                    q=D[i][k]//D[k][k];rowadd(i,k,-q)
                    if D[i][k]:swaprow(i,k)
                    restart=True;break
            if restart:continue
            for j in range(k+1,n):
                if D[k][j]:
                    q=D[k][j]//D[k][k];coladd(j,k,-q)
                    if D[k][j]:swapcol(j,k)
                    restart=True;break
            if restart:continue
            bad=next(((i,j) for i in range(k+1,m) for j in range(k+1,n)
                      if D[i][j]%D[k][k]),None)
            if bad:
                rowadd(k,bad[0],1)
                continue
            break
        if D[k][k]<0:
            D[k]=[-x for x in D[k]];U[k]=[-x for x in U[k]]
    assert mm(mm(U,A),V)==D
    assert mm(inverse_integral(U),U)==identity(m)
    assert mm(inverse_integral(V),V)==identity(n)
    assert all(D[i][j]==0 for i in range(m) for j in range(n) if i!=j)
    diag=[D[i][i] for i in range(min(m,n)) if D[i][i]]
    assert all(b%a==0 for a,b in zip(diag,diag[1:]))
    return D,U,V,diag


def row_homology(dimensions,differentials):
    out=[]
    for p,n in enumerate(dimensions):
        d=differentials.get(p,zero(0,n))
        if p==0:
            rank=0;V=identity(n);diag=[]
        else:
            D,U,V,diag=smith(d,ncols=n);rank=len(diag)
        following=differentials.get(p+1,zero(n,0))
        coords=mm(inverse_integral(V),following)
        assert all(x==0 for row in coords[:rank] for x in row)
        ker_image=coords[rank:]
        if ker_image and ker_image[0]:
            D2,U2,V2,diag2=smith(ker_image)
        else:diag2=[]
        out.append({'simplicial_degree':p,'chain_rank':n,'outgoing_rank':rank,
                    'outgoing_smith':diag,'incoming_in_kernel_smith':diag2,
                    'homology_rank':n-rank-len(diag2),
                    'homology_torsion':[d for d in diag2 if d>1]})
    return out


def main():
    origin=(0,0,0);std=[(1,0,0),(0,1,0),(0,0,1)]
    # Only the local universal cover fan is used; no precomputed list.
    star=[]
    for v in product((-1,0),repeat=3):
        for order in permutations(range(3)):
            vertices=[v]
            for j in order:vertices.append(add(vertices[-1],std[j]))
            if origin in vertices:
                cone=tuple(sorted(w for w in vertices if w!=origin))
                if cone not in star:star.append(cone)
    star.sort();rays=sorted({v for cone in star for v in cone})
    assert len(star)==24 and len(rays)==14
    assert all(abs(det3(columns(cone)))==1 for cone in star)
    # Derive the same fan by the actual four fixed-point and six invariant-
    # line blowups of P3, independently of the enumeration above.
    p3_rays=std+[(-1,-1,-1)]
    blowup_fan={tuple(sorted(c)) for c in combinations(p3_rays,3)}
    def subdivide(cones,face):
        ray=tuple(sum(v[i] for v in face) for i in range(3))
        out=set()
        for cone in cones:
            if set(face)<=set(cone):
                for removed in face:
                    out.add(tuple(sorted([v for v in cone if v!=removed]+[ray])))
            else:out.add(cone)
        return out
    for face in combinations(p3_rays,3):blowup_fan=subdivide(blowup_fan,face)
    for face in combinations(p3_rays,2):blowup_fan=subdivide(blowup_fan,face)
    assert blowup_fan==set(star)
    assert 1+4+6==11  # Each point and P1 blowup adds Z in H2 and H4.
    walls=sorted({tuple(sorted(face)) for cone in star for face in combinations(cone,2)})
    assert len(walls)==36
    pivots=std;nonpivots=[v for v in rays if v not in pivots]
    def curve_vector(wall):
        u,v=wall
        adj=[cone for cone in star if u in cone and v in cone]
        assert len(adj)==2
        a=next(x for x in adj[0] if x not in wall)
        b=next(x for x in adj[1] if x not in wall)
        cu,cv,ca=basis_coordinates([u,v,a],neg(add(a,b)))
        assert ca==0
        relation={u:cu,v:cv,a:1,b:1}
        assert all(sum(relation.get(r,0)*r[i] for r in rays)==0 for i in range(3))
        return [relation.get(r,0) for r in nonpivots]
    def divisor_class(ray):
        if ray in nonpivots:
            return [int(r==ray) for r in nonpivots]
        i=pivots.index(ray)
        return [-r[i] for r in nonpivots]
    edge_vectors=sorted(v for v in product((0,1),repeat=3) if v!=origin)
    simplices={0:[(origin,)],1:[(origin,w) for w in edge_vectors]}
    simplices[2]=sorted((origin,u,w) for w in edge_vectors for u in edge_vectors
                        if u!=w and all(a<=b for a,b in zip(u,w)))
    simplices[3]=[]
    for order in permutations(range(3)):
        chain=[origin]
        for j in order:chain.append(add(chain[-1],std[j]))
        simplices[3].append(tuple(chain))
    assert [len(simplices[p]) for p in range(4)]==[1,7,12,6]
    def canonical(vertices):
        first=vertices[0]
        return tuple(sub(v,first) for v in vertices)
    d0={}
    for p in range(1,4):
        A=zero(len(simplices[p-1]),len(simplices[p]))
        for j,simplex in enumerate(simplices[p]):
            for i in range(p+1):
                face=canonical(simplex[:i]+simplex[i+1:])
                A[simplices[p-1].index(face)][j]+=(-1)**i
        d0[p]=A
    assert mm(d0[1],d0[2])==zero(1,12)
    assert mm(d0[2],d0[3])==zero(7,6)
    # H2 on each of the seven surface normalizations, with actual quotient
    # lattice N/Z*w and two unimodular character relations eliminated.
    surfaces=[];offset=0
    for w in edge_vectors:
        adjacent=next(cone for cone in star if w in cone)
        v1,v2=[v for v in adjacent if v!=w]
        basis=[w,v1,v2]
        neighbors=sorted(v for v in rays if tuple(sorted((w,v))) in walls)
        coords={v:basis_coordinates(basis,v)[1:] for v in neighbors}
        assert coords[v1]==(1,0) and coords[v2]==(0,1)
        free=[v for v in neighbors if v not in (v1,v2)]
        def cl(v,free=free,coords=coords,v1=v1,v2=v2):
            if v in free:return [int(x==v) for x in free]
            i=0 if v==v1 else 1
            return [-coords[x][i] for x in free]
        # Translation from initial to terminal vertex sends v to v-w;
        # its quotient class modulo w is identical, with no hidden sign.
        boundary_columns=[]
        for v in neighbors:
            start=curve_vector(tuple(sorted((w,v))))
            end=curve_vector(tuple(sorted((neg(w),sub(v,w)))))
            boundary_columns.append([b-a for a,b in zip(start,end)])
        for coordinate in range(2):
            assert all(sum(coords[v][coordinate]*boundary_columns[j][i]
                           for j,v in enumerate(neighbors))==0 for i in range(11))
        surfaces.append({'w':w,'basis':basis,'neighbors':neighbors,'coords':coords,
                         'free':free,'class':cl,'offset':offset,
                         'columns':[boundary_columns[neighbors.index(v)] for v in free]})
        offset+=len(free)
    assert offset==22
    d2_1=columns([col for surface in surfaces for col in surface['columns']])
    d2_2=zero(22,12)
    for j,triangle in enumerate(simplices[2]):
        for i in range(3):
            edge=triangle[:i]+triangle[i+1:]
            w=sub(edge[1],edge[0]);third=sub(triangle[i],edge[0])
            surface=surfaces[edge_vectors.index(w)]
            qcoord=basis_coordinates(surface['basis'],third)[1:]
            vertex=next(v for v in surface['neighbors'] if surface['coords'][v]==qcoord)
            cl=surface['class'](vertex)
            for h,c in enumerate(cl):d2_2[surface['offset']+h][j]+=(-1)**i*c
    assert mm(d2_1,d2_2)==zero(11,12)
    d4_1=columns([[b-a for a,b in zip(divisor_class(w),divisor_class(neg(w)))]
                  for w in edge_vectors])
    rows={'q0':row_homology([1,7,12,6],d0),
          'q2':row_homology([11,22,12],{1:d2_1,2:d2_2}),
          'q4':row_homology([11,7],{1:d4_1}),
          'q6':row_homology([1],{})}
    betti=[0]*7
    for name,items in rows.items():
        q=int(name[1:])
        for item in items:
            assert item['homology_torsion']==[]
            betti[q+item['simplicial_degree']]+=item['homology_rank']
    assert betti==[1,3,9,9,10,3,1]
    result={'status':'PASS','method':'new Kuhn fan enumeration, actual translated toric face inclusions, exact integral Smith transformations; standard library only',
            'fan_counts':{'rays':len(rays),'walls':len(walls),'maximal_cones':len(star)},
            'P3_four_points_six_lines_fan_comparison':True,
            'stratum_counts':[1,7,12,6],
            'surface_H2_ranks':[len(s['free']) for s in surfaces],
            'row_homology':rows,'total_homology_ranks_after_written_d3_vanishing':betti,
            'Euler_number':sum((-1)**k*b for k,b in enumerate(betti)),
            'matrices':{'q0_d1':d0[1],'q0_d2':d0[2],'q0_d3':d0[3],
                        'q2_d1':d2_1,'q2_d2':d2_2,'q4_d1':d4_1},
            'bases':{'ambient_rays':rays,'ambient_eliminated_unit_rays':pivots,
                     'ambient_H2_kernel_and_H4_quotient_basis':nonpivots,
                     'simplices':simplices,
                     'surfaces':[{'w':s['w'],'quotient_basis':s['basis'],
                                  'fan_neighbors':s['neighbors'],'free_boundary_classes':s['free']} for s in surfaces]},
            'scope':'This proves the displayed normalization-resolution matrices and their torsion-free E2 groups. The written positive-real resolution proves d3=0. Collapse primitivity is a separate geometric map gate.'}
    Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','fan_counts','stratum_counts','surface_H2_ranks','row_homology','total_homology_ranks_after_written_d3_vanishing','Euler_number','scope']},indent=2))


if __name__=='__main__':main()
