"""Exhaustive integral tests for four specified exceptional-line points.

Parameters are exactly n=0,1,2,3. For each, the order conductor is computed,
every stable quotient lattice in the proved finite interval is enumerated,
every primitive extension coset is enumerated, and the full H^3/H^5 test
is run. These finite runs do not assert anything for other n.
"""
import sympy as S
from pathlib import Path
import json
from fourfolds_exceptional_probe import pair
from fourfolds_lattice_algorithm import order_and_conductor,finite_stable_lattices
from fourfolds_two_classes_lattices import extension_classes
from fourfolds_survivor_test import test_pair,Z

records=[]
for n in (0,1,2,3):
    print('EXCEPTIONAL n=',n,flush=True)
    A,C=pair(n);order=order_and_conductor(A,C)
    assert order['stable_lattice']
    L0=order['lattice_basis'];AA=Z(L0.inv()*A*L0);CC=Z(L0.inv()*C*L0)
    quotient_lattices=finite_stable_lattices(AA,CC,order['conductor'])
    print('complete quotient count',len(quotient_lattices),flush=True)
    totals=passed=0
    for index,H in enumerate(quotient_lattices):
        A1=Z(H.inv()*AA*H);B1=Z(H.inv()*CC.inv()*H)
        print('QUOTIENT',index,'relative index',abs(H.det()),flush=True)
        rows=extension_classes(A1,B1)
        for row in rows:
            totals+=1
            result=test_pair(row['A'].T,row['B'].T)
            passed+=result['passes']
            records.append({'n':n,'quotient_index':index,'quotient_basis':(L0*H).tolist(),
                            'A':row['A'].tolist(),'B':row['B'].tolist(),'result':result})
    print('SUMMARY n=',n,'quotient lattices',len(quotient_lattices),'primitive extensions',totals,'survivors',passed,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2,default=int))
print('ALL FOUR EXHAUSTIVE PARAMETER TESTS COMPLETED',flush=True)
