#!/usr/bin/env python3
"""Literal component-label maps in the seven raw KM markings."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import sympy as s

HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation5_iii_d2'
path=INPUT_ROOT.parent/'continuation5_iii_infra/S6_SERIES_PUBLISH_III_02KM_marked_inputs.json'
assert sha256(path.read_bytes()).hexdigest()=='3c0979e269f4ea24c6d8b693e0453935b1bdaca0abd305eb30fc23babeee75de'
rows=json.loads(path.read_text())['rows']
expected=[[(8,3)],[(7,5),(2,1)],[(7,3)],[(5,2),(4,3)],
          [(5,3),(2,1)],[(5,2),(3,1)],[(2,1)]]
for row,want in zip(rows,expected):
    result=[]
    for fibre,mat,g in zip(row['fibers'],row['elliptic_matrices'],
                           row['generator_section_cocycle']):
        if not (fibre[0]=='I' and fibre[1:].isdigit()):
            continue
        n=int(fibre[1:])
        if n==1:
            continue
        A=s.Matrix(mat)
        u=s.cancel((A[0,0]-1)/n)
        assert u.is_Integer
        H=s.Matrix([[1,0],[-u,1]])
        Hi=s.Matrix([[1,0],[u,1]])
        assert H*Hi==Hi*H==s.eye(2)
        assert A==H*s.Matrix([[1,n],[0,1]])*Hi
        c=row['Q']*s.Matrix(g)
        k=int(c[0])
        assert c==k*H[:,0]
        raw=k%n
        geom=(-k)%n
        for j in range(n):
            psi=lambda x:(-x)%n
            forward=lambda x:(x+raw)%n
            backward=lambda x:(x-raw)%n
            assert backward(forward(j))==forward(backward(j))==j
            assert psi(forward(psi(j)))==backward(j)
            assert psi(backward(psi(j)))==forward(j)
        assert s.gcd(raw,n)==1
        result.append((n,raw))
    assert result==want
    print('Row',row['row'],'(n,a(Q),geometric Q):',
          [(n,k,(-k)%n) for n,k in result],
          '; geometric forward +a, raw forward -a, inverse opposite.')

additive={3:(2,[0,1],[0,1],1),5:(3,[0,-1],[0,-1],1),
          6:(2,[1,1],[1,0],1),7:(3,[-1,0],[-1,0],2)}
for row in rows:
    if row['row'] not in additive:
        continue
    modulus,L,v,expected_class=additive[row['row']]
    i=row['additive_index_zero_based']
    A=s.Matrix(row['elliptic_matrices'][i])
    g=s.Matrix(row['generator_section_cocycle'][i])
    L=s.Matrix([L])
    v=s.Matrix(v)
    E=A-s.eye(2)
    assert abs(E.det())==modulus
    assert all(x%modulus==0 for x in L*E) and (L*v)[0]==1
    p=row['P']*g
    q=row['Q']*g
    residue=int((L*p)[0])%modulus
    assert residue==expected_class
    preimage=E.inv()*(p-residue*v)
    assert all(x.is_Integer for x in preimage)
    assert all(x.is_Integer for x in E.inv()*q)
    print('Additive row',row['row'],'raw P',residue,'geometric P',(-residue)%modulus,
          'mod',modulus,'quotient row',list(L),'lift',list(v),
          'kernel preimage',list(preimage))
print('Completed',datetime.now(timezone.utc).isoformat())
