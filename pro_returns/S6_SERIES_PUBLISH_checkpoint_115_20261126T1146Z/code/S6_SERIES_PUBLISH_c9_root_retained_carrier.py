"""Stage the one live carrier role repair after reading all three scopes."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import difflib
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_root_image_repairs'
TMP = ROOT.parents[1] / 'tmp/c9_root_retained_carrier'
TMP.mkdir(parents=True, exist_ok=True)
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
marker = source.index(r'\hypertarget{tag-036J}')
start = source.rfind(r'\begin{theorem}', 0, marker)
stop = source.index(r'\end{proof}', marker) + len(r'\end{proof}')
scope = source[start:stop]
begin = scope.index('In either construction write $b$ for the product midpoint, $W$')
end_text = 'target ball and both asserted isometries.'
end = scope.index(end_text, begin) + len(end_text)
old = scope[begin:end]
assert old.count('W') == 5
new = old.replace('W', r'W_{\rm col}')
candidate = scope[:begin] + new + scope[end:]
assert scope.count(old) == candidate.count(new) == 1
assert candidate.replace(new, old, 1) == scope
assert source.count(old) == 1
whole = source.replace(old, new, 1)
assert whole.count(new) == 1 and whole.replace(new, old, 1) == source
for pattern in [r'\d+', r'\\(?:label|hypertarget)\{[^{}]+\}', r'\\(?:[Cc]ref|[Ee]qref|ref|cite)(?:\[[^]]*\])?\{[^{}]+\}', r'\\mathbb\s*(?:\{[^{}]+\}|[A-Za-z])']:
    assert re.findall(pattern, scope) == re.findall(pattern, candidate)

now = datetime.now(timezone.utc).isoformat()
reason = ('CLAUDE-III-P15. W in the statement is the established cusp fibre; the final metric argument assigned W to the collapsed subset. W_col is exactly W_12,T for the two-torus product and W_24,T for the four-circle product, respectively. Identity on each of these actual subsets and its inverse preserve both distances to the subset, the same quotient equivalence relation and every forward/inverse ball map. All five occurrences follow this definition. The cusp fibre W and its basepoint retain their original names.')
row = dict(change_id='III-C9-ROOT-036J-RETAINED-COLLAPSED-SUBSET', type='D20', statement_id='wb:cusp-cone-angle-forgotten-sphere-carriers', old_location='036J proof; complete final ball-comparison block', old_page='candidate02; actual root image reading 523–696', new_location='036J proof; complete final ball-comparison block', new_page='pending final changed-page review', old_text=old, new_text=new, reason=reason, review_status='Root read the complete current 036J theorem/proof, including all five W roles, against the prior complete original/proposed comparison. Exact difference and full-source reversal checked. Source admission and changed-page rendering remain.')
event = dict(statement_id=row['statement_id'], date='2026-11-26', who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; root', type='used and rechecked in this run', outcome='Read the complete current 036J statement/proof and all five occurrences of the final collapsed-subset name. Compared the one exact change with the cusp-fibre binding, both actual collapsed subsets, the quotient distance and explicit ball-map inverse. Full-source reversal, numeric literals, references and permanent targets verified. Exposed use/rechecking only; no independent-proof or new-image credit.', event_id='publish:c9:III:036J:retained-role-readback', phase='publication continuation 9', source_file='agents/continuation9_root_image_repairs/S6_SERIES_PUBLISH_c9_root_retained_carrier_review.md', source_row='036J complete current theorem/proof; final ball-comparison block', source_event_type='used and rechecked in this run', evidence_group='publish:c9:III:036J:retained-role-readback', publish_input_file='S6_SERIES_PUBLISH_III.tex', publish_input_row='036J', date_utc=now, where='Complete current source reread and exact bounded comparison; actual candidate02 images remain the prior root evidence.')
for canonical, name, rows in [('S6_SERIES_PUBLISH_defects_III.tsv', 'S6_SERIES_PUBLISH_c9_root_retained_carrier_defects.tsv', [row]), ('CHECK_EVENTS.tsv', 'S6_SERIES_PUBLISH_c9_root_retained_carrier_CHECK_EVENTS.tsv', [event])]:
    with (ROOT / canonical).open(newline='') as f:
        fields = next(csv.reader(f, delimiter='\t'))
    with (OUT / name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
(TMP / '036J_original.tex').write_text(scope, newline='\n')
(TMP / '036J_proposed.tex').write_text(candidate, newline='\n')
diff = ''.join(difflib.unified_diff(scope.splitlines(True), candidate.splitlines(True), fromfile='036J-current', tofile='036J-proposed'))
(OUT / 'S6_SERIES_PUBLISH_c9_root_retained_carrier.diff').write_text(diff, newline='\n')
print('036J:', len(scope.splitlines()), 'current source lines; five role occurrences; one exact fragment and one scoped used event.')
print('Complete-scope and full-source inverse, numerical literals, references, blackboard tokens and permanent identifiers verified.')
print(diff)
