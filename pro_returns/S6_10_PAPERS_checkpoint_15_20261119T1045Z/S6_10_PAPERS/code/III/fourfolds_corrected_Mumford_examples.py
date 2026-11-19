"""Actual all-Mumford examples from the D50 corrected initial lines.

The only extension of D46 used here is its punctured monodromy formula,
proved by iterating to hQ narrow while cancelling the literal vertical
correction. Every filled fibre is multiplicative Mumford, so the existing
D43 marked cap calculation applies unchanged. No new original cap is used.
"""
from pathlib import Path
import json
import sympy as s
import manifolds_general_initial as G
import root_vertical_corrections as R
ROOT=Path(__file__).resolve().parent

def corrected_lifts(info,a,b,weights):
    assert all(k.startswith('I') and k[1:].isdigit() for k in info['kodaira_types'])
    assert sum(weights)==a*b*s.Rational(info['height_matrix'][0][0])
    for kind,component in zip(info['kodaira_types'],info['component_maps']):
        order=int(component['moduli'][0]) if component['moduli'] else 1
        residue=int(component['rows'][0][0]) if component['rows'] else 0
        assert R.solve_local(kind,a*residue%order,b*residue%order)['exists']
    A=[G.local_lift(B,a*s.Matrix(c),b*s.Matrix(c),w)
       for B,c,w in zip(info['elliptic_matrices'],info['section_cocycles'][0],weights)]
    assert all(x.q==1 for M in A for x in M)
    product=s.eye(4)
    for M in A:product*=M
    assert product==s.eye(4)
    # Independent actual h-fold comparison with the uncorrected narrow case.
    h=1
    from math import gcd,lcm
    for component in info['component_maps']:
        m=int(component['moduli'][0]) if component['moduli'] else 1
        v=int(component['rows'][0][0]) if component['rows'] else 0
        h=lcm(h,m//gcd(m,b*v))
    Ah=G._uncorrected_lifts(info,a,b*h,[h*w for w in weights])
    S=s.diag(1,1,1,h)
    assert all(M*S==S*Mh for M,Mh in zip(A,Ah))
    return A

G._uncorrected_lifts=G.actual_lifts
G.actual_lifts=corrected_lifts
rows=[]
for a,b in [(2,4),(4,2)]:
    for zero in range(1,5):
        weights=[0]*5;weights[zero]=1
        for e in [-1,1]:
            result=G.compute(45,'default',a,b,weights,e=e)
            assert result['homology'][1]==dict(free=0,torsion=[])
            assert result['fundamental_group']['vertical_quotient']==dict(free=0,torsion=[])
            assert result['euler']==2
            assert result['homology'][2]==dict(free=0,torsion=[b])
            assert result['homology'][3]==dict(free=0,torsion=[b])
            assert all(result['homology'][j]==dict(free=0,torsion=[]) for j in [1,4,5])
            result['chosen_I8_vertical_correction']=R.solve_local('I8',3*a%8,3*b%8)
            result['boundary_marking']='D.GI2 actual punctured marking; no extra affine boundary translations; ordinary gamma clutch e.'
            rows.append(result)
            print('OS45 corrected',a,b,'zero',zero,'e',e,
                  'H2',result['homology'][2],'H3',result['homology'][3],flush=True)
(ROOT/'fourfolds_corrected_Mumford_examples.json').write_text(json.dumps(rows,indent=2,default=int)+'\n')
print('ALL',len(rows),'marked examples passed; actual vertical group killed and ordinary clutch has gamma numerator ±1.')
