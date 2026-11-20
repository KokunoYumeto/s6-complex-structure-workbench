"""Apply the reviewed fresh cusp calculation replacement once."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
patch_path = ROOT / 'audit_paper_i/I_cusp_hexagon_program_patch.json'
assert hashlib.sha256(patch_path.read_bytes()).hexdigest() == '720dbc567dce37f2dbb1cea08d759bbbcd5d9aa7ec62a8b43122ce0e159f3e13'
program = ROOT / 'audit_paper_i/code/cusp_hexagon_exact.py'
output = ROOT / 'audit_paper_i/code/cusp_hexagon_exact.output.json'
data = json.loads(output.read_text())
assert data['source_sha256'] == hashlib.sha256(program.read_bytes()).hexdigest()
assert data['passed'] == 65 and all(c['result'] == 'PASS' for c in data['checks'])
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
    review='Root read the entire original theorem and proof, the exact program and guarded replacement; fresh after-reading verification remains attributed to its producing audit.',
    scope='Complete integral fan automorphism enumeration, oriented side pushforward and character pullback, symbolic cusp constants and obstructions; the normalization and quotient arguments remain the printed geometric proof.'
)
(ROOT / 'analysis/I_cusp_program_integration_06.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'applied': len(patches), 'named_checks': data['passed']}))
