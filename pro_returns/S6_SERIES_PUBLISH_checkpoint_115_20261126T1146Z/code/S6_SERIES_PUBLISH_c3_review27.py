"""Scheduled review27, using a stable original-unit movement witness."""
from S6_SERIES_PUBLISH_c3_edit import *
from datetime import datetime, timezone
import io
import zipfile

due=datetime.fromisoformat('2026-11-22T20:56:58+00:00')
assert datetime.now(timezone.utc)>=due
assert '## Progress review 27 —' not in (ROOT/'PROGRESS_LEDGER.md').read_text()
_,rows=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
with zipfile.ZipFile(ROOT.parent.parent/'S6_SERIES_PUBLISH_checkpoint_40.zip') as z:
    names=[n for n in z.namelist() if n.endswith('/S6_SERIES_PUBLISH_unit_progress.tsv')]
    assert len(names)==1
    old=list(csv.DictReader(io.StringIO(z.read(names[0]).decode()),delimiter='\t'))
key=lambda r:(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind'])
oldmap={key(r):r for r in old}
excluded=['D10','D14','D16','D18','D23','D24']
witnesses=[r for r in rows if r['paper']=='II' and r['unit_id']=='night:P4.53'
    and r['row_kind']=='defect' and r['defect_type'] not in excluded
    and oldmap[key(r)]['status']=='open' and r['status']=='done']
assert len(witnesses)==19
assert all(r['date_utc']>'2026-11-22T20:42:00+00:00' for r in witnesses)
counts=Counter((r['paper'],r['status']) for r in rows)
status_lines='\n'.join(f'- Paper {paper}: {sum(v for (p,s),v in counts.items() if p==paper and s!="done")} unit-defect/structure rows remain other than done; {counts[(paper,"done")]} are recorded done.' for paper in ['II','III','IV'])
stamp=now()
addition=f'''

## Progress review 27 — {stamp}

Scheduled for 2026-11-22T20:56:58+00:00. Movement is present.
The stable original unit night:P4.53 closed 19 previously open
local defect rows, verified against the checkpoint40 ledger.
The witness excludes inherited D10/D16, placement D14,
bibliography D18, final rendered typography D23, front-matter
concordance D24, structure, new subdivisions and alias migrations.
Its complete original/receiving comparison is recorded at
II-C3-ROOT-CUBIC-DOUBLE-UNIT-ADMISSION. The D22 application row
was reopened when a root-level map was insufficiently named,
then closed at II-C3-ROOT-ELLIPTIC-CONTRACTION-ADMISSION: the
weighted transport now acts on g_u with initial alpha P and
c=alpha, and its level embeds in the identical full fibre.
P451 already proves the general unit flow; P452 explicitly
invokes it and was unchanged. No theorem was refuted by this
application clarification.

The quartic and elliptic-contraction comparisons are admitted.
A517 now states its existing isolated-germ vanishing-sphere
argument before its full-root torus application. P322 owns the
weighted transport, variation bounds and exact free/nonfree
scalar-character comparison. The complete degree6/7/9 elliptic
contraction proof retains its formal-function, fixed-parameter,
vertex and numerical arguments. P222's same local normalization
and conductor multiplication maps now state the semilocal unit
criterion used in the cubic proof.

The Hopf boundary, resolution-index, fibre-group, component-genus
and rational-toric units are admitted. P327 owns the general
central primary covering and the exact algebraic pullback of
meromorphic-function fields, with applications at UN38/UN43/P325.
UN64/P325/P326/UN65 are admitted with their full original scopes,
normal extensions, residue maps, group attachments and compact
constructions. P326 was moved unchanged before all its consumers;
UN46/UN57 still await the assigned replacement of their duplicate
collar arguments. The UN64–68 block will follow its compact period
construction inputs. The BHPV P410 locator now uses the complete
theorem/table on pp243–244 with the same Hodge/minimal-model maps.

The latest integrated working PDF has 801 pages and 5,311,002
bytes. Three pdfLaTeX passes, with shell escape disabled, are
clear of undefined references/citations, missing glyphs/fonts,
duplicate labels/destinations and rerun requests. Its two overfull
boxes have maximum1.7175pt, with none above2pt. The transferred
Euler alias was repaired and both labels now resolve to the same
equation number. Final rendered-page credit remains zero.

The current unit ledger gives every open criterion and its evidence:
{status_lines}
These counts describe current units and are not movement counts.
The main gate remains completion of PaperII text, global structure,
first-part/provenance/count comparisons, final build and every page.
The remaining local R19/P456/P457/R20 units and the complete
occurrence/marked-cycle/contraction/sign sections are being read
and compared. P320/P321 and the preserved final splitting problem
are prepared for receiving admission. PaperIII's128 and PaperIV's66
required checks, their refined consumers and all text/build/page
gates remain open. The final I–V consistency/deposit step remains
open. I and V retain their closed gates and neither source has
been reopened or rebuilt.

Neither protected E.5.2/E.5.3 statement changed. The refined
02Y6/02XE exhaustive consumer pass in II remains admitted.
Consecutive hourly reviews without movement:0. Next review:
2026-11-22T21:56:58+00:00 (28). Next checkpoint:
2026-11-22T21:26:58+00:00 (41). This review adds no independent
proof, final-page or packaging movement credit.
'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (ROOT/name).open('a',newline='\n') as f:f.write(addition)
print(f'Review27 {stamp}:19 stable original-unit closures; no-stall counter0.')
