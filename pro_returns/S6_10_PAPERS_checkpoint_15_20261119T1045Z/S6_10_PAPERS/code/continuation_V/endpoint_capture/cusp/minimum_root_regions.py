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
source=json.loads(Path(__file__).with_name('fuchsian_model.json').read_text())
cover_path=Path('/workspace/scratch/ae06852560d6/materials/S6_10_PAPERS_2_night_run/night_run/code/part1/certified_minimum_root.json')
cover=json.loads(cover_path.read_text())
I=pb.I

BLOCK=32
def blocked_polynomial(coefficients):
 return [acb_poly(coefficients[j:j+BLOCK]) for j in range(0,len(coefficients),BLOCK)]
def scalar_poly_matrix(polys,z):
 power=z**BLOCK
 def evaluate(blocks):
  value=acb(0)
  for block in reversed(blocks):value=value*power+block(z)
  return value
 return acb_mat([[evaluate(polys[i][j]) for j in range(6)] for i in range(6)])
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
  self.upoly=[[blocked_polynomial([U[i,j] for U in self.coeff]) for j in range(6)] for i in range(6)]
  if name=='infinity':
   U1=self.raw(1/self.scale);self.H=pb.X*U1.inv()
  else:
   t=arb('1/4');lam=1/256
   U=self.raw(t/self.scale);F=pb.path([1,lam]);D=acb_mat([[acb(t)**(-[0,2,1,0,-1,-2][i]) if i==j else 0 for j in range(6)] for i in range(6)])
   self.H=pb.X*F*D*U.inv()
  self.Hc=precondition(self.H)
  self.Ycoef=[self.Hc*U for U in self.coeff]
  self.ypoly=[[blocked_polynomial([Y[i,j] for Y in self.Ycoef]) for j in range(6)] for i in range(6)]
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

if __name__ == '__main__':
 start=time.time();charts={n:Chart(n) for n in ['infinity','zero']};minimum=charts['infinity'].center_h
 # Uniform Hessian on the full central square.
 c=charts['infinity'];square=[-.1,.1,-.1,.1];Y=c.box(square);z=acb(arb(0,arb('0.1')),arb(0,arb('0.1')));G,Gp=c.connection(z);Yp=Y*G;Ypp=Y*(G*G+Gp)
 M,b,co,d=equations(Y);Mi=M.inv();x=Mi*b
 parts={}
 for key,Z in [('x',Yp),('y',Yp*acb(0,1)),('xx',Ypp),('xy',Ypp*acb(0,1)),('yy',-Ypp)]:parts[key]=equations(Z)
 xder={t:Mi*(parts[t][1]-parts[t][0]*x) for t in ['x','y']}
 Hess={}
 for ts,t,s in [('xx','x','x'),('xy','x','y'),('yy','y','y')]:
  Mt,bt,ct,dt=parts[t];Ms,bs,cs,ds=parts[s];Mts,bts,cts,dts=parts[ts]
  xts=Mi*(bts-Mts*x-Mt*xder[s]-Ms*xder[t])
  Hess[ts]=arb(96)/(625*arb.pi())*((cts*x+ct*xder[s]+cs*xder[t]+co*xts)[0,0].real-dts)
 Hess['determinant']=Hess['xx']*Hess['yy']-Hess['xy']**2
 local_pass=bool(Hess['xx']>0 and Hess['determinant']>0)
 print('hessian', {k:str(v) for k,v in Hess.items()},'pass',local_pass,flush=True)
 # Exact quadtree cover validation uses coordinates only, never prior outcomes.
 def cover_ok(name,boxes):
  accepted={tuple(b[:4]) for b in boxes};used=set();holes=[];discarded=0
  slope=(2*arb.pi()/5).tan()
  def walk(b,depth):
   nonlocal discarded
   key=tuple(b)
   if key in accepted:used.add(key);return
   x0,x1,y0,y1=b
   outside=(arb(x0)**2+arb(y0)**2>arb('.98')**2)
   if name=='infinity':outside=outside or arb(y0)>slope*arb(x1) or (arb(x1)<=arb('.1') and arb(y1)<=arb('.1'))
   if outside:discarded+=1;return
   if depth==8:holes.append(b);return
   xm=(x0+x1)/2;ym=(y0+y1)/2
   for q in [[x0,xm,y0,ym],[xm,x1,y0,ym],[x0,xm,ym,y1],[xm,x1,ym,y1]]:walk(q,depth+1)
  walk([0.,1.,0.,1.],0)
  return {'valid':not holes and len(used)==len(accepted),'used':len(used),'discarded':discarded,'holes':holes[:10]}
 results={}
 for name,chart in charts.items():
  boxes=cover['charts'][name]['accepted_boxes'];accepted=[];failures=[]
  attempted=0;max_extra_depth=0
  def verify_box(b,index,depth=0):
   global attempted,max_extra_depth
   attempted+=1;max_extra_depth=max(max_extra_depth,depth)
   try:
    h=hvalue(chart.box(b));passed=bool(h>minimum);reason={'h':str(h),'h_lower':str(h.lower()),'h_upper':str(h.upper()),'gap_lower':str((h-minimum).lower()),'above_common_exact_threshold':bool(h>arb('-1.0945402503114027801162682630549457037'))}
   except (ZeroDivisionError,ValueError) as e:passed=False;reason={'error':str(e)}
   if passed:assert bool(h>arb('-1.0945402503114027801162682630549457037'))
   if passed:accepted.append({'original_index':index,'extra_depth':depth,'box':b[:4],**reason});return
   if depth>=5:failures.append({'original_index':index,'extra_depth':depth,'box':b[:4],**reason});return
   x0,x1,y0,y1=b[:4];xm=(x0+x1)/2;ym=(y0+y1)/2
   for q in [[x0,xm,y0,ym],[xm,x1,y0,ym],[x0,xm,ym,y1],[xm,x1,ym,y1]]:verify_box(q,index,depth+1)
  for index,b in enumerate(boxes):
   verify_box(b,index)
   if (index+1)%200==0:print('boxes',name,index+1,'leaves',len(accepted),'failures',len(failures),'attempts',attempted,flush=True)
  results[name]={'new_norm_bound':str(chart.bound),'center_h':str(chart.center_h),'cover_geometry':cover_ok(name,boxes),'passed':len(accepted),'attempted':attempted,'max_extra_depth':max_extra_depth,'failed':len(failures),'failures':failures,'accepted':accepted}
 passed=local_pass and all(v['failed']==0 and v['cover_geometry']['valid'] for v in results.values())
 out={'status':'PASS' if passed else 'INCOMPLETE','method':'Fresh polynomial root series, norm majorants, real preconditioning, analytic matrix derivatives and rectangle-coordinate witness verification','order':ORDER,'dps':ctx.dps,'radius':str(RADIUS),'local_hessian':{k:str(v) for k,v in Hess.items()},'local_hessian_pass':local_pass,'root_regions':results,'runtime_seconds':time.time()-start,'scope':'Only finite root regions and central Hessian. Cusp and collar have separate obligations.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'status':out['status'],'hessian_pass':local_pass,'regions':{k:{'passed':v['passed'],'failed':v['failed'],'cover':v['cover_geometry']} for k,v in results.items()},'runtime':out['runtime_seconds']},indent=2),flush=True)
