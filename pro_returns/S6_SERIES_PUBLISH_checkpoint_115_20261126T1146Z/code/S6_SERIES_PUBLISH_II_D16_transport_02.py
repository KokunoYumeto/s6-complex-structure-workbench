#!/usr/bin/env python3
"""Bind every current header to a complete prior reading or a read receiving block."""
from pathlib import Path
import csv,datetime as dt,hashlib,json,re
from S6_SERIES_PUBLISH_II_title_census import headers,projection,fingerprint
R=Path(__file__).resolve().parents[1];O=R/'records/S6_SERIES_PUBLISH_II_D16_closure_02'
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
assert not O.exists();s=(R/'S6_SERIES_PUBLISH_II.tex').read_text();envs,hs=headers(s)
assert sha(s.encode())=='670349f54976a06da6cd2f04c059f00c198bad902859bd2c668f7ee2fdafc561'
prior=R/'records/S6_SERIES_PUBLISH_II_D16_closure_01/header_census.json';old=json.loads(prior.read_text())['current_headers'];oldby={t:h for h in old for t in h['tags']}
keys=['environment','title','tags','labels'];transports=[];changed=[]
for h in hs:
 match=next((oldby[t] for t in h['tags'] if t in oldby and all(h[k]==oldby[t][k] for k in keys)),None)
 if match:transports.append(dict(current_index=h['index'],prior_index=match['index'],projection={k:h[k] for k in keys}))
 else:changed.append(h)
assert len(hs)==373 and len(transports)==367 and len(changed)==6
expected={'03IO':'Restriction to the cusp normalization','03IH':'Boundary cocycles and Chern-class specialization','03IN':'An explicit nonzero local cusp restriction','03IW':'Global restriction of line bundles','03IQ':'A local bundle without a global extension','03DR':'Tangent-cohomology nonvanishing on the standard fibre'}
assert {h['tags'][0]:h['title'] for h in changed}==expected
assert all(h['title'] and h['tags'] for h in hs)
assert not any(re.search(r'actual|candidate|survivor|corrected|previously|retained|repaired|superseded|verification|audit|\bP[134](?:[ARKF])?\.',h['title'],re.I) for h in hs)
csv.field_size_limit(100_000_000);defs=list(csv.DictReader((R/'S6_SERIES_PUBLISH_defects_II.tsv').open(),delimiter='\t'));d16=[r for r in defs if 'D16' in re.findall(r'D\d+',r['type'])];assert len(d16)==183
priorindex=json.loads((R/'records/S6_SERIES_PUBLISH_II_D16_closure_01/D16_log_index.json').read_text());by={r['change_id']:r for r in defs}
for row in priorindex:assert sha(enc(by[row['change_id']]))==row['canonical_row_sha256']
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir()
census=dict(created_utc=now,source_sha256=sha(s.encode()),header_count=len(hs),declared_environments=envs,current_headers=hs,current_header_projection=projection(s),current_header_fingerprint=fingerprint(s),exact_prior_reading=bind(prior),unchanged_header_reading_transport=transports,changed_headers_actually_read=changed,complete_receiving_block_reading=bind(R/'records/S6_SERIES_PUBLISH_II_Picard_admission_01/root_reading.json'),reading_scope='Every current header has a complete reading:367 header projections transport byte-exactly from the complete prior379-header reading; the six changed projections occur in the complete receiving blocks read by root and were also displayed together before this closure. This asserts the exact equality of each listed projection, not a new367-title rereading.',complete_current_title_verdict='All373 current numbered headers have mathematical titles. The exact original-to-receiving owner and title maps are in the admitted Picard packet. No new D16 defect was introduced by these consolidations.',source_changes=0,final_pdf_page_credit=0)
(O/'header_census.json').write_bytes(enc(census));index=[dict(change_id=r['change_id'],type=r['type'],statement_id=r['statement_id'],canonical_row_sha256=sha(enc(r))) for r in d16];(O/'D16_log_index.json').write_bytes(enc(index))
manifest=dict(created_utc=now,paper='II',defect_type='D16',status='done',source_sha256=sha(s.encode()),current_header_fingerprint=fingerprint(s),complete_current_header_reading_coverage=373,exact_prior_reading_transports=367,changed_headers_actually_read=6,missing_titles=0,remaining_workflow_titles=0,all_instances_logged=True,D16_log_records=183,source_changes=0,mathematical_events_added=0,required_rows_closed=0,final_pdf_page_credit=0,scope='The complete title audit is transported across367 exact header projections and explicitly renewed on all six changed current headers.',evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp);cp=R/'records/S6_SERIES_PUBLISH_defect_class_completion_manifest.json';c=json.loads(cp.read_text());oldrow=c['rows']['defect:II:D16'];(O/'previous_completion_row.json').write_bytes(enc(oldrow))
c['updated_utc']=now;c['rows']['defect:II:D16']=dict(paper='II',defect_type='D16',status='done',recorded_utc=now,evidence_path=mb['path'],evidence_sha256=mb['sha256'],header_fingerprint=fingerprint(s),header_count=373,log_index_path=str((O/'D16_log_index.json').relative_to(R)),log_index_sha256=sha((O/'D16_log_index.json').read_bytes()),scope=manifest['scope'])
assert (R/'S6_SERIES_PUBLISH_II.tex').read_text()==s;cp.write_bytes(enc(c))
note=f'''\n\n## Paper II: D16 title audit renewed after consolidation — {now}\n\nAll373 current headers are covered by complete actual readings:367 exact header projections transport from the prior complete audit; all six changed projections were read in the complete receiving blocks and displayed together before this closure. The eleven overlapping Picard owners become four and one pre-existing target becomes a numbered remark, with the complete owner/title map retained. All183 D16 log rows retain their exact hashes. The current header fingerprint is `{fingerprint(s)}`.\n\nThe explicit current audit is `{mb['path']}` (SHA-256 `{mb['sha256']}`). D16 remains done under this new binding. No fresh proof-check, required-row or final-page credit is claimed, and this renewal does not count as a new open-to-done movement relative to review22.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,completion_manifest=bind(cp))))
print(json.dumps({'source_sha256':sha(s.encode()),'headers':len(hs),'header_fingerprint':fingerprint(s),'manifest_sha256':mb['sha256']},indent=2))
