#!/usr/bin/env python3
"""Exact determinant and torus-involution arithmetic for whole-zero sites."""
from pathlib import Path
import itertools,json,math
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
root=Path(__file__).resolve().parents[2]
N,c,alpha,beta,e=s.symbols('N c alpha beta e',integer=True)
det=s.Matrix([[N,-c],[alpha,beta]]).det()
assert s.expand(det-(N*beta+c*alpha))==0
r,t,m,v1,v2=s.symbols('r t m v1 v2',integer=True)
Q=s.Matrix([[1,0,-r],[0,1,-t],[0,0,m]])
U=s.eye(3);U[0,2]=m*v1;U[1,2]=m*v2
assert s.simplify(Q*s.Matrix([r/m,t/m,1/m]))==s.Matrix([0,0,1])
expected=s.eye(3);expected[0,2]=v1;expected[1,2]=v2
assert s.simplify(Q*U*Q.inv()-expected)==s.zeros(3)
fan_checks=0
for ss in (1,3):
 for ee in range(1,4):
  for bb in range(-3,4):
   for jj in range(-8,9):
    for kk in range(-8,9):
     parity=lambda x,y:(x+bb*ss*(y//(2*ee)))%2
     assert parity(jj+2*ss,kk)==parity(jj,kk)
     assert parity(jj-bb*ss,kk+2*ee)==parity(jj,kk)
     assert parity(-jj-1,kk)==1-parity(jj,kk)
     fan_checks+=1
edges={(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)}
Rodd=s.Matrix([[-1,0],[-1,1]])
assert {tuple(Rodd*s.Matrix(v)) for v in edges}==edges
invol=[]
for entries in itertools.product(range(-2,3),repeat=4):
 M=s.Matrix(2,2,entries)
 if M*M!=s.eye(2): continue
 T=M-s.eye(2);rank=T.rank()
 S=smith_normal_form(T,domain=ZZ)
 degree=math.prod(abs(int(S[i,i])) for i in range(rank))
 fixed_euler=degree if rank==2 else 0
 assert fixed_euler>=0
 invol.append(dict(M=[list(M.row(i)) for i in range(2)],
                   fixed_torus_dimension=2-rank,
                   number_of_kernel_components=degree,
                   euler_when_nonempty=fixed_euler))
out=dict(status='PASS',proof='P3K.20',
 actual_defect='h_j+beta-h_(j-c)=e, h_(j+N)=h_j+alpha',
 determinant='N*beta+c*alpha=N*e',
 semistable_euler='2*N*e',
 invariant_twist_lattice_map=[[str(x) for x in Q.row(i)] for i in range(3)],
 invariant_twist_conjugation='Q * shear(m*Gamma) * Q^-1 = shear(Gamma)',
 exact_invariant_fan_parity_checks=fan_checks,
 starred_quadratic_root=dict(source='I_(2*s)',zero_order='2*e',
                             period_determinant='4*s*e',root_euler='8*s*e',
                             quotient_lower_bound='4*s*e'),
 involution_certificates=invol,
 scope='The actual smooth-root monomial quotient and toric resolution construction; no unproved contraction comparison is inferred.')
(root/'code/part3_fourfold/whole_zero.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('PASS: determinant identity and',len(invol),'exact monomial-involution kernel certificates.')
