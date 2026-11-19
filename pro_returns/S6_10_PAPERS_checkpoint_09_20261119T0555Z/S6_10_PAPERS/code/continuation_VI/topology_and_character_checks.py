#!/usr/bin/env python3
"""New 19-Nov continuation calculation, written from statements, stdlib only.
No earlier computation program is imported or read. Finite tests are labelled
as tests; exact identities and geometric proofs are in the review receipts.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, gcd
from random import Random
import json
from pathlib import Path


def eye(n):
    return [[Q(i==j) for j in range(n)] for i in range(n)]


def mul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def transpose(A):
    return list(map(list,zip(*A)))


def determinant(A):
    A=[list(map(Q,row)) for row in A]; d=Q(1)
    for i in range(len(A)):
        j=next((j for j in range(i,len(A)) if A[j][i]),None)
        if j is None:return Q(0)
        if j!=i:A[i],A[j]=A[j],A[i];d=-d
        p=A[i][i];d*=p
        for j in range(i+1,len(A)):
            t=A[j][i]/p
            for k in range(i,len(A)):A[j][k]-=t*A[i][k]
    return d


def rank(A):
    A=[list(map(Q,row)) for row in A]; r=0
    for c in range(len(A[0])):
        p=next((p for p in range(r,len(A)) if A[p][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];v=A[r][c]
        A[r]=[x/v for x in A[r]]
        for j in range(len(A)):
            if j!=r:
                t=A[j][c];A[j]=[x-t*y for x,y in zip(A[j],A[r])]
        r+=1
        if r==len(A):break
    return r


def inverse(A):
    n=len(A);B=[list(map(Q,a))+i for a,i in zip(A,eye(n))]
    for c in range(n):
        p=next(p for p in range(c,n) if B[p][c]);B[c],B[p]=B[p],B[c]
        v=B[c][c];B[c]=[x/v for x in B[c]]
        for j in range(n):
            if j!=c:
                t=B[j][c];B[j]=[x-t*y for x,y in zip(B[j],B[c])]
    return [r[n:] for r in B]


def power(A,n):
    B=eye(len(A))
    for _ in range(n):B=mul(B,A)
    return B


pairs=list(combinations(range(4),2))
B=[[Q(0) for _ in pairs] for _ in pairs]
for i,a in enumerate(pairs):
    for j,b in enumerate(pairs):
        seq=a+b
        if len(set(seq))==4:
            B[i][j]=(-1)**sum(seq[x]>seq[y] for x in range(4) for y in range(x+1,4))
rng=Random(20261119);parity_hist={}
for trial in range(400):
    A=eye(4)
    for _ in range(1+trial%9):
        i,j=rng.sample(range(4),2);a=rng.choice([-2,-1,1,2]);E=eye(4);E[i][j]=a;A=mul(E,A)
    if trial%3==0:
        A=mul([[-Q(i==j) for j in range(4)] for i in range(4)],A)
    assert determinant(A)==1
    G=[[A[i][k]*A[j][l]-A[i][l]*A[j][k] for k,l in pairs] for i,j in pairs]
    assert mul(mul(transpose(G),B),G)==B
    assert determinant(G)==1
    r=rank([[x-Q(i==j) for j,x in enumerate(row)] for i,row in enumerate(G)])
    assert r%2==0
    parity_hist[str(6-r)]=parity_hist.get(str(6-r),0)+1

# Toric periodic triangulation computed as a multicomplex, retaining loop edges.
def edge_key(a,b,N):
    forward=((a[0]%N,a[1]%1),(b[0]-a[0],b[1]-a[1]))
    reverse=((b[0]%N,b[1]%1),(a[0]-b[0],a[1]-b[1]))
    return min(forward,reverse)

toric=[]
for N in range(1,41):
    edges={};faces=[];vertices=set()
    for x in range(N):
        a=(x,0);b=(x+1,0);c=(x+1,1);d=(x,1)
        for tri in [(a,b,c),(a,c,d)]:
            area=(tri[1][0]-tri[0][0])*(tri[2][1]-tri[0][1])-(tri[1][1]-tri[0][1])*(tri[2][0]-tri[0][0])
            assert area==1;faces.append(tri)
            for p in tri:vertices.add((p[0]%N,p[1]%1))
            for i in range(3):
                e=edge_key(tri[i],tri[(i+1)%3],N);edges[e]=edges.get(e,0)+1
    assert set(edges.values())=={2}
    assert (len(vertices),len(edges),len(faces))==(N,3*N,2*N)
    toric.append({'index':N,'vertices':len(vertices),'edges':len(edges),'triangles':len(faces),'euler_support':len(faces)})

# Blowup cohomology: construct graded vector-space contributions, then alternate.
base=[1,4,7,8,7,4,1]
blowups=[]
for k in range(21):
    for m in range(21):
        b=base[:]
        for _ in range(k):
            for j,v in enumerate([1,4,1]):b[j+2]+=v
        for _ in range(m):b[2]+=1;b[4]+=1
        assert b==[1,4,7+k+m,8+4*k,7+k+m,4,1]
        e=sum((-1)**j*v for j,v in enumerate(b));assert e==2*(m-k)
        blowups.append({'curves':k,'points':m,'betti':b,'euler':e})
assert (comb(4-1,2),2-2*comb(4-1,2))==(3,-4)
negative_operation=[0,0,2,6,2,0,0]
assert sum((-1)**j*v for j,v in enumerate(negative_operation))==-2

# Exact rational augmentation character and Koszul contraction. The cyclotomic
# companion is multiplication by x modulo 1+x+...+x^(p-1).
character_tests=[]
for p in [2,3,5,7]:
    d=p-1;C=[[Q(0) for _ in range(d)] for _ in range(d)]
    for j in range(d-1):C[j+1][j]=1
    for i in range(d):C[i][d-1]=-1
    assert power(C,p)==eye(d)
    for exponents in [(1,0,0,0),(0,1,2,3),(p-1,p-1,0,1)]:
        ops=[]
        for a in exponents:
            M=power(C,a%p);ops.append([[x-Q(i==j) for j,x in enumerate(row)] for i,row in enumerate(M)])
        pivot=next(i for i,a in enumerate(exponents) if a%p)
        inv=inverse(ops[pivot]);assert mul(inv,ops[pivot])==eye(d)
        bases=[list(combinations(range(4),k)) for k in range(5)]
        # d(v⊗e_I)=Σ M_jv⊗e_j∧e_I; h= M_pivot^-1⊗ι_pivot.
        def apply(vec,degree,kind):
            out={}
            for (I,a),value in vec.items():
                if kind=='d':
                    moves=[(j,ops[j],(-1)**sum(i<j for i in I),tuple(sorted((j,)+I))) for j in range(4) if j not in I]
                else:
                    moves=[] if pivot not in I else [(pivot,inv,(-1)**I.index(pivot),tuple(i for i in I if i!=pivot))]
                for j,M,sign,J in moves:
                    for b in range(d):
                        out[J,b]=out.get((J,b),Q(0))+value*sign*M[b][a]
            return {k:v for k,v in out.items() if v}
        for degree in range(5):
            for I in bases[degree]:
                for a in range(d):
                    v={(I,a):Q(1)}
                    dh=apply(apply(v,degree,'h'),degree-1,'d')
                    hd=apply(apply(v,degree,'d'),degree+1,'h')
                    total=dh.copy()
                    for key,value in hd.items():total[key]=total.get(key,Q(0))+value
                    assert {k:v for k,v in total.items() if v}==v
        character_tests.append({'prime':p,'exponents':exponents,'dimension':d,'verified_identity':'dh+hd=1 in all five degrees'})

# INT.2 weighted unit removal and consecutive-root separation are exact rational
# exponent checks. They test 4,000 triples, not a numerical claim of universality.
weighted=[]
for a in range(1,21):
    for b in range(1,21):
        for n in range(1,11):
            den=2*(a+n*b)
            assert Q(2*a,den)+b*Q(2*n,den)==1
            separation=Q(b,a+n*b)
            assert 0<separation<1
            assert -Q(a,b)-n<0
            weighted.append((a,b,n))

out={'authorship':'New independent stdlib program, 19 November 2026; no inherited computation imported.',
     'interpretation':'Finite exact tests; universal conclusions are supplied by mathematical proofs in analysis/continuation_VI.',
     'exterior_square_tests':{'count':400,'kernel_dimension_histogram':parity_hist},
     'toric_quotients':toric,'blowup_cases':blowups,'negative_operation_betti_increment':negative_operation,
     'koszul_contraction_tests':character_tests,'weighted_local_triples_tested':len(weighted),
     'status':'all assertions passed'}
path=Path(__file__).with_name('topology_and_character_results.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['blowup_cases','toric_quotients']},indent=2))
