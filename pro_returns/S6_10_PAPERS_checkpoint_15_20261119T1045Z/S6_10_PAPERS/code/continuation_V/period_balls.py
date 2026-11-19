#!/usr/bin/env python3
"""New certified Taylor continuation of the rank-six Fuchsian model.
Uses only current independently computed residue data and marked matrices.
All local Taylor tails use an analytic Cauchy/Gronwall bound. Numerical
rank selection only chooses a minor subsequently inverted with complex balls.
"""
from pathlib import Path
import sys,json,math,time
import numpy as np
from scipy.linalg import qr
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'build/continuation_numeric/python'))
from flint import acb,arb,acb_mat,ctx
ctx.dps=110
ORDER=220
source=json.loads(Path(__file__).with_name('fuchsian_model.json').read_text())
R0=acb_mat([[acb(x) for x in r] for r in source['R0']])
Ra=acb_mat([[acb(x) for x in r] for r in source['Rcusp']])
a=acb('-256/3125');I=acb_mat([[int(i==j) for j in range(6)] for i in range(6)])
Q1=R0+Ra
stats={'steps':0,'order':ORDER,'dps':ctx.dps,'maximum_local_tail':0.0}
def norm(M):
 vals=[sum((M[i,j].abs_upper() for j in range(M.ncols())),arb(0)).upper() for i in range(M.nrows())]
 return max(vals,key=float)
k0=norm(R0);ka=norm(Ra)
def local(z,delta):
 zz=acb(z.real,z.imag);dd=acb(delta.real,delta.imag)
 d0=zz.abs_lower();da=(zz-a).abs_lower();radius=min(d0,da,key=float)/2
 rho=dd.abs_upper()/radius
 assert rho<arb('0.3')
 K=k0/(d0-radius)+ka/(da-radius)
 tail=((K*radius).exp()*rho**(ORDER+1)/(1-rho)).upper()
 p0=zz*(zz-a);p1=2*zz-a;q0=Q1*zz-R0*a
 coeff=[I]
 prev=acb_mat(6,6)
 for n in range(ORDER):
  cur=coeff[-1]
  nxt=(cur*(q0-I*(n*p1))+prev*(Q1-I*(n-1)))/(p0*(n+1))
  coeff.append(nxt);prev=cur
 value=coeff[-1]
 for c in reversed(coeff[:-1]):value=value*dd+c
 err=acb(arb(0,tail),arb(0,tail))
 value=acb_mat([[value[i,j]+err for j in range(6)] for i in range(6)])
 stats['steps']+=1;stats['maximum_local_tail']=max(stats['maximum_local_tail'],float(tail))
 return value

def edge(H,z,w):
 delta=w-z;dist=min(abs(z),abs(z+256/3125))
 if abs(delta)>dist/10:
  m=(z+w)/2
  return edge(edge(H,z,m),m,w)
 return H*local(z,delta)
def path(points):
 H=I
 for z,w in zip(points,points[1:]):H=edge(H,complex(z),complex(w))
 return H
start=time.time();r=1/32
connector=path([1,r])
zero_circle=path([r,r+1j*r,-r+1j*r,-r-1j*r,r-1j*r,r])
Lzero=connector*zero_circle*connector.inv()
Linfty=path([1,1-1j,-1-1j,-1+1j,1+1j,1])
print('monodromy_done',stats['steps'],time.time()-start,flush=True)
M1=[[1,0,0,0,0,0],[0,1,1,2,2,1],[0,-1,0,-1,0,1],[1,-1,-1,-1,-1,-1],[-1,1,0,0,0,0],[1,0,0,1,0,0]]
M2=[[1,0,0,0,0,0],[0,0,0,0,1,0],[0,-1,-1,-1,-1,-1],[0,0,0,0,0,1],[0,1,0,0,0,0],[0,0,1,0,0,0]]
A=acb_mat(M1).transpose();B=acb_mat(M2).transpose()
positions=[(i,j) for i in range(6) for j in range(1,6)]
def approximate(x):return complex(float(x.real.mid()),float(x.imag.mid()))
def intertwiner(L1,L2):
 rows=[];rhs=[]
 for L,T in [(L1,A),(L2,B)]:
  for i in range(6):
   for j in range(1,6):
    rows.append([(L[c,j] if r==i else acb(0))-(T[i,r] if c==j else acb(0)) for r,c in positions])
    rhs.append(-L[0,j] if i==0 else acb(0))
 approx=np.array([[approximate(x) for x in row] for row in rows])
 _,_,piv=qr(approx.T,pivoting=True,mode='economic');chosen=list(map(int,piv[:30]))
 selected=acb_mat([rows[k] for k in chosen]);right=acb_mat([[rhs[k]] for k in chosen]);det=selected.det()
 assert not det.contains(0)
 sol=selected.solve(right);X=acb_mat(6,6);X[0,0]=1
 for k,(i,j) in enumerate(positions):X[i,j]=sol[k,0]
 residuals=[X*L1-A*X,X*L2-B*X]
 maxres=max(float(v.abs_upper()) for m in residuals for i in range(6) for j in range(6) for v in [m[i,j]])
 contains=all(m[i,j].contains(0) for m in residuals for i in range(6) for j in range(6))
 return X,chosen,str(det),maxres,contains
attempts=[];chosen_result=None
for invert in [(False,False),(True,True),(False,True),(True,False)]:
 L1=Linfty.inv() if invert[0] else Linfty;L2=Lzero.inv() if invert[1] else Lzero
 for conjugation in [0,1,-1]:
  C=I if conjugation==0 else (L2 if conjugation==1 else L2.inv())
  LL1=C*L1*C.inv()
  try:
   result=intertwiner(LL1,L2)
   attempts.append({'inverses':invert,'infinity_zero_conjugation':conjugation,'max_residual':result[3],'all_residuals_contain_zero':result[4]})
   if result[4]:chosen_result=(result,LL1,L2,invert,conjugation);break
  except ZeroDivisionError as e:attempts.append({'inverses':invert,'conjugation':conjugation,'error':str(e)})
 if chosen_result:break
if chosen_result is None:
 print(json.dumps(attempts,indent=2));raise RuntimeError('No compatible marked monodromy pair certified')
(result,usedL1,usedL2,invert,conjugation)=chosen_result;X,selected_rows,det,maxres,contains=result
print('intertwiner_done',attempts[-1],flush=True)
def height(Y):
 # unknowns Re v2, Im v2, Re v1, Im v1
 rows=[];rhs=[]
 for i in range(1,6):
  u,v=Y[i,1],Y[i,2]
  rows.append([u.imag,u.real,v.imag,v.real]);rhs.append(Y[i,3].real)
 approx=np.array([[float(x.mid()) for x in r] for r in rows])
 _,_,piv=qr(approx.T,pivoting=True,mode='economic');chosen=list(map(int,piv[:4]))
 C=acb_mat([[acb(x) for x in rows[i]] for i in chosen]);b=acb_mat([[acb(rhs[i])] for i in chosen])
 sol=C.solve(b);v2=acb(sol[0,0].real,sol[1,0].real);v1=acb(sol[2,0].real,sol[3,0].real)
 residual=[(Y[i,1]*v2+Y[i,2]*v1-acb(0,1)*Y[i,3]).imag for i in range(1,6)]
 assert all(v.contains(0) for v in residual)
 h=arb(96)/(625*arb.pi())*(Y[0,1]*v2+Y[0,2]*v1-acb(0,1)*Y[0,3]).imag
 return h,chosen,residual
h1,_,_=height(X)
H2=path([1,2]);D2inv=acb_mat([[acb(2)**(-source['gauge_exponents'][i]) if i==j else 0 for j in range(6)] for i in range(6)])
Y2=X*H2*D2inv;h2,_,_=height(Y2)
assert h1 < -1
# Confirm the 34-decimal interval printed in P1.16, as an exact decimal pair.
lo=arb('-1.0342766224163217994942488453783461');hi=arb('-1.0342766224163217994942488453783460')
printed_h1_matches=bool(h1>lo and h1<hi)
def mat(M):return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
out={'method':'Fuchsian row-ODE Taylor recurrence with Cauchy/Gronwall interval tail','stats':stats,'runtime_seconds':time.time()-start,'zero_path':[str(x) for x in [1,r,r+1j*r,-r+1j*r,-r-1j*r,r-1j*r,r,1]],'infinity_path':[str(x) for x in [1,1-1j,-1-1j,-1+1j,1+1j,1]],'monodromy_matching_attempts':attempts,'selected_rows':selected_rows,'selected_minor_determinant':det,'X':mat(X),'Lzero':mat(Lzero),'Linfty':mat(Linfty),'Y2':mat(Y2),'h1':str(h1),'h2':str(h2),'printed_h1_interval_verified':printed_h1_matches,'scope':'Certified local continuations and selected linear systems. Existence of compatible overdetermined intertwiner is a separate exact P1.15 dependency; residual containment is checked. No global minimum or infinity assertion is inferred.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['stats','runtime_seconds','h1','h2','printed_h1_interval_verified','scope']},indent=2),flush=True)
