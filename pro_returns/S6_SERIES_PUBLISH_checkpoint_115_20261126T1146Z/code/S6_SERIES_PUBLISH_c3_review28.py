"""Scheduled review 28 with a stable pre-existing unit-row witness."""
from S6_SERIES_PUBLISH_c3_edit import *
import io
import zipfile

assert now() >= '2026-11-22T21:56:58+00:00'
assert '## Progress review 28 —' not in (ROOT/'PROGRESS_LEDGER.md').read_text()
_, rows = read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
with zipfile.ZipFile(ROOT.parent.parent/'S6_SERIES_PUBLISH_checkpoint_40.zip') as archive:
    names = [n for n in archive.namelist() if n.endswith('/S6_SERIES_PUBLISH_unit_progress.tsv')]
    assert len(names) == 1
    old = list(csv.DictReader(io.StringIO(archive.read(names[0]).decode()), delimiter='\t'))
key = lambda r: (r['paper'], r['unit_id'], r['defect_type'] or r['row_kind'])
oldmap = {key(r): r for r in old}
excluded = {'D10', 'D14', 'D16', 'D18', 'D23', 'D24'}
witnesses = [r for r in rows if r['paper']=='II' and r['unit_id']=='night:P4.57'
    and r['row_kind']=='defect' and r['defect_type'] not in excluded
    and oldmap[key(r)]['status']=='open' and r['status']=='done'
    and r['date_utc']>'2026-11-22T20:57:29+00:00']
assert len(witnesses)==19, [(r['defect_type'],r['date_utc']) for r in witnesses]
counts = Counter((r['paper'],r['status']) for r in rows)
lines = '\n'.join(f'- Paper {p}: {sum(v for (q,s),v in counts.items() if q==p and s!="done")} unit-defect/structure rows remain other than done; {counts[(p,"done")]} recorded done.' for p in ['II','III','IV'])
stamp = now()
entry = f'''

## Progress review 28 — {stamp}

Scheduled for 2026-11-22T21:56:58+00:00. Movement is present.
The stable original unit night:P4.57 has closed 19 previously open
local defect rows since review 27. Each has the same paper, unit and
criterion key in checkpoint 40 and the current ledger. The witness
excludes inherited D10/D16, global placement D14, bibliography D18,
rendered typography D23, front-matter D24 and structure. New subdivisions,
renamings, aliases, packaging and this review receive no movement credit.

The complete Hopf-boundary comparison is admitted: P338 supplies the
degree-two ruled-boundary residue obstruction; P325 retains the reduced
two-axis conclusion and treats the effective multiple-axis divisor with
explicit normal forms. UN64 and UN82 invoke those exact maps. P347 owns
the finite product cover used by the elliptic root constructions. The
single Enriques-family proof retains the r=2 statement and equation
aliases by explicit specialization, and the entire Kummer occurrence
proof has been compared. These admissions record full old/new agent or
root readings without independent-reproof credit. The canonical-flat and
marked-cycle packages are prepared; their pending admissions are not
counted as completed work here. UN34/35/37, the weighted constructions,
and the general normalized-root and coarsening data remain in progress.

The latest verified integrated working build precedes those latest
admissions. It has 807 pages and 5,352,461 bytes; three pdfLaTeX passes
with shell escape disabled produced no undefined references/citations,
missing glyphs/fonts, duplicate labels/destinations or rerun requests.
Two overfull boxes remain, maximum 1.7175pt, none above 2pt. A rebuild
after the pending admissions remains due. Final rendered-page credit is
still zero.

Current row totals (descriptive, not movement counts):
{lines}

The main gate remains Paper II's complete text, global structure,
provenance, final build and every rendered page. Paper III's 128 and
Paper IV's 66 required checks and their text/build/page gates remain
open. The joint I–V step remains open. The I and V closed gates are
preserved; neither paper has been reopened or rebuilt. Protected
E.5.2/E.5.3 statements have not changed. The refined 02Y6/02XE consumer
review in II remains admitted; III/IV consumers await those papers.

Consecutive hourly reviews without movement: 0. Next review:
2026-11-22T22:56:58+00:00 (29). Next checkpoint:
2026-11-22T22:11:58+00:00 (42). Checkpoint 41 was saved and verified.
'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (ROOT/name).open('a',newline='\n') as handle:
        handle.write(entry)
print(f'Review 28 {stamp}: 19 stable original-unit closures; no-stall counter 0.')
