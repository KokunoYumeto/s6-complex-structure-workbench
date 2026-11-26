"""Preserve GL computation bytes and prepare the complete Programs pair."""
from pathlib import Path
import csv
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]
base = 'agents/ii_checks_provenance/recovery_20261121T2000Z/clean_group12/'
mp = base + 'S6_SERIES_PUBLISH_II_clean_group12_computation_methods.json'
methods = json.loads((R / mp).read_text())
copies = []
items = [methods[key] for key in ('prereading_program', 'prereading_output',
    'prereading_receipt', 'old_slice', 'old_slice_receipt', 'old_output',
    'postrelease_program', 'postrelease_output')]
execution = base + 'S6_SERIES_PUBLISH_II_clean_group12_execution_receipt.json'
items.append({'path': execution, 'sha256': 'e1437d02ca0f679bc0a058f94b71a4435311965284584ddd7d23ed193f2c5ca9'})
for item in items:
    data = (R / item['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256']
    destination = 'code/' + Path(item['path']).name
    assert not (R / destination).exists()
    (R / destination).write_bytes(data)
    copies.append({'source': item['path'], 'destination': destination, 'sha256': item['sha256']})
source = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
assert hashlib.sha256(source.encode()).hexdigest() == '0451c788c5cfab04e0a2b0ec8075f440752f26ae8b19395aae5a975227dd6cf1'
end = '\\end{longtable}'
start = source.index('\\section*{Programs}')
stop = source.index(end, start) + len(end)
old = source[start:stop]
assert old.count('\\href{') == 19
rows = []
for title, key in [
    ('Cusp normalization jets, conductor cochains, weighted cohomology and restriction-map inverses', 'prereading_program'),
    ('Critical-value norm and exact cusp jet basis changes', 'postrelease_program')
]:
    name = Path(methods[key]['path']).name
    rows.append(title + r' (\cref{cdp:st:E14}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/' + name + r'}{\nolinkurl{' + name + r'}} \\[3pt]' + '\n')
new = old[:-len(end)] + ''.join(rows) + end
assert new.count('\\href{') == 21
folder = R / 'records/S6_SERIES_PUBLISH_II_GL_context_pairs'
folder.mkdir(exist_ok=False)
bindings = {}
for kind, data in [('before', old), ('after', new)]:
    path = folder / ('programs_' + kind + '.tex')
    path.write_text(data)
    bindings['program_table_' + kind] = {'path': str(path.relative_to(R)),
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
ledger = R / 'CHECK_EVENTS.tsv'
with ledger.open() as stream:
    historical_rows = [row for row in csv.DictReader(stream, delimiter='\t')
                       if row['statement_id'] == 'cdp:st:E14']
assert len(historical_rows) == 5
out = R / 'records/S6_SERIES_PUBLISH_II_GL_code_and_programs_binding.json'
assert not out.exists()
record = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    copies=copies, **bindings, prior_rows=19, new_rows=21,
    source_sha256=hashlib.sha256(source.encode()).hexdigest(),
    ledger_sha256=hashlib.sha256(ledger.read_bytes()).hexdigest(),
    exact_historical_owner_rows=historical_rows, canonical_writes=0,
    run_credit=0, reading_credit=0,
    scope='Byte-identical computation copies and exactly two table rows. All nineteen current rows and the common repository commit macro are retained. The five exact owner ledger rows were actually read before this capture; this script adds no reading or mathematical credit.')
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'record': str(out.relative_to(R)),
    'sha256': hashlib.sha256(out.read_bytes()).hexdigest(), 'copies': copies,
    'prior_rows': 19, 'new_rows': 21}, indent=2))
