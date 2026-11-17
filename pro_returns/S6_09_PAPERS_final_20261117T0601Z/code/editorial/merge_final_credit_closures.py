"""Merge exact scoped final attribution/status overlays, preserving history.

Only supplied inventory fields and explicitly reviewed kind/status repairs are
applied.  The complete previous values remain in the event ledger.  This does
not infer a proof check from a credit search or from the absence of a match.
"""
from pathlib import Path
import csv
import json
import sys
import hashlib

D = Path(__file__).resolve().parents[2]
p = D / 'S6_09_PAPERS_inventory.csv'
before_hash = hashlib.sha256(p.read_bytes()).hexdigest()
with p.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
assert len(fields) == 17 and len(rows) == 1184
index = {(r['source_run'], r['source_id']): r for r in rows}
events = []


def encode(v):
    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)


for arg in sys.argv[1:]:
    source = Path(arg)
    if not source.is_absolute():
        source = D / source
    payload = json.loads(source.read_text())
    overlay = payload if isinstance(payload, list) else payload['rows']
    for item in overlay:
        key = (item['source_run'], item['source_id'])
        row = index[key]
        if item.get('printed_label'):
            assert row['printed_label'] in [item['printed_label'], item.get('alias_label')], key
        before = dict(row)
        for field in ['found_in_AC26', 'found_in_E26', 'found_in_DGKX_v1',
                      'found_elsewhere', 'credited_to', 'your_check', 'check_outcome']:
            if field in item:
                row[field] = encode(item[field])
        if item.get('recommended_kind'):
            row['kind'] = item['recommended_kind']
        elif item.get('kind'):
            row['kind'] = item['kind']
        if 'notes' in item:
            row['notes'] = encode(item['notes'])
        current_mapping = item.get('distinct_proof_current_mapping')
        if current_mapping:
            marker = 'distinct_proof=pending comparison'
            if marker in row['notes']:
                row['notes'] = row['notes'].replace(marker, 'distinct_proof=complete source-to-print comparison; ' + encode(current_mapping))
        note = 'Final scoped credit/status closure: ' + str(source.relative_to(D))
        if item.get('credit_note'):
            note += '; ' + encode(item['credit_note'])
        if item.get('found_in_DGKX_v2'):
            note += '; DGKX v2: ' + encode(item['found_in_DGKX_v2'])
        if current_mapping:
            note += '; complete distinct-proof mapping: ' + encode(current_mapping)
        if note not in row['notes']:
            row['notes'] = (row['notes'] + ' | ' + note).strip(' |')
        if before != row:
            events.append({'source_run': key[0], 'source_id': key[1],
                           'overlay': str(source.relative_to(D)),
                           'before': before, 'after': dict(row),
                           'historical_recorded_checks_unchanged': before['recorded_checks'] == row['recorded_checks']})
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fields)
    writer.writeheader()
    writer.writerows(rows)
record = D / 'records/final_credit_closure_merge.json'
old = json.loads(record.read_text()) if record.exists() else {'events': []}
record.write_text(json.dumps({'rows': len(rows), 'columns': fields,
    'before_sha256': before_hash, 'after_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
    'events': old['events'] + events,
    'remaining_empty_credit_rows': [[r['source_run'], r['source_id']] for r in rows if not r['credited_to']],
    'scope': 'Explicit per-result source searches/openings and prior completed proof mappings only; all prior field values and historical check events retained.'}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'updated_rows': len(events), 'remaining_empty_credit_rows': sum(not r['credited_to'] for r in rows)}))
