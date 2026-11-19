#!/usr/bin/env python3
"""Independent structural coverage audit of the canonical event union."""
import csv,json,re,collections
csv.field_size_limit(16 * 1024 * 1024)
from pathlib import Path

P=Path(__file__).resolve().parents[2];A=P/'analysis/continuation_ledger'
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
canonical=list(csv.DictReader((P/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
inventory=list(csv.DictReader((P/'S6_10_PAPERS_inventory.csv').open()))
provenance=[json.loads(line) for line in (A/'event_provenance.jsonl').open()]
received=set()
for event in provenance:
 for pr in event['provenance']:
  received.add((pr['source'],str(pr['source_row']),event['statement_id']))

missing=[];expected_count=0;table_count=0
paths=sorted((P/'records').glob('*events.tsv'))+sorted((P/'analysis').glob('*/current_check_events.tsv'))
for path in paths:
 table_count+=1
 for number,row in enumerate(csv.DictReader(path.open(),delimiter='\t'),2):
  value=row.get('statement_id') or row.get('label') or row.get('labels') or ''
  labs=json.loads(value) if value.strip().startswith('[') else re.split('[;,]',value)
  for lab in labs:
   lab=lab.strip().replace('s6:night:','night:')
   if not lab:continue
   expected_count+=1;key=(str(path.relative_to(P)),str(number),lab)
   if key not in received:missing.append(key)
labels={r['statement_id'] for r in canonical}
bad_status=[(r['label'],r['status']) for r in inventory if r['status'] not in {'proved','open','false as stated'} and not r['status'].startswith('proved under hypotheses H')]
extra=sorted(labels-{r['label'] for r in inventory})
papers='\n'.join((P/f'S6_10_PAPERS_{x}.tex').read_text() for x in ['I','II','III','IV','V','VI'])
result={
 'source_event_tables':table_count,'expanded_source_event_occurrences':expected_count,
 'missing_source_occurrences':missing,
 'events':len(canonical),'event_ids_unique':len({r['event_id'] for r in canonical})==len(canonical),
 'invalid_event_types':sorted({r['type'] for r in canonical}-allowed),
 'checkers_without_effort':[r['event_id'] for r in canonical if 'effort ' not in r['who']],
 'undated_current_events':[r['event_id'] for r in canonical if r['phase']!='historical' and not r['date']],
 'inventory_rows':len(inventory),'unique_inventory_labels':len({r['label'] for r in inventory}),
 'inventory_rows_without_event':[r['label'] for r in inventory if r['label'] not in labels],
 'invalid_inventory_statuses':bad_status,
 'noninventory_event_labels':extra,
 'noninventory_labels_are_printed_equations':all('\\label{'+x+'}' in papers and ':eq:' in x for x in extra),
 'source_Q03_rows_in_inventory':[r['label'] for r in inventory if 'Q03' in r['source_run']],
 'source_night_rows':sum(r['source_run']=='S6_06_BLIND' for r in inventory),
 'scope':'Mechanical coverage only. No mathematical proof or three-check gate is awarded by this audit.'
}
assert not missing and result['event_ids_unique']
assert not result['invalid_event_types'] and not result['checkers_without_effort'] and not result['undated_current_events']
assert not result['inventory_rows_without_event'] and not bad_status
assert result['noninventory_labels_are_printed_equations'] and not result['source_Q03_rows_in_inventory']
result['outcome']='PASS'
(A/'audit_event_union.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
