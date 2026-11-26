"""The scheduled hourly review uses actual stable-unit closures as witnesses."""
from S6_SERIES_PUBLISH_c3_edit import *
from datetime import datetime, timezone

due=datetime.fromisoformat('2026-11-22T17:56:58+00:00')
assert datetime.now(timezone.utc)>=due, 'Hourly review is not yet due.'
ledger=ROOT/'PROGRESS_LEDGER.md'
assert '## Progress review 24 —' not in ledger.read_text()
_,rows=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
witness_units=['night:P4.6','night:P4.12','night:P4.8','night:P4.14',
    'night:P4R.1','night:P4R.6','night:P4.33','night:P4R.2',
    'night:P4.16','night:P4.19','night:P4.28','night:P4R.3',
    'night:P4R.4','night:P4R.5','night:P4.21']
witnesses=[r for r in rows if r['paper']=='II' and r['unit_id'] in witness_units
    and r['defect_type'] not in ['D10','D14','D16','D23']
    and r['row_kind']=='defect']
assert len(witnesses)==15*21
assert all(r['status']=='done' and r['date_utc']>'2026-11-22T16:56:58+00:00'
    for r in witnesses)
stamp=now()
addition=f'''\n\n## Progress review 24 — {stamp}

Scheduled for 2026-11-22T17:56:58+00:00, one hour after this continuation
started. Movement is present. Fifteen stable original irreducible-support
subsection units have each closed 21 previously open local defect rows:
315 explicit open-to-done witnesses in the current unit ledger. Their
units are {', '.join(witness_units)}. The complete original/receiving
readings and individual edits are recorded in CHECK_EVENTS.tsv and the
Paper II defects table. These witnesses exclude inherited D10/D16,
final order D14, and rendered typography D23.

Additional admitted text covers the foundations, cotangent/Euler and
normalization sections, with actual subsection-level records. The single
compact torus construction preserves the original local/global maps and
all conclusion aliases; its later duplicate subsection has been removed.
That scope migration and the subdivision of other sections are not counted
as movement. The meridian presentation, conductor duality, canonical-boundary
identity, curve-graph formula and blowup group maps now have single earlier
owners. Normalization's twelve units retain open inherited-locator and
rendered-typography rows. There are 129 plain program paths in the source;
derived records, counts, tags and deposit fields remain deferred.

Paper II's 198 required checks remain resolved. No additional global defect
class or final-PDF gate is closed. Papers III and IV remain unstarted, and
I/V retain their closed gates until the five-together step. The later
tangent/period/deformation fragment is ready but not yet admitted at this
review. E.5.2/E.5.3 statements remain unchanged. Six working pages were
actually viewed; final rendered-page credit remains zero.

Consecutive hourly reviews without movement: 0. Continue with the remaining
irreducible-support units and the prepared later-part integration; the
parallel unrestricted/reducible Euler work is proceeding from exact common
owners. Next hourly review: 2026-11-22T18:56:58+00:00 (25). Next scheduled
checkpoint: 2026-11-22T18:26:58+00:00 (37).
'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (ROOT/name).open('a',newline='\n') as f:f.write(addition)
print(f'Review24 at {stamp}: movement present;315 stable-unit defect-row witnesses; no-stall counter0.')
