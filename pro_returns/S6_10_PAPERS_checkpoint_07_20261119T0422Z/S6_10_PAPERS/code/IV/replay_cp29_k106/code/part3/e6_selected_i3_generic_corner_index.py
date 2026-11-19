"""Exact protected generic-face owners and full recorded period labels."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
ip=ROOT/'code/part3/e6_selected_i3_common_fan.json'
cp=ROOT/'code/part3/e6_selected_i3_corner_lifts.json'
g=json.loads(ip.read_text());d=json.loads(cp.read_text());out={};checks=0
def T(v,n,lo,hi):
 x,y,r,s=v;a,b=n
 return (x+(r*lo[0][0]+s*hi[0][0])*a+(r*lo[0][1]+s*hi[0][1])*b,
         y+(r*lo[1][0]+s*hi[1][0])*a+(r*lo[1][1]+s*hi[1][1])*b,r,s)
def canonical(C,lo,hi):
 X,Y,R,S=map(sum,zip(*C));a=R*lo[0][0]+S*hi[0][0];b=R*lo[0][1]+S*hi[0][1];c=R*lo[1][0]+S*hi[1][0];e=R*lo[1][1]+S*hi[1][1];D=a*e-b*c
 assert D>0
 n=((e*X-b*Y)//D,(a*Y-c*X)//D)
 return tuple(sorted(T(v,(-n[0],-n[1]),lo,hi) for v in C)),n
for mode,corner in d['corners'].items():
 lo=corner['period_matrices']['lower'];hi=corner['period_matrices']['upper']
 faces={tuple(map(tuple,x['canonical_rays'])):x for x in corner['facets'] if x['boundary']=='generic'}
 rows=[]
 for ci,co in enumerate(g['cones']):
  if mode=='zero':
   par=g['parent_zero_instances'][co['zero_parent']];i,j=par['shift']
   C=[]
   for x,y,h in co['rays']:
    x-=h*(7*i+2*j);y-=h*(i+2*j)
    C.append((y,x+3*y-6*h,0,h))
   parent_word={'K':i,'J':j,'native_h':i+j,'native_B':2*i+j}
  else:
   C=[(x,y,0,h) for x,y,h in co['rays']]
   parent_word={'K':0,'J':0,'native_h':0,'native_B':0}
  key,n=canonical(C,lo,hi);face=faces[key]
  assert len(face['occurrences'])==1
  occ=face['occurrences'][0];m=occ['period_from_canonical'];shift=[m[k]-n[k] for k in range(2)]
  target=corner['cones'][occ['cone']]
  actual=[target['rays'][k] for k in occ['local_columns']]
  translated=[T(v,shift,lo,hi) for v in C]
  assert set(map(tuple,actual))==set(translated)
  permutation=[actual.index(list(v)) for v in translated]
  checks+=1
  rows.append({'common_cone':ci,'common_rays':co['rays'],'native_upper_rays_before_canonicalization':C,'parent_inverse_period_word':parent_word,'native_canonicalizing_period':n,'corner_cone':occ['cone'],'corner_columns':occ['local_columns'],'native_period_from_input_to_owner':shift,'upper_vertex_permutation':permutation,'corner_inverse_matrix':target['inverse_matrix'],'physical_weights':target['physical_weights'],'zero_parent':co['zero_parent'],'one_parent':co['one_parent'],'infinity_parent':co['infinity_parent']})
 assert len(rows)==4264 and len({r['corner_cone'] for r in rows})==4264
 checks+=1
 out[mode]=rows
result={'status':'PASS','checks':checks,'common_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),'corner_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'scope':'Every protected generic facet with literal original-parent inverse period, final owner, target frame and vertex permutation. Full unit functions are the source SI3.21-22 and SI3.26-27, with these exact period labels.','corners':out}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='corners'},indent=2))
