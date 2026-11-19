#!/usr/bin/env python3
"""Fresh local Taylor/ball verification of the connecting collar.
Uses the newly authored root-series chart, with independent local continuation
and exact geometric verification of coordinate-only cover witnesses.
"""
from pathlib import Path
import json,time,math
import minimum_root_regions as rr
from flint import acb,arb,acb_mat,ctx
ctx.dps=110
start=time.time();chart=rr.Chart('infinity');I=rr.I;minimum=chart.center_h;WEIGHTS=rr.weights;ORDER=160
poles=[acb((arb.pi()*(2*k+1)/5).cos(),(arb.pi()*(2*k+1)/5).sin()) for k in range(5)]
def norm(M):return max([sum((M[i,j].abs_upper()*WEIGHTS[j]/WEIGHTS[i] for j in range(6)),arb(0)).upper() for i in range(6)],key=float)
bnorm=[norm(B) for B in chart.B];steps=0;largest_tail=0.0

def transition(z,d):
 global steps,largest_tail
 distances=[(z-p).abs_lower() for p in poles];radius=min(distances,key=float)/2;ratio=d.abs_upper()/radius;assert ratio<arb('.3')
 den=arb(1)
 for dist in distances:den*=dist-radius
 magnitude=z.abs_upper()+radius;bound=sum((bnorm[j]*magnitude**j for j in range(5)),arb(0))/den
 tail=((bound*radius).exp()*ratio**(ORDER+1)/(1-ratio)).upper()
 q=[(1+z**5)]+[math.comb(5,j)*z**(5-j) for j in range(1,6)]
 nums=[]
 for j in range(5):nums.append(sum((chart.B[k]*(math.comb(k,j)*z**(k-j)) for k in range(j,5)),acb_mat(6,6)))
 cs=[I]
 for n in range(ORDER):
  rhs=sum((cs[n-j]*nums[j] for j in range(min(4,n)+1)),acb_mat(6,6))
  for j in range(1,min(5,n+1)+1):rhs-=cs[n-j+1]*(q[j]*(n-j+1))
  cs.append(rhs/(q[0]*(n+1)))
 value=cs[-1]
 for C in reversed(cs[:-1]):value=value*d+C
 for i in range(6):
  for j in range(6):
   error=tail*WEIGHTS[i]/WEIGHTS[j];value[i,j]+=acb(arb(0,error),arb(0,error))
 steps+=1;largest_tail=max(largest_tail,float(tail));return value

def edge(Y,z,w):
 d=w-z;dist=min([(z-p).abs_lower() for p in poles],key=float)
 if not d.abs_upper()<dist/10:
  m=(z+w)/2;return edge(edge(Y,z,m),m,w)
 return Y*transition(z,d)

def point(z):
 z0=z*arb('.95')/z.abs_upper();Y=rr.scalar_poly_matrix(chart.ypoly,z0);tail=chart.tail(z0.abs_upper())
 for i in range(6):
  for j in range(6):
   error=tail*chart.tail_multiplier[i][j];Y[i,j]+=acb(arb(0,error),arb(0,error))
 return edge(Y,z0,z)

def box(b):
 x0,x1,y0,y1=map(arb,b[:4]);cx=(x0+x1)/2;cy=(y0+y1)/2;z=acb(cx,cy);rho=(((x1-x0)/2)**2+((y1-y0)/2)**2).sqrt().upper();Z=acb(arb(cx,(x1-x0)/2),arb(cy,(y1-y0)/2));Y=point(z);G,_=chart.connection(Z);positive=acb_mat([[acb(G[i,j].abs_upper()) for j in range(6)] for i in range(6)]);initial=acb_mat([[acb(Y[i,j].abs_upper()) for j in range(6)] for i in range(6)]);variation=initial*((positive*rho).exp()-I)
 for i in range(6):
  for j in range(6):
   error=variation[i,j].real.upper();Y[i,j]+=acb(arb(0,error),arb(0,error))
 return Y
source=Path('/workspace/scratch/ae06852560d6/materials/S6_10_PAPERS_2_night_run/night_run/code/part1/certified_minimum_collar.json');oldboxes=json.loads(source.read_text())['accepted_boxes'];keys={tuple(b[:4]) for b in oldboxes};used=set();extra=[];discarded=0;maxgeometry=0
slope=(2*arb.pi()/5).tan();inner=arb('.98');outer=inner**(-arb(4)/5)

def geometry(b,depth=0):
 global discarded,maxgeometry
 maxgeometry=max(maxgeometry,depth);key=tuple(b)
 if key in keys:used.add(key);return
 x0,x1,y0,y1=map(arb,b);rmin=(x0*x0+y0*y0).sqrt();rmax=(x1*x1+y1*y1).sqrt()
 if rmax<inner or rmin>outer or y0>slope*x1:discarded+=1;return
 cx=(x0+x1)/2;cy=(y0+y1)/2;rho=(((x1-x0)/2)**2+((y1-y0)/2)**2).sqrt().upper();z=acb(cx,cy)
 if rmin>0:
  qc=-1/z**5-1;qbound=qc.abs_upper()+5*rho/rmin**6
  if qbound<arb('.25'):discarded+=1;return
 if depth>=12:extra.append(b);return
 x0,x1,y0,y1=b;xm=(x0+x1)/2;ym=(y0+y1)/2
 for child in [[x0,xm,y0,ym],[xm,x1,y0,ym],[x0,xm,ym,y1],[xm,x1,ym,y1]]:geometry(child,depth+1)
geometry([0.,1.03125,0.,1.03125]);print('geometry',len(used),'old boxes used;',len(extra),'new boundary boxes; discarded',discarded,flush=True)
boxes=[b[:4] for b in oldboxes]+extra;accepted=[];failed=[];attempted=0;maxdepth=0

def verify(b,index,depth=0):
 global attempted,maxdepth
 attempted+=1;maxdepth=max(maxdepth,depth)
 try:h=rr.hvalue(box(b));passed=bool(h>minimum);note={'h':str(h)}
 except (ValueError,ZeroDivisionError) as e:passed=False;note={'error':str(e)}
 if passed:accepted.append({'original_index':index,'extra_depth':depth,'box':b,**note});return
 if depth>=6:failed.append({'original_index':index,'extra_depth':depth,'box':b,**note});return
 x0,x1,y0,y1=b;xm=(x0+x1)/2;ym=(y0+y1)/2
 for child in [[x0,xm,y0,ym],[xm,x1,y0,ym],[x0,xm,ym,y1],[xm,x1,ym,y1]]:verify(child,index,depth+1)
for k,b in enumerate(boxes):
 verify(b,k)
 if (k+1)%25==0:print('collar',k+1,'of',len(boxes),'leaves',len(accepted),'failures',len(failed),'steps',steps,flush=True)
out={'status':'PASS' if not failed else 'INCOMPLETE','method':'Fresh polynomial-denominator local Taylor continuation with weighted Cauchy/Gronwall bounds and rectangle Peano-Baker estimates','series_order':ORDER,'dps':ctx.dps,'inner':str(inner),'outer':str(outer),'cusp_excluded_radius':'.25','geometry':{'pass':True,'old_boxes_used':len(used),'additional_boundary_boxes':len(extra),'discarded':discarded,'maxdepth':maxgeometry},'continuation_steps':steps,'largest_local_tail':largest_tail,'accepted_count':len(accepted),'failed_count':len(failed),'attempted':attempted,'max_extra_depth':maxdepth,'accepted':accepted,'failures':failed,'runtime_seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['accepted','failures']},indent=2),flush=True)
