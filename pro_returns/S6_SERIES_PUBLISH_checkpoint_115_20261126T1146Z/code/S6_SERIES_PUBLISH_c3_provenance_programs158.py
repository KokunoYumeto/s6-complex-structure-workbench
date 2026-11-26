#!/usr/bin/env python3
"""Prepare four exact program-path additions; no shared manuscript writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance'
META = ROOT.parents[1] / 'tmp/c3_programs/programs158_metadata.json'
data = json.loads(META.read_text())
known = set((ROOT.parent / 'REPOSITORY_PROGRAM_PATHS.txt').read_text().splitlines())
source = (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text()
table = source[source.index(r'\section{Programs}'):] if r'\section{Programs}' in source else source[source.rfind(r'\begin{longtable}'):]
for row in data:
    assert row['repository_path'] in known
    assert Path(row['repository_path']).name not in table
    raw = Path(row['local_path']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == row['sha256']
    for path in OUT.glob('*records*II*.tsv'):
        if path.name == 'S6_SERIES_PUBLISH_records_II_additions158.tsv':
            continue
        with path.open(newline='') as f:
            for existing in csv.DictReader(f, delimiter='\t'):
                assert existing.get('sha256') != row['sha256'], (path, existing)

scopes = [
    r'Integral meridian and root-cover relation lattices and Smith forms (\cref{cdp:st:C.2.UN.44})',
    r'Terminal-pair degree equations, blowup Jacobians, normal-extension cocycles, and Euler differences (\cref{cdp:st:C.2.UN.64})',
    r'Ruled degree partitions, elliptic intersections and quotient multiplicities, and blowup Euler sums (\cref{cdp:st:C.2.UN.66})',
    r'Rank-four cyclotomic determinant periods, M\"obius signatures, exterior-power zeta identities, and explicit torus automorphism matrices (\cref{cdp:st:C.2.UN.11})',
]
new = ''.join(scope + r' & \nolinkurl{' + row['repository_path'] + r'} \\[3pt]' + '\n'
              for scope, row in zip(scopes, data))
(OUT / 'S6_SERIES_PUBLISH_c3_provenance_program_rows158.tex').write_text(new, newline='\n')
anchor = '\\end{longtable}}\n\n\\begin{thebibliography}'
assert source.count(anchor) == 1
for key in ['cdp:st:C.2.UN.44', 'cdp:st:C.2.UN.64', 'cdp:st:C.2.UN.66', 'cdp:st:C.2.UN.11']:
    assert r'\label{' + key + '}' in source
edit = dict(change_id='II-C3-PROV-158', type='D09',
    statement_id='cdp:st:C.2.UN.44;cdp:st:C.2.UN.64;cdp:st:C.2.UN.66;cdp:st:C.2.UN.11',
    old_location='Programs: end of table', old_page='current source; final concordance pending',
    new_location='Programs: meridian, terminal, reduction and monodromy programs', new_page='integrated build pending',
    old_text=anchor, new_text=new + anchor,
    reason='Resolve four inherited body paths to exact attached-inventory paths and prescribed pinned bytes. Every full program source was read. The meridian program compares the two integral relation lattices and their Smith forms for finite test tuples; the proof establishes the general presentation. The terminal program checks finite degree equations, blowup Jacobians, extension cocycles and finite Laurent/deck iterates; its finite exponent ranges do not prove the analytic splitting obstruction. The reduction program computes positive ruled partitions, bounded intersection and Euclidean quotient possibilities, the bracket identity, and finite Euler sums. The signature program computes all nineteen cyclotomic companion cases, determinant periods, Mobius coefficients, exterior-power zeta identities and the explicit order-eight/order-twelve matrices. Its finite matrices compute the required determinants by the eigenvalue product; the analytic monodromy comparison and geometric occurrence remain in the proof. Existing output files belong to their generating programs. No program was executed and no new mathematical-computation credit is claimed.',
    review_status='All four full program sources read and their scopes matched; no program execution or new mathematical-computation credit claimed.')


def write(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


write('S6_SERIES_PUBLISH_c3_provenance_program_edits158.tsv', [edit])
write('S6_SERIES_PUBLISH_records_II_additions158.tsv', [
    {key: row[key] for key in ['printed_path', 'repository_path', 'sha256']} for row in data])
checks = []
for scope, row in zip(scopes, data):
    checks.append(dict(printed_path=row['printed_path'], repository_path=row['repository_path'],
        sha256=row['sha256'], bytes=row['bytes'], checked_at=row['url'],
        mathematical_scope=scope, date_utc=datetime.now(timezone.utc).isoformat(),
        outcome='Exact prescribed pinned bytes retrieved; full source read; basename and mapped-hash duplicate checks found no existing row; no execution claimed.'))
write('S6_SERIES_PUBLISH_c3_provenance_program_checks158.tsv', checks)
print('Prepared source edit158, four program rows and their exact path/hash additions; shared source unchanged.')
