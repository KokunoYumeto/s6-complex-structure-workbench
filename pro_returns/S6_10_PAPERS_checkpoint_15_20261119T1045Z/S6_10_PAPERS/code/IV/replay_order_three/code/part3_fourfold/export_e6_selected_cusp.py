#!/usr/bin/env python3
"""P3K.95 complete proof export; leaves all central includes untouched."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[2]
src = BASE / 'notes/part3_e6_selected_cusp_working.md'
body = src.read_text()
body = body[body.index('## Statement'):]
protected = {}


def store_span(value):
    key = 'PROTECTEDSPAN' + str(len(protected)) + 'END'
    protected[key] = value
    return key


def hold(match):
    return store_span(match.group(0))


body = re.sub(r'\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)', hold, body)
body = re.sub(
    r'^## (.+)$',
    lambda m: r'\par\medskip\noindent\textbf{' + m.group(1)
              + r'.}\par\nopagebreak[4]',
    body, flags=re.M)
body = re.sub(r'\*([^*\n]+)\*',
              lambda m: r'\emph{' + m.group(1) + '}', body)
tick = chr(96)
body = re.sub(tick + '([^' + tick + r'\n]+)' + tick,
              lambda m: store_span(r'\path{' + m.group(1) + '}'), body)
body = re.sub(r'(?<!\\)_', r'\\_', body)
body = re.sub(r'(?<!\\)\^', r'\\textasciicircum{}', body)
body = re.sub(r'(?<!\\)%', r'\\%', body)
for key, value in protected.items():
    body = body.replace(key, value)
cut = body.index(r'\par\medskip\noindent\textbf{EC.1.')
include = (
    r'\subsection{The E6 selected cusp with its actual finite cap}' + '\n'
    + r'\begin{statement}{P3K.95}{Proved}' + '\n'
    + body[:cut] + r'\end{statement}' + '\n'
    + r'\begin{proof}' + '\n' + body[cut:]
    + r'\end{proof}' + '\n')
out = BASE / 'notes/part3_e6_selected_cusp.tex'
out.write_text(include)
template = (BASE / 'code/part3_fourfold/k93_standalone.tex').read_text()
template = template.replace('part3_source_infinity_closed_formula.tex',
                            'part3_e6_selected_cusp.tex')
(BASE / 'code/part3_fourfold/k95_standalone.tex').write_text(template)
record = {
    'id': 'P3K.95',
    'status': 'Proved; standalone visual QA pending',
    'utc': datetime.now(timezone.utc).isoformat(),
    'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
    'tex_sha256': hashlib.sha256(out.read_bytes()).hexdigest(),
    'root_and_peer_audit':
        'Full root and independent peer audits passed EC.1–7; the final '
        'literal EU sector/reference and Hopf/Gysin/MV orbit additions '
        'also passed, including even-zeta descent.',
    'scope': 'M6, b=1, m=2, both primitive norm signs, every retained '
             'character/reference, fixed scalar, positive ordered w loop, '
             'all selected lattice-basis fans.',
    'qa': 'pending',
    'master_modified': False,
}
(BASE / 'records/k95_proof_assembly.json').write_text(
    json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
