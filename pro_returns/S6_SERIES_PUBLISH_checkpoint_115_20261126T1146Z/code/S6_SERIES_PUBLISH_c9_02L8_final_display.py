"""Reflow the actual 2.95844pt fibre-quotient display; preserve its exact tokens.

Root read the complete adjoining argument and both completed build outputs.
The only change is a gathered line break before the wedge-order annotation.
The explicit inverse below recovers the whole original fragment byte for byte.
This is a layout repair, with no additional mathematical check event.
"""
from pathlib import Path
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'S6_SERIES_PUBLISH_III.tex'
defects = ROOT / 'S6_SERIES_PUBLISH_defects_III.tsv'
before = source.read_text()
prior_defects = defects.read_text()
old = r'''\[
 f_{\mathrm{coinv}}(x)=
 \begin{pmatrix}
 1&0&0&0&0&0\\
 0&0&\rho_{{\rm cov},1}&0&\rho_{{\rm cov},2}&\rho_{{\rm cov},3}
 \end{pmatrix}
 \bigwedge\nolimits^2R^{-1}x
 \quad\text{in wedge order }(12,13,14,23,24,34).
\]'''
new = old.replace('\\[\n', '\\[\n\\begin{gathered}\n', 1).replace(
    r' \quad\text{in wedge order }',
    ' \\\\[2pt]\n' + r' \text{in wedge order }', 1).replace(
    '\n\\]', '\n\\end{gathered}\n\\]', 1)
reverse = new.replace('\\[\n\\begin{gathered}\n', '\\[\n', 1).replace(
    ' \\\\[2pt]\n' + r' \text{in wedge order }',
    r' \quad\text{in wedge order }', 1).replace(
    '\n\\end{gathered}\n\\]', '\n\\]', 1)
assert reverse == old
assert before.count(old) == 1
after = before.replace(old, new, 1)
assert after.replace(new, old, 1) == before
for expression in (r'\\label\{[^{}]+\}', r'\\hypertarget\{[^{}]+\}',
                   r'\\(?:begin|end)\{proof\}', r'\d+'):
    # The explicit layout spacing adds only the literal 2 in [2pt].
    compared = after.replace(new, new.replace(r'\\[2pt]', r'\\', 1), 1) if expression == r'\d+' else after
    assert re.findall(expression, before) == re.findall(expression, compared)
csv.field_size_limit(100000000)
reader = csv.DictReader(io.StringIO(prior_defects), delimiter='\t')
fields = reader.fieldnames
rows = list(reader)
key = 'III-C9-02L8-FINAL-DISPLAY-01'
assert not any(row['change_id'] == key for row in rows)
row = dict.fromkeys(fields, '')
row.update(change_id=key, type='D23', statement_id='maps:src:D.2.32',
    old_location='02L8 proof, fibre Wang quotient display; final pre-reflow source lines 27635-27643',
    old_page='current candidate03 / legacy candidate02; 2.95844pt diagnostic',
    new_location='Same fibre Wang quotient display, two gathered lines',
    new_page='Pending final build and actual image reading', old_text=old, new_text=new,
    reason='Both completed kernels report 2.95844pt overflow. A line break places the complete wedge-order annotation below the matrix formula. Reversing only the inserted gathered environment and line-break spacing recovers the entire old fragment exactly. Matrix entries, exponent, map, ordered wedge coordinates, right inverse in the following text, and all targets are preserved. No new mathematical event or count is added.',
    review_status='Exact source comparison done by root; final two-kernel build and actual changed-page reading remain open')
stream = io.StringIO(newline='')
writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
writer.writerow(row)
assert source.read_text() == before and defects.read_text() == prior_defects
source.write_text(after)
with defects.open('a', newline='') as f:
    f.write(stream.getvalue())
print('Applied one exact 02L8 D23 display reflow; complete old/new fragment retained.')
print('Full inverse recovers original source; all labels, targets, proof boundaries and mathematical numerical literals preserved.')
print('No CHECK_EVENT, count, source finding or unit status changed. Final build and image gate remain open.')
