"""Reopen the actual LI layout criterion after its observed page mismatch."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
assert hashlib.sha256(source.read_bytes()).hexdigest() == '75000e4890bf8ff639d74dbfcfff77f06d1a48579c02667df04a4b1b7c29a254'
for name in ('code/S6_SERIES_PUBLISH_c9_anchors_current_candidate09.out',
             'code/S6_SERIES_PUBLISH_c9_anchors_legacy_candidate08.out'):
    output = (ROOT / name).read_text()
    assert 'Completed read-only comparison: 249 formal owners.' in output
    assert 'Owners with aux/anchor or tag/anchor page differences: 1' in output
    assert 'EXCEPTION maps:src:D.2.41 383 382 383' in output
protected_names = ('S6_SERIES_PUBLISH_III.tex', 'CHECK_EVENTS.tsv',
    'S6_SERIES_PUBLISH_findings_III.tsv', 'S6_SERIES_PUBLISH_build_progress.tsv',
    'S6_SERIES_PUBLISH_defects_III.tsv', 'S6_SERIES_PUBLISH_provenance_checks.tsv',
    'records/S6_SERIES_PUBLISH_III_current_check_counts.json')
protected = {name: (ROOT / name).read_bytes() for name in protected_names}
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
raw = path.read_bytes()
reader = csv.DictReader(io.StringIO(raw.decode(), newline=''), delimiter='\t')
fields = reader.fieldnames
rows = list(reader)
row, = [r for r in rows if (r['paper'], r['unit_id'], r['row_kind'], r['defect_type'])
        == ('III', 'maps:src:D.2.41', 'defect', 'D23')]
assert row['status'] == 'done'
old = dict(row)
now = datetime.now(timezone.utc).isoformat()
row.update(status='open', date_utc=now,
    evidence=row['evidence'] + '; code/S6_SERIES_PUBLISH_c9_anchors_current_candidate09.out; code/S6_SERIES_PUBLISH_c9_anchors_legacy_candidate08.out',
    detail=row['detail'] + ' Reopened after both actual successor formal-owner comparisons: Theorem14.2/02LI has aux and permanent-tag page383 but named theorem.14.2 anchor page382. Both703-page PDFs match source75000e4890bf8ff639d74dbfcfff77f06d1a48579c02667df04a4b1b7c29a254. Root read both complete inspector outputs. Actual382–383 image assessment, the exact formal-opening reservation, a fresh zero-exception comparison and complete successor-unit reading remain required. The source-semantic D20/P15 disposition is unchanged; this reopening earns no movement credit.')

def encode(value):
    stream = io.StringIO(newline='')
    csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n').writerow(value)
    return stream.getvalue().encode()

a, b = encode(old), encode(row)
assert raw.count(a) == 1 and b not in raw
changed = raw.replace(a, b, 1)
assert changed.replace(b, a, 1) == raw and b'\r' not in changed
assert path.read_bytes() == raw
assert all((ROOT / name).read_bytes() == value for name, value in protected.items())
path.write_bytes(changed)
assert path.read_bytes() == changed
assert all((ROOT / name).read_bytes() == value for name, value in protected.items())
print('UTC', now)
print('D23 maps:src:D.2.41: done -> open after the actual paired anchor exception.')
print('III units', dict(Counter(r['status'] for r in rows if r['paper'] == 'III')))
print('Only the exact existing unit row changed; all other bytes, source, events and counts retained.')
