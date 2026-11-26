"""Admit root-reviewed four-line anchor packet and reopen its three D23 rows.

Root read the full proposal review, script, output, complete four-line diff,
all JSON/TSV openings and reasons, and the eight actual boundary page images.
No mathematical text, event, count or completed visual gate is changed.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json

ROOT = Path(__file__).resolve().parents[1]
PREFIX = ROOT / 'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate04_anchor'
source_path = ROOT / 'S6_SERIES_PUBLISH_III.tex'
defect_path = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
unit_path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
csv.field_size_limit(100000000)
snapshot = {p: p.read_bytes() for p in (source_path, defect_path, unit_path)}
source = snapshot[source_path].decode()
assert hashlib.sha256(snapshot[source_path]).hexdigest() == '04341e7d93b9677dbfadb7d4a6ee3b60874b14ff71475af810590476d8472ca2'
proposals = json.loads(PREFIX.with_name(PREFIX.name + '_proposals.json').read_text())
with PREFIX.with_name(PREFIX.name + '_defects.tsv').open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    defect_fields, additions = reader.fieldnames, list(reader)
assert len(proposals) == len(additions) == 4
reader = csv.DictReader(io.StringIO(snapshot[defect_path].decode()), delimiter='\t')
assert reader.fieldnames == defect_fields
existing_ids = {r['change_id'] for r in reader}
reviewed = 'Root read all four exact fragments and reasons, complete proposal/diff/output, and all eight actual candidate04 boundary images; source-only layout admission, with fresh destinations and final images pending.'
stamp = datetime.now(timezone.utc).isoformat()
after = source
for p, row in zip(proposals, additions):
    assert p['change_id'] == row['change_id'] and p['change_id'] not in existing_ids
    assert p['statement_id'] == row['statement_id']
    assert p['old'] == row['old_text'] and p['new'] == row['new_text'] and p['reason'] == row['reason']
    assert p['new'] == '\\Needspace{6\\baselineskip}\n' + p['old']
    assert after.count(p['old']) == 1 and after.count(p['new']) == 0
    after = after.replace(p['old'], p['new'], 1)
    row['review_status'] = 'Admitted by root at ' + stamp + '; ' + reviewed
restored = after
for p in reversed(proposals):
    assert restored.count(p['new']) == 1
    restored = restored.replace(p['new'], p['old'], 1)
assert restored == source
buf = io.StringIO(newline='')
writer = csv.DictWriter(buf, defect_fields, delimiter='\t', lineterminator='\n')
writer.writerows(additions)
new_defects = snapshot[defect_path] + buf.getvalue().encode()

units = snapshot[unit_path].decode()
reader = csv.DictReader(io.StringIO(units), delimiter='\t')
unit_fields, all_units = reader.fieldnames, list(reader)
keys = sorted({p['containing_unit'] for p in proposals})
assert keys == sorted(['maps:src:D.1.5', 'maps:src:D.2.53', 'wb:cusp-s12-carrier-homotopy'])

def record(row):
    stream = io.StringIO(newline='')
    csv.DictWriter(stream, unit_fields, delimiter='\t', lineterminator='\n').writerow(row)
    return stream.getvalue()

for key in keys:
    row, = [r for r in all_units if r['paper'] == 'III' and r['unit_id'] == key and r['defect_type'] == 'D23']
    assert row['status'] == 'done'
    old_record = record(row)
    assert units.count(old_record) == 1
    row.update(status='open', date_utc=stamp,
        evidence=row['evidence'] + '; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate04_anchor_review.md; agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate04_anchor_images.md; code/S6_SERIES_PUBLISH_c9_admit_candidate04_anchors.out',
        detail=row['detail'] + ' Reopened at the actual candidate04 formal-anchor finding: the ordinary environment destination precedes the visible statement/tag page. The exact pre-environment reservation is admitted; current candidate05 and legacy candidate04 formal comparisons and actual final images remain required. Earlier source/proof credit is preserved.')
    units = units.replace(old_record, record(row), 1)

new_bytes = {source_path: after.encode(), defect_path: new_defects, unit_path: units.encode()}
for path, data in snapshot.items():
    assert path.read_bytes() == data
pending = []
try:
    for path, data in new_bytes.items():
        assert b'\r' not in data
        temp = path.with_name(path.name + '.c9_anchor_pending')
        assert not temp.exists()
        temp.write_bytes(data)
        pending.append((temp, path))
    for path, data in snapshot.items():
        assert path.read_bytes() == data
    for temp, path in pending:
        temp.replace(path)
finally:
    for temp, path in pending:
        temp.unlink(missing_ok=True)
print('Admitted four exact pre-environment Needspace additions and four D23 defect rows.')
print('Complete inverse restores every prior source byte; every mathematical statement, proof, target and numerical expression is unchanged.')
print('Reopened only three existing III D23 rows:', ', '.join(keys))
print('All other physical progress records are byte-preserved. No CHECK_EVENT, count, provenance or derived record changed.')
print('Fresh two-kernel destination checks and final actual-image reading remain open.')
print('Actual admission UTC:', stamp)
