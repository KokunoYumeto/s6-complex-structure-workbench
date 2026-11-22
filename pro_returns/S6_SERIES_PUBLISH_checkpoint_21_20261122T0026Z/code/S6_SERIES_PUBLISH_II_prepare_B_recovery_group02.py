"""Bind the reconstructed B-group02 proposals to the exact recovered source."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
P=R/'agents/ii_checks_provenance/recovery_20261121T2000Z/group02/S6_SERIES_PUBLISH_II_B_group02_recovery_proposals.json'
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
assert sha(P.read_bytes())=='e507abfdb4e6a068e3ce4220e413ec7e24e974e2775982b4e39a55a6bf0fb214'
p=json.loads(P.read_text());before=(R/'S6_SERIES_PUBLISH_II.tex').read_text();s=before
patches=[];bindings=[]
for target in p['targets']:
 owner=target['statement_owner'];orig=target['original_full_block'];prop=target['proposed_full_block']
 oldblock=(R/orig['path']).read_text();newblock=(R/prop['path']).read_text()
 assert sha(oldblock)==orig['sha256'] and sha(newblock)==prop['sha256']
 assert s.count(oldblock)==1
 trial=oldblock
 for c in target['guards']:
  assert trial.count(c['old'])==1
  trial=trial.replace(c['old'],c['new'])
 assert trial==newblock
 currentblock=oldblock
 for c in target['guards']:
  blockstart=s.index(currentblock);pos=blockstart+currentblock.index(c['old'])
  a,z=pos,pos+len(c['old']);blockend=blockstart+len(currentblock)
  while s.count(s[a:z])!=1:
   a=max(blockstart,a-100);z=min(blockend,z+100)
   assert a<pos or z>pos+len(c['old'])
  old=s[a:z];new=s[a:pos]+c['new']+s[pos+len(c['old']):z]
  patches.append(dict(old=old,new=new,type=c['defect_type'].replace(',','/'),statement_id=owner,
       reason=c['reason']+' Complete original/proposed blocks were actually read by the proposing checker; root has read all literal guards, full mathematical comparison paragraphs, the methods addendum and complete new certificate code/output. Mathematical check completion is separately recorded.',
       originating_change_id=c['change_id'],changed_old_literal=c['old'],changed_new_literal=c['new']))
  s=s[:a]+new+s[z:]
  currentblock=currentblock.replace(c['old'],c['new'])
 assert currentblock==newblock and s.count(newblock)==1
 bindings.append(dict(owner=owner,before=orig,after=prop,root_proposed_block_actually_read=False, root_literal_guards_and_full_comparison_read=True,
    exact_guard_sequence_reproduces_proposed_block=True,source_exposure='Editorial integration after target proof access; no independent proof is claimed by root.'))
c=p['bibliography_guard']
assert s.count(c['old'])==1
patches.append(dict(old=c['old'],new=c['new'],type=c['defect_type'],statement_id='bibliography:Hassett2009Rational',reason=c['reason'],originating_change_id=c['change_id']))
s=s.replace(c['old'],c['new'],1)
g=dict(paper='II',source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,
 created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),proposal={'path':str(P.relative_to(R)),'sha256':sha(P.read_bytes())},
 bindings=bindings,mathematical_events_added=0,visual_reading_credit=0)
out=R/'records/S6_SERIES_PUBLISH_II_B_recovery_group02_editorial_guard.json';assert not out.exists()
out.write_text(json.dumps(g,indent=2)+'\n')
print(json.dumps(dict(path=str(out.relative_to(R)),sha256=sha(out.read_bytes()),patches=len(patches),owners=len(bindings),source_after_sha256=sha(s)),indent=2))
