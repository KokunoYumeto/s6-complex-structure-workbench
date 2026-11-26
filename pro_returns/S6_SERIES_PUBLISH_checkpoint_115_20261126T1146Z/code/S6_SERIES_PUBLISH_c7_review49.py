#!/usr/bin/env python3
"""Record the scheduled first hourly review of continuation seven."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 24, 20, 34, 24, tzinfo=timezone.utc)
assert now >= due
ledger = (root / 'PROGRESS_LEDGER.md').read_text()
assert '\n## Review 49 — ' not in ledger
baseline = re.search(r'Closed required identities at Review48: ([^\n]+)\.', ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 92

def table(name):
    with (root / name).open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))

rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {r['event_id']: r for r in table('CHECK_EVENTS.tsv')}
closed = [r for r in rows if r['status'] == 'done']
tags = {r['tag'] for r in closed}
new = sorted(tags - previous)
assert len(rows) == 128 and not previous - tags
for row in closed:
    for eid in (s.strip() for s in row['check_event_id'].split(';')):
        if eid:
            assert eid in events and events[eid]['statement_id'] == row['label']
open_tags = sorted(r['tag'] for r in rows if r['status'] != 'done')
pending = sorted(r['tag'] for r in rows if r['status'] != 'done'
                 and r['proof_status'] == 'released_after_derivation')
states = Counter(r['proof_status'] for r in rows if r['status'] != 'done')
units = Counter(r['paper'] for r in table('S6_SERIES_PUBLISH_unit_progress.tsv')
                if r['status'] == 'open')
assert units['III'] == 784 and units['IV'] == 756
source_sha = hashlib.sha256((root / 'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert source_sha == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
counts = re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.', ledger)
assert counts
no_movement = 0 if new else int(counts[-1]) + 1
note = f'''
## Review 49 — {now.isoformat()}

INCOMPLETE. This is the hourly review scheduled for {due.isoformat()}.
Since the latest received review, Review48, {len(new)} required identities
have closed: {', '.join(new) or 'none'}. Paper III now has {len(closed)}/128
complete and {128-len(closed)} open. Every recorded closure event resolves
to its exact statement; no admitted required identity has reopened.

The KR closure includes the whole-original comparison, every auxiliary
assertion, the complete receiving proof, new integral arithmetic and its
read output, primary-source scopes, exact replacement guards and permanent
identities. This completed required check supplies qualifying movement.

The KS divisor-cube countercheck is accepted at its full geometric scope:
the embedded cusp divisor has integral cube six, and the proposed D.V3
target has zero cube on every integral degree-two class. D27 records the
resulting defect type. Its 55 new III/IV unit criteria and the later joint
applications to I, II and V remain open. The fresh complete KS refinement
passed root review, including the direct construction on the KS star,
the full parameter homology, the primitive cubic and the flag-manifold
identification. Its original was individually released at
2026-11-24T20:29:31.562852+00:00; whole-original comparison and receiver
admission remain pending. Fresh completion and release earn no closure.

For S8/S9, the corrected global handle class has an explicit integral dual
cycle and capped square -8k. The incoming-boundary restriction is 2m,
and the compression-cap meridian contributes with the independently
derived orientation. The delta twist and negative-numerator maps extend
over the specified caps and local models. Both full receivers are now
written, and their whole-original comparisons and root review are under
way. The two earlier failed substitutions in each original remain
disclosed. Neither required identity is admitted at this review.

Fresh original-filled catalogue calculations for KV/KW are in progress;
their originals remain embargoed. The pinned public repository's bounded
KU response inputs have been retrieved and their Git object identities
checked. Retrieval supplies no computation, proof or required-check credit.

All open III identities: {', '.join(open_tags)}.
Proof-state counts: {dict(states)}. Released comparisons still open:
{', '.join(pending) or 'none'}. The required progress table retains each
row's exact state, inputs and evidence locators.

All 784 III unit criteria, 66 IV required checks and 756 IV unit criteria
remain open. The other unit counts in the current table are {dict(units)}.
III's canonical source remains at SHA256 {source_sha}.
Required checks precede the complete unit pass, staged repairs, provenance,
clean build and reading every rendered page. IV follows III. I, II and V
retain their closed gates until the five-together step; the two specified
Paper II inputs E.5.2 and E.5.3 remain unchanged. Joint final gates remain
open. The delivered checkpoint71 records its own earlier snapshot.

Closed required identities at Review49: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Review50 is due2026-11-24T21:34:24+00:00. Checkpoint72 is due
2026-11-24T21:04:24+00:00. This review refreshes no inventory or census and
creates no manifest, seal, receipt or derived-file copy.
'''
for name in ('PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md'):
    path = root / name
    prior = path.read_text()
    assert '\n## Review 49 — ' not in prior
    path.write_text(prior + note, newline='\n')
print(f'Review49: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}')
print('Newly completed: ' + ', '.join(new))
print('Released comparisons open: ' + ', '.join(pending))
print('Recorded UTC: ' + now.isoformat())
