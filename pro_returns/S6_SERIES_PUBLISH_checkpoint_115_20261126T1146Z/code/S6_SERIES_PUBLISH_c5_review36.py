"""Record the first scheduled hourly review of continuation five."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 23, 19, 26, 17, tzinfo=timezone.utc)
assert now >= due, 'Review 36 is not yet due.'
csv.field_size_limit(100000000)
with (ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv').open() as f:
    units = list(csv.DictReader(f, delimiter='\t'))
open_units = Counter(r['paper'] for r in units if r['status'] == 'open')
with (ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv').open() as f:
    required = list(csv.DictReader(f, delimiter='\t'))
assert len(required) == 128
closed = [r for r in required if r['status'] == 'done']
new = [r for r in closed if r['check_event_id'].startswith('publish:c5:')]
assert len(closed) - len(new) == 19
assert all(r['check_event_id'] and r['proof_comparison_evidence']
           and r['derivation_completed_utc'] for r in closed)
assert new
note = f'''
## Review 36 — {now.isoformat()}

INCOMPLETE. This continuation's scheduled 19:26:17 UTC hourly review
records qualifying movement: {len(closed)} of Paper III's 128 existing
required-check identities are complete, {len(new)} more than the attached
checkpoint 52 baseline of nineteen. The newly closed identities are
{', '.join(r['tag'] for r in new)}. Each closure has its written derivation
fixed before individual proof release, a complete comparison against the
printed proof, receiving guards and a root-admitted check event. The
separate 02KD integral-homology comparison has also been completed and
admitted; as a transitive dependency outside the 128-row table, it adds
no required-row movement.

The new work settles the explicit quotient and cusp maps, the rational
cover calculation, the integral ruling-to-torus map used for the cover
ring, the pullback of characteristic classes through the actual transfer,
the based cusp factorization, the conifold smoothing topology and its
comparison with the stated CDP98 examples. The exact matrix, covering,
chain, divisor and quotient maps are recorded in the respective check
packets. Source applications remain queued: the III source SHA-256 is
still 9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0.

There are {128-len(closed)} open III required identities. Their exact
per-row states, including proof-closed, released and comparison-pending
states, remain in S6_SERIES_PUBLISH_required_progress_III.tsv. All open
unit statuses remain in S6_SERIES_PUBLISH_unit_progress.tsv; counts by
paper are {dict(open_units)}. No III unit criterion closes by completing
a required check. The III text restructuring, every unremoved unit defect,
the receiving edits, the provenance claims, the clean build, typesetting
and each page-image reading retain their separate gates. IV's 66 required
checks and 729 unit criteria await completion of III. The main question
remains the complete publication revision of all five papers.

No packaging, source download, extraction, hash, administrative row,
unadmitted derivation or numerical replay is counted as movement. The
02LR and 02KG comparison gates and the current carrier and smoothing
derivations have their actual recorded states; review credit does not
anticipate their admission. The full frozen derivation and new arithmetic
remain required before each target proof opens.

Paper II retains its completed original 25-type gate. D26 and any later
new types for I, II and V remain joint-step work. Current I and V sources
have not been reopened; bounded cached-I dependencies give no fresh-I
credit. II E.5.2 and E.5.3 are unchanged. Every III/IV use of the refined
II 02Y6 and 02XE statements still needs its explicit downstream recheck.
The earlier root exposures recorded in the live table remain binding,
including D.1.12, the 037X/037Y/0382 cusp-cover scope material and 02KU;
an unexposed checker must own their strict fresh checks.

Consecutive reviews without qualifying movement: 0. Review 37 is due
2026-11-23T20:26:17+00:00. Checkpoint 53 was saved and delivered at the
scheduled first 45-minute boundary; checkpoint 54 is due at
2026-11-23T19:56:17+00:00. This review adds no inventory, census, manifest,
seal, receipt, rebinding or derived-file copy.
'''
for name in ('PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md'):
    path = ROOT / name
    old = path.read_text()
    assert '\n## Review 36 — ' not in old
    path.write_text(old + note, newline='\n')
print(f'Review 36: {len(closed)}/128 required identities closed; '
      f'{len(new)} newly closed; no-movement count 0.')
