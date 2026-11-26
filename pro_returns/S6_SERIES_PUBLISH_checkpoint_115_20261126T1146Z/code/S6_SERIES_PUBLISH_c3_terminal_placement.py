"""Place terminal geometry after the marked support constructions it uses."""
from S6_SERIES_PUBLISH_c3_edit import *
before=SOURCE.read_text()
start=r'\subsection{Terminal ruled contractions}\label{subsec:II:terminal-ruled-contractions}'
end=r'\section{Compact occurrence of prescribed component classes}\hypertarget{tag-0345}{}\label{sec:II:09}'
anchor=r'\section{Actual contractions, canonical reduction and finite generation}\hypertarget{tag-0347}{}\label{sec:II:11}'
assert all(before.count(x)==1 for x in [start,end,anchor])
a,b=before.index(start),before.index(end)
block=before[a:b]
after=before[:a]+before[b:]
heading=r'\section{Terminal contractions and canonical-flat fibres}\label{sec:II:canonical-flat-classification}'+'\n\n'
after=after.replace(anchor,heading+block+anchor,1)
old_heading=r'\section{Local torus fillings and canonical-flat component geometry}'
new_heading=r'\section{Semistable torus fillings}'
assert after.count(old_heading)==1
after=after.replace(old_heading,new_heading,1)
preserve_identifiers(before,after)
assert after.count(block)==1
assert after.index(r'\label{sec:II:10}')<after.index(start)<after.index(r'\label{sec:II:11}')
SOURCE.write_text(after,newline='\n')
rows=[]
for n,kind in enumerate(['D12','D14','D24'],1):
    rows.append(dict(change_id=f'II-C3-ROOT-TERMINAL-PLACEMENT-{n:02}',type=kind,
        statement_id='cdp:st:C.2.UN.64;cdp:st:C.2.UN.65;cdp:st:C.2.UN.66;cdp:st:C.2.UN.67;cdp:st:C.2.UN.68',
        old_location='Terminal units before compact occurrence and marked support constructions',
        old_page='working source before final build',new_location='New terminal-contraction section immediately after the marked support section and before UN69',
        new_page='integrated final build pending',old_text=start+' ... '+end,
        new_text=heading+'[identical complete terminal block]'+anchor,
        reason='The terminal classification uses the compact and marked-support constructions. Their full body now precedes these applications. The collar owner P326 has already been extracted earlier for UN46/UN57. The original section now contains only its semistable torus fillings. Every byte of the moved statement/proof block is unchanged.',
        review_status='Exact block identity and unique positions verified; prior complete proof comparisons remain. Final whole-paper dependency and first-part review open; no migration movement or page-reading credit.'))
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id')
add_event('sec:II:canonical-flat-classification;sec:II:all:08',
    'II-C3-ROOT-TERMINAL-PLACEMENT','used and rechecked in this run',
    'The complete already compared UN64–68 block moves byte-identically after the marked support constructions and before their UN69 contraction consumers. P326 remains at its earlier independent owner. All old labels and targets remain. This is a placement check; global order is still open and no proof re-derivation, new closure or final-page reading is claimed.',
    'Terminal contraction and canonical-flat section placement',source=__file__)
print('Terminal block moved unchanged after section10.')
