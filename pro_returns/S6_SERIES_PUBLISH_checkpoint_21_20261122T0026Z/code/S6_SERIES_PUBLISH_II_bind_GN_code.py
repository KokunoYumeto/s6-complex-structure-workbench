"""Preserve GN computation versions and prepare its exact Programs pair."""
from pathlib import Path
import csv
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]
base = 'agents/ii_infra/recovery_20261121/'
proposal_path = base + 'S6_SERIES_PUBLISH_II_01GN_program_table_proposal_v2.json'
assert hashlib.sha256((R / proposal_path).read_bytes()).hexdigest() == 'a178afd103a5efc25736b4a1e3874d6f75dd6948e197fb6a8f111b2297998095'
proposal = json.loads((R / proposal_path).read_text())
copies = []
items = []
for row in proposal['rows']:
    for key in ['program', 'output']:
        items.append((row[key], row['copy_' + key + '_to']))
for name in ['S6_SERIES_PUBLISH_II_01GN_prereading_certificate.py',
             'S6_SERIES_PUBLISH_II_01GN_prereading_certificate_output.json',
             'S6_SERIES_PUBLISH_II_01GN_prereading_certificate_failed_run_01.json',
             'S6_SERIES_PUBLISH_II_01GN_prereading_input_receipt_v2.json',
             'S6_SERIES_PUBLISH_II_01GN_postrelease_program_scope_audit.json']:
    path = base + name
    items.append(({'path': path, 'sha256': hashlib.sha256((R / path).read_bytes()).hexdigest()},
                  'code/' + name))
for item, destination in items:
    data = (R / item['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256']
    assert not (R / destination).exists()
    (R / destination).write_bytes(data)
    copies.append({'source': item['path'], 'destination': destination, 'sha256': item['sha256']})
source = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
assert hashlib.sha256(source.encode()).hexdigest() == '801f7d402b26585a0f86cdb4e501e09b000965bf9ff22941cc737b1e3804a532'
end = '\\end{longtable}'
start = source.index('\\section*{Programs}')
stop = source.index(end, start) + len(end)
old = source[start:stop]
assert old.count('\\href{') == 21
addition = ''.join(row['table_row_tex'] + '\n' for row in proposal['rows'])
new = old[:-len(end)] + addition + end
assert new.count('\\href{') == 23
folder = R / 'records/S6_SERIES_PUBLISH_II_GN_context_pairs'
folder.mkdir(exist_ok=False)
bindings = {}
for kind, data in [('before', old), ('after', new)]:
    path = folder / ('programs_' + kind + '.tex')
    path.write_text(data)
    bindings['program_table_' + kind] = {'path': str(path.relative_to(R)),
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
ledger = R / 'CHECK_EVENTS.tsv'
with ledger.open() as stream:
    history = [row for row in csv.DictReader(stream, delimiter='\t')
               if row['statement_id'] == 'cdp:st:E16']
assert len(history) == 4
out = R / 'records/S6_SERIES_PUBLISH_II_GN_code_and_programs_binding.json'
assert not out.exists()
record = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    copies=copies, **bindings, prior_rows=21, new_rows=23,
    source_sha256=hashlib.sha256(source.encode()).hexdigest(),
    ledger_sha256=hashlib.sha256(ledger.read_bytes()).hexdigest(),
    exact_historical_owner_rows=history, canonical_writes=0, run_credit=0, reading_credit=0,
    scope='Byte-identical successful and failed computation versions/output/receipts are preserved. Exactly two reviewed program rows are appended to the complete current table. The four exact historical owner rows were read by root before this capture; this script adds no reading or mathematical event.')
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'record': str(out.relative_to(R)), 'sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
    'copies': copies, 'prior_rows': 21, 'new_rows': 23}, indent=2))
