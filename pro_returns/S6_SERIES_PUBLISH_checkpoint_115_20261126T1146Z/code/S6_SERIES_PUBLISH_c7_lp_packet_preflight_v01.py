#!/usr/bin/env python3
"""Read-only literal-scope check of the LP record writer before its first run."""
from pathlib import Path
import ast

root = Path(__file__).resolve().parents[1]
old = root / 'agents/continuation7_iii_weighted_cups_root'
stage = root / 'agents/continuation7_iii_weighted_cups_receiving'
prefix = 'S6_SERIES_PUBLISH_III_02LP'
texts = {
    'os': (old / (prefix + '_released_statement.tex')).read_text(),
    'op': (old / (prefix + '_released_proof.tex')).read_text(),
    'np': (stage / (prefix + '_receiving.tex')).read_text(),
}
writer = root / 'code/S6_SERIES_PUBLISH_c7_lp_prepare_packet_v01.py'
tree = ast.parse(writer.read_text())
missing = []
count = 0
for node in ast.walk(tree):
    if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
        continue
    if node.func.id != 'part' or len(node.args) != 3:
        continue
    if not isinstance(node.args[0], ast.Name) or node.args[0].id not in texts:
        continue
    name = node.args[0].id
    start, end = map(ast.literal_eval, node.args[1:])
    text = texts[name]
    count += 1
    a = text.find(start)
    if a < 0:
        missing.append((node.lineno, name, 'start', start))
    elif text.find(end, a) < 0:
        missing.append((node.lineno, name, 'end', end))
print('READ_ONLY_PART_CHECKS', count)
for item in missing:
    print('UNRESOLVED_LITERAL', repr(item))
print('UNRESOLVED_COUNT', len(missing))
print('No record writer was executed; no proposal or canonical file was changed.')
