"""Record root's actual organization/body comparison; assign no PDF credit."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
organization = source[source.index(r'\subsection{How the paper is organized}'):source.index(r'\begin{figure}', source.index(r'\subsection{How the paper is organized}'))]
questions = source[source.index(r'\part*{Open problems}'):source.index(r'\section{Programs}')]
assert 'remaining\ncap-map and smooth-type classification' in organization
for label in ('mapsIII:problem:degree-zero-lines-and-multiplicities',
              'mapsIII:problem:finite-cusp-cover-compactification',
              'mapsIII:problem:raw-conical-quotient-classes', 'maps:src:D.2.4'):
    assert r'\label{' + label + '}' in questions
assert source.count(r'\section{') == 28
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
row, = [r for r in rows if r['paper'] == 'III' and r['unit_id'] == 'the-series-and-this-paper' and r['defect_type'] == 'D24']
assert row['status'] == 'open'
row.update(status='done', date_utc=datetime.now(timezone.utc).isoformat(),
    evidence='code/S6_SERIES_PUBLISH_c9_D24_source_review.py/.out; root read the complete current organization subsection, all28 section titles and the complete final Open problems part.',
    detail='The organization paragraph follows the actual source order: marked periods and sphere maps; cyclic/Kummer invariants; elliptic profiles, cap maps and smooth sectors; OS49 and conifold smoothing; global quotients, compact carriers, framed/nullbordism and metric arguments. Its four final topics resolve to the actual degree-zero-line/multiplicity, finite-cusp-cover, conical-class and remaining-filling problems. Root read all four problem statements and their complete established-reduction passages, including the current residual-model values in02LG. The earlier source structural-description gate is settled without a text change. The separate build, D14 hierarchy/proportion and every-page visual gates remain open.')
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Closed one source D24 row after the actual complete organization/final-part comparison.')
print('All28 section titles and all four final problem statements/read reductions agree with section1.6.')
print('No source rewrite, new proof event, build or PDF-page credit assigned.')
