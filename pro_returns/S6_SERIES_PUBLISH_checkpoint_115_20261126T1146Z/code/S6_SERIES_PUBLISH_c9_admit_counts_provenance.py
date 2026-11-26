"""Apply the final root-reviewed III count and deposit/provenance declarations.

The temporary proposal is outside the checkpoint tree. Its five source/deposit
edits are recorded in the canonical defect table; the nine existing provenance
claims are updated in place. No copy or diff of a derived file is retained.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import csv
import io
import json
import os
import re
import tempfile
import S6_SERIES_PUBLISH_c9_III_check_counts as counts

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
p = argparse.ArgumentParser()
p.add_argument('--proposals', type=Path, required=True)
p.add_argument('--counts', type=Path, required=True)
p.add_argument('--reviewed', required=True)
a = p.parse_args()
changes = json.loads(a.proposals.read_text())
assert len(changes) == 14
allowed = {'S6_SERIES_PUBLISH_III.tex', 'S6_SERIES_PUBLISH_deposit_fields_III.json',
           'S6_SERIES_PUBLISH_deposit_fields.md', 'S6_SERIES_PUBLISH_provenance_checks.tsv'}
assert {r['path'] for r in changes} == allowed
original = {name: (ROOT / name).read_bytes() for name in allowed}
original['CHECK_EVENTS.tsv'] = (ROOT / 'CHECK_EVENTS.tsv').read_bytes()
original['S6_SERIES_PUBLISH_defects_III.tsv'] = (ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv').read_bytes()
original['S6_SERIES_PUBLISH_unit_progress.tsv'] = (ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').read_bytes()
count_name = 'records/S6_SERIES_PUBLISH_III_current_check_counts.json'
original[count_name] = (ROOT / count_name).read_bytes()
candidate = dict(original)

def parse_table(body):
    reader = csv.DictReader(io.StringIO(body.decode()), delimiter='\t')
    return reader.fieldnames, list(reader)

def encode_table(fields, rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()

df, defects = parse_table(original['S6_SERIES_PUBLISH_defects_III.tsv'])
pf, provenance = parse_table(original['S6_SERIES_PUBLISH_provenance_checks.tsv'])
uf, units = parse_table(original['S6_SERIES_PUBLISH_unit_progress.tsv'])
assert encode_table(pf, provenance) == original['S6_SERIES_PUBLISH_provenance_checks.tsv']
deposit = json.loads(original['S6_SERIES_PUBLISH_deposit_fields_III.json'])
data = counts.current_data(ROOT)
count_bytes = a.counts.read_bytes()
count_result = json.loads(count_bytes)
assert count_result['selected_event_ids'] == [r['event_id'] for r in data['selected']]
assert count_result['recorded_evidence_groups'] == sorted(data['groups'])
candidate[count_name] = count_bytes
count_change, = [r for r in changes if r['change_id'] == 'C9-III-METHODOLOGY-COUNTS']
assert ' '.join(count_change['new_text'].split()) == counts.count_prose(data)
now = datetime.now(timezone.utc).isoformat()
defect_count = 0
for change in changes:
    name, operation = change['path'], change['operation']
    if operation == 'text_replace':
        old, new = change['old_text'], change['new_text']
        text = candidate[name].decode()
        assert text.count(old) == 1, change['change_id']
        candidate[name] = text.replace(old, new, 1).encode()
    elif operation == 'json_field_replace':
        key = change['field']
        assert deposit[key] == change['old_value'], change['change_id']
        old = json.dumps(change['old_value'], ensure_ascii=False, indent=2)
        new = json.dumps(change['new_value'], ensure_ascii=False, indent=2)
        deposit[key] = change['new_value']
    elif operation == 'tsv_row_replace':
        key = change['key']['claim_id']
        matches = [i for i, row in enumerate(provenance) if row['claim_id'] == key]
        index, = matches
        assert provenance[index] == change['old_row']
        assert change['new_row']['paper'] == 'III'
        provenance[index] = change['new_row']
        continue
    else:
        raise AssertionError(operation)
    assert not any(r['change_id'] == change['change_id'] for r in defects)
    row = dict.fromkeys(df, '')
    row.update(change_id=change['change_id'], type=change['type'],
        statement_id=change.get('statement_id', 'methodology'),
        old_location=name + (' > JSON field ' + change['field'] if operation == 'json_field_replace' else ' > exact recorded fragment'),
        new_location=name + ' > corresponding current field or fragment',
        old_text=old, new_text=new, reason=change['reason'],
        review_status='Root read the complete proposal and its exact documentary/count evidence. ' + a.reviewed + ' Admitted ' + now + '; final PDF and joint-series gates retain their stated scope.')
    defects.append(row)
    defect_count += 1
assert defect_count == 5
candidate['S6_SERIES_PUBLISH_deposit_fields_III.json'] = (json.dumps(deposit, ensure_ascii=False, indent=2) + '\n').encode()
candidate['S6_SERIES_PUBLISH_provenance_checks.tsv'] = encode_table(pf, provenance)
candidate['S6_SERIES_PUBLISH_defects_III.tsv'] = encode_table(df, defects)
unit, = [r for r in units if r['paper'] == 'III' and r['unit_id'] == 'methodology' and r['defect_type'] == 'D15']
assert unit['status'] == 'open'
unit.update(status='done', date_utc=now,
    evidence='code/S6_SERIES_PUBLISH_c9_III_check_counts.py; records/S6_SERIES_PUBLISH_III_current_check_counts.json; C9-III-METHODOLOGY-COUNTS and matching deposit/provenance rows',
    detail='The stale count instance is replaced by the current exact six-category derivation, including eight verified literal intake associations and the exposed58-input computation event. Source, deposit and the nine existing documentary claims agree. All raw events remain unchanged; the separate final PDF and joint-series gates retain their scope.')
candidate['S6_SERIES_PUBLISH_unit_progress.tsv'] = encode_table(uf, units)
source_before, source_after = original['S6_SERIES_PUBLISH_III.tex'].decode(), candidate['S6_SERIES_PUBLISH_III.tex'].decode()
ids = lambda s: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', s))
assert ids(source_before) == ids(source_after)
abstract = source_after.split(r'\begin{abstract}', 1)[1].split(r'\end{abstract}', 1)[0]
assert deposit['abstract'].split() == abstract.split()
assert 'How it was checked. ' + counts.count_prose(data) in deposit['provenance']
assert all(b'\r' not in body for body in candidate.values())
assert candidate['CHECK_EVENTS.tsv'] == original['CHECK_EVENTS.tsv']
for name, body in original.items():
    assert (ROOT / name).read_bytes() == body, 'An input changed: ' + name
temporary = {}
try:
    for name, body in candidate.items():
        if body == original[name]:
            continue
        with tempfile.NamedTemporaryFile(dir=ROOT, prefix='c9-admit-', suffix='.tmp', delete=False) as stream:
            stream.write(body)
            temporary[name] = Path(stream.name)
    for name, body in original.items():
        assert (ROOT / name).read_bytes() == body
    for name, path in temporary.items():
        os.replace(path, ROOT / name)
finally:
    for path in temporary.values():
        path.unlink(missing_ok=True)
print('Admitted five exact source/deposit defect rows and updated nine existing III provenance claims.')
print('Selected statement-event associations', len(data['selected']), 'evidence groups', len(data['groups']))
for kind in counts.TYPES:
    print(kind, data['counts'][kind], sep='\t')
print('Raw CHECK_EVENTS unchanged; complete abstract token agreement; permanent source targets retained.')
print('One methodology D15 row closed at source scope. No build, page or independent-proof credit.')
