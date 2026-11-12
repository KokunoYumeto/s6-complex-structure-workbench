"""Supplementary integer-chain checks for the original integral comparison."""
from pathlib import Path
import json, hashlib, math
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
W=Path(__file__).resolve().parents[1]
src=W/'src/the-original-integral-stable-group-and-its-completion-maps.md'
checks=[]; models=[]
def ck(name,value):
 assert value,name
 checks.append(name)
def bezout(a,b):
 old_r,r=a,b;old_s,s=1,0;old_t,t=0,1
 while r:
  q=old_r//r;old_r,r=r,old_r-q*r;old_s,s=s,old_s-q*s;old_t,t=t,old_t-q*t
 return old_r,old_s,old_t
for p in [2,3,5,7]:
 for a in range(1,7):
  q=p**a;g,u,v=bezout(12,q)
  d=Matrix([[0,12,q]])
  B=Matrix([[q,0],[0,q],[0,-12]])
  V=Matrix([[1,0,0],[0,q//g,u],[0,-12//g,v]])
  label=f'p={p}, a={a}'
  ck('Original cone squares to zero '+label,d*B==Matrix.zeros(1,2))
  ck('Full integral kernel coordinates '+label,V.det()==1 and d*V==Matrix([[0,0,g]]))
  coordinates=V.inv()*B
  ck('Both original incoming columns '+label,coordinates==Matrix([[q,0],[0,g],[0,0]]))
  invs=smith_normal_form(coordinates[:2,:],domain=ZZ)
  ck('Integer homology invariant factors '+label,sorted(abs(int(invs[i,i])) for i in range(2))==[g,q])
  gn=math.gcd(12,p*q); zn=Matrix([0,p*q//gn,-12//gn]);z=V[:,1]
  T=Matrix.diag(1,1,p);Tlow=Matrix([[1]]);Thigh=p*Matrix.eye(2)
  dn=Matrix([[0,12,p*q]]);Bn=Matrix([[p*q,0],[0,p*q],[0,-12]])
  ck('Actual cone transition is a chain map '+label,d*T==Tlow*dn and T*Bn==B*Thigh)
  ck('Actual torsion transition and connecting sign '+label,T*zn==(p*g//gn)*z and (int((T*zn)[2])-p*int(zn[2]))%12==0 and int(z[2])==-12//g)
  e=0;rem=12
  while rem%p==0:e+=1;rem//=p
  if e:
   ge=math.gcd(12,p**(a+e));factor=p**e*g//ge
   ck('Full exponent transition vanishes '+label,factor%g==0)
  else:ck('No omitted primary torsion '+label,g==1)
  models.append(dict(prime=p,exponent=a,original_differential=list(d),original_incoming=list(B),gcd=g,actual_cycle=list(z),transition_coefficient=p*g//gn))
ck('Original Bezout projectors',9**2-9==72 and 64**2-64==56*72 and 9*64==8*72 and 9+64==1+72)
for t in range(72):
 t2=9*t%72;t3=64*t%72
 ck(f'Both original primary inclusions t={t}',(t2+t3)%72==t and 8*t2%72==0 and 9*t3%72==0 and t2==9*(t%8)%72 and t3==8*((8*t)%9)%72)
ck('Exercise 8.1 original value',9*17%72==9 and 64*17%72==8 and (9+8)%72==17)
ck('Exact primary kernels',[t for t in range(72) if 9*t%72==0]==list(range(0,72,8)) and [t for t in range(72) if 64*t%72==0]==list(range(0,72,9)))
for r in range(13):
 m=max(3,r+2)
 ck(f'Original stable range and every next index r={r}',all(m+k+r<=2*(m+k)-2 for k in range(15)) and (m==3 or m-1+r>2*(m-1)-2))
ck('Original receiving sphere dimensions',[(7+5,7),(8+6,8),(9+7,9)]==[(12,7),(14,8),(16,9)])
report=dict(passed=len(checks),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),checks=checks,original_cone_models=models,scope='Finite supplementary checks of full integer cone differentials, integral kernel bases and incoming boundaries, actual transition chain maps, connecting signs, primary projection coefficients and original sphere indices. All-index finiteness, topological comparisons and inverse-limit proofs are written in the source; these checks do not certify those proofs.',publication=False)
out=W/'checks/INTEGRAL_STABLE_COMPARISON_CHECKS.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2,default=int)+'\n','utf-8')
print(json.dumps(dict(passed=len(checks),source_sha256=report['source_sha256'])))
