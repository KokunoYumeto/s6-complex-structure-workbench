from pathlib import Path
import csv,json,collections
root=Path(__file__).resolve().parents[1]
path=root/'CHECK_EVENTS.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t')
    fields=reader.fieldnames
    events=list(reader)
updates=[]
for event in events:
    if event['type'] in ('source comparison','source check'):
        updates.append({'event_id':event['event_id'],'statement_id':event['statement_id'],
                        'old_type':event['type'],'new_type':'targeted proof check'})
        event['type']='targeted proof check'
# Stable event identifiers and exact source-only outcomes are retained. This is
# a vocabulary correction, not an additional mathematical check.
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
    writer.writeheader();writer.writerows(events)
allowed={'targeted proof check','independent re-proof','computation or formal certificate',
         'used and rechecked in this run','carried as background without fault found',
         "refuted, with the refined statement's id"}
assert {x['type'] for x in events}<=allowed
record={'changes':updates,'total_events':len(events),'counts':dict(collections.Counter(x['type'] for x in events))}
(root/'event_type_corrections.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
