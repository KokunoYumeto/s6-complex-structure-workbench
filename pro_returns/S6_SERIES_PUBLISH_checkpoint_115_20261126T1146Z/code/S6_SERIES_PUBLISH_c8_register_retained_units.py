"""Track the actual new subsections without awarding completed criteria."""
from collections import Counter
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now=datetime.now(timezone.utc).isoformat()
note='agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_retained_angle_unit_review.md'
source=u.repairs.SOURCE.read_text()
for key in ('quotient_maps','retained_angle','based_smoothing','named_fibrations'):
    fragment=(u.WORK/'root'/(key+'.tex')).read_text()
    assert source.count(fragment)==1,key
pf,ps=r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
before=Counter(x['status'] for x in ps if x['paper']=='III')
old=[x for x in ps if x['paper']=='III' and x['unit_id']=='maps:src:B.3.1']
assert len(old)==28
assert not any(x['paper']=='III' and x['unit_id']=='mapsIII:def:cusp-suspension-maps' for x in ps)
for row in old:
    row.update(unit_id='mapsIII:def:cusp-suspension-maps',unit_title='Angle-forgetting and cusp-core quotient maps',date_utc=now,
       evidence=note,detail='Old aggregate unit rekeyed after the actual J7 relocation. All28 statuses are preserved; rekeying receives no completion credit. D12/structure admission is separately pending.')
for row in ps:
    if row['paper']=='III' and row['unit_id']=='wb:h24:ret:section':
        assert row['status']=='open'
        row.update(unit_title='The regular cusp torus',date_utc=now,evidence=note,
          detail='Actual first retained-angle subsection now canonical; whole review exists, final consolidation admission pending.')
new=[
 ('mapsIII:based-regular-fibre-smoothing','Based smoothing at a regular fibre'),
 ('mapsIII:lem:retained-angle-differential','Differential and orientation of the cusp torus'),
 ('wb:h24:ret:framing-proposition','Stable framing and the spin invariant'),
 ('maps:src:B.3.1','The retained-angle homotopy class'),
]
for ident,title in new:
    assert '\\label{'+ident+'}' in source
    assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps)
    for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
        row={k:'' for k in pf}
        row.update(paper='III',unit_id=ident,unit_title=title,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c,
          status='open',date_utc=now,evidence=note,detail='Actual complete canonical subsection; all28 rows created open. Final shared-owner/Q257 admission remains pending; no progress from this registration.')
        ps.append(row)
after=Counter(x['status'] for x in ps if x['paper']=='III')
assert after['done']==before['done'] and after['open']==before['open']+112
ef,es=r.table(u.ROOT/'CHECK_EVENTS.tsv')
eid='publish:c8:III:retained-actual-boundaries'
assert not any(x['event_id']==eid for x in es)
event={k:'' for k in ef}
event.update(statement_id='mapsIII:def:cusp-suspension-maps; wb:h24:ret:section; maps:src:B.3.1; maps:src:B.4.1',date='2026-11-25',
 who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',
 outcome='Read actual successful quotient/retained application at20:10:13UTC and exact J9-to-Q021 and03BE-to-Q7/JA boundaries. Read actual successful JA application at20:10:44UTC and its exact following cell input. Complete fragments match current canonical source once each. Rekey28 old quotient rows and create112 actual subsection rows, all without changing any completed status. Q257/native consolidation and final gates remain open. '+note,
 event_id=eid,phase='continuation8 publication unit comparison',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:retained-boundaries',date_utc=now,where=note)
es.append(event)
r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
print('UTC',now)
print('REKEYED_ROWS',len(old),'NEW_ACTUAL_OPEN_ROWS',112,'NEW_COMPLETED_CRITERIA',0)
print('III_DONE',after['done'],'III_OPEN',after['open'])
