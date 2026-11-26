#!/usr/bin/env python3
"""Admit the fully compared FH/XB/XC packet and its exact historical program maps."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint
R=Path(__file__).resolve().parents[1]
A=R/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_final_v1'
OUT=R/'records/S6_SERIES_PUBLISH_II_editorial_proofs_02'
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
index=A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_index.json'
assert sha(index.read_bytes())=='da7fee90b2e2f59b3fe262a724daeef7d9b0ffb4443679ee37800dc3fd41cb21'
ix=json.loads(index.read_text())
for x in ix['files']:
 b=(R/x['path']).read_bytes();assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['path']
old=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=old.decode();assert sha(old)==ix['source_snapshot_sha256']
guards=json.loads((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_guards.json').read_text())
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
 assert collections.Counter(re.findall(r'\(4\.39[a-d]\)',before))==collections.Counter(re.findall(r'\(4\.39[a-d]\)',after))
 p=new.index(before);new=new[:p]+after+new[p+len(before):];inverse.append(dict(offset=p,old=before,new=after,owner=owner['owner']))
 comparisons.append(dict(owner=owner['owner'],tag=tag,before_sha256=sha(before.encode()),after_sha256=sha(after.encode()),proof_items=owner['proof_items_preserved'],original_displays=owner['old_displays_preserved'],all_original_displays_preserved=True,outside_proof_program_paragraph_included=owner['outside_program_paragraph_included']))
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
eb=(R/'CHECK_EVENTS.tsv').read_bytes();events,ef=table(eb);proposed=json.loads((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_event_proposals.json').read_text())['events'];added_events=[]
for e in proposed:
 assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events}
 row={k:e.get(k,'') for k in ef};row['phase']='publication editorial comparison';row['source_event_type']=e['type'];added_events.append(row)
assert len(added_events)==3 and len({x['evidence_group'] for x in added_events})==1
bundle=tab(added_events,ef);event_after=eb+tab(added_events,ef,False)
db=(R/'S6_SERIES_PUBLISH_defects_II.tsv').read_bytes();defects,df=table(db)
added,af=table((A/'S6_SERIES_PUBLISH_II_A2_D09_D04_batch02_defects.tsv').read_bytes());assert af==df and len(added)==20
for row in added:
 row['change_id']='II-EDITORIAL-PROOFS02-'+row['change_id'];assert row['change_id'] not in {x['change_id'] for x in defects}
 row['review_status']='A and root read the complete before/after proof blocks and the XB/XC following program paragraphs. Root read full16222-byte comparison,4040-byte preservation program,2548-byte output, reading receipt and both retrieval receipts. Exact forward/inverse and mathematical-display identities verified; original numbered equation references preserved. Historical sources/outputs were fully read by A. No new targeted/independent credit; final page reading pending.'
defect_after=db+tab(added,df,False)
rp=R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json';rb=rp.read_bytes();registry=json.loads(rb);registry['bundles'].append(dict(path=str((OUT/'event_rows.tsv').relative_to(R)),bytes=len(bundle),sha256=sha(bundle),admission_manifest=str((OUT/'manifest.json').relative_to(R))))
changes=[('S6_SERIES_PUBLISH_II.tex',old,new.encode()),('CHECK_EVENTS.tsv',eb,event_after),('S6_SERIES_PUBLISH_defects_II.tsv',db,defect_after),(str(rp.relative_to(R)),rb,enc(registry))]
OUT.mkdir();(OUT/'inverse.json').write_bytes(enc(inverse));(OUT/'event_rows.tsv').write_bytes(bundle);(OUT/'defect_rows.tsv').write_bytes(tab(added,df))
(OUT/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before editorial proofs02',tofile='II after editorial proofs02')))
manifest=dict(created_utc=now,A_index=bind(index),sealed_bindings_verified=len(ix['files']),source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),
 complete_root_readings='FH original was read in full as the exact3105-byte post-title block earlier in this turn; new2970-byte block read in full. Full old/new XB5008/4813 andXC8853/9164 blocks read, including both outside-proof paragraphs. Complete comparison, preservation program/output, Programs rows, reading/retrieval receipts read.',
 owner_comparisons=comparisons,owner_guards=19,programs_guards=1,all_mutations_exactly_invertible=True,all_labels_tags_statement_record_triples_preserved=True,
 mathematical_preservation='All14 items and20 original displays retained. The homogeneous discriminant assertion now gives Q_h=XU^2+B_hU+C_h, the exact Z=Xw/U=X^2q substitution, and the X^4 residual quadratic factor. Its original integer-bound and monomial-degree equation references move to those proved steps. All four numbered tags and their literal reference tokens remain for D19.',
 program_rows=3,program_link_scope='A successfully opened all three historical sources at the full value of the current SsixRepositoryCommit macro, and five saved outputs; source/output hashes and exact URLs are in the sealed retrieval receipts. No newly created program is claimed to exist remotely.',
 events_added=3,event_types={'used and rechecked in this run':3},evidence_groups=1,ledger_rows_before=len(events),ledger_rows_after=len(events)+3,defect_rows_added=20,
 required_rows_closed=0,global_defect_classes_closed=0,existing_D16_title_projection_unchanged=True,current_header_fingerprint=fingerprint(new),final_pdf_page_credit=0,
 canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a),before_bytes=len(b),after_bytes=len(a)) for n,b,a in changes],
 immutable_evidence=[bind(p) for p in sorted(OUT.iterdir())],code=bind(Path(__file__)))
mp=OUT/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
assert (R/'CHECK_EVENTS.tsv').read_bytes().startswith(eb)
note=f'''\n\n## Paper II: fibre blowups and two local critical-curve proofs — {now}\n\nAdmitted the complete comparative editorial review of01FH,02XB and02XC. Both original program paragraphs following the local proofs are included in the exact guards. All14 proof items and20 original displays remain. The homogeneous discriminant claim now states its weighted input, the exact coordinate substitution and the fourth-order factor in the proof. The remaining file names and output reports move to three historical Programs citations actually opened at the full pinned commit. All four existing manual equation tags and their raw reference tokens remain for D19.\n\nThe admission `{mb['path']}` (SHA-256 `{mb['sha256']}`) adds20 individual defect records and three exposed-reread events in one evidence group. Source SHA-256 `{sha(new.encode())}`; ledger {len(events)+3} rows. The379-header title projection is unchanged, so its existing D16 closure transports exactly. No further global class, required row or final PDF page is closed.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(OUT/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after_bindings=[bind(R/n) for n,_,_ in changes],all_prior_ledger_bytes_preserved=True)))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','owner_guards','programs_guards','events_added','ledger_rows_after','defect_rows_added','existing_D16_title_projection_unchanged','final_pdf_page_credit']},indent=2));print('Manifest:',mb['path'],mb['sha256'])
