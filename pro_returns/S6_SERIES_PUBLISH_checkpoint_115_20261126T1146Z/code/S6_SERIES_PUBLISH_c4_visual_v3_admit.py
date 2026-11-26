"""Admit fourteen exact repairs identified while completing the v2 image pass.

Ten declared-kind wordings, one proof-square placement, and three fully
compared tail references. Default is read-only; no derived census is written.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys
import fitz
from S6_SERIES_PUBLISH_c4_edit import ROOT,SOURCE,append_rows,preserve_identifiers,apply_edit
from S6_SERIES_PUBLISH_c4_admit import protected_statement
from S6_SERIES_PUBLISH_c4_derive_II import parse_statements,parse_aux,current_data,count_prose
from S6_SERIES_PUBLISH_c4_final_provenance import write_deposit_markdown

FIXED_SOURCE='c5b971cbfc549c32e082b6f6423439fbbc68d5550da0d13a3b3653e1e3e6dcc8'
FIXED_PDF='da3b7b7dd810b1a36a783cfa36b91d2fb744019763b32768b6b3fe887dac530d'
csv.field_size_limit(100000000)

def rows(path):
    with Path(path).open() as f:return list(csv.DictReader(f,delimiter='\t'))

def main():
    before=SOURCE.read_text()
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==FIXED_SOURCE
    statements,owners,_,_=parse_statements(before)
    by_id={r['statement_id']:r for r in statements}
    aux=parse_aux(ROOT/'build/II_c4_final_v2/S6_SERIES_PUBLISH_II.aux')
    def owner(old):
        position=before.index(old)
        return next(r for r in statements if r['start']<=position<r['stop'])
    pdf_path=ROOT/'build/II_c4_final_v2/S6_SERIES_PUBLISH_II.pdf'
    assert hashlib.sha256(pdf_path.read_bytes()).hexdigest()==FIXED_PDF
    with fitz.open(pdf_path) as pdf:
        page_text=[re.sub(r'\s+',' ',p.get_text()) for p in pdf]
    # These exact source contexts and declared target owners were read by
    # root. Only the presentation of the same referenced number changes.
    phrases=[
        (r'Statement \ref{cdp:st:D.1.2} gives the last equality.', 'Statement 5.1 gives the last equality.'),
        (r'Statement \ref{cdp:st:C2d} applies to this smooth curve', 'Statement 8.10 applies'),
        (r'Statement \ref{cdp:st:A.5.8} gives a holomorphic ruling', 'Statement 9.7 gives a holomorphic ruling'),
        (r'Statement \ref{cdp:st:A.5.7} now applies everywhere along', 'Statement 10.4 now applies'),
        (r'Statement \ref{cdp:st:A.5.15} excludes it.', 'Statement 10.8 excludes it.'),
        (r'Statement \ref{cdp:st:C2d} gives a smooth normalization near the', 'Statement 8.10 gives a smooth'),
        (r'Statement \ref{cdp:st:C2d} gives an unramified degree-three', 'Statement 8.10 gives an unramified'),
        (r'The compact-component theorem \cref{cdp:st:C.2.UN.15} applies to the resolved finite-base-change family', 'The compact-component theorem proposition 41.7 applies'),
        ('The compact-component theorem '+r'\cref{cdp:st:C.2.UN.15}'+' applies\nalso to this finite base-change family', 'The compact-component theorem proposition 41.7 applies'),
        (r'exact cyclic quotient theorem \cref{cdp:st:C.2.UN.23}.', 'exact cyclic quotient theorem proposition 42.1.'),
    ]
    guards=[]; defects=[]
    for number,(old,query) in enumerate(phrases,1):
        assert before.count(old)==1,(number,before.count(old))
        own=owner(old)
        target=re.search(r'\\(?:c?ref)\{([^}]+)\}',old)[1]
        assert by_id[owners[target]]['kind']=='proposition'
        new=old.replace(r'Statement \ref',r'\Cref').replace('theorem '+r'\cref','result in '+r'\cref')
        first=int(aux[own['statement_id']]['page'])
        following=[r for r in statements if r['start']>=own['stop']]
        last=int(aux[following[0]['statement_id']]['page']) if following else len(page_text)
        matches=[p+1 for p,text in enumerate(page_text) if query in text and first<=p+1<=last]
        assert len(matches)==1,(number,query,matches,first,last)
        page=matches[0]
        cid=f'II-C4-V3-KIND-{number:02d}'
        guards.append((cid,old,new))
        reason=(f'The exact target {target} is declared as a proposition and prints number {aux[target]["number"]}. '
            'The replacement passes that same label to the result-kind-aware command, or places the descriptive phrase before its declared-kind reference. '
            'Every mathematical application, target label and number is preserved.')
        defects.append(dict(change_id=cid,type='D23',statement_id=own['statement_id'],
            old_location=own['statement_id'],old_page=f'{page} in PDF {FIXED_PDF}',
            new_location=own['statement_id'],new_page='pending rebuilt-page reading',old_text=old,new_text=new,
            reason=reason,review_status='Root read every exact source context and target declaration/number. The PDF text match is used only to locate the old occurrence, with no image-reading credit. Rebuilt appearance remains open.'))
        print(cid,'page',page,'target',target,'Proposition',aux[target]['number'])
    horizontal=ROOT/'agents/continuation4_horizontal'
    qed=rows(horizontal/'S6_SERIES_PUBLISH_c4_pages_v2_111_121_replacements.tsv')
    assert len(qed)==1
    conductor=ROOT/'agents/continuation4_conductor'
    tail=rows(conductor/'S6_SERIES_PUBLISH_c4_pages_v2_tail_replacements.tsv')
    assert len(tail)==3
    for number,(r,page) in enumerate(zip(qed+tail,['117–118','756','761','762']),1):
        cid=f'II-C4-V3-IMAGE-{number:02d}'
        guards.append((cid,r['old_text'],r['new_text']))
        defects.append(dict(change_id=cid,type='D23',statement_id=r['statement_id'],
            old_location=r['statement_id'],old_page=page+' in PDF '+FIXED_PDF,
            new_location=r['statement_id'],new_page='pending rebuilt-page reading',
            old_text=r['old_text'],new_text=r['new_text'],reason=r['reason'],
            review_status='Actual v2 image findings; complete original/receiving proof and exact target comparisons by horizontal, with every historical interval member retained. Root read the full comparison and each exact guard. The QED placement adds only its formatting command. Rebuilt image reading remains open.'))
    assert len(guards)==len(defects)==14
    after=before
    for cid,old,new in guards:
        assert after.count(old)==1,(cid,after.count(old))
        preserve_identifiers(old,new)
        after=after.replace(old,new,1)
    for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}'):
        assert re.findall(pattern,before)==re.findall(pattern,after)
    for sid in ('push:src:E.5.2','push:src:E.5.3'):
        assert protected_statement(before,sid)==protected_statement(after,sid)
    events=rows(horizontal/'S6_SERIES_PUBLISH_c4_v2_tail_proof_CHECK_EVENTS.tsv')
    assert len(events)==2 and {e['type'] for e in events}=={'used and rechecked in this run'}
    assert not {e['event_id'] for e in events}&{e['event_id'] for e in rows(ROOT/'CHECK_EVENTS.tsv')}
    assert not {d['change_id'] for d in defects}&{d['change_id'] for d in rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv')}
    if '--apply' not in sys.argv:
        print('Read-only validation: fourteen exact guards and two full-proof comparison events ready.')
        return
    SOURCE.write_text(after,newline='\n')
    append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',defects,'change_id')
    append_rows(ROOT/'CHECK_EVENTS.tsv',events,'event_id')
    data=current_data()
    old_count=re.search(r'The records associate [\s\S]+?each outcome specifies its scope and prior proof exposure\.',data['text'])[0]
    new_count=count_prose(data)
    apply_edit(old_count,new_count,'II-C4-FINAL-V3-COUNTS',['D15'],'methodology',
        'Section 1.5 final exposed-reference reading counts',
        'Include the two completed UN85/UN86 original/receiving proof comparisons at their actual used-and-rechecked type; all other associations and exposure scopes are retained.',
        review='Exact current-label/alias event selection; no typography-only event or independent derivation is added.')
    path=ROOT/'S6_SERIES_PUBLISH_deposit_fields_II.json'
    deposit=json.loads(path.read_text())
    old_flat=old_count.replace('\n',' ');new_flat=new_count.replace('\n',' ')
    assert deposit['provenance'].count(old_flat)==1
    deposit['provenance']=deposit['provenance'].replace(old_flat,new_flat,1)
    path.write_text(json.dumps(deposit,ensure_ascii=False,indent=2)+'\n',newline='\n')
    write_deposit_markdown(deposit)
    append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[dict(change_id='II-C4-FINAL-V3-DEPOSIT-COUNTS',
        type='D15',statement_id='Paper II deposit fields',old_location='Paper II deposit count paragraph',
        old_page='not applicable',new_location='Paper II deposit count paragraph',new_page='not applicable',
        old_text=old_flat,new_text=new_flat,reason='Use the same final exact-subject selection as the manuscript after the two actual UN85/UN86 proof comparisons.',
        review_status='Source and deposit count prose synchronized; actual final rendering and derived records remain open.')],'change_id')
    print('Admitted fourteen repairs; counts',len(data['selected']),'associations and',len(data['groups']),'groups.')
    print('All labels, tags and both protected statements preserved. Final image reading remains open.')

if __name__=='__main__':main()
