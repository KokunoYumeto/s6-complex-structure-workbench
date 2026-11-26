"""Admit the fully compared rank-two and cyclic quotient units."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_07_'
fragment=folder/(prefix+'replacement.tex')
old=(folder/(prefix+'input.tex')).read_text();new=fragment.read_text()
before=SOURCE.read_text();assert before.count(old)==1
after=before.replace(old,new,1)
_,remote=read_tsv(folder/(prefix+'remote_repairs.tsv'))
for row in remote:
    assert after.count(row['old_text'])==1,row['statement_id']
    after=after.replace(row['old_text'],row['new_text'],1)
    print('Applied remote',row['statement_id'])
preserve_identifiers(before,after)
for oldids,newids in zip(identifiers(before),identifiers(after)):
    for name,count in oldids.items():assert newids[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
oldunit='subsec:II:rank-two-component-frames'
oldrows=[x for x in rows if x['paper']=='II' and x['unit_id']==oldunit]
assert len(oldrows)==26
rows=[x for x in rows if not(x['paper']=='II' and x['unit_id']==oldunit)]
for oldrow in oldrows:
    current=dict(oldrow)
    current.update(unit_id='subsec:II:rank-one-elliptic-fields',unit_title='Rank-one fields on elliptic surfaces',
      status='done' if oldrow['defect_type'] in ['D10','D16'] else 'open',
      date_utc=now(),evidence=str(fragment.relative_to(ROOT)),
      detail='Remaining unreviewed material begins at UN.26. D10/D16 remain done; all other inherited unreviewed classes and structure remain open. Boundary migration earns no movement credit.')
    rows.append(current)
_,incoming=read_tsv(folder/(prefix+'unit_status.tsv'))
assert len(incoming)==52
for item in incoming:
    kind=item['criterion'];status=item['status'];detail=item['reason']
    if kind in ['D14','D18','D23','structure']:status='open'
    rows.append(dict(paper='II',unit_id=item['unit'],unit_title=item['title'],
      row_kind='structure' if kind=='structure' else 'defect',defect_type='' if kind=='structure' else kind,
      status=status,date_utc=now(),evidence=str(fragment.relative_to(ROOT)),
      detail=detail+' Complete exposed original/receiving agent comparison; no independent or subdivision movement credit.'))
write_tsv(path,fields,rows)
add_event('lem:II:elliptic-first-integral; cdp:st:C.2.UN.22; cdp:st:C.2.UN.23; rem:II:projective-torus-quotients; lem:II:algebraic-leaf-fibration; cdp:st:C.2.UN.15',
 'II-C3-ROOT-RANK-TWO-ADMISSION','used and rechecked in this run',
 'The current complete old fragment matches the exposed original exactly. Root read the entire detailed comparison, complete P303 and P304, the full terminal component-quotient application and both bounded remote wording changes; root does not claim an additional complete reading of the whole large fragment. The conductor agent fully read every old and final receiving proof and both complete remote blocks, as recorded in six exposed events. P303 preserves the elliptic first-integral proof and explicitly supplies the local section/Jacobian maps for the monodromy table, including the etale multiple-fibre root and canonical-degree minimality. UN.22 has one proof; the full analytic quotient, ramification, toric valuations and fundamental-group argument remain in UN.23. P304 identifies H with the derivative image G/G0. Every old label/target multiplicity and all21 labelled display payloads remain. D14/D18/D23/structure stay open and UN.26 onward stays unreviewed. The newly observed Yoshihara bibliography conflict is assigned for an exact primary-source correction. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: rank-two fields and cyclic torus quotients',source='agents/continuation3_conductor/S6_SERIES_PUBLISH_c3_conductor_07_comparison.md')
print('Admitted two reviewed units and two bounded wording guards; rank-one unit remains open.')
