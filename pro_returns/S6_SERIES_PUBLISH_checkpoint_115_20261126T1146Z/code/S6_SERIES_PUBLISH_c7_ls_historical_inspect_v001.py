"""Bounded structural inspection of the retained LS historical evidence.

No historical code is executed.  Only the named compute/local_lift
definitions and import declarations in their helper are exposed.
"""
from pathlib import Path
from datetime import datetime, timezone
import ast
import json

lane = Path('agents/continuation7_iii_vertical_correction_receiving')
print('START', datetime.now(timezone.utc).isoformat())
p = lane / 'S6_SERIES_PUBLISH_manifolds_general_initial.py'
text = p.read_text()
lines = text.splitlines()
for node in ast.parse(text).body:
    if isinstance(node, (ast.Import, ast.ImportFrom)) or (isinstance(node, ast.FunctionDef) and node.name in ('compute','local_lift')):
        print('HELPER_LINES', node.lineno, node.end_lineno)
        print('\n'.join(lines[node.lineno-1:node.end_lineno]))
old = json.loads((lane / 'S6_SERIES_PUBLISH_fourfolds_corrected_Mumford_examples.json').read_text())
row = old[0]
for key,value in row.items():
    if key in ('local','H1_matrix','H2_matrix'):
        print('ROW_FIELD',key,'TYPE',type(value).__name__)
        if isinstance(value,dict):
            print('FIELD_KEYS',list(value))
            for name,item in value.items():
                if isinstance(item,list):
                    print('SUBFIELD',name,'LEN',len(item),'FIRST_TYPE',type(item[0]).__name__ if item else 'empty')
                else:
                    print('SUBFIELD',name,item)
        elif isinstance(value,list):
            print('FIELD_LEN',len(value),'FIRST',value[0])
    else:
        print('ROW_FIELD',key,json.dumps(value,separators=(',',':')))
print('COMPLETE', datetime.now(timezone.utc).isoformat())
