"""Stage two literal punctuation repairs in the fully read main-theorem unit."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
EXPECTED = '5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187'
OUT = ROOT / 'agents/continuation9_candidate10_front_punctuation'
STEM = 'S6_SERIES_PUBLISH_c9_candidate10_front_punctuation'
FIELDS = 'change_id type statement_id old_location old_page new_location new_page old_text new_text reason review_status'.split()
source_bytes = SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == EXPECTED
source = source_bytes.decode()
csv.field_size_limit(100000000)
with (ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').open(newline='') as stream:
    unit, = [r for r in csv.DictReader(stream, delimiter='\t')
             if (r['paper'], r['unit_id'], r['row_kind'], r['defect_type'])
             == ('III', 'series:III:main-theorems', 'defect', 'D23')]
assert unit['status'] == 'done'
old_b = r""" \qquad M[x:y]=[x:y-x].
 \end{gathered}
\]
where $P_{3,4}(z_1,z_2)=(z_1^3,z_2^4)/\|(z_1^3,z_2^4)\|$
has degree twelve."""
new_b = old_b.replace(r'M[x:y]=[x:y-x].', r'M[x:y]=[x:y-x],', 1)
old_f = r"""$\ell=n(e_\gamma-e_u)+d\delta$, $n,d\in\mathbb Z$, freeness
is equivalent to"""
new_f = r"""$\ell=n(e_\gamma-e_u)+d\delta$, $n,d\in\mathbb Z$. Freeness
is equivalent to"""
specs = [
    ('001', 'series:III:B', old_b, new_b,
     'The displayed coordinate assignment belongs to the same sentence as its following where clause. Replace its terminal full stop by a comma, keeping the coordinate map, homotopy, inverse-reference sentence and all mathematical data exactly.'),
    ('002', 'series:III:F', old_f, new_f,
     'End the let sentence after its integer parameter domain, then begin the freeness sentence. This removes the comma splice while retaining the complete affine-cap parameters, exact freeness equivalence and both n cases.')
]
stamp = datetime.now(timezone.utc).isoformat()
proposal = source
rows = []
for suffix, owner, old, new, reason in specs:
    assert proposal.count(old) == 1 and new not in proposal
    assert re.findall(r'\d+', old) == re.findall(r'\d+', new)
    assert re.findall(r'\\(?:label|hypertarget|[Cc]ref|ref|eqref)\s*\{[^{}]*\}', old) == re.findall(r'\\(?:label|hypertarget|[Cc]ref|ref|eqref)\s*\{[^{}]*\}', new)
    if suffix == '001':
        assert old.replace('.', ',') == new.replace('.', ',')
    else:
        assert old.replace(', freeness', '. Freeness') == new
    pos = source.index(old)
    location = 'S6_SERIES_PUBLISH_III.tex:' + str(source.count('\n', 0, pos) + 1)
    rows.append(dict(change_id='C9-III-CANDIDATE10-FRONT-PUNCT-' + suffix,
                     type='D23', statement_id=owner, unit_id='series:III:main-theorems',
                     old_location=location, old_page='', new_location=owner, new_page='',
                     old_text=old, new_text=new, reason=reason,
                     review_status='Root read the complete current main-theorem/outline/front-matter source215–954 and both exact old/new fragments. Punctuation-only comparison completed at ' + stamp + '; source admission and successor image inspection remain pending. No check event.'))
    proposal = proposal.replace(old, new, 1)
reverse = proposal
for row in reversed(rows):
    assert reverse.count(row['new_text']) == 1
    reverse = reverse.replace(row['new_text'], row['old_text'], 1)
assert reverse == source
assert re.findall(r'\\(?:label|hypertarget)\s*\{[^{}]*\}', source) == re.findall(r'\\(?:label|hypertarget)\s*\{[^{}]*\}', proposal)
OUT.mkdir(exist_ok=True)
payload = dict(source_sha256=EXPECTED, proposals=rows)
(OUT / (STEM + '.json')).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', newline='\n')
with (OUT / (STEM + '_defects.tsv')).open('w', newline='') as stream:
    writer = csv.DictWriter(stream, FIELDS, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows({key: row[key] for key in FIELDS} for row in rows)
(OUT / (STEM + '.diff')).write_text(''.join(difflib.unified_diff(source.splitlines(True), proposal.splitlines(True), fromfile='frozen current10 source', tofile='punctuation proposal')), newline='\n')
review = r"""# Current10 main-theorem punctuation: root comparison

Reader: GPT-6 Astra (OpenAI), ChatGPT Pro mode; root.

Root read the entire current front matter from the section opening at source215 through its end at954, in two complete untruncated outputs215–598 and599–954. This includes every main theorem A–G, every Further results item, all seven outlines, the comparison table, methodology and organization diagram.

Two literal punctuation defects occur in series:III:main-theorems. Theorem B places a full stop after M[x:y]=[x:y-x] and then continues the sentence with lowercase “where”; the proposal supplies a comma. Theorem F(d) joins its let sentence to “freeness is equivalent” with a comma; the proposal supplies a full stop and initial capital. The complete surrounding statements and their exact before/after fragments have been read. Every mathematical expression, parameter, coefficient, reference, label, target and formal boundary is retained. The two literal inverse punctuation substitutions recover the entire frozen source.

These are two D23 source rows and no mathematical check event. The source is unchanged by this staging program. Its existing D23 containing-unit row is currently done; the guarded source admission must reopen that row when the punctuation changes. Final images must show the complete front-matter unit and both corrected joins. The current source hash is 5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187; no successor image or final criterion closure is asserted here.
"""
(OUT / (STEM + '_review.md')).write_text(review, newline='\n')
assert SOURCE.read_bytes() == source_bytes
print('Prepared two exact punctuation guards and two D23 rows; no event.')
for row in rows:
    print(row['change_id'], row['statement_id'], row['old_location'])
    print('OLD:\n' + row['old_text'])
    print('NEW:\n' + row['new_text'])
print('Full inverse recovers the frozen source; labels and all mathematical expressions are unchanged.')
print('D23 series:III:main-theorems remains done until the actual source-change invalidation.')
