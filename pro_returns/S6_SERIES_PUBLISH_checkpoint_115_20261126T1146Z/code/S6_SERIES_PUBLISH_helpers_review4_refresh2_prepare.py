#!/usr/bin/env python3
"""Create distinct reviewed helpers for class validity and the02UH resolution metadata."""
from pathlib import Path
import datetime as dt,difflib,hashlib,json
R=Path(__file__).resolve().parents[1]
OUT=R/'records/S6_SERIES_PUBLISH_helpers_review4_refresh2'
assert not OUT.exists()
sha=lambda b:hashlib.sha256(b).hexdigest()
updates=[]
oldp=R/'code/S6_SERIES_PUBLISH_continuation2_progress_review_v3.py';before=oldp.read_bytes();s=before.decode()
insert='''def update_defect_classes(rows):
 cp=R/'records/S6_SERIES_PUBLISH_defect_class_completion_manifest.json'
 if not cp.exists():return
 from S6_SERIES_PUBLISH_II_title_census import fingerprint
 manifest=read(cp)['rows'];current_title_hash=fingerprint((R/'S6_SERIES_PUBLISH_II.tex').read_text())
 csv.field_size_limit(100_000_000)
 with (R/'S6_SERIES_PUBLISH_defects_II.tsv').open(newline='') as f:
  defects={x['change_id']:x for x in csv.DictReader(f,delimiter='\\t')}
 for row in rows:
  if row['id'] not in manifest:continue
  e=manifest[row['id']];assert e['paper']=='II' and e['defect_type']=='D16' and e['status']=='done'
  assert row['kind']=='defect' and row['paper']=='II'
  assert sha((R/e['evidence_path']).read_bytes())==e['evidence_sha256']
  assert sha((R/e['log_index_path']).read_bytes())==e['log_index_sha256']
  for item in read(R/e['log_index_path']):
   assert sha(encode(defects[item['change_id']]))==item['canonical_row_sha256']
  valid=current_title_hash==e['header_fingerprint']
  row['status']='done' if valid else 'open'
  row['detail']=('done: '+e['scope']) if valid else 'open: the complete current title projection changed after the recordedD16 audit; a new explicit title audit is required.'
  row['evidence']={k:e[k] for k in ['evidence_path','evidence_sha256','header_fingerprint','log_index_path','log_index_sha256']}
  row['evidence']['current_header_fingerprint']=current_title_hash
'''
assert s.count('def main():')==1
s=s.replace('def main():',insert+'def main():',1)
assert s.count(' update(rows,manifest)\n')==1
s=s.replace(' update(rows,manifest)\n',' update(rows,manifest)\n update_defect_classes(rows)\n',1)
s=s.replace('"""Timed hourly review, including additional discovered-error gates, with immutable exact deltas."""','"""Timed hourly review with actual required completions and source-validated D16 closure."""',1)
updates.append((oldp,R/'code/S6_SERIES_PUBLISH_continuation2_progress_review_v4.py',before,s.encode()))
oldp=R/'code/S6_SERIES_PUBLISH_continuation2_refresh_II_deliverables.py';before=oldp.read_bytes();s=before.decode()
old="  if label in counts:row['current_statement_owner']=counts[label]['current_statement_owner']\n"
new="""  if label in counts:row['current_statement_owner']=counts[label]['current_statement_owner']
  if label=='night:P3K.36' and 'editorial_anchor_disposition_20261122' in record:
   resolution_path=R/'records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json'
   resolution=json.loads(resolution_path.read_text());assert resolution['printed_owner']=='ii:LR:covering'
   assert row['status']=='false as stated'
   record['current_printed_anchor_owner']=counts[label]['current_statement_owner']
   record['required_check_resolution_owner']=resolution['printed_owner']
   record['required_check_resolution_record']=str(resolution_path.relative_to(R))
   record['required_check_resolution_sha256']=sha(resolution_path.read_bytes())
   record['owner_field_scope']='The current_statement_owner field preserves the recorded required-check disposition to the proved retained covering subclaim. The current_printed_anchor_owner identifies the reference remark. These fields assert no equality between the historical compound claim and the covering theorem.'
   row['current_statement_owner']=resolution['printed_owner']
   row['check_record']=json.dumps(record,ensure_ascii=False)
"""
assert s.count(old)==1;s=s.replace(old,new,1)
updates.append((oldp,R/'code/S6_SERIES_PUBLISH_continuation2_refresh_II_deliverables_v2.py',before,s.encode()))
OUT.mkdir();receipts=[]
for oldp,newp,b,a in updates:
 assert not newp.exists();assert oldp.read_bytes()==b;compile(a.decode(),str(newp),'exec');newp.write_bytes(a)
 dp=OUT/(newp.name+'.diff');dp.write_text(''.join(difflib.unified_diff(b.decode().splitlines(True),a.decode().splitlines(True),fromfile=str(oldp.relative_to(R)),tofile=str(newp.relative_to(R)))))
 receipts.append(dict(original_path=str(oldp.relative_to(R)),original_sha256=sha(b),new_path=str(newp.relative_to(R)),new_sha256=sha(a),diff_path=str(dp.relative_to(R)),diff_sha256=sha(dp.read_bytes())))
record=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),scope='Original helpers retained byte-identically. Review4 validates full-header projection and every D16 log-row hash, reopening the class after header changes. Refresh2 preserves the historical02UH required-owner resolution and separately records its printed reference-remark owner; no statement equality or extra event association is introduced.',helpers=receipts,canonical_data_mutations=0,code_sha256=sha(Path(__file__).read_bytes()))
(OUT/'receipt.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
