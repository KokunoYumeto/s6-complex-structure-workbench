"""Bind the six reviewed source pairs to forty-seven exact guarded edits."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
p='agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group02/S6_SERIES_PUBLISH_II_clean_group02_final_proposals.json'
assert sha((R/p).read_bytes())=='016785e949ae4cd67469a3c985591b3d9d28cd9f4fefc682a8fe7c9fbf32eb96'
data=json.loads((R/p).read_text());before=(R/'S6_SERIES_PUBLISH_II.tex').read_text();s=before
patches=[];bindings=[]
for t in data['targets']:
 assert t['actual_complete_original_proof_read'] and t['actual_complete_proposed_proof_read']
 old=t['original_full_block'];new=t['proposed_full_block']
 assert sha((R/old['path']).read_bytes())==old['sha256'] and sha((R/new['path']).read_bytes())==new['sha256']
 cur=(R/old['path']).read_text();expected=(R/new['path']).read_text();assert s.count(cur)==1
 for g in t['guards']:
  assert cur.count(g['old'])==1,(t['tag'],g['change_id'])
  start=s.index(cur);pos=start+cur.index(g['old']);a,z=pos,pos+len(g['old']);end=start+len(cur)
  while s.count(s[a:z])!=1:
   prev=(a,z);a,z=max(start,a-100),min(end,z+100);assert (a,z)!=prev
  o=s[a:z];n=s[a:pos]+g['new']+s[pos+len(g['old']):z]
  patches.append(dict(old=o,new=n,type=g['defect_type'].replace(',','/'),statement_id=t['statement_owner'],
   reason=g['reason']+' The checker actually reread both complete blocks. Root read every literal guard, each complete proposed block, all comparison scopes, and all fresh program sources and outputs.',
   originating_change_id=g['change_id'],changed_old_literal=g['old'],changed_new_literal=g['new']))
  s=s[:a]+n+s[z:];cur=cur.replace(g['old'],g['new'],1)
 assert cur==expected and s.count(expected)==1
 bindings.append(dict(owner=t['statement_owner'],tag=t['tag'],original=old,proposed=new,
   actual_complete_pair_read_by_checker=True,root_complete_proposed_read=True,
   root_all_literal_guards_and_comparison_scopes_read=True,comparison=t['comparison']))
assert len(patches)==47
out=R/'records/S6_SERIES_PUBLISH_II_B_clean_02_editorial_guard.json';assert not out.exists()
g=dict(paper='II',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_before_sha256=sha(before),source_after_sha256=sha(s),
 patches=patches,bindings=bindings,evidence={'path':p,'sha256':sha((R/p).read_bytes())},
 proof_repairs=['WK: specify the Nth power as the unipotent operator.','WK: use the evaluation pairing to identify the induced H1-dual operator A^T on H^1 and prove det(I-(A^m)^T)=det(I-A^m).'],
 mathematical_events_added=0,visual_reading_credit=0)
out.write_text(json.dumps(g,indent=2)+'\n')
print(json.dumps(dict(guard=str(out.relative_to(R)),sha256=sha(out.read_bytes()),patches=len(patches),source_after_sha256=sha(s)),indent=2))
