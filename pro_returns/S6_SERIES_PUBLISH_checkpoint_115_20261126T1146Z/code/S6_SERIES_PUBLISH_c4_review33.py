"""Record the fourth scheduled hourly review of the fourth continuation."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv

ROOT=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime(2026,11,23,14,47,46,tzinfo=timezone.utc)
assert now>=due, 'Scheduled review 33 is not yet due.'
csv.field_size_limit(100000000)
with (ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv').open() as f:
    units=list(csv.DictReader(f,delimiter='\t'))
open_units=Counter(r['paper'] for r in units if r['status']=='open')
assert open_units['II']==0
with (ROOT/'S6_SERIES_PUBLISH_required_progress_III.tsv').open() as f:
    required=list(csv.DictReader(f,delimiter='\t'))
assert len(required)==128
closed=[r for r in required if r['status']=='done']
prior={'02QC','02Q8'}
new=[r for r in closed if r['tag'] not in prior]
assert all(r['check_event_id'] and r['proof_comparison_evidence'] and r['derivation_completed_utc'] for r in closed)
assert len(new)>0
note=f'''
## Review 33 — {now.isoformat()}

INCOMPLETE. The scheduled 14:47:46 UTC review records qualifying movement:
{len(closed)} of the 128 existing Paper III required-check identities are now
complete, {len(new)} more than the two at review 32. The newly closed identities
are {', '.join(r['tag'] for r in new)}. Each has a written complete fresh
derivation fixed before its individual proof release, a full comparison of
the printed proof, and a root-admitted targeted event. Their supporting
computations, source reads and repairs form those events rather than extra
independent-check credit. Extraction, hashes, newly added records and
checkpoint packaging receive no qualifying-movement credit.

The 982 original checkpoint-44 open II unit criteria remain closed, with all
5,876 II criteria done and the final II gate retained. Open publication-unit
criteria by paper: {dict(open_units)}. No III unit criterion is closed merely
by completion of a required check. {128-len(closed)} III required checks remain
open. IV's 66 required checks await the III gate; the current I and V
manuscripts remain unopened until the joint step.

The review has identified concrete III receiving-proof work: the full-family
stable framing in 02J5; the explicit reversed-meridian lattice automorphism
in 02K4; and replacement of unverified geometric realizations in 02L5 by
actual holomorphic collar gluings. The exact cusp gluing arrow is exterior
to local, G0 composed with translation, and its inverse-loop sign is being
bound explicitly in the receiving proofs. The 02K3 fan presentation is being
joined to the prescribed fan by diag(1,-1,1), with the corresponding torus
map and scalar-lattice preservation. These source applications, unit-level
mathematical/editorial criteria and final page readings remain pending.

The main question remains the complete five-paper publication revision.
Work continues in III with individually assigned fresh local Kummer,
retained-angle, global fundamental-group and normal-global-cover checks.
All target proof embargoes are preserved until each written derivation is
reviewed and released. The bounded cached-I proof exposure recorded in the
preceding ledger entry receives no fresh-I credit and does not open the
current I manuscript. The protected II statements E.5.2 and E.5.3 remain
unchanged. Every III/IV application of refined II 02Y6 and 02XE still requires
its explicit downstream recheck.

Consecutive reviews without qualifying movement: 0. Review 34 is due
2026-11-23T15:47:46+00:00. Checkpoint 49 has been saved and delivered;
checkpoint 50 is due 2026-11-23T15:17:46+00:00. No per-edit inventory,
manifest, seal, rebinding or derived-file copy is produced by this review.
'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    p=ROOT/name
    old=p.read_text()
    assert '\n## Review 33 — ' not in old
    p.write_text(old+note,newline='\n')
print(f'Review33: {len(closed)} existing III required rows closed; {len(new)} new since review32; no-movement count0.')
