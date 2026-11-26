"""Twelfth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 7, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 60 — ' not in ledger
baseline = re.search(r'Closed required identities at Review59: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 118


def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


fields, rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02LJ': ('fresh_derivation_and_new_computation_in_progress', '/root/iii_02ks',
        'Fresh work remains behind the statement-only boundary. The checker reports a new488-line raw computation with208 output lines and a separate80-line action/coefficient check with528 literal refinement identities. The full written proof is still being completed and root has not read those new sources or streams. Original LJ proof, auxiliary history and historical programs remain closed. No admission or smaller-gate credit is claimed.'),
    '02LK': ('released_receiver_and_post_exposure_root_review_pending', '/root/iii_02kr',
        'The whole858-line frozen fresh proof, its fresh sources and actual streams were root-read before release06:36:44 UTC. Root has read the whole original statement and249-line proof. The stable962-line receiver and whole-original comparison are saved; post-exposure Laurent206-line and Tor196-line programs and their actual streams await root reading, as does the full receiver. Proposal records are in preparation. The separately recorded original-sentence root exposure retains its precise nonfresh scope.'),
    '02LN': ('clean_statement_fresh_derivation_in_progress', '/root/iii_graph',
        'A new clean statement-only intake at agents/continuation7_iii_ln_statement/S6_SERIES_PUBLISH_III_02LN_statement_only.tex contains exactly the161 canonical theorem lines18799–18959, SHA25647206aebd9e3f5727ae2bb43293febe92c9f500d3cafbc1e27935dc64332febe. Root read the whole clean intake. The old862-line packet and its argument-bearing addenda remain closed to the fresh checker, as do the original proof and historical programs. Fresh all-weight/all-repair local and global derivation is in progress using explicitly attributed dependencies; LI is admitted and LK remains pending.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review60: ' + explanation

closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
assert new == ['02LF', '02LI', '02LM']
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
## Review 60 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review59, {len(new)} required identities have closed: {', '.join(new)}.
Paper III has {len(closed)}/128 complete and {len(open_rows)} open.
Every admitted row resolves to its exact events; no previously closed
identity has reopened. K9 remains a restored preexisting identity and
earns no new-row movement credit. Consecutive no-movement count is zero.
No smaller-main-gate credit is claimed for unfinished proofs, receivers,
records, original releases, source retrieval or packaging.

LM was admitted at06:57:20.448962 UTC after complete source, original,
auxiliary,998-line receiver and record reading. Eight of eleven P/model
assignments change. The five-copy b20 framing bridge is preserved with
its actual post-exposure scope; the677-line fresh derivation is frozen.
LF was admitted at07:19:16.470822 UTC after whole original, auxiliary,
796-line receiver and all new source/stream/record reading. All eight
model conclusions stand. Three D25 repairs specify the actual rotating
cusp fixed set, Borel line relation and transported wall calculation.
LI was admitted at07:31:46.379889 UTC after its whole original, auxiliary,
498 mathematical receiver lines and exact printed-tag addition to499,
bounded receiver peer, all sources/streams and final records. All fifteen
integral formulas stand; the D26 count is495 for the broad family and459
for its all-star-original subset, with exact inclusion/replacement maps.

LF's redundant packet manifest
agents/continuation7_iii_three_primary_receiving/S6_SERIES_PUBLISH_III_02LF_packet_manifest_v001.json
was removed under prompt section0.5, which prohibits edit manifests.
The authoritative defects, CHECK_EVENTS, exact guards and every executed
source/output remain. The retained root correction source records the
removed file's prior hash and the separate final-event scope correction.

LK's whole original is read. Its962-line receiver, whole-original
comparison and post-exposure Laurent/Tor sources and streams still await
root completion; LK remains open. LJ's new raw computation and independent
action/coefficient route support its developing fresh proof, with no
original exposure. LN uses only the clean161-line canonical statement;
the old argument-bearing packet and original remain closed. Neither
unfinished fresh lane earns closure credit.

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

Checkpoint85 saved118/128 at06:54:30.575838 UTC. The three later admissions
have their separately recorded actual times. Checkpoint86 is due at this
review boundary; its exact snapshot and delivery are separately recorded.

Closed required identities at Review60: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T08:34:24+00:00.
Next checkpoint87 after the due86: 2026-11-25T08:19:24+00:00.
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
    assert '\n## Review 60 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review60: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
