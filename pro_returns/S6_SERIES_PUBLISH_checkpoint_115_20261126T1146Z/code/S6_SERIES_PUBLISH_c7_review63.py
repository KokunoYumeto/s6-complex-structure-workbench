"""Fifteenth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 10, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 63 — ' not in ledger
baseline = re.search(r'Closed required identities at Review62: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 124

def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)

fields, rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02LS': ('released_historical_maps_receiver_and_records_review_in_progress', '/root/iii_02ks',
        'Fresh1216 frozen09:29:21 and original released09:37:04.929071. Root wholly read original/auxiliary and all three historical primary sources160/60/82, retrieval/retention/inspection/extraction sources and actual streams, bounded exact called helper bodies, and both new post-local150/post-relations161 sources. The direct lossless2038-line readback reconstructs every627+37+138 stdout line and both old JSON files exactly; agent wholly read it, root whole reading pending. Exact old70-to-new59 relation maps and inverses, physical-reflection divisor difference and meridian shear are retained. The772-line receiver remains under complete comparison and record review; no admission claimed.'),
    '02LG': ('clean_statement_fresh_synthesis_pending_supporting_unit_checks', '/root',
        'Original/history remain closed. Fresh synthesis must incorporate the completed LQ/LU and pending LS comparison plus LT/LV supporting results. LT798-line fresh proof and all293 source/21output lines are root-read; unit-only original released10:29:02.864443 without a required row. LV fresh lattice and toric computations are complete at their declared finite scopes, with all sources/outputs root-read. The refined circle-bordism route and exact global source-sphere auxiliary remain under fresh investigation. No completed LG proof or smaller-main-gate credit is claimed.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review63: ' + explanation
closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
assert set(new) == {'02LQ', '02LU'} and len(closed) == 126
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
no_movement = 0
open_table = '\n'.join('| ' + ' | '.join((r['tag'], r['label'], r['packet_status'], r['proof_status'])) + ' |'
                       for r in sorted(open_rows, key=lambda r: r['tag']))
note = f'''
## Review 63 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review62, {len(new)} required identities have closed: {', '.join(new)}.
Paper III has {len(closed)}/128 complete and {len(open_rows)} open.
Every admitted identity resolves to its exact events. K9 remains a
restored preexisting check and earns no new-row movement credit.
No smaller-main-gate credit is claimed for unfinished proofs, releases,
historical retrieval, receiver preparation, readback or packaging.

LQ was admitted09:43:52.976553 UTC after whole statement, original,
auxiliary,725-line receiver, historical replay and final-record reading.
The exact involution and inverse repair its intermediate orientation
assertion and preserve the theorem conclusions in the transported
marking. All24 D19 identity maps were read and checked bijectively.

LU was admitted10:20:11.164157 UTC after whole original/auxiliary,
652-line receiver and every comparison/record/source/stream reading.
Its complete archived comparison reconstructs42 tables,273 records
and1151 local maps, retaining the212 required residue cases and45
additional cases. Only the isolated historical rejection expression
was executed; no whole historical-module execution is claimed.
The final note gives literal input identities for the default kernel,
selector, KS zero divisor and whole-fibre difference. Its16 defects,
six events and three guarded replacements retain the exact scopes.

LS remains released and under complete comparison. Root read all
three primary historical sources and the exact extracted helpers,
all retrieval/retention/inspection sources and actual streams, and
the full two new validators. The lossless readback preserves every
old JSON field and the actual full marked relation maps/inverses.
Root whole output/receiver/record reading remains pending.

LT's798-line fresh proof, all293 source lines,21 stdout lines, empty
stderr, input/calculation notes and failed-edit preservation are
root-read. Its original was released as a unit-only obligation at
10:29:02.864443 UTC, proof21120--21275. No required-progress identity
was invented and no publication unit was closed.

LV's original/history remain closed. Root has a substantial new
derivation, an exact fresh lattice run and a toric coefficient run.
The index-two divisor lattice, all680 cubic coordinates, all mixed
coefficients, component restrictions and cyclic boundary periods
are retained with explicit inverse maps. Root wholly read the306-line
circle-bordism and local-obstruction note. Its refined-class route is
checked; the global source-sphere construction remains open.
LG's fresh synthesis remains open. No partial proof
is admitted through the completed neighboring cases.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

Released required comparisons still open: {', '.join(pending) or 'none'}.
All {units['III']} III unit criteria, all66 IV required checks and
all {units['IV']} IV unit criteria retain their open rows.
The canonical III source remains unchanged at SHA256 {source_sha}.
The main gate is all III required checks before source/bibliography
integration, full unit/provenance work, clean build and every rendered
page. IV follows III. I,II,V stay closed until the joint step.
The II E.5.2/E.5.3 inputs remain unchanged.

Checkpoint89 saved125/128 at09:49:42.331032 UTC, before LU admission.
Checkpoint90 is due at this review boundary10:34:24 UTC.

Closed required identities at Review63: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T11:34:24+00:00.
Next checkpoint91: 2026-11-25T11:19:24+00:00.
No inventory/census refresh or edit manifest, seal, receipt or rebinding
is made. Packaging earns no movement credit.
'''
buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer, fields, delimiter='\t', lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
(ROOT / 'S6_SERIES_PUBLISH_required_progress_III.tsv').write_text(buffer.getvalue(), newline='\n')
for name in ['PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md']:
    path = ROOT / name
    prior = path.read_text()
    assert '\n## Review 63 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review63: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
