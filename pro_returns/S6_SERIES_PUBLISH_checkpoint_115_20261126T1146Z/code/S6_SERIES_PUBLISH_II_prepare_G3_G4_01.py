"""Bind the two complete manual-target proof pairs and their citation edits."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
p='agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_G3_G4_guards_v2.json'
c='agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_G3_G4_comparison.json'
assert sha((R/p).read_bytes())=='3048003d35d0247af05293c8788836183132379252f14de609185047a06785ab'
assert sha((R/c).read_bytes())=='0ea2ac88ddda3844cf5edb28db0eeee099da7a29b2a624499356662a5416c836'
g=json.loads((R/p).read_text());comp=json.loads((R/c).read_text())
before=(R/'S6_SERIES_PUBLISH_II.tex').read_text();s=before;patches=[]
for b in g['blocks']:
 assert sha((R/b['before_path']).read_bytes())==b['before_sha256']
 assert sha((R/b['after_path']).read_bytes())==b['after_sha256']
 assert s.count((R/b['before_path']).read_text())==1
for t in comp['checks']:
 assert t['complete_original_actually_read'] and t['complete_proposed_actually_read']
 assert not t['unresolved_mathematical_findings']
for x in g['guards']:
 assert s.count(x['before'])==1,(x['id'],s.count(x['before']))
 patches.append(dict(old=x['before'],new=x['after'],type=x['type'],statement_id=x['statement_id'],
  reason=x['reason']+' The checker and root actually read the complete original mixed argument and proposed statement/proof pairs; root also read all fresh programs and outputs and the complete comparison narrative. The exact program-row and bibliography changes were reviewed.',originating_change_id=x['id']))
 s=s.replace(x['before'],x['after'],1)
for b in g['blocks']:assert s.count((R/b['after_path']).read_text())==1
out=R/'records/S6_SERIES_PUBLISH_II_G3_G4_editorial_guard_01.json';assert not out.exists()
record=dict(paper='II',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,
 original_proposal={'path':p,'sha256':sha((R/p).read_bytes())},comparison={'path':c,'sha256':sha((R/c).read_bytes())},blocks=g['blocks'],
 root_complete_original_and_proposed_math_blocks_read=True,mathematical_events_added=0,visual_reading_credit=0)
out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(dict(guard=str(out.relative_to(R)),sha256=sha(out.read_bytes()),patches=len(patches),source_after_sha256=sha(s)),indent=2))
