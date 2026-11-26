#!/usr/bin/env python3
"""Fresh post-release computation of G_N via an SL2 quotient and additive kernel.

This program reads no old program or result. It enumerates only the 2x2
quotient, derives kernel generators by Schreier telescoping, and computes
an exact integer-lattice index for that kernel. It never enumerates G_N.
"""
from collections import deque
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

A1 = Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
Q = Matrix([[0,0,0,6],[0,0,1,0],[0,-1,0,0],[-6,0,0,0]])
assert A1.T*Q*A1 == Q and A2.T*Q*A2 == Q
assert A1**3 == A2**4 == Matrix.eye(4)

def reduced(a,n):
    return tuple(int(x)%n for x in a)

def multiply(a,b,n):
    return (reduced(Matrix(4,4,a[0])*Matrix(4,4,b[0]),n),(a[1]+b[1])%n)

def inverse(a,n):
    # All representatives below are reductions of determinant-one matrices.
    # adjugate remains the inverse modulo n, so no field division is used.
    m=Matrix(4,4,a[0])
    assert int(m.det())%n == 1%n
    return (reduced(m.adjugate(),n),(-a[1])%n)

def quotient(a):
    m=a[0]
    return (m[5],m[6],m[9],m[10])

def kernel_coordinates(a,n):
    m=Matrix(4,4,a[0]); identity=Matrix.eye(2)
    assert quotient(a)==reduced(identity,n)
    assert tuple(m.row(0))==(1,0,0,0)
    assert tuple(m.col(3))==(0,0,0,1)
    r1,r2,z=int(m[3,1]),int(m[3,2]),int(m[3,0])
    assert int(m[1,0])%n == (-6*r2)%n
    assert int(m[2,0])%n == (6*r1)%n
    return (r1%n,r2%n,(z-6*r1*r2)%n,a[1]%n)

def rebuild(v,n):
    r1,r2,zbar,c=v
    z=(zbar+6*r1*r2)%n
    m=Matrix([[1,0,0,0],[-6*r2,1,0,0],[6*r1,0,1,0],[z,r1,r2,1]])
    return (reduced(m,n),c%n)

def one(n):
    assert 12%n==0
    ident=(reduced(Matrix.eye(4),n),0)
    generators=[(reduced(A1,n),(-1)%n),(reduced(A2,n),0)]
    generators += [inverse(g,n) for g in generators]
    # Build representatives only for the 2x2 quotient.
    representatives={quotient(ident):ident}
    words={quotient(ident):[]}
    todo=deque([quotient(ident)])
    while todo:
        key=todo.popleft()
        for i,g in enumerate(generators):
            value=multiply(representatives[key],g,n)
            q=quotient(value)
            if q not in representatives:
                representatives[q]=value
                words[q]=words[key]+[i]
                todo.append(q)
    # Complete independent list of determinant-one 2x2 matrices.
    sl2={v for v in product(range(n),repeat=4) if (v[0]*v[3]-v[1]*v[2])%n==1%n}
    assert set(representatives)==sl2
    schreier=[]
    coordinate_vectors=[]
    for q,t in representatives.items():
        for i,g in enumerate(generators):
            tg=multiply(t,g,n)
            nxt=quotient(tg)
            k=multiply(tg,inverse(representatives[nxt],n),n)
            v=kernel_coordinates(k,n)
            assert rebuild(v,n)==k
            if any(v):
                schreier.append({'quotient':list(q),'word_to_q':words[q],
                                 'generator_index':i,'word_to_next':words[nxt],
                                 'matrix':list(k[0]),'second_coordinate':k[1],
                                 'additive_coordinates':list(v)})
                coordinate_vectors.append(v)
    unique=sorted(set(coordinate_vectors))
    # Check the explicit additive law on all Schreier-generator pairs.
    # The symbolic law for the complete coordinate ambient is proved in
    # the comparison; these checks bind its application to the exact data.
    for v in unique:
        for w in unique:
            summed=tuple((x+y)%n for x,y in zip(v,w))
            assert multiply(rebuild(v,n),rebuild(w,n),n)==rebuild(summed,n)
    columns=[n*Matrix.eye(4)[:,i] for i in range(4)]
    columns += [Matrix(v) for v in unique]
    relation_lattice=Matrix.hstack(*columns)
    basis=hermite_normal_form(relation_lattice)
    assert basis.shape==(4,4)
    cokernel_index=abs(int(basis.det()))
    kernel_size=n**4//cokernel_index
    assert n**4 % cokernel_index==0
    if n==2:
        free_generators=[(1,0,0,0),(0,1,0,0),(0,0,0,1)]
        assert all(v[2]==0 for v in unique)
        parameterization='(r1,r2,c) -> (r1,r2,0,c)'
    elif n==3:
        free_generators=[(1,0,0,0),(0,1,0,0)]
        assert all(v[2]==v[3]==0 for v in unique)
        parameterization='(r1,r2) -> (r1,r2,0,0)'
    else:
        free_generators=[(1,0,2,0),(0,1,2,0),(0,0,0,1)]
        assert all(v[2]==(2*(v[0]+v[1]))%4 for v in unique)
        parameterization='(r1,r2,c) -> (r1,r2,2*(r1+r2),c)'
    assert all(v in unique for v in free_generators)
    assert kernel_size==n**len(free_generators)
    return {'N':n,'quotient_order':len(sl2),'quotient_representatives':[
                {'quotient':list(q),'word':words[q]} for q in representatives],
            'schreier_generators':schreier,
            'unique_additive_kernel_generators':[list(v) for v in unique],
            'integer_relation_basis':[[int(x) for x in row] for row in basis.tolist()],
            'cokernel_index':cokernel_index,'kernel_order':kernel_size,
            'kernel_free_generators':[list(v) for v in free_generators],
            'kernel_parameterization':parameterization,
            'G_order':len(sl2)*kernel_size,
            'global_cover_degree':n*n*len(sl2)*kernel_size,
            'method':'SL2 quotient; Schreier kernel; explicit additive coordinate isomorphism; integer lattice index'}

def main():
    result={'completed_utc':datetime.now(timezone.utc).isoformat(),
            'program_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'phase':'new post-proof-release method before opening old code or historical outputs',
            'results':[one(n) for n in (2,3,4)]}
    result['completed_utc']=datetime.now(timezone.utc).isoformat()
    out=Path(__file__).resolve().parents[1]/'agents/continuation4_iii_root/S6_SERIES_PUBLISH_III_02K6_schreier_kernel.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    for r in result['results']:
        print({k:r[k] for k in ('N','quotient_order','kernel_order','cokernel_index','G_order','global_cover_degree')})
        print('kernel generators',r['unique_additive_kernel_generators'])
        print('relation basis',r['integer_relation_basis'])
    print('completed_utc',result['completed_utc'])

if __name__=='__main__':main()
