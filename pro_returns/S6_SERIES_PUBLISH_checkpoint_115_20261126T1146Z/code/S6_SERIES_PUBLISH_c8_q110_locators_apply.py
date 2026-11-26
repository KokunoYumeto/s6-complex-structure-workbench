"""Apply the exact three Q110 references after its canonical definition exists."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat()
lane=u.ROOT/'agents/continuation8_iii_weighted_units'
_,proposals=r.table(lane/'S6_SERIES_PUBLISH_Q110_locator_proposals.tsv')
source=u.repairs.SOURCE.read_text(encoding='utf-8');candidate=source
assert source.count(r'\label{mapsIII:def:elliptic-marked-data}')==1
df,rows=r.table(r.DEFECTS);ef,events=r.table(u.ROOT/'CHECK_EVENTS.tsv')
pairs=list(dict.fromkeys((x['old_text'],x['new_text']) for x in proposals));assert len(pairs)==3
for old,new in pairs:
 assert candidate.count(old)==1
 candidate=candidate.replace(old,new,1)
u.check_permanent_identifiers(source,candidate)
fragments={}
for key in ['whole_fibre_initial_pairs','canonical_star_logs']:
 p=u.WORK/'weighted'/(key+'.tex');text=p.read_text(encoding='utf-8')
 for old,new in pairs:
  if old in text:
   assert text.count(old)==1;text=text.replace(old,new,1)
 fragments[p]=text
 assert candidate.count(text)==1
for row in proposals:
 assert not any(x['change_id']==row['change_id'] for x in rows)
 out={k:row.get(k,'') for k in df};out['review_status']=row.get('review_status','')+'; canonical Q110 and exact old/new passages read by root, then applied '+now+'; final global reference gate open.'
 rows.append(out)
_,local=r.table(lane/'S6_SERIES_PUBLISH_Q110_locator_CHECK_EVENTS.tsv')
for row in local:
 assert row['type']=='used and rechecked in this run'
 assert not any(x['event_id']==row['event_id'] for x in events)
 out={k:row.get(k,'') for k in ef};out['outcome']=row['outcome']+' Exact three locator changes applied after Q110 became canonical; root read every old/new passage. No additional whole-proof or independent-check credit.';events.append(out)
u.repairs.SOURCE.write_text(candidate,encoding='utf-8',newline='\n')
for p,text in fragments.items():p.write_text(text,encoding='utf-8',newline='\n')
r.write_table(r.DEFECTS,df,rows);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,events)
print('UTC',now)
for _,new in pairs: print(new)
print('EXACT_SOURCE_EDITS',len(pairs),'DEFECT_ROWS',len(proposals),'BOUNDED_EVENTS',len(local))
print('NO_UNIT_CRITERION_CREDIT; GLOBAL_REFERENCE_GATE_OPEN')
