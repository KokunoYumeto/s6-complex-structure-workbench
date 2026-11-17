"""Inventory the newly checked characteristic prerequisites before III assembly."""
from pathlib import Path
import csv,json
OUT=Path(__file__).resolve().parents[2];ROOT=OUT.parent
p=OUT/'S6_09_PAPERS_inventory.csv'
with p.open(newline='') as f:
    reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
index={(r['source_run'],r['source_id']):r for r in rows}
items=json.loads((OUT/'work/maps_audit/course_characteristic_provider_inventory.json').read_text())
added=[]
for item in items:
    if item['duplicate_of_existing_inventory']:continue
    key=('WORKING_EDITION_COURSE_PROVIDER',item['source_id'])
    if key in index:continue
    r={k:'' for k in fields}
    r.update(source_run=key[0],source_id=key[1],source_file=item['source_file'],paper='III',kind='Classical '+item['kind'].lower(),
      wording_vs_source='Complete classical source argument inventoried before Paper III assembly; final printed label and wording will be reconciled with the manuscript.',
      recorded_checks=item['credit']+' This is source provenance; the producing header is not an independent proof check.',
      your_check='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 17 November2026: complete provider proof read and re-derived by the independent maps reader; exact scope '+str(item['start_line'])+'–'+str(item['end_line'])+' in '+item['source_file']+'.',
      check_outcome='Complete source proof reading passed; final source-to-print comparison awaits required Paper III assembly.',
      found_elsewhere='Classical singular cohomology, Thom/Euler or characteristic-class argument; full source re-derivation retained. No new-result claim.',
      credited_to='Classical topology and characteristic classes; the complete receiving-source re-derivation is retained.',
      notes='Additional proof prerequisite, preserving all original928 rows. Source SHA256 '+item['source_sha256']+'; detailed reader record work/maps_audit/course_characteristic_provider_inventory.json.')
    for k in ['found_in_AC26','found_in_E26','found_in_DGKX_v1']:
        r[k]='Classical prerequisite, not claimed new; no result-specific negative literature-absence assertion.'
    lines=(ROOT/item['source_file']).read_text().splitlines()
    r['statement_as_printed']='SOURCE PENDING FINAL PLACEMENT:\n'+'\n'.join(lines[item['start_line']-1:item['end_line']])
    rows.append(r);index[key]=r;added.append(item)
assert len(fields)==17 and len(index)==len(rows)
with p.open('w',newline='') as f:
    writer=csv.DictWriter(f,fields);writer.writeheader();writer.writerows(rows)
(OUT/'records/characteristic_inventory_additions.json').write_text(json.dumps(added,indent=2)+'\n')
print('Added',len(added),'classical prerequisites; total rows',len(rows))
