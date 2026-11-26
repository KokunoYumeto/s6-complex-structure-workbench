"""Admit the complete compared intrinsic rank-one elliptic-field proof."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_08_'
fragment=folder/(prefix+'replacement.tex')
old=(folder/(prefix+'input.tex')).read_text();new=fragment.read_text()
before=SOURCE.read_text();assert before.count(old)==1
after=before.replace(old,new,1)
preserve_identifiers(before,after)
for oldids,newids in zip(identifiers(before),identifiers(after)):
    for name,count in oldids.items():assert newids[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,items=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,items,key))

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
unit='subsec:II:rank-one-elliptic-fields'
oldrows=[x for x in rows if x['paper']=='II' and x['unit_id']==unit]
assert len(oldrows)==26
rows=[x for x in rows if not(x['paper']=='II' and x['unit_id']==unit)]
for oldrow in oldrows:
    current=dict(oldrow)
    current.update(unit_id='subsec:II:component-core-genus',unit_title='Compact component cores and geometric genus',
      status='done' if oldrow['defect_type'] in ['D10','D16'] else 'open',
      date_utc=now(),evidence=str(fragment.relative_to(ROOT)),
      detail='Following unreviewed material begins at UN.28. D10/D16 remain done; all other inherited classes and structure remain open. Boundary migration earns no movement credit.')
    rows.append(current)
_,incoming=read_tsv(folder/(prefix+'unit_status.tsv'))
assert len(incoming)==26
for item in incoming:
    kind=item['criterion'];status=item['status'];detail=item['reason']
    if kind in ['D14','D18','D23','structure']:status='open'
    rows.append(dict(paper='II',unit_id=item['unit'],unit_title=item['title'],
      row_kind='structure' if kind=='structure' else 'defect',defect_type='' if kind=='structure' else kind,
      status=status,date_utc=now(),evidence=str(fragment.relative_to(ROOT)),
      detail=detail+' Root also read the complete old and receiving proof and comparison. No independent or subdivision movement credit.'))
write_tsv(path,fields,rows)
add_event('cdp:st:C.2.UN.26','II-C3-ROOT-RANK-ONE-ADMISSION','used and rechecked in this run',
 'The guarded source matches the complete original fragment. Root read the entire original and receiving UN.26 statements and proofs and the full comparison. The same relative canonical pushforward, Riemann--Roch section, contraction sign, coordinate gluing, dense elliptic-fibre translations and full holomorphic-locus closedness argument remain. The quotient ratio gives the same Stein factor; the induced base action is explicitly descended using q_*O_X=O_B and inverted by g^-1 before taking B/G. The two generators retain the same eigencharacter and all five labelled display payloads. The conductor agent reopened the primary author preprint at Guillot Theorem3.3 and its complete proof, p.9. D14/D18/D23 and final structure remain open; UN.28 onward remains unreviewed. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: Rank-one fields on elliptic surfaces',
 source='agents/continuation3_conductor/S6_SERIES_PUBLISH_c3_conductor_08_comparison.md')
print('Admitted the rank-one elliptic-field unit; component-core and final-placement work remains open.')
