"""Record the scheduled second hourly review of continuation five."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv

ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime(2026,11,23,20,26,17,tzinfo=timezone.utc)
assert now>=due, 'Review 37 is not yet due.'
csv.field_size_limit(100000000)
with (ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv').open() as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
assert len(rows)==128
closed=[r for r in rows if r['status']=='done']
previous_new={'02JA','02KC','02KF','02KH','02Q7','02M3','02M1'}
new=[r for r in closed if r['check_event_id'].startswith('publish:c5:') and r['tag'] not in previous_new]
assert len(closed)==26+len(new)
assert new
assert all(r['check_event_id'] and r['proof_comparison_evidence'] and r['derivation_completed_utc'] for r in closed)
with (ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv').open() as f:
    units=list(csv.DictReader(f,delimiter='\t'))
open_units=Counter(r['paper'] for r in units if r['status']=='open')
note=f'''
## Review 37 — {now.isoformat()}

INCOMPLETE. The scheduled 20:26:17 UTC review records qualifying
movement since Review 36: {len(new)} further existing Paper III required
rows are now done, namely {', '.join(r['tag'] for r in new)}. Paper III
stands at {len(closed)}/128 required checks, with {128-len(closed)} open.
Every closure has its complete fresh derivation and new computation
before individual proof release, its full printed/receiving comparison,
and its admitted event. The separate transitive 02KD check remains
outside the 128-row table and receives no required-row movement credit.

The new admitted work covers the radial period and quotient maps,
integral finite and reduced-filling attachment maps, exact orientations,
finite-family analytic scope, sphere construction and mixed cubic data,
and the smoothing's canonical and cohomological invariants. In the
order-four family the positive normal-circle and printed matrices are
related by explicit integral source and target involutions. The current
unadmitted packets retain their actual fresh, released or comparison
states; no unfinished comparison or numerical replay is credited.

The exact status of every required row remains in
S6_SERIES_PUBLISH_required_progress_III.tsv, and every open unit status
remains in S6_SERIES_PUBLISH_unit_progress.tsv. Open unit counts by paper
are {dict(open_units)}. All 756 Paper III unit criteria are still open;
source repairs remain queued. The III manuscript SHA-256 remains
9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0.
Its unit restructuring and defect removal, provenance, clean build,
typesetting and every final page reading retain their separate gates.
Paper IV's 66 required checks and 729 unit criteria still await III.
The main question remains completion of all five publication-ready papers.

Current I and V remain closed until the joint step; bounded cached-I
inputs earn no fresh-I credit. Paper II retains its final original gate.
Its E.5.2 and E.5.3 remain unchanged, and every III/IV use of the refined
II 02Y6/02XE statements still requires its downstream scope check.
D26 and later types on I, II and V, series references and notation,
deposit fields, records tables and the joint first-part readings remain
joint-step gates. Root's earlier target exposures remain binding;
the additional K9 paragraph exposure is recorded, and its complete
fresh derivation belongs to the unexposed finite-family checker.

Consecutive reviews without qualifying movement: 0. Review 38 is due
2026-11-23T21:26:17+00:00. Checkpoint 54 was saved and delivered at the
second scheduled 45-minute boundary; checkpoint 55 is due at
2026-11-23T20:41:17+00:00. Packaging and source retrieval count as no
movement. No inventory, census, manifest, seal, receipt, rebinding or
derived-file copy is made for this review.
'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    path=ROOT/name
    old=path.read_text()
    assert '\n## Review 37 — ' not in old
    path.write_text(old+note,newline='\n')
print(f'Review 37: {len(closed)}/128 required rows done; {len(new)} new since Review 36; no-movement count 0.')
