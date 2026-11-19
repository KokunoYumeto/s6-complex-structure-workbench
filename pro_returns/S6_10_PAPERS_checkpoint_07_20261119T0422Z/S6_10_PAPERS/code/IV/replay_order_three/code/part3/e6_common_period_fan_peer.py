"""Independent exact geometry and monomial audit of root's common fan."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import json,hashlib,time
base=Path(__file__).resolve().parents[2]
src=base/'code/part3_root/e6_common_period_fan.json'
raw=src.read_bytes();d=json.loads(raw)
checks=[]
def yes(n,b):
 assert b,n;checks.append(n)
def det(N):
 return sum(N[0][i]*(N[1][(i+1)%3]*N[2][(i+2)%3]-N[1][(i+2)%3]*N[2][(i+1)%3]) for i in range(3))
def cols(vs):return [[vs[j][i] for j in range(3)] for i in range(3)]
def mv(N,v):return [sum(a*b for a,b in zip(r,v)) for r in N]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def decode(q):return F(*q) if isinstance(q,list) else F(q)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def area(q):return sum(cross(q[i],q[(i+1)%len(q)]) for i in range(len(q)))/2
def sub(a,b):return (a[0]-b[0],a[1]-b[1])
def clip(poly,tri):
 for i in range(3):
  a,b=tri[i],tri[(i+1)%3];out=[];v=sub(b,a)
  if not poly:break
  for j in range(len(poly)):
   p,q=poly[j],poly[(j+1)%len(poly)]
   sp=cross(v,sub(p,a));sq=cross(v,sub(q,a))
   if sp>=0:out.append(p)
   if (sp>=0)!=(sq>=0):
    lam=sp/(sp-sq);out.append((p[0]+lam*(q[0]-p[0]),p[1]+lam*(q[1]-p[1])))
  poly=out
 return poly
polys=[];source_ok=True;infinity_unit_missing=False
for index,c in enumerate(d['cones']):
 N=cols(c['rays']);yes('regular cone '+str(index),det(N)==1)
 yes('physical cocharacter '+str(index),mv(N,c['physical_weights'])==[1,0,0])
 yes('canonical original orders '+str(index),c['original_canonical_orders']==[2*v[2]-1 for v in c['rays']])
 for kind,key,mkey,ukey in [('zero','parent_zero_instances','zero_monomial_matrix','zero_unit_exponents'),
                            ('one','parent_one_instances','one_monomial_matrix','one_unit_exponents')]:
  par=d[key][c[kind+'_parent']];Np=cols(par['rays']);E=c[mkey]
  yes(kind+' actual monomial square '+str(index),mm(Np,E)==N and all(x>=0 and isinstance(x,int) for row in E for x in row))
  for u,vec in par['common_character_units'].items():
   yes(kind+' full '+u+' unit square '+str(index),[x+y for x,y in zip(mv(Np,c[ukey][u]),vec)]==[0,0,0])
 pi=d['parent_infinity_triangles'][c['infinity_parent']]
 Pi=cols([(int(decode(v[0])),int(decode(v[1])),1) for v in pi])
 yes('infinity monomial square '+str(index),mm(Pi,c['infinity_monomial_matrix'])==N)
 if 'infinity_unit_exponents' in c:
  yes('actual R=pP unit square '+str(index),mv(Pi,c['infinity_unit_exponents']['p'])==[0,0,1])
 else:infinity_unit_missing=True
 yes('actual source node characters '+str(index),all(v[1]+3*v[2]>=0 and -v[1]>=0 for v in c['rays']))
 if 'source_Z1' in c:
  yes('full stored source Z1 '+str(index),c['source_Z1']=={'p_power':1,'exponents':[v[1]+3*v[2] for v in c['rays']]})
  yes('full stored source W1 '+str(index),c['source_W1']=={'p_power':0,'exponents':[-v[1] for v in c['rays']]})
 p=[(F(v[0],v[2]),F(v[1],v[2])) for v in c['rays']]
 yes('positive triangle '+str(index),area(p)>0)
 yes('inside exact fundamental hexagon '+str(index),
     all(-5<=x<=0 and -2<=y<=0 and -4<=x-y<=1 for x,y in p))
 polys.append(p)
yes('complete exact area',sum(area(p) for p in polys)==9)
boxes=[(min(x for x,y in p),max(x for x,y in p),min(y for x,y in p),max(y for x,y in p)) for p in polys]
tested=0
for i,j in combinations(range(len(polys)),2):
 a,b=boxes[i],boxes[j]
 if not(a[0]<b[1] and b[0]<a[1] and a[2]<b[3] and b[2]<a[3]):continue
 p=clip(polys[i],polys[j]);tested+=1
 assert len(p)<3 or area(p)==0,('overlapping interiors',i,j,p)
checks.append('all potentially overlapping triangle interiors are disjoint')
incidence={}
for c in d['cones']:
 for edge in combinations(c['rays'],2):
  key=tuple(sorted(tuple(v) for v in edge));incidence[key]=incidence.get(key,0)+1
yes('all edge incidences are one or two',all(v in (1,2) for v in incidence.values()))
edge_counts={'interior':sum(v==2 for v in incidence.values()),'boundary':sum(v==1 for v in incidence.values())}
yes('complete stored edge incidence',edge_counts==d['edge_incidence_counts'])
def faces(row):
 ans=set()
 for c in d['cones']:
  for a,b in combinations(c['rays'],2):
   if sum(x*y for x,y in zip(row,a))==0 and sum(x*y for x,y in zip(row,b))==0:ans.add(tuple(sorted((tuple(a),tuple(b)))))
 return ans
for name,target,source,shift in [('K',(1,0,0),(1,0,5),(5,1)),('J',(0,1,0),(0,1,2),(1,2)),('KJinv',(1,-1,-1),(1,-1,4),(4,-1))]:
 transformed={tuple(sorted((v[0]+shift[0]*v[2],v[1]+shift[1]*v[2],v[2]) for v in F0)) for F0 in faces(source)}
 yes('complete periodic face '+name,transformed==faces(target))
out={'status':'GEOMETRY_PASS_UNIT_TYPING_OPEN' if infinity_unit_missing else 'PASS',
 'input':str(src.relative_to(base)),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'count':len(checks),'checks':checks,'regular_cones':len(polys),
 'exact_intersection_pairs_checked':tested,'normalized_area':9,
 'remaining_unit_typing':('Actual infinity charts use R=pP; add the corresponding parent p unit row.' if infinity_unit_missing else None),
 'scope':'Generic three-fan overlap only: complete exact coverage, all parent monomial maps, period faces, physical weights and original canonical orders. No corner-source graph, finite-isotropy contribution or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))
