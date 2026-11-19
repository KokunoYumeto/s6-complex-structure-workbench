#!/usr/bin/env python3
"""Retain exact renewed owner evidence without replacing named attributions."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json

csv.field_size_limit(16*1024*1024)
P=Path(__file__).resolve().parents[2]
source=P/'analysis/continuation_V/inventory_credit_updates.tsv'
raw=source.read_bytes();updates=list(csv.DictReader(raw.decode().splitlines(),delimiter='\t'))
inventory=P/'S6_10_PAPERS_inventory.csv';before=inventory.read_bytes()
with inventory.open(newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
by={u['label']:u for u in updates};changes=[];old_credits=[r['credited_to'] for r in rows]
for row in rows:
 if row['label'] not in by:continue
 update=by[row['label']];notes=json.loads(row['notes'])
 entry={'source':str(source.relative_to(P)),'source_sha256':hashlib.sha256(raw).hexdigest(),
        'raw_owner_record':update,'scope':'The exact owner renewal record is appended. Existing named-credit text is retained verbatim; this transport awards no additional proof or source check.'}
 records=notes.setdefault('continuation_renewed_owner_credit_records',[])
 if entry in records:continue
 records.append(entry);row['notes']=json.dumps(notes,ensure_ascii=False)
 changes.append({'label':row['label'],'source_run':row['source_run'],'source_id':row['source_id'],
                 'preserved_credited_to_sha256':hashlib.sha256(row['credited_to'].encode()).hexdigest(),'appended_record':entry})
assert old_credits==[r['credited_to'] for r in rows]
if changes:
 with inventory.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
 receipt=P/'analysis/continuation_ledger/owner_credit_note_append_receipt.json'
 payload={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'source':str(source.relative_to(P)),
          'before_inventory_sha256':hashlib.sha256(before).hexdigest(),'after_inventory_sha256':hashlib.sha256(inventory.read_bytes()).hexdigest(),
          'all_existing_credited_to_values_identical':True,'appended_rows':changes,'new_mathematical_check_awarded':False}
 if receipt.exists():
  prior=json.loads(receipt.read_text());prior.setdefault('later_applications',[]).append(payload);payload=prior
 receipt.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'appended_rows':len(changes),'named_credit_fields_preserved':True}))
