"""Record the actual duplicate J7 proof pending complete consolidation."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
now = datetime.now(timezone.utc).isoformat()
note = 'agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_extension_named_units_review.md'
pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
selected = [x for x in ps if x['paper'] == 'III' and x['unit_id'] == 'maps:src:B.3.1' and (x['defect_type'] or 'structure') in {'D12', 'structure'}]
assert len(selected) == 2 and all(x['status'] == 'done' for x in selected)
for row in selected:
    row.update(status='open', date_utc=now, evidence=note,
        detail='Whole later retained-angle proof and current J7 proof reveal the actual duplicate full proof. A complete seven-proof/four-subsection consolidation is staged, with every old identity and full family scope preserved, but final whole readback and canonical application remain pending.')
ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
eid = 'publish:c8:III:retained-angle-overlap-reopening'
assert not any(x['event_id'] == eid for x in es)
row = {k: '' for k in ef}
row.update(statement_id='maps:src:B.3.1', date='2026-11-25',
    who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',
    type='used and rechecked in this run',
    outcome='Whole retained-angle input and current J7 proof, complete J7/03AE/03BD/03BC/03BE comparisons, and bounded J5 circle-framing owner read. The duplicate J7 proof requires D12/structure reopening. The staged consolidation retains the full original/admissible |p|=1 scope, all old formula aliases and auxiliary framings, with one shared Q255 smoothing owner and later Q257 comparison pending. No staged identity check gives proof-completion credit.',
    event_id=eid, phase='continuation8 publication overlap review', source_file=note,
    source_event_type='used and rechecked in this run', evidence_group=eid, date_utc=now, where=note)
es.append(row)
with (u.ROOT / note).open('a', newline='\n') as f:
    f.write('\n## Retained-angle full-proof overlap reopened\n\n' + now + ' UTC. Root has read the entire later retained-angle input and the complete current J7 proof, together with all five complete historical comparisons. The later text is a second full proof of J7. The earlier D12/structure closure did not account for that remaining copy and is reopened. A 950-line four-subsection retained unit and 280-line earlier quotient unit are staged with all old identities and complete family scope preserved; they have no completion credit until whole final readback, the Q255/Q257 owner placements and actual canonical application. The earlier Q011/J8/J9 material remains at its canonical position. No rekey or tag count is progress.\n')
r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
print('UTC', now)
print('TWO_SOURCE_CRITERIA_REOPENED; ONE_USED_EVENT; STAGED_REWRITE_HAS_NO_COMPLETION_CREDIT')
