"""Eighth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 3, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 56 — ' not in ledger
baseline = re.search(r'Closed required identities at Review55: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 112


def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


fields, rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02LE': (
        'fresh_minimal_patterns_derivation_in_progress', '/root/iii_02ks',
        'The original remains closed. The exact ten-pattern target and admitted LB/LC refinements are inputs to the fresh minimal-pattern classification. No complete derivation or original release is claimed.'),
    '02LH': (
        'fresh_odd_weighted_graph_and_cap_derivation', '/root/iii_02kr',
        'The original remains closed. The odd common-divisor graph quotient, doubled cocycle and unique odd halving are written. Actual peripheral lifts, saturated local kernels and the finite-first cusp component maps are being completed with full torsion retained.'),
    '02LL': (
        'fresh_characteristic_trace_and_index_under_root_review', '/root/iii_graph',
        'The original remains closed. The new written characteristic round-handle trace and finite index give a position-dependent candidate refined class. Root has read that entire note, its new program and every output line; the complete companion fresh proof and source hypotheses remain under root review. No admission credit yet.'),
    '02LP': (
        'fresh_refined_two_primary_bit_open', '/root',
        'The original remains closed for root. Full marked homology, cup products, higher coefficient mu and vanishing Chern/spin classes are written and the bounded peer review is complete. P is zero for 4 not dividing d and lies in {0,(d/2)s} otherwise. The exact Gamma coordinate morphism and the fully read 2013 three-frame criterion do not choose the remaining bit. No gate-reduction credit is claimed for that reformulation.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review56: ' + explanation

closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
assert {'02LC', '02LD'} <= set(new)
assert '02K9' in previous
for row in closed:
    for event_id in row['check_event_id'].split(';'):
        if event_id.strip():
            assert event_id.strip() in events
            assert events[event_id.strip()]['statement_id'] == row['label']
open_rows = [r for r in rows if r['status'] != 'done']
pending = [r['tag'] for r in open_rows if r['proof_status'] == 'released_after_derivation']
units = Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv')[1]
                if r['status'] == 'open')
assert units['III'] == 784 and units['IV'] == 756
source_sha = hashlib.sha256((ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
old_counts = re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.', ledger)
assert old_counts
no_movement = 0 if new else int(old_counts[-1]) + 1
open_table = '\n'.join(
    '| ' + ' | '.join((r['tag'], r['label'], r['packet_status'], r['proof_status'])) + ' |'
    for r in sorted(open_rows, key=lambda r: r['tag']))
note = f'''
## Review 56 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review55, {len(new)} required identities have closed:
{', '.join(new)}. Paper III has {len(closed)}/128 complete and
{len(open_rows)} open. Every closed row resolves to its exact events;
no identity admitted at Review55 has reopened. These closures are
qualifying movement. The consecutive no-movement count is {no_movement}.
K9 is a restored preexisting identity and earns no new-row credit.

LD was admitted at03:09:39 UTC after the complete fresh derivation,
its pre-exposure supplement, all new programs and output, the whole
original, every auxiliary claim, the1759-line receiver and469-line
comparison were read. The weighted cusp boundary maps retain the
full H1 torsion; finite-first kernels and all sample primitivities
are established by actual integral maps. The495-pattern broad scope
and459-pattern unchanged-star scope have explicit inclusion and
projection maps. D26 records that scope distinction. Its35 defect
rows and two events belong to their recorded common evidence group.

LC was admitted at03:14:41 UTC after the full1378-line fresh proof,
all new code and output, the whole251-line original proof, every
auxiliary, the1032-line receiver and349-line comparison were read.
The actual physical normal weights and exact group automorphisms
give the corrected zero rule w^2=nu^2 and the refined coefficient
(Q_f-a nu)/2. Ten assignments change, while the three oriented types
still have twelve patterns each. D25 records the local wall and
weight errors; D27 records the false assignment. The ten defect
rows and four events retain their precise scopes. The retained
execution-history limitation is explicit: earlier failed source
versions and failed-run streams are unavailable, while the final
sources and all saved successful output were read. No unavailable
bytes, empty stderr or historical execution are claimed.

LE and LH are in fresh derivation with their originals closed.
LH now retains the odd vertical torsion in the graph quotient and
the distinct cusp component meridians; the complete cap sequence
and independent matrices remain in progress.

LL's new characteristic round-handle note has actual solid-torus
maps and inverses, a characteristic extension, an integral endpoint
and every nonidentity finite character. Its position-dependent
candidate P values are undergoing root review with the entire
companion fresh proof. No target original has been exposed and no
required row is admitted from this candidate calculation.

LP's partial fresh proof and bounded peer review establish the
full marked homology, cup products, higher coefficient fundamental
class and vanishing Chern/spin classes. The even refined class is
still in the two-element range at4-divisible d. The exact Gamma
morphism and Zhubr2013's fully read three-frame criterion reformulate
that gate without selecting its value. They earn no strictly
smaller-gate credit. Root's original remains closed and the former
checker's exposed route remains quarantined.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

Released comparisons still open: {', '.join(pending) or 'none'}.
All {units['III']} III unit criteria, all66 IV required checks and
all {units['IV']} IV unit criteria retain their existing open rows.
The canonical III source remains unchanged at SHA256 {source_sha}.
The main gate is all III required checks before guarded source
and bibliography integration, the full unit pass, provenance,
clean build and rendered-page reading. IV follows III. I,II,V
retain their closed gates until the five-together step. The II
E.5.2/E.5.3 inputs remain unchanged.

Checkpoint80 saved the112/128 snapshot at03:07:18 UTC, before the
LC and LD admissions. The next checkpoint is due03:49:24 UTC;
no extra checkpoint is made at this review.

Closed required identities at Review56: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T04:34:24+00:00.
Next checkpoint: 2026-11-25T03:49:24+00:00.
No inventory/census refresh or edit manifest, seal, receipt or
rebinding is made. Packaging earns no movement credit.
'''
buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer, fields, delimiter='\t', lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
(ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv').write_text(buffer.getvalue(), newline='\n')
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    path = ROOT / name
    prior = path.read_text()
    assert '\n## Review 56 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review56: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
