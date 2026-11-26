"""Place proved comb bounds/duality before the preserved final question."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_provenance/splitting'
_,guards=read_tsv(folder/'S6_SERIES_PUBLISH_splitting_guards.tsv')
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old_text'])==1,row['change_id']
    after=after.replace(row['old_text'],row['new_text'],1)
anchor=r'\begin{definition}[Cup-product kernel of a positive comb]\hypertarget{tag-P278}{}\label{def:II:comb-cup-kernel}'
head=r'\subsection{Comb cup kernels and Hodge numbers}\label{subsec:II:comb-cup-hodge}'
assert after.count(anchor)==1
after=after.replace(anchor,head+'\n\n'+anchor,1)
_,programs=read_tsv(folder.parent/'S6_SERIES_PUBLISH_c3_provenance_program_edits159.tsv')
for row in programs:
    assert after.count(row['old_text'])==1,row['change_id']
    after=after.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/('S6_SERIES_PUBLISH_splitting_'+suffix))
    if suffix=='CHECK_EVENTS.tsv':
        for row in rows:
            if 'effort' not in row['who']:row['who']+='; effort setting not separately exposed'
    print(suffix,append_rows(ROOT/target,rows,key))
print('Program159',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',programs,'change_id'))
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[dict(
    change_id='II-C3-ROOT-COMB-SUBSECTION-BOUNDARY',type='D14',
    statement_id='def:II:comb-cup-kernel;inv:E2.2;inv:E2.4;inv:E2.5',
    old_location='Single comb section',old_page='integrated concordance pending',
    new_location='Comb cup kernels and Hodge numbers; degree bounds and duality; vector fields and twelve-tooth smoothings',
    new_page='integrated build pending',old_text=anchor,new_text=head+'\n\n'+anchor,
    reason='The inserted proved owners create actual subsections. Give the preceding unchanged kernel/Hodge block its descriptive subsection as well. The E2.4/E2.5 block is unchanged apart from its supplied heading.',
    review_status='All prior mathematical bodies remain unchanged; inherited completed local reviews follow the exact receiving ranges. Subdivision earns no movement credit.')],'change_id')

fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
prior_comb=[r for r in progress if r['paper']=='II' and r['unit_id']=='sec:II:combs']
assert len(prior_comb)==26
retained=[r for r in progress if not(r['paper']=='II' and r['unit_id'] in ['sec:II:combs','app:II:programs'])]
for unit,title in [('sec:II:combs','Comb cup kernels and Hodge numbers'),('subsec:II:twelve-tooth-smoothings','Vector fields and twelve-tooth smoothings')]:
    for old in prior_comb:
        row=dict(old);row.update(unit_id=unit,unit_title=title,date_utc=now(),
            evidence='CHECK_EVENTS.tsv: II-C3-ROOT-SPLITTING-ADMISSION',
            detail=old['detail']+' The exact unchanged block has its own subsection; inherited local review, no migration movement credit.')
        retained.append(row)
_,statuses=read_tsv(folder/'S6_SERIES_PUBLISH_splitting_unit_status.tsv')
titles={'app:II:programs':'The remaining splitting problem','subsec:II:comb-kernel-bounds-duality':'Degree bounds and cup duality'}
for row in statuses:
    kind=row['defect_type'];unit=row['unit']
    status='open' if kind in ['D14','D23'] else 'done'
    detail=row['outcome']
    if kind in ['D15','D24']:detail='No instance in this mathematical unit; the separate front-matter units retain their own criteria.'
    retained.append(dict(zip(fields,['II',unit,titles[unit],'defect',kind,status,now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-SPLITTING-ADMISSION',detail])))
for unit,title in titles.items():
    retained.append(dict(zip(fields,['II',unit,title,'structure','', 'open',now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-SPLITTING-ADMISSION',
        'Proved owners now precede their applications and the final part contains its unchanged remaining question. Whole-paper placement review remains open; subdivision is not movement credit.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in retained]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,retained)
add_event('prop:II:comb-kernel-bounds;prop:II:comb-cup-duality;inv:E2.3',
    'II-C3-ROOT-SPLITTING-ADMISSION','used and rechecked in this run',
    'Root and the assigned reviewer read the complete original 174-line final section and every receiving proved/final paragraph; the reviewer also read all complete E15/P278/E2.2/E2.4/E2.5 inputs. P320 carries the exact root-character/coarse matrix maps, source degree−2, target O(2m), degree identity, four Hom-section contributions, all Hodge/tangent values and both pencil kernels with their inverse local maps. P321 retains the same Cech sign and matrix row(b,−a,d,−c), inverse wedge map, unsaturated cokernel and finite-stabilizer invariants. Its data are exactly those of the earlier cup definitions. Only the same unresolved splitting question remains in the final part; no new geometric occurrence of the two abstract pencils is asserted. All old targets survive. The complete two pinned program sources were read by the assigned reviewer, with paths/hashes verified; addition159 puts their relevant computations in the Programs table. No program was executed and no independent or final-page credit is added.',
    'Comb bounds/duality owners and final splitting problem; Programs addition159',source=__file__)
print('P320/P321 and program159 admitted; final question preserved; unit ranges reconciled.')
