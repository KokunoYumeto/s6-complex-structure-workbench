"""Ninth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 4, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 57 — ' not in ledger
baseline = re.search(r'Closed required identities at Review56: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 114


def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


fields, rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02LE': (
        'released_complete_original_comparison_in_progress', '/root/iii_02ks',
        'The complete fresh derivation and all its new programs and output were read before release. Root has now read the whole original statement and201-line proof. The comparison, every auxiliary and receiver remain pending admission.'),
    '02LH': (
        'fresh_complete_saved_data_audit_before_release', '/root/iii_02kr',
        'The original remains closed. The frozen757-line fresh proof and586-line local companion, all eleven programs and all stdout/stderr have been read by root. A separate audit reconstructs every saved matrix and checks the large serialized data before original release. No manual reading of every large JSON entry is claimed.'),
    '02LL': (
        'released_final_receiver_records_under_root_review', '/root/iii_graph',
        'Root has read the entire frozen876-line final receiver and the whole original and auxiliary review. Its comparison, guards and event records are being completed and read. The row remains open until root admission.'),
    '02LP': (
        'released_fresh_bordism_complete_auxiliary_review_complete', '/root/iii_graph',
        'The complete fresh proof, characteristic circle bordism and refined-class proof were frozen and read before original release. The actual bordism proves the remaining two-primary P coefficient zero. Root has read all released statement/proof lines and the complete663-line post-exposure auxiliary review. Receiver, comparison and admission remain open.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review57: ' + explanation

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
assert old_counts and old_counts[-1] == '0'
no_movement = 0 if new else int(old_counts[-1]) + 1
open_table = '\n'.join(
    '| ' + ' | '.join((r['tag'], r['label'], r['packet_status'], r['proof_status'])) + ' |'
    for r in sorted(open_rows, key=lambda r: r['tag']))
note = f'''
## Review 57 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review56, {len(new)} required identities have closed:
{', '.join(new) or 'none'}. Paper III has {len(closed)}/128 complete and
{len(open_rows)} open. Every closed row resolves to its exact events;
no identity admitted at Review56 has reopened. K9 remains a restored
preexisting identity and earns no new-row movement credit.
The consecutive no-movement count is {no_movement}. No strictly
smaller-main-gate credit is claimed for the unadmitted work below.

LL's final876-line receiver has been wholly read by root, together
with its complete fresh proof, characteristic companion, original
proof and post-exposure auxiliaries. The comparison and final guard
and event records are still under review. The exact character and
critical-cycle computations change four original model positions.
No admission is inferred from the existence of the final receiver.

LE's fresh proof was completed and frozen at04:04:24 UTC. After
root read the whole proof, all new sources and every saved output,
the original was released at04:13:26 UTC. Root has read the whole
released statement and201-line proof. The physical fixed-curve
characters give three oriented types at order10 and two at order14.
Every original auxiliary, including the coprime coefficient-space
maps and connected-sum bordism, is being settled in the receiver.

LH's757-line fresh proof and586-line local companion were frozen
at04:21:45 UTC with its original closed. Root has read both in full,
the statement/dependency packet, all eleven programs and all their
stdout/stderr. The saved large JSON files received generation and
readout checks, without a claim that every entry was manually read.
A separate audit now reconstructs all6326 global matrices and
checks the saved local maps, finite actions and24 Smith equivalences.
The original remains closed pending that audit and root review.

LP's complete fresh proof, circle-bordism companion and refined
proof were frozen at04:06:19 UTC. The actual characteristic bordism
proves P=0 also at4-divisible d. Root then read the entire released
original, including both proof spans, and the663-line complete
post-exposure auxiliary review. That review supplies the support
gauge and its inverse, the physical three-frame/link calculation,
the cohomology-operation normalization and exact recognition scope.
The receiver and comparison remain to be assembled and admitted.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

Released comparisons still open: {', '.join(pending) or 'none'}.
All {units['III']} III unit criteria, all66 IV required checks and
all {units['IV']} IV unit criteria retain their open rows.
The canonical III source remains unchanged at SHA256 {source_sha}.
The main gate is all III required checks before guarded source
and bibliography integration, the full unit pass, provenance,
clean build and rendered-page reading. IV follows III. I,II,V
retain their closed gates until the five-together step. The II
E.5.2/E.5.3 inputs remain unchanged.

Checkpoint81 saved114/128 at03:50:37 UTC. Checkpoint82 is due at
04:34:24 UTC and will record its actual snapshot time. It is the
scheduled checkpoint, not an additional hourly-review archive.

Closed required identities at Review57: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T05:34:24+00:00.
Next checkpoint after82: 2026-11-25T05:19:24+00:00.
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
    assert '\n## Review 57 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review57: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + (', '.join(new) or 'none'))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
