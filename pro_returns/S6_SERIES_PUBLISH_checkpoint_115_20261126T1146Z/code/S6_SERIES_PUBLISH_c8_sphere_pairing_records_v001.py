"""Write only the reviewed early sphere-pairing owner's local records."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path

root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
name='S6_SERIES_PUBLISH_SPHERE_PAIRING_'
fragment='agents/continuation8_iii_integration/units/root/sphere_smash_pairing.tex'
review=lane/(name+'unit_review.md')
text=(root/fragment).read_text()
assert len(text.splitlines())==199 and '\r' not in text
def write(suffix,fields,rows):
    with (lane/(name+suffix)).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
criteria=[]
for line in review.read_text().splitlines():
    if line.startswith('| '):
        cells=[c.strip() for c in line.strip('|').split('|')]
        if cells[0] in {f'D{i:02}' for i in range(1,28)}|{'Structure'}:
            assert len(cells)==2
            criteria.append([cells[0],'source-local complete; root admission/global gates open',cells[1]])
assert len(criteria)==28
write('unit_criteria.tsv',['criterion','proposed_state','evidence'],criteria)
path=lane/(name+'publication_defects.tsv')
with path.open(newline='') as f:
    r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
assert len(rows)==12
addition=r'''The cube representative of a based map $f:S^m\to S^n$ is
$f_C=h_n^{-1}fh_m$; the inverse transport is $f=h_nf_Ch_m^{-1}$.
The same formulas transport based homotopies at each time.
Below, $x,y,g$ also denote these representatives, and the displayed
$\mu$ maps specify the source and target coordinates of every smash.
'''
assert text.count(addition)==1
for kind in ['D20','D22','D26']:
    rows.append(dict(zip(fields,[f'III-C8-SPHERE-PUB-006-{kind}',kind,'wb:def:ordered-cube-spheres','root/sphere_smash_pairing.tex end of Q253','pending page concordance','root/sphere_smash_pairing.tex end of Q253','pending final build','',addition,'State the exact conjugation from round-sphere maps to cube maps, its inverse and its action on based homotopies, so reuse of x/y/g notation is an explicit coordinate transport. Added by a bounded exact patch and read back.',''])))
for row in rows:
    row['review_status']='whole repaired input, original/receiving proofs, comparisons, candidate and final bounded addition read; source-local complete; root admission/global gates open'
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
scopes=[
    ('Q253','wb:def:ordered-cube-spheres','Whole new ordered-cube definition read, including explicit stereographic homeomorphism/inverse, block concatenation/inverse, pinch map and f_C=h_n^{-1} f h_m with inverse. Actual final bounded addition read. No independent-check credit.'),
    ('038V','wb:cusp-s12-full-carrier-null','Whole repaired634-line parent input read for dependencies. Whole released statement/proof,132-line receiving proof, comparison and both primary records read. Whole early194-line candidate plus final5-line exact transport addition read. Full all-pairs theorem, both actual pinch homomorphisms, twists, all integral groups and parity argument retained; native application preserved as later Q254. Equations0390/0392/0391 wholly read. No new required or independent row; global admission/placement gates open.'),
    ('038T','wb:cusp-s12-all-higher-smashes-null','Whole released statement/proof,40-line receiving proof, comparison and ten-line defining input read. Whole final proof read in early candidate. All based maps and integers r>=2 retained; direct r2 case and exact ordered H_r, quotient continuity, initial/terminal values and fixed basepoint verified. No independent-check credit; global gates open.')]
event_fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
events=[]
for tag,label,scope in scopes:
    event='III-C8-SPHERE-'+tag+'-PUBLICATION-READBACK'
    events.append([label,'2026-11-25','GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight unit editor','used and rechecked in this run',scope,event,'continuation-eight-publication',str(review.relative_to(root)),'whole substantive review','used and rechecked in this run',event,'','',now,fragment])
write('CHECK_EVENTS.tsv',event_fields,events)
program='code/S6_SERIES_PUBLISH_c8_sphere_pairing_edit_v001.py'
write('program_table_proposals.tsv',['printed_path','repository_path','sha256','description'],[[program,program,hashlib.sha256((root/program).read_bytes()).hexdigest(),'Whole source and actual six-line stdout/empty stderr read. Guarded split of wholly read universal proofs, local presentation changes and original-identifier preservation across two owners; no mathematical independent-check credit.']])
print('UTC',now,'CRITERIA',len(criteria),'DEFECT_ROWS',len(rows),'EVENTS',len(events))
print('FRAGMENT',fragment,'LINES',len(text.splitlines()),'SHA256',hashlib.sha256(text.encode()).hexdigest())
for tag,label,scope in scopes: print('READING_EVENT',tag,label,scope)
print('BOUNDED_ADDITION_READBACK\n'+addition,end='')
print('NO_SHARED_WRITES; NO_NEW_INDEPENDENT_CREDIT; EARLY_PLACEMENT_REQUIRES_ROOT_ADMISSION')
