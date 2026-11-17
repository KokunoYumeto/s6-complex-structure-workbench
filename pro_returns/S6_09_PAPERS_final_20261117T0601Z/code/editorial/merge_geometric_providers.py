"""Add necessary geometric/stable provider proof units before III assembly.
The recorded receiving proof check does not imply closure of imported dependencies.
"""
from pathlib import Path
import csv,json
D=Path(__file__).resolve().parents[2];p=D/'S6_09_PAPERS_inventory.csv'
with p.open(newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
index={(r['source_run'],r['source_id']):r for r in rows};added=[];refreshed=[]
items=[]
for name in ['course_geometric_provider_inventory.json','course_duality_euler_provider_inventory.json']:
 items.extend(json.loads((D/'work/maps_audit'/name).read_text()))
for item in items:
 if item['duplicate_of_existing_inventory']:continue
 key=(item['source_run'],item['source_id'])
 exists=key in index
 row=index[key] if exists else {k:'' for k in fields}
 printed=row.get('printed_label','');printed_statement=row.get('statement_as_printed','')
 for k in fields:
  if k in item:row[k]=item[k] if isinstance(item[k],str) else json.dumps(item[k],ensure_ascii=False)
 row['kind']='Classical '+item['kind'].lower()
 row['printed_label']=printed
 row['statement_as_printed']=printed_statement if printed else 'SOURCE PROOF UNIT PENDING PLACEMENT: '+item.get('source_heading',item['title'])
 row['your_check']='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November2026: independent maps reader read and re-derived the complete receiving proof unit '+str(item['proof_range'])+'; exact event '+item['current_check_event']+'. Imported dependency closure is separately scoped and is not presumed.'
 row['check_outcome']=item['check_outcome']+' Final source-to-print comparison pending Paper III assembly.'
 row['credited_to']=item.get('credited_to',item.get('source_credit','Classical topology, re-derived here.'))
 row['notes']+=' Source SHA256 '+item['source_sha256']+'; full retained proof '+item['retained_complete_proof']+'; reserved label '+item['reserved_label']+'. Producer: '+item['producer']+', effort '+item['producer_effort']+', '+item['producer_date']+'. Full raw producer provenance and ranges are retained in the provider inventory.'
 if not exists:rows.append(row);index[key]=row;added.append(item['source_id'])
 else:refreshed.append(item['source_id'])
assert len(fields)==17 and len(index)==len(rows)
with p.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
(D/'records/geometric_inventory_additions.json').write_text(json.dumps({'added':added,'refreshed':refreshed,'count':len(added),'total':len(rows),'scope':'Complete receiving proof units independently read; imported dependency closure and exact literature comparisons remain separately scoped.'},indent=2)+'\n')
print('Added',len(added),'geometric provider units; inventory',len(rows))
