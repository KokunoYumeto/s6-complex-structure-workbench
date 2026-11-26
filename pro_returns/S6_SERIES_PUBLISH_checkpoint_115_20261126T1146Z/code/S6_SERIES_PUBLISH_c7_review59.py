"""Eleventh hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 6, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 59 — ' not in ledger
baseline = re.search(r'Closed required identities at Review58: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 117


def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


fields, rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02LF': ('released_comparison_and_receiver_in_progress', '/root/iii_graph',
        'Fresh1408-line derivation and all new code/streams have been wholly read by root; the bounded peer was frozen before its original exposure. Original released06:20:11 UTC. Root and receiver checker have read its whole statement,198-line proof and17-line following auxiliary. The receiver checker has wholly read the retrieved historical sources and saved AH data; the cited historical output files remain unavailable. Exact rotating-cusp and support-transport repairs are in progress. The earlier root spill was following computational auxiliary, not the proof body; it remains target-derived exposure and earns no independent fresh credit.'),
    '02LI': ('released_original_comparison_pending', '/root',
        'Fresh1262-line derivation, both608-line programs, both actual combined execution streams and all1601 saved-data lines have been wholly read by root. Original released06:26:55 UTC. Root has read the whole released statement; the original199-line proof and its following auxiliary still await whole reading. A fresh-only bounded peer review is being finalized.'),
    '02LK': ('fresh_frozen_root_code_review_in_progress', '/root/iii_02kr',
        'Fresh858-line general-lattice proof is frozen and has now been wholly read by root, together with its source-scope and calculation-readout notes. Root is reading the321-line lattice program and172-line saved-data validator before all actual execution streams and release. All139 saved cases were computationally validated by the fresh checker; no manual reading of every serialized entry is claimed. Original remains closed except the separately recorded single root sentence exposure, which earns no independent fresh credit.'),
    '02LM': ('released_whole_receiver_and_records_review_pending', '/root/iii_02ks',
        'Original and following auxiliary have been wholly read. The fresh677-line proof and its review remain frozen. After exposure, the Tor_2 scope of Zhubr2013 required the original five-copy bridge for b=20; this repair is used and rechecked, without fresh-check credit. The receiver checker has read the three historical sources and assembled a stable998-line one-proof receiver. Its full comparison, new202-line auxiliary execution and final records await root reading and admission.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review59: ' + explanation

closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
assert new == ['02LH']
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
open_table = '\n'.join('| ' + ' | '.join((r['tag'], r['label'], r['packet_status'], r['proof_status'])) + ' |'
                       for r in sorted(open_rows, key=lambda r: r['tag']))
note = f'''
## Review 59 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review58, {len(new)} required identity has closed: {', '.join(new)}.
Paper III has {len(closed)}/128 complete and {len(open_rows)} open.
Every admitted row resolves to its exact events; no previously closed
identity has reopened. K9 remains a restored preexisting identity and
earns no new-row movement credit. Consecutive no-movement count is now
{no_movement}. No smaller-main-gate credit is claimed for an unfinished
derivation, original release, receiver or packaging work.

LH was admitted at05:55:46 UTC after the whole original, every auxiliary,
the1680-line receiver, all new sources and execution streams, comparison,
guards and proposed records were read. Its full odd-weight cap maps,
nonprimitive rims, torsion, covers and transfers stand with the exact
inclusion/retraction between459 all-star-original and495 broad families.
The D26 scope repair changes no stated homology formula.

LF and LI have complete frozen fresh proofs and new calculations, wholly
read by root before their releases at06:20:11 and06:26:55 UTC. LF's whole
original/auxiliary reading is complete, and its receiving comparison is
in progress. LI's original proof remains to be read. LK's whole858-line
fresh proof has now been read by root; its code/stream reading is in
progress and its original remains closed. Root's precise LF auxiliary
and LK sentence exposures stay recorded without independent fresh credit.
LM's original comparison found the necessary Tor_2 framing scope repair:
the five-copy bridge for b=20 is preserved as post-exposure used-and-
rechecked work. Its998-line receiver and final records await root reading.
None of these four unfinished rows is admitted by this review.

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

Checkpoint84 saved118/128 at06:05:14 UTC; the later LF/LI releases and
LK freeze have their own subsequent scopes. No checkpoint is made here.

Closed required identities at Review59: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T07:34:24+00:00.
Next checkpoint85: 2026-11-25T06:49:24+00:00.
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
    assert '\n## Review 59 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review59: {len(closed)}/128 done; {len(new)} new closure; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
