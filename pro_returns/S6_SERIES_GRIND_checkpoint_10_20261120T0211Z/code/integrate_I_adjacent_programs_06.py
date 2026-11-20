"""Apply the thirteen reviewed Paper I actual-program replacements once."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
patch_path = ROOT / 'audit_paper_i/I_adjacent_program_patches.json'
assert hashlib.sha256(patch_path.read_bytes()).hexdigest() == '7d1cf833eb0190cbd33b39dcd102d9d1a933a936041d7ff12d111af43256e580'
program = ROOT / 'audit_paper_i/code/adjacent_exact.py'
output = ROOT / 'audit_paper_i/code/adjacent_exact.output.json'
data = json.loads(output.read_text())
assert data['source_sha256'] == hashlib.sha256(program.read_bytes()).hexdigest()
assert data['passed'] == 55 and len(data['data']['root_count_rows']) == 481
assert all(x['result'] == 'PASS' for x in data['checks'])
body = ROOT / 'parts/I.body.linked.tex'
source = body.read_text()
before = hashlib.sha256(source.encode()).hexdigest()
patches = json.loads(patch_path.read_text())
for patch in patches:
    assert source.count(patch['old']) == 1, patch['label']
    source = source.replace(patch['old'], patch['new'], 1)
body.write_text(source)
receipt = dict(
    utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    before_sha256=before,
    after_sha256=hashlib.sha256(source.encode()).hexdigest(),
    program_sha256=data['source_sha256'],
    output_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),
    applied=patches,
    review='Root read all thirteen replacements and the entire independent program before applying; fresh execution remains attributed to its producing audit.',
    scope='Exact algebra, integral lattices, bounded root counts, local maps and signature example only; no analytic extension, properness or coherent-base-change claim is supplied by this code.',
)
(ROOT / 'analysis/I_adjacent_program_integration_06.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'applied': len(patches), 'named_checks': data['passed'], 'root_count_rows': 481}))
