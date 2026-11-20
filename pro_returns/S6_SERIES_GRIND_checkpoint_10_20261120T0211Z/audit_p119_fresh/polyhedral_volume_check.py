"""Exact orientation/word checks for the post-review volume supplement.

This does not claim a completed adapter to the finite-cap cellular diagram.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
import derive_chain as f

P=Path(__file__).parent
J=s.zeros(6)
for col in range(6):
    missing=5-col
    J[missing,col]=(-1)**missing
assert J.det()==1 and J.inv()==-J
one=s.ones(1,6)
alt=one*J
assert alt==s.Matrix([[-1,1,-1,1,-1,1]])
for i in range(3):
    assert f.M[i].det()==1
    assert J*f.W[i,5]==f.M[i].inv().T*J

X=f.ext(f.S,5)[:,[2,1,0]]
assert (f.W[0,5]-s.eye(6))*X==s.zeros(6,3)
X1=-f.W[2,5]*f.W[0,5]*X
X2=-f.W[0,5]*X
terms=[(f.W[i,5]-s.eye(6))*xx for i,xx in [(1,X1),(2,X2)]]
assert terms[0]+terms[1]==s.zeros(6,3)
vol=[alt*t/2 for t in terms]
assert vol[0]+vol[1]==s.zeros(1,3)
norms={}
eta={}
for i in (1,2):
    norm=sum([f.W[i,5]**a for a in range(f.mult[i])],s.zeros(6))
    row=alt*(f.W[i,5]-s.eye(6))/2
    assert row*norm==s.zeros(1,6)
    norms[i]=norm.tolist();eta[i]=row.tolist()
report={
 'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS for the stated orientation, inverse-word, and norm identities; finite-cap comparison remains open',
 'orientation_adapter_J':J.tolist(),'J_inverse':J.inv().tolist(),
 'alternating_row_onesJ':alt.tolist(),'actual_raw_xj':X.tolist(),
 'inverse_word_edge1':X1.tolist(),'inverse_word_edge2':X2.tolist(),
 'edge_boundary_terms':[x.tolist() for x in terms],
 'edge_volume_terms':[x.tolist() for x in vol],
 'eta_rows':eta,'finite_norm_matrices':norms,
 'remaining_gate':'Construct an integral comparison from the polyhedral prism/filling model to the exact marked finite-cap model of P1.12, including its affine meridian and every changed source/target chain map. The rational eta row alone is not such an adapter.',
 'source_fresh_program_sha256':hashlib.sha256((P/'derive_chain.py').read_bytes()).hexdigest()
}
(P/'polyhedral_volume_check.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps({'utc':report['utc'],'J':J.tolist(),'xj':X.tolist(),
                  'volumes':[x.tolist() for x in vol],'eta':eta,
                  'status':report['status']},indent=2,default=str))
