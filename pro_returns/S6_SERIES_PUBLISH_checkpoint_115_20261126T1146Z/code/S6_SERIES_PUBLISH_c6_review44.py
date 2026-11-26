#!/usr/bin/env python3
"""Second hourly review of continuation six, against the Review43 closed set."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert now >= datetime(2026,11,24,13,15,57,tzinfo=timezone.utc)
ledger = (ROOT/'PROGRESS_LEDGER.md').read_text()
baseline = re.search(r'Closed required identities at Review43: ([^\n]+)\.',ledger)
assert baseline
previous = set(baseline[1].split(', '))
assert len(previous) == 76


def table(name):
    with (ROOT/name).open(newline='') as stream:
        return list(csv.DictReader(stream,delimiter='\t'))


rows = table('S6_SERIES_PUBLISH_required_progress_III.tsv')
events = {row['event_id']:row for row in table('CHECK_EVENTS.tsv')}
closed = [row for row in rows if row['status'] == 'done']
tags = {row['tag'] for row in closed}
new = sorted(tags-previous)
reopened = sorted(previous-tags)
assert len(rows) == 128 and not reopened
for row in closed:
    eids = [value.strip() for value in row['check_event_id'].split(';') if value.strip()]
    assert eids
    for eid in eids:
        assert eid in events and events[eid]['statement_id'] == row['label']
pending = sorted(row['tag'] for row in rows if row['status'] != 'done'
                 and row['proof_status'] == 'released_after_derivation')
open_tags = sorted(row['tag'] for row in rows if row['status'] != 'done')
open_proofs = Counter(row['proof_status'] for row in rows if row['status'] != 'done')
units = Counter(row['paper'] for row in table('S6_SERIES_PUBLISH_unit_progress.tsv')
                if row['status'] == 'open')
sha = hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_III.tex').read_bytes()).hexdigest()
assert sha == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
previous_count = re.findall(r'Consecutive reviews without qualifying movement: (\d+)\.',ledger)
assert previous_count and int(previous_count[-1]) == 0
no_movement = 0 if new else int(previous_count[-1])+1
note = f'''
## Review 44 — {now.isoformat()}

INCOMPLETE. The scheduled 13:15:57 UTC review records {len(new)} required
III rows newly done since Review43: {', '.join(new) or 'none'}.
The current total is {len(closed)}/128 complete and {128-len(closed)} open.
No identity reopened. All event identifiers, including each event in
the multiple-event S2/S4/S5 rows, resolve to that row's exact statement.

The admitted comparisons in this interval include the OS49 finite
quotients and their integral homology; the compact pullback and translated
line bundles, with their exact divisor correction on a common resolution;
the actual framed-torus nullbordism and its smash powers; the direct smooth
classification through the circle quotient and its local replacement;
and the exact conical postcomposition, including a detected nonzero kernel
and both moving-four-sphere initial maps. Each closure has its written
pre-release derivation, full original and receiving comparison, exact
replacement guards, defect rows and admitted event. Source application and
page review have received no credit from these proof admissions.

All still-open III identities: {', '.join(open_tags)}.
Their proof-state counts are {dict(open_proofs)}. Individually released
comparisons still open: {', '.join(pending) or 'none'}.
Every individual status and unresolved input remains in
S6_SERIES_PUBLISH_required_progress_III.tsv; IV's 66 required checks remain
in S6_SERIES_PUBLISH_required_progress_IV.tsv. The next fresh work includes
the actual OS49 parameter and page maps, the framed-fibre coefficient,
the OS56/II geometric and filling maps, and the 172 natural-component
fundamental-group rows. Intermediate derivations and arithmetic have not
been counted as completed checks.

Every unit-row status remains in S6_SERIES_PUBLISH_unit_progress.tsv.
Open unit counts: {dict(units)}. All 756 III and 729 IV unit criteria
remain open. III's source has not been edited and retains SHA256 {sha}.
The main question remains all five publication-ready papers. Its current
gate is completion of the {128-len(closed)} remaining III checks, followed
by all III unit restructuring and defects, provenance and links, clean
standalone pdfLaTeX build, typesetting checks and every rendered-page
reading. IV follows in the same order, then the five papers together.
All uncompleted III/IV provenance, build and final-page rows remain open;
no new final candidate PDF has been certified.

I and V retain their published closed gates until the joint step. II
remains final, with E.5.2/E.5.3 unchanged. Every III/IV downstream use of
refined II02Y6/02XE requires its prescribed scope check. Joint D26 and later
defect applications, cross-references, notation, deposit fields, records
tables, page concordances and final first-part readings remain open.

Closed required identities at Review44: {', '.join(sorted(tags))}.

Consecutive reviews without qualifying movement: {no_movement}.
Review45 is due 2026-11-24T14:15:57+00:00. Checkpoint64 was delivered at
its scheduled boundary; checkpoint65 is due 2026-11-24T13:30:57+00:00.
Packaging is no movement. This review creates no inventory, census,
manifest, seal or derived-file copy.
'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    path = ROOT/name
    current = path.read_text()
    assert '\n## Review 44 — ' not in current
    path.write_text(current+note,newline='\n')
print(f'Review44: {len(closed)}/128 done; {len(new)} new closures; no-movement count {no_movement}.')
print('Newly completed:',', '.join(new))
print('Open released comparisons:',', '.join(pending))
