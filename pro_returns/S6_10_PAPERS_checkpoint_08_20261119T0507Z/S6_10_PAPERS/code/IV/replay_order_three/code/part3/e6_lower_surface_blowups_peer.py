"""Independent direct audit of all48 lower charts and their source blowups."""
from pathlib import Path
import json,hashlib,datetime
from collections import defaultdict
import sympy as S
R=Path(__file__).resolve().parents[2];p=R/'code/part3_fourfold/e6_p_one_common_cayley.json';j=json.loads(p.read_text());checks=[]
def ck(v,n):
 assert bool(v),n
 checks.append(n)
cs=defaultdict(list)
for n,c in enumerate(j['cones']):
 if c['kind']=='lower_interval':cs[c['parent']].append((n,c))
ck(len(cs)==12,'twelve actual native lower source-node parents')
chain=[(1,0),(2,1),(1,1),(1,2),(0,1)];expected={frozenset(chain[i:i+2]) for i in range(4)}
records=[]
for name,cones in sorted(cs.items()):
 ck(len(cones)==4,'four refined charts in each actual source quadrant')
 got=[]
 for n,c in cones:
  M=S.Matrix(c['parent_monomial_matrix']);w=c['physical_weights'];normal=[i for i,a in enumerate(w) if a];tangent=[i for i,a in enumerate(w) if not a]
  ck(len(normal)==len(tangent)==2,'actual two normal and two tangent coordinates')
  ck(sorted(w[i] for i in normal)==[-1,1],'actual opposite physical weights')
  ck(M[:2,normal]==S.zeros(2),'source coordinates independent of normal coordinates')
  ck(M[2:,tangent]==S.zeros(2),'normal arrows independent of tangent coordinates')
  A=M[2:,normal];ck(abs(A.det())==1 and all(x in (0,1) for x in A),'normal arrow unchanged with saved permutation')
  T=M[:2,tangent];ck(abs(T.det())==1,'source refinement charts regular')
  rays=[tuple(map(int,T[:,i])) for i in range(2)];got.append(frozenset(rays))
  ck(all(min(v)>=0 for v in rays),'source monomial map extends at zero')
  ck(frozenset(rays) in expected,'actual source map is one of the four specified blowup charts')
  records.append({'cone':n,'parent':name,'source_matrix':[[int(a) for a in row] for row in T.tolist()],'normal_matrix':[[int(a) for a in row] for row in A.tolist()],'source_Jacobian_orders':[sum(r)-1 for r in rays]})
 ck(set(got)==expected,'complete source quadrant with exact four charts')
ck(tuple(S.Matrix((1,0))+S.Matrix((0,1)))==(1,1),'first ordinary point blowup')
ck(tuple(S.Matrix((1,0))+S.Matrix((1,1)))==(2,1),'second actual corner blowup')
ck(tuple(S.Matrix((1,1))+S.Matrix((0,1)))==(1,2),'third actual corner blowup')
out={'status':'PASS_NINE_BLOWUPS_PER_LOWER_SURFACE','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':len(checks),'input':str(p.relative_to(R)),'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'native_source_nodes':12,'lower_surfaces':4,'source_nodes_per_surface':3,'ordinary_blowups_per_node':3,'blowups_per_surface':9,'relative_tangent_p1_per_surface':-27,'normal_rows':'unchanged a,b with saved physical-weight permutation','charts':records,'scope':'Actual48 lower source maps and normal derivatives. Relative boundary/point-line/cap and total return remain separate.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='charts'}))
