"""Record continuation five's fifth hourly review from actual closed row sets."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert now >= datetime(2026, 11, 23, 23, 26, 17, tzinfo=timezone.utc)
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
baseline = re.search(r'^Closed required identities at Review39: (.+)\.$', ledger, re.M)
assert baseline
previous_closed = set(baseline[1].split(', '))
assert len(previous_closed) == 46


def table(name):
    with (ROOT / name).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {row['event_id']: row for row in table('CHECK_EVENTS.tsv')}
closed = [row for row in rows if row['status'] == 'done']
closed_tags = {row['tag'] for row in closed}
new = sorted(closed_tags - previous_closed)
reopened = sorted(previous_closed - closed_tags)
assert len(rows) == 128 and new and not reopened
for row in closed:
    assert row['check_event_id'] in events
    assert events[row['check_event_id']]['statement_id'] == row['label']
units = table('S6_SERIES_PUBLISH_unit_progress.tsv')
open_units = Counter(row['paper'] for row in units if row['status'] == 'open')
pending = sorted(row['tag'] for row in rows
                 if row['status'] == 'open'
                 and row['proof_status'] == 'released_after_derivation')
source_sha = hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
note = f'''
## Review 40 — {now.isoformat()}

INCOMPLETE. The scheduled 23:26:17 UTC review records qualifying movement
since Review39: {len(new)} existing required III rows changed to done,
namely {', '.join(new)}. Paper III has {len(closed)}/128 required checks
complete and {128-len(closed)} open. This comparison uses the actual
closed-identity set recorded at Review39, not dates on events proposed
before their admission. No previously closed identity reopened.

Every credited closure has a complete written fresh derivation and new
computation before its individual proof release, a full original/receiving
comparison, and an admitted event. The metric checks specify the marked
quotient isometries, collar and local-homology maps, pointed convergence
maps and distance obstructions. The arbitrary-compatible-metric assertion
has its recorded counterexample and scope correction. The finite-filling
checks retain the exact marked frame changes and integral homology maps.
Publication repairs remain in their guarded packets; they are not yet
applied to the manuscript.

Individually released comparisons still open: {', '.join(pending) or 'none'}.
All work on these pending comparisons receives no completed-row credit.
The seven-family calculation includes the full relative and Mayer--Vietoris
maps and a pre-exposure affine-norm addendum. The cone-obstruction derivation
includes the M=1 identity endpoint and the M>1 branch-cover obstruction.
The fixed-metric realization includes all-order actual-period derivatives
and complete metric-ball estimates. Their individual comparison and
admission states remain those of the live required-row table.

Every required-row status is in S6_SERIES_PUBLISH_required_progress_III.tsv;
every unit-row status is in S6_SERIES_PUBLISH_unit_progress.tsv.
Open unit counts: {dict(open_units)}. All 756 III unit criteria remain
open. III source SHA256: {source_sha}.
The main question remains completion of all five publication-ready papers.
Its remaining gates are III's required checks, unit restructuring and defect
removal, provenance, clean build, typesetting and every rendered-page
reading; then IV's 66 checks and 729 unit criteria and its corresponding
publication gates; then the joint series work.

Current I and V remain closed until the joint step. Bounded earlier-I
construction inputs receive no I credit. II retains its final gate and
unchanged E.5.2/E.5.3 statements. Every III/IV use of refined II02Y6/02XE
still requires the downstream scope check. Joint D26/later-type application,
references, notation, deposit fields, records tables and final first-part
readings remain pending.

Closed required identities at Review40: {', '.join(sorted(closed_tags))}.

Consecutive reviews without qualifying movement: 0. Review41 is due
2026-11-24T00:26:17+00:00. Checkpoint58 was saved on the 22:56 boundary;
checkpoint59 is due 2026-11-23T23:41:17+00:00. Packaging and unadmitted
work count as no movement. This review produces no inventory, census,
manifest, seal or copy of derived files.
'''
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    path = ROOT / name
    text = path.read_text()
    assert '\n## Review 40 — ' not in text
    path.write_text(text + note, newline='\n')
print(f'Review40: {len(closed)}/128 done; {len(new)} newly closed since39; no-movement count0.')
print('Newly completed:', ', '.join(new))
print('Open released comparisons:', ', '.join(pending))
