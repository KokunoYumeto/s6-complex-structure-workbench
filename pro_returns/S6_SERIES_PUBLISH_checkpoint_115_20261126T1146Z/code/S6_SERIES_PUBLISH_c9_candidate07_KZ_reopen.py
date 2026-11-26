"""Reopen the one actual D20 owner confirmed by root's complete source read."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source = SOURCE.read_bytes()
assert hashlib.sha256(source).hexdigest() == '178fc512258907264ab80d01e426ca269b975a0ee5bf6b005bfb5aaaeee861c2'
REPORT = 'agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate07_KZ_heading_review.md'
report = (ROOT / REPORT).read_text()
assert 'all 216 current source lines 21555' in report
assert 'six occurrences of the circle' in report
text = source.decode()
scope = '\n'.join(text.splitlines()[21554:21770]) + '\n'
assert scope.startswith('\\begin{theorem}[Homology obstruction')
assert scope.endswith('\\end{proof}\n')
assert scope.count('u(s)') == 1
assert 'for the transverse elliptic circles' in scope
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
before = path.read_bytes()
reader = csv.DictReader(io.StringIO(before.decode(), newline=''), delimiter='\t')
fields, rows = reader.fieldnames, list(reader)
row, = [r for r in rows if (r['paper'], r['unit_id'], r['defect_type']) == ('III', 'maps:src:D.2.24', 'D20')]
assert row['status'] == 'done'
old = dict(row)
now = datetime.now(timezone.utc).isoformat()
row.update(status='open', date_utc=now,
    evidence=row['evidence'] + '; ' + REPORT,
    detail=row['detail'] + ' Current07 actual pages251–253 exposed plain u as the transverse elliptic circle and plain u(s) as the selected translated unit within the same proof. Global read the complete216-line statement/proof and all four external caller contexts. Root then read all216 original source lines, the complete authored comparison, final diff and actual output, confirming both roles and the exact deck-map/inverse identity. Reopen this actual containing D20 owner for the qualified same-function binding and its final source/build/image admission. The prior done evidence remains historical; paragraph scope supplies no exemption. No independent proof or computation credit is added.')
def encode(value):
    stream = io.StringIO(newline='')
    csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n').writerow(value)
    return stream.getvalue().encode()
old_bytes, new_bytes = encode(old), encode(row)
assert before.count(old_bytes) == 1 and new_bytes not in before
after = before.replace(old_bytes, new_bytes, 1)
assert after.replace(new_bytes, old_bytes, 1) == before
assert b'\r' not in after
assert path.read_bytes() == before and SOURCE.read_bytes() == source
path.write_bytes(after)
assert path.read_bytes() == after
print('UTC', now)
print('Actual transition: III maps:src:D.2.24 D20 done -> open')
print('Paper III unit statuses:', dict(Counter(r['status'] for r in rows if r['paper'] == 'III')))
print('All bytes outside the one exact unit row preserved; source unchanged.')
print('No check event, count, finding, build-status or derived-record write.')
