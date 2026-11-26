#!/usr/bin/env python3
"""Place the existing raw-class question in the final mathematical part."""
from pathlib import Path
from collections import Counter
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'agents/continuation8_iii_integration/units/later/limits_and_open_points.tex'
DEFECTS = ROOT / 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_carriers_publication_defects.tsv'
old = PATH.read_text()
anchor = r'\begin{problem}[Remaining filling and smooth classification]'
assert old.count(anchor) == 1
addition = r'''\begin{problem}[Unstable classes of the conical quotient maps]
\hypertarget{tag-Q30V}{}\label{mapsIII:problem:raw-conical-quotient-classes}
{\normalfont\scriptsize tag Q30V}\par
Use the fixed cusp disc, marked quotients, original finite fillings
and basepoint $x_0\in W$ of
\cref{wb:cusp-cone-S12-route,wb:cusp-cone-S24-route}.
For the based source homeomorphisms $h_2:X^{\wedge2}\to S^{12}$
and $h_4:X^{\wedge4}\to S^{24}$ of
\cref{wb:cusp-cone-optimal-exponents}, determine
\[
 [q_2^{\wedge2}h_2^{-1}]
       \in\pi_{12}(\mathcal A^{\wedge2}),\qquad
 [q_1^{\wedge4}h_4^{-1}]
       \in\pi_{24}(\mathcal C^{\wedge4}).
\]
The target homotopy equivalences are
\eqref{wb:cusp-cone-A-smash-wedge} and
\eqref{wb:cusp-cone-C-smash-wedge}.

The target maps $p_A=\widehat p_2$ and
$p_C=\widehat p_1p_{\mathcal C\mathcal B}$ of
\cref{wb:cusp-cone-optimal-exponents,wb:cusp-cone-angle-forgotten-sphere-carriers}
satisfy $p_Aq_2=\widehat q_3$ and
$p_Cq_1=\widehat q_\gamma$ on all of $X$.
Their smash powers send the displayed classes to the zero classes
computed in \cref{wb:cusp-cone-sphere-map-homotopy-status}.
The zero and nonzero surjective representatives in
\cref{wb:cusp-cone-target-homotopy-types} prove that the listed
ordinary invariants and homotopy-section obstruction do not
determine the two classes asked for here.
\end{problem}

'''
new = old.replace(anchor, addition + anchor)
identities = lambda s: Counter(re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}', s))
before, after = identities(old), identities(new)
assert all(after[k] == v for k, v in before.items())
assert set(after) - set(before) == {'tag-Q30V', 'mapsIII:problem:raw-conical-quotient-classes'}
lg = old[old.index(anchor):]
assert new[new.index(anchor):] == lg
with DEFECTS.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 73
rows.append(dict(change_id='c8-III-carriers-074', type='D13/D14/D20/D26',
    statement_id='mapsIII:problem:raw-conical-quotient-classes',
    old_location='037M proved insufficiency conclusion; final part before 02LG',
    old_page='pending final concordance', new_location='limits_and_open_points.tex before 02LG',
    new_page='pending final build', old_text=anchor, new_text=addition + anchor,
    reason='Give the two existing raw geometric class questions their final numbered problem, with exact source maps, target groups and postcomposition maps. Preserve the complete 037M zero/nonzero construction and the independently established angle-forgotten nullity; infer no raw class value.',
    review_status='new final problem awaiting immediate whole readback; final placement remains root-owned'))
PATH.write_text(new)
with DEFECTS.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('Added one final problem Q30V with both exact raw maps and target groups.')
print('Existing labels and targets retain their multiplicities; the complete 02LG suffix is byte-identical.')
print('Exact local defect row c8-III-carriers-074 written; no central file changed.')
