"""Link every compact/moving chart reference to the final original-lattice fan.

This checks provenance and exhaustiveness; the separate root programs
recompute the rational localization and moving-cap intersection values.
"""
from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json
from K111_fan4_exact import *
root=Path(__file__).resolve().parents[1];checks=0
def ck(p,s):
 global checks
 checks+=1
 if not p:raise AssertionError(s)
def read(fn):return json.loads((root/fn).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
common=read('K111_new_regular_common_fan.json')
compact=read('K111_T2_compact_ledger.json');moving=read('K111_new_moving_cap.json')
source_files={'zero':'K111_new_zero_endpoint_v2.json','one':'K111_new_one_endpoint.json','infinity':'K111_new_infinity_endpoint.json'}
fan={e:{c.get('id',i):c for i,c in enumerate(read(f)['cones'])} for e,f in source_files.items()}
delta={'zero':(-1,0,0,0),'one':(0,1,0,0),'infinity':(1,0,0,0)}
aux={'zero':(-1,1,0,0),'one':(-1,0,0,0),'infinity':(0,1,0,0)}
used={e:Counter() for e in fan}
owners=compact['physical_owners']
native_physical_owner={e:{} for e in fan}
def rays(c):return tuple(map(tuple,c['rays']))
def normal(c,d):return tuple(sorted(v for v,w in zip(rays(c),mv(c['inverse'],d)) if w))
for curve in compact['generic_curve_clutches']:
 n=common['cones'][curve['common_cone']]['rays'];expected=set(map(tuple,n))
 for e,a in curve['clutches'].items():
  c=fan[e][a['chart']];used[e][a['chart']]+=1
  upper=[v for v in rays(c) if v[3]==0];lower=[v for v in rays(c) if v[3]!=0]
  ck(len(upper)==3 and lower==[tuple(a['transverse_ray'])],'actual generic endpoint facet and transverse ray in final fan')
  ck(set(mv(a['character_matrix'],v) for v in upper)==expected,'full actual character map carries final endpoint cone to its named ordered common cone')
  pf=normal(c,delta[e]);mapped=tuple(sorted(mv(a['character_matrix'],v) for v in pf))
  ck(mapped in [tuple(map(tuple,f)) for f in owners[curve['physical_owner']]['faces']],'actual generic physical face belongs to the saved common owner')
  ck(pf not in native_physical_owner[e] or native_physical_owner[e][pf]==curve['physical_owner'],'same native generic physical face has the same common owner')
  native_physical_owner[e][pf]=curve['physical_owner']
for p in compact['compact_corner_second_fixed_pieces']+compact['excluded_second_fixed_pieces']:
 e=p['endpoint'];o=owners[p['physical_owner']];allowed={tuple(map(tuple,f)) for f in o['faces']}
 for cid in p['chart_ids']:
  ck(cid in fan[e],'every compact/excluded piece chart occurs in the final same fan')
  c=fan[e][cid];used[e][cid]+=1
  pf=normal(c,delta[e])
  if o['kind']=='compact generic':
   ck(native_physical_owner[e][pf]==p['physical_owner'],'generic-owner corner piece uses its actual native-to-common physical face map')
  else:ck(pf in allowed,'every compact/excluded chart has its actual final-fan physical owner')
 first=fan[e][p['chart_ids'][0]];face=tuple(map(tuple,p['normal_face']))
 ck(set(face)<=set(rays(first)),'saved second-fixed normal face occurs in its first final-fan chart')
 if 'degrees' not in p:continue
 if p['degrees'] is None:
  ck(list(mv(first['inverse'],delta[e]))==p['physical_weights'],'point physical weights from exact final-fan ordered inverse')
  ck(list(mv(first['inverse'],aux[e]))==p['second_weights'],'point second weights from exact final-fan ordered inverse')
 else:
  tang=[v for v in rays(first) if v not in face];ck(len(tang)==1,'corner curve actual tangent complement')
  C=(*face,tang[0]);den=det(C);J=tuple(tuple(v//den for v in row) for row in adj(C))
  ck(abs(den)==1,'actual corner curve reordered lattice is unimodular')
  ck(list(mv(J,delta[e])[:3])==p['physical_weights'],'curve physical normal weights from exact final-fan columns')
  ck(list(mv(J,aux[e])[:3])==p['second_weights'],'curve second normal weights from exact final-fan columns')
for e in fan:
 ck(set(used[e])==set(fan[e]),'every final endpoint chart occurs in the complete compact/generic/excluded ledger')
 ck(set(used[e].values())=={1},'every final endpoint chart occurs exactly once in that ledger')
moving_ids=set()
for c in moving['charts']:
 original=fan['zero'][c['owner']];moving_ids.add(c['owner'])
 ck(c['original_rays']==original['rays'],'moving chart uses the exact ordered final zero cone')
 ck(c['physical_weights']==original['physical_weights'],'moving physical weights are the final same-fan weights')
 T=((1,0,8,1),(0,1,6,1),(0,0,1,0),(0,0,0,1))
 aligned=[list(mv(T,v)) for v in c['original_rays']] if c['face']=='native zero after T0' else c['original_rays']
 ck(aligned==c['aligned_rays'],'moving normal alignment is the actual whole T0 source-period matrix')
expected={cid for p in compact['excluded_second_fixed_pieces'] if p['endpoint']=='zero' for cid in p['chart_ids']}
ck(moving_ids==expected,'entire actual zero moving owner is exactly the separately capped owner excluded from compact localization')
refs={}
for fn in [*source_files.values(),'K111_new_regular_common_fan.json','K111_T2_compact_ledger.json','K111_new_moving_cap.json','K111_actual_boundary_comparison.json','K111_point_graph_lift_scope.json','K111_new_auxiliary_edge_chain_replay.json']:
 refs[fn]=dict(bytes=(root/fn).stat().st_size,sha256=sha(root/fn))
for name in ['K111_compact_owner_independent.json','K111_moving_cap_independent.json']:
 p=root.parent/'code'/'outputs'/name;d=json.loads(p.read_text());inputfn='K111_T2_compact_ledger.json' if 'compact' in name else 'K111_new_moving_cap.json'
 ck(d['input_sha256']==refs[inputfn]['sha256'],'parent independent receipt uses exactly the unchanged linked output')
 if 'ordered_common_fan_sha256' in d:ck(d['ordered_common_fan_sha256']==refs['K111_new_regular_common_fan.json']['sha256'],'parent ordered common fan is exactly current common fan')
 refs['../code/outputs/'+name]=dict(bytes=p.stat().st_size,sha256=sha(p),checks=d['checks'])
out=dict(status='PASS',checks=checks,scope='Every final endpoint chart occurs exactly once in the saved generic/compact/excluded ledger. All physical owners, every corner weight, every generic mapped facet, and every native moving cone/whole T0 alignment are linked to the unchanged final source files. Parent independent output hashes match these exact compact and moving certificates.',endpoint_chart_counts={e:len(f) for e,f in fan.items()},moving_charts=len(moving_ids),files=refs)
(root/'K111_same_atlas_link.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
