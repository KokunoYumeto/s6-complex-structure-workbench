"""Thirteenth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 8, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 61 — ' not in ledger
baseline = re.search(r'Closed required identities at Review60: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 121


def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


fields, rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02LJ': ('released_receiver_and_comparison_records_under_root_review', '/root/iii_02ks',
        'Fresh1480-line proof frozen07:46:54; original released08:00:09.739241. Root read every original and following auxiliary, full1515-line staged receiver, historical118-line source and724-line JSON, new140-line validator and all77 output lines, both retrieval sources and every actual stream. Receiver-only textfix_v003 yields1476 lines after moving the alternate circle-pair proof to checking notes and the computational auxiliary inside the proof. Final comparison/proposals and exact diff readback remain required before admission. Seven model assignments are corrected; no historical executable was run.'),
    '02LN': ('released_original_comparison_and_historical_audit_in_progress', '/root/iii_graph',
        'Complete1078-line fresh proof frozen08:13:52, root wholly read including final changes. Both full190/414-line sources and all89/68 combined output lines read. Exactly two mathematical executions, each first-run success. Original individually released08:20:46.096207. Root read whole161-line statement,302-line proof and all following auxiliary lines19264–19286. Whole-original comparison and exact historical audit scope remain in progress; no admission yet.'),
    '02LQ': ('clean_statement_fresh_local_and_global_derivation_in_progress', '/root/iii_02kr',
        'Actual holomorphic toric root, inverse, period conjugacies and component reflection are derived. Fresh prism/central-lift derivation resolves the candidate f=0 mixed-torus coefficient; the complete normalization chain and unbounded global inverse Smith maps are being written. No LQ mathematical program has run at the checkpoint87 boundary. Original and historical target remain closed; unfinished work receives no closure or smaller-gate credit.'),
    '02LS': ('fresh_vertical_proof_and_os45_full_bar_readback_pending', '/root/iii_02ks',
        'Fresh local affine-Cartan and global height proofs are saved. New381-line raw OS45 bar program has one successful execution,16 full23-by59 matrices and all reversible Smith maps. Its88-line long stdout and saved fullJSON still require whole reading. The final all-parameter fresh derivation and literal odd-star component-ordering comparison remain open. Original and historical targets stay closed.'),
    '02LU': ('clean_statement_and_named_dependency_fresh_derivation_in_progress', '/root',
        'Root read whole clean56-line LU statement and extracted only the named LT dependency112-line statement21006–21117, with no LT/LU proof or historical exposure. The additive h=1 mapping-cone quotient and inverse are being derived freshly. No LT admission is inferred: LT has no required-progress row. Literal odd-star degree ordering and complete marked boundary maps remain to be settled before fresh completion.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review61: ' + explanation

closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
assert '02LK' in new
assert set(new) <= {'02LK', '02LJ', '02LN', '02LQ', '02LS', '02LU', '02LG'}
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
## Review 61 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review60, {len(new)} required identities have closed: {', '.join(new)}.
Paper III has {len(closed)}/128 complete and {len(open_rows)} open.
Every admitted row resolves to its exact events; no previously closed
identity has reopened. K9 remains a restored preexisting identity and
earns no new-row movement credit. Consecutive no-movement count is zero.
No smaller-main-gate credit is claimed for unfinished proofs, receivers,
original releases, source retrieval, record preparation or packaging.

LK was admitted at08:05:55.936627 UTC after whole original, auxiliary,
962-line receiver and record reading. Root read the complete Laurent
and Tor programs, all actual streams, the exact historical replay and
the75-case validator. The mathematics stands. Its29 recorded defects
repair presentation; fourteen printed manual numbers have exact
bijective permanent-identity maps to automatic equation numbering.
The narrow LK admission helper retains exact guards and all existing
mathematical, identity, chronology and event checks.

LJ's frozen fresh derivation and original are wholly read. Root has
also read its complete staged receiver, historical source and output,
new validator and every actual stream. The final receiver-only changes
move the alternative whole-circle argument to checking notes and put
the computational paragraph inside the proof. Its seven model
corrections are the exact physical wall/normal-weight computations.
The required table, rather than existence of a receiver, determines
its admission status below.

LN's complete fresh proof was frozen08:13:52 and individually released
08:20:46.096207. Root read the whole original and all following
auxiliaries after that release. Its historical audit and comparison
are in progress. LQ, LS and LU continue fresh local/global proofs with
their originals closed. LU's only newly exposed dependency text is
the112-line clean LT theorem; its proof and historical program remain
closed and no LT required-row admission is invented. LG remains closed.

### Every open III required identity

| Tag | Statement | Packet/check state | Original-proof state |
|---|---|---|---|
{open_table}

Released comparisons still open: {', '.join(pending) or 'none'}.
All {units['III']} III unit criteria, all66 IV required checks and
all {units['IV']} IV unit criteria retain their open rows.
The canonical III source remains unchanged at SHA256 {source_sha}.
The main gate is all III required checks before source/bibliography
integration, the full unit pass, provenance, clean build and every
rendered page. IV follows III. I,II,V remain closed until the joint step.
The II E.5.2/E.5.3 inputs remain unchanged.

Checkpoint87 saved122/128 at08:19:50.567237 UTC. Its actual delivery
preceded the later LN release; work after that snapshot remains in the
live continuation and will enter the next scheduled checkpoint.

Closed required identities at Review61: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T09:34:24+00:00.
Next checkpoint88: 2026-11-25T09:04:24+00:00.
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
    assert '\n## Review 61 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review61: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
