"""Place the three re-derived family applications next to their statements.

This editorial operation grants no check. The actual current derivations and
opened input theorems are recorded separately in records/root_events.tsv.
The original S6_09 source remains unchanged.
"""
from pathlib import Path
import json, re

OUT = Path(__file__).resolve().parents[2]
BASE = OUT.parents[1]
SOURCE = BASE / 'sources/s6_09/S6_09_PAPERS_I.tex'
text = SOURCE.read_text()
index = json.loads((OUT / 'analysis/inventory_source_index.json').read_text())
revisions = OUT / 'papers/I/revisions'

for sid in ('D.1.2', 'D.1.6', 'D.2.3'):
    label = 'fam:src:' + sid
    loc = index['S6_02_FAMILY:' + sid]
    statement = text[loc['start']:loc['statement_end']]
    anchor = r'\label{app:rederive:fam-src-' + sid + '}'
    start = text.index(r'\begin{proof}', text.index(anchor))
    end = text.index(r'\end{proof}', start) + len(r'\end{proof}')
    proof = text[start:end]
    proof = proof.replace(r'\begin{proof}', r'\begin{proof}' + '\n' + anchor, 1)
    proof = proof.replace(r'\cite[Theorems 4.1 and 4.4]{Schnell19}',
                          r'\cite[Theorem 4.1, p.~1, and Theorem 4.4, p.~3]{Schnell19}')
    proof = proof.replace(r'\cite[Theorem 4.1 and equation (4.3)]{Schnell19}',
                          r'\cite[Theorem 4.1, p.~1, and equation (4.3), p.~2]{Schnell19}')
    uses = {
        'D.1.2': r'\cref{fam:src:C.2.1,fam:src:D.1.1}; the explicit lattice map and section intersection computation below; \cite[Lemma 2.1]{Engel2026}; \cite[Theorem 4.4, p.~3]{Schnell19}',
        'D.1.6': r'\cref{fam:eq:cd-NS,fam:src:D.1.4}; \cite[Theorem 4.1, p.~1, and Theorem 4.4, p.~3]{Schnell19}',
        'D.2.3': r'\cref{fam:src:D.1.6,fam:src:D.2.1,fam:src:D.2.2}; \cite[Theorem 4.1 and equation (4.3), pp.~1--2]{Schnell19}',
    }[sid]
    (revisions / (label.replace(':', '_') + '.tex')).write_text(
        statement + '\n\\Uses{' + uses + '}\n' + proof + '\n')
    print(label, 'full application proof integrated')
