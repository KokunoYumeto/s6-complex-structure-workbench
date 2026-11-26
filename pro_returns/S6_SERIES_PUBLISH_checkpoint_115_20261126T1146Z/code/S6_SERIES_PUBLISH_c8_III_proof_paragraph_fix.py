"""Initialize the two read proof-list items before their run-in headings."""
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
from S6_SERIES_PUBLISH_c8_III_remaining_layout_repairs import unit_for
from S6_SERIES_PUBLISH_c8_III_check_counts import parse_statements

now = datetime.now(timezone.utc).isoformat()
source = u.repairs.SOURCE.read_text(encoding='utf-8')
owners, _, _ = parse_statements(source)
specs = [
    ('night:P3F.26', 'later/os49_construction.tex', 'The source and its line.'),
    ('night:P3F.34', 'later/os49_graph_caps.tex', 'The fixed exterior and the oriented boundary circle.'),
]
assert len(re.findall(r'\\begin\{proof\}\s*\\paragraph\{', source)) == 2
df, ds = r.table(r.DEFECTS)
ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
candidate = source
updates = []
reason = ('Pass04 stops at the second paragraph with Improper prevdepth. The installed amsthm proof opens a trivlist/item whose everypar clears newlist; an immediate run-in paragraph replaces that hook before it runs, leaving paragraph termination suppressed. Inserting leavevmode first runs that pending item hook. Root read the exact installed proof/list/section/addpenalty code and both source contexts. No mathematical text, heading, label or target changes; deleting this exact inserted command recovers the old proof start.')
for index, (sid, rel, heading) in enumerate(specs, 1):
    old = '\\begin{proof}\n\\paragraph{' + heading + '}'
    new = old.replace('\\begin{proof}\n', '\\begin{proof}\n\\leavevmode\n', 1)
    assert source.count(old) == 1
    position = source.index(old)
    owner = [row for row in owners if row.start <= position < row.stop]
    assert len(owner) == 1 and owner[0].statement_id == sid
    path = u.WORK / rel
    previous = path.read_text(encoding='utf-8')
    assert previous.count(old) == 1
    updates.append((path, previous.replace(old, new, 1)))
    candidate = candidate.replace(old, new, 1)
    row = unit_for(source, position, ps)
    row.update(status='open', date_utc=now, evidence='code/S6_SERIES_PUBLISH_c8_III_proof_paragraph_fix.py; code/S6_SERIES_PUBLISH_c8_tex_final_build_notes.md', detail='Actual proof-item/run-in-heading failure repaired by initialization; current compilation and Proof/title spacing require final rendered verification.')
    ident = f'III-C8-TEX-P04-PROOF-PARAGRAPH-{index:02d}'
    assert not any(item['change_id'] == ident for item in ds)
    ds.append(dict(change_id=ident, type='D23', statement_id=sid, old_location='proof beginning and first paragraph heading', old_page='incomplete pass04; first failure after provisional545', new_location='same proof beginning with item initialized', new_page='pending successful build and visual reading', old_text=old, new_text=new, reason=reason, review_status='bounded root installed-code and both source-context reading ' + now + '; final layout/page remains open'))
    print('EXACT_OLD\n' + old + '\nEXACT_NEW\n' + new + '\nOWNER ' + sid + ' UNIT ' + row['unit_id'])
u.check_permanent_identifiers(source, candidate, set(), set())
eid = 'publish:c8:III:tex-pass04-proof-paragraph'
assert not any(row['event_id'] == eid for row in es)
event = {key: '' for key in ef}
event.update(statement_id='III:layout-pass04-proof-paragraph', date='2026-11-25', who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root and tex_runtime reviewer', type='used and rechecked in this run', outcome=reason + ' Runtime reviewer also read both complete owning theorem statements. No proof, required, independent, clean-build or visual-page credit is added.', event_id=eid, phase='continuation8 actual TeX repairs', source_file='code/S6_SERIES_PUBLISH_c8_III_proof_paragraph_fix.py', source_event_type='used and rechecked in this run', evidence_group=eid, date_utc=now, where='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass04.log')
es.append(event)
for path, content in updates:
    path.write_text(content, encoding='utf-8', newline='\n')
u.repairs.SOURCE.write_text(candidate, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
print('APPLIED_UTC', now, 'EXACT_EDITS', len(updates))
