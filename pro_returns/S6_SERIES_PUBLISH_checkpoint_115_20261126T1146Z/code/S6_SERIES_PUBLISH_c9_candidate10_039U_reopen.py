"""Reopen the actual compactification D20 unit and P15 from full-page findings."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
assert hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest() == '5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187'
note = 'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate10_new_source_findings.md'
assert 'Root actually viewed and read complete physical images 614, 615 and 616' in (ROOT / note).read_text()
protected = {name: (ROOT / name).read_bytes() for name in ('S6_SERIES_PUBLISH_III.tex', 'CHECK_EVENTS.tsv', 'S6_SERIES_PUBLISH_build_progress.tsv', 'S6_SERIES_PUBLISH_defects_III.tsv', 'S6_SERIES_PUBLISH_provenance_checks.tsv', 'records/S6_SERIES_PUBLISH_III_current_check_counts.json')}
now = datetime.now(timezone.utc).isoformat()
paths = ['S6_SERIES_PUBLISH_unit_progress.tsv', 'S6_SERIES_PUBLISH_findings_III.tsv']
updates = {}
for name in paths:
    raw = (ROOT / name).read_bytes()
    reader = csv.DictReader(io.StringIO(raw.decode(), newline=''), delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
    if name == paths[0]:
        row, = [r for r in rows if (r['paper'], r['unit_id'], r['row_kind'], r['defect_type']) == ('III', 'mapsIII:sec:regular-quotients', 'defect', 'D20')]
        old = dict(row)
        assert row['status'] == 'done'
        row.update(status='open', date_utc=now, evidence=row['evidence'] + '; ' + note,
            detail=row['detail'] + ' Reopened after root actually read full current10 images614–616: in the same039Uproof a,b are integer attaching-loop values, a is later a toric vector and stereographic scalar, and b is a sphere pole. Complete statement/proof source comparison, exact role qualifications and domain/map/inverse retention are pending. Earlier radial and other source comparisons retain their actual attribution. The accepted PDF stays fixed for full reading; this reopening earns no movement credit.')
        status_counts = Counter(r['status'] for r in rows if r['paper'] == 'III')
    else:
        row, = [r for r in rows if r['id'] == 'P15']
        old = dict(row)
        assert row['status'] == 'done'
        row.update(status='open', date_utc=now, evidence=row['evidence'] + '; ' + note,
            source_resolution=row['source_resolution'] + ' Reopened from actual current10 images614–616 and source52800–52850/52945–53005: selected a/b roles in039U require the complete statement/proof qualification comparison. All previously completed four-owner comparisons remain historical completed work; no new proof or event is claimed.',
            remaining_gate='Complete039U statement/proof selected-role review, exact recorded correction with maps/inverses and exposed comparison, then successor build and affected-page agreement. The current accepted image target remains fixed during its complete reading.')
    def encode(value):
        stream = io.StringIO(newline='')
        csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n').writerow(value)
        return stream.getvalue().encode()
    a, b = encode(old), encode(row)
    assert raw.count(a) == 1 and b not in raw
    changed = raw.replace(a, b, 1)
    assert changed.replace(b, a, 1) == raw and b'\r' not in changed
    updates[name] = raw, changed
assert all((ROOT / name).read_bytes() == raw for name, (raw, _) in updates.items())
assert all((ROOT / name).read_bytes() == value for name, value in protected.items())
for name, (_, changed) in updates.items():
    (ROOT / name).write_bytes(changed)
assert all((ROOT / name).read_bytes() == changed for name, (_, changed) in updates.items())
assert all((ROOT / name).read_bytes() == value for name, value in protected.items())
print('UTC', now)
print('D20 mapsIII:sec:regular-quotients and P15: done -> open from actual039U role reuse.')
print('III unit state', dict(status_counts))
print('Only two exact existing rows changed; all earlier row evidence and every other byte retained.')
print('Source, accepted build, PDF, events, counts, defects and provenance unchanged; no movement credit.')
