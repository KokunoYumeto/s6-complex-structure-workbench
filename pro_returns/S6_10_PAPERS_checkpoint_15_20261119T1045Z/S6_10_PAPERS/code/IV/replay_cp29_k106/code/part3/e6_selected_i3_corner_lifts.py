#!/usr/bin/env python3
"""Literal relative selected-I3 p=0 and p=infinity corner lifts.

The upper fan is the executed 4264-cone generic common fan.  Each old
four-cone is subdivided by the common refinement of its upper face, joined
to its unchanged complementary face.  Remaining residue stars are periodic
and relative to BOTH protected boundaries.  All parent quotient maps and
actual period-unit vectors are retained; no characteristic count is made.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict
from functools import lru_cache,reduce
from math import gcd
import importlib.util,json,hashlib,time,heapq
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('saved_periodic_resolution',ROOT/'code/part3/source_zero_regular_fan.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
det4=old.det4;det3=old.det3
common=json.loads((ROOT/'code/part3/e6_selected_i3_common_fan.json').read_text())
inf=json.loads((ROOT/'code/part3/e6_selected_i3_infinity_fan.json').read_text())
checks=[]
def ck(label,test):
 assert test,label
 checks.append(label)
def orient(C):
 C=tuple(map(tuple,C));return C if det4(C)>0 else (C[1],C[0],C[2],C[3])
def matcols(C):return list(map(list,zip(*C)))
def coords4(C,v):
 D=det4(C)
 return tuple(F(det4(C[:i]+(tuple(v),)+C[i+1:]),D) for i in range(4))
def primitive(v):
 g=reduce(gcd,map(abs,v));return tuple(x//g for x in v)
def coeff3(C,v):
 D=det3(tuple(zip(*C)))
 return tuple(F(det3(tuple(zip(*(C[:i]+(tuple(v),)+C[i+1:])))),D) for i in range(3))
def signed_area2(t):
 a,b,c=t;return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def on_top_segment(v,a,b):
 # All endpoints a,b have upper height one; v has positive upper height.
 x,y,_,h=v;aa=(a[0],a[1]);bb=(b[0],b[1]);pp=(F(x,h),F(y,h))
 return (bb[0]-aa[0])*(pp[1]-aa[1])==(bb[1]-aa[1])*(pp[0]-aa[0]) and all(min(aa[k],bb[k])<=pp[k]<=max(aa[k],bb[k]) for k in range(2))
class Fan:
 def __init__(self,mode):
  self.mode=mode;self.P=((1,0),(0,1)) if mode=='zero' else ((0,0),(0,1))
  self.H=((3,-1),(6,2)) if mode=='zero' else ((7,2),(1,2))
  self.delta=(0,1,0,0) if mode=='zero' else (1,0,0,0)
  self.cells={};self.index={};self.faces=defaultdict(set);self.heap=[];self.seq=0;self.history=[];self.all_cells={};self.start=time.monotonic()
  self.raw=[];self.initial=[]
 def T(self,v,n):
  x,y,r,s=v;a,b=n
  return (x+(r*self.P[0][0]+s*self.H[0][0])*a+(r*self.P[0][1]+s*self.H[0][1])*b,
          y+(r*self.P[1][0]+s*self.H[1][0])*a+(r*self.P[1][1]+s*self.H[1][1])*b,r,s)
 def canonical(self,C):
  X,Y,R,S=map(sum,zip(*C));aa=R*self.P[0][0]+S*self.H[0][0];bb=R*self.P[0][1]+S*self.H[0][1];cc=R*self.P[1][0]+S*self.H[1][0];dd=R*self.P[1][1]+S*self.H[1][1];D=aa*dd-bb*cc
  if D:
   assert D>0;n=((dd*X-bb*Y)//D,(aa*Y-cc*X)//D)
  else:
   assert self.mode=='infinity' and S==0 and X==0 and R>0;n=(0,Y//R)
  return tuple(sorted(self.T(v,(-n[0],-n[1])) for v in C)),n
 def add(self,C,parent):
  C,n=self.canonical(tuple(C));parent=tuple(self.T(v,(-n[0],-n[1])) for v in parent)
  if C in self.index:return self.index[C]
  D=abs(det4(C));ck('nonzero joined or star cone',D>0)
  # This is the actual face-orbit separation used by the residue algorithm.
  raykeys=[self.canonical((v,))[0] for v in C if v[2] and v[3]]
  ck('nonprotected ray-orbit separation',len(set(raykeys))==len(raykeys))
  cid=self.seq;self.seq+=1;entries=[]
  for d in range(1,5):
   for inds in combinations(range(4),d):
    FF=tuple(C[i] for i in inds);Fc,nn=self.canonical(FF);key=(d,Fc);entry=(cid,inds,nn);self.faces[key].add(entry);entries.append((key,entry))
  row={'C':C,'D':D,'parent':parent,'entries':entries};self.cells[cid]=row;self.all_cells[cid]=row;self.index[C]=cid;heapq.heappush(self.heap,(-D,cid));return cid
 def remove(self,cid):
  row=self.cells.pop(cid);del self.index[row['C']]
  for key,entry in row['entries']:
   self.faces[key].remove(entry)
   if not self.faces[key]:del self.faces[key]
 def boundary(self):
  top=set();bottom=set();bdim=3 if self.mode=='zero' else 2
  for row in self.cells.values():
   C=row['C']
   for face in combinations(C,3):
    if all(v[2]==0 for v in face):top.add(self.canonical(face)[0])
   for face in combinations(C,bdim):
    if all(v[3]==0 for v in face):bottom.add(self.canonical(face)[0])
  return top,bottom
 def create(self):
  top_groups=defaultdict(list)
  if self.mode=='zero':
   H=self.H
   ns=[[(0,0),(1,0),(1,-1)],[(0,0),(0,-1),(1,-1)]]
   for ti,triangle in enumerate(ns):
    low=[(*n,1,0) for n in triangle]
    hi=[(H[0][0]*n[0]+H[0][1]*n[1],H[1][0]*n[0]+H[1][1]*n[1],0,1) for n in triangle]
    for C in [(low[0],low[1],low[2],hi[2]),(low[0],low[1],hi[1],hi[2]),(low[0],hi[0],hi[1],hi[2])]:self.raw.append({'rays':C,'group':ti})
   for row in common['cones']:
    par=common['parent_zero_instances'][row['zero_parent']];i,j=par['shift'];triangle=[]
    for x,y,h in row['rays']:
     x-=h*(7*i+2*j);y-=h*(i+2*j)
     triangle.append((y,x+3*y-6*h,0,h))
    top_groups[par['k']//12].append(tuple(triangle))
  else:
   for row in inf['cones']:
    C=tuple((x,y,s,r) for x,y,r,s in row['rays']);self.raw.append({'rays':C,'group':row.get('parent_index') if row['parent']=='upper' else None})
   for row in common['cones']:top_groups[row['infinity_parent']].append(tuple((x,y,0,h) for x,y,h in row['rays']))
  alltop=[C for lst in top_groups.values() for C in lst]
  ck(self.mode+' complete generic top count',len(alltop)==4264)
  edges={tuple(sorted(F)) for C in alltop for F in combinations(C,2)}
  for ri,raw in enumerate(self.raw):
   C=tuple(raw['rays']);top=tuple(v for v in C if v[2]==0);low=tuple(v for v in C if v[2]!=0)
   if len(top)==3:
    choices=top_groups[raw['group']]
    # Every listed common triangle lies in the actual raw upper face.
    tri=tuple((v[0],v[1],v[3]) for v in top)
    for Ftop in choices:ck(self.mode+' common top containment',all(min(coeff3(tri,(v[0],v[1],v[3])))>=0 for v in Ftop))
   elif len(top)==2:
    choices=[Ftop for Ftop in edges if all(on_top_segment(v,*top) for v in Ftop)]
    assert choices
   elif len(top)==1:choices=[top]
   else:raise AssertionError(('unexpected upper face',self.mode,C))
   for face in choices:
    joined=low+tuple(face);ck(self.mode+' full joined dimension',len(joined)==4 and det4(joined)!=0)
    self.initial.append({'rays':joined,'raw_parent':ri});self.add(joined,C)
  self.protected=self.boundary();self.initial_count=len(self.cells)
  ck(self.mode+' common boundary orbit count',len(self.protected[0])==4264)
  ck(self.mode+' retained lower boundary count',len(self.protected[1])==(2 if self.mode=='zero' else 1))
  print(json.dumps({'mode':self.mode,'stage':'joined','cones':len(self.cells),'max_det':max(x['D'] for x in self.cells.values())}),flush=True)
 def residue_point(self,C):
  A=tuple(zip(*C));signed=det4(C);D=abs(signed);sgn=1 if signed>0 else -1
  for j in range(4):
   nums=[]
   for i in range(4):
    minor=tuple(tuple(A[r][k] for k in range(4) if k!=i) for r in range(4) if r!=j)
    nums.append((sgn*(-1)**(i+j)*det3(minor))%D)
   if any(nums):
    vv=tuple(sum(C[i][r]*nums[i] for i in range(4)) for r in range(4));assert all(t%D==0 for t in vv);p=tuple(t//D for t in vv);g=reduce(gcd,map(abs,p));return tuple(t//g for t in p),nums,D*g
  raise AssertionError('no nonzero residue')
 def resolve(self):
  while self.heap:
   nd,cid=heapq.heappop(self.heap)
   if cid not in self.cells:continue
   if nd==-1:break
   row=self.cells[cid];C=row['C'];p,nums,den=self.residue_point(C);inds=tuple(i for i,t in enumerate(nums) if t);Fraw=tuple(C[i] for i in inds);Fc,n=self.canonical(Fraw);pc=self.T(p,(-n[0],-n[1]));key=(len(inds),Fc)
   ck('stellar centre misses BOTH protected boundaries',pc[2]>0 and pc[3]>0)
   coeff={self.T(C[i],(-n[0],-n[1])):nums[i] for i in inds};affected=list(self.faces[key]);ck('orbit star meets each cone at most once',len({x[0] for x in affected})==len(affected))
   replacement=[];trace=[]
   for aid,ais,an in affected:
    ar=self.cells[aid];AC=ar['C'];pp=self.T(pc,an)
    for ai in ais:
     new=list(AC);new[ai]=pp;num=coeff[self.T(AC[ai],(-an[0],-an[1]))];Dnew=abs(det4(tuple(new)))
     ck('exact strict stellar determinant decrease',0<Dnew<ar['D'] and Dnew*den==num*ar['D'])
     replacement.append((tuple(new),ar['parent']))
    trace.append({'old':AC,'parent':ar['parent'],'period':an,'determinant':ar['D']})
   for aid,_,_ in affected:self.remove(aid)
   newids=[self.add(CC,PP) for CC,PP in replacement]
   self.history.append({'ray':pc,'face':Fc,'numerators':[coeff[v] for v in Fc],'denominator':den,'affected':trace,'new_ids':newids})
  ck(self.mode+' all final cones regular',all(row['D']==1 for row in self.cells.values()))
  ck(self.mode+' both protected fans unchanged',self.boundary()==self.protected)
 def export(self):
  cones=[];facets=defaultdict(list);invariant_cache={}
  for ci,row in enumerate(sorted(self.cells.values(),key=lambda r:r['C'])):
   C=orient(row['C']);parent=row['parent'];D=abs(det4(parent));inverse=[coords4(C,e) for e in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]]
   inverse=list(map(list,zip(*inverse)));ck('integral child inverse',all(q.denominator==1 for rr in inverse for q in rr))
   relative=[coords4(parent,v) for v in C];ck('exact parent cone containment',all(q>=0 for rr in relative for q in rr))
   # The quotient monomial algebra consists of nonnegative a for which
   # a^t parent^-1 is integral.  Degree<=D suffices by the finite-group
   # partial-sum argument; retain every such generator, not only its order.
   if parent not in invariant_cache:
    Pinv=[coords4(parent,e) for e in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]]
    gens=[]
    for total in range(1,D+1):
     for a0 in range(total+1):
      for a1 in range(total-a0+1):
       for a2 in range(total-a0-a1+1):
        a=(a0,a1,a2,total-a0-a1-a2);m=tuple(sum(a[k]*Pinv[j][k] for k in range(4)) for j in range(4))
        if all(t.denominator==1 for t in m):gens.append({'cover_exponent':a,'torus_character':tuple(int(t) for t in m)})
    invariant_cache[parent]=gens
   maps=[]
   for gen in invariant_cache[parent]:
    exps=[sum(a*b for a,b in zip(gen['torus_character'],v)) for v in C];ck('original quotient-generator arrow nonnegative',min(exps)>=0);maps.append({'cover_exponent':gen['cover_exponent'],'child_exponents':exps})
   ww=coords4(C,self.delta);ck('physical weights integral',all(t.denominator==1 for t in ww))
   cones.append({'id':ci,'rays':C,'inverse_matrix':[[int(t) for t in rr] for rr in inverse],'physical_weights':[int(t) for t in ww],'original_canonical_orders':[v[2]+2*v[3]-1 for v in C],'source_parameter_orders':[v[3] for v in C],'raw_parent_rays':parent,'raw_parent_determinant':D,'parent_quotient_generators':maps})
   for inds in combinations(range(4),3):
    FF=tuple(C[i] for i in inds);Fc,n=self.canonical(FF);facets[Fc].append({'cone':ci,'local_columns':inds,'period_from_canonical':n})
  fd=[]
  for Fc,occ in facets.items():
   boundary='generic' if all(v[2]==0 for v in Fc) else 'selected' if all(v[3]==0 for v in Fc) else None
   ck('complete facet incidence',len(occ)==(1 if boundary else 2))
   entry={'canonical_rays':Fc,'boundary':boundary,'occurrences':occ,'gluings':[]}
   if len(occ)==2:
    aa,bb=occ;nn=tuple(bb['period_from_canonical'][i]-aa['period_from_canonical'][i] for i in (0,1));CA=cones[aa['cone']]['rays'];CB=cones[bb['cone']]['rays'];target_inverse=cones[bb['cone']]['inverse_matrix']
    sourceface=[CA[i] for i in aa['local_columns']];targetface=[CB[i] for i in bb['local_columns']];mapped=[self.T(v,nn) for v in sourceface];ck('literal period facet arrow',set(mapped)==set(targetface))
    # The full p=0 h,B map has c0^b in Vpt, c0=(p-1)^4*c_global.
    # At infinity K,J it has
    # f^(2a+b) in Vreg.  These are the actual remaining unit functions.
    unit=(0,nn[1],0,0) if self.mode=='zero' else (2*nn[0]+nn[1],0,0,0)
    exps=[sum(a*b for a,b in zip(rr,unit)) for rr in target_inverse]
    entry['gluings'].append({'from':aa['cone'],'to':bb['cone'],'period':nn,'vertex_permutation':[targetface.index(v) for v in mapped],'unit_name':'c0' if self.mode=='zero' else 'f','target_coordinate_unit_exponents':exps})
   fd.append(entry)
  return {'mode':self.mode,'coordinate_order':['Z','Vpt','ord_p','ord_P'] if self.mode=='zero' else ['Vreg','Z','ord_u','ord_R'],'period_matrices':{'lower':self.P,'upper':self.H},'physical_cocharacter':self.delta,'initial_joined_count':self.initial_count,'regular_cones':len(cones),'relative_stellar_steps':len(self.history),'protected_generic_cones':len(self.protected[0]),'protected_lower_cones':len(self.protected[1]),'original_volume_character':[0,0,1,2],'full_source_base_maps':({'s':'P*(p-1)/u_s','t':'P/u_P','q_old':'P*p*c_q','Q':'P^3*p'} if self.mode=='zero' else {'s':'R*(1-u)/u_s','t':'R*u/u_P','q_old':'R*c_q','Q':'R^3*u^2'}),'raw_parents':self.raw,'initial_joins':self.initial,'stellar_history':self.history,'cones':cones,'facets':fd,'seconds':round(time.monotonic()-self.start,2)}
outputs={}
for mode in ['zero','infinity']:
 fan=Fan(mode);fan.create();fan.resolve();outputs[mode]=fan.export();print(json.dumps({k:outputs[mode][k] for k in ['mode','initial_joined_count','regular_cones','relative_stellar_steps','protected_generic_cones','protected_lower_cones','seconds']}),flush=True)
outputs['zero']['full_unit_dictionary']={'c0':'(p-1)^4*c','c':'lambda0*c_q*K*u_s^(-4)','c0_common_divisor_unit_exponents':{'p_minus_1':4,'c':1},'B_Vpt':'P^2*p*c0*Vpt','forward_selected_closing_after_B_inverse_squared':'(Z,Vpt) -> (P^2*Z,P^(-2)*(c_q/c0)^2*Vpt)'}
outputs['infinity']['full_unit_dictionary']={'f':'(1-u)^4*c','c':'lambda0*c_q*K*u_s^(-4)','generic_substitution':'u=p^(-1), f=p^(-4)*(p-1)^4*c'}
out={'status':'PASS','checks':len(checks),'generic_json_sha256':hashlib.sha256((ROOT/'code/part3/e6_selected_i3_common_fan.json').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256((ROOT/'notes/part3_e6_selected_i3_working.md').read_bytes()).hexdigest(),'scope':'Actual relative periodic regular corner fans and all original quotient/period-unit morphisms. Full source/Cartier/reference-cap attachment and return remain open.','corners':outputs}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'counts':{k:v['regular_cones'] for k,v in outputs.items()}},indent=2))
