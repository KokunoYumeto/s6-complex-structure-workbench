"""Apply the exact outstanding pass08 layout and paragraph-anchor repairs."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
csv.field_size_limit(100000000)
s = SOURCE.read_text()
original = s
edits = []

def edit(name, old, new, types, owner, reason):
    global s
    assert s.count(old) == 1, (name, s.count(old))
    s = s.replace(old, new, 1)
    edits.append(dict(change_id='III-C9-LAYOUT-' + name, type=types,
                      statement_id=owner, old_location='cp100/pass08 visual finding; exact source guard',
                      old_page='', new_location='same statement or labelled heading', new_page='',
                      old_text=old, new_text=new, reason=reason,
                      review_status='exact source comparison admitted; current rendered page and hyperlink verification pending'))

edit('positive-dimensional',
     'The hexagonal toric surface has six point orbits; its positive-\ndimensional torus orbits have Euler characteristic zero. Hence',
     'The hexagonal toric surface has six point orbits; its\npositive-dimensional torus orbits have Euler characteristic zero. Hence',
     'D23', 'maps:src:D.2.43',
     'Pass08 page112: move the line break before the compound word; all orbit and characteristic-class assertions are unchanged.')

for name, start, end, owner in [
    ('component-table', r'\begin{tabular}{lp{0.47\textwidth}cl}', r'\end{tabular}', 'maps:src:D.2.31'),
    ('chern-table', 'Type & \\(s_i\\) & \\(q_i^c\\) & Local free cokernel', r'\end{tabular}', 'maps:src:D.2.32'),
]:
    a = s.index(start); b = s.index(end, a) + len(end)
    old = s[a:b]
    new = old
    for raw, math in [('III*', r'\(III^*\)'), ('IV*', r'\(IV^*\)'), ('I3*', r'\(I_3^*\)'), ('I1*', r'\(I_1^*\)')]:
        new = new.replace('\n' + raw + ' &', '\n' + math + ' &')
    assert new != old
    edit(name, old, new, 'D20;D23', owner,
         'Pass08 pages306 and319: print each existing Kodaira symbol with its specified star and numerical subscript. Every table coefficient and component action remains byte-identical.')

edit('component-prose',
     'of all remaining components: the III* outer exchange forces the\ntwo long-arm exchanges, the IV* outer cycle forces its three',
     'of all remaining components: the \\(III^*\\) outer exchange forces the\ntwo long-arm exchanges, the \\(IV^*\\) outer cycle forces its three',
     'D20;D23', 'maps:src:D.2.31',
     'The adjacent prose uses the same Kodaira symbols as the corrected component table; only mathematical typography changes.')

for name, heading in [('integral-exterior-heading', 'The integral exterior on all natural rows.'),
                      ('global-fan-heading', 'The global comparison of cusp fans.')]:
    old = '\\item \\emph{' + heading + '}'
    edit(name, old, '\\Needspace{5\\baselineskip}\n' + old,
         'D14;D23', 'maps:src:D.2.31',
         'Pass08 orphan proof-item heading on page307 or311: reserve five text baselines before the heading so its first paragraph remains with it; mathematical text is unchanged.')

old = '\\subsection{Integral homology of every free cap}'
edit('free-cap-heading', old, '\\Needspace{9\\baselineskip}\n' + old,
     'D14;D23', 'night:P3F.34',
     'Pass08 page582: the subsection and theorem title stood without statement text. Reserve nine baselines for the subsection, theorem title, tag and opening statement; preserve their order and content.')

formal = [
    'mapsIII:rem:cusp-replacement', 'maps:src:B.5.1', 'mapsaudit:finite-degree-three',
    'maps:src:C.1.2', 'maps:src:D.1.10', 'maps:src:D.2.2', 'maps:src:D.2.16',
    'maps:src:D.2.29', 'maps:src:D.2.44', 'wb:cusp-s12-all-higher-smashes-null',
    'mapsIII:lem:radial-slice-embeddings', 'wb:cusp-cone-metric-scope',
    'wb:cusp-cone-S12-sphere-map-null', 'wb:cusp_s12_carrier_homotopy:L567',
    'wb:cusp-s12-native-smash-null',
]
for i, label in enumerate(formal, 1):
    token = '\\label{' + label + '}'
    pos = s.index(token)
    matches = list(re.finditer(r'\\begin\{(?:theorem|lemma|proposition|corollary|remark|computed)\}', s[:pos]))
    a = matches[-1].start()
    old = s[a:pos + len(token)]
    assert len(old) < 500
    edit('statement-space-' + str(i).zfill(2), old,
         '\\Needspace{6\\baselineskip}\n' + old,
         'D18;D23', label,
         'Pass08 auxiliary reference target lay at the previous page bottom while the statement tag and printed heading began on the next page. Reserve six baselines before this exact statement opening. The counter, labels, tag and mathematical text are unchanged; final PDF target coordinates still require verification.')

paragraphs = [
    ('0003', 'a-page-carrying-the-actual-source-line', 'The page and its compact model.'),
    ('034V', 'the-full-graph-to-page-comparison-by-regular-bands', 'The cusp product and based marking.'),
    ('01GY', 'characteristic-calculation-and-the-scope-of-the-result', 'The integral square and return.'),
    ('034Z', 'the-page-including-the-finite-cap-line', 'The finite cap and page line.'),
    ('034Q', 'the-actual-graph-line-and-return', 'Transport of the graph and the return.'),
]
for tag, label, heading in paragraphs:
    target = '\\hypertarget{tag-' + tag + '}{}\\label{' + label + '}'
    paragraph = '\\paragraph{' + heading + '}'
    old = target + '\n' + paragraph
    new = paragraph + '\\leavevmode\n' + target
    edit('paragraph-' + tag, old, new, 'D18;D23', label,
         'The source put this proof-paragraph label before its own heading, so it inherited the preceding target/title. Execute the run-in heading before the unchanged target and label. No theorem number is assigned to this paragraph and no mathematical text changes; final named-destination validation remains required.')

edit('local-cover-title',
     '\\section{Local covers, global quotients and cusp carriers}',
     '\\section{Local covers of the cusp}',
     'D14;D24', 'sec:III:carriers',
     'After the admitted regrouping this section contains completed Kummer covers; global quotients and carriers have their own following sections. The title now states the actual bounded contents. All units and their order remain unchanged.')

identity = lambda x: Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', x))
assert identity(s) == identity(original)
inverse = s
for e in reversed(edits):
    assert inverse.count(e['new_text']) == 1
    inverse = inverse.replace(e['new_text'], e['old_text'], 1)
assert inverse == original
with (ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv').open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t'); rows = list(reader); fields = reader.fieldnames
assert not {e['change_id'] for e in edits} & {x['change_id'] for x in rows}
SOURCE.write_text(s, newline='\n')
with (ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv').open('w', newline='') as f:
    w = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows + edits)
print('Applied', len(edits), 'exact typography, heading-space and paragraph-target changes.')
print('The inverse substitutions recover the whole pre-edit source; every literal label/target is preserved.')
print('No proof content changes and no mathematical check-event credit. Final layout/target review is open.')
