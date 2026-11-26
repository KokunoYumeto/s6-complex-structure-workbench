"""Fourteenth hourly review of continuation seven; no inventory refresh."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
DUE = datetime(2026, 11, 25, 9, 34, 24, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= DUE
ledger = (ROOT / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 62 — ' not in ledger
baseline = re.search(r'Closed required identities at Review61: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 122


def table(name):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter='\t')
        return reader.fieldnames, list(reader)


fields, rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')[1]}
updates = {
    '02LQ': ('released_receiver_wholly_read_comparison_records_pending', '/root/iii_02kr',
        'Fresh736-line derivation frozen08:47:03.397764; original released08:54:58.364200. Root wholly read original396-line proof and all following auxiliaries,297-line post derivation, historical210-line source and exact called helper bodies, retrieval sources and streams, exact replay, and independent post-exposure checks for12 markings,95 local and1638 global cases. Root wholly read724-line receiver; a one-based table-index clarification produces725 lines and awaits exact final diff reading. Narrow D25 geometric-orientation correction uses an explicitly involutive conductor-chain map; all theorem conclusions are retained in the transported marking. Final records and basis-transition readback remain pending.'),
    '02LS': ('complete_frozen_fresh_proof_root_review_and_release_pending', '/root/iii_02ks',
        'Complete1216-line fresh proof frozen09:29:21, SHA ee6cbed56c156a8f590c0f7926121a9a3baf5ba4fdbccf9302d56a7df126ef7d. Root wholly read preceding1183 lines plus every final hunk, all assembly/edit sources and actual streams. All600 lossless readback lines are read; the two explicit inverses reconstruct the594-line first readback and all88 original stdout lines and16 complete JSON objects exactly. The signed criterion, degree, marked period maps, full23-by59 OS45 relations, all cap maps, relative-disc inverse and fundamental group are proved. Original and historical target remain closed at this review.'),
    '02LU': ('released_original_comparison_and_new_residue_audit_in_progress', '/root/iii_graph',
        'Complete698-line fresh proof frozen09:19:58;135-line graph peer review and root review read. Original individually released09:21:18.362497; root wholly read56-line statement,92-line proof and following auxiliary21444–21455. Fresh h=1 mapping-cone quotient has literal sections, bounding chains and full boundary columns. New45-residue computation is complete in the comparison lane; root reading and historical audit remain pending. Historical main209 and audit61 lines read by agent only. Its literal d=0 implementation guard is being kept separate from the explicitly marked uncorrected-cap construction.'),
    '02LG': ('clean_statement_fresh_synthesis_pending', '/root',
        'Root reread whole82-line clean statement and exact corrected LM table. Original and historical target remain closed. Fresh synthesis must incorporate the admitted LJ six oriented types, LM corrected residual models, LN weighted cases, and completed LQ/LS/LU results. The nonrequired LT/LV unit proofs remain open; no completion is inferred from nearby homology checks.'),
}
for row in rows:
    if row['tag'] in updates and row['status'] == 'open':
        state, who, explanation = updates[row['tag']]
        row['packet_status'] = state
        row['assigned_checker'] = who
        row['notes'] += ' Review62: ' + explanation

closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
assert {'02LJ', '02LN'} <= set(new)
assert set(new) <= {'02LJ', '02LN', '02LQ', '02LS', '02LU', '02LG'}
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
## Review 62 — {now.isoformat()}

INCOMPLETE. Scheduled boundary: {DUE.isoformat()}.
Since Review61, {len(new)} required identities have closed: {', '.join(new)}.
Paper III has {len(closed)}/128 complete and {len(open_rows)} open.
Every admitted row resolves to its exact events; no previously closed
identity has reopened. K9 remains a restored preexisting identity and
earns no new-row movement credit. Consecutive no-movement count is zero.
No smaller-main-gate credit is claimed for unfinished proofs, receivers,
original releases, source retrieval, record preparation or packaging.

LJ was admitted at08:51:05.219879 UTC after whole original, auxiliary,
1476-line receiver and comparison-record reading. Its14 weighted
patterns give six oriented types. Seven original model assignments
were corrected by the explicit wall and normal-weight calculations.
Alternative proofs remain in checking notes.

LN was admitted at09:08:51.122973 UTC after whole original, auxiliary,
1191-line receiver and record reading. Root read both historical
sources, the exact additional-variant validation, every actual failure
and success stream and all retained records. Its scalar-exclusion
reason was corrected at the precise intermediate-assertion scope:
index16 alone is shared by an admitted natural I1 scalar case; the
actual scalar map preserves the positive-I1 support. The theorem's
homology and monodromy computations are retained.

LQ's complete original, auxiliaries and724-line receiver are wholly
read. Its one-based indexing clarification and final comparison
records remain pending. Root also read its exact historical replay
and independent12/95/1638-case post-exposure checks. The recorded
geometric orientation error is repaired by an explicit involution
with its inverse; theorem conclusions survive the transported marking.

LS's full fresh proof is frozen09:29:21. The root has accounted for
all1216 final lines through whole1183-line reading and four complete
changed hunks. Every executed assembly/edit source and actual stream
is read. Both lossless-reader inverse maps and every600-line final
readback entry are read. Its original remains closed at this review.

LU's complete fresh proof and peer review preceded its individual
release09:21:18.362497. Root read the whole original and its following
auxiliary. Its full original comparison and audit are in progress.
LG remains at clean-statement fresh synthesis. LT/LV are open unit
obligations; no nonexistent required-progress rows are created.

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

Checkpoint88 saved123/128 at09:04:25.116297 UTC, before LN admission.
Work after that snapshot remains in the live continuation and enters
the next scheduled checkpoint.

Closed required identities at Review62: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Next review: 2026-11-25T10:34:24+00:00.
Next checkpoint89: 2026-11-25T09:49:24+00:00.
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
    assert '\n## Review 62 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review62: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
