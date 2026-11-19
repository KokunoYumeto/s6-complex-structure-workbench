#!/usr/bin/env python3
"""Fresh reconstruction checks for K86, PS and NP, with original proof directions retained."""
from pathlib import Path
import hashlib,json
import sympy as s
BASE=Path(__file__).resolve().parents[2]
passed=[]
def ck(name,v):
 assert s.simplify(v)==0,(name,s.simplify(v))
 passed.append(name)
a,b,j,mu=s.symbols("a b j mu")
P,c,v=s.symbols("P c v",nonzero=True)
ck("full TL point factor",(1+P)/(2*((P+1)/(2*P)))-P)
ck("full marked P",(-(1+c)**2/v-(1+c)/(1-c)).subs(v,c*c-1))
x,y,xb,yb=s.symbols("x y xb yb");r2=x*xb+y*yb
G=s.Matrix([[-yb,-x],[-xb,y]]);Gc=s.Matrix([[-y,-xb],[-x,yb]])
ck("conjugate Hopf determinant",G.det()+r2)
for z in G*Gc.T-r2*s.eye(2):ck("unitary coefficient map",z)
x0,r=s.symbols("x0 r")
ck("literal blowup residue",x0/((x0-1)**2-1-x0*r)-1/(x0-2-r))
wp,wm,cS=s.symbols("wp wm cS");d=wm-wp;c1sq=-(1-2*a)**2;c2=-a*(a-1)+d
kB=c2-c1sq;ellB=3-c1sq+4*c2
ck("whole fixed Euler cube",kB-(3*a*a-3*a+1+d))
ck("whole fixed p1 line",ellB-(4+4*d))
ck("reduced complete pair",(8-kB-cS-1).subs(a,2)+d+cS)
ck("good complete pair",(2-kB-cS).subs(a,1)-(1-d-cS))
VV=s.Matrix([x,-y]);HH=s.Matrix([yb,xb])/r2
ck("actual source horizontal",(s.Matrix([[y,x]])*HH)[0]-1)
ck("source determinant",s.Matrix.hstack(VV,HH).det()-1)
for z in HH-yb/(x*r2)*VV-s.Matrix([0,1/x]):ck("x shear",z)
for z in HH+xb/(y*r2)*VV-s.Matrix([1/y,0]):ck("y shear",z)
Q=s.Matrix([[1,-1],[0,1]]);targets=[]
for av in (1,2):
 bv=3-av;W=s.Matrix([[1,bv],[-av,-2]]);B=2*Q.inv()*W*Q
 l=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]]
 xx,yy=Q.inv()*s.Matrix([0,1]);w=[xx,yy,-xx-yy];dd=[-xx-2*yy,-2*xx-yy,xx-yy]
 I=[-w[i]+dd[i]*(l[i]+1) for i in range(3)];J=[-w[i]-dd[i]*(l[i]+1) for i in range(3)]
 z=s.symbols("v00 v01 v02 v11 v12 v22 d0 d1 d2")
 V=s.Matrix([[z[0],z[1],z[2]],[z[1],z[3],z[4]],[z[2],z[4],z[5]]]);D=s.Matrix(z[6:]);eq=[]
 for i in (1,2):
  e=s.zeros(3,1);e[i]=w[i];e[0]-=w[0];f=s.zeros(3,1);f[i]=I[i];f[0]-=I[0]
  eq+=list(V*e-f);eq+=[w[i]*D[i]-w[0]*D[0]-J[i]+J[0]]
 eq+=[V[2,2]+2+2*mu,D[2]+2+2*mu]
 sol=s.solve(eq,z);assert len(sol)==9
 for ee in eq:ck("full nine-variable target",ee.subs(sol))
 inc=[s.simplify((D[i]-V[i,i]).subs(sol)/4) for i in (0,1)]
 want=[3*mu+3,3*mu+3] if av==1 else [3*mu+9,3*mu]
 for g,h in zip(inc,want):ck("actual directed increment",g-h)
 targets.append({"a":av,"V":str(V.subs(sol)),"D":str(D.subs(sol)),"increments":list(map(str,inc))})
def wedge(A,B):
 out={}
 for I,u in A.items():
  for J,vv in B.items():
   if set(I)&set(J):continue
   sg=(-1)**sum(i>jj for i in I for jj in J);key=tuple(sorted(I+J))
   out[key]=s.expand(out.get(key,0)+sg*u*vv)
 return out
def ff(i,jj,vv):return {(min(i,jj),max(i,jj)):vv*(1 if i<jj else -1)}
def plus(*args):
 out={}
 for D in args:
  for I,vv in D.items():out[I]=s.expand(out.get(I,0)+vv)
 return out
alpha,theta,tt=s.symbols("alpha theta tt")
F=plus(ff(0,3,1),ff(4,3,-2),ff(0,2,j),ff(4,2,-2*j-a))
db=plus(ff(0,2,-j),ff(4,2,-j*(1+b*j)),ff(4,3,-b*j))
be={(1,):-j,(2,):-j*(alpha+(1+b*j)*theta),(3,):-b*j*theta}
Fs=plus(F,{I:tt*z for I,z in db.items()})
top=wedge(be,wedge(Fs,Fs)).get((0,1,2,3,4),0)
ck("full outward collar",s.integrate(3*top,(tt,0,1))+6*a*j+9*j*j+2*b*j**3)
Pb=2*b*(j+1)*j*(j-1)/6+(3-b)*(j+1)*j/2
dk=-9*j-3*b*j*j+b*j+6*a*j+9*j*j+2*b*j**3
ck("full cube assembly",(dk-6*Pb).subs(a,3-b))
m,n,k,rho,H=s.symbols("m n k rho H")
Dlog=n*rho*H+s.pi*s.I*n*m*rho*(rho-1)
DZ=n*k*theta*H+2*s.pi*s.I*n*m*k*k*theta*theta
ck("full DZ phase comparison",DZ-Dlog.subs(rho,k*theta)-s.pi*s.I*n*m*(k*k*theta*theta+k*theta))
phase_cases=0
for nv in (-1,1):
 for bv in (1,2):
  for jv in range(-3,4):
   for mv in range(1,9):
    for kv in range(4):
     assert (mv*nv*kv*(kv-1))%2==0
     assert (mv*nv*kv*(kv+1))%2==0
     assert (-nv*bv-nv*(4+2*bv*jv-bv))%2==0
     phase_cases+=1
paths=["notes/part3_source_zero_normal_clutch_working.md","notes/part3_source_zero_psi_pairing_audit.md","notes/part3_source_zero_native_parameter_composition.md"]
result={"status":"PASS","recovery_type":"Fresh executable reconstruction, not byte-identical original certificate","symbolic_checks":len(passed),"phase_seam_cases":phase_cases,"checks":passed,"full_target_systems":targets,"source_sha256":{p:hashlib.sha256((BASE/p).read_bytes()).hexdigest() for p in paths}}
(BASE/"code/part3_fourfold/reconstructed_k86_ps_np_checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k not in ("checks","full_target_systems","source_sha256")},indent=2))

