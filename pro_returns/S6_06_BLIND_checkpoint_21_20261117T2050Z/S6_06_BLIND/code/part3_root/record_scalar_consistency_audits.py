"""Record the exact scalar obstruction and the independently repaired C2 map."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[2]
files=['notes/part3_scalar_outer_clutch_audit.md',
       'notes/part3_scalar_c1_native_arrow_working.md',
       'notes/part3_scalar_consistency_dependencies.md',
       'code/part3/scalar_c1_outer_marking.json']
record={'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root','status':'PASS',
 'files':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in files},
 'verified_points':[
  'The actual primitive forward q^-1 arrow, reindexing by B and varying-unit seam E=(gZ,eta V) agree with K10/K22/K25. The literal doubled seam is the pullback of the single native product and retains every cap square.',
  'C1 native coordinates (c,a,b) and (eta v,g w,(g eta)^-1 u) have exact standard normal transition and the displayed q-preserving Cox lift on both small resolutions.',
  'The doubled ordinary trace gives V11=2,delta1=-2, pair(0,-2). The actual pure-left boundary correction gives native(2,-2); its actual relative square gives single(1,-1).',
  'The outer C1 normal map is diag(eta/alpha,kappa alpha/(g eta)), with source-base factor g/kappa. Conjugating its negative first line gives determinant winding -2M, whereas the other outer comparison is identity.',
  'The explicit coordinate-arrow convention and oriented two-overlap torus give the scalar Cech class -M and determinant class -2M. No full C1 characteristic residue is inferred from this local class.',
  'The marked pointed-curve equations a+u=0,c+v=M and the arbitrary GL2 positive-weight determinant square give -M=0. For nonzero M this proves the claimed simultaneous periodic equivariant product cannot exist.',
  'The C2 double ordinary pair is (-2J,0). Its explicit Hopf boundary correction is pure left of degree -2J; the actual pulled-back native pair and the single native pair are (0,0).',
  'The actual C2 Cox conjugation therefore has zero central increment for all integral scalar winding, with the full q^e closing and period reindex retained.',
  'The C2 outer normal arrows are identity and diag(alpha^-1,kappa alpha), with base kappa^-1. They are scalar-independent, so the common inner physical-circle gauge matches both outer collars. The retained joint-cap and fixed-normal corrections pull back from their parameter-free factors and have zero characteristic index.',
  'This narrow C2 integer comparison repairs the initial/reflected scalar equality used by K57/K58. It does not repair the old C1/shear or universal scalar-fan claims.'
 ],
 'scope':'The exact obstruction, literal native C1/C2 computations and narrow C2 characteristic repair. The old all-fan assertions receive a separate correction ledger; no OS49 outer correction is inferred without its own map.'}
p=root/'records/root_audit_scalar_consistency.json'
assert not p.exists()
p.write_text(json.dumps(record,indent=2)+'\n')
print('PASS: scalar product obstruction, actual outer clutch, native pairs and narrow C2 integer repair.')
