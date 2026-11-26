#!/usr/bin/env python3
"""Timed hourly review with actual required completions and source-validated D16 closure."""
from pathlib import Path
import argparse,collections,copy,csv,datetime as dt,hashlib,json
R=Path(__file__).resolve().parents[1]
START=dt.datetime(2026,11,22,3,15,57,tzinfo=dt.timezone.utc)
def sha(b):return hashlib.sha256(b).hexdigest()
def encode(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def read(p):return json.loads(p.read_text())
def update(rows,manifest):
 for row in rows:
  if row['kind']=='required_check' and row['paper']=='II':
   historical_owner=row['id'][len('check:'):]
   owner={'night:P3K.36':'ii:LR:covering'}.get(historical_owner,historical_owner)
   if owner in manifest and row['status']!='done':
    e=manifest[owner];assert e['paper']=='II' and e['status']=='done'
    row['status']='done';row['detail']='done: '+e['scope']
    row['evidence']={k:e[k] for k in ['evidence_path','evidence_sha256']}
    if owner!=historical_owner:
     resolution=R/'records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json'
     row['evidence'].update(current_statement_owner=owner,required_row_disposition=str(resolution.relative_to(R)),required_row_disposition_sha256=sha(resolution.read_bytes()))
def update_defect_classes(rows):
 cp=R/'records/S6_SERIES_PUBLISH_defect_class_completion_manifest.json'
 if not cp.exists():return
 from S6_SERIES_PUBLISH_II_title_census import fingerprint
 manifest=read(cp)['rows'];current_title_hash=fingerprint((R/'S6_SERIES_PUBLISH_II.tex').read_text())
 csv.field_size_limit(100_000_000)
 with (R/'S6_SERIES_PUBLISH_defects_II.tsv').open(newline='') as f:
  defects={x['change_id']:x for x in csv.DictReader(f,delimiter='\t')}
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
def main():
 p=argparse.ArgumentParser();p.add_argument('number',type=int);a=p.parse_args();assert a.number>=14
 due=START+dt.timedelta(hours=a.number-13);now=dt.datetime.now(dt.timezone.utc)
 assert now>=due,'The hourly review is not due.'
 dest=R/'records'/f'S6_SERIES_PUBLISH_progress_review_{a.number:02d}.json';assert not dest.exists()
 current=R/'records/S6_SERIES_PUBLISH_progress_rows_current.json'
 base_comp=read(R.parent/'S6_SERIES_PUBLISH_checkpoint_21/records/S6_SERIES_PUBLISH_required_check_completion_manifest.json')['rows']
 if a.number==14:
  assert not current.exists()
  predecessor=R/'records/S6_SERIES_PUBLISH_progress_review_13.json';old=copy.deepcopy(read(predecessor)['rows'])
  update(old,base_comp);counter=0
  baseline_scope='Checkpoint21 completion manifest applied to the inherited review13 row table; continuation starts with zero reviews without movement.'
 else:
  predecessor=R/'records'/f'S6_SERIES_PUBLISH_progress_review_{a.number-1:02d}.json';prior=read(predecessor)
  assert sha(current.read_bytes())==prior['current_rows_sha256']
  old=read(current)['rows'];counter=prior['consecutive_reviews_without_movement'];baseline_scope='Previous immutable review and its exact current-row hash.'
 rows=copy.deepcopy(old)
 additional=R/'records/S6_SERIES_PUBLISH_additional_required_checks_II.json'
 if additional.exists():
  existing={x['id'] for x in rows}
  for item in read(additional)['rows']:
   if item['id'] not in existing:
    assert item['status']=='open' and item['kind']=='required_check' and item['paper']=='II'
    bound=item['evidence'];assert sha((R/bound['path']).read_bytes())==bound['sha256']
    rows.append(copy.deepcopy(item));existing.add(item['id'])
 manifest=read(R/'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json')['rows']
 for owner,e in manifest.items():
  if e['paper']=='II' and owner not in base_comp:assert sha((R/e['evidence_path']).read_bytes())==e['evidence_sha256'],owner
 update(rows,manifest)
 update_defect_classes(rows)
 # Enumerated claims supplement the still-open inventory gate. Mere discovery
 # or a wording change earns no movement; closure needs a separate reviewed gate.
 known={x['id']:x for x in rows}
 csv.field_size_limit(100_000_000)
 with (R/'S6_SERIES_PUBLISH_provenance_checks.tsv').open(newline='') as f:
  for claim in csv.DictReader(f,delimiter='\t'):
   if claim['paper']!='II':continue
   rid='provenance:II:'+claim['claim_id']
   if rid not in known:
    row=dict(id=rid,kind='provenance',paper='II',status='open',title=claim['claim'],detail=claim['resolution_status']+'; '+claim['remaining_gate'],evidence=dict(path='S6_SERIES_PUBLISH_provenance_checks.tsv',claim_id=claim['claim_id']))
    rows.append(row);known[rid]=row
 assert len({x['id'] for x in rows})==len(rows)
 oldby={x['id']:x for x in old};changes=[{'id':x['id'],'before':oldby.get(x['id']),'after':x} for x in rows if x!=oldby.get(x['id'])]
 newly_done=[x['id'] for x in rows if x['status']=='done' and x['id'] in oldby and oldby[x['id']]['status']!='done']
 administrative_resolutions=[x for x in newly_done if x=='check:night:P3K.36']
 newly_done=[x for x in newly_done if x not in administrative_resolutions]
 movement=bool(newly_done);counter=0 if movement else counter+1
 counts={}
 for row in rows:counts.setdefault(row['paper'],{}).setdefault(row['kind'],collections.Counter())[row['status']]+=1
 current_payload={'schema':'continuation2-current-progress-rows','recorded_utc':now.isoformat(),'rows':rows,'row_counts':counts,'scope':'Papers I and V retain their closed gates. Paper II is current. Other rows are held at their inherited states. PDF page and provenance inventory gates remain open until actual candidates and a complete claim inventory are established; individual enumerated provenance claims are recorded separately.'}
 payload=encode(current_payload)
 snapshot=dict(review=a.number,scheduled_utc=due.isoformat(),recorded_utc=now.isoformat(),continuation_start_utc=START.isoformat(),
  previous_snapshot=str(predecessor.relative_to(R)),previous_snapshot_sha256=sha(predecessor.read_bytes()),baseline_scope=baseline_scope,
  previous_rows_sha256=sha(encode(old)),current_rows_path=str(current.relative_to(R)),current_rows_sha256=sha(payload),row_counts=counts,
  exact_row_changes=changes,administrative_resolved_owner_rows=administrative_resolutions,newly_done_rows=newly_done,movement_since_previous_review=movement,consecutive_reviews_without_movement=counter,mandatory_stop=counter>=2,
  current_II_source_sha256=sha((R/'S6_SERIES_PUBLISH_II.tex').read_bytes()),ledger_sha256=sha((R/'CHECK_EVENTS.tsv').read_bytes()),
  main_gate='Complete Paper II checks, all25 defect classes, restructuring, provenance, build and all final page readings; then III, then IV, then final five-paper integration. I and V remain closed until that integration.',
  movement_rule='Only an open row reaching done or a proved strictly smaller main gate qualifies. Counts, wording activity and checkpoint packaging add no movement. No gate reduction is claimed in this review.',
  mathematical_events_added=0,page_reading_credit=0)
 current.write_bytes(payload);dest.write_bytes(encode(snapshot))
 text=f'\n\n## Scheduled progress review {a.number:02d} — {now.isoformat()}\n\n'
 text+=f'{len(newly_done)} open rows reached done in this interval. Consecutive reviews without movement: {counter}. The dated current row table is `{current.relative_to(R)}`; its exact hash and all changed rows are recorded in `{dest.relative_to(R)}`. The attached base and these deltas retain the preceding states without full per-review copies.\n\n'
 text+=snapshot['main_gate']+'\n\n| Paper | Required checks done | Required checks open | Defect types open | Page reading | Provenance |\n|---|---:|---:|---:|---|---|\n'
 for paper in ['I','II','III','IV','V']:
  c=counts[paper];checks=c.get('required_check',{});pages=c.get('page',{});prov=c.get('provenance',{})
  text+=f"| {paper} | {checks.get('done',0)} | {checks.get('open',0)} | {c.get('defect',{}).get('open',0)} | {'held closed' if paper in ['I','V'] else 'open; candidate pending'} | {'held closed' if paper in ['I','V'] else 'open'} |\n"
 if administrative_resolutions:text+='\nAdministrative required-owner reconciliation, excluded from new movement: '+', '.join(administrative_resolutions)+'. See records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json; the historical compound claim remains refuted.\n'
 text+='\nNewly completed rows: '+(', '.join('`'+x+'`' for x in newly_done) if newly_done else 'none')+'.\n'
 nextdue=due+dt.timedelta(hours=1);text+=f'\nNext review: {nextdue.isoformat()}. Checkpoint packaging remains on its separate45-minute schedule.\n'
 if counter>=2:text+='\nThe mandatory two-review stop rule is triggered. The final package must state the exact incomplete status.\n'
 for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
  q=R/name;q.write_bytes(q.read_bytes()+text.encode())
 print(json.dumps({k:snapshot[k] for k in ['review','newly_done_rows','movement_since_previous_review','consecutive_reviews_without_movement','mandatory_stop','row_counts']},indent=2))
if __name__=='__main__':main()
