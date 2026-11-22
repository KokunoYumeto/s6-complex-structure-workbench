"""Preserve exact GI programs/outputs and prepare its two end-table rows."""
from pathlib import Path
import datetime
import hashlib
import json

R = Path(__file__).resolve().parents[1]
base = 'agents/ii_infra/recovery_20261121/'
comparison = json.loads((R / (base + 'S6_SERIES_PUBLISH_II_01GI_comparison.json')).read_text())
copies = []
for key in ('fresh_program', 'fresh_output', 'different_method_program',
            'different_method_output', 'old_slice', 'old_run'):
    item = comparison[key]
    data = (R / item['path']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == item['sha256']
    destination = 'code/' + Path(item['path']).name
    assert not (R / destination).exists()
    (R / destination).write_bytes(data)
    copies.append({'source': item['path'], 'destination': destination, 'sha256': item['sha256']})

source = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
assert hashlib.sha256(source.encode()).hexdigest() == '7da6ccc1170e25175a8feec240949bf6740eda6c94e7361f59b5a44c5c0e5107'
end = '\\end{longtable}'
start = source.index('\\section*{Programs}')
stop = source.index(end, start) + len(end)
old = source[start:stop]
assert old.count('\\href{') == 15
rows = []
for title, key in [
    ('Integral marking, period and root-coordinate maps, and weighted-line cohomology', 'fresh_program'),
    ('Hilbert-series recurrence and the degree-three Riemann--Roch expansion', 'different_method_program')
]:
    name = Path(comparison[key]['path']).name
    rows.append(title + r' (\cref{cdp:st:E11}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/' + name + r'}{\nolinkurl{' + name + r'}} \\[3pt]' + '\n')
new = old[:-len(end)] + ''.join(rows) + end
assert new.count('\\href{') == 17
folder = R / 'records/S6_SERIES_PUBLISH_II_GI_context_pairs'
folder.mkdir(exist_ok=False)
bindings = {}
for kind, data in [('before', old), ('after', new)]:
    path = folder / ('programs_' + kind + '.tex')
    path.write_text(data)
    bindings['program_table_' + kind] = {
        'path': str(path.relative_to(R)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
out = R / 'records/S6_SERIES_PUBLISH_II_GI_code_and_programs_binding.json'
assert not out.exists()
record = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              copies=copies, **bindings, prior_rows=15, new_rows=17,
              source_sha256=hashlib.sha256(source.encode()).hexdigest(),
              canonical_writes=0, run_credit=0, reading_credit=0,
              scope='Byte-identical copies only; exact two-row table addition retaining all current rows. Common repository macro retained; no remote availability asserted.')
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'record': str(out.relative_to(R)), 'sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
                  'copies': copies, 'prior_rows': 15, 'new_rows': 17}, indent=2))
