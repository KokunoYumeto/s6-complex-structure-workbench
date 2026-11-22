#!/usr/bin/env python3
"""Postrelease checks of added compact quotient maps and prior program results."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from datetime import datetime,timezone
import hashlib,json,subprocess,sys
AREA=Path(__file__).resolve().parent
ROOT=AREA.parents[2]
def plus(a,b):
 c=defaultdict(int,a)
 for k,v in b.items():c[k]+=v
 return {k:v for k,v in c.items() if v}
def scale(a,c):return {k:c*v for k,v in a.items() if c*v}
def mul(a,b):
 c=defaultdict(int)
 for (i,j),v in a.items():
  for (k,l),w in b.items():c[i+k,j+l]+=v*w
 return {k:v for k,v in c.items() if v}
def power(a,n):
 r={(0,0):1}
 for _ in range(n):r=mul(r,a)
 return r
def subst(f,a,b):
 r={}
 for (i,j),v in f.items():r=plus(r,scale(mul(power(a,i),power(b,j)),v))
 return r
x={(1,0):1};y={(0,1):1}
tac=mul(y,plus(y,scale(power(x,2),-1)))
sy=plus(power(x,2),scale(y,-1))
assert subst(tac,x,sy)==tac
assert subst(sy,x,sy)==y
tri=mul(mul(x,y),plus(x,scale(y,-1)))
tx=scale(y,-1);ty=plus(x,scale(y,-1))
assert subst(tri,tx,ty)==tri
def matmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
m=[[0,-1],[1,-1]];m2=matmul(m,m);m3=matmul(m2,m)
assert m3==[[1,0],[0,1]] and m!=m3 and m2!=m3
translations={r:[str(Q(k,r)) for k in range(1,r+1)] for r in [2,3]}
for r in [2,3]:
 assert all(Q(k,r).denominator!=1 for k in range(1,r))
 assert Q(r,r).denominator==1
old=ROOT/'records/S6_SERIES_PUBLISH_II_opened_programs_recovery_01/genus_one_conductor.py'
assert hashlib.sha256(old.read_bytes()).hexdigest()=='5b228e81babc0ff65fd653dcf06ff562afa1a2f0b675a7870e5da180f1ba0155'
run=subprocess.run([sys.executable,str(old)],capture_output=True,text=True,check=False)
output=AREA/'S6_SERIES_PUBLISH_II_WL_prior_program_reexecution.txt'
with output.open('x') as f:f.write(run.stdout);f.write(run.stderr)
assert run.returncode==0,run.stderr
fresh=json.loads((AREA/'S6_SERIES_PUBLISH_II_WJ_WL_fresh_exact_output.json').read_text())
matches=[]
for kind,branches in [('tangent',2),('triple',3)]:
 for n in [2,3,4,6,8]:
  row=next(q for q in fresh['jet_checks'] if q['kind']==kind and q['jet_order']==n)
  literal=f" jet order {n} normalization dimension {branches*n} image rank {row['image_dimension']} delta {row['delta']} conductor exponent 2 on every branch"
  assert literal in run.stdout
  matches.append({'kind':kind,'order':n,'fresh_rank':row['image_dimension'],'fresh_delta':row['delta'],'old_output_matches':True})
r={'created_utc':datetime.now(timezone.utc).isoformat(),'phase':'After new WJ/WL freezes and target release; no additional independent event.',
   'tacnode_involution_preserves_equation':True,'tacnode_involution_square_is_identity':True,
   'triple_projective_map_preserves_cubic':True,'triple_linear_map_order':3,
   'triple_matrix_square':m2,'triple_matrix_cube':m3,
   'elliptic_translation_exact_orders':translations,
   'normalization_quotient_inverse':'[z,e] in the j-th cyclically permuted component maps to (sigma_tilde^(-j)z,tau^(-j)e); direct substitution of a group generator leaves this unchanged.',
   'conductor_algebra_scope':'Local analytic algebras on E only; no global trivialization of the nilpotent algebra bundle is asserted.',
   'prior_program':{'path':str(old.relative_to(ROOT)),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'opened_after_freeze':True,'returncode':run.returncode},
   'prior_program_output':{'path':str(output.relative_to(ROOT)),'sha256':hashlib.sha256(output.read_bytes()).hexdigest()},
   'method_comparison':'Prior program uses SymPy polynomial substitution and repeated augmented-matrix ranks. The fresh prereading program uses standard-library Fraction row reduction and the simultaneous annihilator conditions for multiplication by every branch idempotent and monomial. Arbitrary convergent-series proofs are frozen separately.',
   'matched_prior_cases':matches,'events_added':0}
p=AREA/'S6_SERIES_PUBLISH_II_WJ_WL_postrelease_exact_output.json'
with p.open('x') as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'matched_cases':len(matches)},indent=2))
