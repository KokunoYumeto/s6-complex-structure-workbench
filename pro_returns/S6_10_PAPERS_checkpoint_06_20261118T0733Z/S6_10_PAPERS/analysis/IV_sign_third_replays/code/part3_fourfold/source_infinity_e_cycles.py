#!/usr/bin/env python3
"""Exact central cycles of the local E fixed surfaces.

The actual v=0 Tate identity Q*P^2=1 trivializes the determinant
normal line by Z^a*V^2 on the punctured source annulus.  The
calculation uses that explicit relative marking.  It does not
identify this E atlas with the cap atlas.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import gcd
import json,gc
ROOT=Path(__file__).resolve().parents[2]

def quad(v,I):
 return sum(v[i]*I[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))
def det(v,w):return v[0]*w[1]-w[0]*v[1]

def one(a,b,N):
 src=ROOT/'code/part3_fourfold'/f'source_infinity_fixed_charts_{a}_{b}_{N}.json'
 with (ROOT/'records/literature_fourfold.md').open('a') as f:
  f.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened '
    +str(src.relative_to(ROOT))+'. Reason: exact central E-cycle intersection '
    'and relative determinant-normal calculation. Material: actual rays, '
    'face periods and physical normal labels; no cap attachment inferred.\n')
 data=json.loads(src.read_text())
 charts={c['id']:c for c in data['charts']}
 comps=[c for c in data['components'] if c['boundary_tag']=='E']
 rows=[];total=Q(0);checks=0
 for c in comps:
  v=c['canonical_vectors']
  assert len(v)==2 and all(t[0]==0 and t[2:]==[1,0] for t in v)
  j=min(t[1] for t in v)
  assert sorted(t[1] for t in v)==[j,j+1]
  rays={}
  for name in c['charts']:
   ch=charts[name];assert ch['sector']=='E'
   n1,n2=ch['period_from_canonical']
   for col in ch['zero_weight_columns']:
    Z,V,r,s=[ch['matrix'][i][col] for i in range(4)]
    Z-=s*(2*n1+b*n2)
    V-=r*N*n2+s*(-a*n1+(N-2)*n2)
    assert s>0 and gcd(Z,s)==1
    l=Z//(2*s)
    Z-=2*l*s;V+=a*l*s
    db=(2*j+1)*r-2*V-a*Z
    key=(Z,s)
    val={'ray':[Z,s],'ambient_unwrapped':[Z,V,r,s],
         'determinant_normal_divisor':db}
    if key in rays:assert rays[key]['determinant_normal_divisor']==db
    else:rays[key]=val
    checks+=3
  ordered=sorted(rays.values(),key=lambda t:Q(t['ray'][0],t['ray'][1]))
  R=len(ordered);assert R>=2
  I=[[0]*R for _ in range(R)]
  for i in range(R):
   prev=ordered[(i-1)%R]['ray'][:]
   cur=ordered[i]['ray']
   nxt=ordered[(i+1)%R]['ray'][:]
   if i==0:prev[0]-=2*prev[1]
   if i==R-1:nxt[0]+=2*nxt[1]
   assert det(prev,cur)==-1 and det(cur,nxt)==-1
   I[i][i]=det(prev,nxt)
   I[i][(i-1)%R]+=1;I[i][(i+1)%R]+=1
   checks+=2
  mult=[t['ray'][1] for t in ordered]
  assert all(sum(I[i][j]*mult[j] for j in range(R))==0 for i in range(R))
  K=[s-1 for s in mult]
  D=[t['determinant_normal_divisor'] for t in ordered]
  K2=quad(K,I);D2=quad(D,I)
  assert K2==-(R-2)
  p1=K2-2*R
  res=Q(p1-3*D2,24)
  total+=res
  rows.append({'id':c['id'],'chain_index':j,'curve_count':R,
    'curves':ordered,'intersection_matrix':I,'fibre_multiplicities':mult,
    'canonical_divisor':K,'canonical_square':K2,
    'determinant_normal_divisor':D,'determinant_normal_square':D2,
    'relative_euler':R,'relative_p1':p1,
    'relative_normal_link_residue':str(res)})
  checks+=R+3
 summary={'utc':datetime.now(timezone.utc).isoformat(),
  'parameters':{'a':a,'b':b,'N':N},
  'status':'PASS: actual local E cycles, intersections and explicit relative normal marking',
  'checks':checks,'component_count':len(rows),
  'relative_E_residue':str(total),
  'scope':'Local E annular marking by dlog(Z) wedge dT and Z^a V^2. '
    'The cap component permutation and global boundary orientation are not identified.'}
 stem=ROOT/'code/part3_fourfold'/f'source_infinity_e_cycles_{a}_{b}_{N}'
 Path(str(stem)+'.json').write_text(json.dumps({'summary':summary,'components':rows},
  separators=(',',':'))+'\n')
 Path(str(stem)+'_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps(summary,indent=2),flush=True)
 del data,charts
 gc.collect()
if __name__=='__main__':
 for case in ((2,1,6),(1,2,8)):one(*case)
