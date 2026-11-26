#!/usr/bin/env python3
"""Prepare two exact program-path additions; no shared manuscript writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation3_provenance'
META = ROOT.parents[1] / 'tmp/c3_programs/programs157_metadata.json'
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
        if path.name == 'S6_SERIES_PUBLISH_records_II_additions157.tsv':
            continue
        with path.open(newline='') as f:
            for existing in csv.DictReader(f, delimiter='\t'):
                assert existing.get('sha256') != row['sha256'], (path, existing)

scopes = [
    r'Finite cyclic characters, reflection quotients and elliptic-fibre Euler sums (\cref{cdp:st:C.2.UN.33})',
    r'Finite-order determinant and M\"obius sums, cyclic fixed-point and orbit counts, and formal four-curve projection identities (\cref{cdp:st:C.2.UN.11,cdp:st:C.2.UN.24,cdp:st:C.2.UN.39})',
]
new = ''.join(scope + r' & \nolinkurl{' + row['repository_path'] + r'} \\[3pt]' + '\n'
              for scope, row in zip(scopes, data))
(OUT / 'S6_SERIES_PUBLISH_c3_provenance_program_rows157.tex').write_text(new, newline='\n')
anchor = '\\end{longtable}}\n\n\\begin{thebibliography}'
assert source.count(anchor) == 1
for key in ['cdp:st:C.2.UN.33', 'cdp:st:C.2.UN.11', 'cdp:st:C.2.UN.24', 'cdp:st:C.2.UN.39']:
    assert r'\label{' + key + '}' in source
edit = dict(change_id='II-C3-PROV-157', type='D09',
    statement_id='cdp:st:C.2.UN.33;cdp:st:C.2.UN.11;cdp:st:C.2.UN.24;cdp:st:C.2.UN.39',
    old_location='Programs: end of table', old_page='current source; final concordance pending',
    new_location='Programs: cyclic character, fixed-point and determinant programs', new_page='integrated build pending',
    old_text=anchor, new_text=new + anchor,
    reason='Resolve both inherited body paths to exact attached-inventory paths and pinned bytes. Neither basename nor SHA256 is already represented in the mapped appendix. The first program enumerates the finite cyclic characters and reflection reductions, then checks the resulting Euler/coherent-character sums. The second computes exact cyclotomic companion-matrix determinants, Mobius coefficients, finite quotient fixed-point/orbit counts and universal formal projection identities. Its finite matrices give the determinant values through the eigenvalue product; they do not identify the full monodromy matrix with its semisimple part. Its JSON output remains associated with its generating program. The printed proofs retain the analytic quotient, resolution and elliptic-pencil arguments. No program execution or geometric-proof credit is inferred from this source/path check.',
    review_status='Both full program sources read and their scopes matched; no program execution or new mathematical-computation credit claimed.')


def write(name, rows):
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


write('S6_SERIES_PUBLISH_c3_provenance_program_edits157.tsv', [edit])
write('S6_SERIES_PUBLISH_records_II_additions157.tsv', [
    {key: row[key] for key in ['printed_path', 'repository_path', 'sha256']} for row in data])
checks = []
for scope, row in zip(scopes, data):
    checks.append(dict(printed_path=row['printed_path'], repository_path=row['repository_path'],
        sha256=row['sha256'], bytes=row['bytes'], checked_at=row['url'],
        mathematical_scope=scope, date_utc=datetime.now(timezone.utc).isoformat(),
        outcome='Exact prescribed pinned bytes retrieved; full source read; basename and mapped-hash duplicate checks found no existing row; no execution claimed.'))
write('S6_SERIES_PUBLISH_c3_provenance_program_checks157.tsv', checks)
print('Prepared source edit157, two program rows and their exact path/hash additions; shared source unchanged.')
