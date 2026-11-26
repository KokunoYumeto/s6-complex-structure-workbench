"""Admit the complete elliptic-core units and their exact torsor applications."""
from S6_SERIES_PUBLISH_c3_edit import *

folder=ROOT/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_13_'
before=SOURCE.read_text(); after=before
old=(folder/(prefix+'input.tex')).read_text()
new=(folder/(prefix+'replacement.tex')).read_text()
assert after.count(old)==1
after=after.replace(old,new,1)
_, repairs=read_tsv(folder/(prefix+'remote_repairs.tsv'))
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
    if suffix=='CHECK_EVENTS.tsv':
        for row in rows:
            if 'effort' not in row['who']:row['who']+='; effort setting not separately exposed'
    print(suffix,append_rows(ROOT/target,rows,key))

fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
old_unit='cdp:st:C.2.UN.66'
assert sum(r['paper']=='II' and r['unit_id']==old_unit for r in progress)==26
retained=[r for r in progress if not(r['paper']=='II' and r['unit_id']==old_unit)]
_,statuses=read_tsv(folder/(prefix+'unit_status.tsv'))
for row in statuses:
    unit=old_unit if row['unit']=='subsec:II:elliptic-core-reduction' else row['unit']
    kind=row['criterion']
    status='open' if kind in ['D14','D23','structure'] else row['status']
    detail=row['reason']+' Complete original/receiving proofs read by conductor; root read all 981 receiving main lines, P330 and every changed remote application, plus the complete comparison. Migration of subsection rows supplies no movement credit.'
    retained.append(dict(zip(fields,['II',unit,row['title'],
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,
        status,now(),'CHECK_EVENTS.tsv: II-C3-ROOT-CONDUCTOR13-ADMISSION',detail])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in retained]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,retained)

_,sources=read_tsv(folder/(prefix+'sources.tsv'))
source_rows=[dict(source=r['source_id'],url=r['url'],version=r['version'],
    locus=r['exact_locus']+'; '+r['reader'],date_utc=r['date_utc'],sha256=r['sha256'],
    own_word_summary=r['own_paraphrase'],
    use='P260 uses the point-blowup comparison for global invariants and supplies its separate two-chart proof for the direct-image sheaf identities. The receiving contraction is explicitly q=q0 tau.') for r in sources]
print('Sources',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',source_rows,'source'))
add_event('lem:II:vertical-elliptic-alignment;lem:II:zero-chern-elliptic-torsor;cdp:st:C.2.UN.66;cdp:st:C.2.UN.67;cdp:st:C.2.UN.24;cdp:st:C.2.UN.32;cdp:st:C.2.UN.61',
    'II-C3-ROOT-CONDUCTOR13-ADMISSION','used and rechecked in this run',
    'Conductor read every complete old and receiving P260/UN66/UN67/K3/UN61 proof and the P330 transfer. Root read the complete 981-line receiving main package, full P330 and comparison, and all remote changed applications with surrounding proof context. P260 retains the given T,q and exact vertical-boundary domain, proves q=q0 tau and identifies identity monodromy before using P306 on the relatively minimal T0. Its local Laurent calculation proves both direct-image identities; its global invariants give pg=g(B)<=1 and chi=0. The original intermediate unrestricted smooth-multiple assertion is repaired at its contraction, while UN66 verifies when tau is the identity. The vertical boundary case on P1 is handled before the horizontal Euclidean cover. The ruled extension identifies the section and its normal line through dual and tensor projectivizations. UN67 retains the full pencil, Stein degree and exact normal-order argument. P330 proves the identical analytic torsor class through gE-gmodel=cj-ci, local translations and their inverses, and the full rank-four period lattice. KX13/14 and PT7/8 keep their identifiers at this one owner; K3 and UN61 name their exact inputs. Final global placement and PDF reading remain open. No independent-proof or final-page credit.',
    'Complete elliptic-core and torsion-normal units with bounded remote torsor applications',source=__file__)
print('Conductor13 admitted; stable original UN66 progress identity retained.')
