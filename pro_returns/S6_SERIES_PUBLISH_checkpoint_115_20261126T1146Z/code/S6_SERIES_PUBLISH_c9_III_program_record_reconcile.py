"""Add the one reviewed replay record after the final source disposition.

Preserve the 181 existing record triples and their physical row bytes.
Do not fetch historical sources, execute programs, or refresh check counts.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import io
import os
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = 'code/S6_SERIES_PUBLISH_c9_ku_matrix_replay.py'
EXPECTED = '840786ad2d66216f3700bb8270ce7941349226a96dd707c0af18a3c0ed673f8f'
csv.field_size_limit(100000000)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('mode', choices=('inspect', 'apply'))
parser.add_argument('--reviewed')
args = parser.parse_args()

def parse(data):
    reader = csv.DictReader(io.StringIO(data.decode()), delimiter='\t')
    return reader.fieldnames, list(reader)

def encode(fields, rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()

names = ('S6_SERIES_PUBLISH_III.tex', 'S6_SERIES_PUBLISH_records_III.tsv',
         'S6_SERIES_PUBLISH_provenance_checks.tsv', 'CHECK_EVENTS.tsv',
         'S6_SERIES_PUBLISH_findings_III.tsv', PROGRAM)
original = {name: (ROOT / name).read_bytes() for name in names}
_, findings = parse(original[names[4]])
assert all(row['status'] == 'done' for row in findings if row['id'] not in ('P4', 'T1'))
source = original[names[0]].decode()
start = source.index(r'\section{Programs}')
stop = source.index(r'\begin{thebibliography}', start)
printed = re.findall(r'\\(?:nolinkurl|path)\{([^{}]+)\}', source[start:stop])
assert len(printed) == len(set(printed)) == 182
fields, records = parse(original[names[1]])
assert fields == ['printed_path', 'repository_path', 'sha256'] and len(records) == 181
assert [p for p in printed if p != PROGRAM] == [row['printed_path'] for row in records]
assert set(printed) - {row['printed_path'] for row in records} == {PROGRAM}
assert hashlib.sha256(original[PROGRAM]).hexdigest() == EXPECTED
lines = original[names[1]].splitlines(keepends=True)
assert len(lines) == len(records) + 1 and all(line.endswith(b'\n') for line in lines)
raw_rows = dict(zip((row['printed_path'] for row in records), lines[1:]))
new_row = (PROGRAM + '\t' + PROGRAM + '\t' + EXPECTED + '\n').encode()
candidate_records = lines[0] + b''.join(new_row if path == PROGRAM else raw_rows[path] for path in printed)
_, final_records = parse(candidate_records)
assert len(final_records) == 182
assert [row for row in final_records if row['printed_path'] != PROGRAM] == records
pf, claims = parse(original[names[2]])
claim, = [row for row in claims if row['claim_id'] == 'III-C8-P16']
historical = 'Root wholly read 181 rows, 50 HTTP200 accesses and 42 stored-digest agreements; eight cases retain unavailable prior digests. This reviewer adds no old-execution credit.'
assert historical in claim['evidence']
addition = ('The current printed table has 182 paths. The one new replay record was added from the actual admitted program bytes, with printed and repository path ' + PROGRAM + '. All 181 prior record triples and their physical row bytes are preserved; the eight prior-digest unknowns and all historical execution limits remain. This record update supplies no new execution, independent-proof or PDF visibility credit.')
print('One missing record, exact new row:')
print(new_row.decode(), end='')
print('All 181 prior records retained byte for byte; their ordering is the printed order with the one new path inserted.')
print('P16 evidence/current-resolution addition:', addition)
print('The historical 181-row sentence remains unchanged. P16 status and final-PDF gate remain unchanged.')
if args.mode == 'inspect':
    print('Inspection only; no canonical file changed.')
    raise SystemExit(0)
assert args.reviewed
now = datetime.now(timezone.utc).isoformat()
claim['evidence'] += '; agents/continuation9_defect_records/S6_SERIES_PUBLISH_c9_program_record_reconciliation_review.md; code/S6_SERIES_PUBLISH_c9_III_program_record_reconcile.py; code/S6_SERIES_PUBLISH_c9_III_program_record_reconcile_inspect.out; code/S6_SERIES_PUBLISH_c9_III_program_record_reconcile_apply.out; ' + addition
claim['current_resolution'] += ' ' + addition + ' Root review: ' + args.reviewed + ' Admitted ' + now + '.'
candidate_claims = encode(pf, claims)
_, previous_claims = parse(original[names[2]])
for old, new in zip(previous_claims, claims):
    assert old['claim_id'] == new['claim_id']
    if old['claim_id'] != 'III-C8-P16':
        assert old == new
    else:
        assert all(old[key] == new[key] for key in pf if key not in ('evidence', 'current_resolution'))
updates = {names[1]: candidate_records, names[2]: candidate_claims}
temporary = {}
try:
    for name, data in original.items():
        assert (ROOT / name).read_bytes() == data, name
    for name, data in updates.items():
        assert b'\r' not in data
        with tempfile.NamedTemporaryFile(dir=ROOT, prefix='c9-program-record-', delete=False) as stream:
            stream.write(data)
            temporary[name] = Path(stream.name)
    for name, data in original.items():
        assert (ROOT / name).read_bytes() == data, name
    for name, path in temporary.items():
        os.replace(path, ROOT / name)
finally:
    for path in temporary.values():
        path.unlink(missing_ok=True)
print('Added the one program record and appended its actual evidence to P16 at', now)
print('No manuscript, CHECK_EVENTS, check count, status, other provenance row or final-PDF gate changed.')
