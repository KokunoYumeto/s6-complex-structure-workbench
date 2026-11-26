"""Scheduled review: cite genuine row closures, not subdivision or packaging."""
from S6_SERIES_PUBLISH_c3_edit import *
from datetime import datetime, timezone

due=datetime.fromisoformat('2026-11-22T18:56:58+00:00')
assert datetime.now(timezone.utc)>=due,'Hourly review is not yet due.'
assert '## Progress review 25 —' not in (ROOT/'PROGRESS_LEDGER.md').read_text()
_,rows=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
witnesses=[r for r in rows if r['paper']=='II' and r['unit_id']=='night:P4.25'
    and r['row_kind']=='defect' and r['defect_type'] not in ['D10','D14','D16','D23']]
assert len(witnesses)==21
assert all(r['status']=='done' and r['date_utc']>'2026-11-22T17:57:21+00:00' for r in witnesses)
stamp=now()
addition=f'''

## Progress review 25 — {stamp}

Scheduled for 2026-11-22T18:56:58+00:00. Movement is present. As a
conservative stable-unit witness, night:P4.25 has closed its 21 previously
open local defect rows after the complete original/receiving proof and
unit reading. The exact rows and event II-C3-ROOT-REDUCED-CONDUCTOR-UNIT
are in the unit ledger and CHECK_EVENTS; their current evidence fields
identify the recorded reading. Inherited D10/D16, global placement D14,
rendered typography D23 and structure are excluded. Other completed
receiving readings, restored reopened rows and scope consolidations are
recorded individually; unit subdivision, alias migration, packaging and
reclosure of an already-counted row supply no additional witness here.

Paper II now has one complete general Hopf-normalization proof with all
five legacy identities, one proper irrational-ruled Euler proof with both
legacy identities, and earlier common conductor, curve, ruled-boundary,
minimal-resolution and pushout owners. Root has reread the full receiving
Hopf, ruled, differential, binary-product and persistent-normalization
arguments. The class-VII, bounded contracted-section duality, and later
push-stability/comb/Picard text has been admitted with the exact exposed
agent comparisons. E.5.2 and E.5.3 statements remain unchanged.

A new proof-premise check is open: P4R.14, P4R.15, P4.41 and P4.45 must
justify their boundary transport for the actual full fibre when analytic
branches have unequal multiplicities. A common-power equality is already
available in the irreducible cusp applications. For unequal multiplicities,
an explicit cyclic parametrization of a two-factor nonzero level has been
derived; its factor-preserving deformation and compact-cycle boundary
comparison remain under investigation. No counterexample, refined theorem
or completed proof is asserted. This open check blocks final mathematical
validation and is not hidden by the 198 inherited required-check entries,
whose recorded resolved status remains unchanged. D10 and D16 stay done.

The last completed working pdfLaTeX build, before the newest integrations,
has 793 pages, zero undefined references/citations or missing fonts/glyphs,
and no overflow above 2 pt. Its one overfull box is 1.7175 pt. It is not the
final candidate. Final rendered-page credit remains zero. The complete
component-cover/translation-field package is ready for bounded admission;
later analytic/Picard and contracted-boundary work is continuing. The
refined 02Y6/02XE consumer pass, whole-paper ordering, final provenance,
standalone build and every-page reading remain open.

Papers III and IV remain unstarted. Papers I and V retain their closed
gates and their manuscripts have not been reopened. Consecutive hourly
reviews without movement: 0. Next review: 2026-11-22T19:56:58+00:00 (26).
The next checkpoint is due 2026-11-22T19:11:58+00:00 (38). This review
adds no independent-proof or final-page credit.
'''
# The exact witness event name is read from the actual progress evidence.
evidence=sorted({r['evidence'] for r in witnesses})
addition=addition.replace('event II-C3-ROOT-REDUCED-CONDUCTOR-UNIT', 'reading evidence '+', '.join(evidence))
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (ROOT/name).open('a',newline='\n') as f:f.write(addition)
add_event('night:P4R.14; night:P4R.15; night:P4.41; night:P4.45',
    'II-C3-LOCAL-FULL-FIBRE-MULTIPLICITY-OPEN','used and rechecked in this run',
    'Foundations full consumer reading identified an unclosed premise in the written reduced-function boundary comparison: the broad setting permits unequal full-fibre branch multiplicities, while the common-power map is proved for irreducible support. Exact two-factor cyclic parametrization is derived; factor-preserving deformation and compact-cycle transport for the actual full fibre remain under investigation. No refutation or conditional replacement asserted. The affected final mathematical gate remains open.',
    'S6_SERIES_PUBLISH_II.tex: local A3, nonzero-Hessian and D4 transport consumers',source='code/S6_SERIES_PUBLISH_c3_review25.py')
print(f'Review25 {stamp}: 21 conservative stable-unit closure witnesses; movement present; no-stall counter 0. Full-fibre multiplicity premise explicitly open.')
