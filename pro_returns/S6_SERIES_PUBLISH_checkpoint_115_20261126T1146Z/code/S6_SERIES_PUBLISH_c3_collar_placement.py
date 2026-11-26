"""Place the unchanged general collar owner before all of its applications."""
from S6_SERIES_PUBLISH_c3_edit import *

before=SOURCE.read_text()
a=before.index(r'\begin{lemma}[Smooth normal-product collars]')
b=before.index(r'\end{proof}',a)+len(r'\end{proof}')
owner=before[a:b]
head=re.search(r'^\\subsection\{[^\n]+\}\\label\{subsec:II:fibre-fundamental-groups\}',before,re.M).group(0)
new_head=r'\subsection{Smooth normal-product collars}\label{subsec:II:normal-product-collars}'
after=before[:a]+before[b:]
assert after.count(head)==1
after=after.replace(head,new_head+'\n\n'+owner+'\n\n'+head,1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
SOURCE.write_text(after,newline='\n')
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[dict(
    change_id='II-C3-ROOT-COLLAR-EARLIER-PLACEMENT',type='D14',
    statement_id='lem:II:normal-product-collars',
    old_location='Beginning of canonical-flat central-fibre subsection',
    old_page='integrated build pending',
    new_location='Own subsection before fibre fundamental groups and all marked-cycle constructions',
    new_page='integrated build pending',old_text=owner,new_text=new_head+'\n\n'+owner,
    reason='The canonical-flat applications move after their compact-construction inputs. Their general smooth collar owner must precede UN46/UN57 as well, so move its exact unchanged statement and complete proof before those applications.',
    review_status='The complete P326 statement/proof was read in package12. This move is byte-identical and preserves every label and target; no new proof or page credit.')],'change_id')
fields,rows=read_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
unit='subsec:II:normal-product-collars'
assert not any(r['paper']=='II' and r['unit_id']==unit for r in rows)
for kind in [f'D{i:02}' for i in range(1,26)]+['structure']:
    status='open' if kind in ['D12','D14','D23','structure'] else 'done'
    detail='Complete unchanged collar owner read and admitted; exact smooth divisor-section, normal-product and attaching maps retained. Unit migration is not movement credit.'
    if kind=='D12':detail='Later UN46/UN57 repeated collar constructions await their assigned exact applications of this general owner.'
    if kind in ['D14','structure']:detail='The owner precedes all applications; final whole-paper structure review remains open.'
    if kind=='D23':detail='Source read; final integrated page reading remains open.'
    rows.append(dict(zip(fields,['II',unit,'Smooth normal-product collars',
        'structure' if kind=='structure' else 'defect','' if kind=='structure' else kind,
        status,now(),'CHECK_EVENTS.tsv: II-C3-ROOT-COLLAR-PLACEMENT',detail])))
write_tsv(ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',fields,rows)
set_unit_status('subsec:II:canonical-flat-fibres','D12','done',
    'UN65 applies the earlier P325 and P326 to the same proved boundary/collar data. The unresolved later collar repetitions are tracked at the extracted P326 unit, where the shared proof now resides.',
    'CHECK_EVENTS.tsv: II-C3-ROOT-COLLAR-PLACEMENT')
add_event('lem:II:normal-product-collars','II-C3-ROOT-COLLAR-PLACEMENT',
    'used and rechecked in this run',
    'The exact complete P326 statement and proof from admitted package12 moved byte-for-byte to a dedicated subsection before the fibre-group and marked-cycle constructions. All labels and targets retain their multiplicities. This prevents a forward dependence when UN64–68 move after the period constructions. Later UN46/UN57 proof transfers remain open and are now tracked on the collar unit; no new derivation or final-page credit.',
    'Smooth normal-product collars subsection',source=__file__)
print('P326 moved unchanged before every current and planned consumer.')
