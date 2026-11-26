"""Admit the full attributed LV review and the actual LP/LV boundary."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now = datetime.now(timezone.utc).isoformat()
note = 'agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_lv_publication_admission.md'
df, ds = r.table(r.DEFECTS)
ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
folder = u.ROOT / 'agents/continuation8_iii_weighted_units'
edits = r.table(folder / 'S6_SERIES_PUBLISH_LV_publication_defects.tsv')[1]
events = r.table(folder / 'S6_SERIES_PUBLISH_LV_CHECK_EVENTS.tsv')[1]
assert (len(edits), len(events)) == (453, 2)
for row in edits:
    assert not any(x['change_id'] == row['change_id'] for x in ds)
    out = {k: row.get(k, '') for k in df}
    out['review_status'] = row.get('review_status', '') + '; full attributed review admitted ' + now + '; actual LV boundary held: ' + note
    ds.append(out)
for row in events:
    assert row['type'] == 'used and rechecked in this run'
    assert not any(x['event_id'] == row['event_id'] for x in es)
    out = {k: row.get(k, '') for k in ef}
    out['outcome'] = row['outcome'] + ' Root read the entire substantive review, all criteria, actual application output and actual following 02K9 boundary. All LV criteria remain open until that unit is relocated. No new independent credit. ' + note
    es.append(out)
ident = 'maps:src:D.2.53'
assert not any(x['paper'] == 'III' and x['unit_id'] == ident for x in ps)
for c in [f'D{i:02d}' for i in range(1, 28)] + ['structure']:
    row = {k: '' for k in pf}
    row.update(paper='III', unit_id=ident, unit_title='The weighted OS45 manifold',
               row_kind='structure' if c == 'structure' else 'defect',
               defect_type='' if c == 'structure' else c, status='open',
               date_utc=now, evidence=note,
               detail='Full source review admitted; all28 held because unheaded02K9 still follows LV. Actual complete subsection boundary and common/final PDF gates remain.')
    ps.append(row)
lp = [x for x in ps if x['paper'] == 'III' and x['unit_id'] == 'maps:src:D.2.48']
assert len(lp) == 28 and all(x['status'] == 'open' for x in lp)
closed = 0
for row in lp:
    c = row['defect_type'] or 'structure'
    done = c not in {'D04', 'D06', 'D09', 'D18'}
    row.update(status='done' if done else 'open', date_utc=now, evidence=note,
               detail='Full LP proof admitted earlier; complete LV subsection is now its actual successor. Four common gates and final PDF remain.')
    closed += done
assert closed == 24
r.write_table(r.DEFECTS, df, ds)
r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
print('UTC', now)
print('EXACT_DEFECT_ROWS', len(edits), 'ATTRIBUTED_USED_EVENTS', len(events))
print('SOURCE_CRITERIA_CLOSED', closed, 'NEW_ACTUAL_UNIT_ROWS', 28)
print('LV_ALL28_HELD_AT_ACTUAL_02K9_BOUNDARY; COMMON_AND_FINAL_PDF_GATES_OPEN')
