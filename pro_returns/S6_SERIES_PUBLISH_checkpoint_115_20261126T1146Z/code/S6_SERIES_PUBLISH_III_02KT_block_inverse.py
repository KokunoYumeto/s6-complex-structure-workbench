#!/usr/bin/env python3
"""Separate pre-release inverse addendum, written after KY auxiliary exposure."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
import sympy as s

HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation6_iii_d2'
frozen=INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KT_fresh_derivation.md'
assert sha256(frozen.read_bytes()).hexdigest()=='d6e82781bd3b6a1b11ae71e1e475ffc2fdb8d58b07583d4ad6f9368743a5069e'
a00,a01,a10,a11,b0,b1,q0,q1,c=s.symbols('a00 a01 a10 a11 b0 b1 q0 q1 c')
A=s.Matrix([[a00,a01],[a10,a11]]);beta=s.Matrix([[b0,b1]]);q=s.Matrix([q0,q1])

def assemble(A,beta,q,c):
    return A.row_join(s.zeros(2,1)).row_join(q).col_join(
        beta.row_join(s.Matrix([[1,c]]))).col_join(s.Matrix([[0,0,0,1]]))

def inverse_formula(T):
    A=T[:2,:2];beta=T[2,:2];q=T[:2,3];c=T[2,3];Ai=A.inv()
    return assemble(Ai,-beta*Ai,-Ai*q,(beta*Ai*q)[0]-c)

T=assemble(A,beta,q,c);Ti=inverse_formula(T)
assert s.simplify(T*Ti)==s.eye(4) and s.simplify(Ti*T)==s.eye(4)
print('Both symbolic block products equal I4 over Q(A,beta,q,c).')
data=json.loads((INPUT_ROOT/'S6_SERIES_PUBLISH_III_02KT_fresh_maps.json').read_text())
count=0
for row in data['rows']:
    for entries in row['matrices']:
        T=s.Matrix(entries);Ti=inverse_formula(T)
        assert T[:2,:2].det()==1
        assert all(x.q==1 for x in Ti)
        assert T*Ti==Ti*T==s.eye(4)
        count+=1
print('Exact integral inverses checked for',count,'local matrices in',len(data['rows']),'fixed whole-fibre tuples.')
print('Original 227-line fresh derivation hash and bytes remain fixed.')
print('KT original proof remains closed; this separate addendum follows KY auxiliary exposure.')
print('Completed UTC:',datetime.now(timezone.utc).isoformat())
