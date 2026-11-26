#!/usr/bin/env python3
"""Exact source proposals after candidate02 third-quarter image reading."""
from pathlib import Path
import csv
import hashlib
import io

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'S6_SERIES_PUBLISH_III.tex'
OUT=ROOT/'agents/continuation9_reading_thirdquarter'
source=SOURCE.read_text()
items=[
('D20','maps:src:D.2.37','353',
 r'the free group \(H_1(V)=\mathbb Z\gamma\oplus\mathbb Z^{N-1}\)',
 r'the free abelian group \(H_1(V)=\mathbb Z\gamma\oplus\mathbb Z^{N-1}\)',
 'The displayed H_1 target is the direct sum with commuting addition. The identity on its gamma and base-coordinate generators preserves the injective boundary-column map and its division-on-image inverse. Adding abelian states that existing group law precisely; no assertion or matrix changes.'),
('D23','maps:src:D.2.37','355–356',
 r'\emph{The free rank of the full boundary cokernel.}',
 '\\Needspace{5\\baselineskip}\n\\emph{The free rank of the full boundary cokernel.}',
 'Actual candidate02 image355 leaves this italic heading alone at the foot; its first paragraph begins356. Reserve five baselines before this exact heading so it stays with following argument. Text and mathematical formulas are unchanged.'),
('D23','mapsIII:def:odd-weighted-data','358–359',
 r'\subsection{Shared odd factors and saturated cap kernels}',
 '\\Needspace{9\\baselineskip}\n\\subsection{Shared odd factors and saturated cap kernels}',
 'Actual image358 has the subsection13.3 title and Definition13.8 header/tagQ138 at the foot, while the entire definition body begins359. Reserve nine baselines before this block; the heading, definition and all permanent identifiers remain intact. Rebuilt image review must confirm the keep-together result.'),
('D20','maps:src:D.2.40','375',
 'For every remaining cap, duality and the cap bases above give the free group',
 'For every remaining cap, duality and the cap bases above give the free abelian group',
 'The following equality is H_2(U_j,partial U_j)=H^4(U_j), with its component-disc integral basis and rank stated immediately below. Both sides have their homology/cohomology addition, and the identity on the stated basis preserves every boundary column. The added adjective makes the existing commuting group structure explicit.'),
('D02','maps:src:D.2.40','375',
 'The ray/character map, inverse, and the Bézout\nreconstruction of the angular generator are proved\nthere. None of these angular entries is suppressed.\n\nThe full degree-three images of the remaining caps\nare exactly the full unchanged-cap columns, by their complete Wang kernels.',
 'The ray/character map, inverse, and the Bézout\nreconstruction of the angular generator are proved\nthere.\n\nThe full degree-three images of the remaining caps\nare exactly the full unchanged-cap columns, by their complete Wang kernels.',
 'The preceding display states every cusp boundary column x_*+j c_22 delta and the immediately preceding sentence identifies the ray/character map, inverse and Bezout reconstruction. The deleted sentence is defensive reassurance about omission and adds no map, entry, hypothesis or inference. Every actual angular coordinate remains in the formula and subsequent Smith construction.'),
('D20','maps:src:D.2.41','385',
 r'and the free group $\ker\Gamma$ adds no torsion.',
 r'and the free abelian group $\ker\Gamma$ adds no torsion.',
 'The preceding construction identifies ker Gamma with a projected integer lattice and constructs the additive splitting H_2(X)=C direct-sum ker Gamma by component-disc coordinates. The identity on that integer basis is an isomorphism of additive groups and preserves the section and inverse coefficient reading. Adding abelian states the existing commuting law; no mathematical assertion or boundary map changes.'),
('D23','mapsIII:rem:all-weight-integral-calculation','385–386',
 r'\begin{remark}[Integral computation and the odd-factor comparison]',
 '\\Needspace{5\\baselineskip}\n\\begin{remark}[Integral computation and the odd-factor comparison]',
 'Actual image385 ends with the Remark14.3/tagQ141 heading alone, and its entire body begins386. Reserve five baselines before the unchanged remark environment so the heading stays with its first paragraph. All statements, permanent identifiers and formulas remain intact; rebuilt image review must confirm the result.'),
('D08','maps:src:D.2.46','394',
 r'with the index change \(r=N-1\), whose inverse is \(N=r+1\).',
 r'with the index change \(r=N-1\).',
 'The two scalar formulas express the same count: r independent base loops correspond to N=r+1 total boundary sites. Substitution in either direction gives the identity on this integer index set. The removed words only rearrange that index convention; the ordered peripheral maps c_i and J_i, the bar-polygon inverse, the Smith inverse rows and every genuine geometric inverse remain verbatim. This is the observed P11 redundant reverse-renaming prose, typed D08.'),
]
fields=next(csv.reader(io.StringIO((ROOT/'S6_SERIES_PUBLISH_defects_III.tsv').read_text()),delimiter='\t'))
rows=[]
candidate=source
for i,(kind,sid,pages,old,new,reason) in enumerate(items,1):
    assert source.count(old)==1,(i,source.count(old))
    assert candidate.count(old)==1,(i,'candidate old',candidate.count(old))
    candidate=candidate.replace(old,new,1)
    rows.append(dict(change_id=f'CLAUDE-III-C9-PDF-THIRD-{i:03d}',type=kind,statement_id=sid,
                     old_location='Exact source fragment after actual image reading',old_page='candidate02 physical'+pages,
                     new_location='same statement/definition, identifiers and maps',new_page='pending final rebuild',
                     old_text=old,new_text=new,reason=reason,
                     review_status='Actual page images read; exact source context checked. Root admission and rebuilt image review pending.'))
for i,(_,_,_,old,new,_) in enumerate(items,1):
    assert candidate.count(new)==1,(i,'candidate new',candidate.count(new))
inverse=candidate
for _,_,_,old,new,_ in reversed(items):
    assert inverse.count(new)==1
    inverse=inverse.replace(new,old,1)
assert inverse==source
OUT.mkdir(parents=True,exist_ok=True)
p=OUT/'S6_SERIES_PUBLISH_c9_thirdquarter_defects.tsv'
with p.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Source SHA256:',hashlib.sha256(source.encode()).hexdigest())
print('Exact unique fragments:',len(rows))
print('All eight old fragments unique in current source; all eight new fragments unique after exact application; full reverse recovery passed.')
print('Row005 expanded old count:',source.count(items[4][3]),'; expanded new count before:',source.count(items[4][4]),'; after:',candidate.count(items[4][4]))
for r in rows:print(r['change_id'],r['type'],r['statement_id'],r['old_page'])
print('Page368 candidate withdrawn after source check: fibre matrix is mathsf K_d, graph kernel is italic K_d; no row staged.')
print('Output:',p.relative_to(ROOT))
print('No canonical source, defect, event or derived file changed.')
