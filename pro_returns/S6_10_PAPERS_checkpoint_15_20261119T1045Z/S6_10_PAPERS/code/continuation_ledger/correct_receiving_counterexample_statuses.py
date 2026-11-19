#!/usr/bin/env python3
"""Assign status to the assertion actually printed in four receiving rows.

The rejected earlier positive claims keep their Refuted provenance. This
metadata operation awards no continuation mathematical check or gate.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

csv.field_size_limit(16*1024*1024)
ROOT=Path(__file__).resolve().parents[2]
AUDIT=ROOT/'analysis/continuation_ledger'
sha=lambda b:hashlib.sha256(b).hexdigest()
reasons={
 'push:src:C.5.1':'The printed corollary asserts the proved exclusion of the specified analytic filling and its Chern-data request, together with the established zero physical return. Its earlier rejected analytic-filling premise retains false-as-stated provenance. The pre-continuation targeted event explicitly checked this negative implication and the actual smooth-boundary computations; no fresh complete proof is claimed by this status correction.',
 'maps:src:B.6.7':'The printed proposition is the proved ordinary scalar-shear obstruction/counterexample, including the exact order-six quotient defect. The rejected positive shear-homotopy assertion remains false as stated. The pre-continuation targeted event records the full semidirect-product/coboundary calculation and rational solution (1/6,0,0), Smith factors (1,1,6); this metadata correction adds no new proof review.'}
v_source=ROOT/'analysis/continuation_V/receiving_status_correction.json'
reasons.update(json.loads(v_source.read_text())['reasons'])
reasons['night:P2.11']='Root verified that the current Paper I receiving assertion is the proved negative smoothing obstruction: the specified one-component central space has virtual Euler number zero whereas the proposed smooth fibre has Euler number two. The inherited Refuted status belongs to the rejected positive smoothing claim. The source Refuted provenance remains preserved and all current renewal gates remain separate.'
receipt_path=AUDIT/'receiving_counterexample_status_corrections.json'
previous=json.loads(receipt_path.read_text()) if receipt_path.exists() else {}
changes=[]
for rel in ['papers/IV/body.tex','papers/IV/body_source.tex']:
 path=ROOT/rel;before=path.read_bytes();text=before.decode();patches=[]
 for label in ['push:src:C.5.1','maps:src:B.6.7']:
  old='\\StatementRecord{'+label+'}{false as stated}'
  new='\\StatementRecord{'+label+'}{proved}'
  if old in text:
   assert text.count(old)==1;text=text.replace(old,new,1);patches.append({'before':old,'after':new})
  else:assert text.count(new)==1
 if patches:
  path.write_text(text);changes.append({'file':rel,'before_sha256':sha(before),'after_sha256':sha(text.encode()),'patches':patches})
override_path=AUDIT/'owner_overrides.json';overrides=json.loads(override_path.read_text())
old_overrides={label:overrides.get(label) for label in reasons}
for label,reason in reasons.items():
 overrides[label]={'status':'proved','basis':reason,'scope':'The assertion actually printed is the counterexample/negative/corrected conclusion. Original source Refuted fields and old status history remain unchanged. No renewed gate is awarded by this metadata operation.',
                   'authority':('IV receiving-status audit of exact printed assertions and earlier targeted events' if label in ['push:src:C.5.1','maps:src:B.6.7'] else 'Explicit root Paper I owner verification and correction instruction, 19 November 2026' if label=='night:P2.11' else 'Explicit V owner correction: analysis/continuation_V/receiving_status_correction.json')}
override_path.write_text(json.dumps(overrides,ensure_ascii=False,indent=2)+'\n')
inventory=ROOT/'S6_10_PAPERS_inventory.csv'
with inventory.open(newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
inventory_changes=[]
for row in rows:
 if row['label'] not in reasons:continue
 notes=json.loads(row['notes']);label=row['label']
 value={'rejected_earlier_claim_status':'false as stated','receiving_assertion_status':'proved','reason':reasons[label],
        'receipt':'analysis/continuation_ledger/receiving_counterexample_status_corrections.json','new_proof_gate_awarded':False}
 if notes.get('continuation_receiving_counterexample_status')!=value:
  inventory_changes.append({'label':label,'previous_status':row['status'],'new_status':'proved','previous_note':notes.get('continuation_receiving_counterexample_status')})
  notes['continuation_receiving_counterexample_status']=value;row['notes']=json.dumps(notes,ensure_ascii=False)
 # Reconciler applies the status itself and retains an exact status-history row.
with inventory.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
if not previous:
 previous={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'source_changes':changes,'inventory_notes':inventory_changes,'old_owner_overrides':old_overrides,'reasons':reasons,
           'scope':'Receiving assertion/status alignment only. The asserted counterexamples already had recorded proofs; no new mathematical conclusion or current proof gate follows from this operation.'}
else:
 previous['source_changes'].extend(changes);previous['inventory_notes'].extend(inventory_changes)
 previous['reasons'].update(reasons)
receipt_path.write_text(json.dumps(previous,ensure_ascii=False,indent=2)+'\n')
event_path=ROOT/'records/continuation_IV_events.tsv'
with event_path.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');event_fields=r.fieldnames;events=list(r)
for label in ['push:src:C.5.1','maps:src:B.6.7']:
 outcome='Receiving assertion/status alignment: '+reasons[label]+' Receipt: analysis/continuation_ledger/receiving_counterexample_status_corrections.json. Original raw Refuted fields are preserved; metadata reconciliation only; no new mathematical check.'
 if not any(e['statement_id']==label and e['outcome']==outcome for e in events):
  events.append({'statement_id':label,'date':'2026-11-19','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation','type':'used and rechecked in this run','outcome':outcome})
with event_path.open('w',newline='') as f:w=csv.DictWriter(f,event_fields,delimiter='\t');w.writeheader();w.writerows(events)
print(json.dumps({'receiving_labels':list(reasons),'source_files_changed':len(changes),'receipt':str(receipt_path)},indent=2))
