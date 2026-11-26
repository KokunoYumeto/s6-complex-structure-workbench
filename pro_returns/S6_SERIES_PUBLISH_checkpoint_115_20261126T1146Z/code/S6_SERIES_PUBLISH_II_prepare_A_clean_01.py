"""Bind fourteen reviewed literal guards and one end-table program citation."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
base='agents/ii_checks_A/recovery_20261121T195642Z/'
index_path=base+'S6_SERIES_PUBLISH_II_A_recovery_clean_group01_final_index.json'
assert sha((R/index_path).read_bytes())=='6b05cf460cac28cc6429003a649159244e09bf12baed6534112eb460da46a5da'
idx=json.loads((R/index_path).read_text())
for f in idx['files']:assert sha((R/f['path']).read_bytes())==f['sha256']
p=json.loads((R/idx['files'][0]['path']).read_text())
rereads=json.loads((R/(base+'clean_group01/S6_SERIES_PUBLISH_II_A_recovery_clean_group01_rereads.json')).read_text())
rs={x['tag']:x for x in rereads['records']}
before=(R/'S6_SERIES_PUBLISH_II.tex').read_text();s=before;patches=[];bindings=[]
for b in p['blocks']:
 old=(R/b['original_path']).read_text();new=(R/b['proposed_path']).read_text()
 assert sha(old)==b['original_sha256'] and sha(new)==b['proposed_sha256']
 assert rs[b['tag']]['complete_original_and_proposed_read']
 assert rs[b['tag']]['original_sha256']==sha(old) and rs[b['tag']]['proposed_sha256']==sha(new)
 owner=re.search(r'\\StatementRecord\{([^}]+)\}',old).group(1)
 assert s.count(old)==1
 cur=old
 for g in [x for x in p['guards'] if x['tag']==b['tag']]:
  assert sha(cur)==g['intermediate_before_sha256']
  assert cur.count(g['literal_old'])==1
  start=s.index(cur);pos=start+cur.index(g['literal_old']);a,z=pos,pos+len(g['literal_old']);end=start+len(cur)
  while s.count(s[a:z])!=1:
   prior=(a,z);a,z=max(start,a-100),min(end,z+100);assert (a,z)!=prior
  oldliteral=s[a:z];newliteral=s[a:pos]+g['literal_new']+s[pos+len(g['literal_old']):z]
  patches.append(dict(old=oldliteral,new=newliteral,type='/'.join(g['defect_types']),statement_id=owner,
    reason=g['reason']+' '+g['mathematical_transport']+' Root read every literal guard, the full comparison narrative, and the complete fresh programs/outputs. The checker actually reread both complete blocks.',
    originating_change_id=g['guard_id'],changed_old_literal=g['literal_old'],changed_new_literal=g['literal_new']))
  s=s[:a]+newliteral+s[z:];cur=cur.replace(g['literal_old'],g['literal_new'],1)
  assert sha(cur)==g['intermediate_after_sha256']
 assert cur==new and s.count(new)==1
 bindings.append(dict(owner=owner,tag=b['tag'],original={'path':b['original_path'],'sha256':sha(old)},
   proposed={'path':b['proposed_path'],'sha256':sha(new)},actual_complete_pair_read_by_checker=True,
   root_all_literal_guards_and_complete_comparisons_read=True,root_complete_proposed_block_read=False))
start=s.index(r'\section*{Programs}');end=s.index(r'\end{longtable}}',start)+len(r'\end{longtable}}')
table=s[start:end]
row=r'''Jet covariance, binary-cubic discriminants and inverse-Jacobian pole coefficients (\cref{cdp:st:C2d}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/C_jets.py}{\nolinkurl{C_jets.py}} \\[3pt]
'''
assert 'C_jets.py' not in table
newtable=table.replace(r'\end{longtable}}',row+r'\end{longtable}}')
patches.append(dict(old=table,new=newtable,type='D09',statement_id='tab:II:programs',
 reason='Move the exact pinned C_jets.py citation removed from the proof into the sole end table. The old/new methods were compared in the complete checker narrative; root read the whole original table and this added row. No new mathematical event is assigned to a citation move.'))
s=s[:start]+newtable+s[end:]
o=R/'records/S6_SERIES_PUBLISH_II_A_clean_01_editorial_guard.json';assert not o.exists()
g=dict(paper='II',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,bindings=bindings,
 evidence_index={'path':index_path,'sha256':sha((R/index_path).read_bytes())},mathematical_events_added=0,visual_reading_credit=0)
assert len(patches)==15
o.write_text(json.dumps(g,indent=2)+'\n')
print(json.dumps(dict(guard=str(o.relative_to(R)),sha256=sha(o.read_bytes()),patches=len(patches),source_after_sha256=sha(s)),indent=2))
