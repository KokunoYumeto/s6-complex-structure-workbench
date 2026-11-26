"""Record the wholly read common based smoothing lemma, without shared writes."""
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
prefix='S6_SERIES_PUBLISH_BASED_SMOOTHING_'
fragment='agents/continuation8_iii_integration/units/root/based_smoothing.tex'
text=(root/fragment).read_text()
assert hashlib.sha256(text.encode()).hexdigest()=='d279d123465e24955feaddccb95295dfc99143557f5e51ad569d3f08d20070cc'
review=lane/(prefix+'unit_review.md')
criteria=[]
for line in review.read_text().splitlines():
    if line.startswith('| '):
        cells=[x.strip() for x in line.strip('|').split('|')]
        if cells[0] in {f'D{i:02}' for i in range(1,28)}|{'Structure'}:
            assert len(cells)==2
            criteria.append([cells[0],'source-local complete; root admission/global gates open',cells[1]])
assert len(criteria)==28
def write(suffix,fields,rows):
    with (lane/(prefix+suffix)).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows)
write('unit_criteria.tsv',['criterion','proposed_state','evidence'],criteria)
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
reason='Create one complete common owner for the based regular-fibre smoothing proof. All bump, protected tube, full-fibre gap, explicit convolution, radial/geodesic homotopies, fixed differential and based Pontryagin comparison are proved. Exact old-owner replacement rows belong to their separate unit edits. No independent-check increment.'
rows=[[f'III-C8-SMOOTHING-PUB-001-{kind}',kind,'mapsIII:based-regular-fibre-smoothing','new common proof from whole original038S items13-15 and retained/X comparison','pending page concordance','root/based_smoothing.tex','pending final build','',text,reason,'whole128-line final statement/proof read; root separately reports complete approval; source-local complete; all global gates open'] for kind in ['D12','D13','D14','D20','D22','D26']]
write('publication_defects.tsv',fields,rows)
now=datetime.now(timezone.utc).isoformat()
event='III-C8-SMOOTHING-Q255-PUBLICATION-READBACK'
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
scope='Whole128-line Q255 statement and complete proof read after explicit convolution refinement; all based bump, fixed T/K0, exact d0 complement, injectivity-radius bounds, homotopy endpoints/full-fibre/differential preservation and based PT interpolation checked. Whole original038S320 proof lines, receiver/comparison/primary record and prior907-line retained proof used; later root966-line reading is separately attributed. No new required or independent-check credit. Actual early placement and global gates remain root.'
write('CHECK_EVENTS.tsv',fields,[['mapsIII:based-regular-fibre-smoothing','2026-11-25','GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical reasoning effort not separately exposed; continuation eight unit editor','used and rechecked in this run',scope,event,'continuation-eight-publication',str(review.relative_to(root)),'whole substantive review','used and rechecked in this run',event,'','',now,fragment]])
print('UTC',now,'CRITERIA',len(criteria),'DEFECT_ROWS',len(rows),'EVENTS',1)
print('FRAGMENT',fragment,'LINES',len(text.splitlines()),'SHA256',hashlib.sha256(text.encode()).hexdigest())
print('READING_EVENT',scope)
print('CANONICAL_AND_SHARED_WRITES 0; NEW_INDEPENDENT_CHECK_CREDIT 0')
