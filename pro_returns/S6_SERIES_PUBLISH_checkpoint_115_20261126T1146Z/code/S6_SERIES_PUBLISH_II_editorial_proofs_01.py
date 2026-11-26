#!/usr/bin/env python3
"""Admit the completely compared R10/R14/R15 editorial packet, preserving its exact maps."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
R=Path(__file__).resolve().parents[1]
A=R/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_final_v1'
OUT=R/'records/S6_SERIES_PUBLISH_II_editorial_proofs_01'
csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def table(b):
 r=csv.DictReader(io.StringIO(b.decode()),delimiter='\t');return list(r),r.fieldnames
def tab(rows,fields,header=True):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter='\t',lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return o.getvalue().encode()
assert not OUT.exists()
index=A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_index.json'
assert sha(index.read_bytes())=='50efa1d57bfe4b50d158c937a5018fc82043d581558e5dd83fef71cfaf22b5fd'
ix=json.loads(index.read_text())
for x in ix['files']:
 b=(R/x['path']).read_bytes();assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['path']
old=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=old.decode()
assert sha(old)=='eb8e4f2e5a77da9830ccb1673bfbe5e4ae7284ec1384b87e6597a4c6c69c5d88'
guards=json.loads((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_guards.json').read_text())
new=s;inverse=[];comparisons=[]
for owner in ix['owners']:
 tag=owner['tag'];before=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex').read_text();after=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex').read_text()
 assert new.count(before)==1 and sha(before.encode())==owner['before_sha256'] and sha(after.encode())==owner['after_sha256']
 replay=before
 for g in [g for g in guards if g['tag']==tag]:
  assert replay.count(g['old'])==g['expected_count']==1,g['id'];replay=replay.replace(g['old'],g['new'],1)
 assert replay==after
 displays=lambda t:re.findall(r'\\\[(.*?)\\\]',t,re.S)
 assert not (collections.Counter(displays(before))-collections.Counter(displays(after)))
 assert before.count('\\item')==after.count('\\item')==owner['proof_items_preserved']
 p=new.index(before);new=new[:p]+after+new[p+len(before):]
 inverse.append(dict(offset=p,old=before,new=after,owner=owner['owner']))
 comparisons.append(dict(owner=owner['owner'],tag=tag,before_sha256=sha(before.encode()),after_sha256=sha(after.encode()),all_old_displays_preserved=True,proof_items=owner['proof_items_preserved']))
program_original=(A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_Programs_rows.tex').read_text()
commit=re.search(r'\\newcommand\{\\SsixRepositoryCommit\}\{([a-f0-9]+)\}',new)[1]
assert commit=='83d76022bcd442278b760db9ff438afceed6c6ea'
assert program_original.count('/83d76022bc/')==3
programs=program_original.replace('/83d76022bc/',r'/\SsixRepositoryCommit/')
program_start=new.index(r'\section*{Programs}');p=new.index(r'\end{longtable}}',program_start)
assert all(name not in new[program_start:] for name in ['tacnode_hessian.py','smooth_a3_polar.py','hessian_product.py'])
new=new[:p]+programs+new[p:];inverse.append(dict(offset=p,old='',new=programs,owner='Programs'))
back=new
for g in reversed(inverse):
 p=g['offset'];assert back[p:p+len(g['new'])]==g['new'];back=back[:p]+g['old']+back[p+len(g['new']):]
assert back==s
for p in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:
 assert re.findall(p,s)==re.findall(p,new)
all_labels=set(re.findall(r'\\label\{([^}]+)\}',new))
for m in re.finditer(r'\\cref\{([^}]+)\}',programs):assert set(m[1].split(','))<=all_labels
now=dt.datetime.now(dt.timezone.utc).isoformat()
eb=(R/'CHECK_EVENTS.tsv').read_bytes();events,ef=table(eb)
proposed=json.loads((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_event_proposals.json').read_text())['events'];added_events=[]
for e in proposed:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 row={k:e.get(k,'') for k in ef};row['phase']='publication editorial comparison';row['source_event_type']=e['type'];added_events.append(row)
assert len(added_events)==3
event_bundle=tab(added_events,ef);event_after=eb+tab(added_events,ef,False)
db=(R/'S6_SERIES_PUBLISH_defects_II.tsv').read_bytes();defects,df=table(db)
proposal_rows,_=table((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch01_defects.tsv').read_bytes());added=[]
assert len(proposal_rows)==len(guards)==24
for x in proposal_rows:
 row={k:'' for k in df};row.update(change_id='II-EDITORIAL-PROOFS01-'+x['id'],type=x['defect_ids'],statement_id=x['owner'],old_location=x['source_line_span'],old_page='historical source; exact source bytes bound',new_location=x['owner'],new_page='pending integrated build',old_text=x['old'],new_text=x['new'],reason=x['reason']+' '+x['mathematical_disposition'],review_status='A and root each read all three complete original and amended proofs. Exact guards, inverse, all proof items and original displays checked. Historical program sources/outputs read by A; root read complete preservation program/output and comparison. No new independent or targeted check; final PDF reading pending.')
 added.append(row)
defect_after=db+tab(added,df,False)
rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();registry=json.loads(rb)
registry['bundles'].append(dict(path=str((OUT/'event_rows.tsv').relative_to(R)),bytes=len(event_bundle),sha256=sha(event_bundle),admission_manifest=str((OUT/'manifest.json').relative_to(R))))
registry_after=enc(registry)
OUT.mkdir()
for name,data in [('event_rows.tsv',event_bundle),('defect_rows.tsv',tab(added,df)),('inverse.json',enc(inverse)),('program_rows.tex',programs.encode())]:(OUT/name).write_bytes(data)
(OUT/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before editorial proofs01',tofile='II after editorial proofs01')))
(OUT/'program_commit_macro.diff').write_text(''.join(difflib.unified_diff(program_original.splitlines(True),programs.splitlines(True),fromfile='A sealed program rows',tofile='admitted rows using existing macro')))
changes=[('S6_SERIES_PUBLISH_II.tex',old,new.encode()),('CHECK_EVENTS.tsv',eb,event_after),('S6_SERIES_PUBLISH_defects_II.tsv',db,defect_after),(str(rp.relative_to(R)),rb,registry_after)]
manifest=dict(created_utc=now,A_index=bind(index),sealed_bindings_verified=len(ix['files']),source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),
 root_complete_readings=['All six complete before/after owning blocks, containing20 proof items and32 original displays.','Complete9726-byte comparison.','Complete4220-byte new Taylor/quotient program and1969-byte output.','All three program-table rows and the complete reading receipt.'],
 root_reading_limits='The first combined metadata output was truncated and has no full-output credit. The complete historical sources and outputs were read by A, not root. The full mathematical owning blocks and preservation program/output were separately read in bounded outputs.',
 owner_comparisons=comparisons,guards=len(guards),all_mutations_exactly_invertible=True,all_labels_tags_statement_records_preserved=True,
 mathematical_preservation='All original proof items,32 displays and geometric steps retained. The two already asserted examples are now given by explicit polynomials and Hessian formulas. The cusp formula uses aa=alpha and cc=gamma; the product formula follows the printed degree-two Taylor expansion. The original five R14 manual equation tags and every raw equation reference remain for D19.',
 program_rows=3,program_macro_resolution=dict(old_abbreviation='83d76022bc',macro='SsixRepositoryCommit',expanded_commit=commit,scope='Existing full commit begins with the retrieved abbreviation; exact URL verification at final pin remains within provenance.'),
 events_added=3,ledger_rows_before=len(events),ledger_rows_after=len(events)+3,event_types={'used and rechecked in this run':3},defect_rows_added=len(added),
 required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,
 canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a),before_bytes=len(b),after_bytes=len(a)) for n,b,a in changes],
 immutable_evidence=[bind(p) for p in sorted(OUT.iterdir())],code=bind(Path(__file__)))
mp=OUT/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
assert (R/'CHECK_EVENTS.tsv').read_bytes().startswith(eb)
note=f'''\n\n## Paper II: complete comparative editorial review of three local proofs — {now}\n\nThe complete original and revised proofs02Y3,02Y7 and02Y8 were read by A and root. All20 proof items and32 original displays remain. The cusp-Hessian and moving-node examples previously named in program reports now print their exact input polynomials, matrices and values. Raw statement references resolve to their existing owners and the standing setting; five manual equation tags and their equation references remain unchanged for D19. Three historical programs are cited once each in Programs through the existing commit macro. The exact aa=alpha, cc=gamma and Taylor/quotient computations are in the comparative record.\n\nThe admission `{mb['path']}` (SHA-256 `{mb['sha256']}`) records24 individual edits and three exposed-reread events. The canonical source is `{sha(new.encode())}` and ledger has {len(events)+3} rows. D09/D04 remain open across the rest of the source; no required row, global defect class or final PDF page is closed.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(OUT/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],all_prior_ledger_bytes_preserved=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','guards','events_added','ledger_rows_after','defect_rows_added','global_defect_classes_closed','final_pdf_page_credit']},indent=2))
print('Manifest:',mb['path'],mb['sha256'])
