from S6_SERIES_PUBLISH_c3_edit import *
import re

folder=ROOT/'agents/continuation3_provenance'
text=SOURCE.read_text()
original=text
_,links=read_tsv(folder/'S6_SERIES_PUBLISH_c3_provenance_link_edits.tsv')
_,proposals=read_tsv(folder/'S6_SERIES_PUBLISH_c3_provenance_text_edits.tsv')
source_rows=links+[r for r in proposals if int(r['change_id'].split('-')[-1])<=134]
for row in source_rows:
    assert text.count(row['old_text'])==1, row['change_id']
    text=text.replace(row['old_text'],row['new_text'],1)
preserve_identifiers(original,text)
address='https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-ii'
assert text.count(address)==1
assert set(re.findall(r'https?://[^}\s]*githubusercontent[^}\s]*|https?://[^}\s]*github\.com[^}\s]*',text))=={address}
assert re.findall(r'\b[0-9a-f]{40}\b',text)==['bc08b5278bcad2beb70b6862c5722f1b9f636db6']
SOURCE.write_text(text,newline='\n')
print('Source edits admitted:',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',source_rows,'change_id'))

apply_edit(r'\StatementRecord{series:II:B}{proved}{03K3}{\SeriesRef{cdp:st:D.1.2}, \SeriesRef{cdp:st:C.3.1}}',
    r'\StatementRecord{series:II:B}{proved}{03K3}{\SeriesRef{cdp:st:D.1.2}, \SeriesRef{cdp:st:C.3.1}, \SeriesRef{cdp:st:C.3.11}}',
    'II-C3-CLASSIFICATION-MAIN-OWNER',['D14'],'series:II:B','Theorem B input declaration',
    'Theorem B keeps its original complete hypotheses and conclusions. C.3.1 supplies necessary fibre properties; C.3.11 now uniquely owns the exhaustive list and occurrence conclusion, so include that exact supplying owner.')
apply_edit('classification are \\cref{cdp:st:D.1.2,cdp:st:C.3.1}.',
    'classification are \\cref{cdp:st:D.1.2,cdp:st:C.3.1,cdp:st:C.3.11}.',
    'II-C3-CLASSIFICATION-STATUS-OWNER',['D18'],'series:II:B','Theorem B relation to literature',
    'Point the exhaustive classification clause to its sole receiving owner while retaining the exact integral and necessary-property sources.')
apply_edit('integral refinement and general-fibre comparisons:\n\\cref{cdp:st:D.1.2,cdp:st:C.3.1}.',
    'integral refinement and general-fibre comparisons:\n\\cref{cdp:st:D.1.2,cdp:st:C.3.1,cdp:st:C.3.11}.',
    'II-C3-CLASSIFICATION-TABLE-OWNER',['D18'],'series:II:B','Known and new, row B',
    'The table now names the same exact integral, necessary-property and final-classification owners as the theorem status line.')
apply_edit('\\item \\SeriesRef{cdp:st:C.3.11}\\quad Full-fibre cohomology and direct images.',
    '\\item \\SeriesRef{cdp:st:C.3.11}\\quad Complete smooth-fibre classification, occurrence and full-fibre cohomology.',
    'II-C3-CLASSIFICATION-FURTHER-RESULT',['D24'],'cdp:st:C.3.11','Further results',
    'The one-line description now matches all conclusions owned by C.3.11 after the exact scope consolidation.')

_,claims=read_tsv(folder/'S6_SERIES_PUBLISH_c3_provenance_claim_rows.tsv')
for row in claims:
    if row['claim_id']=='II-C3-LIT-B2':
        row['current_resolution']+=' Final exhaustive classification and occurrence now have the sole owner C.3.11, with the necessary-property assertions in C.3.1; both front-matter loci name these exact owners.'
    if row['claim_id']!='II-C3-PV-DEPOSIT':
        row['resolution_status']='Primary comparison complete; source proposals admitted.'
        row['remaining_gate']='Final text and count recomputation, remaining program additions, deposit integration and rendered front-matter reading.'
print('Claim rows admitted:',append_rows(ROOT/'S6_SERIES_PUBLISH_provenance_checks.tsv',claims,'claim_id'))
print('Source has one prescribed repository URL and one commit literal; 125 plain program paths are admitted.')
print('Deposit rows135–138 and records refresh remain deferred to text-final as instructed.')
