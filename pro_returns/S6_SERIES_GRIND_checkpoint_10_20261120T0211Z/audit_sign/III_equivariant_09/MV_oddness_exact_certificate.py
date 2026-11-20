from pathlib import Path
import sympy as S,json,hashlib,datetime
p=Path(__file__).resolve().parent
d=json.loads((p/'collar_exact_certificate.json').read_text());R=S.Matrix(d['boundary_matrix'])
a=S.Matrix([0,1,0,0,0,0]);v=S.Matrix([-12,8,4,-8,0,-3]);B=S.Matrix.hstack(a,v)
F=S.Matrix([[0,1,-8,0,0,-8],[0,0,1,0,0,1]])
C=S.Matrix([[-3,0,-8,4,0,-12],[0,0,0,0,1,0]])
tests={'primitive_split':F*B==S.eye(2),'all_columns_in_twice_split':R==2*B*C,'alpha_detector':(F*a)[0]==1,'two_alpha_literal_preimage':R*S.Matrix([1,0,0,1,0,0])==2*a}
assert all(tests.values())
ints=lambda m:[[int(x) for x in row] for row in m.tolist()]
r={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','checks':4,'tests':{k:bool(v) for k,v in tests.items()},'basis_columns':ints(B),'left_inverse':ints(F),'R_factor':ints(C),'logical_map':'Wang free quotient gives tensor injection; UCT gives injection into mod2 homology; MV coefficient naturality detects N.','scope':'After-freeze correction/clarification; the original frozen documents are unchanged.','producer_note':'Initial inline execution passed all four assertions but json.dumps rejected SymPy Zero. The current serializer converts matrix entries to ordinary integers. This was an output serialization error, not a failed mathematical assertion.'}
o=p/'MV_oddness_exact_certificate.json';o.write_text(json.dumps(r,indent=2)+'\n')
print('PASS',len(tests));print('addendum_sha256',hashlib.sha256((p/'MV_oddness_addendum.md').read_bytes()).hexdigest());print('certificate_sha256',hashlib.sha256(o.read_bytes()).hexdigest())
