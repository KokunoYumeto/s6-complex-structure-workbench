#!/usr/bin/env python3
"""Transport the explicit V replacement's dependency/credit fields reversibly."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
csv.field_size_limit(16*1024*1024)
P=Path(__file__).resolve().parents[2]
source=P/'analysis/continuation_V/inventory_batch14_updates.tsv'
raw=source.read_bytes();updates={r['label']:r for r in csv.DictReader(raw.decode().splitlines(),delimiter='\t')}
inventory=P/'S6_10_PAPERS_inventory.csv';before=inventory.read_bytes()
with inventory.open(newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
changes=[]
for row in rows:
 label=row['label'];notes=json.loads(row['notes'])
 if label in updates:
  u=updates[label]
  if row['uses']!=u['uses'] or row['credited_to'].split(' | Sweep1 cross-run comparison: ')[0]!=u['credited_to']:
   old={'uses':row['uses'],'credited_to':row['credited_to']}
   change={'label':label,'source_run':row['source_run'],'source_id':row['source_id'],'old_fields':old,
    'new_fields':{'uses':u['uses'],'credited_to':u['credited_to']},'raw_owner_update':u,
    'source':str(source.relative_to(P)),'source_sha256':hashlib.sha256(raw).hexdigest()}
   notes.setdefault('continuation_superseded_owner_inventory_fields',[]).append(change)
   row['uses']=u['uses'];row['credited_to']=u['credited_to'];changes.append(change)
 if label=='cdp:st:A.1.1':
  entry={'source':'analysis/continuation_II_ledger/A1_1_comparison.md',
   'source_sha256':hashlib.sha256((P/'analysis/continuation_II_ledger/A1_1_comparison.md').read_bytes()).hexdigest(),
   'scope':'Renewed exact AC26 pp86-90 comparison through N*,V,T,Q and ker(delta); general conormal and long-exact mechanisms credited as classical by opened primary Stacks01UM/01DZ and Gathmann15.10/16.8 sources. Prior rich named AC26 attribution is retained verbatim.',
   'source_search':'analysis/continuation_II_ledger/A1_1_renewed_credit_search.json'}
  records=notes.setdefault('continuation_renewed_owner_credit_records',[])
  if entry not in records:records.append(entry);changes.append({'label':label,'appended_credit_receipt':entry,'credited_to_preserved_verbatim':True})
 row['notes']=json.dumps(notes,ensure_ascii=False)
if changes:
 with inventory.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
 receipt=P/'analysis/continuation_ledger/owner_batch14_inventory_transport.json'
 payload={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'before_inventory_sha256':hashlib.sha256(before).hexdigest(),
  'after_inventory_sha256':hashlib.sha256(inventory.read_bytes()).hexdigest(),'changes':changes,
  'scope':'Explicit current replacement Uses and credit fields only; exact prior fields retained in notes and receipt. This transport awards no new mathematical check.'}
 if receipt.exists():
  previous=json.loads(receipt.read_text());previous.setdefault('later_applications',[]).append(payload);payload=previous
 receipt.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'changed_records':len(changes),'source':str(source)}))
