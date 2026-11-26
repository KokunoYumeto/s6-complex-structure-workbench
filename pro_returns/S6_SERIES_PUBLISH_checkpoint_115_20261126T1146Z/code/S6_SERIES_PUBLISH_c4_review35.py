"""Record the sixth scheduled hourly review of the fourth continuation."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 23, 16, 47, 46, tzinfo=timezone.utc)
assert now >= due, 'Scheduled review 35 is not yet due.'
csv.field_size_limit(100000000)
with (ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').open() as f:
    units = list(csv.DictReader(f, delimiter='\t'))
open_units = Counter(r['paper'] for r in units if r['status'] == 'open')
assert open_units['II'] == 0
with (ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv').open() as f:
    required = list(csv.DictReader(f, delimiter='\t'))
assert len(required) == 128
closed = [r for r in required if r['status'] == 'done']
prior = {'02QC', '02Q8', '02J4', '02QE', '02J3', '02K5', '02J6',
         '02J5', '02K3', '02K4', '02J7', '02K6', '02K7', '02K2', '02J8'}
assert prior <= {r['tag'] for r in closed}
new = [r for r in closed if r['tag'] not in prior]
assert all(r['check_event_id'] and r['proof_comparison_evidence']
           and r['derivation_completed_utc'] for r in closed)
assert len(new) > 0
note = f'''
## Review 35 — {now.isoformat()}

INCOMPLETE. The scheduled 16:47:46 UTC review records qualifying movement:
{len(closed)} of the 128 existing Paper III required-check identities are
complete, {len(new)} more than review 34's exact baseline of fifteen.
The newly closed identities are {', '.join(r['tag'] for r in new)}.
Each has a complete written pre-proof derivation, its individual authorized
proof release, the full printed-proof comparison and a root-admitted event.
The replacement 02L5 check is the isolated fresh-Euler event; its earlier
withdrawn event remains history and receives no live completion credit.

The completed checks supply the actual cofiber and whole-neighbourhood maps,
the integral cusp normalization complex with explicit matrix basis changes,
and the characteristic-class and rational-ring constraints through the
actual deck, restriction and coefficient maps. In 02KE the unqualified
undetermined-class tail fails at d=1: multiplication by 1 has zero kernel.
Its bounded statement refinement has the prescribed refutation disposition;
that disposition is part of the same error finding and adds no independent
method or required-row movement. The separate integral-homology gate 02KD
is an existing transitive dependency, with its 1004-line fresh derivation
and new arithmetic fixed before the 16:37:31 UTC proof release. It creates
no new required identity. Its comparison and receiving disposition retain
their exact evidence state, as do the 02JA and 02KC checks.

No extraction, hash, new administrative criterion, checkpoint packaging,
unadmitted agent completion, primary-source reading or numerical replay
is counted as qualifying movement. New D26 criteria and the five paper-level
application gates remain outside this baseline. Open unit criteria by paper:
{dict(open_units)}. No III unit criterion is closed merely by completing a
required check. {128-len(closed)} III required identities remain open. All
receiving source applications, provenance and unit publication criteria,
typesetting and final page-image reading remain at their own explicit gates.

The II closure remains its dated completion against the original 25-type
register. Its D26 application awaits the joint step; no historical closure
is treated as a completed new-type application. IV's 66 required checks
await the III gate. Current I and V manuscripts remain unopened until the
joint step. Bounded cached-I statement inputs receive no fresh-I credit.
The protected II E.5.2 and E.5.3 statements remain unchanged, and every
III/IV use of the refined 02Y6 and 02XE inputs still requires its explicit
downstream recheck.

Exposure precision: root's earlier two-line 02JA proof exposure remains
recorded; horizontal supplied that fresh derivation without those lines.
While resolving the exact historical KD program-run identifiers after its
proof release, root's ledger search also displayed the retained D.1.12
checking outcome. Root therefore claims no fresh D.1.12 derivation; a checker
unexposed to that outcome must own any subsequent strict fresh check there.
Neither current I nor current V text was opened by that metadata search.

The main question remains the complete five-paper publication revision.
Consecutive reviews without qualifying movement: 0. Review 36 is due
2026-11-23T17:47:46+00:00. Checkpoint 51 has been saved and delivered;
checkpoint 52 is due now at 16:47:46 UTC and is prepared immediately after
this review. Checkpoint 53 is due 17:32:46 UTC. No per-edit inventory,
manifest, seal, rebinding or derived-file copy is produced by this review.
'''
for name in ('PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md'):
    path = ROOT / name
    old = path.read_text()
    assert '\n## Review 35 — ' not in old
    path.write_text(old + note, newline='\n')
print(f'Review35: {len(closed)} existing III required rows closed; '
      f'{len(new)} new since review34; no-movement count 0.')
