#!/usr/bin/env python3
"""Admit the fully compared AJ/B1/AM editorial packet and exact program scopes."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint
R=Path(__file__).resolve().parents[1]
A=R/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_final_v1'
OUT=R/'records/S6_SERIES_PUBLISH_II_editorial_proofs_03'
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
index=A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_index.json'
assert sha(index.read_bytes())=='0dd84888941d0091be7122337a13b761535f320757dacf876c9b9799bf401f06'
ix=json.loads(index.read_text())
for x in ix['files']:
 b=(R/x['path']).read_bytes();assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['path']
old=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=old.decode();assert sha(old)==ix['source_snapshot_sha256']
guards=json.loads((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_guards.json').read_text())
new=s;inverse=[];comparisons=[]
for owner in ix['owners']:
 tag=owner['tag'];before=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex').read_text();after=(A/f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex').read_text()
 assert new.count(before)==1 and sha(before.encode())==owner['before_sha256'] and sha(after.encode())==owner['after_sha256']
 replay=before
 for g in [g for g in guards if g['tag']==tag]:
  assert replay.count(g['old'])==g['expected_count']==1,g['id'];replay=replay.replace(g['old'],g['new'],1)
 assert replay==after
 displays=lambda t:re.findall(r'\\\[(.*?)\\\]',t,re.S)
 assert displays(before)==displays(after)
 assert before.count('\\item')==after.count('\\item')==owner['proof_items_preserved']
 assert re.findall(r'\\begin\{enumerate\}\[[^\n]*\]',before)==re.findall(r'\\begin\{enumerate\}\[[^\n]*\]',after)
 p=new.index(before);new=new[:p]+after+new[p+len(before):];inverse.append(dict(offset=p,old=before,new=after,owner=owner['owner']))
 comparisons.append(dict(owner=owner['owner'],tag=tag,before_sha256=sha(before.encode()),after_sha256=sha(after.encode()),proof_items=owner['proof_items_preserved'],original_displays=owner['all_original_displays_preserved'],all_display_bytes_and_order_preserved=True,following_paragraph_included=True))
pg=[g for g in guards if not g['tag']];assert len(pg)==1;g=pg[0]
assert new.count(g['old'])==1;p=new.index(g['old']);new=new[:p]+g['new']+new[p+len(g['old']):];inverse.append(dict(offset=p,old=g['old'],new=g['new'],owner=g['owner']))
back=new
for g in reversed(inverse):
 p=g['offset'];assert back[p:p+len(g['new'])]==g['new'];back=back[:p]+g['old']+back[p+len(g['new']):]
assert back==s
for p in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:
 assert re.findall(p,s)==re.findall(p,new)
assert fingerprint(s)==fingerprint(new)
now=dt.datetime.now(dt.timezone.utc).isoformat()
eb=(R/'CHECK_EVENTS.tsv').read_bytes();events,ef=table(eb);proposed=json.loads((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_event_proposals.json').read_text())['events'];added_events=[]
for e in proposed:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 row={k:e.get(k,'') for k in ef};row['phase']='publication editorial comparison';row['source_event_type']=e['type'];added_events.append(row)
assert len(added_events)==3 and len({x['evidence_group'] for x in added_events})==1
bundle=tab(added_events,ef);event_after=eb+tab(added_events,ef,False)
db=(R/'S6_SERIES_PUBLISH_defects_II.tsv').read_bytes();defects,df=table(db)
proposed_defects,af=table((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch03_defects.tsv').read_bytes());assert af==df and len(proposed_defects)==8
added=[]
for original in proposed_defects:
 for kind in original['type'].split(';'):
  row=original.copy();row['type']=kind;row['change_id']='II-EDITORIAL-PROOFS03-'+original['change_id']+'-'+kind
  assert row['change_id'] not in {x['change_id'] for x in defects+added}
  row['review_status']='A and root read all six complete old/new owning blocks and their following paragraphs (AJ3742/3621,BK6233/6020,AM4039/3935 bytes). Root read full12270-byte comparison,4188-byte preservation program,1879-byte output, all reading/retrieval/preservation receipts,3806-byte historical-credit receipt and963-byte Programs rows. Exact guards/inverse and all14 displayed formulas verified. Supporting AE/AI and historical sources/outputs, including645 rows, were fully read by A. No independent, targeted, required-row or final-page credit.'
  added.append(row)
assert len(added)==11
defect_after=db+tab(added,df,False)
rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();registry=json.loads(rb);registry['bundles'].append(dict(path=str((OUT/'event_rows.tsv').relative_to(R)),bytes=len(bundle),sha256=sha(bundle),admission_manifest=str((OUT/'manifest.json').relative_to(R))))
changes=[('S6_SERIES_PUBLISH_II.tex',old,new.encode()),('CHECK_EVENTS.tsv',eb,event_after),('S6_SERIES_PUBLISH_defects_II.tsv',db,defect_after),(str(rp.relative_to(R)),rb,enc(registry))]
OUT.mkdir();(OUT/'inverse.json').write_bytes(enc(inverse));(OUT/'event_rows.tsv').write_bytes(bundle);(OUT/'defect_rows.tsv').write_bytes(tab(added,df))
(OUT/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before editorial proofs03',tofile='II after editorial proofs03')))
manifest=dict(created_utc=now,A_index=bind(index),sealed_bindings_verified=len(ix['files']),source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),
 complete_root_readings='All six complete original/final statement-proof blocks, including each following paragraph, read. Full comparison, preservation program/output, reading/retrieval/preservation receipts, historical-credit receipt and Programs rows read. The supporting AE/AI proof readings and all historical source/output readings belong to A; root does not claim those full readings.',
 owner_comparisons=comparisons,owner_guards=7,programs_guards=1,all_mutations_exactly_invertible=True,all_labels_tags_statement_record_triples_preserved=True,
 mathematical_preservation='All11 proof items and14 displayed formulas retained byte-for-byte in their original order. B1 names its existing jointly vanishing groups and resolves the exact normal-crossing map. The A.13 character formula moves intact into AM item3. Historical program range3<=m<=12 remains in Programs and does not restrict the theorem. AJ mathematics remains unchanged; its old adjacent program is attributed to its actual AE/AI computations.',
 historical_credit='The original supplied-note attribution is preserved in the immutable old block and exact guarded diff, with the attached CDP report excerpt and hash. The original correction-note document remains unidentified. No new publication attribution or priority assertion is made.',
 program_rows=3,program_link_scope='All three historical sources and outputs were opened by A at the full current repository-commit value; six URL/hash/status records are sealed. No new remote program publication is asserted.',
 events_added=3,event_types={'used and rechecked in this run':3},evidence_groups=1,ledger_rows_before=len(events),ledger_rows_after=len(events)+3,defect_rows_added=11,
 defect_classification='Eight proposed changed-span records are expanded into11 individual class records by splitting their exact semicolon lists; no additional source edit is introduced.',
 required_rows_closed=0,global_defect_classes_closed=0,existing_D16_title_projection_unchanged=True,current_header_fingerprint=fingerprint(new),final_pdf_page_credit=0,
 canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a),before_bytes=len(b),after_bytes=len(a)) for n,b,a in changes],
 immutable_evidence=[bind(p) for p in sorted(OUT.iterdir())],code=bind(Path(__file__)))
mp=OUT/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
assert (R/'CHECK_EVENTS.tsv').read_bytes().startswith(eb)
note=f'''\n\n## Paper II: local algebra, nodal family and thickened-fibre presentation — {now}\n\nAdmitted the complete comparative editorial review of01AJ,01BK and01AM, including all following paragraphs. All11 proof items and14 displayed formulas retain their exact bytes and order. The two B1 groups and its normal-crossing map now have explicit references; the gluing convention and exceptional scalar remain in the proof. The full A.13 character count moves into AM item3. AJ's proof is unchanged, and its adjacent historical program is attributed to the actual AE/AI computations. The supplied-note credit is preserved in records with its honest unidentified-original scope. Three historical Programs links were actually opened at the full pinned commit.\n\nThe admission `{mb['path']}` (SHA-256 `{mb['sha256']}`) adds11 individual class records and three exposed-reread events in one evidence group. Source SHA-256 `{sha(new.encode())}`; ledger {len(events)+3} rows. The full title projection is unchanged, preserving D16. No further global class, required row or final PDF page closes.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(OUT/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],all_prior_ledger_bytes_preserved=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','owner_guards','programs_guards','events_added','ledger_rows_after','defect_rows_added','existing_D16_title_projection_unchanged','final_pdf_page_credit']},indent=2));print('Manifest:',mb['path'],mb['sha256'])
