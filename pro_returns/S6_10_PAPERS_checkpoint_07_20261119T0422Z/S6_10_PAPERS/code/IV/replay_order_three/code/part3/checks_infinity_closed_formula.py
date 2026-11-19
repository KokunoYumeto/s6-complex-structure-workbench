"""Independent K93 full paired-prism and class evaluation audit."""
from pathlib import Path
import sys,json
from fractions import Fraction
import sympy as S
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"part3_root"))
import source_zero_all_fans as ZA,source_all_fans as CA
r,u,z,j,a=S.symbols("r u z j a",nonzero=True)
P=S.Matrix([[u,-r],[(1-u*z)/r,z]])
E=S.Matrix([[0,1],[1,0]]);J=S.diag(-1,1)
Ps=J*P*E
W=S.Matrix([[1,3-a],[-a,-2]])
BZ=2*P.inv()*W*P;BS=2*Ps.inv()*W*Ps
BC=-6*P.inv()*S.diag(1,0)*P
checks=[]
def ck(name,e):
 assert S.factor(e)==0,(name,S.factor(e))
 checks.append(name)
for k,e in enumerate(BZ+E*BS*E+2*BC+8*S.eye(2)):ck("full_winding_"+str(k),e)
def local(B,t,rr,uu):
 w=[rr,uu,-rr-uu];d=[-rr-2*uu,-2*rr-uu,rr-uu]
 l=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]]
 return ([t*w[i]+d[i]*(l[i]-t) for i in range(3)],[t*w[i]-d[i]*(l[i]-t) for i in range(3)])
IZ,JZ=local(BZ,-1,r,u);IS,JS=local(BS,-1,u,r);IC,JC=local(BC,-3,r,u)
weights=[r,u,-r-u];perm=[1,0,2]
for i in range(3):
 ck("I_reflected_"+str(i),IZ[i]+IS[perm[i]]+2*IC[i]+8*weights[i])
 ck("J_reflected_"+str(i),JZ[i]+JS[perm[i]]+2*JC[i]+8*weights[i])
Pb=lambda n:(3-a)*(n+1)*n*(n-1)/3+a*(n+1)*n/2
mu=2-a
cz=lambda n:-2-2*mu-12*Pb(n)
ez=lambda n:-2-2*mu+12*Pb(n)
cc=lambda n:18*n*(n-1)
ec=lambda n:-12-18*n*(n-1)
ck("selected_seed_c",cz(j)+cz(1-j)+2*cc(j)+4*(2*a+3))
ck("selected_seed_e",2*cz(j)-ez(j)+2*cz(1-j)-ez(1-j)+2*(2*cc(j)-ec(j))+4*(8*a-3))
D=r*u*(r+u);NN=r*r+r*u+u*u
c=-4*(2*a+1)*D*D;e=4*D*((2*a+1)*NN+2*a-8)
f=lambda N:1-a-3*(a-1)*(N-1)-(2*a+1)*(N-1)*(N-3)/4
for i,(rr,uu,wi) in enumerate([(r+u,u,r),(r,r+u,u)]):
 Dn=rr*uu*(rr+uu);Sn=rr*rr+rr*uu+uu*uu;w2=-rr-uu
 ck("norm_increment_"+str(i),Sn-NN-2*D/wi)
 ck("D_ratio_"+str(i),Dn/w2+D/wi)
 Vii=-8+c/wi**2;di=-8+e/wi
 Vnew=-8-4*(2*a+1)*Dn**2/w2**2
 dnew=-8+4*Dn*((2*a+1)*Sn+2*a-8)/w2
 ck("reset_V_"+str(i),Vnew-Vii)
 ck("reset_d_"+str(i),dnew-(2*Vii-di))
 ck("class_increment_"+str(i),f(Sn)-f(NN)+(di-Vii)/4)
def formula(aa,P):
 x,y=CA.inv(P)[1],CA.inv(P)[3];N=x*x+x*y+y*y
 return 1-aa-3*(aa-1)*(N-1)-(2*aa+1)*(N-1)*(N-3)//4
for aa in (1,2):
 for jj in range(-3,4):
  for word in [(),(0,),(0,0),(0,1),(0,0,1),(0,1,0),(0,1,1)]:
   PP=(1,0,jj,1)
   for k in word:PP=CA.mul(PP,(CA.Q0,CA.Q1)[k])
   q1=ZA.calculate(PP,aa,1,0)["physical_class_mod28"]
   q2=ZA.calculate(CA.mul((-1,0,0,1),PP),aa,1,0)["physical_class_mod28"]
   qc=CA.calculate(PP)["physical_class_mod28"]
   assert (-q1-q2-qc-formula(aa,PP))%28==0
   checks.append("algorithm_"+str((aa,jj,word)))
expected={1:[0,6,8,10,14,20,22,24],2:[5,7,9,13,19,21,23,27]}
for aa in (1,2):
 vals=sorted({int(f(2*t+1).subs(a,aa))%28 for t in range(28)})
 assert vals==expected[aa]
 checks.append("full_residue_"+str(aa))
out={"status":"PASS","count":len(checks),"checks":checks,"complete_images":expected}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","count":len(checks)}))
