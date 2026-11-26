"""Record the scheduled second hourly review of this continuation."""
from pathlib import Path
from datetime import datetime,timezone
import csv
import io
import zipfile
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc)
due=datetime(2026,11,23,12,47,46,tzinfo=timezone.utc)
assert stamp>=due,'The scheduled review is not due.'
csv.field_size_limit(100000000)
with zipfile.ZipFile(ROOT.parents[1]/'upload/S6_SERIES_PUBLISH_continue_cp44.zip') as archive:
    names=[n for n in archive.namelist() if n.endswith('S6_SERIES_PUBLISH_checkpoint_44/S6_SERIES_PUBLISH_unit_progress.tsv')]
    assert len(names)==1
    initial=list(csv.DictReader(io.StringIO(archive.read(names[0]).decode()),delimiter='\t'))
with (ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv').open() as f:
    current=list(csv.DictReader(f,delimiter='\t'))
key=lambda r:(r['paper'],r['unit_id'],r['row_kind'],r['defect_type'])
index={key(r):r for r in current}
closed=[r for r in initial if r['paper']=='II' and r['status']=='open' and index[key(r)]['status']=='done']
assert len(closed)>=729
open_ii=[r for r in current if r['paper']=='II' and r['status']=='open']
counts=Counter(r['defect_type'] or r['row_kind'] for r in open_ii)
new_since_review30=len(closed)-101
assert new_since_review30>0
note=f'''\n## Review 31 — {stamp.isoformat()}

INCOMPLETE. The scheduled 12:47:46 UTC review records qualifying movement:
{len(closed)} existing checkpoint-44 open Paper II unit rows are now done,
{new_since_review30} more than the corrected 101 at review 30. New receiving-unit
rows and packaging receive no movement credit. Every open unit remains
individually recorded with its status, evidence and detail in
S6_SERIES_PUBLISH_unit_progress.tsv. There are {len(open_ii)} still-open II unit
criteria: {dict(sorted(counts.items()))}.

The complete 787-page fixed candidate was actually viewed. Its 36 guarded
repairs and seven exposed full-proof/reference comparisons are admitted.
The rebuilt 787-page candidate passes the pdfLaTeX typesetting gate: one
0.89041pt overfull box, none above 2pt, and no missing font/glyph, undefined
reference/citation, duplicate label/destination, rerun request or unresolved
fallback. Exact image comparison retains 650 earlier clear readings; the
137 changed images have their actual current clear/open rows in the v2 page
logs. Newly found proof-square and reference-wording defects remain open for
the next bounded repair and rebuilt-image reading. Compilation, hashing and
rendering supply no visual-reading or mathematical proof credit.

The source and deposit counts now agree at 3,389 exact event associations in
2,802 evidence groups. The source-record merge retains all prior bibliography
fields and adds 15 missing shared entries, 125 II-scoped annotations and 17
already performed source readings; it creates no new check event. The 51
provenance rows await their final reconciliation and the derived-record finish.
The source-stage plan for the remaining 48 non-D23 rows is prepared; it gives
no closure credit before admission. D23 rows await the complete final image
pass and disposition of every observed issue.

The main question remains the five publication-ready papers. The strongest
current gate is the bounded II visual remainder, final source/record/provenance
reconciliation, and then completion of III, IV and the joint step in that order.
All 198 II required-check dispositions are retained. III's 128 and IV's 66
required checks and their unit criteria remain pending and individually
recorded; neither paper has begun. I and V retain their gates and stay unopened
until the joint step. The protected E.5.2/E.5.3 statements retain exact bytes;
the III/IV uses of refined 02Y6/02XE remain an explicit later check.

Consecutive reviews without qualifying movement: 0. Review 32 is due
2026-11-23T13:47:46+00:00. Checkpoint 47 is due
2026-11-23T13:02:46+00:00. No inventory, seal, manifest or derived-file copy
is produced for this review.
'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    path=ROOT/name
    old=path.read_text()
    assert '\n## Review 31 — ' not in old
    path.write_text(old+note,newline='\n')
print('Review 31 recorded:',len(closed),'baseline closures;',new_since_review30,'since review30; no-movement count0.')
