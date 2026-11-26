"""Reopen the actual containing D23 unit after root's four-row admission."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
REVIEW = 'agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate06_diagnostic_root_review.md'
APPLY = 'code/S6_SERIES_PUBLISH_c9_candidate06_diagnostic_batch_apply.out'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source = SOURCE.read_bytes()
assert hashlib.sha256(source).hexdigest() == '178fc512258907264ab80d01e426ca269b975a0ee5bf6b005bfb5aaaeee861c2'
assert b'Root accepts these exact source edits' in (ROOT / REVIEW).read_bytes()
assert b'APPLIED after explicit root-review acknowledgment: four D23 rows and four exact source edits.' in (ROOT / APPLY).read_bytes()
path = ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'
before = path.read_bytes()
reader = csv.DictReader(io.StringIO(before.decode(), newline=''), delimiter='\t')
fields, rows = reader.fieldnames, list(reader)
row, = [r for r in rows if r['paper'] == 'III' and r['unit_id'] == 'mapsIII:def:two-torus-suspension' and r['defect_type'] == 'D23']
assert row['status'] == 'done'
old = dict(row)
now = datetime.now(timezone.utc).isoformat()
row.update(status='open', date_utc=now,
    evidence=row['evidence'] + '; ' + REVIEW + '; ' + APPLY,
    detail=row['detail'] + ' Current06/legacy05 place the 035X ordinary destination on page621 and its visible theorem opening/permanent tag on page622. Global actually viewed both complete current06 pages. Root admitted the exact six-baseline reservation before the theorem environment. This actual containing D23 unit is reopened for the next destination comparison and actual changed-page reading; the prior evidence and its historical scope are retained.')
def encode(value):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writerow(value)
    return stream.getvalue().encode()
old_bytes, new_bytes = encode(old), encode(row)
assert before.count(old_bytes) == 1 and new_bytes not in before
after = before.replace(old_bytes, new_bytes, 1)
assert after.replace(new_bytes, old_bytes, 1) == before
assert b'\r' not in after
assert path.read_bytes() == before and SOURCE.read_bytes() == source
path.write_bytes(after)
assert path.read_bytes() == after
builds = list(csv.DictReader((ROOT / 'S6_SERIES_PUBLISH_build_progress.tsv').open(newline=''), delimiter='\t'))
build, = [r for r in builds if r['paper'] == 'III']
assert build['status'] == 'open'
print('UTC', now)
print('Actual transition: III mapsIII:def:two-torus-suspension D23 done -> open')
print('Paper III unit statuses:', dict(Counter(r['status'] for r in rows if r['paper'] == 'III')))
print('All bytes outside the single exact unit row preserved; source unchanged; build remains open.')
print('No check event, count, finding, build-status or derived-record write.')
