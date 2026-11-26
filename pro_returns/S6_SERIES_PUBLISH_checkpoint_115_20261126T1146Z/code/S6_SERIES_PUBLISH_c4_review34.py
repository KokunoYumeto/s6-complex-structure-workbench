"""Record the fifth scheduled hourly review of the fourth continuation."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 23, 15, 47, 46, tzinfo=timezone.utc)
assert now >= due, 'Scheduled review 34 is not yet due.'
csv.field_size_limit(100000000)
with (ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').open() as f:
    units = list(csv.DictReader(f, delimiter='\t'))
open_units = Counter(r['paper'] for r in units if r['status'] == 'open')
assert open_units['II'] == 0
with (ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv').open() as f:
    required = list(csv.DictReader(f, delimiter='\t'))
assert len(required) == 128
closed = [r for r in required if r['status'] == 'done']
prior = {'02QC', '02Q8', '02J4', '02QE', '02J3', '02K5', '02J6', '02J5', '02K3', '02K4'}
assert prior <= {r['tag'] for r in closed}
new = [r for r in closed if r['tag'] not in prior]
assert all(r['check_event_id'] and r['proof_comparison_evidence'] and r['derivation_completed_utc'] for r in closed)
assert len(new) > 0
note = f'''
## Review 34 — {now.isoformat()}

INCOMPLETE. The scheduled 15:47:46 UTC review records qualifying movement:
{len(closed)} of the 128 existing Paper III required-check identities are now
complete, {len(new)} more than the corrected review-33 baseline of ten. The
newly closed identities are {', '.join(r['tag'] for r in new)}. Review 33's
initial eleventh identity, 02L5, had its strict fresh-check credit withdrawn
because of the subsequently identified clutch-arrow discrepancy. Its old
event remains in the append-only history; it contributes no live completion
credit. A new isolated checker has supplied a complete pre-exposure derivation
using the prescribed exterior-to-local gluing, new arithmetic, and a complete
comparison; central review and distinct-event admission are still pending.
The completed 02J9 package is likewise awaiting central full reading.

Each admitted identity has a complete written fresh derivation fixed before
its individual proof release, a full comparison of the printed proof, and a
root-admitted targeted event. Computations and primary-source readings support
these events; they do not add independent check credit. No extraction, hash,
new administrative row, checkpoint packaging, or unadmitted agent completion
is counted as qualifying movement.

The original checkpoint-44 open II unit criteria remain closed. The dated II
gate concerns the original 25-type register. New statement-scope type D26 has
been entered in S6_DEFECT_REGISTER.csv, with explicit pending application to
all five papers. It adds 28 III and 27 IV open criteria and five paper-level
application gates. These newly added rows receive no baseline-progress credit.
II's D26 application is pending at joint review; no existing II row was
reopened without an actual found instance. Open unit criteria by paper:
{dict(open_units)}. No III unit criterion is closed merely by completing a
required check. {128-len(closed)} III required checks remain open. IV's 66
required checks await the III gate, and current I and V manuscripts remain
unopened until the joint step.

Concrete receiving-proof work now includes the exact local Kummer map and
its degree under the rescaled source torus; the N=1 scope of normalization
claims; local invariant-ring flatness and global cover gluing; the actual
cyclic fundamental-group presentation; and complete angle-forgetting and
cofiber homotopies. These source applications, unit criteria and final visual
readings are still pending. The new Euler arithmetic agrees with original
saved numerical outputs, but neither equality of those outputs nor source
formulas establishes the missing identification with the API's saved
attachments and geometric realizations. No such identification is credited.

The root's overly broad II filename search also returned two lines of the
02JA proof from III. The assigned fresh checker, horizontal, has not received
those lines or any target proof or prior outcome; root claims no fresh 02JA
derivation. The current I and V texts remain closed. Bounded cached-I
statement inputs are identified as such and receive no fresh-I credit.

The main question remains the complete five-paper publication revision.
The protected II statements E.5.2 and E.5.3 remain unchanged. Every III/IV
application of refined II 02Y6 and 02XE still requires its explicit downstream
recheck. Consecutive reviews without qualifying movement: 0. Review 35 is
due 2026-11-23T16:47:46+00:00. Checkpoint 50 has been saved and delivered;
checkpoint 51 is due 2026-11-23T16:02:46+00:00. No per-edit inventory,
manifest, seal, rebinding or derived-file copy is produced by this review.
'''
for name in ('PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md'):
    path = ROOT / name
    old = path.read_text()
    assert '\n## Review 34 — ' not in old
    path.write_text(old + note, newline='\n')
print(f'Review34: {len(closed)} existing III required rows closed; {len(new)} new since corrected review33; no-movement count 0.')
