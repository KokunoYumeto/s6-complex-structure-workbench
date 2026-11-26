#!/usr/bin/env python3
"""Renew all current title readings after the combined nodal proposition."""
from pathlib import Path
import csv,datetime as dt,hashlib,json,re
from S6_SERIES_PUBLISH_II_title_census import headers,projection,fingerprint
R=Path(__file__).resolve().parents[1];O=R/'records/S6_SERIES_PUBLISH_II_D16_closure_05'
sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
assert not O.exists();s=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
assert sha(s.encode())=='0fdba09975c85603db9c7dba958aa5db2a7271c02b680ed67dffc5abaf50afb1'
envs,hs=headers(s);prior=R/'records/S6_SERIES_PUBLISH_II_D16_closure_04/header_census.json'
old=json.loads(prior.read_text())['current_headers'];oldby={t:h for h in old for t in h['tags']}
keys=['environment','title','tags','labels'];transports=[];changed=[]
for h in hs:
 match=next((oldby[t] for t in h['tags'] if t in oldby and all(h[k]==oldby[t][k] for k in keys)),None)
 if match:transports.append(dict(current_index=h['index'],prior_index=match['index'],projection={k:h[k] for k in keys}))
 else:changed.append(h)
assert len(hs)==373 and len(transports)==372 and len(changed)==1
assert {h['tags'][0]:h['title'] for h in changed}=={'01BK':'A complete nodal-family computation'}
assert all(h['title'] and h['tags'] for h in hs)
assert not any(re.search(r'actual|candidate|survivor|corrected|previously|retained|repaired|superseded|verification|audit|\bP[134](?:[ARKF])?\.',h['title'],re.I) for h in hs)
csv.field_size_limit(100_000_000);defs=list(csv.DictReader((R/'S6_SERIES_PUBLISH_defects_II.tsv').open(),delimiter='\t'))
d16=[r for r in defs if 'D16' in re.findall(r'D\d+',r['type'])];assert len(d16)==183
by={r['change_id']:r for r in defs}
for row in json.loads((R/'records/S6_SERIES_PUBLISH_II_D16_closure_04/D16_log_index.json').read_text()):assert sha(enc(by[row['change_id']]))==row['canonical_row_sha256']
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir()
census=dict(created_utc=now,source_sha256=sha(s.encode()),header_count=len(hs),declared_environments=envs,current_headers=hs,current_header_projection=projection(s),current_header_fingerprint=fingerprint(s),exact_prior_reading=bind(prior),unchanged_header_reading_transport=transports,changed_headers_actually_read=changed,complete_receiving_block_reading=bind(R/'records/S6_SERIES_PUBLISH_II_nodal_admission_01/root_reading.json'),reading_scope='All372 surviving prior full header projections transport exactly. The complete old and receiving B1 statements/proofs were read before admission, and its sole changed projection was displayed and read after admission. The two former lemma headers become permanent aliases within B1; their mathematical claims are transported by the exact maps in the admission.',complete_current_title_verdict='All373 current numbered headers have mathematical titles; no remaining title defect.',source_changes=0,final_pdf_page_credit=0)
(O/'header_census.json').write_bytes(enc(census))
index=[dict(change_id=r['change_id'],type=r['type'],statement_id=r['statement_id'],canonical_row_sha256=sha(enc(r))) for r in d16];(O/'D16_log_index.json').write_bytes(enc(index))
manifest=dict(created_utc=now,paper='II',defect_type='D16',status='done',source_sha256=sha(s.encode()),current_header_fingerprint=fingerprint(s),complete_current_header_reading_coverage=373,exact_prior_reading_transports=372,changed_headers_actually_read=1,missing_titles=0,remaining_workflow_titles=0,all_instances_logged=True,D16_log_records=183,source_changes=0,mathematical_events_added=0,required_rows_closed=0,final_pdf_page_credit=0,scope='Complete title audit transported across372 exact projections and explicitly renewed for the changed B1 receiving proposition and its exact old-lemma aliases.',evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
cp=R/'records/S6_SERIES_PUBLISH_defect_class_completion_manifest.json';before=cp.read_bytes();c=json.loads(before)
(O/'previous_completion_row.json').write_bytes(enc(c['rows']['defect:II:D16']))
c['updated_utc']=now;c['rows']['defect:II:D16']=dict(paper='II',defect_type='D16',status='done',recorded_utc=now,evidence_path=mb['path'],evidence_sha256=mb['sha256'],header_fingerprint=fingerprint(s),header_count=373,log_index_path=str((O/'D16_log_index.json').relative_to(R)),log_index_sha256=sha((O/'D16_log_index.json').read_bytes()),scope=manifest['scope'])
assert cp.read_bytes()==before and (R/'S6_SERIES_PUBLISH_II.tex').read_text()==s;cp.write_bytes(enc(c))
note=f'\n\n## Paper II: D16 title audit after nodal consolidation — {now}\n\nAll373 current headers have complete actual reading coverage:372 exact prior projections and the explicitly read changed B1 projection. All183 D16 log records retain their exact hashes. Current header fingerprint `{fingerprint(s)}`. Manifest `{mb["path"]}` (SHA-256 `{mb["sha256"]}`). D16 remains done under this binding; no new movement relative to review23, mathematical event or final-page credit is asserted.\n'
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,completion_manifest=bind(cp))))
print(json.dumps(dict(headers=len(hs),fingerprint=fingerprint(s),manifest_sha256=mb['sha256']),indent=2))
