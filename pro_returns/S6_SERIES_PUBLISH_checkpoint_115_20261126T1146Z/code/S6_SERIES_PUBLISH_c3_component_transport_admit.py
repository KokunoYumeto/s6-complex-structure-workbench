"""Admit the compact-cycle owner and its two fully compared consumers."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_09_'
before=SOURCE.read_text();after=before
for suffix in ['', 'UN36_']:
    old=(folder/(prefix+suffix+'input.tex')).read_text()
    new=(folder/(prefix+suffix+'replacement.tex')).read_text()
    assert after.count(old)==1,suffix
    after=after.replace(old,new,1)
preserve_identifiers(before,after)
for oldids,newids in zip(identifiers(before),identifiers(after)):
    for name,count in oldids.items():assert newids[name]==count,name
    for name,count in (newids-oldids).items():assert newids[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                         ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,items=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,items,key))

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
oldunit='subsec:II:component-core-genus'
oldrows=[x for x in rows if x['paper']=='II' and x['unit_id']==oldunit]
assert len(oldrows)==26
rows=[x for x in rows if not(x['paper']=='II' and x['unit_id']==oldunit)]
for unit,title in [('subsec:II:elliptic-return-maps','Elliptic return maps and component genera'),
                   ('subsec:II:hopf-component-boundaries','Hopf components and fibre boundaries')]:
    for oldrow in oldrows:
        current=dict(oldrow)
        current.update(unit_id=unit,unit_title=title,
          status='done' if oldrow['defect_type'] in ['D10','D16'] else 'open',
          date_utc=now(),evidence=str((folder/(prefix+'comparison.md')).relative_to(ROOT)),
          detail='Following unreviewed material retains all open classes and structure, with D10/D16 done. This boundary migration earns no movement credit.')
        rows.append(current)
_,incoming=read_tsv(folder/(prefix+'unit_status.tsv'))
assert len(incoming)==52
for item in incoming:
    kind=item['criterion'];status=item['status'];detail=item['reason']
    if kind in ['D14','D18','D23','structure']:status='open'
    rows.append(dict(paper='II',unit_id=item['unit'],unit_title=item['title'],
      row_kind='structure' if kind=='structure' else 'defect',defect_type='' if kind=='structure' else kind,
      status=status,date_utc=now(),evidence=str((folder/(prefix+'comparison.md')).relative_to(ROOT)),
      detail=detail+' Root also read both complete original/receiving proofs and the complete new common lemma. No subdivision or independent credit.'))
write_tsv(path,fields,rows)

_,sources=read_tsv(folder/(prefix+'sources.tsv'))
mapped=[]
for row in sources:
    mapped.append(dict(source=row['source_id'],url=row['url'],version=row['version'],
      locus=row['exact_locus'],date_utc=row['date_utc'],sha256='PDF: '+row['sha256'],
      own_word_summary=row['own_paraphrase'],
      use='P305/UN.28/UN.36 exact application; '+row['reader']+'. '+row['bytes']+' bytes. Published-work bytes remain outside the checkpoint.'))
print('Primary-source readings',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',mapped,'source'))
add_event('lem:II:compact-component-transport; cdp:st:C.2.UN.28; cdp:st:C.2.UN.36',
 'II-C3-ROOT-COMPACT-COMPONENT-ADMISSION','used and rechecked in this run',
 'Root read the complete original and receiving UN.28 and UN.36 statements and proofs, complete receiving P305, and full comparison. The integral complement sequence and its real scalar extension retain their exact coefficient maps; positivity of real holomorphic two-forms is proved by the displayed integral. The common higher root factors through P240 by r=s^(N/m_i), giving only the specified smooth single-component cover of total degree m_i. The full compact two-flow construction preserves all intersections and returns each identical parametrized cycle over the whole disc. UN.36 retains integral sum-of-lifts transfer, each weight m_i, kernel-in-radical, the rank-six index determinant -c^2, both boundary-rank bounds, and all oriented exterior-square actions including the epsilon*e13 cross term. Root checked their invariant bases and Gram entries directly. PG.3/CL.8 share one exact formula with both stable labels and targets; the real and integral exact sequences remain separately identified. Three exact primary-source readings are recorded at the conductor agent reader extent. D14/D18/D23 and final placement stay open; following elliptic/Hopf units remain open. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: component cores and integral invariant lattices',
 source='agents/continuation3_conductor/S6_SERIES_PUBLISH_c3_conductor_09_comparison.md')
print('P305 and both complete consumers admitted; following unreviewed units remain open.')
