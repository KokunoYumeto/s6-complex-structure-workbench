"""Reopen precisely the four additional D20 instances found by contextual reading."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
instances = {
    'maps:src:D.2.31': '02L7: the regular CRT aggregate vector/map/scalars reuse V,T,X,N,F with other objects in the same proof.',
    'maps:src:D.2.41': '02LI: F denotes a fibre-chain map and later a fixed-basis matrix in the same proof.',
    'maps:src:D.2.50': '02LS: J denotes the symplectic 2 by 2 matrix and later the ambient graph map.',
    'wb:sphere-metric-tangent-scope': '03DF: d denotes a collar function and later the dimension of the link.',
}
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
now = datetime.now(timezone.utc).isoformat()
found = set()
for row in rows:
    if row['paper'] == 'III' and row['defect_type'] == 'D20' and row['unit_id'] in instances:
        assert row['status'] == 'done', row['unit_id']
        row.update(status='open', date_utc=now,
            evidence='continuation9 global P15 contextual proof reading; exact scoped proposals in preparation',
            detail=instances[row['unit_id']] + ' Reopened on the observed instance; no mathematical result or required check reopened.')
        found.add(row['unit_id'])
assert found == set(instances), set(instances) - found
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Reopened four observed D20 criteria. Potential candidates still under contextual review are not treated as findings.')
