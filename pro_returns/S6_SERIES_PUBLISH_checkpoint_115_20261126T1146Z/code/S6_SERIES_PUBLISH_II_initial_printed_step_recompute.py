#!/usr/bin/env python3
"""Fresh post-freeze comparison calculations for II 01F8/01F9.

The derivations were frozen before reading either target. This script checks
their printed computational steps by symbolic pullbacks and exact 2x2 matrices
over a SymPy algebraic number field, with no historical computation imported.
"""
from pathlib import Path
import hashlib,itertools,json
import sympy as S
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'agents/ii_infra/checks'
x,y,z,u,v,w,t=S.symbols('x y z u v w t',real=True)
tau=(1+S.sqrt(3)*S.I)/2
sigma=S.Matrix([[0,-1,0],[1,1,0],[0,-S.Rational(1,2),1]])
assert sigma**6==S.eye(3)
def law(a,b):return S.Matrix([a[0]+b[0],a[1]+b[1],a[2]+b[2]+(a[0]*b[1]-a[1]*b[0])/2])
assert all(S.expand(q)==0 for q in sigma*law(S.Matrix([x,y,z]),S.Matrix([u,v,w]))-law(sigma*S.Matrix([x,y,z]),sigma*S.Matrix([u,v,w])))
new=sigma*S.Matrix([x,y,z]);lattice=S.expand(new[2]-new[0]*new[1]/2-(z-x*y/2))
assert S.expand(lattice-(x*y+y*(y-1)/2))==0
old=sigma.inv()*S.Matrix([u,v,w]);inverse_lattice=S.expand(old[2]-old[0]*old[1]/2-(w-u*v/2))
assert S.expand(inverse_lattice-(u*v+u*(u-1)/2))==0
coords=S.Matrix([x,y,z,t]);trans=S.Matrix([new[0],new[1],new[2],t]);jac=trans.jacobian(coords)
alpha=S.Matrix([[1,tau,0,0]]);beta=S.Matrix([[(y-1)/2,-(x+1)/2,1,S.I]])
pull_alpha=S.simplify(alpha*jac)
pull_beta=S.simplify(beta.subs({x:new[0],y:new[1]},simultaneous=True)*jac)
assert all(S.simplify(q)==0 for q in pull_alpha-tau*alpha)
assert all(S.simplify(q)==0 for q in pull_beta-beta)
form_matrix=alpha.col_join(beta).col_join(S.conjugate(alpha)).col_join(S.conjugate(beta))
assert S.simplify(form_matrix.det())!=0
horizontal=sigma[:2,:2];assert (horizontal-S.eye(2)).det()==1
def parity(p):return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2
phi=(1+S.sqrt(5))/2
K=S.QQ.algebraic_field(S.I,S.sqrt(5));ki=K.from_sympy(S.I);zero=K.zero;one=K.one
points=set()
for j in range(4):
 for sign in [-1,1]:points.add(tuple(K.convert(sign if i==j else 0) for i in range(4)))
for signs in itertools.product([-1,1],repeat=4):points.add(tuple(K.convert(S.Rational(a,2)) for a in signs))
for signs in itertools.product([-1,1],repeat=3):
 raw=(S.Integer(0),S.Rational(signs[0],2),signs[1]*phi/2,signs[2]*(phi-1)/2)
 for perm in itertools.permutations(range(4)):
  if parity(perm)==0:points.add(tuple(K.from_sympy(raw[i]) for i in perm))
assert len(points)==120
assert all(sum((a*a for a in q),zero)==one for q in points)
matrices=[]
for a,b,c,d in points:matrices.append((a+ki*b,c+ki*d,-c+ki*d,a-ki*b))
lookup={m:i for i,m in enumerate(matrices)};assert len(lookup)==120
def multiply(a,b):return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
assert all(a*d-b*c==one for a,b,c,d in matrices)
table=[]
for a in matrices:table.append([lookup[multiply(a,b)] for b in matrices])
unit=lookup[(one,zero,zero,one)];inverses=[]
for a,b,c,d in matrices:inverses.append(lookup[(d,-b,-c,a)])
assert all(table[i][inverses[i]]==table[inverses[i]][i]==unit for i in range(120))
commutators={table[table[table[i][j]][inverses[i]]][inverses[j]] for i in range(120) for j in range(120)}
assert len(commutators)==120
result={'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'prereading_derivations':'01F8/01F9 frozen2026-11-21T18:42:32Z; target proofs read only after the bound release receipts.',
 'method':'New symbolic Lie-group law and differential pullback calculations; exact complex2x2 matrix multiplication over SymPy QQ(i,sqrt(5)), compared with the printed quaternion-coordinate enumeration. No earlier code imported.',
 '01F8':{'sigma_six_identity':True,'sigma_preserves_heisenberg_law':True,'forward_lattice_increment':str(lattice),'inverse_lattice_increment':str(inverse_lattice),'lattice_integrality_reason':'x*y+y(y-1)/2 and u*v+u(u-1)/2 are integers on integer pairs','pullback_alpha':str(pull_alpha),'pullback_beta':str(pull_beta),'four_form_matrix_determinant':str(S.simplify(form_matrix.det())),'det_A_minus_I':1,'integrability':'d alpha=0; d beta=-dx wedge dy=(1/(i sqrt3))*alpha wedge conjugate(alpha), with no(0,2) term; alpha wedge d beta=0.'},
 '01F9':{'coordinate_points':len(points),'unit_norms_checked':120,'distinct_faithful_matrices':len(lookup),'closed_matrix_products':14400,'determinant_one_matrices':120,'inverse_pairs_checked':120,'distinct_single_commutators':len(commutators),'abelianization':'zero'},
 'mathematical_events_added':0}
p=OUT/'S6_SERIES_PUBLISH_II_initial_printed_step_output.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
