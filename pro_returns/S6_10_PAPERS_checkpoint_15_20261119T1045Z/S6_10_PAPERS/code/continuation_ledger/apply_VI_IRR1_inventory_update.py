#!/usr/bin/env python3
"""Apply the VI owner's exact receiving Uses and proof-scope metadata."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

csv.field_size_limit(16 * 1024 * 1024)
P = Path(__file__).resolve().parents[2]
source = P / 'analysis/continuation_VI/IRR1_inventory_update.json'
receipt = P / 'analysis/continuation_ledger/IRR1_inventory_update_receipt.json'
inventory = P / 'S6_10_PAPERS_inventory.csv'
update = json.loads(source.read_text())
with inventory.open(newline='') as f:
    reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
changes=[]
for row in rows:
    if row['label'] != update['label']: continue
    notes = json.loads(row['notes'])
    value={'source':str(source.relative_to(P)), 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(), 'proof_scope':update['proof_scope']}
    if row['uses'] == update['uses'] and notes.get('continuation_owner_inventory_scope') == value:
        continue
    changes.append({'label':row['label'],'source_run':row['source_run'],'source_id':row['source_id'],
                    'before_uses':row['uses'],'after_uses':update['uses'],
                    'before_owner_scope':notes.get('continuation_owner_inventory_scope'),'after_owner_scope':value})
    row['uses']=update['uses'];notes['continuation_owner_inventory_scope']=value
    row['notes']=json.dumps(notes,ensure_ascii=False)
if changes:
    old=inventory.read_bytes()
    with inventory.open('w',newline='') as f:
        w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
    record={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'before_inventory_sha256':hashlib.sha256(old).hexdigest(),
            'after_inventory_sha256':hashlib.sha256(inventory.read_bytes()).hexdigest(),'changes':changes,
            'scope':'Explicit VI-owner Uses/scope receipt only; no mathematical gate inferred by this transport.'}
    if receipt.exists():
        history=json.loads(receipt.read_text());history.setdefault('later_applications',[]).append(record);record=history
    receipt.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changed_rows':len(changes),'receipt':str(receipt)}))
