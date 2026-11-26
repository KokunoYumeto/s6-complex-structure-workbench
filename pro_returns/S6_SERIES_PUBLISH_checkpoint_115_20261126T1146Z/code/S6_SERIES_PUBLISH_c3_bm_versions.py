"""Qualify opened preprint locators and correct the admission's owner identifiers."""
from S6_SERIES_PUBLISH_c3_edit import *

old = r'\cite[\S0.2(2), pp.~3--4; Theorem~1.6 and Remarks~1.7, pp.~5--6; Theorem~1.10, p.~7]{BierstoneMilman1997}'
new = r'\cite[arXiv v2, \S0.2(2), pp.~3--4; Theorem~1.6 and Remarks~1.7, pp.~5--6; Theorem~1.10, p.~7]{BierstoneMilman1997}'
apply_edit(old, new, 'II-C3-BM-ROOT-VERSION-RECORD', ['D18'],
           'prop:II:cyclic-root-normalization', 'P342 source record',
           'The opened source is arXiv v2; the bibliography also contains journal pagination. Identify the edition for these page locators.')
old = r'''\cite[\S0.2(2), pp.~3--4;
Theorem~1.6 and Remarks~1.7, pp.~5--6; Theorem~1.10, p.~7]{BierstoneMilman1997}'''
new = r'''\cite[arXiv v2, \S0.2(2), pp.~3--4;
Theorem~1.6 and Remarks~1.7, pp.~5--6; Theorem~1.10, p.~7]{BierstoneMilman1997}'''
apply_edit(old, new, 'II-C3-BM-ROOT-VERSION-PROOF', ['D18'],
           'prop:II:cyclic-root-normalization', 'P342 proof, embedded resolution',
           'The exact source-read record identifies the cited pages as arXiv v2.')
old = r'''\cite[\S0.2(2), preprint p.~3; Theorem~1.6 and Remarks~1.7,
preprint pp.~5--6]{BierstoneMilman1997}'''
new = r'''\cite[arXiv v2, \S0.2(2), p.~3; Theorem~1.6 and Remarks~1.7,
pp.~5--6]{BierstoneMilman1997}'''
apply_edit(old, new, 'II-C3-BM-PERIOD-VERSION', ['D18'],
           'cdp:st:D.2.6', 'Period extension proof, embedded resolution',
           'Qualify the preprint edition with the same opened arXiv-v2 setup and theorem. No map or hypothesis changes.')
add_event('prop:II:cyclic-root-normalization;cdp:st:D.2.6',
          'II-C3-BM-VERSION-QUALIFIERS', 'used and rechecked in this run',
          'Root compared the full cited source records and exact receiving citation contexts. P342 and D2.6 now identify arXiv v2 for their preprint page numbers. The complete P342 receiver was read before its admission; the present bounded locator edit claims no additional full proof reading, source opening or independent check.',
          'P342 source/proof and D2.6 resolution citation', source=__file__)

fields, events = read_tsv(ROOT / 'CHECK_EVENTS.tsv')
rows = [r for r in events if r['event_id'] == 'II-C3-ROOT-ELLIPTIC-LIFT-ADMISSION']
assert len(rows) == 1
correct = ('def:II:elliptic-root-curve;lem:II:equivariant-elliptic-torsor-lift;'
           'cdp:st:C.2.UN.34;cdp:st:C.2.UN.35;cdp:st:C.2.UN.37;cdp:st:C.2.UN.31;'
           'lem:II:identity-monodromy-elliptic;lem:II:local-cyclic-elliptic;'
           'lem:II:hopf-curve-restriction;sec:II:09')
for label in correct.split(';'):
    assert r'\label{' + label + '}' in SOURCE.read_text(), label
old_identifiers = rows[0]['statement_id']
rows[0]['statement_id'] = correct
write_tsv(ROOT / 'CHECK_EVENTS.tsv', fields, events)
helper = ROOT / 'code/S6_SERIES_PUBLISH_c3_elliptic_lift_admit.py'
text = helper.read_text()
assert old_identifiers in text
helper.write_text(text.replace(old_identifiers, correct, 1), newline='\n')
print('Three edition qualifiers and exact root-admission owner identifiers corrected; no derived refresh.')
