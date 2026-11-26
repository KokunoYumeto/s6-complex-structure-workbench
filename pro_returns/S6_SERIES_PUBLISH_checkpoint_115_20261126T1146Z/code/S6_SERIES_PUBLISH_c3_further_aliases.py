"""Reconcile further-result entries with their single current statement owners."""
from S6_SERIES_PUBLISH_c3_edit import *

source = SOURCE.read_text()
left = source.index(r'\paragraph{Further results.}')
right = source.index(r'\clearpage', left)
listed = source[left:right]
pairs = [
    ('night:P4.18', 'cdp:st:A.5.15'),
    ('cdp:st:C.2.CR.4', 'night:P4.28'),
    ('inv:wb:uniform-nontorsion-provenance', 'wb:thm:uniform-nontorsion-audit'),
    ('cdp:st:C.2.UN.24', 'cdp:st:C.2.UN.32'),
    ('cdp:st:C.2.UN.25', 'cdp:st:C.2.UN.27'),
    ('cdp:st:C.2.UN.46', 'cdp:st:C.2.UN.57'),
    ('cdp:st:C.2.UN.51', 'cdp:st:C.2.UN.57'),
    ('cdp:st:C.2.UN.55', 'cdp:st:C.2.UN.57'),
]
for index, (alias, owner) in enumerate(pairs, 1):
    # Verify the exact label map in the current body before deleting a
    # second navigation entry. All mathematical statements and targets stay.
    alias_pos = source.index(r'\label{' + alias + '}', right)
    owner_pos = source.index(r'\label{' + owner + '}', right)
    assert source.rfind(r'\begin{', right, alias_pos) == source.rfind(r'\begin{', right, owner_pos), (alias, owner)
    lines = [line + '\n' for line in listed.splitlines() if line.startswith(r'\item \SeriesRef{' + alias + '}')]
    assert len(lines) == 1, alias
    apply_edit(lines[0], '', f'II-C3-FURTHER-ALIAS-{index:02}', ['D12','D24'],
               alias + ';' + owner, 'Further results',
               'Both labels belong to the same current numbered statement. Keep its one navigation entry under the owning label; the full body statement, proof and every old target remain unchanged.',
               'Root read the former list and the current owning statements; exact co-location of both labels is checked before the edit. The complete old/new proofs were already compared at their original consolidation admissions.')

old = r'\item \SeriesRef{cdp:st:C.2.UN.27}\quad A fixed punctured torus family has infinitely many zero-Euler fillings with essential projective elliptic components of coherent Euler characteristic one.'
new = r'\item \SeriesRef{cdp:st:C.2.UN.27}\quad Essential Enriques and projective elliptic components in zero-Euler fillings of one punctured torus family.'
apply_edit(old, new, 'II-C3-FURTHER-ENRIQUES', ['D24'], 'cdp:st:C.2.UN.27;cdp:st:C.2.UN.25',
           'Further results', 'The single entry names both the r=2 Enriques member and the r>=3 projective elliptic members of the same fully stated construction.',
           'Root read the complete current combined statement and its explicit r=2 identification; only its navigation description changes.')
old = r'\item \SeriesRef{cdp:st:C.2.UN.57}\quad The exact marked-cycle criterion without an algebraic-dimension restriction.'
new = r'\item \SeriesRef{cdp:st:C.2.UN.57}\quad The exact marked Hopf and ruled cycle criterion and its compact realizations.'
apply_edit(old, new, 'II-C3-FURTHER-CYCLES', ['D24'], 'cdp:st:C.2.UN.57;cdp:st:C.2.UN.46;cdp:st:C.2.UN.51;cdp:st:C.2.UN.55',
           'Further results', 'The one entry names the full Hopf/ruled cycle criterion and compact conclusion of the single combined statement.',
           'Root read the complete combined current statement, including the full elliptic translation and two-Hopf special case; only its navigation description changes.')
old = 'B & New integral refinement and fibre classification; the rational component\nformula is \\cite[\\S10.5, p.~91]{AC26}.\\\\'
new = 'B & New integral refinement; rational component formula:\n\\cite[\\S10.5, p.~91]{AC26}; fibre classification: \\cref{cdp:st:C.3.1,cdp:st:C.3.11}.\\\\'
apply_edit(old, new, 'II-C3-FIRSTPART-B-SCOPE', ['D15'], 'series:II:B',
           'Known and new, row B', 'Attach the novelty wording to the integral refinement explicitly checked in the literature comparison, and give the exact current owners for the fibre classification.',
           'Root read the full literature comparisons II-C3-LIT-B1 and B2 and the current main statement. No mathematical statement or source attribution changes.')
add_event('cdp:st:A.5.15;night:P4.28;wb:thm:uniform-nontorsion-audit;cdp:st:C.2.UN.32;cdp:st:C.2.UN.27;cdp:st:C.2.UN.57;series:II:B',
          'II-C3-FURTHER-OWNER-RECONCILIATION', 'used and rechecked in this run',
          'Root compared the further-results entries with the current numbered statement owners and verified the exact co-located label map for all eight repeated entries. Their body statements, complete proofs and old targets are unchanged. The single Enriques/elliptic entry retains both r=2 and r>=3 outcomes, and the cycle entry names the shared Hopf/ruled criterion and compact realizations. Row B novelty wording is confined to the integral refinement checked in the admitted primary-source comparison. Remaining first-part and whole-paper reconciliation stays open; no new proof or independent credit.',
          'Further results; Known and new, row B', source=__file__)
print('Eight duplicate owner entries removed; two combined descriptions and the bounded B source-status scope reconciled.')
