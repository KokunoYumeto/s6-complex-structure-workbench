"""Admit the three complete original-cap publication reviews at actual boundaries."""
from datetime import datetime,timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now=datetime.now(timezone.utc).isoformat();note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_original_caps_admission.md'
df,ds=r.table(r.DEFECTS);ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv');pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
folder=u.ROOT/'agents/continuation8_iii_foundations'
selected=[x for x in r.table(folder/'S6_SERIES_PUBLISH_c8_foundations_defects.tsv')[1] if x['change_id'].startswith('C8-FND-ORIGINAL-CAPS-')]
labels=set(re.findall(r'\\label\{([^}]+)\}',(u.WORK/'foundations/original_cap_homology.tex').read_text()))
events=[x for x in r.table(folder/'S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv')[1] if x['statement_id'] in labels]
assert(len(selected),len(events))==(83,10),(len(selected),len(events))
for row in selected:
 assert not any(x['change_id']==row['change_id'] for x in ds)
 out={k:row.get(k,'') for k in df};out['review_status']=row.get('review_status','')+'; complete attributed review and canonical placement admitted '+now+'; actual boundary/common/PDF holds: '+note;ds.append(out)
for row in events:
 assert row['type']=='used and rechecked in this run' and not any(x['event_id']==row['event_id'] for x in es)
 out={k:row.get(k,'') for k in ef};out['outcome']=row['outcome']+' Root read all three complete reviews and their individual all28 criterion tables, actual placement outputs and following boundaries. Whole-proof readings remain attributed. No new independent credit. '+note;es.append(out)
closed=added=0
for ident,title,complete in [('maps:src:D.2.31','Original additive caps with zero component Chern class',True),('maps:src:D.2.32','All original additive caps and their integral homology',True),('maps:src:D.2.33','Original multiplicative caps and pending next boundary',False)]:
 assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps)
 for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
  done=complete and c not in {'D04','D06','D09','D18'};row={k:'' for k in pf};row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,status='done' if done else 'open',date_utc=now,evidence=note,detail='Full attributed source/proof and all28 review admitted; '+('actual next subsection present, with four common gates open.' if complete else 'all criteria held until the complete LA actual subsection begins.'));ps.append(row);added+=1;closed+=done
rows=[x for x in ps if x['paper']=='III' and x['unit_id']=='maps:src:D.2.30'];assert len(rows)==28 and all(x['status']=='open' for x in rows)
for row in rows:
 c=row['defect_type'] or 'structure';done=c not in {'D04','D06','D09','D18'};row.update(status='done' if done else 'open',date_utc=now,evidence=note,detail='The completed L6 proof now has the actual complete L7 subsection after it; common/PDF gates remain.');closed+=done
assert(closed,added)==(72,84)
r.write_table(r.DEFECTS,df,ds);r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es);r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now);print('EXACT_DEFECT_ROWS',len(selected),'ATTRIBUTED_USED_EVENTS',len(events));print('SOURCE_CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added);print('L9_ALL28_HELD; FOUR_COMMON_GATES_AND_FINAL_PAGES_OPEN')
