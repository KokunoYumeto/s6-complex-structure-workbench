#!/usr/bin/env python3
"""Independently audit every actual records TSV and current-check source row.

Unlike the event-only count, this includes source-opening tables and checks
the complete original field dictionary, not just the location/label key.
No canonical file or inventory value is written.
"""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re,collections,io

csv.field_size_limit(16*1024*1024)
P=Path(__file__).resolve().parents[2];A=P/'analysis/continuation_ledger'
proofs=[json.loads(line) for line in (A/'event_provenance.jsonl').read_text().splitlines()]
indexed=collections.defaultdict(list)
for event in proofs:
 for provenance in event['provenance']:
  indexed[(provenance['source'],str(provenance['source_row']),event['statement_id'])].append((event,provenance))
paths=sorted((P/'records').glob('*.tsv'))+sorted((P/'analysis').glob('*/current_check_events.tsv'))
snapshot={row['path']:row for row in json.loads((A/'source_manifest.json').read_text())}
missing=[];pending=[];raw_mismatches=[];unknown=[];empty=[];tables=[];mapping=[]
for path in paths:
 raw_bytes=path.read_bytes();rel=str(path.relative_to(P))
 rows=list(csv.DictReader(io.StringIO(raw_bytes.decode()),delimiter='\t'))
 row_count=0;expanded=0
 for num,row in enumerate(rows,2):
  row_count+=1
  if any(key in row for key in ['statement_id','label','labels']):
   value=row.get('statement_id') or row.get('label') or row.get('labels') or ''
   schema='event'
  elif 'used_by' in row:
   value=row['used_by'];schema='source opening'
  else:
   unknown.append({'source':rel,'source_row':num,'fields':list(row)});continue
  labels=json.loads(value) if value.strip().startswith('[') else re.split(r'\s*[;,]\s*',value)
  labels=[str(x).strip().replace('s6:night:','night:') for x in labels if str(x).strip()]
  if not labels:empty.append({'source':rel,'source_row':num,'raw_row':row})
  for label in labels:
   expanded+=1;key=(rel,str(num),label);matches=indexed.get(key,[])
   if not matches:
    previous=snapshot.get(rel)
    if previous and num>previous['rows']+1 and hashlib.sha256(raw_bytes).hexdigest()!=previous['sha256']:
     pending.append({'key':key,'raw_new_row':row,'basis':'This row was appended beyond the source row count captured by the frozen canonical source manifest.'})
    else:missing.append(key)
   exact=[(event,pr) for event,pr in matches if pr['raw_event']==row]
   if matches and not exact:raw_mismatches.append({'key':key,'expected':row,'received':[pr['raw_event'] for _,pr in matches]})
   mapping.append({'source':rel,'source_row':num,'source_label':label,'schema':schema,
    'raw_row_sha256':hashlib.sha256(json.dumps(row,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
    'canonical_event_ids':[event['event_id'] for event,_ in exact],
    'complete_original_fields_preserved':bool(exact)})
 tables.append({'source':rel,'sha256':hashlib.sha256(raw_bytes).hexdigest(),
  'original_rows':row_count,'expanded_label_occurrences':expanded})
result={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'tables':len(tables),
 'original_rows':sum(x['original_rows'] for x in tables),'expanded_label_occurrences':len(mapping),
 'schema_occurrences':dict(collections.Counter(x['schema'] for x in mapping)),
 'missing_from_captured_snapshot':missing,'later_appended_occurrences_pending':pending,
 'raw_field_mismatches':raw_mismatches,'unknown_schema_rows':unknown,'empty_label_rows':empty,
 'canonical_ledger_sha256':hashlib.sha256((P/'CHECK_EVENTS.tsv').read_bytes()).hexdigest(),
 'scope':'Complete mechanical provenance preservation only. No proof, computation, source-verification or owner gate is awarded by this audit.'}
assert not missing and not raw_mismatches and not unknown and not empty,result
result['outcome']='PASS for captured canonical snapshot; later appended rows explicitly pending' if pending else 'PASS'
(A/'all_record_row_audit.output.json').write_text(json.dumps(result,indent=2)+'\n')
(A/'all_record_row_manifest.json').write_text(json.dumps(tables,indent=2)+'\n')
with (A/'all_record_row_mapping.jsonl').open('w') as f:
 for item in mapping:f.write(json.dumps(item,ensure_ascii=False)+'\n')
print(json.dumps(result,indent=2))
