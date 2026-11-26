#!/usr/bin/env python3
"""Admit the eight-owner comparative program/reference packet without new check credit."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint as titlefp
from S6_SERIES_PUBLISH_II_D10_census import valid as d10valid,fingerprint as d10fp
R=Path(__file__).resolve().parents[1]
A=R/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch04_final_v1'
P='S6_SERIES_PUBLISH_II_A2_D09_D04_batch04_'
O=R/'records/S6_SERIES_PUBLISH_II_editorial_proofs_04';MAN=str((O/'manifest.json').relative_to(R))
csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def table(b):
 rd=csv.DictReader(io.StringIO(b.decode()),delimiter='\t');return list(rd),rd.fieldnames
def tab(rows,fields,header=True):
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=fields,delimiter='\t',lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return out.getvalue().encode()
assert not O.exists();index=A/(P+'index.json')
assert sha(index.read_bytes())=='a87e9142f44e400636c5653cb72f4aecb35264329c48e4cf08c3b8c7a2adf4bd'
ix=json.loads(index.read_text())
for f in ix['files']:
 b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path']
old=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=old.decode()
assert sha(old)=='a23693573204ffa57ded14b8e5037ec92b990f5fe4fb636baf28a9f160073153'
guards=json.loads((A/(P+'guards.json')).read_text());assert len(guards)==37;ranges=[]
for g in guards:
 assert s.count(g['old'])==g['expected_count']==1,g['id'];a=s.index(g['old']);ranges.append((a,a+len(g['old']),g['id']))
 assert sha(g['old'].encode())==g['old_sha256'] and sha(g['new'].encode())==g['new_sha256']
for a,b in zip(sorted(ranges),sorted(ranges)[1:]):assert a[1]<=b[0],(a,b)
new=s;inverse=[]
for g in guards:
 a=new.index(g['old']);inverse.append(dict(id=g['id'],offset=a,old=g['old'],new=g['new']))
 new=new[:a]+g['new']+new[a+len(g['old']):]
back=new
for g in reversed(inverse):
 a=g['offset'];assert back[a:a+len(g['new'])]==g['new'];back=back[:a]+g['old']+back[a+len(g['new']):]
assert back==s
math=lambda x:re.findall(r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?!\$).*?(?<!\\)\$|'+r'\\begin\{(?:align\*?|equation\*?|gather\*?)\}.*?\\end\{(?:align\*?|equation\*?|gather\*?)\}',x,re.S)
comparisons=[]
for owner in ix['owners']:
 tag=owner['tag'];before=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex').read_text();after=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex').read_text()
 assert sha(before.encode())==owner['before_sha256'] and sha(after.encode())==owner['after_sha256']
 assert s.count(before)==1 and new.count(after)==1
 it=iter(math(after));assert all(any(q==x for q in it) for x in math(before)),tag
 assert before.count(r'\item')==after.count(r'\item')==owner['items_preserved']
 for pat in [r'\\(?:label|hypertarget|tag)\{[^}]*\}',r'\\eqref\{[^}]*\}',r'\\begin\{enumerate\}(?:\[[^\n]*\])?']:
  assert re.findall(pat,before)==re.findall(pat,after),tag
 following_before=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_before.tex').read_text();following_after=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex').read_text()
 assert s.count(before+following_before)==1 and new.count(after+following_after)==1
 comparisons.append(dict(tag=tag,owner=owner['owner'],before_sha256=owner['before_sha256'],after_sha256=owner['after_sha256'],original_math_regions_preserved=len(math(before)),original_item_tokens=owner['items_preserved'],all_original_math_in_exact_order=True))
for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:
 assert re.findall(pat,s)==re.findall(pat,new)
assert titlefp(s)==titlefp(new) and d10valid(new) and d10fp(s)==d10fp(new)
refs=json.loads((A/(P+'reference_map.json')).read_text());assert len(refs)==27
for ref in refs:assert new.count(r'\label{'+ref['target']+'}')==1
scope=json.loads((A/(P+'scope_receipt.json')).read_text());sp=Path(scope['historical_metadata_path']);assert sha(sp.read_bytes())==scope['historical_metadata_sha256']
assert [r for r in csv.DictReader(sp.open()) if r['id'] in ['P4.26','P4.46']]==scope['selected_exact_rows']
definition=(A/'S6_SERIES_PUBLISH_II_A2_batch04_scope_P204.tex').read_text();assert sha(definition.encode())==scope['standing_definition_sha256'] and new.count(definition)==1
now=dt.datetime.now(dt.timezone.utc).isoformat();eb=(R/'CHECK_EVENTS.tsv').read_bytes();events,ef=table(eb)
ev=[]
for e in json.loads((A/(P+'event_proposals.json')).read_text())['events']:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 row={k:e.get(k,'') for k in ef};row['phase']='publication editorial comparison';row['source_event_type']=e['type'];row['publish_input_file']=MAN;ev.append(row)
assert len(ev)==8 and len({r['evidence_group'] for r in ev})==1
db=(R/'S6_SERIES_PUBLISH_defects_II.tsv').read_bytes();defs,df=table(db);proposed,_=table((A/(P+'defects.tsv')).read_bytes());assert len(proposed)==47
added=[];byguard={g['id']:g for g in guards}
for d in proposed:
 g=byguard[d['guard_id']];row={k:'' for k in df}
 row.update(change_id='II-EDITORIAL-PROOFS04-'+d['id'],type=d['type'],statement_id=d['owner'],old_location=d['tag']+' / '+d['guard_id']+' / original line '+d['source_line'],old_page='source locator bound by complete original owner',new_location=d['owner']+' / '+d['guard_id'],new_page='pending integrated build',old_text=d['old_text'],new_text=d['new_text'],reason=g['reason'],review_status='Full eight-owner original/final comparison by A. Root read the complete comparison map, all eight exact diffs, full old/new XL with its following paragraph, full final XF/XK, exact historical domain rows, Programs guards and bounded node program/output. No fresh independent, targeted, required-row, class or final-page credit.');added.append(row)
assert not ({r['change_id'] for r in added}&{r['change_id'] for r in defs})
bundle=tab(ev,ef);rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();reg=json.loads(rb)
reg['bundles'].append(dict(path=str((O/'event_rows.tsv').relative_to(R)),bytes=len(bundle),sha256=sha(bundle),admission_manifest=MAN))
O.mkdir();(O/'inverse.json').write_bytes(enc(inverse));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before editorial proofs04',tofile='II after editorial proofs04')))
(O/'event_rows.tsv').write_bytes(bundle);(O/'defect_rows.tsv').write_bytes(tab(added,df))
reading=dict(recorded_utc=now,full_comparison=bind(A/(P+'comparison.md')),all_eight_exact_diffs=[bind(A/f'S6_SERIES_PUBLISH_II_A2_{x["tag"]}_exact.diff') for x in ix['owners']],complete_root_block_readings=[bind(A/f'S6_SERIES_PUBLISH_II_A2_{x}.tex') for x in ['02XL_before','02XL_after','02XL_following_before','02XF_after','02XK_after']],complete_receipts_read=[bind(A/(P+x+'.json')) for x in ['scope_receipt','reading_receipt','reference_map']],complete_node_program=bind(R/'code/S6_SERIES_PUBLISH_II_A2_D09_batch04_boundary_nodes.py'),complete_node_output=bind(A/'S6_SERIES_PUBLISH_II_A2_D09_batch04_boundary_nodes_output.json'),program_table='All seven new rows and both complete existing-row guards read.',limits='A read all complete originals/finals and historical sources/outputs. Root does not claim another full reading of every owner or any historical program execution. No extra event from root admission.')
(O/'root_reading.json').write_bytes(enc(reading))
changes=[('S6_SERIES_PUBLISH_II.tex',old,new.encode()),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,False)),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(added,df,False)),(str(rp.relative_to(R)),rb,enc(reg))]
manifest=dict(created_utc=now,sealed_index=bind(index),sealed_bindings_verified=len(ix['files']),source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),unique_disjoint_guards=37,exact_inverse=True,owner_comparisons=comparisons,original_item_tokens=42,original_bracket_displays=85,new_bracket_displays=2,mathematical_preservation='Every original mathematical region remains byte-identical in order. The previously stated shifted-square example is now proved with the actual analytic Jacobians and node-coordinate maps. All original fixed-axis proof steps remain.',domain_transport='P204 and the two exact historical metadata rows identify the original XF/XK domain; no changed mathematical hypothesis or error correction is asserted.',raw_references_resolved=27,program_rows_added=7,existing_program_rows_amended=2,historical_program_links_opened_by_A=25,historical_programs_executed_this_batch=0,new_program_remote_publication_pending=True,events_added=8,event_groups=1,event_types={'used and rechecked in this run':8},ledger_rows_before=len(events),ledger_rows_after=len(events)+8,defect_rows_added=47,defect_rows_after=len(defs)+47,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,D10_fingerprint_unchanged=d10fp(new),D16_fingerprint_unchanged=titlefp(new),canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a),before_bytes=len(b),after_bytes=len(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
note=f'''\n\n## Paper II: eight local-defect proof and program comparisons — {now}\n\nAdmitted the complete comparative packet for02XE,02XF,02XK,02XL,02XN,02Y9,02YA and02YB. All42 original proof-item tokens,85 original bracket displays and every other original mathematical region retain their bytes and order. The existing shifted-square example is moved from production commentary into XL's proof with explicit invertible coordinate maps to its two ordinary nodes; the complete original fixed-axis proof remains. The exact historical metadata identifies XK's original irreducible-or-normal-crossing whole-fibration domain. Twenty-seven raw statement names now resolve to their same permanent labels.\n\nEight program paragraphs move to Programs/records. Seven table rows are added and two existing rows receive historical links; all eight historical sources and17 saved outputs/failure files were opened and read by A. Historical outputs are not new executions. The new bounded node calculation has its actual exposed scope and no additional check event. Its new remote link remains in the final publication verification gate.\n\nAdmission `{mb['path']}` (SHA-256 `{mb['sha256']}`) adds47 individual class records and eight exposed-reread events in one group. Source SHA-256 `{sha(new.encode())}`; ledger {len(events)+8} rows. D10/D16 fingerprints remain valid. No required row, further global class or final PDF page closes.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],all_prior_ledger_bytes_preserved=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','unique_disjoint_guards','ledger_rows_after','defect_rows_added','defect_rows_after']},indent=2));print('Manifest',mb['sha256'])
