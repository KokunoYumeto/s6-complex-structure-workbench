"""Admit the full-base elliptic owner, its two consumers and version locators."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_10_'
before=SOURCE.read_text();after=before
old=(folder/(prefix+'input.tex')).read_text();new=(folder/(prefix+'replacement.tex')).read_text()
assert after.count(old)==1
after=after.replace(old,new,1)
_,remote=read_tsv(folder/(prefix+'remote_repairs.tsv'));assert len(remote)==1
for row in remote:
    assert after.count(row['old_text'])==1,row['statement_id']
    after=after.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(before,after)
for oldids,newids in zip(identifiers(before),identifiers(after)):
    for name,count in oldids.items():assert newids[name]==count,name
    for name,count in (newids-oldids).items():assert newids[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix));print(suffix,append_rows(ROOT/target,rows,key))

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
unit='subsec:II:elliptic-return-maps'
oldrows=[r for r in rows if r['paper']=='II' and r['unit_id']==unit];assert len(oldrows)==26
rows=[r for r in rows if not(r['paper']=='II' and r['unit_id']==unit)]
for oldrow in oldrows:
    item=dict(oldrow)
    item.update(unit_id='subsec:II:cyclic-component-models',unit_title='Cyclic component models and elliptic fibre configurations',
      status='done' if oldrow['defect_type'] in ['D10','D16'] else 'open',date_utc=now(),
      evidence=str((folder/(prefix+'comparison.md')).relative_to(ROOT)),
      detail='Following material remains open apart from inherited D10/D16. Subsection boundary migration supplies no movement credit.')
    rows.append(item)
_,incoming=read_tsv(folder/(prefix+'unit_status.tsv'));assert len(incoming)==26
for item in incoming:
    kind=item['criterion'];status=item['status']
    if kind in ['D14','D18','D23','structure']:status='open'
    rows.append(dict(paper='II',unit_id=item['unit'],unit_title=item['title'],
      row_kind='structure' if kind=='structure' else 'defect',defect_type='' if kind=='structure' else kind,
      status=status,date_utc=now(),evidence=str((folder/(prefix+'comparison.md')).relative_to(ROOT)),
      detail=item['reason']+' Complete original/receiving comparisons are the conductor agent evidence; root read every receiving proof and the full comparison.'))
write_tsv(path,fields,rows)

bibprefix='S6_SERIES_PUBLISH_c3_conductor_bib155_156_'
_,bibrows=read_tsv(folder/(bibprefix+'edits.tsv'))
for row in bibrows:
    apply_edit(row['old_text'],row['new_text'],row['change_id'],[row['type']],row['statement_id'],
      row['old_location'],row['reason'],row['review_status'].replace('Parent admission pending.','Root compared both complete exact old/new entries and admitted this version-locator change.'))
_,events=read_tsv(folder/(bibprefix+'CHECK_EVENTS.tsv'))
print('Bibliography metadata events',append_rows(ROOT/'CHECK_EVENTS.tsv',events,'event_id'))
for sourceprefix in [prefix,bibprefix]:
    _,sources=read_tsv(folder/(sourceprefix+'sources.tsv'));mapped=[]
    for row in sources:
        mapped.append(dict(source=row['source_id'],url=row['url'],version=row['version'],locus=row['exact_locus'],
          date_utc=row['date_utc'],sha256=('PDF: '+row['sha256']) if row['sha256'] else '',
          own_word_summary=row['own_paraphrase'],
          use=row['reader']+'. '+row['bytes']+' bytes where a downloaded PDF exists. '+row['storage']))
    print('Primary readings',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',mapped,'source'))
add_event('lem:II:identity-monodromy-elliptic; lem:II:elliptic-first-integral; cdp:st:C.2.UN.29',
 'II-C3-ROOT-ELLIPTIC-RETURN-ADMISSION','used and rechecked in this run',
 'Root read the complete receiving P306, P303 and UN29 statements and proofs and the complete old/receiving comparison and four exact owner maps. The conductor agent full original/receiving readings are admitted at their stated exposed extent. P306 imposes no base-genus bound. Root checked the marked period ratio, the coefficient-one Abel-Jacobi map, the local equations t=u h^m, t=s^m, w^m=u, s=wh, relative minimality via the étale canonical comparison, the fixed-point equation for the deck linear part, and the invariant direct image over every multiple value. UN29 retains every ambient return-germ construction and all coefficient identities through orders d and 2d, period injection, the finite-base-change genus bound and the complete cyclic quotient/Iitaka comparison. P303 retains the inverse-time-loop pole exclusion, period map and canonical two-form calculation; its fixed elliptic curve is identified by [z] to [lambda_1 z]. The global combined guard preserves all original labels and targets, including RG13 moved into the shared earlier owner. Bibliography entries155/156 identify the exact author layouts. D14/D18/D23 and following cyclic models remain open. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: elliptic first integrals and return maps',source=__file__)
print('P306, both full consumers and bibliography155/156 admitted; no duplicate P306 insertion.')
