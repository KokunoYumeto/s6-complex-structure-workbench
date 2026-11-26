"""Prepare one exact selected-generator branch qualification; no master writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import difflib
import re

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / 'agents/continuation9_root'
STEM = 'S6_SERIES_PUBLISH_c9_02OG_generator_branch'
OWNER = 'mapsD:repair:collision-realization'
REVIEW = 'agents/continuation9_root/' + STEM + '_review.md'
source = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
old = r'''$[q]$.  Its logarithm cocycle is $q+d(h)$ for an integral $h$;
changing the branch by $-h$ gives exactly $q$, with inverse branch
change $+h$.  The quotient maps prove that $G$ generates the
Mordell--Weil group and that this group has no torsion.'''
new = r'''$[q]$.  Its logarithm cocycle is $q+d(h_G)$ for an integral $h_G$;
changing the branch by $-h_G$ gives exactly $q$, with inverse branch
change $+h_G$.  The quotient maps prove that $G$ generates the
Mordell--Weil group and that this group has no torsion.'''
assert source.count(old) == 1 and source.count(new) == 0
assert new.count('h_G') == 4
start = source.index(r'\hypertarget{tag-02OG}')
stop = source.index(r'\end{proof}', start) + len(r'\end{proof}')
assert 'h_G' not in source[start:stop]
candidate = source.replace(old, new, 1)
assert candidate.replace(new, old, 1) == source
identities = lambda body: re.findall(r'\\(?:label|hypertarget)\{[^{}]*\}', body)
assert identities(source) == identities(candidate)
assert re.findall(r'\d+', source) == re.findall(r'\d+', candidate)
now = datetime.now(timezone.utc).isoformat()

def header(name):
    with (ROOT / name).open(newline='') as stream:
        return next(csv.reader(stream, delimiter='\t'))

def write(name, fields, row):
    with (DIRECTORY / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerow(row)

fields = header('S6_SERIES_PUBLISH_defects_III.tsv')
row = dict.fromkeys(fields, '')
row.update(change_id='C9-III-02OG-GENERATOR-BRANCH-001', type='D20',
    statement_id=OWNER, old_location='02OG, selected section generator and its height',
    new_location='02OG, selected section generator and its height',
    old_text=old, new_text=new,
    reason='Qualify the selected generator branch h_G separately from the earlier raw profile-indexed cocycle coordinates. The row50 assembly output includes the exact shift h-k(1,-1); the row56 output has its displayed direct formula. All four selected uses and the negative/positive branch inverse remain the same vector and maps.',
    review_status='Root read the full adjoining cocycle/section/pairing passage and exact map comparison. Prepared; guarded admission and final changed-page review remain.')
write(STEM + '_defects.tsv', fields, row)
fields = header('CHECK_EVENTS.tsv')
event = dict.fromkeys(fields, '')
event_id = 'publish:c9:III:02OG:generator_branch'
event.update(statement_id=OWNER, date='2026-11-26',
    who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode',
    type='used and rechecked in this run',
    outcome='Read the complete current cocycle assembly, junction and section interpretation, generator paragraph and following pairing/decomposition. Compared the profile50 shifted assembly output and profile56 direct output with the selected generator branch. One exact fragment qualifies all four h_G uses and preserves d, both branch changes and their composites, the height formulas and inverse group maps. Complete-source reversal and ordered identifier/numeral comparisons passed. Exposed bounded review; no independent proof, new numerical computation or image credit.',
    event_id=event_id, phase='publication continuation 9', source_file=REVIEW,
    source_row='Complete adjoining cocycle and selected-generator comparison, current source8205–8475',
    source_event_type='used and rechecked in this run', evidence_group=event_id,
    publish_input_file='agents/continuation9_root/' + STEM + '_defects.tsv',
    publish_input_row='one exact fragment', date_utc=now,
    where='Paper III, tag02OG, selected generator branch and its precise cocycle-chart identification')
write(STEM + '_CHECK_EVENTS.tsv', fields, event)
(DIRECTORY / (STEM + '.diff')).write_text(''.join(difflib.unified_diff(
    old.splitlines(keepends=True), new.splitlines(keepends=True),
    fromfile='02OG selected branch before', tofile='02OG selected branch proposed')) + '\n')
print('One exact fragment; four selected h_G uses.')
print('Unique guard, complete source reversal, ordered labels/targets and numeric literals passed.')
print('Both event type fields are used and rechecked in this run; canonical source and tables unchanged.')
