"""Integrate the exact reviewed A-group edits after the E4 citation transport."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
P=R/'agents/ii_checks_A/editorial/group01/S6_SERIES_PUBLISH_II_A_group01_editorial_proposals.json'
T=R/'agents/ii_checks_A/editorial/group01/S6_SERIES_PUBLISH_II_A_group01_E4_transported_pairs.json'
p=json.loads(P.read_text());trans={x['tag']:x for x in json.loads(T.read_text())}
before=(R/'S6_SERIES_PUBLISH_II.tex').read_text();s=before;patches=[];bindings=[]
for x in p['proposals']:
 owner=x['statement_owner'];tag=x['tag']
 oldp=x['original_block_path'];oldh=x['original_block_sha256']
 newp=x['proposed_block_path'];newh=x['proposed_block_sha256']
 if tag in trans:
  t=trans[tag];oldp=t['original_path'];oldh=t['original_sha256'];newp=t['proposed_path'];newh=t['proposed_sha256']
 oldblock=(R/oldp).read_text();newblock=(R/newp).read_text()
 assert sha(oldblock)==oldh and sha(newblock)==newh
 assert s.count(oldblock)==1,tag
 currentblock=oldblock
 for k,g in enumerate(x['literal_edits'],1):
  assert currentblock.count(g['old'])==g['occurrences']==1,(tag,k)
  blockstart=s.index(currentblock);pos=blockstart+currentblock.index(g['old']);blockend=blockstart+len(currentblock)
  a,z=pos,pos+len(g['old'])
  while s.count(s[a:z])!=1:
   a=max(blockstart,a-100);z=min(blockend,z+100)
  old=s[a:z];new=s[a:pos]+g['new']+s[pos+len(g['old']):z]
  patches.append(dict(old=old,new=new,type='/'.join(g['defect_types']),statement_id=owner,reason=g['mathematical_reference_identity'],originating_change_id=f'II-A-group01-{tag}-{k:02}',changed_old_literal=g['old'],changed_new_literal=g['new']))
  s=s[:a]+new+s[z:];currentblock=currentblock.replace(g['old'],g['new'])
 assert currentblock==newblock and s.count(newblock)==1,tag
 bindings.append(dict(tag=tag,owner=owner,before=dict(path=oldp,sha256=oldh),after=dict(path=newp,sha256=newh),exact_guard_sequence_verified=True,root_review_scope='All literal guards and complete comparison sections reviewed. Complete paired proof reading is the checker record, with four E4-transported pairs separately reread. No additional root reading or independence event claimed.'))
out=R/'records/S6_SERIES_PUBLISH_II_A_group01_editorial_guard.json';assert not out.exists()
out.write_text(json.dumps(dict(paper='II',source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,bindings=bindings,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),evidence=[dict(path=str(q.relative_to(R)),sha256=sha(q.read_bytes())) for q in [P,T,R/'agents/ii_checks_A/S6_SERIES_PUBLISH_II_A_group01_actual_rereading_records.json',R/'agents/ii_checks_A/S6_SERIES_PUBLISH_II_A_group01_E4_actual_rereads.json',R/'agents/ii_checks_A/comparisons/S6_SERIES_PUBLISH_II_A_group01_comparisons.md']],events_added=0,visual_reading_credit=0),indent=2)+'\n')
print(json.dumps(dict(path=str(out.relative_to(R)),sha256=sha(out.read_bytes()),patches=len(patches),owners=len(bindings),source_after_sha256=sha(s))))
