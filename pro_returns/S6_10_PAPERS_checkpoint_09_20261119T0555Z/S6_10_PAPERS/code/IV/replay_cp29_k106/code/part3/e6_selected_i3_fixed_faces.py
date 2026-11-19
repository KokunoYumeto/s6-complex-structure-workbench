"""Exact physical minimal-face orbits of all three selected-I3 corners.

The canonical translations solve the full integral period matrix; no
bounded word search is used. All actual coefficient functions are retained.
"""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction as F
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
paths={'generic':ROOT/'code/part3/e6_selected_i3_common_fan.json','corners':ROOT/'code/part3/e6_selected_i3_corner_lifts.json','one':ROOT/'code/part3/e6_selected_i3_p_one_cayley.json','index':ROOT/'code/part3/e6_selected_i3_generic_corner_index.json'}
data={k:json.loads(p.read_text()) for k,p in paths.items()}
labels=[]
def ck(n,t):
 assert t,n
 labels.append(n)
def cols(C):return list(map(list,zip(*C)))
def mv(A,v):return [sum(a*b for a,b in zip(row,v)) for row in A]
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def T(v,word,mode):
 a,b=word
 if mode=='generic':
  x,y,h=v;return (x+(7*a+2*b)*h,y+(a+2*b)*h,h)
 x,y,r,s=v
 if mode=='zero':return (x+(r+3*s)*a-s*b,y+6*s*a+(r+2*s)*b,r,s)
 if mode=='infinity':return (x+s*(7*a+2*b),y+s*(a+2*b)+r*b,r,s)
 return (x+r*(3*a-b),y+4*(r+s)*b,r,s)
def canonical(C,mode):
 X,Y,*base=map(sum,zip(*C))
 if mode=='generic':
  H=base[0];aa,bb,cc,dd=7*H,2*H,H,2*H
 else:
  R,H=base
  if mode=='zero':aa,bb,cc,dd=R+3*H,-H,6*H,R+2*H
  elif mode=='infinity':aa,bb,cc,dd=7*H,2*H,H,R+2*H
  else:aa,bb,cc,dd=3*R,-R,0,4*(R+H)
 det=aa*dd-bb*cc
 if det:
  ck('positive period determinant',det>0)
  n=((dd*X-bb*Y)//det,(aa*Y-cc*X)//det);kernel=[]
 else:
  ck('actual rank-one lower period',mode in ['one','infinity'] and aa==bb==cc==0 and dd>0 and X==0)
  n=(0,Y//dd);kernel=[[1,0]]
 return tuple(sorted(T(v,(-n[0],-n[1]),mode) for v in C)),n,kernel
def unit_vectors(mode,n):
 a,b=n
 if mode=='generic':return {'p':[-4*(2*a+b),-b,0],'p_minus_1':[4*(2*a+b),0,0],'c':[2*a+b,0,0]}
 if mode=='zero':return {'c0':[0,b,0,0]}
 if mode=='infinity':return {'f':[2*a+b,0,0,0]}
 return {'p':[a,-2*a+b,0,0],'c':[0,b,0,0]}
def tag(face,mode):
 if mode=='generic':return 'common_base'
 if mode=='one':
  if all(v[3]==0 for v in face):return 'generic_common_boundary'
  if all(v[2]==0 for v in face):return 'lower_boundary'
 else:
  if all(v[2]==0 for v in face):return 'generic_common_boundary'
  if all(v[3]==0 for v in face):return 'lower_boundary'
 return 'interior'
configs={'generic':data['generic']['cones'],'zero':data['corners']['corners']['zero']['cones'],'one':data['one']['cones'],'infinity':data['corners']['corners']['infinity']['cones']}
outputs={}
for mode,cones in configs.items():
 groups={};charts=[]
 for ci,co in enumerate(cones):
  N=cols(co['rays']);n=len(N);delta=[1,0,0] if mode=='generic' else ([0,1,0,0] if mode in ['zero','one'] else [1,0,0,0])
  if 'inverse_matrix' in co:A=co['inverse_matrix']
  elif 'dual_characters' in co:A=co['dual_characters']
  else:A=[[int(v) for v in row] for row in S.Matrix(N).inv().tolist()]
  ck(mode+': full integral inverse '+str(ci),mm(N,A)==[[int(i==j) for j in range(n)] for i in range(n)])
  w=mv(A,delta);ck(mode+': retained physical weights '+str(ci),w==co['physical_weights'])
  nz=[i for i,x in enumerate(w) if x];ti=[i for i,x in enumerate(w) if not x]
  face=[tuple(co['rays'][i]) for i in nz];fc,word,kernel=canonical(face,mode)
  C=[T(v,(-word[0],-word[1]),mode) for v in co['rays']]
  weightmap={tuple(C[i]):w[i] for i in nz};cw=[weightmap[v] for v in fc]
  rec=groups.setdefault(fc,{'canonical_face':fc,'normal_weights':cw,'dimension':4-len(fc),'tag':tag(fc,mode),'period_stabilizer_basis':kernel,'occurrences':[]})
  ck(mode+': consistent normal eigenlines '+str(ci),rec['normal_weights']==cw and rec['period_stabilizer_basis']==kernel)
  rec['occurrences'].append({'cone':ci,'period_from_canonical':word,'canonical_four_or_three_rays':C,'normal_columns':nz,'tangent_columns':ti,'normal_period_unit_exponents':{un:mv(A,vec) for un,vec in unit_vectors(mode,word).items()}})
  charts.append({'cone':ci,'canonical_face':fc,'period_from_canonical':word,'inverse_matrix':A,'physical_weights':w,'normal_columns':nz,'tangent_columns':ti})
 components=[];mapping={}
 for fc,rec in sorted(groups.items()):
  i=len(components);mapping[fc]=i;rec['id']=i
  ck(mode+': same tag '+str(i),all(tag(tuple(T(v,o['period_from_canonical'],mode) for v in fc),mode)==rec['tag'] for o in rec['occurrences']))
  if rec['dimension']==0:
   prod=1
   for w in rec['normal_weights']:prod*=w
   rec['positive_U_pair']=[str(F(1,prod)),str(F(sum(w*w for w in rec['normal_weights']),prod))]
   rec['physical_M_pair']=[str(-F(1,prod)),str(-F(sum(w*w for w in rec['normal_weights']),prod))]
  components.append(rec)
 for ch in charts:ch['component']=mapping[ch.pop('canonical_face')]
 outputs[mode]={'cones':len(cones),'components':components,'charts':charts,'summary':[{'dimension':dim,'tag':tg,'count':count} for (dim,tg),count in sorted(Counter((r['dimension'],r['tag']) for r in components).items())]}
 print(mode,outputs[mode]['summary'],flush=True)
# The actual protected generic-facet map identifies each generic component.
for mode in ['zero','infinity']:
 ids=defaultdict(set)
 for row in data['index']['corners'][mode]:
  ci=row['common_cone'];target=row['corner_cone']
  ids[outputs['generic']['charts'][ci]['component']].add(outputs[mode]['charts'][target]['component'])
 ck(mode+': each common component has one actual corner continuation',all(len(v)==1 for v in ids.values()))
 outputs[mode]['generic_component_identifications']=[{'common_component':i,'component':next(iter(v))} for i,v in sorted(ids.items())]
ids=defaultdict(set)
for ci,co in enumerate(configs['one']):
 if co['kind']!='upper_star':continue
 for ref in co.get('generic_references',[]):
  gid=ref['common_cone'];ids[outputs['generic']['charts'][gid]['component']].add(outputs['one']['charts'][ci]['component'])
ck('one: each common component has one actual corner continuation',all(len(v)==1 for v in ids.values()))
outputs['one']['generic_component_identifications']=[{'common_component':i,'component':next(iter(v))} for i,v in sorted(ids.items())]
for mode in ['zero','one','infinity']:
 ck(mode+': every common component retained',len(outputs[mode]['generic_component_identifications'])==len(outputs['generic']['components']))
 # Every recorded normal comparison carries the exact original unit function.
 outputs[mode]['full_unit_dictionary']=({'c0':'(p-1)^4*c','c':'lambda0*c_q*K*u_s^(-4)'} if mode=='zero' else {'f':'p^(-4)*(p-1)^4*c','u':'p^(-1)'} if mode=='infinity' else {'p':'1+v','c':'lambda0*c_q*K*u_s^(-4)'})
out={'status':'PASS','checks':len(labels),'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths.values()},'atlases':outputs,'scope':'Exact minimal physical faces, all integral period identifications and full normal unit arrows for4264 generic and three executed corners. Compact characteristic evaluations, cap/reference attachment and total return remain separate.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS',len(labels),flush=True)
