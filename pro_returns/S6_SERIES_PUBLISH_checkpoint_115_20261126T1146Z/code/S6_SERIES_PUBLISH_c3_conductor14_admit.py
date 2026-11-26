"""Admit the Hopf adjacency unit and its exact arbitrary-cover field clause."""
from S6_SERIES_PUBLISH_c3_edit import *
folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_14_'
before=SOURCE.read_text();after=before
old=(folder/(prefix+'input.tex')).read_text();new=(folder/(prefix+'replacement.tex')).read_text()
assert after.count(old)==1
after=after.replace(old,new,1)
_,repairs=read_tsv(folder/(prefix+'remote_repairs.tsv'))
for row in repairs:
    assert after.count(row['old_text'])==1,row['statement_id']
    after=after.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(before,after)
for old_ids,new_ids in zip(identifiers(before),identifiers(after)):
    assert all(new_ids[k]==v for k,v in old_ids.items())
    assert all(new_ids[k]==1 for k in new_ids-old_ids)
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    for row in rows:
        if suffix=='CHECK_EVENTS.tsv' and 'effort' not in row['who']:row['who']+='; effort setting not separately exposed'
    print(suffix,append_rows(ROOT/target,rows,key))
fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
assert sum(r['paper']=='II' and r['unit_id']=='sec:II:10' for r in progress)==26
retained=[r for r in progress if not(r['paper']=='II' and r['unit_id']=='sec:II:10')]
_,statuses=read_tsv(folder/(prefix+'unit_status.tsv'))
for row in statuses:
    unit='sec:II:10' if row['unit']=='subsec:II:marked-cycle-tree-constructions' else row['unit']
    kind=row['criterion'];status=row['status'];reason=row['reason']
    if kind in ['D14','D23','structure']:status='open'
    if unit=='subsec:II:hopf-axis-adjacency' and kind=='D18':
        status='done';reason='Both exact primary versions and curve/normal-form loci were freshly read and matched to the already verified bibliography keys. No local unverified citation remains; separate bibliography-wide checks retain their own rows.'
    reason+=' Root read complete receiving UN40 and comparison and every changed P327 application; conductor read complete old/new UN40/P327. Original sec10 identity remains open on the following construction unit; no migration movement credit.'
    retained.append(dict(zip(fields,['II',unit,row['title'],'structure' if kind=='structure' else 'defect',
        '' if kind=='structure' else kind,status,now(),'CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR14-ADMISSION',reason])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in retained]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,retained)
_,sources=read_tsv(folder/(prefix+'sources.tsv'))
incoming=[dict(source=r['source_id']+' (third-continuation Hopf adjacency)',url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],
    use='UN40 applies the exact primary curve/normal-form list after P327 identifies the algebraic dimension through the given finite unramified cover. Divisor pushforward and canonical pullback preserve every original coefficient and adjacency conclusion.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',incoming,'source'))
add_event('cdp:st:C.2.UN.40;lem:II:central-primary-hopf-cover',
    'II-C3-ROOT-CONDUCTOR14-ADMISSION','used and rechecked in this run',
    'Conductor read complete old and receiving UN40/P327; root read the complete receiving UN40, full comparison and all changed P327 statement/proof paragraphs. The original arbitrary multiplicities, arbitrary point blowdowns and chosen primary finite unramified cover remain. UN17 is applied to the same canonical evaluation, identity normalization and zero intrinsic conductor. Divisor-class pushforward is defined on each prime and on principal divisors; the generic SNC calculation proves the pushed boundary reduced. P327 now states its already general local-sheet symmetric-polynomial argument for each given finite connected unramified p, retaining the central-cover construction. The exact curve lists are cited after this p gives a(P)=a(H). All six HA formula payloads, independent characters, nonlinear infinite order and neighbour inequalities remain. The original sec10 identity stays open on the unread construction remainder. No independent or final-page credit.',
    'Hopf axes and arbitrary-cover algebraic dimension',source=__file__)
print('Conductor14 admitted.')
