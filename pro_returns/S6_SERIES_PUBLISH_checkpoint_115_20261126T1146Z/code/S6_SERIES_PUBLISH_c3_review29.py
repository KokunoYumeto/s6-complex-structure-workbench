"""Scheduled review29, using only stable pre-existing unit-row movements."""
from S6_SERIES_PUBLISH_c3_edit import *
import io,zipfile

assert now()>='2026-11-22T22:56:58+00:00'
assert '## Progress review 29 —' not in (ROOT/'PROGRESS_LEDGER.md').read_text()
_,rows=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
with zipfile.ZipFile(ROOT.parent.parent/'S6_SERIES_PUBLISH_checkpoint_42.zip') as z:
 names=[n for n in z.namelist() if n.endswith('/S6_SERIES_PUBLISH_unit_progress.tsv')];assert len(names)==1
 old=list(csv.DictReader(io.StringIO(z.read(names[0]).decode()),delimiter='\t'))
key=lambda r:(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind'])
oldmap={key(r):r for r in old}
expected={'the-series-and-this-paper':18,'known-and-new':19,'sec:II:09':18,'sec:II:all:12':18}
for unit,count in expected.items():
 witness=[r for r in rows if r['paper']=='II' and r['unit_id']==unit and key(r) in oldmap
  and oldmap[key(r)]['status']=='open' and r['status']=='done'
  and r['date_utc']>'2026-11-22T21:58:48+00:00']
 assert len(witness)==count,(unit,len(witness))
restored=[r for r in rows if r['paper']=='II' and r['unit_id']=='sec:II:07']
assert len(restored)==26
assert all(r['status']=='open' for r in restored if r['defect_type'] not in ['D10','D16'])
counts=Counter((r['paper'],r['status']) for r in rows)
totals='\n'.join(f'- Paper{p}: {sum(v for (q,t),v in counts.items() if q==p and t!="done")} unit-defect/structure rows remain other than done; {counts[(p,"done")]} recorded done.' for p in ['II','III','IV'])
build=(ROOT/'code/S6_SERIES_PUBLISH_c3_build_latest.out').read_text()
assert all(f'pdfLaTeX pass {i}: exit 0' in build for i in range(1,4))
assert 'undefined references/citations: 0' in build
assert 'rendered unresolved-reference fallback pages: 0' in build
pdf=re.search(r'\((\d+) pages, (\d+) bytes\)',build);assert pdf
stamp=now()
entry=f'''

## Progress review 29 — {stamp}

Scheduled for 2026-11-22T22:56:58+00:00. Movement is present:
73 stable pre-existing local defect rows changed from open to done.
The same paper/unit/criterion keys in checkpoint42 and the current
ledger give 18 rows for the series introduction, 19 for Known and new,
18 for the original section09 remainder, and 18 for the final Euler
theorem. These changes all follow review 28. Inherited D10/D16,
new subdivisions, aliases, placements and packaging receive no credit.

The complete reduced-horizontal tail was found missing from the unit
ledger: neither its actual subsection nor the original section07
remainder identity represented it. Earlier admissions had covered
preceding units and bounded consumers, not its complete 4575-line tail.
The original section07 identity is restored with 26 rows: D10/D16 stay
done and 24 rows remain open. Its full proof comparison is in progress.
This restoration is disclosed as a coverage correction, not movement.

Admitted since the previous review are the root/descent comparisons,
compact negative-curve example, elliptic lift and occurrence chain,
normal-crossing elliptic alignment and rational torsion-normal
obstruction, and the complete reduced-star consolidation. The latter
corrected the false intermediate claim that the central degree-zero
line is always non-torsion: the allowed product-torus example has a
trivial line. The construction requires degree zero and all original
star conclusions are preserved. The first-part exact period conventions,
primary locators and seven-part organization are integrated. Its figure
now identifies the actual P263 premise of C4f. The final Euler proof
has a complete old/new root comparison; its INT1–3 receiver row stays open.

The current working build has{pdf[1]} pages and{pdf[2]} bytes. Three
pdfLaTeX passes with shell escape disabled have no unresolved reference,
citation, missing font/glyph, duplicate label/destination or rerun request;
one overflow remains below 1pt. The rendered UNRESOLVED fallback scan
also reports zero. Root actually read working page 18 before and after
the direct-reference and figure-line corrections. Final-page credit is zero.

Current row totals, descriptive rather than movement counts:
{totals}

The original sections 07, 10 and 11 remainders stay open. The marked weighted
cycle, common elliptic-model and horizontal-boundary packages are being
read in full and are not admitted by this review. Paper II's global
structure, provenance, final build and every final page remain open;
Paper III's128 and Paper IV’s 66 required checks and their text/build/page
gates follow. The joint I–V step is pending. I and V have not been reopened
or rebuilt. E.5.2/E.5.3 remain unchanged. The refined 02Y6/02XE consumer
pass in II is admitted; the III/IV passes await those papers.

Consecutive hourly reviews without movement: 0. Next review:
2026-11-22T23:56:58+00:00 (30). Checkpoint 43 is due with this review;
the following checkpoint 44 is due 2026-11-22T23:41:58+00:00.
'''
for filename in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (ROOT/filename).open('a',newline='\n') as f:f.write(entry)
print('Review29 recorded:73 stable original-unit closures; original sec07 remainder restored and open; no-stall counter0.')
