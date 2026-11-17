"""Register the fully audited reflected-fan characteristic pair, K46."""
from datetime import datetime, timezone
from pathlib import Path
import ast
import json

root = Path(__file__).resolve().parents[1]
path = root / 'code/update_report.py'
source = path.read_text()
source = source.replace('P3K.40–P3K.45', 'P3K.40–P3K.46')
old = 'This conclusion does not assign its separate characteristic pair or an integer derivative.'
new = (
    'P3K.46 supplies the actual reflected fixed-C0 cap map, retaining the full '
    'Picard unit and its winding, and proves the reflected Jin pair(6,0) with '
    'relative coordinates(0,-6,1). Its physical completion has pair(-6,0); '
    'the explicit parameter reversal gives the stated Jin convention. '
    'The separate nonfixed-edge integer and the general source-loop fan '
    'formula remain under proof.'
)
assert source.count(old) == 2
source = source.replace(old, new)
ast.parse(source)
path.write_text(source)
record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'statement': 'P3K.46',
    'active_include': 'notes/part3_source_cusp_reflected_pair.tex',
    'root_audit': 'records/root_audit_P3K_46.json',
    'standalone_qa': 'records/k46_standalone_visual_qa.json',
    'scope': 'The actual reflected fan and its fixed-C0 product; no general fan formula assigned.'
}
(root / 'records/checkpoint13_reflected_pair_inclusion.json').write_text(json.dumps(record, indent=2) + '\n')
print('Included and registered audited P3K.46.')
