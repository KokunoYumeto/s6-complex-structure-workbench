"""Admit signed roots and the complete paired/secondary occurrence units."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_occurrence_root'
prefix='S6_SERIES_PUBLISH_c3_occurrence_pairs_'
before=SOURCE.read_text();after=before
for row in json.loads((folder/(prefix+'guards.json')).read_text()):
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
_,rows=read_tsv(folder/(prefix+'defects.tsv'))
for row in rows:
    row['review_status']='Root read complete original UN18/UN21 and complete receiving P339/UN18/UN21, with every exact transfer, quotient and cohomology map. Exposed used-and-rechecked comparison; no independent or final-page credit.'
print('Defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))

fields,progress=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
assert sum(r['paper']=='II' and r['unit_id']=='sec:II:09' for r in progress)==26
for row in progress:
    if row['paper']=='II' and row['unit_id']=='sec:II:09':
        row.update(unit_title='Enriques and further elliptic components; remaining occurrence units',
            date_utc=now(),evidence='CHECK_EVENTS.tsv: II-C3-ROOT-OCCURRENCE-PAIRS-ADMISSION',
            detail='Original section9 open identity retained on the unread remainder beginning subsec:II:enriques-elliptic-occurrence. New reviewed subdivisions are not counted as closures of this original row.')
units=[('subsec:II:signed-root-fibrations','Signed root fibrations'),
       ('subsec:II:paired-root-occurrence','Paired roots and projective elliptic components'),
       ('subsec:II:secondary-kodaira-occurrence','Secondary Kodaira components')]
for unit,title in units:
    for kind in [f'D{i:02}' for i in range(1,26)]+['structure']:
        status='open' if kind in ['D14','D23','D24','structure'] else 'done'
        if unit=='subsec:II:signed-root-fibrations' and kind=='D12':status='open'
        progress.append(dict(zip(fields,['II',unit,title,'structure' if kind=='structure' else 'defect',
            '' if kind=='structure' else kind,status,now(),
            'CHECK_EVENTS.tsv: II-C3-ROOT-OCCURRENCE-PAIRS-ADMISSION',
            'Complete original and receiving text read against all25 classes. Exact tuple, chart, covering, cohomology and divisor-persistence applications compared; no missing local instance found. Original section9 identity remains open on the unread remainder. Final order, front matter and rendered pages remain open. P339/UN6 duplicate ambient proof has its explicit pending bounded transfer; subdivision supplies no movement credit.'])))
keys=[(r['paper'],r['unit_id'],r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys)==len(set(keys))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,progress)
set_unit_status('subsec:II:elliptic-root-fillings','D12','open',
    'The newly extracted P339 is also the exact positive-divisor ambient construction used here. Root will transfer the duplicate local quotient/properness/product proof after provenance’s guarded P336/UN6 admission, preserving ER4–ER8 aliases and every component map. This identified repetition reopens only D12.',
    'CHECK_EVENTS.tsv: II-C3-ROOT-OCCURRENCE-PAIRS-ADMISSION')
add_event('lem:II:signed-root-fibration;cdp:st:C.2.UN.18;cdp:st:C.2.UN.21',
    'II-C3-ROOT-OCCURRENCE-PAIRS-ADMISSION','used and rechecked in this run',
    'Root read complete old and receiving UN18/UN21 and the complete P339 owner, against all25 defect classes. The shared signed-root construction now states its full disjoint smooth-divisor domain with exact homogeneous space, reciprocal gluing, cyclic maps, free finite charts, properness, full multiplicities, product inverse and globally framed higher direct images. UN18 uses the identical two-point blowup, signed exceptional curves, m and q; every projective-cover, canonical, Seifert, integral and coherent computation and base-change comparison remains. UN21 uses the exact m=1 inverse projection to the nonzero line bundle; its half-period quotient, canonical character, integral mapping-torus and invariant bounding-chain calculations, scheme-fibre eigenframes and final normalization morphism remain. P337 is applied at the same elliptic axes, and P236 at the same smooth-fillings central divisors. Every original label/target remains once, and all local manual equation numbers become section numbers. One duplicated alternate projectivity argument and process/history clauses are recorded in defects. The P339/UN6 bounded transfer is explicitly pending; original sec9 remainder stays open. No independent-check or final-page credit.',
    'Signed-root owner; paired roots; secondary Kodaira components',source=__file__)
print('P339, UN18 and UN21 admitted; UN6 ambient transfer and section9 remainder remain open.')
