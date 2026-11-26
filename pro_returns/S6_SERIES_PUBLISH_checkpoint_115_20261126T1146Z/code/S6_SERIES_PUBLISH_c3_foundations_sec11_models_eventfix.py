from pathlib import Path
import csv

root=Path(__file__).resolve().parents[1]
path=root/'agents/continuation3_foundations/sec11/S6_SERIES_PUBLISH_sec11_models_CHECK_EVENTS.tsv'
with path.open(newline='') as f:
    r=csv.DictReader(f,delimiter='\t'); fields=r.fieldnames; rows=list(r)
target='publish:c3:foundations:sec11:models:UN66'
hits=0
for row in rows:
    if row['event_id']==target:
        old='Read the complete original/current 771-line UN66 block and the complete 474-line receiver through the last inclusion-exclusion argument.'
        new='Read the complete original/current UN66 block and the complete receiving proof through the last inclusion-exclusion argument.'
        assert old in row['outcome']
        row['outcome']=row['outcome'].replace(old,new)
        hits+=1
assert hits==1
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
log=root/'code/S6_SERIES_PUBLISH_c3_foundations_sec11_models_log.py'
text=log.read_text()
assert old in text
log.write_text(text.replace(old,new),newline='\n')
print('Only the UN66 event outcome and its generator text were synchronized; source and guards unchanged.')
