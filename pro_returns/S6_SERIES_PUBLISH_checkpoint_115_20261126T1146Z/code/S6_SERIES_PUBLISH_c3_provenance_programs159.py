#!/usr/bin/env python3
"""Prepare exact comb-program paths, without writing shared source."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance'
meta = ROOT.parents[1] / 'tmp/c3_programs/programs159_metadata.json'
data = json.loads(meta.read_text())
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
table = source[source.index(r'\section*{Programs}'):source.index(r'\begin{thebibliography}')]
inventory = set((ROOT.parent / 'REPOSITORY_PROGRAM_PATHS.txt').read_text().splitlines())
for row in data:
    assert row['repository_path'] in inventory
    assert Path(row['repository_path']).name not in table
    assert hashlib.sha256(Path(row['local_path']).read_bytes()).hexdigest() == row['sha256']
    for path in OUT.glob('*records*II*.tsv'):
        if path.name == 'S6_SERIES_PUBLISH_records_II_additions159.tsv':
            continue
        with path.open(newline='') as f:
            for existing in csv.DictReader(f, delimiter='\t'):
                assert existing.get('sha256') != row['sha256'], (path, existing)

scopes = [
    r'Root-curve cohomology and sample comb bundle degrees (\cref{inv:E2.2,prop:II:comb-kernel-bounds})',
    r'Character descent, nonnegative coarse splittings and tangent cohomology for $m=12,13,20,100$ (\cref{cdp:st:E15,inv:E2.2,prop:II:comb-kernel-bounds})',
]
new = ''.join(scope + r' & \nolinkurl{' + row['repository_path'] + r'} \\[3pt]' + '\n'
              for scope, row in zip(scopes, data))
(OUT / 'S6_SERIES_PUBLISH_c3_provenance_program_rows159.tex').write_text(new, newline='\n')
anchor = '\\end{longtable}}\n\n\\begin{thebibliography}'
assert source.count(anchor) == 1
edit = dict(change_id='II-C3-PROV-159', type='D09',
    statement_id='cdp:st:E15;inv:E2.2;prop:II:comb-kernel-bounds;inv:E2.3',
    old_location='Programs: end of table', old_page='source guard; final concordance pending',
    new_location='Programs: root-curve and positive-comb computations', new_page='integrated build pending',
    old_text=anchor, new_text=new + anchor,
    reason='The inherited final splitting paragraph names d_exact.py and d_comb.py, neither present in the current appendix under its basename or mapped hash. Both match exact attached-inventory paths and freshly retrieved prescribed pinned bytes. Read every source line. The first compares weighted monomials/coarse degrees over its finite weight range and reports comb degree expressions at four m values; it also includes separate seed matrices, local syzygies and elliptic duplication calculations. The second evaluates character-descent degrees, exhausts nonnegative splitting pairs and checks tangent/Euler/Hodge-length expressions at those four m values. Its older unresolved/Kuranishi-bounds report fields are not used as the status of the current theorem; E15 is the full proved Kuranishi owner. The end-table rows name only the computations used in this receiving block. No program execution or new mathematical-computation credit is claimed.',
    review_status='Both complete pinned sources read; path and hash duplicates checked. Ready with P320 receiving owner; no execution claimed.')


def write(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


write('S6_SERIES_PUBLISH_c3_provenance_program_edits159.tsv', [edit])
write('S6_SERIES_PUBLISH_records_II_additions159.tsv', [
    {key: row[key] for key in ['printed_path', 'repository_path', 'sha256']} for row in data])
write('S6_SERIES_PUBLISH_c3_provenance_program_checks159.tsv', [dict(
    printed_path=row['printed_path'], repository_path=row['repository_path'],
    sha256=row['sha256'], bytes=row['bytes'], checked_at=row['url'],
    mathematical_scope=scope, date_utc=datetime.now(timezone.utc).isoformat(),
    outcome='Exact attached-inventory path and prescribed pinned bytes verified; complete program source read; no current appendix or mapped-hash duplicate; no program execution.')
    for scope, row in zip(scopes, data)])
print('Prepared addition159: two exact program rows and path/hash records; shared source unchanged.')
