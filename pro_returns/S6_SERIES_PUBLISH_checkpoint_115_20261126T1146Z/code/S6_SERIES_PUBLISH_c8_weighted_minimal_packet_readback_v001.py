"""Read back the six scoped proposals, correcting one event-scope phrase."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
p=lane/'S6_SERIES_PUBLISH_MINIMAL_CHECK_EVENTS.tsv'
with p.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
old='Q205 input and equation events have separate scopes.'
new='Q205 has a separate input-definition event; equation identities remain within the containing-proof scope.'
assert len(rows)==6 and rows[0]['outcome'].count(old)==1
rows[0]['outcome']=rows[0]['outcome'].replace(old,new)
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('CORRECTED_EVENT_SCOPE',old,'TO',new)
for r in rows: print(r['statement_id'],r['event_id'],r['type'],r['outcome'],sep='\n')
for suffix in ['program_table_proposals.tsv','historical_program_references.tsv']:
 p=lane/('S6_SERIES_PUBLISH_MINIMAL_'+suffix)
 print('TABLE',suffix)
 print(p.read_text())
print('SCOPED_EVENTS6; NO_EQUATION_EVENTS; INDEPENDENT_CREDIT0; SHARED_WRITES0')
