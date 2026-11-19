#!/usr/bin/env python3
"""New cusp Frobenius/ball verification. Earlier JSON supplies rectangles only.
The residue recurrence, weighted majorant, integral cusp basis and inequalities
are constructed here from the newly derived two-pole connection.
"""
from pathlib import Path
import json,time,math
import sympy as S
import numpy as np
from scipy.linalg import qr
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
import infinity_and_splitting as ins
pb=ins.pb
from flint import acb,arb,acb_mat,acb_poly,ctx
ctx.dps=110
I=pb.I;R=pb.Ra;A=pb.R0;NTERMS=600;MAJOR=arb('.4');W=[arb(100),arb(1),arb(1),arb(1),arb(1),arb(1)]
def norm(M):return max([sum((M[i,j].abs_upper()*W[j]/W[i] for j in range(6)),arb(0)).upper() for i in range(6)],key=float)
rnorm=norm(R);anorm=norm(A);C=1+2*rnorm+4*rnorm*rnorm;K=((1-MAJOR).log()*(-C*anorm)).exp().upper()
def ad(Q):return Q*R-R*Q
coeff=[I];partial=I
for n in range(1,NTERMS+1):
 rhs=partial*A;U=rhs/n+ad(rhs)/(n*n)+ad(ad(rhs))/(n*n*n);coeff.append(U);partial=U-partial
# partial=sum_{k=0}^{n}(-1)^{n-k} P_k generates P*A/(1+q).
BLOCK=32
polys=[[[acb_poly([P[i,j] for P in coeff[k:k+BLOCK]]) for k in range(0,len(coeff),BLOCK)] for j in range(6)] for i in range(6)]
def tail(r):
 ratio=r/MAJOR;assert ratio<1
 return (K*ratio**(NTERMS+1)/(1-ratio)).upper()
def Pvalue(z):
 z=acb(z);power=z**BLOCK
 def ev(blocks):
  v=acb(0)
  for b in reversed(blocks):v=v*power+b(z)
  return v
 out=acb_mat([[ev(polys[i][j]) for j in range(6)] for i in range(6)]);err=tail(z.abs_upper())
 for i in range(6):
  for j in range(6):
   rad=err*W[i]/W[j];out[i,j]+=acb(arb(0,rad),arb(0,rad))
 return out
start=time.time();q0=acb('1/100');lambda0=pb.a*(1+q0);points=[acb(1),acb(1,1),lambda0+acb(0,1),lambda0];F=I
for z,w in zip(points,points[1:]):F=ins.edge(F,z,w)
H=pb.X*F*Pvalue(q0).inv()*(I-R*q0.log())
Nball=H*R*H.inv()*acb(0,2*arb.pi());N=S.zeros(6)
for i in range(6):
 for j in range(6):
  x=Nball[i,j];v=round(float(x.real.mid()));assert x.real.contains(v) and x.imag.contains(0) and x.real.rad()<arb('1e-80') and x.imag.rad()<arb('1e-80');N[i,j]=v
assert N*N==S.zeros(6) and N.rank()==3
D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(N).convert_to(S.ZZ));D,U,V=[Q.to_Matrix() for Q in [D,U,V]]
assert all(abs(D[i,i])==1 for i in range(3));beta=V[:,:3];alpha=N*beta;J=alpha.row_join(beta);assert abs(J.det())==1
standard=S.zeros(6);standard[:3,3:]=S.eye(3);assert J.inv()*N*J==standard
Ji=acb_mat([[acb(str(J.inv()[i,j])) for j in range(6)] for i in range(6)]);Hj=Ji*H;ej=Ji*acb_mat([[int(i==0)] for i in range(6)]);minimum=ins.constant;cstar=-minimum;shift=625*arb.pi()/96*cstar
# Uniform holomorphic remainder in |q|<=.01, constructed from absolute series.
inner=arb('1/100');Pdisc=acb_mat(I)
for i in range(6):
 for j in range(6):
  variation=sum((coeff[n][i,j].abs_upper()*inner**n for n in range(1,NTERMS+1)),arb(0))+tail(inner)*W[i]/W[j]
  Pdisc[i,j]+=acb(arb(0,variation),arb(0,variation))
Vdisc=Hj*Pdisc;period=acb_mat([[Vdisc[i,j]-(shift*ej[i,0] if j==3 else 0) for j in [1,2,3]] for i in range(6)])
top=acb_mat([[period[i,j] for j in range(3)] for i in range(3)]);bottom=acb_mat([[period[i+3,j] for j in range(3)] for i in range(3)]);Cdisc=top*bottom.inv();y0=-inner.log()/(2*arb.pi())
B=acb_mat([[acb(Cdisc[i,j].imag+(y0 if i==j else 0)) for j in range(3)] for i in range(3)])
cubic=[B.det().real,sum((B[i,i].real*B[j,j].real-B[i,j].real*B[j,i].real for i in range(3) for j in range(i+1,3)),arb(0)),sum((B[i,i].real for i in range(3)),arb(0)),arb(1)]
innerpass=all(x>0 for x in cubic)
print('cusp_basis',J.tolist(),'inner_cubic',list(map(str,cubic)),'inner_pass',innerpass,flush=True)
def hvalue(Y):
 rows=[[acb(Y[i,1].imag),acb(Y[i,1].real),acb(Y[i,2].imag),acb(Y[i,2].real)] for i in range(1,6)];arr=np.array([[float(x.real.mid()) for x in r] for r in rows]);_,_,piv=qr(arr.T,pivoting=True,mode='economic');ids=list(map(int,piv[:4]));M=acb_mat([rows[i] for i in ids]);b=acb_mat([[acb(Y[i+1,3].real)] for i in ids]);v=M.solve(b);co=acb_mat([[acb(Y[0,1].imag),acb(Y[0,1].real),acb(Y[0,2].imag),acb(Y[0,2].real)]]);return arb(96)/(625*arb.pi())*((co*v)[0,0].real-Y[0,3].real)
def value(q):return H*(I+R*q.log())*Pvalue(q)
def box(b):
 x0,x1,y0,y1=map(arb,b[:4]);cx=(x0+x1)/2;cy=(y0+y1)/2;z=acb(cx,cy);rho=(((x1-x0)/2)**2+((y1-y0)/2)**2).sqrt().upper();Z=acb(arb(cx,(x1-x0)/2),arb(cy,(y1-y0)/2));Y=value(z);G=R/Z+A/(1+Z);positive=acb_mat([[acb(G[i,j].abs_upper()) for j in range(6)] for i in range(6)]);initial=acb_mat([[acb(Y[i,j].abs_upper()) for j in range(6)] for i in range(6)]);variation=initial*((positive*rho).exp()-I)
 for i in range(6):
  for j in range(6):
   error=variation[i,j].real.upper();Y[i,j]+=acb(arb(0,error),arb(0,error))
 return Y
# The inner punctured disc is connected. One height value fixes its side
# of the nonvanishing determinant throughout the disc.
innerheight=hvalue(value(acb('1/100')));innerpass=innerpass and bool(innerheight>minimum)
original=Path('/workspace/scratch/ae06852560d6/materials/S6_10_PAPERS_2_night_run/night_run/code/part1/certified_minimum_cusp_annulus.json');boxes=json.loads(original.read_text())['accepted_boxes']
keys={tuple(b[:4]) for b in boxes};used=set();holes=[];discarded=0

def geometry(b,depth=0):
 global discarded
 key=tuple(b)
 if key in keys:used.add(key);return
 x0,x1,y0,y1=b
 mnx=0 if x0<=0<=x1 else min(abs(x0),abs(x1));mny=0 if y0<=0<=y1 else min(abs(y0),abs(y1));mxx=max(abs(x0),abs(x1));mxy=max(abs(y0),abs(y1))
 if arb(mnx)**2+arb(mny)**2>arb('.25')**2 or arb(mxx)**2+arb(mxy)**2<arb('.01')**2:discarded+=1;return
 if depth>=7:holes.append(b);return
 xm=(x0+x1)/2;ym=(y0+y1)/2
 for child in [[x0,xm,y0,ym],[xm,x1,y0,ym],[x0,xm,ym,y1],[xm,x1,ym,y1]]:geometry(child,depth+1)
geometry([-.25,.25,-.25,.25]);geopass=not holes and used==keys
accepted=[];failed=[];attempted=0;maxdepth=0

def verify(b,index,depth=0):
 global attempted,maxdepth
 attempted+=1;maxdepth=max(maxdepth,depth)
 try:h=hvalue(box(b));passed=bool(h>minimum);note={'h':str(h),'h_lower':str(h.lower()),'h_upper':str(h.upper()),'gap_lower':str((h-minimum).lower()),'above_common_exact_threshold':bool(h>arb('-1.0945402503114027801162682630549457037'))}
 except (ValueError,ZeroDivisionError) as e:passed=False;note={'error':str(e)}
 if passed:assert bool(h>arb('-1.0945402503114027801162682630549457037'))
 if passed:accepted.append({'original_index':index,'extra_depth':depth,'box':b[:4],**note});return
 if depth>=5:failed.append({'original_index':index,'extra_depth':depth,'box':b[:4],**note});return
 x0,x1,y0,y1=b[:4];xm=(x0+x1)/2;ym=(y0+y1)/2
 for child in [[x0,xm,y0,ym],[xm,x1,y0,ym],[x0,xm,ym,y1],[xm,x1,ym,y1]]:verify(child,index,depth+1)
for k,b in enumerate(boxes):
 verify(b,k)
 if (k+1)%1000==0:print('annulus',k+1,'leaves',len(accepted),'failed',len(failed),'attempts',attempted,flush=True)
out={'status':'PASS' if innerpass and geopass and not failed else 'INCOMPLETE','method':'Fresh Fuchsian-residue Frobenius series; weighted Cauchy majorant; exact primitive Smith cusp basis; cubic positivity and adaptive ball rectangle cover','series_order':NTERMS,'majorant_radius':str(MAJOR),'weighted_R_norm':str(rnorm),'weighted_A_norm':str(anorm),'majorant_K':str(K),'tail_at_quarter':str(tail(arb('.25'))),'cusp_N':[[int(x) for x in row] for row in N.tolist()],'integral_J':[[int(x) for x in row] for row in J.tolist()],'H':pb.mat(H),'inner_cubic':list(map(str,cubic)),'inner_cubic_lower_bounds':[str(x.lower()) for x in cubic],'inner_cubic_upper_bounds':[str(x.upper()) for x in cubic],'inner_height':str(innerheight),'inner_pass':bool(innerpass),'geometry':{'pass':geopass,'used':len(used),'discarded':discarded,'holes':holes},'annulus':{'passed':len(accepted),'failed':len(failed),'attempts':attempted,'max_extra_depth':maxdepth,'accepted':accepted,'failures':failed},'runtime_seconds':time.time()-start,'scope':'Cusp disk and annulus only; root regions and collar remain separately certified. Integral identification of monodromy and pointwise half-plane height depend on P1.15/P1.8.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['H','annulus']},indent=2),flush=True)
