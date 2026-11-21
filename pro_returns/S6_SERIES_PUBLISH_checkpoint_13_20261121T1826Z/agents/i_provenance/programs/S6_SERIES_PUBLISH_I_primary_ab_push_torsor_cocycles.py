"""Finite group certificates for the unramified torsor transgression.

The existence and localization statements are proved by the cited
Hochschild--Serre and Ogg--Shafarevich exact sequences in B.3.6.
This script verifies the finite cyclic cocycles and residue classes;
it does not claim an explicit equation for the resulting torsor.
"""
from pathlib import Path
from fractions import Fraction
import json

n=12
kappa=6
def cocycle(i,j,order=n):
    return kappa*((i+j)//order)
checks=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            assert cocycle(j,k)-cocycle((i+j)%n,k)+cocycle(i,(j+k)%n)-cocycle(i,j)==0
            checks+=1
assert kappa%n!=0 and 2*kappa%n==0
print('Cyclic carry cocycle checked on',checks,'triples.')
print('Class6 in Z/12 is nonzero of exact order2.')
local=[]
for e,component_order in ((3,3),(4,2),(12,1)):
    assert kappa%component_order==0
    # Local divisibility supplies a point q_e with e*q_e=6P.  In this
    # abstract relation the cochain i*q_e has the carry cocycle above.
    b=[Fraction(i*kappa,e) for i in range(e)]
    for i in range(e):
        for j in range(e):
            assert b[i]+b[j]-b[(i+j)%e]==cocycle(i,j,e)
    local.append({'ramification':e,'component_group_order':component_order,
                  'class_in_component_group':kappa%component_order,
                  'abstract_division_cochain':[str(v) for v in b]})
    print('Local ramification',e,': 6P has component0 mod',component_order,
          '; division cochain verifies the local carry coboundary.')
out={'cyclic_order':n,'class':kappa,'class_order':2,
     'cocycle_triples_checked':checks,'local_checks':local,
     'scope':'Finite algebra only; the unramified torsor existence uses proved exact sequences, not this finite check alone.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL FINITE TORSOR-COCYCLE CHECKS PASSED')
