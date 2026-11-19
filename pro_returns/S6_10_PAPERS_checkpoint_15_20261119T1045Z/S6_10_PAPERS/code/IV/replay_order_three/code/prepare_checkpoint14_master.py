"""Preserve build47 and include the seven fully audited new proofs."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
dest = root / 'records/checkpoint14_prior_master47'
dest.mkdir(exist_ok=True)
record = {'utc': datetime.now(timezone.utc).isoformat(), 'master_build': 47,
          'reason': 'Preserve the preceding master and log before including K50–56.', 'files': {}}
for name in ['S6_06_BLIND_paper.pdf', 'S6_06_BLIND_paper.log']:
    source, target = root / name, dest / name
    assert not target.exists(), target
    shutil.copy2(source, target)
    record['files'][name] = {'bytes': source.stat().st_size,
        'sha256': hashlib.sha256(source.read_bytes()).hexdigest()}
assert record['files']['S6_06_BLIND_paper.pdf']['sha256'] == '2f3d49d0d8443d69ccd2f7a28a195eaf0c2970e692e41ffc5f00485eacc4ef34'
(dest / 'preservation.json').write_text(json.dumps(record, indent=2) + '\n')
names = ['source_cusp_ordinary_relative', 'source_cusp_circle_trace',
         'source_cusp_stable_trace', 'source_unselected_collision',
         'source_cusp_first_flops', 'source_cusp_general_fan_product',
         'source_cusp_vertical_fans']
target = root / 'notes/part3.tex'
content = target.read_text()
for name in names:
    path = 'notes/part3_' + name + '.tex'
    assert (root / path).is_file(), path
    include = '\\input{' + path + '}'
    assert include not in content, include
    content += '\n' + include + '\n'
target.write_text(content)
print('Preserved build47 and included K50–56. No archive created.')
