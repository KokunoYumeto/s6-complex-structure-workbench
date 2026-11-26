from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_06_'
fragment=folder/(prefix+'replacement.tex')
before=SOURCE.read_text();after=before
start=r'\subsection{Translation fields and component surfaces}\label{subsec:II:component-field-inputs}'
end=r'\begin{proposition}[A component cover with a rank-two translation frame has coherent Euler characteristic zero]\hypertarget{tag-01D0}{}\label{cdp:st:C.2.UN.22}'
assert after.count(start)==after.count(end)==1
left,right=after.index(start),after.index(end)
after=after[:left]+fragment.read_text()+after[right:]
_,remote=read_tsv(folder/(prefix+'remote_repairs.tsv'))
for row in remote:
    assert after.count(row['old_text'])==1,row['statement_id']
    after=after.replace(row['old_text'],row['new_text'],1)
    print('Applied remote',row['statement_id'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
oldunit='subsec:II:component-field-inputs'
oldrows=[x for x in rows if x['paper']=='II' and x['unit_id']==oldunit]
assert len(oldrows)==26
rows=[x for x in rows if not(x['paper']=='II' and x['unit_id']==oldunit)]
for old in oldrows:
    current=dict(old)
    current.update(unit_id='subsec:II:rank-two-component-frames',unit_title='Rank-two frames and finite quotients',
      date_utc=now(),evidence=str(fragment.relative_to(ROOT)),
      detail='Remaining unreviewed material starts at UN.22. Its inherited open rows remain open. This boundary migration has no movement credit.')
    rows.append(current)
_,incoming=read_tsv(folder/(prefix+'unit_status.tsv'))
assert len(incoming)==130
for item in incoming:
    criterion=item.get('criterion',item.get('row'));status=item['status'];detail=item.get('reason',item.get('basis',''))
    if criterion in ['D14','structure']:
        status='open';detail+=' Final whole-paper placement remains open.'
    assert not any(x['paper']=='II' and x['unit_id']==item['unit'] and (x['defect_type'] or x['row_kind'])==criterion for x in rows)
    rows.append(dict(paper='II',unit_id=item['unit'],unit_title=item.get('title',item['unit']),
      row_kind='structure' if criterion=='structure' else 'defect',defect_type='' if criterion=='structure' else criterion,
      status=status,date_utc=now(),evidence=str(fragment.relative_to(ROOT)),
      detail=detail+' Exposed complete original/receiving agent reading; no independent credit or subdivision movement credit.'))
write_tsv(path,fields,rows)
add_event('lem:II:cyclic-component-cover; def:II:semicomplete-fields; lem:II:semicomplete-transport; lem:II:zero-dimensional-field-surface; lem:II:algebraic-leaf-fibration; cdp:st:C.2.UN.15; cdp:st:C.2.UN.16; cdp:st:C.2.UN.17; cdp:st:C.2.UN.19; cdp:st:C.2.UN.20; lem:II:torus-tube-numerical',
 'II-C3-ROOT-COMPONENT-FIELDS-ADMISSION','used and rechecked in this run',
 'Root read the entire detailed owner/source comparison, all five complete shared owners P238–P240/P301/P302, and the full old/receiving remote P281 proof. Checked the normalized-root map and cyclic stabilizer, finite-field coefficient extension, nonruled quotient comparison, exact source-defined semicompleteness and closedness scopes, component-ideal tangency, common minimal-model derivation, algebraic-leaf incidence and first-integral maps, and the irreducible mS substitution into the canonical generator. Imported 12 exposed complete old/new agent proof readings for the full five-unit package. The complete signed-divisor/null-block/flat-character argument remains in UN17; all42 equation comparisons and original label/target multiplicities are preserved. Root does not claim an additional full reading of every line of the large receiving fragment. D14/structure, inherited source completion and final rendering remain open. UN22 onward remains an open unit. No independent or final PDF credit.',
 'S6_SERIES_PUBLISH_II.tex: component covers, translation fields and canonical support',source='code/S6_SERIES_PUBLISH_c3_component_fields_admit.py')
print('Admitted five component-field units and bounded P281 application; later rank-two unit remains open.')
