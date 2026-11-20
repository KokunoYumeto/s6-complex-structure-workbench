"""Actual native moving-star normal maps and own cap for the fresh zero fan.

All rays and degrees are extracted from its complete physical lower-face
charts. Native characters, T0, actual source fan and both reciprocal normal
maps are retained. The cap class direction is the explicit NC.19-20 map.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,gc
from K111_fan4_exact import *

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'K111_new_zero_endpoint_v2.json').read_text());data.pop('stellar_history',None);gc.collect()
checks=0
def ck(x,m):
 global checks
 checks+=1
 if not x:raise AssertionError(m)
A=(0,0,0,1);B1=(-1,0,0,1);B2=(-2,-1,0,1);B3=(-1,-1,0,1)
face0=tuple(sorted((A,B1)));face1=tuple(sorted((B2,B3)))
T0=((1,0,8,1),(0,1,6,1),(0,0,1,0),(0,0,0,1));I=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
delta=(-1,0,0,0);divisor={};edges=set();records=[]
for rec in data['cones']:
 c=tuple(tuple(v) for v in rec['rays']);weights=tuple(rec['physical_weights']);face=tuple(sorted(v for v,w in zip(c,weights) if w))
 if face not in [face0,face1]:continue
 H=I if face==face0 else T0;aligned=tuple(mv(H,v) for v in c)
 ck(mv(H,delta)==delta,'actual T0 alignment retains physical cocharacter')
 ck({mv(H,v) for v in face}=={A,B1},'entire native normal face aligns exactly')
 mm=(1,-1,1,1) if face==face0 else (1,-2,1,1)
 mp=(-1,2,0,0) if face==face0 else (-1,1,0,0)
 qm=[];orders=[]
 for v,w in zip(aligned,weights):
  dm=dot(mm,v);dp=dot(mp,v)
  if w==-1:ck((dm,dp)==(1,0),'full negative native normal derivative')
  elif w==1:ck((dm,dp)==(0,1),'full positive native normal derivative')
  else:
   ck(w==0,'all actual moving normal weights are exactly minus/plus one')
   q=(v[1],v[2]);qm.append(q);orders.append((dm,dp))
   if q in divisor:ck(divisor[q]==(dm,dp),'complete coefficient divisors agree in every adjacent native chart')
   divisor[q]=(dm,dp)
 ck(len(qm)==2,'complete moving surface chart has two tangent rays')
 detq=qm[0][0]*qm[1][1]-qm[0][1]*qm[1][0]
 ck(abs(detq)==1,'actual native source quotient chart is saturated and regular')
 edges.add(tuple(sorted(qm)))
 records.append(dict(owner=rec['id'],face='native infinity' if face==face0 else 'native zero after T0',original_rays=c,aligned_rays=aligned,physical_weights=weights,negative_row=mm,positive_row=mp,source_rays=qm,divisor_orders=orders,full_units=['c_q/eta','eta'] if face==face0 else ['c_q*f0/eta','eta/f0']))
ck(divisor[(1,0)]==divisor[(-1,0)]==(0,0),'both horizontal native Cartier-module orders vanish')
interior=sorted((v for v in divisor if v[1]>0),key=lambda v:F(v[0],v[1]),reverse=True)
rays=[(1,0),*interior,(-1,0)]
ck(edges=={tuple(sorted((a,b))) for a,b in zip(rays,rays[1:])},'whole extracted native source fan covers its original marked half-plane exactly once')
ck((0,1) in interior,'original generic Z point section meets the actual zero-valuation component')
n=len(interior);M=[[F(0) for j in range(n)] for i in range(n)]
walls=[]
for i,v in enumerate(interior):
 left=rays[i];right=rays[i+2];idx=0 if v[0] else 1
 s=-F(left[idx]+right[idx],v[idx])
 ck(s.denominator==1 and all(left[k]+right[k]+s*v[k]==0 for k in range(2)),'exact full native source wall relation')
 M[i][i]=s
 if i:M[i][i-1]=1
 if i+1<n:M[i][i+1]=1
 walls.append(dict(ray=v,left=left,right=right,self_intersection=s))
coeffs=[[divisor[v][k] for v in interior] for k in range(2)]
pair=lambda a,b:sum(a[i]*M[i][j]*b[j] for i in range(n) for j in range(n))
xyz=[pair(coeffs[0],coeffs[0]),pair(coeffs[0],coeffs[1]),pair(coeffs[1],coeffs[1])]
hd=list(divisor[(0,1)])
ck(all(sum(M[i][j]*interior[j][1] for j in range(n))==0 for i in range(n)),'actual full divisor of original P spans the intersection kernel')

# Contract only the actual sum of its current two neighbors, retaining the
# marked (0,1) native sphere fibre and the two horizontal sections.
remaining=list(rays);chronology=[];exceptional=[]
while len(remaining)>3:
 possible=[]
 for i in range(1,len(remaining)-1):
  v=remaining[i]
  if v==(0,1):continue
  if tuple(a+b for a,b in zip(remaining[i-1],remaining[i+1]))==v:possible.append(i)
 ck(bool(possible),'next actual ordinary native source contraction exists')
 i=min(possible,key=lambda i:(remaining[i][1],remaining[i]));left,v,right=remaining[i-1:i+2]
 degrees=tuple(divisor[v][k]-divisor[left][k]-divisor[right][k] for k in range(2))
 exceptional.append(degrees)
 chronology.append(dict(left=left,removed=v,right=right,coefficient_divisor_exceptional=degrees,source_maps=['(u,w)->(u,u*w)','(u,w)->(u*w,w)'],inverse_maps=['w_old/u_old','u_old/w_old']))
 remaining.pop(i)
ck(remaining==[(1,0),(0,1),(-1,0)],'actual marked native sphere-times-disc endpoint of contractions')
fresh=[-sum(x*x for x,y in exceptional),-sum(x*y for x,y in exceptional),-sum(y*y for x,y in exceptional)]
ck(fresh==xyz,'chronological ordinary blowups reproduce the full divisor intersection matrix')
x2=2*hd[0]+xyz[0];xy=-hd[0]-hd[1]-xyz[1];y2=2*hd[1]+xyz[2]
c1=x2+2*xy+y2;c2=xy;p1=-3*len(chronology)
physical=[c1-c2,p1+c1-4*c2]
out=dict(scope='Fresh complete native moving star from the new zero atlas. Every original coefficient derivative, T0 map, source wall and own-cap line class is retained. The explicit NC opposite-parameter-disc bordism gives x=h+Dminus and y=-h-Dplus; the two actual divisor and chronological-blowup computations agree. These values belong to the newly constructed auxiliary model.',
         checks=checks,charts=records,source_rays=rays,divisor_coefficients=coeffs,intersection_matrix=M,walls=walls,normal_divisor_intersections=xyz,marked_section_pairings=hd,chronological_contractions=chronology,
         own_cap_positive_line_intersections=[x2,xy,y2],own_cap_bundle_c1_squared=c1,own_cap_bundle_c2=c2,own_cap_tangent_p1=p1,physical_moving_pair=physical)
(root/'K111_new_moving_cap.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps(dict(checks=checks,charts=len(records),compact_source_curves=n,contractions=len(chronology),divisor_intersections=serial(xyz),marked_section_pairings=hd,positive_line_intersections=serial([x2,xy,y2]),c1_squared=serial(c1),c2=serial(c2),tangent_p1=p1,physical_moving_pair=serial(physical)),indent=2))
