"""Read the complete example unit and consolidate the duplicated equality remark."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text()
a=s.index(r'\subsection{Explicit checks on the hypotheses}')
b=s.index(r'\subsection',a+20)
old=s[a:b];new=old.replace(r'\subsection{Explicit checks on the hypotheses}',
 r'\subsection{Projective torus fibrations and Hopf bundles}\label{subsec:II:torus-and-hopf-examples}',1)
new=new.replace('point blowup preserves the fundamental group.',
 r'''each point-blowup map $\pi_Z:S'\to S$ induces an isomorphism
on fundamental groups by \cref{lem:II:blowup-topology}, applied
to that smooth surface and its point centre $Z$ of codimension two.''',1)
new=new.replace(r'''No fibre has
a finite unramified torus cover. The covering obstruction gives a counterexample to the smooth-support equality description of \SeriesRef{cdp:st:C.2.G.1} when its torus-fibre hypothesis is omitted. The numerical normal-crossings sign theorem \ref{night:P4.7} applies to this fibration.''',r'''Every fibre has fundamental group $\Z$ and therefore has no
finite unramified torus cover. Thus the torus-fibre hypothesis
in the smooth-support equality description of
\cref{cdp:st:C.2.G.1} is necessary even under $b_1=b_2=0$.
The numerical normal-crossings sign theorem
\cref{night:P4.7} applies to this fibration.''',1)
assert new!=old
apply_edit(old,new,'II-C3-TORUS-HOPF-EXAMPLES',['D03','D08','D12','D14'],
 'night:P4.10;night:P4.11','Complete projective/Hopf example subsection',
 'Replace the process heading by the two geometric constructions. Keep every Weierstrass, conifold blowup, fibre-Euler, fundamental-group and quotient calculation. Apply the earlier blowup fundamental-group owner to the identical smooth surface/point maps. State the Hopf covering obstruction with its computed fundamental group; its proof retains the exact finite-cover injection and rank contradiction.',
 'Root read the complete original and receiving unit. Its numerical and covering hypotheses and all maps are preserved.')

s=SOURCE.read_text()
a=s.index(r'\subsection{Identity monodromy and the irreducible equality case}')
b=s.index(r'\part{Periods, tangent cohomology and deformations}',a)
old49=s[a:b]
assert old49.count(r'\begin{remark}')==1 and old49.count(r'\end{remark}')==1
anchor=r'\label{stmt:P4.58}'
alias=r'''
\hypertarget{tag-02Y1}{}\label{night:P4.9}\label{stmt:P4.9}
\StatementRecord{night:P4.9}{proved}{02Y1}{\cref{night:P4.58}}
'''
after=s.replace(old49,'',1).replace(anchor,anchor+alias,1)
after=after.replace(r'{\SeriesRef{night:P4.10}, \SeriesRef{night:P4.11}, \SeriesRef{night:P4.26}',
                     r'{\SeriesRef{night:P4.26}',1)
front=r'\item \SeriesRef{night:P4.9}\quad Euler values of irreducible fibre supports.'+'\n'
assert after.count(front)==1
after=after.replace(front,'',1)
preserve_identifiers(s,after)
SOURCE.write_text(after,newline='\n')
rows=[]
for j,kind in enumerate(['D01','D04','D05','D08','D11','D12','D13','D14','D24'],1):
 rows.append(dict(change_id=f'II-C3-IRREDUCIBLE-EQUALITY-ALIAS-{j:02}',type=kind,
  statement_id='night:P4.9;night:P4.58',old_location='Duplicate irreducible equality remark and following process paragraph',
  old_page='current continuation source; final concordance pending',new_location='P4.58 common statement and complete proof',
  new_page='integrated build pending',old_text=old49+front,new_text=alias,
  reason='P49 repeats the identical irreducible-support restriction of P458 for the same f and full supports and adds no proof. Transfer its labels, permanent tag and hidden record to that owner; remove its duplicate front-list line and empty subsection. Delete the following production-history paragraph, whose mathematical support domain is already explicit in P458 and the standing definition. P458 proof uses no P410/P411 construction, so remove those two hidden dependency entries. No mathematical conclusion or hypothesis is changed.',
  review_status='Root read the complete original P49/orphan paragraph and complete current P458 statement and proof. The alias is exactly the identity specialization to the same irreducible supports; all tags and labels are preserved.'))
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id')
add_event('night:P4.9;night:P4.58','II-C3-ROOT-IRREDUCIBLE-EQUALITY-ALIAS',
 'used and rechecked in this run',
 'Root read all of P49 and its following process paragraph and the full P458 statement/proof. P49 gives exactly P458 on the same irreducible supports of the same f:Y to B. Its labels/tag/hidden record are now aliases at P458, and no result is restated or proved again. The removed paragraph records production history and an already stated support-domain restriction. P458 hypotheses and proof are unchanged. Unit-row removal records migration only, not a newly completed proof or progress credit.',
 'P49 complete old unit and P458 receiving owner',source=__file__)
add_event('night:P4.10;night:P4.11','II-C3-ROOT-TORUS-HOPF-EXAMPLE-UNIT',
 'used and rechecked in this run',
 'Complete original and receiving example unit read: twelve nodal Weierstrass fibres, diagonal-ideal small-resolution charts, irreducible NC supports, Euler24, two section embeddings killing torus factors, nonzero projective class, free proper C-action and its unit-norm S3xS3 slice, exp(-2pi) Hopf fibres, and the finite-index injection contradiction are all preserved. Shared point-blowup pi1 invariance is applied on the exact surface maps. Bibliography and final rendering remain open; no independent check claimed.',
 'Projective torus fibrations and Hopf bundles complete subsection',source=__file__)

for number in range(1,26):
 kind=f'D{number:02}'
 if kind in ['D10','D16']:continue
 set_unit_status('night:P4.10',kind,'open' if kind in ['D14','D18','D23'] else 'done',
  'Complete old and receiving subsection read. All local instances logged; exact construction maps and original numerical conclusions retained. Whole-paper placement, BHPV source verification and final typography remain open.',
  'CHECK_EVENTS.tsv: II-C3-ROOT-TORUS-HOPF-EXAMPLE-UNIT')
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
oldrows=[r for r in rows if r['paper']=='II' and r['unit_id']=='night:P4.9']
assert len(oldrows)==26,len(oldrows)
rows=[r for r in rows if r not in oldrows]
write_tsv(path,fields,rows)
print('Complete example unit closed locally; P49 unit migrated to identical P458 owner without movement credit.')
