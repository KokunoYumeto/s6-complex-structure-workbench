"""Admit all five compared marked-cycle guards and their program-table rows."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_15_'
provenance=ROOT/'agents/continuation3_provenance'
before=SOURCE.read_text(); after=before
original=(folder/(prefix+'input.tex')).read_text()
receiving=(folder/(prefix+'replacement.tex')).read_text()
assert after.count(original)==1
after=after.replace(original,receiving,1)
_,guards=read_tsv(folder/(prefix+'remote_repairs.tsv'))
assert len(guards)==4
for row in guards:
    assert after.count(row['old_text'])==1,row['statement_id']
    after=after.replace(row['old_text'],row['new_text'],1)
marker='\\end{longtable}}\n\n\\begin{thebibliography}'
program_fragment=(provenance/'S6_SERIES_PUBLISH_c3_provenance_program_rows162.tex').read_text()
assert after.count(marker)==1
after=after.replace(marker,program_fragment+marker,1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    for row in rows:
        if suffix=='CHECK_EVENTS.tsv' and 'effort' not in row['who']:
            row['who']+='; effort setting not separately exposed'
    print(suffix,append_rows(ROOT/target,rows,key))
_,programs=read_tsv(provenance/'S6_SERIES_PUBLISH_c3_provenance_program_edits162.tsv')
assert len(programs)==1
programs[0].update(old_text=marker,new_text=program_fragment+marker)
print('Program defect rows',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',programs,'change_id'))
fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
_,statuses=read_tsv(folder/(prefix+'unit_status.tsv'))
remainder='subsec:II:star-weighted-constructions'
incoming={r['unit'] for r in statuses if r['unit']!=remainder}
progress=[r for r in progress if not(r['paper']=='II' and r['unit_id'] in incoming)]
for row in progress:
    if row['paper']=='II' and row['unit_id']=='sec:II:10':
        row.update(unit_title='Star, weighted and tree constructions',date_utc=now(),
            evidence='CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR15-ADMISSION',
            detail='The original section10 identity retains its open criteria on the actual following star/weighted/tree remainder. Its cycle material has moved to compared receiving subsections; that subdivision earns no movement credit. D10/D16 stay done.')
for row in statuses:
    if row['unit']==remainder:continue
    kind='structure' if row['criterion']=='restructuring' else row['criterion']
    status='open' if kind in ['D14','D23','D24','structure'] else row['status']
    progress.append(dict(zip(fields,['II',row['unit'],row['title'],
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,status,now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR15-ADMISSION',
        row['reason']+' Root read all complete receiving owners, criterion, suspension and examples; conductor read all complete originals and replacements. Final global placement remains open. Original section10 remainder stays open.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
_,sources=read_tsv(folder/(prefix+'primary_sources.tsv'))
incoming=[dict(source=r['source_id']+' (third-continuation marked cycles)',url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
    use='The exact nonresonant Hopf curve list and elliptic line factors enter P329/UN48; section translation extends on the specified smooth projective relatively minimal elliptic model. Exposed source reading only.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))
add_event('lem:II:normal-product-collars;def:II:marked-normal-cycle;lem:II:moving-marked-cycle;lem:II:logarithmic-period-family;cdp:st:C.2.UN.57;cdp:st:C.2.UN.48;ex:II:three-hopf-cycle',
    'II-C3-ROOT-CONDUCTOR15-ADMISSION','used and rechecked in this run',
    'Conductor read all five complete original blocks and every complete receiving statement/proof. Root read complete P326/P329/P333/P331, the full merged criterion, UN48 and P332 and the full comparison. The collar extension constructs the actual labelled Cartier branches from the normalization maps; its original SNC conclusion is preserved. The moving owner constructs Hopf and ruled frames separately, proves Hausdorff proper connected plumbing with compact cores, and identifies the entire punctured family by logarithmic maps and inverses. One criterion retains all four original theorem tags and their full union of conclusions, including the exact normal-period sign and conjugate filling. UN48 retains the complete elliptic-suspension realization and P332 the full examples and finite divisors. All 57 equation transfers and every original label/target preserve exact multiplicity. P329/P333 D12 awaits the separate UN41 receiving admission. Program162 paths and complete pinned-source reading are documented by provenance; root read the complete receiving table and its exact scope records. No mathematical-program execution, independent proof, required-check increment, final-page or subdivision movement credit.',
    'Smooth collars; marked lattices and moving cycles; logarithmic periods; marked-cycle criterion; elliptic suspensions; explicit cycles; Programs',source=__file__)
print('Five marked-cycle guards and 13 program-table rows admitted atomically.')
