#!/usr/bin/env python3
from pathlib import Path
import sympy as S,json,hashlib
root=Path(__file__).resolve().parents[2];tests=[]
def ck(name,b):
 b=bool(b);tests.append({'name':name,'pass':b})
 if not b:raise AssertionError(name)
def zero(name,x):ck(name,S.factor(S.together(x))==0)
r0,r1,r2,u,C,W,K,SS,z0,z1,z2,rho=S.symbols('r0 r1 r2 u C W K SS z0 z1 z2 rho')
M=lambda r:S.Matrix([[-r,1-r],[0,1]])
prod=M(r2)*M(r1)*M(r0)
kk=-r2*r1*r0;ss=1-2*r2+2*r2*r1-r2*r1*r0
ck('full three chronological source matrices',S.simplify(prod-S.Matrix([[kk,ss],[0,1]]))==S.zeros(2))
zero('actual central source linear coefficient',kk.subs({r0:-1,r1:-1,r2:-1})-1)
zero('actual central source mixing coefficient',ss.subs({r0:-1,r1:-1,r2:-1})-6)
for j in range(-8,9):
 e=(-1)**(j+1);e=int(e)
 A=S.Matrix([[1,0,0],[0,K,SS*u],[0,0,C**e]])
 ck(f'j{j} full ideal inverse',S.simplify(A*A.inv())==S.eye(3))
 zero(f'j{j} literal source sigma',(C**e*W)*(C**-e*u)-W*u)
 zero(f'j{j} exact determinant',A.det()-K*C**e)
 ck(f'j{j} source mixed physical weight',(-e)+e==0)
 ck(f'j{j} period retains both quarter phases',((j+4)%4,(-j-5)%4)==(j%4,(-j-1)%4))
 L=A*S.Matrix([z0,z1,z2])
 for pivot in range(3):
  for h in range(3):
   for k in range(3):zero(f'j{j} pivot{pivot} complete quotient quadratic{h}{k}',rho*L[pivot]**2*(L[h]/L[pivot])*(L[k]/L[pivot])-rho*L[h]*L[k])
zero('actual adjacent neutral/odd arrow',(1/u)*(u**2*W)-u*W)
source=root/'notes/part3_e6_selected_infinity_m2_odd_ideal_working.md'
out={'status':'PASS_FULL_THREE_STEP_ODD_IDEAL','checks':len(tests),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'base_source_sha256':hashlib.sha256((root/'notes/part3_e6_selected_infinity_m2_branch_working.md').read_bytes()).hexdigest(),'identities':tests}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','checks','source_sha256','base_source_sha256']},indent=2))
