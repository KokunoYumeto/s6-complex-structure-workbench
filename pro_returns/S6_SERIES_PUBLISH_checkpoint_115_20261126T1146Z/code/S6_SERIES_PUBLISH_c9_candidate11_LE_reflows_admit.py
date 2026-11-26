"""Admit exactly the two root-reviewed LE display reflows; no event or status change."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib
import io
import json
import os
import re
import tempfile

ROOT = Path(__file__).resolve().parents[1]
csv.field_size_limit(100000000)
p = argparse.ArgumentParser()
p.add_argument('--reviewed', required=True)
a = p.parse_args()
stem = ROOT / 'agents/continuation9_findings/S6_SERIES_PUBLISH_c9_candidate11_LE_two_reflows'
payload = json.loads(stem.with_suffix('.json').read_text())
fields = 'change_id type statement_id old_location old_page new_location new_page old_text new_text reason review_status'.split()
with stem.with_name(stem.name + '_defects.tsv').open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    assert reader.fieldnames == fields
    rows = list(reader)
assert rows == payload['proposals'] and len(rows) == 2
assert payload['containing_unit'] == 'maps:src:D.2.35'
assert all(row['type'] == 'D23' and row['statement_id'] == 'maps:src:D.2.38' for row in rows)
source_path = ROOT / 'S6_SERIES_PUBLISH_III.tex'
defect_path = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
original = {source_path: source_path.read_bytes(), defect_path: defect_path.read_bytes()}
protected_names = ('CHECK_EVENTS.tsv', 'S6_SERIES_PUBLISH_unit_progress.tsv',
    'S6_SERIES_PUBLISH_findings_III.tsv', 'S6_SERIES_PUBLISH_build_progress.tsv',
    'records/S6_SERIES_PUBLISH_III_current_check_counts.json',
    'S6_SERIES_PUBLISH_reading_III.md', 'S6_SERIES_PUBLISH_required_progress_III.tsv')
protected = {ROOT / name: (ROOT / name).read_bytes() for name in protected_names}
assert hashlib.sha256(original[source_path]).hexdigest() == payload['source_sha256'] == '5c03702c24467c3f471009cecd748be5e2d8138082c9fbc9abd13ddfe77372fe'
def table(body):
    return list(csv.DictReader(io.StringIO(body.decode(), newline=''), delimiter='\t'))
units = table(protected[ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv'])
unit, = [r for r in units if (r['paper'], r['unit_id'], r['defect_type']) == ('III', 'maps:src:D.2.35', 'D23')]
assert unit['status'] == 'open'
finding, = [r for r in table(protected[ROOT / 'S6_SERIES_PUBLISH_findings_III.tsv']) if r['id'] == 'P15']
assert finding['status'] == 'done'
build, = [r for r in table(protected[ROOT / 'S6_SERIES_PUBLISH_build_progress.tsv']) if r['paper'] == 'III']
assert build['status'] == 'open'
old_ids = {r['change_id'] for r in table(original[defect_path])}
assert len({r['change_id'] for r in rows}) == 2 and not old_ids.intersection(r['change_id'] for r in rows)
before = original[source_path].decode()
after = before
for row in rows:
    old, new = row['old_text'], row['new_text']
    assert after.count(old) == 1 and new not in after
    after = after.replace(old, new, 1)
reverse = after
for row in reversed(rows):
    assert reverse.count(row['new_text']) == 1
    reverse = reverse.replace(row['new_text'], row['old_text'], 1)
assert reverse.encode() == original[source_path]
for pattern in (r'\\(?:label|hypertarget|ref|eqref|cref|Cref)\{[^}]*\}', r'\d+'):
    assert re.findall(pattern, before) == re.findall(pattern, after)
def tokens(text):
    for layout in (r'\begin{gathered}', r'\end{gathered}', r'\quad', r'\\'):
        text = text.replace(layout, '')
    return re.sub(r'\s+', '', text)
assert tokens(before) == tokens(after)
matrix = re.search(r'\\begin\{pmatrix\}.*?\\end\{pmatrix\}', rows[0]['old_text'], re.S).group()
assert matrix in rows[0]['new_text']
assert after.count(r'\begin{gathered}') - before.count(r'\begin{gathered}') == 2
assert after.count(r'\end{gathered}') - before.count(r'\end{gathered}') == 2
stamp = datetime.now(timezone.utc).isoformat()
for index, row in enumerate(rows):
    row['old_page'] = 'Unaccepted current11 physical page ' + ('464' if index == 0 else '469') + '; actual root image reading and both final compiler diagnostics'
    row['review_status'] += ' Root admitted ' + stamp + ': ' + a.reviewed + ' Final successor images remain pending.'
output = io.StringIO(newline='')
writer = csv.DictWriter(output, fields, delimiter='\t', lineterminator='\n')
writer.writerows(rows)
candidate = {source_path: after.encode(), defect_path: original[defect_path] + output.getvalue().encode()}
assert all(b'\r' not in body for body in candidate.values())
assert table(candidate[defect_path])[-2:] == rows
staged, recovery, attempted = {}, {}, []
clean = False
try:
    for path in candidate:
        for dest, body, prefix in ((staged, candidate[path], 'c9-reflow-new-'), (recovery, original[path], 'c9-reflow-old-')):
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=prefix, delete=False) as f:
                dest[path] = Path(f.name)
                f.write(body)
                f.flush()
                os.fsync(f.fileno())
            assert dest[path].read_bytes() == body
    for path, body in {**original, **protected}.items():
        assert path.read_bytes() == body
    for path in candidate:
        attempted.append(path)
        os.replace(staged[path], path)
    for path, body in {**candidate, **protected}.items():
        assert path.read_bytes() == body
    clean = True
except BaseException:
    for path in reversed(attempted):
        assert path.read_bytes() in (candidate[path], original[path])
        assert recovery[path].read_bytes() == original[path]
        os.replace(recovery[path], path)
    for path, body in {**original, **protected}.items():
        assert path.read_bytes() == body
    clean = True
    raise
finally:
    if clean:
        for path in (*staged.values(), *recovery.values()):
            path.unlink(missing_ok=True)
print('Actual admission UTC', stamp)
print('Two exact D23 display reflows admitted; source reverse and original matrix bytes verified.')
print('Source SHA256', hashlib.sha256(source_path.read_bytes()).hexdigest())
print('No event, count, P15, unit-status, build-status or reading-record change.')
print('Already-open LE D23 and build gates remain open for current12/legacy11 and actual changed-page reading.')
