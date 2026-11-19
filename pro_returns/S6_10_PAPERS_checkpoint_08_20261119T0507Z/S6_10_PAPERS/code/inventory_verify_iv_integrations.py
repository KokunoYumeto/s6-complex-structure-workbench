#!/usr/bin/env python3
"""Verify exact receiving repairs and close only their recorded editing gates.

No proof event is created, no original review date is changed, and no layout or
cross-reference certification is inferred from text matching.
"""
import csv
import datetime
import hashlib
import json
import re
from pathlib import Path
from inventory_reconcile import TexIndex

W = Path(__file__).resolve().parents[1]
body = W / 'papers/IV/body.tex'
index = TexIndex(body.resolve())
at = datetime.datetime.now(datetime.timezone.utc).isoformat()
record = 'analysis/inventory_iv_receiving_integration_verification.json'
checks = []
blocks = {}


def block(label):
    if label not in blocks:
        location = index.locate(label)
        assert location['found'], label
        blocks[label] = index.text[location['start']:location['end']]
    return blocks[label]


def exact(patch, source):
    text = block(patch['label'])
    old, new = patch['exact_old'], patch['exact_new']
    count = text.count(new)
    assert count == 1, (patch['id'], 'replacement count', count)
    unreplaced = text.replace(new, '').count(old)
    assert unreplaced == 0, (patch['id'], 'unreplaced old', unreplaced)
    checks.append(dict(id=patch['id'], label=patch['label'],
                       replacement_source=source, exact_new_count=count,
                       old_outside_replacement_count=unreplaced,
                       receiving_block_sha256=hashlib.sha256(text.encode()).hexdigest()))


retained_path = 'analysis/IV_retained_batch/receiving_replacements.json'
for patch in json.loads((W / retained_path).read_text()):
    exact(patch, retained_path)

k107_path = 'analysis/IV_K107_cp30/receiving_replacements.json'
k107 = json.loads((W / k107_path).read_text())
for patch in k107['new_replacements'] + [k107['retained_receiving_replacement']]:
    exact(patch, k107_path)
assert r"\vartheta(Q):=\Theta'_Q(1)" in block('night:P3K.107')
assert 'TU.4. Exact scope of the repair' in block('night:P3K.107')

product_path = 'analysis/IV_product_batch/receiving_replacements.json'
product = json.loads((W / product_path).read_text())
exact(product[1], product_path)
text = block('night:P3K.38')
table = product[0]['exact_new'].split(r'\begin{longtable}', 1)[1].split(r'\end{longtable}', 1)[0]
# The owner sized the same five columns against the enclosing enumerate width.
# Record this one literal layout substitution; every mathematical row remains
# byte-identical and is checked below as part of the complete table.
receiving_table = table.replace(r'\columnwidth', r'\linewidth')
assert text.count(r'\begin{longtable}' + receiving_table + r'\end{longtable}') == 1
assert len(re.findall(r'^CS\d+\s*&', text, re.M)) == 30
assert text.find(r'\end{longtable}') < text.rfind(r'\end{proof}')
assert 'two-way good-cap period basis' in text
assert 'impossible good III*/good II branch' in text
checks.append(dict(id='K38-complete-branch-table', label='night:P3K.38',
                   replacement_source=product_path, complete_table_exact_count=1,
                   branch_rows=30, table_inside_numbered_proof=True,
                   layout_substitution={r'\columnwidth': r'\linewidth'},
                   scope='Complete table equality after the single literal column-width substitution; all mathematical cells are unchanged. Enumerate markers are receiving formatting.',
                   receiving_block_sha256=hashlib.sha256(text.encode()).hexdigest()))
for label, required in [
    ('night:P3K.49', r'\cref{night:P3K.41}, only its retained CP.1--4 product, collar and source-cusp maps'),
    ('night:P3K.51', r'\cref{night:P3K.50}, only OR.2--3 and the actual ordinary-product \(V_{00}\) input')]:
    assert block(label).count(required) == 1
    checks.append(dict(id=label + '-bounded-Uses', label=label, exact_uses=required,
                       receiving_block_sha256=hashlib.sha256(block(label).encode()).hexdigest()))

receipt = dict(recorded_at=at, source_checkpoint=30,
               body_sha256=hashlib.sha256(body.read_bytes()).hexdigest(),
               operation='Exact receiving text/Uses checks only; no mathematical review or execution credit added.',
               checks=checks,
               remaining_global_gates='Final owner/canonical build, cross-reference and layout QA remain separate.')
(W / record).write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')

targets = {
    'IV-INV-D-010': ('night:P3K.107', 'Final canonical cross-reference and layout review remains separate; the two source repairs and receiving integration are verified, with the complete CP30 revision recorded separately.'),
    'IV-INV-D-022': ('night:P3K.107', ''),
    'IV-INV-D-011': ('night:P3K.38', ''),
    'IV-INV-D-015': ('night:P3K.49', ''),
    'IV-INV-D-016': ('night:P3K.51', ''),
    **{f'IV-INV-D-{number:03}': (f'night:P3K.{k}', '')
       for number, k in zip(range(23, 28), [24, 25, 27, 29, 30])},
}


def close(item, label, remaining):
    if item.get('remaining_gates') and 'remaining_gates_at_review' not in item:
        item['remaining_gates_at_review'] = item['remaining_gates']
    item['remaining_gates'] = remaining
    item['receiving_integration_verified_at'] = at
    item['receiving_integration_record'] = record
    item['current_receiving_block_sha256'] = hashlib.sha256(block(label).encode()).hexdigest()


tsv_names = ['IV_K107_events', 'IV_K107_cp30_events', 'IV_product_batch_events', 'IV_retained_batch_events']
for name in tsv_names:
    path = W / 'records' / (name + '.tsv')
    with path.open() as source:
        reader = csv.DictReader(source, delimiter='\t')
        fields = list(reader.fieldnames)
        rows = list(reader)
    for row in rows:
        if row.get('event_id') in targets:
            close(row, *targets[row['event_id']])
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    temporary = path.with_suffix('.tsv.tmp')
    with temporary.open('w', newline='') as out:
        writer = csv.DictWriter(out, fieldnames=fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)

for directory in ['IV_K107', 'IV_K107_cp30', 'IV_product_batch', 'IV_retained_batch']:
    path = W / 'analysis' / directory / 'current_events.json'
    data = json.loads(path.read_text())
    for item in data:
        if item.get('event_id') in targets:
            close(item, *targets[item['event_id']])
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
    path = W / 'analysis' / directory / ('current_reviews.json' if 'batch' in directory else 'current_review.json')
    data = json.loads(path.read_text())
    items = data if isinstance(data, list) else [data]
    by_label = {label: remaining for label, remaining in targets.values()}
    if directory == 'IV_K107':
        by_label['night:P3K.107'] = targets['IV-INV-D-010'][1]
    for item in items:
        if item.get('label') in by_label:
            close(item, item['label'], by_label[item['label']])
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(dict(record=record, checks=len(checks), events_with_precise_editing_gates_closed=len(targets)), indent=2))
