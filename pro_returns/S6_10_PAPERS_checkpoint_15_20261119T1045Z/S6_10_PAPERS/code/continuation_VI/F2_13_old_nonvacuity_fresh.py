#!/usr/bin/env python3
"""Fresh post-target arithmetic of the isolated old F2.13 auxiliary item."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
p=Path('analysis/continuation_V/F2_13_old_probe_definition_only.json');data=json.loads(p.read_text());checks=[];out={};I=s.eye(6);ell=I[0,:]
def check(n,b):
 assert b,n
 checks.append(n)
def arr(M):return [[str(v) for v in row] for row in M.tolist()]
for key,u1,u2 in [('A',[1,3,-3,0,1,0],[1,-1,1,2,-1,1]),('B',[1,0,0,1,0,1],[1,0,0,1,0,0])]:
 d=data[key];A=s.Matrix(d['old_probe_A_before_Q']);B=s.Matrix(d['old_probe_B_before_Q']);Q=s.Matrix(d['Q']);AA=Q.inv()*A*Q;BB=Q.inv()*B*Q
 check(key+' actual cohomology Q map',A*Q==Q*AA and B*Q==Q*BB)
 check(key+' definition after-Q agreement',AA==s.Matrix(d['old_A_after_Q']) and BB==s.Matrix(d['old_B_after_Q']))
 check(key+' integral automorphisms',all(v.q==1 for v in AA) and all(v.q==1 for v in BB) and AA.det()==BB.det()==1)
 AA=s.Matrix(6,6,[int(v) for v in AA]);BB=s.Matrix(6,6,[int(v) for v in BB])
 M1=AA.T;M2=BB.T;N=(M1*M2).inv()-I
 check(key+' exact orders',M1**5==I and M1!=I and M2**6==I and all(M2**d!=I for d in [1,2,3]))
 check(key+' actual homology dual map',M1*Q.T==Q.T*A.T and M2*Q.T==Q.T*B.T)
 check(key+' square-zero cusp',N*N==s.zeros(6))
 check(key+' integer cusp entries before ZZ conversion',all(v.q==1 for v in N))
 N=s.Matrix(6,6,[int(v) for v in N])
 S=smith_normal_form(N,domain=s.ZZ);di=[abs(int(S[i,i])) for i in range(6) if S[i,i]];check(key+' primitive rank-three cusp',di==[1,1,1])
 u1=s.Matrix(u1);u2=s.Matrix(u2)
 check(key+' both old fixed vectors',M1*u1==u1 and M2*u2==u2)
 check(key+' common exact quotient circle',ell*M1==ell and ell*M2==ell)
 check(key+' two old ell values one',(ell*u1)[0]==(ell*u2)[0]==1)
 for m,sign in [(5,1),(6,-1)]:
  for j in range(1,m):check(key+' nonidentity affine power '+str((m,j)),s.Rational(sign*j,m).q!=1)
 J=(M1-I).row_join(M2-I);target=I[:,1:];check(key+' exact full coinvariant kernel',hermite_normal_form(J)==target)
 L=hermite_normal_form(N);history=[arr(L)]
 for k in range(12):
  Lnew=hermite_normal_form(L.row_join(M1*L).row_join(M2*L));history.append(arr(Lnew))
  if Lnew==L:break
  L=Lnew
 else:raise AssertionError('normal closure did not stabilize')
 check(key+' invariant normal closure is actual kernel',L==target)
 rel=s.Matrix([[-1,5,0],[1,0,6],[0,1,1]])
 check(key+' peripheral unit determinant',rel.det()==1 and rel.inv()==s.Matrix([[-6,-5,30],[-1,-1,6],[1,1,-5]]))
 out[key]={'cusp_smith':di,'old_Q_map':arr(Q),'normal_closure_HNF_history':history,'old_vectors':{'u1':arr(u1),'u2':arr(u2)},'peripheral_relation_inverse':arr(rel.inv())}
result={'status':'PASS','checks':len(checks),'check_names':checks,'cases':out,'chronology':'New independent computation after reading the isolated old auxiliary target; no before-reading proof credit for its Q-lattice route','old_producer_imported':False,'definition_packet_sha256':sha256(p.read_bytes()).hexdigest(),'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'Leray_scope':'Named new canonical table plus actual rational intertwiner supplied by V owner; not inferred here from a basis-name match'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','checks','source_sha256']},indent=2))
