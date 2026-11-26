"""Admit the complete normal-crossing alignment and rational-boundary receivers."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder = ROOT / 'agents/continuation3_foundations/sec11'
prefix = 'S6_SERIES_PUBLISH_sec11_nc_alignment_'
before = SOURCE.read_text()
after = before
guards = json.loads((folder / (prefix + 'guards.json')).read_text())
assert len(guards) == 2
for row in guards:
    assert after.count(row['old']) == 1, row['key']
    after = after.replace(row['old'], row['new'], 1)
for old, new in zip(identifiers(before), identifiers(after)):
    assert old == new
SOURCE.write_text(after, newline='\n')

for suffix, target, key in [
    ('defects.tsv', 'S6_SERIES_PUBLISH_defects_II.tsv', 'change_id'),
    ('CHECK_EVENTS.tsv', 'CHECK_EVENTS.tsv', 'event_id')
]:
    _, rows = read_tsv(folder / (prefix + suffix))
    if suffix == 'CHECK_EVENTS.tsv':
        assert all(row['type'] == 'used and rechecked in this run' and 'effort' in row['who'] for row in rows)
    print(suffix, append_rows(ROOT / target, rows, key))

fields, progress = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
_, statuses = read_tsv(folder / (prefix + 'unit_progress.tsv'))
units = {r['unit'] for r in statuses}
assert units == {'subsec:II:elliptic-alignment','subsec:II:torsion-normal-rational-obstruction'}
assert len(statuses) == 52
progress = [r for r in progress if not (r['paper'] == 'II' and r['unit_id'] in units)]
titles = {label:title for title,label in re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}',after,re.M)}
for row in statuses:
    kind = 'structure' if row['row'] == 'restructuring' else row['row']
    progress.append(dict(zip(fields,['II',row['unit'],titles[row['unit']],
        'structure' if kind == 'structure' else 'defect','' if kind == 'structure' else kind,
        'open' if kind in {'D14','D23','D24','structure'} else row['status'],now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-NC-ALIGNMENT-ADMISSION',
        row['basis'] + ' Foundations read complete old/current and new proofs and prerequisite owners. Root read all complete receiving statements and proofs, the full comparison and all-class assessments, then reread the updated P344/P306 root-chart paragraph and final Hopf references. These are two existing actual subsections; original sec11 remainder and global placement/final pages remain open. No independent-check or subdivision credit.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
add_event('lem:II:vertical-elliptic-alignment;cdp:st:C.2.UN.67',
          'II-C3-ROOT-NC-ALIGNMENT-ADMISSION','used and rechecked in this run',
          'Complete P260/UN67 receivers admitted after full foundations old/new and root receiving-proof reads. P260 extends the original SNC domain to full reduced NC with smooth normalization nu:T→S_i and both labelled self-double branches in D. The degree-one component resolution has rho|E=nu r; meromorphic derivations and their polar divisors are transported through this exact map. The rank-one UN29 application occurs on its embedded E, and (r_b)_* identifies the integral monodromy with the same q on T. UN67 retains every restriction sequence, exact-order pencil argument, connected Stein map, canonical/root calculation and coherent Euler contradiction, and proves the labelled NC normal-line comparison. The final root chart cites the admitted P344 at m=a and P306 for its canonical/invariant consequences. Original SNC conclusions and all identifiers are preserved. No new source opening, independent check, required-check increment, original sec11 closure or final-page credit.',
          'Complete existing elliptic-alignment and torsion-normal-rational-obstruction subsections',source=__file__)
print('Two complete NC receiving units admitted; original sec11 remainder stays open.')
