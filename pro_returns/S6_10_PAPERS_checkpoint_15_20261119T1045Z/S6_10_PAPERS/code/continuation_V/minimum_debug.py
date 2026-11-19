#!/usr/bin/env python3
"""New verifier of the two root-region inequality covers and local Hessian.
Earlier JSON is read only for rectangle coordinates (a finite cover witness).
All coefficients, normalizations, ball bounds and inequalities are recomputed.
No prior checking program, coefficient, matrix or interval result is imported.
"""
from pathlib import Path
import json,math,sys,time
import sympy as S
import period_balls as pb
from flint import acb,arb,acb_mat,acb_poly,ctx
ctx.dps=110
ORDER=3000;RADIUS=arb('0.999');weights=[arb(1),arb('1/128'),arb('1/128'),arb('1/32'),arb('1/64'),arb('1/32')]
source=json.loads(Path('/workspace/scratch/ae06852560d6/restore/S6_10_PAPERS/code/continuation_V/minimum_root_regions.py').with_name('fuchsian_model.json').read_text())
cover_path=Path('/workspace/scratch/ae06852560d6/materials/S6_10_PAPERS_2_night_run/night_run/code/part1/certified_minimum_root.json')
cover=json.loads(cover_path.read_text())
I=pb.I

def scalar_poly_matrix(polys,z):return acb_mat([[polys[i][j](z) for j in range(6)] for i in range(6)])
def precondition(H):
 B=acb_mat([[acb(H[i,j].imag if t==0 else H[i,j].real) for j,t in [(1,0),(1,1),(2,0),(2,1),(3,0)]] for i in range(1,6)])
 Binv=B.inv();top=acb_mat([[acb(H[0,1].imag),acb(H[0,1].real),acb(H[0,2].imag),acb(H[0,2].real),0]])*Binv
 T=acb_mat(6,6);T[0,0]=1
 for j in range(1,6):T[0,j]=-top[0,j-1]
 for i in range(1,6):
  for j in range(1,6):T[i,j]=Binv[i-1,j-1]
 return T*H

def equations(Y):
 M=acb_mat([[acb(Y[i,1].imag),acb(Y[i,1].real),acb(Y[i,2].imag),acb(Y[i,2].real)] for i in range(1,5)])
 b=acb_mat([[acb(Y[i,3].real)] for i in range(1,5)])
 c=acb_mat([[acb(Y[0,1].imag),acb(Y[0,1].real),acb(Y[0,2].imag),acb(Y[0,2].real)]])
 d=Y[0,3].real
 return M,b,c,d

def hvalue(Y):
 import numpy as np
 from scipy.linalg import qr
 rows=[[acb(Y[i,1].imag),acb(Y[i,1].real),acb(Y[i,2].imag),acb(Y[i,2].real)] for i in range(1,6)]
 arr=np.array([[float(q.real.mid()) for q in row] for row in rows])
 _,_,piv=qr(arr.T,pivoting=True,mode='economic');chosen=list(map(int,piv[:4]))
 M=acb_mat([rows[i] for i in chosen]);b=acb_mat([[acb(Y[i+1,3].real)] for i in chosen]);_,_,c,d=equations(Y);x=M.solve(b)
 return arb(96)/(625*arb.pi())*((c*x)[0,0].real-d)

class Chart:
 def __init__(self,name):
  self.name=name;self.m=5 if name=='infinity' else 4
  q0,qm,var=(3125,256,'u') if name=='infinity' else (256,3125,'t')
  symbol=S.symbols(var);C=S.Matrix([[S.sympify(x,locals={var:symbol}) for x in r] for r in source['root_connection_matrices'][name]])
  polynomial=(C*(q0+qm*symbol**self.m)).applyfunc(S.cancel)
  self.scale=(arb(q0)/qm).root(self.m)
  self.B=[acb_mat([[acb(str(S.expand(polynomial[i,j]).coeff(symbol,k)))*self.scale**(k+1)/q0 for j in range(6)] for i in range(6)]) for k in range(self.m)]
  rows=[]
  for i in range(6):
   rows.append(sum((self.B[k][i,j].abs_upper()*weights[j]/weights[i] for j in range(6) for k in range(self.m)),arb(0)))
  self.bound=max(rows,key=float).upper()
  self.K=(self.bound*(-(1-RADIUS).log()/self.m+arb(self.m-1)/self.m*RADIUS)).exp().upper()
  self.coeff=[I]
  for n in range(1,ORDER+1):
   rhs=acb_mat(6,6)
   if n>=self.m:rhs-=self.coeff[n-self.m]*(n-self.m)
   for j in range(min(self.m-1,n-1)+1):rhs+=self.coeff[n-1-j]*self.B[j]
   self.coeff.append(rhs/n)
  self.upoly=[[acb_poly([U[i,j] for U in self.coeff]) for j in range(6)] for i in range(6)]
  if name=='infinity':
   U1=self.raw(1/self.scale);self.H=pb.X*U1.inv()
  else:
   t=arb('1/4');lam=1/256
   U=self.raw(t/self.scale);F=pb.path([1,lam]);D=acb_mat([[acb(t)**(-[0,2,1,0,-1,-2][i]) if i==j else 0 for j in range(6)] for i in range(6)])
   self.H=pb.X*F*D*U.inv()
  self.Hc=precondition(self.H)
  self.Ycoef=[self.Hc*U for U in self.coeff]
  self.ypoly=[[acb_poly([Y[i,j] for Y in self.Ycoef]) for j in range(6)] for i in range(6)]
  self.deriv_bound_poly=[[acb_poly([acb(self.Ycoef[n+1][i,j].abs_upper()*(n+1)) for n in range(ORDER)]) for j in range(6)] for i in range(6)]
  self.tail_multiplier=[[sum((self.Hc[i,k].abs_upper()*weights[k]/weights[j] for k in range(6)),arb(0)).upper() for j in range(6)] for i in range(6)]
  self.center_h=hvalue(self.Hc)
  print('chart',name,'B',self.bound,'center_h',self.center_h,flush=True)
 def tail(self,r):
  ratio=arb(r)/RADIUS;assert ratio<1
  return (self.K*ratio**(ORDER+1)/(1-ratio)).upper()
 def raw(self,z):
  z=acb(z);v=scalar_poly_matrix(self.upoly,z);tail=self.tail(z.abs_upper())
  for i in range(6):
   for j in range(6):
    err=tail*weights[i]/weights[j];v[i,j]+=acb(arb(0,err),arb(0,err))
  return v
 def box(self,b):
  x0,x1,y0,y1=map(arb,b[:4]);cx=(x0+x1)/2;cy=(y0+y1)/2
  z=acb(cx,cy);rho=(((x1-x0)/2)**2+((y1-y0)/2)**2).sqrt().upper()
  point=scalar_poly_matrix(self.ypoly,z);tail=self.tail(z.abs_upper())
  for i in range(6):
   for j in range(6):
    err=tail*self.tail_multiplier[i][j];point[i,j]+=acb(arb(0,err),arb(0,err))
  rectangle=acb(arb(cx,(x1-x0)/2),arb(cy,(y1-y0)/2));G,_=self.connection(rectangle)
  absolute_G=acb_mat([[acb(G[i,j].abs_upper()) for j in range(6)] for i in range(6)])
  absolute_Y=acb_mat([[acb(point[i,j].abs_upper()) for j in range(6)] for i in range(6)])
  # Peano--Baker domination on every radial segment of this convex rectangle.
  variation=absolute_Y*((absolute_G*rho).exp()-I)
  for i in range(6):
   for j in range(6):
    err=variation[i,j].real.upper();point[i,j]+=acb(arb(0,err),arb(0,err))
  return point
 def connection(self,z):
  num=acb_mat(6,6);der=acb_mat(6,6)
  for j,B in enumerate(self.B):
   num+=B*z**j
   if j:der+=B*(j*z**(j-1))
  den=1+z**self.m;G=num/den;Gp=der/den-num*(self.m*z**(self.m-1)/den**2)
  return G,Gp


chart=Chart('infinity')
for b in [[.25,.265625,.125,.140625],[.625,.62890625,.75390625,.7578125],[0,.01,0,.01]]:
 Y=chart.box(b)
 z=acb((b[0]+b[1])/2,(b[2]+b[3])/2)
 Y0=scalar_poly_matrix(chart.ypoly,z)
 print('box',b,'point',[[str(Y0[i,j]) for j in range(1,4)] for i in range(1,5)],'tail',chart.tail(z.abs_upper()),flush=True)
 try:print('point-h',hvalue(Y0),flush=True)
 except Exception as e:print('POINT FAIL',e,flush=True)
 print('pointrows',[[str(Y0[i,j]) for j in range(1,4)] for i in range(1,5)],flush=True)
 print('boxrows',[[str(Y[i,j]) for j in range(1,4)] for i in range(1,5)],flush=True)
 try:print('h',hvalue(Y),flush=True)
 except Exception as e:print('FAIL',e,flush=True)
