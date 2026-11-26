"""Scheduled review with a verified stable-unit movement witness."""
from S6_SERIES_PUBLISH_c3_edit import *
from datetime import datetime, timezone
import io
import zipfile

due=datetime.fromisoformat('2026-11-22T19:56:58+00:00')
assert datetime.now(timezone.utc)>=due,'Hourly review is not yet due.'
assert '## Progress review 26 —' not in (ROOT/'PROGRESS_LEDGER.md').read_text()
_,rows=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
with zipfile.ZipFile(ROOT.parent.parent/'S6_SERIES_PUBLISH_checkpoint_38.zip') as z:
    names=[n for n in z.namelist() if n.endswith('/S6_SERIES_PUBLISH_unit_progress.tsv')];assert len(names)==1
    old=list(csv.DictReader(io.StringIO(z.read(names[0]).decode()),delimiter='\t'))
key=lambda r:(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind'])
oldmap={key(r):r for r in old}
witnesses=[r for r in rows if r['paper']=='II' and r['unit_id']=='night:P4.44'
    and r['row_kind']=='defect' and r['defect_type'] not in ['D10','D14','D16','D18','D23']
    and oldmap[key(r)]['status']=='open' and r['status']=='done']
assert len(witnesses)==20
assert all(r['date_utc']>'2026-11-22T19:12:04+00:00' for r in witnesses)
counts=Counter((r['paper'],r['status']) for r in rows)
stamp=now()
status_lines='\n'.join(f'- Paper {paper}: {sum(v for (p,s),v in counts.items() if p==paper and s!="done")} unit-defect/structure rows remain other than done; {counts[(paper,"done")]} are recorded done.' for paper in ['II','III','IV'])
addition=f'''

## Progress review 26 — {stamp}

Scheduled for 2026-11-22T19:56:58+00:00. Movement is present.
The stable original unit night:P4.44 closed exactly 20 previously open
local defect rows after its complete original/receiving reading. This is
verified against the checkpoint38 unit ledger, saved after review25.
The witness excludes inherited D10/D16, global placement D14, bibliography
D18, rendered typography D23, structure, new subdivisions and alias
migrations. CHECK_EVENTS event II-C3-ROOT-UNIFORM-TRANSVERSE-UNIT gives
the exact reading; its defects are recorded in the central defects table.
Other original units also moved, but no additional count is needed here.

All four full-fibre multiplicity proof premises opened at review25 are
resolved. R15 uses P298, R14 retains its complete weighted tacnode
deformation, P4.41 uses its full-function nodal Hessian construction,
and P4.45 now uses P280's exact cubic normalization and factor lifts.
The last proof preserves the unit and every positive factor power,
derives the exact weighted critical-value coordinate and Schur Hessian,
and composes inner and outer full-boundary transport. The separate UN9
full-scope premise is resolved by P299 and its root comparison. These
are completed proof repairs, with no hypothetical replacement and no
change to either protected E.5.2/E.5.3 statement. The historical 198
required Paper II checks remain resolved.

The full refined 02Y6/02XE consumer pass in II is admitted. Shared
conormal, ordinary-triple conductor and conductor-graph owners now have
explicit maps at the rational, elliptic, primary and two-component
applications. The positive ruled configuration has one proof with both
permanent identities. The elliptic identity-monodromy owner includes the
entire normalized root and invariant direct-image descent, and its two
complete consumers are admitted. The compact component/lattice proof,
analytic/Picard/LR work and exact bibliography-version additions remain
part of the current manuscript.

The latest integrated working build has 796 pages (5,245,324 bytes),
three successful pdfLaTeX passes with shell escape disabled, two
overfull boxes with maximum 1.7175 pt and none above 2 pt, and no
undefined reference/citation, missing glyph/font, duplicate
label/destination or rerun request. Final rendered-page credit is zero.
Text finalization, the final build gate and every final page remain open.

The current unit ledger records every open criterion and its evidence:
{status_lines}
These counts describe the current unit structure and are not movement
counts. The other open-row gates remain: II final structure, remaining
body units, all final provenance comparisons/counts and deposited links;
III's 128 and IV's 66 required checks; all III/IV refined consumers,
text/build/page gates; and the final five-together consistency/deposit
step. The complete P205 example, contracted-boundary unit and cyclic/K3
component units are under active complete-proof comparison. Main
theorem and remaining local-sector text follows. Papers I and V retain
their closed gates; neither manuscript has been reopened or rebuilt.

Consecutive hourly reviews without movement: 0. Next hourly review:
2026-11-22T20:56:58+00:00 (27). Checkpoint39 is due now at
2026-11-22T19:56:58+00:00; the next checkpoint is due at
2026-11-22T20:41:58+00:00 (40). No independent-proof, final-page or
packaging movement credit is added by this review.
'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (ROOT/name).open('a',newline='\n') as f:f.write(addition)
print(f'Review26 {stamp}: 20 stable original-unit closure witnesses; all four full-fibre proof premises resolved; no-stall counter0.')
