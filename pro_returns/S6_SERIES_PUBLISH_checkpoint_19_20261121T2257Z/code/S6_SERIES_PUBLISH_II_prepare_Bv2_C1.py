"""Bind reviewed, exact, owner-scoped B-v2 and C-first-four changes."""
from pathlib import Path
import datetime, hashlib, json
R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
before=(R/'S6_SERIES_PUBLISH_II.tex').read_text(); s=before
patches=[]; bindings=[]
bp=R/'agents/ii_checks_provenance/group01/v2_addendum/S6_SERIES_PUBLISH_II_B_group01_scope_methods_addendum.json'
cp=R/'agents/ii_infra/S6_SERIES_PUBLISH_II_first_four_guards_reviewed.json'
assert sha(bp.read_bytes())=='8e6d93fa51227ef509af40999b1358b336bcd2ba21542e3021a432d833610830'
assert sha(cp.read_bytes())=='76dda91242629bdd731bce22c91ed39dbf124cb0909b31af50678cf1ee528ace'
b=json.loads(bp.read_text()); c=json.loads(cp.read_text())
groups=[]
for p in b['incremental_pairs']:
 groups.append(({'01BN':'cdp:st:C.1.1','01AK':'cdp:st:A.2.6'}[p['tag']],p['incremental_before'],p['incremental_after'],p['guards']))
for p in c['blocks']:
 guards=[dict(old=g['before'],new=g['after'],defect_type=g['type'],reason=g['reason'],change_id=g['id']) for g in c['guards'] if g['tag']==p['tag']]
 groups.append((p['statement_id'],dict(path=p['original_full_block'],sha256=p['original_full_block_sha256']),dict(path=p['proposed_full_block'],sha256=p['proposed_full_block_sha256']),guards))
for owner,orig,prop,guards in groups:
 oldblock=(R/orig['path']).read_text(); newblock=(R/prop['path']).read_text()
 assert sha(oldblock)==orig['sha256'] and sha(newblock)==prop['sha256']
 assert s.count(oldblock)==1, owner
 currentblock=oldblock
 for g in guards:
  assert currentblock.count(g['old'])==1
  a0=s.index(currentblock); pos=a0+currentblock.index(g['old']); z0=a0+len(currentblock)
  a,z=pos,pos+len(g['old'])
  while s.count(s[a:z])!=1:
   a=max(a0,a-100);z=min(z0,z+100)
  old=s[a:z];new=s[a:pos]+g['new']+s[pos+len(g['old']):z]
  patches.append(dict(old=old,new=new,type=g['defect_type'],statement_id=owner,reason=g['reason'],originating_change_id=g['change_id'],changed_old_literal=g['old'],changed_new_literal=g['new']))
  s=s[:a]+new+s[z:];currentblock=currentblock.replace(g['old'],g['new'])
 assert currentblock==newblock and s.count(newblock)==1
 bindings.append(dict(owner=owner,before=orig,after=prop,exact_guard_sequence_verified=True))
out=R/'records/S6_SERIES_PUBLISH_II_Bv2_C1_editorial_guard.json';assert not out.exists()
out.write_text(json.dumps(dict(paper='II',source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,bindings=bindings,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),proposals=[dict(path=str(p.relative_to(R)),sha256=sha(p.read_bytes())) for p in [bp,cp]],events_added=0,visual_reading_credit=0),indent=2)+'\n')
print(json.dumps(dict(path=str(out.relative_to(R)),sha256=sha(out.read_bytes()),patches=len(patches),owners=len(bindings),source_after_sha256=sha(s))))
