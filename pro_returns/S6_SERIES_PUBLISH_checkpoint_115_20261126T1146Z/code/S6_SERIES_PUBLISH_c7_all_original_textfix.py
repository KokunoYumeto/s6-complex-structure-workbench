#!/usr/bin/env python3
"""Repair inline math delimiters in the freshly authored L7 note only."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
p = root / 'agents/continuation7_iii_all_original/S6_SERIES_PUBLISH_III_02L7_fresh_derivation.md'
s = p.read_text()
parts = re.split(r'(\\\[[\s\S]*?\\\])', s)
changed = 0
for j in range(0, len(parts), 2):
    t, out, i = parts[j], [], 0
    while i < len(t):
        if t[i] != '(' or (i and t[i-1] == '\\'):
            out.append(t[i]); i += 1
            continue
        start, depth, k = i, 1, i+1
        while k < len(t) and depth:
            depth += (t[k] == '(') - (t[k] == ')')
            k += 1
        if depth:
            out.append(t[i]); i += 1
            continue
        interior = t[start+1:k-1]
        math = ('\\' in interior or any(c in interior for c in '=^_<>')
                or bool(re.fullmatch(r'[A-Za-z0-9,+*/ -]{1,16}', interior))
                and ' ' not in interior)
        if interior.isdigit() or interior == 'OpenAI':
            math = False
        if math:
            out.extend(['\\(', interior, '\\)'])
            changed += 1
        else:
            out.append(t[start:k])
        i = k
    parts[j] = ''.join(out)
s = ''.join(parts)
s = s.replace('s=0,qquad', r's=0,\qquad')
s = s.replace('h(z)/|z|,quad', r'h(z)/|z|,\quad')
s = s.replace('to the last two relations,\n', 'to the second and first relations in that order,\n')
p.write_text(s)
print('Repaired inline mathematical delimiters:', changed)
print('Repaired two display spacing escapes and specified the row-operation order.')
