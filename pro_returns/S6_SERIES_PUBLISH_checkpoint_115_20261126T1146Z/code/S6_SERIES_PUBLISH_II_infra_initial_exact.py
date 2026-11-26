#!/usr/bin/env python3
"""New exact affine/group calculations for II 01F8 and 01F9.

Written from the statement packets before the target proofs are released.
No earlier mathematical program is imported or reused.
"""
from pathlib import Path
import hashlib,itertools,json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'agents/ii_infra/checks';OUT.mkdir(exist_ok=True)
zeta=(1+S.sqrt(3)*S.I)/2;bar=S.conjugate(zeta)
A=S.Matrix([[1,0,1],[1,1,bar],[0,0,1]])
B=S.Matrix([[1,0,zeta],[bar,1,bar],[0,0,1]])
C=S.Matrix([[1,0,0],[0,1,zeta-bar],[0,0,1]])
D=S.Matrix([[1,0,0],[0,1,1],[0,0,1]])
T=S.Matrix([[zeta,0,0],[0,1,S.Rational(1,6)],[0,0,1]])
zero=lambda m:all(S.simplify(x)==0 for x in m)
identities={'AB_commutator_is_C':zero(A*B*A.inv()*B.inv()-C),
            'T_A_Tinverse_is_B':zero(T*A*T.inv()-B),
            'T_B_Tinverse_is_Ainverse_B':zero(T*B*T.inv()-A.inv()*B),
            'T_six_is_D':zero(T**6-D),
            'T_commutes_C':zero(T*C-C*T),'T_commutes_D':zero(T*D-D*T)}
assert all(identities.values())
relations=S.Matrix([[0,0,1,0,0],[1,-1,0,0,0],[1,0,0,0,0],[0,0,0,6,-1]])
snf=smith_normal_form(relations,domain=S.ZZ);diagonal=[abs(int(snf[i,i])) for i in range(4)]
assert diagonal==[1,1,1,1] and relations.rank()==4
def mul(p,q):return tuple(p[q[i]] for i in range(5))
def inv(p):return tuple(p.index(i) for i in range(5))
identity=tuple(range(5))
def parity(p):return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2
even=[p for p in itertools.permutations(range(5)) if parity(p)==0]
commutators={mul(mul(mul(a,b),inv(a)),inv(b)) for a in even for b in even}
generated={identity};queue=[identity]
while queue:
 a=queue.pop()
 for b in commutators:
  c=mul(a,b)
  if c not in generated:generated.add(c);queue.append(c)
assert len(even)==len(generated)==60
QI=S.Matrix([[S.I,0],[0,-S.I]]);QJ=S.Matrix([[0,1],[-1,0]])
assert QI*QJ*QI.inv()*QJ.inv()==-S.eye(2)
phi=(1+S.sqrt(5))/2
vertices={(0,a,b*phi) for a in [-1,1] for b in [-1,1]}|{(a,b*phi,0) for a in [-1,1] for b in [-1,1]}|{(a*phi,0,b) for a in [-1,1] for b in [-1,1]}
for diagonal_rotation in [(1,-1,-1),(-1,1,-1),(-1,-1,1)]:
 assert {tuple(diagonal_rotation[i]*v[i] for i in range(3)) for v in vertices}==vertices
result={'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'method':'Independent symbolic homogeneous-affine matrix multiplication, integer Smith form, exhaustive finite permutation commutator closure, exact quaternion matrices and icosahedron-vertex symmetries.',
 'input_proofs_read':False,'01F8':{'zeta':str(zeta),'affine_identities':identities,'abelianization_relation_matrix':str(relations),
 'smith_diagonal':diagonal,'free_rank':1,'canonical_character_order':6},
 '01F9':{'A5_order':len(even),'A5_derived_subgroup_order':len(generated),'quaternion_central_minus_one_is_commutator':True,
 'coordinate_half_turns_preserve_icosahedron':True},
 'scope':'These exact algebraic identities support the separately written geometric derivations. They do not automatically certify compactness, proper discontinuity, canonical-bundle descent, or any check event.',
 'events_added':0}
p=OUT/'S6_SERIES_PUBLISH_II_initial_exact_output.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
