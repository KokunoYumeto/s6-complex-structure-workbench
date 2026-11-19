#!/usr/bin/env python3
"""Second independent normalization by root Frobenius monodromy.
No Fuchsian continuation/intertwiner program is imported. Input is the newly
derived rational connection and the original marked matrices. First-method
outputs are read only at the final comparison stage.
"""
from pathlib import Path
import sys,json,math,time
import sympy as S
import numpy as np
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'build/continuation_numeric/python'))
from flint import acb,arb,acb_mat,acb_poly,ctx
ctx.dps=100
I=acb_mat([[int(i==j) for j in range(6)] for i in range(6)]);WEIGHTS=[arb(1),arb('1/128'),arb('1/128'),arb('1/32'),arb('1/64'),arb('1/32')];N=1200;LORDER=160;RADIUS=arb('.9');data=json.loads(Path(__file__).with_name('fuchsian_model.json').read_text());steps=0

def norm(M):return max([sum((M[i,j].abs_upper()*WEIGHTS[j]/WEIGHTS[i] for j in range(6)),arb(0)).upper() for i in range(6)],key=float)
def add_error(M,error):
 for i in range(6):
  for j in range(6):
   r=error*WEIGHTS[i]/WEIGHTS[j];M[i,j]+=acb(arb(0,r),arb(0,r))
 return M
class Root:
 def __init__(self,name):
  self.m=5 if name=='infinity' else 4
  q0,qm,var=(3125,256,'u') if name=='infinity' else(256,3125,'t');v=S.symbols(var);C=S.Matrix([[S.sympify(t,locals={var:v}) for t in row] for row in data['root_connection_matrices'][name]]);P=(C*(q0+qm*v**self.m)).applyfunc(S.cancel);self.scale=(arb(q0)/qm).root(self.m)
  self.B=[acb_mat([[acb(str(S.expand(P[i,j]).coeff(v,k)))*self.scale**(k+1)/q0 for j in range(6)] for i in range(6)]) for k in range(self.m)];self.bnorm=[norm(B) for B in self.B]
  total=max([sum((self.B[k][i,j].abs_upper()*WEIGHTS[j]/WEIGHTS[i] for j in range(6) for k in range(self.m)),arb(0)).upper() for i in range(6)],key=float);self.major=(total*(-(1-RADIUS).log()/self.m+arb(self.m-1)/self.m*RADIUS)).exp().upper()
  U=[I]
  for n in range(1,N+1):
   Q=sum((U[n-1-k]*self.B[k] for k in range(min(self.m-1,n-1)+1)),acb_mat(6,6))
   if n>=self.m:Q-=U[n-self.m]*(n-self.m)
   U.append(Q/n)
  self.polys=[[[acb_poly([U[n][i,j] for n in range(k,min(k+32,N+1))]) for k in range(0,N+1,32)] for j in range(6)] for i in range(6)];self.poles=[acb((arb.pi()*(2*k+1)/self.m).cos(),(arb.pi()*(2*k+1)/self.m).sin()) for k in range(self.m)]
 def series(self,z):
  z=acb(z);power=z**32
  def ev(blocks):
   v=acb(0)
   for p in reversed(blocks):v=v*power+p(z)
   return v
  M=acb_mat([[ev(self.polys[i][j]) for j in range(6)] for i in range(6)]);ratio=z.abs_upper()/RADIUS;assert ratio<1;err=(self.major*ratio**(N+1)/(1-ratio)).upper();return add_error(M,err)
 def transition(self,z,d):
  global steps
  distances=[(z-p).abs_lower() for p in self.poles];rad=min(distances,key=float)/2;ratio=d.abs_upper()/rad;assert ratio<arb('.3');den=arb(1)
  for dist in distances:den*=dist-rad
  bound=sum((self.bnorm[j]*(z.abs_upper()+rad)**j for j in range(self.m)),arb(0))/den;err=((bound*rad).exp()*ratio**(LORDER+1)/(1-ratio)).upper();q=[1+z**self.m]+[math.comb(self.m,j)*z**(self.m-j) for j in range(1,self.m+1)];nums=[sum((self.B[k]*(math.comb(k,j)*z**(k-j)) for k in range(j,self.m)),acb_mat(6,6)) for j in range(self.m)];cs=[I]
  for n in range(LORDER):
   rhs=sum((cs[n-j]*nums[j] for j in range(min(self.m-1,n)+1)),acb_mat(6,6))
   for j in range(1,min(self.m,n+1)+1):rhs-=cs[n-j+1]*(q[j]*(n-j+1))
   cs.append(rhs/(q[0]*(n+1)))
  result=cs[-1]
  for C in reversed(cs[:-1]):result=result*d+C
  steps+=1;return add_error(result,err)
 def extend(self,Y,z,w):
  d=w-z;dist=min([(z-p).abs_lower() for p in self.poles],key=float)
  if not d.abs_upper()<dist/10:
   mid=(z+w)/2;return self.extend(self.extend(Y,z,mid),mid,w)
  return Y*self.transition(z,d)
def diagonal(powers,z):return acb_mat([[z**powers[i] if i==j else 0 for j in range(6)] for i in range(6)])
start=time.time();inf=Root('infinity');zero=Root('zero');z1=acb(1/inf.scale);U1=inf.series(z1);zet=acb((2*arb.pi()/5).cos(),(2*arb.pi()/5).sin());Linf=U1.inv()*inf.series(z1*zet)*diagonal([0,-2,-1,0,1,2],zet)
t=acb('1/4');lam=t**4;u=(arb(256)).root(5);zr=acb(u/inf.scale);Ur=inf.extend(U1,z1,zr);connector=U1.inv()*Ur*diagonal([0,-2,-1,0,1,2],acb(u));z0=t/zero.scale;E=diagonal([0,2,1,0,-1,-2],t);Ei=diagonal([0,2,1,0,-1,-2],acb(0,1)*t);Llocal=E.inv()*zero.series(z0).inv()*zero.series(acb(0,1)*z0)*Ei;Lzero=connector*Llocal*connector.inv()
inputdata=json.loads(Path('/workspace/scratch/ae06852560d6/materials/S6_08_PAPERS_2_returns_code/returns/S6_04_MAPS_MANIFOLDS/records/fourfolds_marked_survivor_input.json').read_text());A,B=[acb_mat(M).transpose() for M in inputdata['matrices']];pos=[(i,j) for i in range(6) for j in range(1,6)];rows=[];right=[]
for T,L in [(A,Linf),(B,Lzero)]:
 for i in range(6):
  for j in range(1,6):
   rows.append([(L[c,j] if r==i else acb(0))-(T[i,r] if c==j else acb(0)) for r,c in pos]);right.append(-L[0,j] if i==0 else acb(0))
# Greedy column elimination picks a minor; its invertibility is then proved
# by ball arithmetic rather than presumed from the approximate pivot choice.
M=np.array([[complex(float(x.real.mid()),float(x.imag.mid())) for x in row] for row in rows]);chosen=[];available=list(range(60))
for k in range(30):
 pivot=max(available,key=lambda i:abs(M[i,k]));chosen.append(pivot);available.remove(pivot);assert abs(M[pivot,k])>1e-12
 M[pivot,:]/=M[pivot,k]
 for i in available:M[i,:]-=M[i,k]*M[pivot,:]
C=acb_mat([rows[i] for i in chosen]);rhs=acb_mat([[right[i]] for i in chosen]);det=C.det();assert not det.contains(0);solution=C.solve(rhs);X=acb_mat(6,6);X[0,0]=1
for k,(i,j) in enumerate(pos):X[i,j]=solution[k,0]
residuals=[X*Linf-A*X,X*Lzero-B*X];assert all(V[i,j].contains(0) for V in residuals for i in range(6) for j in range(6))
# lambda2 is evaluated directly in the ordinary infinity-root series.
u2=arb(2)**(-arb(1)/5);Y2=X*U1.inv()*inf.series(acb(u2/inf.scale))*diagonal([0,8,4,0,-4,-8],acb(u2))
def parse(value):
 if value.endswith('j'):
  if ' + ' in value:r,i=value[:-1].rsplit(' + ',1);return acb(arb(r),arb(i))
  return acb(0,arb(value[:-1]))
 return acb(arb(value))
first=json.loads(Path(__file__).with_name('period_balls.json').read_text());comparisons={}
for name,V in [('X',X),('Y2',Y2)]:
 prior=acb_mat([[parse(t) for t in r] for r in first[name]]);difference=V-prior;largest=max([difference[i,j].abs_upper() for i in range(6) for j in range(6)],key=float);all_overlap=all(V[i,j].overlaps(prior[i,j]) for i in range(6) for j in range(6));assert largest<arb('1e-60') and all_overlap;comparisons[name]={'maximum_entry_difference':str(largest),'all_ball_entries_overlap':all_overlap,'at_least60_decimal_places_agree':True}
def mat(M):return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
# Fresh transversality determinants for the explicitly stated c=10 check.
determinants={}
for name,Y in [('lambda1',X),('lambda2',Y2)]:
 F=acb_mat([[Y[i,j]-(acb(625)*arb.pi()/96*10 if i==0 and j==3 else 0) for j in [1,2,3]] for i in range(6)])
 full=acb_mat([[F[i,j] if j<3 else F[i,j-3].conjugate() for j in range(6)] for i in range(6)])
 detF=full.det();assert detF.real.contains(0) and detF.imag>0;determinants[name]=str(detF)
out={'status':'PASS','method':'Independent root-Frobenius monodromy plus polynomial root-connection continuation, no imported first-method program','dps':ctx.dps,'root_terms':N,'local_terms':LORDER,'local_steps':steps,'selected_minor_determinant':str(det),'comparisons':comparisons,'c10_transversality_determinants':determinants,'X':mat(X),'Y2':mat(Y2),'Linf':mat(Linf),'Lzero':mat(Lzero),'runtime_seconds':time.time()-start};Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['X','Y2','Linf','Lzero']},indent=2))
