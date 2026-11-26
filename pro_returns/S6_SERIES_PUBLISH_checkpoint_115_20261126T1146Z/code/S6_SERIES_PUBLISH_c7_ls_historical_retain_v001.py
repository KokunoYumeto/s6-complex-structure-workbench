"""Retain fetched LS bytes and expose only named helper definitions.

The complete helper is preserved as evidence, not executed or broadly read.
The first inline inspection printed only integer_solution and
component_geometry; this saved extraction repeats exactly that bounded scope.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import ast
import json

src = Path('/tmp/S6_SERIES_PUBLISH_c7_LS_historical')
dst = Path('agents/continuation7_iii_vertical_correction_receiving')
dst.mkdir(exist_ok=True)
print('START', datetime.now(timezone.utc).isoformat())
for p in sorted(src.iterdir()):
    blob = p.read_bytes()
    q = dst / p.name
    with q.open('xb') as handle:
        handle.write(blob)
    assert q.read_bytes() == blob
    print('RETAINED', q, 'BYTES', len(blob), 'SHA256', sha256(blob).hexdigest())
p = src / 'S6_SERIES_PUBLISH_manifolds_general_initial.py'
s = p.read_text()
lines = s.splitlines()
pieces = []
for n in ast.parse(s).body:
    if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in ('component_geometry', 'decomp', 'integer_solution', 'ikernel'):
        head = 'DEFINITION %s LINES %s %s' % (n.name, n.lineno, n.end_lineno)
        body = '\n'.join(lines[n.lineno-1:n.end_lineno])
        print(head)
        print(body)
        pieces.append('# ' + head + '\n' + body)
q = dst / 'S6_SERIES_PUBLISH_III_02LS_historical_helper_bounded_v001.py'
q.write_text('\n\n'.join(pieces) + '\n')
print('BOUNDED_EXTRACT', q, 'SHA256', sha256(q.read_bytes()).hexdigest())
for name in ('root_vertical_corrections', 'fourfolds_corrected_Mumford_examples'):
    data = json.loads((src / ('S6_SERIES_PUBLISH_' + name + '.json')).read_text())
    if isinstance(data, dict):
        print('JSON_SCHEMA', name, {k: len(v) if isinstance(v,(dict,list)) else type(v).__name__ for k,v in data.items()})
    else:
        print('JSON_SCHEMA', name, 'ROWS', len(data), 'ROW_KEYS', list(data[0]))
print('COMPLETE', datetime.now(timezone.utc).isoformat())
