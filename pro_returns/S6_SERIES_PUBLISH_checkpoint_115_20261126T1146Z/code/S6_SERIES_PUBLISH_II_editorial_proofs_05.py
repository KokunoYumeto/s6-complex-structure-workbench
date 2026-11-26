#!/usr/bin/env python3
"""Admit the six-owner comparative program/reference packet without new check credit."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint as titlefp
from S6_SERIES_PUBLISH_II_D10_census import valid as d10valid,fingerprint as d10fp
R=Path(__file__).resolve().parents[1]
A=R/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_final_v1'
P='S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_'
O=R/'records/S6_SERIES_PUBLISH_II_editorial_proofs_05';MAN=str((O/'manifest.json').relative_to(R))
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
assert sha(index.read_bytes())=='f8b28fb8c34d1ff0d81fd88690fe3c11119581e674f077e1425dfd77a6c779a3'
ix=json.loads(index.read_text())
for f in ix['files']:
 b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path']
old=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=old.decode()
assert sha(old)=='a06fe74550515e6e3cb74cce2763a9c340d05c4323f44a0699d6a0f39fe522f5'
guards=json.loads((A/(P+'guards.json')).read_text());assert len(guards)==13;ranges=[]
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
 assert before.count(r'\item')==after.count(r'\item')==owner['original_item_tokens']
 for pat in [r'\\(?:label|hypertarget|tag)\{[^}]*\}',r'\\begin\{enumerate\}(?:\[[^\n]*\])?']:
  assert re.findall(pat,before)==re.findall(pat,after),tag
 assert after.startswith(before[:before.rindex(r'\end{enumerate}')]),tag
 following_before=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_before.tex').read_text();following_after=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex').read_text()
 assert s.count(before+following_before)==1 and new.count(after+following_after)==1
 comparisons.append(dict(tag=tag,owner=owner['owner'],before_sha256=owner['before_sha256'],after_sha256=owner['after_sha256'],original_math_regions_preserved=len(math(before)),original_item_tokens=owner['original_item_tokens'],all_original_math_in_exact_order=True))
for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:
 assert re.findall(pat,s)==re.findall(pat,new)
assert titlefp(s)==titlefp(new) and d10valid(new) and d10fp(s)==d10fp(new)
now=dt.datetime.now(dt.timezone.utc).isoformat();eb=(R/'CHECK_EVENTS.tsv').read_bytes();events,ef=table(eb)
ev=[]
for e in json.loads((A/(P+'event_proposals.json')).read_text())['events']:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 row={k:e.get(k,'') for k in ef};row['phase']='publication editorial comparison';row['source_event_type']=e['type'];row['publish_input_file']=MAN;ev.append(row)
assert len(ev)==6 and len({r['evidence_group'] for r in ev})==1
db=(R/'S6_SERIES_PUBLISH_defects_II.tsv').read_bytes();defs,df=table(db);proposed,_=table((A/(P+'defects.tsv')).read_bytes());assert len(proposed)==32
added=[];byguard={g['id']:g for g in guards}
for d in proposed:
 g=byguard[d['guard_id']];row={k:'' for k in df}
 row.update(change_id='II-EDITORIAL-PROOFS05-'+d['id'],type=d['type'],statement_id=d['owner'],old_location=d['tag']+' / '+d['guard_id']+' / original line '+d['source_line'],old_page='source locator bound by complete original owner',new_location=d['owner']+' / '+d['guard_id'],new_page='pending integrated build',old_text=d['old_text'],new_text=d['new_text'],reason=g['reason'],review_status='Full six-owner original/final comparison by A. Root read the complete comparison map, all eight exact diffs, full old/new XL with its following paragraph, full final XF/XK, exact historical domain rows, Programs guards and bounded node program/output. No fresh independent, targeted, required-row, class or final-page credit.');added.append(row)
assert not ({r['change_id'] for r in added}&{r['change_id'] for r in defs})
bundle=tab(ev,ef);rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();reg=json.loads(rb)
reg['bundles'].append(dict(path=str((O/'event_rows.tsv').relative_to(R)),bytes=len(bundle),sha256=sha(bundle),admission_manifest=MAN))
O.mkdir();(O/'inverse.json').write_bytes(enc(inverse));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before editorial proofs05',tofile='II after editorial proofs05')))
(O/'event_rows.tsv').write_bytes(bundle);(O/'defect_rows.tsv').write_bytes(tab(added,df))
reading=dict(recorded_utc=now,full_comparison=bind(A/(P+'comparison.md')),all_six_exact_diffs=[bind(A/f'S6_SERIES_PUBLISH_II_A2_{x["tag"]}_exact.diff') for x in ix['owners']],complete_root_original_readings=[bind(A/f'S6_SERIES_PUBLISH_II_A2_{x}_before.tex') for x in ['01B8','01BF','02YC','02WI','02WH']],complete_moved_passage_readings=[bind(A/f'S6_SERIES_PUBLISH_II_A2_{x}_following_before.tex') for x in ['01B8','01BF','02YC']],complete_support_readings=[bind(A/f'S6_SERIES_PUBLISH_II_A2_batch05_support_{x}.tex') for x in ['P458','A57']],reading_receipt=bind(A/(P+'reading_receipt.json')),program_table=bind(A/(P+'Programs_rows_after.tex')),limits='A read all complete originals and finals, all seven historical source/stdout pairs and two JSON outputs. Root read the specified complete originals plus every exact difference and moved mathematical passage; no separate full final-owner or historical-source read by root is claimed. No historical program execution or additional root event.')
(O/'root_reading.json').write_bytes(enc(reading))
changes=[('S6_SERIES_PUBLISH_II.tex',old,new.encode()),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,False)),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(added,df,False)),(str(rp.relative_to(R)),rb,enc(reg))]
manifest=dict(created_utc=now,sealed_index=bind(index),sealed_bindings_verified=len(ix['files']),source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),unique_disjoint_guards=13,exact_inverse=True,owner_comparisons=comparisons,original_item_tokens=52,original_bracket_displays=91,existing_displays_moved_inside_proofs=6,mathematical_preservation='Every statement and original proof body remains byte-identical. Three complete previously following mathematical passages are moved into their proving owners; the conductor example changes only historical prose, and the other formulas and exact maps remain unchanged.',program_rows_added=1,existing_program_rows_amended=6,new_historical_links_opened_by_A=6,historical_sources_fully_read_by_A=7,historical_stdout_files_read_by_A=7,historical_json_files_read_by_A=2,historical_programs_executed_this_batch=0,new_mathematical_programs=0,events_added=6,event_groups=1,event_types={'used and rechecked in this run':6},ledger_rows_before=len(events),ledger_rows_after=len(events)+6,defect_rows_added=32,defect_rows_after=len(defs)+32,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,D10_fingerprint_unchanged=d10fp(new),D16_fingerprint_unchanged=titlefp(new),canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a),before_bytes=len(b),after_bytes=len(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
note=f'\n\n## Paper II: six complete proof and program comparisons — {now}\n\nAdmitted the fully compared packet for02YF,02YC,02YE,02WI,01BF and01B8. All52 original item tokens,91 bracket displays, every statement and every original proof body retain their exact bytes. The existing conductor-cleared cubic example, two-direction spectral example and rational double-cover calculation now appear within their proving owners; all six moved displays and their precise maps remain. The unchanged supporting WH/A57/P458 proofs establish the exact program and status scope. The separate Reid credit paragraph remains explicitly pending.\n\nSix program-bearing contexts are removed from the mathematical body. One Programs row is added and six are amended; six new historical links were opened. Seven historical sources and stdout files and two JSON outputs were read by A, with no execution or independent event. The nonexistent necessity-examples JSON lookup is preserved as a retrieval failure; the actual stdout source/output exists and was read.\n\nAdmission `{mb["path"]}` (SHA-256 `{mb["sha256"]}`) adds32 individual class records and six exposed-reread associations in one group. Source SHA-256 `{sha(new.encode())}`; ledger {len(events)+6} rows. D10/D16 fingerprints remain valid. No required row, global class or final-PDF page closes.\n'
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],all_prior_ledger_bytes_preserved=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','unique_disjoint_guards','ledger_rows_after','defect_rows_added','defect_rows_after']},indent=2));print('Manifest',mb['sha256'])
