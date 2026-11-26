"""Admit complete attributed cyclic reviews and the actual resolved LV boundary."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now = datetime.now(timezone.utc).isoformat()
note = 'agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_cyclic_and_lv_boundary_admission.md'
folder = u.ROOT / 'agents/continuation8_iii_foundations'
df, ds = r.table(r.DEFECTS)
ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
edits = [x for x in r.table(folder / 'S6_SERIES_PUBLISH_c8_foundations_defects.tsv')[1]
         if x['change_id'].startswith('c8-III-foundations-cyclic-')]
tags = {'02KE','02KF','02KH','02KI','02K8','02KG','02K9','02KA','Q142','Q143','Q144','Q145','Q146'}
events = [x for x in r.table(folder / 'S6_SERIES_PUBLISH_c8_foundations_CHECK_EVENTS.tsv')[1]
          if any(x['event_id'] == 'ce:III:c8:foundations:' + t + ':unit' for t in tags)]
assert (len(edits), len(events)) == (72,13), (len(edits), len(events))
for row in edits:
    assert not any(x['change_id'] == row['change_id'] for x in ds)
    out = {k:row.get(k,'') for k in df}
    out['review_status'] += '; complete attributed whole-unit review and actual canonical boundary admitted ' + now + '; ' + note
    ds.append(out)
for row in events:
    assert row['type'] == 'used and rechecked in this run'
    assert not any(x['event_id'] == row['event_id'] for x in es)
    out = {k:row.get(k,'') for k in ef}
    out['outcome'] += ' Root read the entire substantive review and all28 criteria, then the actual successful application and both canonical boundaries. Whole mathematical source readings retain their stated attribution. ' + note
    es.append(out)
source = u.repairs.SOURCE.read_text()
units = [
 ('maps:src:D.1.5','Cohomology products and characteristic classes of cyclic covers',True),
 ('mapsIII:def:cyclic-coefficient-data','Finite-coefficient cubics and the fundamental class',False),
 ('mapsIII:def:canonical-cyclic-model','Smooth recognition and cyclic complex families',False),
 ('maps:src:D.2.53','The weighted OS45 manifold',True),
]
closed = added = 0
for ident,title,existing in units:
    assert '\\label{' + ident + '}' in source
    selected = [x for x in ps if x['paper']=='III' and x['unit_id']==ident]
    if existing:
        assert len(selected)==28 and all(x['status']=='open' for x in selected)
    else:
        assert not selected
        for c in [f'D{i:02d}' for i in range(1,28)]+['structure']:
            row = {k:'' for k in pf}
            row.update(paper='III',unit_id=ident,row_kind='structure' if c=='structure' else 'defect',defect_type='' if c=='structure' else c)
            ps.append(row);selected.append(row);added+=1
    for row in selected:
        c = row['defect_type'] or 'structure'
        done = c not in {'D04','D06','D09','D18'}
        row.update(unit_title=title,status='done' if done else 'open',date_utc=now,evidence=note,
          detail='Whole attributed source/proof comparisons and every criterion admitted; actual preceding/following boundaries read. Four common integration gates and final PDF remain.')
        closed += done
    eid = 'publish:c8:III:cyclic-lv-boundary:' + ident
    assert not any(x['event_id']==eid for x in es)
    event = {k:'' for k in ef}
    event.update(statement_id=ident,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',
      outcome='Complete substantive review and all28 criteria read, actual successful canonical application/empty stderr and exact successor read. Cyclic old pieces collected from both actual positions; LV now ends directly before OS49. No independent, required, program-rerun or final-page credit. ' + note,
      event_id=eid,phase='continuation8 publication unit comparison',source_file=note,source_event_type='used and rechecked in this run',evidence_group='publish:c8:III:cyclic-lv-boundaries',date_utc=now,where=note)
    es.append(event)
assert (closed,added)==(96,56)
r.write_table(r.DEFECTS,df,ds)
r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
print('UTC',now)
print('EXACT_DEFECT_ROWS',len(edits),'ATTRIBUTED_USED_EVENTS',len(events),'ROOT_USED_EVENTS',len(units))
print('ACTUAL_UNITS',len(units),'CRITERIA_CLOSED',closed,'NEW_ACTUAL_UNIT_ROWS',added)
print('FOUR_COMMON_GATES_AND_FINAL_PDF_OPEN')
