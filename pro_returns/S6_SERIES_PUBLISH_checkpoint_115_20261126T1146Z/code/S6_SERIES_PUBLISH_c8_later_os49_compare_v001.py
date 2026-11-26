#!/usr/bin/env python3
"""Exact extraction comparison before OS49 publication edits; no source mutation."""
from pathlib import Path
from hashlib import sha256
import difflib

ROOT = Path(__file__).resolve().parents[1]
LATER = ROOT / 'agents/continuation8_iii_integration/units/later'
rows = [('02S2','26','os49_construction','continuation6_iii_finite'),
        ('02S3','27','os49_construction','continuation6_iii_finite'),
        ('02S4','28','os49_construction','continuation6_iii_finite'),
        ('02S5','29','os49_construction','continuation6_iii_finite'),
        ('02S8','31','os49_graph_caps','continuation7_iii_graph'),
        ('02S9','32','os49_graph_caps','continuation7_iii_graph')]
for tag, number, stem, folder in rows:
    source = (LATER / (stem + '.tex')).read_text()
    start = source.index('\\label{night:P3F.' + number + '}')
    start = source.index('\\begin{proof}', start)
    end = source.index('\\end{proof}', start) + len('\\end{proof}')
    extracted = source[start:end] + '\n'
    receiver_path = ROOT / 'agents' / folder / ('S6_SERIES_PUBLISH_III_' + tag + '_receiving.tex')
    receiver = receiver_path.read_text()
    a = receiver.index('\\begin{proof}')
    b = receiver.index('\\end{proof}', a) + len('\\end{proof}')
    proof = receiver[a:b] + '\n'
    print('PROOF', tag, 'EXTRACTED_LINES', len(extracted.splitlines()),
          'RECEIVER_LINES', len(proof.splitlines()), 'RECEIVER_SHA256', sha256(receiver_path.read_bytes()).hexdigest())
    print('EXACT_PROOF_IDENTITY', extracted == proof)
    if extracted != proof:
        print(''.join(difflib.unified_diff(proof.splitlines(True), extracted.splitlines(True),
                                         fromfile=tag + '_receiver', tofile=stem + '_extracted')), end='')
print('SA_SB_HAVE_NO_REQUIRED_ROW_OR_C4_C7_RECEIVER; CURRENT_SOURCE_IS_EXPOSED_PUBLICATION_INPUT')
