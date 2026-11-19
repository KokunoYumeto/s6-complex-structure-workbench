"""Exact local complex and parity checks for maps_D2_frame_proof.tex.

The geometric ambient surgery and the obstruction-theory proof are in the
companion TeX.  This script checks the local Hilbert--Burch/Koszul data and
the exact parity arithmetic used after the independently computed links.
"""
from pathlib import Path
import json
import sympy as s

x,y,z,xb,yb=s.symbols('x y z xb yb')
triple=s.Matrix([[x,x],[-y,0],[0,-z]])
gradient=s.Matrix([[y*z,x*z,x*y]])
assert gradient*triple == s.zeros(1,2)
cofactor=s.Matrix([[triple.extract([1,2],[0,1]).det(),
                   -triple.extract([0,2],[0,1]).det(),
                   triple.extract([0,1],[0,1]).det()]])
assert cofactor == gradient
node=s.Matrix([[x,0],[-y,0],[0,1]])
assert s.Matrix([[y,x,0]])*node == s.zeros(1,2)
bott=s.Matrix([[x,yb],[-y,xb]])
bott_star=s.Matrix([[xb,-yb],[y,x]])
norm=x*xb+y*yb
assert bott_star*bott == norm*s.eye(2)
assert bott.det() == norm
assert s.Matrix([[y,x]])*bott == s.Matrix([[0,norm]])

rows=[(45,1,8,j,4) for j in (1,2,3,4)]
rows += [(55,5,4,j,k) for j,k in ((2,37),(3,7),(4,27))]
result=[]
for os,a,c,j,k in rows:
    # The determinant/Spin(1) contribution is 0 or eta^3=12nu.
    # The SU comparison adds k times a stable J generator.
    parities={((detpart+sign*k)%24)%2
              for detpart in (0,12) for sign in (-1,1)}
    assert parities == {k%2}
    d=1-k%2              # Stiefel difference from a Lie tangent frame
    P=(c//2)*(1-d)
    assert 2*P%c == 0
    assert P == (c//2)*(k%2)
    result.append(dict(OS=os,a=a,c=c,zero_index=j,link=k,
                       framed_parity=k%2,stiefel_difference=d,refined_P=P))

out={
 'triple_hilbert_burch_matrix':[[str(t) for t in row] for row in triple.tolist()],
 'signed_maximal_minors':[str(t) for t in cofactor],
 'node_clutch_determinant':str(norm),
 'universal_spin_restriction':2,
 'universal_o4_order':2,
 'rows':result,
 'status':'All exact local and parity checks passed; geometric proofs are separate.'}
root=Path(__file__).resolve().parents[1]
(root/'records/maps_D2_frame_checks.json').write_text(json.dumps(out,indent=2)+'\n')
for row in result: print(row)
print(out['status'])
