"""Reopen only the notation findings actually observed in the fixed PDF."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import io

root = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
now = datetime.now(timezone.utc).isoformat()
for name in ['S6_SERIES_PUBLISH_findings_III.tsv', 'S6_SERIES_PUBLISH_unit_progress.tsv']:
    path = root / name
    old = path.read_bytes()
    reader = csv.DictReader(io.StringIO(old.decode()), delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
    if name.endswith('findings_III.tsv'):
        selected = [row for row in rows if row['id'] in ('P11', 'P15')]
        assert len(selected) == 2
        for row in selected:
            assert row['status'] == 'done'
            row.update(status='open', date_utc=now,
                source_resolution=row['source_resolution'] + ' The actual candidate02 image reading of the complete Theorem18.2 statement/proof (523–533) found a remaining reverse renaming on525 and several semantically different objects sharing B,K,U,V,q,s. These observed instances reopen the finding.',
                remaining_gate='Scoped 02LP notation/wording repair, full proof comparison and changed-page reading.',
                evidence=row['evidence'] + '; agents/continuation9_root/S6_SERIES_PUBLISH_III_pages_523_696_reading.md')
    else:
        row, = [row for row in rows if row['paper'] == 'III' and row['unit_id'] == 'maps:src:D.2.48' and row['defect_type'] == 'D20']
        assert row['status'] == 'done'
        row.update(status='open', date_utc=now,
            evidence=row['evidence'] + '; agents/continuation9_root/S6_SERIES_PUBLISH_III_pages_523_696_reading.md',
            detail=row['detail'] + ' Reopened after actual complete statement/proof image reading on523–533: reverse E-name assignment and normal/period/degree B, polarization/Bezout K, period/Smith U,V and other observed q,s roles require scoped exact notation repair. No unobserved unit is reopened.')
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
    assert path.read_bytes() == old
    path.write_text(out.getvalue(), newline='\n')
print('Reopened supplied P11 and P15 plus the observed 02LP unit D20 row.')
print('The source/PDF remain unchanged; the full candidate02 page reading continues.')
