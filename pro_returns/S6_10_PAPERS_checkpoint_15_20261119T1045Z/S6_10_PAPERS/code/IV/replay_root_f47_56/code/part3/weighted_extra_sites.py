#!/usr/bin/env python3
"""Exact localized extra-site blocks; no order-one clutch is deleted."""
from pathlib import Path
from math import gcd
import json
import sympy as s
ROOT=Path(__file__).resolve().parent
def ints(M): return [[int(x) for x in row] for row in M.tolist()]
def syms(M): return [[str(x) for x in row] for row in M.tolist()]

m,n,A,la,lb=s.symbols('m n A lambda_a lambda_b',integer=True)
rim=s.Matrix([[m,0,0,-la],[0,m,0,-lb],[0,0,m,n]])
U=s.Matrix([[1,0,la/n],[0,1,lb/n],[0,0,1/n]])
assert U*rim[:,3]==s.Matrix([0,0,1])
assert U.det()==1/n
# Over Z_(p), p|m and gcd(m,n)=1 make this an invertible actual
# row change.  U(m R^3)=m R^3, and the last generator is then killed.

I2=s.Matrix([[0,1,0,0],[0,0,0,1]])
J2=s.Matrix([[m,-A,0,0],[0,0,m,A]])
D2=I2.col_join(-J2)
P=s.zeros(4)
for col,row in enumerate([1,3,0,2]):P[row,col]=1
V=s.eye(4);V[2,0]=-A;V[3,1]=A
assert V*D2*P==s.diag(1,1,-m,-m)
assert V.det()==1 and abs(P.det())==1

cc=s.symbols('c0:6')
C=s.Matrix(3,2,cc)
Inv=(-s.eye(3)).row_join(C).col_join(s.zeros(2,3).row_join(-s.eye(2)))
assert Inv*Inv-s.eye(5)==s.zeros(3).row_join(-2*C).col_join(s.zeros(2,5))

source_records=[]
for name,key in [('i1star_boundary.json','H2_inversion_exterior'),
                 ('i1star_iv_boundary.json','H2_exterior_inversion'),
                 ('i1star_iv_reduced_boundary.json','H2_exterior_inversion')]:
    obj=json.loads((ROOT/name).read_text())
    J=s.Matrix(obj[key])
    assert J[1:,1:]==-s.eye(J.rows-1)
    assert all(J[j,0]==0 for j in range(1,J.rows))
    source_records.append({'file':name,'involution':ints(J),'free_action':ints(J[1:,1:])})
obj=json.loads((ROOT/'iv_star_iii_joint.json').read_text())
for case in obj['cases']:
    J=s.Matrix(case['H2_exterior_inversion']); off=1 if case['b']>1 else 0
    assert J[off:,off:]==-s.eye(2)
    source_records.append({'file':'iv_star_iii_joint.json','pair':[case['a'],case['b']],
        'involution':ints(J),'free_action':ints(J[off:,off:])})

prime_checks=[]
for bb,required in [(1,[]),(2,[2]),(2,[4]),(3,[3]),(6,[2,3]),(6,[3,4])]:
    for pp in [2,3,5,7,11,13]:
        if bb%pp==0:
            assert any(x%pp==0 for x in required)
            prime_checks.append({'b':bb,'prime':pp,'required_order_divisors':required})

finite=0
for mm in range(2,35):
    for nn in range(-5,6):
        if gcd(mm,nn)!=1:continue
        for pp in list(s.factorint(mm)):
            for aa,bb in [(0,0),(1,-3),(-4,5)]:
                RR=rim.subs({m:mm,n:nn,la:aa,lb:bb})
                assert (int(nn)%pp)!=0
                field=RR.applyfunc(lambda x:int(x)%pp)
                assert all(field[r,c]==0 for r in range(3) for c in range(3))
                assert any(field[r,3]!=0 for r in range(3))
                finite+=1

out={'status':'PASS','scope':'Localized exclusion of extra effective orders>1; actual source, gamma and delta order-one clutches retained',
     'smooth_rim_matrix':syms(rim),'smooth_localized_row_change':syms(U),
     'multiplicative_complete_D2':syms(D2),'multiplicative_column_change':ints(P),
     'multiplicative_row_change':syms(V),'multiplicative_reduced_D2':syms(V*D2*P),
     'involution_extension':syms(Inv),'involution_square_minus_identity':syms(Inv*Inv-s.eye(5)),
     'actual_source_involutions':source_records,'required_prime_divisors':prime_checks,
     'supplementary_prime_cases':finite,
     'characteristic_two':'The proof works over Z_(2), a characteristic-zero torsion-free coefficient ring; it never divides by2.'}
(ROOT/'weighted_extra_sites.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact smooth localized quotient (R/m)^2, retaining both elliptic coefficients.')
print('PASS: actual multiplicative block -> diag(1,1,-m,-m) by the displayed unimodular maps.')
print('PASS: involution extension has square one exactly when 2C=0; torsion-free coefficients force C=0.')
print('PASS:',len(source_records),'actual source-inversion records;',finite,'supplementary prime cases including p=2.')
