"""Tenth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 5, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 58 — ' not in ledger
baseline = re.search(r'Closed required identities at Review57: ([^\n]+)\.', ledger)
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
    '02LF': ('fresh_three_primary_geometry_and_catalogue_in_progress', '/root/iii_02ks',
        'The fresh checker retains statement-only exposure and is saving the complete C3/C9 operation and full-parameter proof. Its raw-only catalogue program is successful, with the first failed fixed-lift assumption retained. Root accidentally saw canonical16755–16764 during LH boundary verification; that exact spill is recorded and gives root no independent fresh-LF credit. No full fresh freeze or release has occurred.'),
    '02LH': ('released_final_receiver_wholly_read_records_pending', '/root/iii_02kr',
        'Root has read the whole original, the fresh757-line derivation and586-line local companion, the full post-exposure note including smooth collar and omitted-return maps, the final1680-line receiver, all new mathematical programs/streams, all four assembly sources/streams and both syntax-check sources/streams. Final comparison and proposed records await complete reading and admission.'),
    '02LI': ('fresh_all_parity_bar_and_cap_derivation_in_progress', '/root/iii_graph',
        'Original and historical target programs remain closed. The exact bar core, full LH fresh/local inputs and the all-parity central shear with its inverse are being extended to the complete cap/global proof and independent ordered-generator computation. The current work is not frozen or admitted.'),
    '02LK': ('assigned_statement_only_after_lh_records', '/root/iii_02kr',
        'Assigned as the next fresh derivation after LH records. Root has read the exact statement-only packet; no LK original or historical target program has been opened in this lane.'),
    '02LM': ('fresh_critical_cycle_and_framing_derivation_in_progress', '/root',
        'The exact statement-only target and disclosed admitted LL/LP inputs have been read. A new raw-period intake computes all seven marked rows and eleven patterns. Fresh sections1–4 give the full parameter lattice maps, literal critical cycles and finite-II detector/framing route. The coefficient-operation and complete new computation sections remain to be finished before freeze. Original and historical target work remain closed.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review58: ' + explanation

closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
assert {'02LL', '02LE', '02LP'} <= set(new)
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
assert old_counts and old_counts[-1] == '1'
no_movement = 0 if new else int(old_counts[-1])+1
open_table = '\n'.join('| ' + ' | '.join((r['tag'], r['label'], r['packet_status'], r['proof_status'])) + ' |'
                       for r in sorted(open_rows, key=lambda r:r['tag']))
note = f'''
## Review 58 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review57, {len(new)} required identities have closed:
{', '.join(new)}. Paper III has {len(closed)}/128 complete and
{len(open_rows)} open. Every admitted row resolves to its exact events;
no previously closed identity has reopened. K9 remains a restored
preexisting identity and earns no new-row movement credit.
Consecutive no-movement count is now {no_movement}. No strictly smaller
main-gate credit is claimed for unfinished fresh or receiving work.

LL was admitted at04:40:03 UTC, LE at05:05:08 UTC and LP at05:23:14 UTC.
Their root reviews record the complete original/auxiliary/receiver
readings and every new program/stream scope. LL's critical-cycle and
characteristic-bordism computations give the corrected position values;
LE gives three oriented types at order10 and two at order14; LP retains
its theorem with full mod-2d/mod-3d coordinates and P=0 for every d.
LP's independent circle proof stays in the check files, leaving one
receiving proof with every original detector auxiliary.

LH's final1680-line receiver and all assembly sources have now been
wholly read by root. Its comparison and records await final admission.
LI's all-parity bar and cap proof is in progress. LF's fresh checker
has the actual C3/C9 isotropy and a successful new eight-pattern raw
catalogue calculation; its whole proof is not yet frozen. The root's
ten-line accidental LF exposure is recorded without fresh-check credit.
LK is assigned next after LH records. Root has begun LM from its
statement and admitted inputs, saved its full-parameter critical-cycle
and finite-II framing argument, and run the new raw-period intake.
Its remaining coefficient and computation work precedes release.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

Released comparisons still open: {', '.join(pending) or 'none'}.
All {units['III']} III unit criteria, all66 IV required checks and
all {units['IV']} IV unit criteria retain their open rows.
The canonical III source remains unchanged at SHA256 {source_sha}.
The main gate remains all III required checks before exact source and
bibliography integration, the full unit pass, provenance, clean build
and rendered-page reading. IV follows III. I,II,V remain closed until
the five-together step. The II E.5.2/E.5.3 inputs remain unchanged.

Checkpoint83 saved116/128 at05:20:24 UTC; LP was admitted afterward.
Its saved snapshot and this subsequent review have their exact scopes.

Closed required identities at Review58: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T06:34:24+00:00.
Next checkpoint84: 2026-11-25T06:04:24+00:00.
No inventory/census refresh or edit manifest, seal, receipt or rebinding
is made. Packaging earns no movement credit.
'''
buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer, fields, delimiter='\t', lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
(ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv').write_text(buffer.getvalue(), newline='\n')
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    path = ROOT/name
    prior = path.read_text()
    assert '\n## Review 58 — ' not in prior
    path.write_text(prior+note, newline='\n')
print(f'Review58: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
