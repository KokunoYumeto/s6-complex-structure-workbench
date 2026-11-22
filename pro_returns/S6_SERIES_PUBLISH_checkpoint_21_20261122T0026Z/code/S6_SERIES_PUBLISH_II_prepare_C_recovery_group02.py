"""Bind the reviewed C recovery guards without changing historical records."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parents[1]
P=R/'agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_second_group_guards.json'
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
assert sha(P.read_bytes())=='3287306661b04e49c006a085b0e8e3019d9d8c47166697d29c879bc3b1e5fbd2'
p=json.loads(P.read_text());before=(R/'S6_SERIES_PUBLISH_II.tex').read_text();s=before
blocks={};bindings=[];patches=[]
for b in p['blocks']:
 owner=b['statement_id'];old=(R/b['original_full_block']).read_text();new=(R/b['proposed_full_block']).read_text()
 assert sha(old)==b['original_full_block_sha256'] and sha(new)==b['proposed_full_block_sha256']
 assert s.count(old)==1
 blocks[owner]=old
 bindings.append(dict(owner=owner,before={'path':b['original_full_block'],'sha256':sha(old)},after={'path':b['proposed_full_block'],'sha256':sha(new)},root_all_literal_guards_and_full_comparison_read=True,complete_pair_reader='restore_build',root_complete_blocks_read=False))
for c in p['guards']:
 owner=c['statement_id'];old,new=c['before'],c['after']
 if owner in blocks:
  current=blocks[owner];assert current.count(old)==1 and s.count(current)==1
  blockstart=s.index(current);pos=blockstart+current.index(old);a,z=pos,pos+len(old);blockend=blockstart+len(current)
  while s.count(s[a:z])!=1:
   a=max(blockstart,a-100);z=min(blockend,z+100)
   assert a<pos or z>pos+len(old)
  expanded_old=s[a:z];expanded_new=s[a:pos]+new+s[pos+len(old):z]
  blocks[owner]=current.replace(old,new,1)
 else:
  assert owner=='tab:II:programs' and s.count(old)==1
  a=s.index(old);z=a+len(old);expanded_old=old;expanded_new=new
 kind=c['type'].replace('D03','D04')
 if c['id'].endswith('-grammar'):kind='D23'
 patches.append(dict(old=expanded_old,new=expanded_new,type=kind,statement_id=owner,reason=c['reason']+' Root read all literal guards, the complete mathematical comparison and full fresh code/output. The original proposal category is preserved below.',originating_change_id=c['id'],original_proposal_type=c['type'],changed_old_literal=old,changed_new_literal=new))
 s=s[:a]+expanded_new+s[z:]
for b in bindings:
 new=(R/b['after']['path']).read_text();assert blocks[b['owner']]==new and s.count(new)==1
table_start=s.index('\\section*{Programs}')
table_end=s.index('\\begin{thebibliography}',table_start)
table=R/'records/S6_SERIES_PUBLISH_II_C_recovery_group02_combined_program_table.tex'
table.write_text(s[table_start:table_end])
g=dict(paper='II',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_before_sha256=sha(before),source_after_sha256=sha(s),patches=patches,bindings=bindings,proposal={'path':str(P.relative_to(R)),'sha256':sha(P.read_bytes())},combined_program_table={'path':str(table.relative_to(R)),'sha256':sha(table.read_bytes()),'scope':'The single changed D_exact_checks scope row is applied to the current table. The separately applied UN4 row is preserved exactly.'},root_receiver_scope_review='Root reread the complete smooth Main B hypothesis paragraph and its four outline steps after recovery; their scope is the same. The checker record binds all eleven remaining receiving statements and exact NC3/P201 definitions.',mathematical_events_added=0,visual_reading_credit=0)
out=R/'records/S6_SERIES_PUBLISH_II_C_recovery_group02_editorial_guard.json';assert not out.exists();out.write_text(json.dumps(g,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(R)),'sha256':sha(out.read_bytes()),'patches':len(patches),'owners':len(bindings),'source_after_sha256':sha(s)},indent=2))
