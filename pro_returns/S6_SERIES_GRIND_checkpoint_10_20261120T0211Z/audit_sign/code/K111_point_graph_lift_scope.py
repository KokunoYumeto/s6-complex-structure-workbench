"""Exact receiving check: which unchanged cones map to the marked source graph.

The output preserves failures of the full interior graph-lift claim. It
also checks the complete localized exterior and all twelve actual IL
stars, where graph and resolved-node maps are used in the filling proof.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from K111_fan4_exact import *

root=Path(__file__).resolve().parents[1]
checks=0
def ck(p,s):
 global checks
 checks+=1
 if not p:raise AssertionError(s)
def classify(x,p):
 # The original graph's a chart, then the two resolved c charts.
 if all(a>=2*b for a,b in zip(x,p)):return 'a'
 if all(a<=b for a,b in zip(x,p)):return 'c_first'
 if all(b<=a<=2*b for a,b in zip(x,p)):return 'c_second'
 return None
def arrows(chart,x,p,R,y):
 if chart=='a':
  a=[i-2*j for i,j in zip(x,p)]
  ck(all(v>=0 for v in a),'actual graph a=x/P^2 has nonnegative orders')
  ck([i+j for i,j in zip(a,y)]==R,'whole a*y=R identity')
  return {'a':'x/P^2','original':'x=P^2*a; a*y=R','orders':{'a':a}}
 if chart=='c_first':u=x;w=[a-b for a,b in zip(p,x)]
 else:u=[a-b for a,b in zip(x,p)];w=[2*a-b for a,b in zip(p,x)]
 ck(all(a>=0 for a in u+w),'both original resolved graph coordinates are holomorphic')
 ck([a+b for a,b in zip(u,w)]==p,'original P=u*w')
 xx=u if chart=='c_first' else [2*a+b for a,b in zip(u,w)]
 cc=[a+2*b for a,b in zip(u,w)] if chart=='c_first' else w
 ck(xx==x,'original resolved x row')
 ck([a+b for a,b in zip(xx,cc)]==[2*a for a in p],'original x*c=P^2 row')
 ck([a+b for a,b in zip(R,cc)]==y,'original y=R*c row')
 return {'u':'x' if chart=='c_first' else 'x/P','w':'P/x' if chart=='c_first' else 'P^2/x','original':'P=u*w; x=u; c=u*w^2; y=R*u*w^2' if chart=='c_first' else 'P=u*w; x=u^2*w; c=w; y=R*w','orders':{'u':u,'w':w}}

owners=json.loads((root/'K111_T2_compact_ledger.json').read_text())['physical_owners']
output=[]
for end,fn in [('zero','K111_new_zero_endpoint_v2.json'),('one','K111_new_one_endpoint.json'),('infinity','K111_new_infinity_endpoint.json')]:
 path=root/fn; data=json.loads(path.read_text())
 fs={k:[set(map(tuple,f)) for f in o['faces']] for k,o in owners.items() if k.startswith(end+':') and 'lower' in k}
 owner_records={k:[] for k in fs};full_cross=[];resolved_cross=[];localized=[]
 for i,c in enumerate(data['cones']):
  rays=list(map(tuple,c['rays']));rr=[v[2] for v in rays];zz=[v[3] for v in rays]
  p=[a+(b if end=='infinity' else 0) for a,b in zip(rr,zz)]
  R=rr if end=='infinity' else [a+(b if end=='zero' else 0) for a,b in zip(rr,zz)]
  x,y=c['source_rows'];dif=[a-2*b for a,b in zip(x,p)]
  graph_cross=min(dif)<0<max(dif)
  if graph_cross:full_cross.append(i)
  route=classify(x,p)
  if route is None:resolved_cross.append(i)
  for owner,faces in fs.items():
   if any(f<=set(rays) for f in faces):
    rec=dict(chart=i,rays=rays,graph_cross=graph_cross,resolved_route=route,source_rows=[x,y],P_row=p,R_row=R)
    if end=='one':
     ck(route is not None,'all actual lower source charts already map to the original resolved marked graph')
     rec['morphism']=arrows(route,x,p,R,y)
    owner_records[owner].append(rec)
  # This is the entire subfan remaining after inverting the displayed
  # original base, with units retained by identity-character maps.
  keep=[j for j,v in enumerate(rays) if v[2]==0]
  if keep:
   xx=[x[j] for j in keep];yy=[y[j] for j in keep];pp=[p[j] for j in keep];RR=[R[j] for j in keep]
   route0=classify(xx,pp)
   ck(route0 is not None,'every localized exterior face maps to the original resolved source graph')
   morph=arrows(route0,xx,pp,RR,yy)
   localized.append(dict(parent=i,face=[rays[j] for j in keep],route=route0,morphism=morph))
 if end=='one':
  ck(len(owner_records)==12,'all twelve named lower owners included')
  ck(all(len(a)==3 for a in owner_records.values()),'each actual lower owner has all three minimal source charts')
 output.append(dict(endpoint=end,input=fn,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),full_graph_crossing_count=len(full_cross),full_graph_crossing_charts=full_cross,full_resolved_graph_crossing_count=len(resolved_cross),full_resolved_graph_crossing_charts=resolved_cross,localized_exterior=localized,noncompact_owners=owner_records))
out=dict(scope='The current endpoint atlases do not all lift to the proper point graph. This receipt preserves every crossing. The entire pure-lower localized exterior and all twelve complete one-end lower stars do lift through the displayed original graph/resolved-node morphisms. The zero moving cap uses its actual NS.23 outer normal derivative and interior divisor bundle, and does not assert an ambient interior source-graph lift.',checks=checks,endpoints=output)
(root/'K111_point_graph_lift_scope.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':checks,'counts':[{k:e[k] for k in ['endpoint','full_graph_crossing_count','full_resolved_graph_crossing_count']} for e in output]},indent=2))
