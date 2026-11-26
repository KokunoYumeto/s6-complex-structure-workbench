#!/usr/bin/env python3
"""Place the final questions and record exact exposed publication edits."""
from pathlib import Path
import csv
import hashlib
import re
from collections import Counter
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'agents/continuation8_iii_integration/units/later/limits_and_open_points.tex'
OUT = ROOT / 'agents/continuation8_iii_later'
old = PATH.read_text()
assert len(old.splitlines()) == 191
new = old
changes = []

def edit(before, after, kind, sid, reason):
    global new
    assert new.count(before) == 1
    pos = new.index(before)
    changes.append(dict(type=kind, statement_id=sid,
        old_location='limits_and_open_points.tex sequential edit line ' + str(new[:pos].count('\n') + 1),
        old_page='pending final concordance', new_location='same final part', new_page='pending final build',
        old_text=before, new_text=after, reason=reason,
        review_status='whole initial final fragment and prior mathematical scope read; final readback pending'))
    new = new[:pos] + after + new[pos+len(before):]

edit(r'\part{Results not yet established}' + '\n' + r'\section{Limits and open points}',
     r'\part{Open problems}' + '\n' + r'\section{Further classification problems}' + '\n' + r'\subsection{Section lines and sphere multiplicities}',
     'D01/D14/D16', 'maps:rem:natural-sphere-sector-scope',
     'Give the final part mathematical headings and actual subsection boundaries after the completed preceding constructions.')
edit(r'\begin{problem}[Smooth compactifications of finite cusp covers]',
     r'''\begin{problem}[Degree-zero lines and sphere multiplicities]
\hypertarget{tag-Q30Z}{}\label{mapsIII:problem:degree-zero-lines-and-multiplicities}
{\normalfont\scriptsize tag Q30Z}\par
In the elliptic-surface logarithmic construction, allow the arbitrary
fibrewise degree-zero line bundles of
\cite[Remark~8.5]{manEngel26}. Complete the integral cap-map and
filling classification for the remaining choices, and determine
which initial configurations admit infinitely many sphere-producing
multiplicities, as asked in \cite[Question~4, p.~2]{manViaclovskyLogs26}.

The natural and vertically corrected section-line families are the
specializations $M=\mathcal O(P-O)$ and
$M=\mathcal O(P-O+V)$ of \cref{maps:src:D.2.22}.
With the marked section pair, divisor, linearization and filling data
retained, the comparison on either specialization is the identity on
the line bundle and its quotient construction, with identity inverse.
The finite initial-data reduction in that theorem and the integral
algorithms and smooth sectors cited in
\cref{maps:rem:natural-sphere-sector-scope,maps:src:D.2.4}
give the established reductions for those specializations and their
stated filling families.
\end{problem}

\subsection{Cusp compactifications and quotient classes}
\begin{problem}[Smooth compactifications of finite cusp covers]''',
     'D11/D13/D14/D18/D26', 'mapsIII:problem:degree-zero-lines-and-multiplicities',
     'Preserve the removed KX public-question scope once in the final part, with exact identity maps for both established section-line specializations. Do not infer a separation of the two published questions or completion from row counts. Engel page expansion remains root D18 work.')
edit(r'\begin{problem}[Remaining filling and smooth classification]',
     r'\subsection{Remaining cap maps and smooth types}' + '\n' + r'\begin{problem}[Remaining filling and smooth classification]',
     'D14', 'maps:src:D.2.4', 'Place the single admitted LG problem after the completed metric and carrier constructions, with its own actual final subsection.')
edit(r'\textnormal{\scriptsize(tag 02LG)}\par',
     r'{\normalfont\scriptsize tag 02LG}\par', 'D10', 'maps:src:D.2.4',
     'Use the same small visible tag style as the other formal statements; change no mathematical LG text.')

for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}']:
    before, after = Counter(re.findall(pattern,old)), Counter(re.findall(pattern,new))
    assert all(after[k] == v for k,v in before.items())
    assert all(v == 1 for k,v in after.items() if k not in before)
lg = 'Determine the marked integral cap maps and oriented smooth types in'
assert old[old.index(lg):] == new[new.index(lg):]
PATH.write_text(new)
with (OUT / 'S6_SERIES_PUBLISH_III_limits_publication_defects.tsv').open('w', newline='') as handle:
    writer = csv.DictWriter(handle, list(changes[0]), delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(changes)
print('Final part lines', len(new.splitlines()), 'SHA256', hashlib.sha256(new.encode()).hexdigest())
print('Local edit rows', len(changes), 'all prior label/target multiplicities preserved; LG mathematical suffix byte-identical.')
for i,line in enumerate(new.splitlines(),1):
    if line.startswith(r'\subsection'):
        print('Unit', i, line)
print('Only new tag Q30Z; no canonical/shared mutations, no proof or criterion credit.')
