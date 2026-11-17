"""Update the hourly report after the completed ordinary fixed-curve audit."""
from datetime import datetime, timezone
from pathlib import Path
import ast
import json

root = Path(__file__).resolve().parents[1]
path = root / 'code/update_report.py'
text = path.read_text()
old = 'The connecting-map sign, common-exterior variation correction, separate nonfixed-edge integer and general source-loop fan formula remain under proof.'
new = ('The subsequent ordinary-product working proof fixes the connecting sign by the explicit D3-cylinder extension and Stokes orientation, and gives fixed-C0 relative coordinates(6,-6,1), variation0 and ambient relative derivative-12. Its root audit and thirteen exact checks are retained, together with the two native-to-ordinary nonfixed frame maps. The native nonfixed integers, mutual common-exterior variations and general source-loop fan formula remain under proof.')
count = text.count(old)
assert count == 2, count
candidate = text.replace(old, new)
ast.parse(candidate)
record = {'utc': datetime.now(timezone.utc).isoformat(), 'old': old, 'new': new,
          'replacements': count, 'status': 'PASS',
          'scope': 'Working-note progress only; master47 and its229 registered statements are unchanged.'}
(root / 'records/checkpoint13_ordinary_relative_report_update.json').write_text(json.dumps(record, indent=2) + '\n')
path.write_text(candidate)
print(json.dumps(record, indent=2))
