"""Seventh hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 2, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 55 — ' not in ledger
baseline = re.search(r'Closed required identities at Review54: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 110


def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


fields, rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02LC': (
        'whole_original_auxiliary_comparison_in_progress', '/root/iii_02ks',
        'Complete1378-line fresh proof,175-line input/primary note,474-line new program, all690 output lines and36-pattern table read by root. All six frozen hashes match. Individual original released02:30:46 UTC. The corrected marked rule is w^2=nu^2, with ten assignments changed and explicit inverse comparison maps. Whole-original comparison and receiver remain open.'),
    '02LD': (
        'whole_original_auxiliary_comparison_in_progress', '/root/iii_02kr',
        'Complete1646-line fresh proof and all four programs/outputs read by root; the separately frozen pre-exposure supplement proves every projected sample vector primitive for all allowed weights. Individual original released02:23:46 UTC after supplement completion02:21:18. Root and checker have read the entire statement and259-line original. All auxiliary claims and the495/459 scope distinction are being settled.'),
    '02LL': (
        'fresh_residual_two_primary_refined_class_open', '/root/iii_graph',
        'Original remains closed. Full mu and lambda calculations, actual cusp/elliptic weights, cyclic spin-bordism quotient and surgery-model maps are being written. The actual refined P value remains open in the kernel {0,c/2} of multiplication by2. No unproved integer lift of1-a is credited.'),
    '02LP': (
        'fresh_reassigned_after_quarantined_source_exposure', '/root',
        'Original remains closed for root. The former checker exposed isolated held LP/LF/LJ/LC/LO/LV lines in an overbroad bibliography query; its argument route is quarantined and earns no before-exposure check credit. Root read only the exposure note and line/tag metadata, with no argument snippets. Root now owns the fresh LP proof; a bounded independent primary consultation on general-order H6 and power operations is separate.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review55: ' + explanation

closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
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
## Review 55 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review54, {len(new)} required identities have closed:
{', '.join(new) or 'none'}. Paper III has {len(closed)}/128 complete
and {len(open_rows)} open. Every closure resolves to its exact events;
no identity admitted at Review54 has reopened. These required-row
closures are qualifying movement. The no-movement count is
{no_movement}. Restoring the earlier K9 check is excluded from new
movement because its identity was already closed at Review54.

L3 is admitted after the whole fresh proof, the full original,
receiving proof, raw-component program and all output were read.
Its unrestricted fibre/cap maps recover59 sphere patterns on50
initial rows, with the12 unbounded profiles and the remaining
finite profile counts. Exact generator maps and inverse maps
are retained. Its original mathematical conclusion stands.

LB is admitted after the full fresh proof, all333 original proof
lines, every auxiliary comparison, the798-line receiver, two new
programs and all output were read. The actual prescribed fan gives
the cubic1+kappa modulo2. Eight of15 patterns have cube1 and seven
have cube0; the two explicit surgery models and exact augmented
ring maps identify the two smooth types. The old uniform conic
identification is refuted with its refined statement. D25 records
the actual cusp degree and full circle-weight corrections, and
D27 records the changed smooth-type assignment. All labels and
targets remain in the guarded proposals. The complete Andrus
and Zhubr primary loci were read, including the exact recognition
scope and maps. The21 defect rows and seven events are admitted.

The corrected K9 source statement preserves its proved mathematics.
The primary pages print a rank condition on H2; the required
recognition scope is supplied by the explicit H3 surgery reduction
in section4.1. The two guarded source loci are corrected and the
new proposal supersedes the earlier K9 guards at integration.
The old before-exposure derivation remains unchanged. This is a
restored preexisting identity and contributes no new required row.

LC's full fresh proof and every line of output passed root review.
The actual global equivariant class gives mu=0 and the refined
coefficient(Q_f-a nu)/2. The exact Tate and generator maps give
w^2=nu^2 as the zero rule. Ten pattern assignments change; each
of the three oriented types has12 patterns. The full original
was individually released only after that review. Its complete
comparison, correction records and receiving proof remain open.

LD's entire fresh proof, all programs/output and all102 individual
sample-primitivity rows passed root review. The projected-lattice
conjugacy proves that primitivity for every allowed weight. The
complete original was then released and read. Its finite input
has495 patterns; requiring the III*/IV* caps to stay original
restricts it to459 by the proved inclusion and projection. The
scope wording and every original auxiliary assertion remain in
the complete comparison. The cusp boundary H2 claim is undergoing
an explicit integral Wang quotient/section verification.

LL's refined P value remains open at the actual order-two gate.
LP's accidental source exposure is recorded with its full line/tag
metadata, and the exposed route is quarantined. Root owns the
unexposed fresh derivation. The independent primary consultation
on cyclic H6 and coefficient operations supplies no complete LP
proof. These open routes earn no closure credit.

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

Checkpoint79 saved the112/128 state at02:19:29 UTC. It includes
the new L3 and LB closures and the restored K9 source correction.
The next checkpoint is due03:04:24 UTC; no extra checkpoint is
made at this review.

Closed required identities at Review55: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T03:34:24+00:00.
Next checkpoint: 2026-11-25T03:04:24+00:00.
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
    assert '\n## Review 55 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review55: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
