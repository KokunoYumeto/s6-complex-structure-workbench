"""Admit the compared repairs from the complete 787-page fixed-PDF reading.

Default is read-only. --apply changes the manuscript, its existing defect
table, and accurately scoped proof-reading events. It gives no rendered-page
completion and writes no derived inventory, manifest, or copy.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import runpy
import sys
from S6_SERIES_PUBLISH_c4_edit import ROOT, SOURCE, append_rows, preserve_identifiers
from S6_SERIES_PUBLISH_c4_admit import protected_statement
from S6_SERIES_PUBLISH_c4_derive_II import parse_statements, current_data, count_prose

csv.field_size_limit(100000000)
FIXED_SOURCE = '781e9d079bca0cdf1d04704dc0147adf06740a3b4aea9e8476f342eca9407566'
FIXED_PDF = 'e5856a7a707d681f89712150d4f1b100554f29a08bc5a843c5d52aa1d7ca2871'

def rows(path):
    with Path(path).open() as f:
        return list(csv.DictReader(f,delimiter='\t'))

def main():
    apply = '--apply' in sys.argv
    before = SOURCE.read_text()
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == FIXED_SOURCE
    statements, _, _, _ = parse_statements(before)
    def owner(old):
        p = before.index(old)
        containing = [r for r in statements if r['start'] <= p < r['stop']]
        if containing:
            return containing[-1]['statement_id']
        return next(r['statement_id'] for r in statements if r['start'] >= p)
    guards, defects = [], []
    def add(change, sid, page, old, new, reason, review):
        guards.append((change,old,new))
        defects.append(dict(change_id=change,type='D23',statement_id=sid,
            old_location=sid,old_page=str(page)+' in PDF '+FIXED_PDF,
            new_location=sid,new_page='pending final rebuilt-page inspection',
            old_text=old,new_text=new,reason=reason,review_status=review))
    saved_args=sys.argv
    try:
        sys.argv=['root_visual_repairs.py']
        root_items=runpy.run_path(str(ROOT/'code/S6_SERIES_PUBLISH_c4_root_visual_repairs.py'))['items']
    finally:
        sys.argv=saved_args
    for change,sid,page,old,new,reason in root_items:
        add(change,sid,page,old,new,reason,
            'Root viewed the complete original pages and read the exact source contexts. Only the stated layout/capitalization tokens change. Rebuilt images remain open.')
    horizontal=ROOT/'agents/continuation4_horizontal'
    horizontal_pages=[234,250,265,265,269,269,269,300,311,307,314,350,370,377,392]
    horizontal_reasons=[
        'Keep subsection 16.4 and the Proposition 16.5 opening together.',
        'Keep section 17, subsection 17.1 and the Proposition 17.1 opening together.',
        'Capitalize the sentence-initial proposition reference; target and application are exact.',
        'Capitalize the sentence-initial proposition reference; target and application are exact.',
        'Capitalize the sentence-initial proposition reference; target and application are exact.',
        'Capitalize the sentence-initial proposition reference; target and application are exact.',
        'Capitalize the sentence-initial proposition reference; target and application are exact.',
        'Use one result-kind phrase for the exact sign statement night:P4.7, declared as a proposition.',
        'Keep the single title word examples unbroken, with the same PDF-string text.',
        'Print the declared Proposition kind for the same cdp:st:C5a target.',
        'Print the declared Proposition kind for the same cdp:st:A.3.5 target.',
        'Name the cited push:src:E.2.11 by its declared Proposition kind.',
        'Keep the Theorem 29.3 heading with its first statement lines.',
        'Keep the Proposition 31.2 heading with its first statement lines.',
        'Capitalize the sentence-initial proposition reference; target and application are exact.',
    ]
    hr=rows(horizontal/'S6_SERIES_PUBLISH_c4_visual_guards.tsv')
    assert len(hr)==len(horizontal_pages)==len(horizontal_reasons)==15
    for r,page,reason in zip(hr,horizontal_pages,horizontal_reasons):
        add(r['change_id'],owner(r['old_text']),page,r['old_text'],r['new_text'],reason,
            'Actual old-page image and exact declared targets were read by horizontal; root read every old/new guard and its source comparison. Mathematical text and target identities are preserved; rebuilt image check remains open.')
    conductor=ROOT/'agents/continuation4_conductor'
    cr=rows(conductor/'S6_SERIES_PUBLISH_c4_pages_401_600_replacements.tsv')
    cd=rows(conductor/'S6_SERIES_PUBLISH_c4_pages_401_600_defects.tsv')
    assert len(cr)==len(cd)==9
    for r,d in zip(cr,cd):
        assert (r['old_text'],r['new_text'],r['statement_id'])==(d['old_text'],d['new_text'],d['statement_id'])
        add(d['change_id'],r['statement_id'],d['old_page'],r['old_text'],r['new_text'],r['reason'],
            'Actual old pages and all historical interval members read by conductor. Horizontal read full original/receiving proofs and exact target owners; the associated six events retain that exposure. Root read the entire comparison and every exact substitution. New rendered pages remain open.')
    reductions=ROOT/'agents/continuation4_reductions'
    rr=json.loads((reductions/'S6_SERIES_PUBLISH_c4_visual_repairs_guards.json').read_text())
    rd=rows(reductions/'S6_SERIES_PUBLISH_c4_visual_repairs_defects.tsv')
    assert len(rr)==len(rd)==6
    for r,d in zip(rr,rd):
        page=int(r['key'].split('P')[-1])
        guards.append(('II-C4-VISUAL-REDUCTIONS-'+r['key'],r['old'],r['new']))
        defects.append(dict(change_id='II-C4-VISUAL-REDUCTIONS-'+r['key'],type='D23',
            statement_id=d['unit_id'],old_location=d['unit_id'],old_page=str(page)+' in PDF '+FIXED_PDF,
            new_location=d['unit_id'],new_page='pending final rebuilt-page inspection',
            old_text=d['old_text'],new_text=d['new_text'],reason=d['reason'],
            review_status='Actual pages read by reductions. Full original/receiving UN76 proof and exact lattice/cone, finite-quotient and invariant-algebra owners were compared. Root read the exact changes and complete comparison note. Layout additions remove to the original bytes; rebuilt images remain open.'))
    assert len(guards)==len(defects)==36
    after=before
    for change,old,new in guards:
        assert after.count(old)==1,(change,after.count(old))
        preserve_identifiers(old,new)
        after=after.replace(old,new,1)
    for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}'):
        assert re.findall(pattern,before)==re.findall(pattern,after)
    for sid in ('push:src:E.5.2','push:src:E.5.3'):
        assert protected_statement(before,sid)==protected_statement(after,sid)
    events=rows(horizontal/'S6_SERIES_PUBLISH_c4_visual_proof_CHECK_EVENTS.tsv')
    events+=rows(reductions/'S6_SERIES_PUBLISH_c4_visual_repairs_CHECK_EVENTS.tsv')
    assert len(events)==7
    assert {r['type'] for r in events}=={'used and rechecked in this run'}
    assert len({r['event_id'] for r in events})==len(events)
    current_events=rows(ROOT/'CHECK_EVENTS.tsv')
    assert not {r['event_id'] for r in current_events}&{r['event_id'] for r in events}
    assert not {r['change_id'] for r in rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv')}&{r['change_id'] for r in defects}
    if not apply:
        print('Validated 36 exact repairs and seven full-proof/reference reading events. No central write.')
        return
    SOURCE.write_text(after,newline='\n')
    append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',defects,'change_id')
    append_rows(ROOT/'CHECK_EVENTS.tsv',events,'event_id')
    # The seven admitted readings change the printed count prose before the
    # next build. This replaces only that prose and the matching deposit text.
    data=current_data()
    old_count=re.search(r'The records associate [\s\S]+?each outcome specifies its scope and prior proof exposure\.',data['text'])[0]
    new_count=count_prose(data)
    from S6_SERIES_PUBLISH_c4_edit import apply_edit
    apply_edit(old_count,new_count,'II-C4-FINAL-VISUAL-COUNTS',['D15'],'methodology',
        'Section 1.5: admitted proof/reference readings from final image review',
        'Include the seven actually completed exposed full-proof/reference readings in the exact statement-associated counts; keep their used-and-rechecked type and actual evidence-group overlap.',
        review='Seven admitted events only; typography-only repairs supply no mathematical event. All type totals are deterministically selected from admitted exact subjects.')
    deposit_path=ROOT/'S6_SERIES_PUBLISH_deposit_fields_II.json'
    deposit=json.loads(deposit_path.read_text())
    assert deposit['provenance'].count(old_count.replace('\n',' '))==1
    old_deposit_count=old_count.replace('\n',' ')
    deposit['provenance']=deposit['provenance'].replace(old_deposit_count,new_count.replace('\n',' '),1)
    deposit_path.write_text(json.dumps(deposit,ensure_ascii=False,indent=2)+'\n',newline='\n')
    from S6_SERIES_PUBLISH_c4_final_provenance import write_deposit_markdown
    write_deposit_markdown(deposit)
    append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[dict(
        change_id='II-C4-FINAL-VISUAL-DEPOSIT-COUNTS',type='D15',statement_id='Paper II deposit fields',
        old_location='Paper II deposit provenance count paragraph',old_page='not applicable',
        new_location='Paper II deposit provenance count paragraph',new_page='not applicable',
        old_text=old_deposit_count,new_text=new_count.replace('\n',' '),
        reason='Synchronize the exact admitted-event paragraph with the seven exposed proof/reference comparisons recorded during the PDF review.',
        review_status='Same deterministic selection as the manuscript; no new independence or page credit.')],'change_id')
    print('Admitted 36 rendered findings, seven used-and-rechecked events, and matching count prose.')
    print('Exact event associations:',len(data['selected']),'evidence groups:',len(data['groups']))
    print('Labels, tags and both protected statements retain their exact identities/bytes. Rebuilt page reading remains open.')

if __name__=='__main__':
    main()
