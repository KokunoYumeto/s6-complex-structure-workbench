"""Repair the observed radial split and state the verified records destination."""
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
from S6_SERIES_PUBLISH_c8_III_check_counts import parse_statements

now = datetime.now(timezone.utc).isoformat()
source = u.repairs.SOURCE.read_text(encoding='utf-8')
owners, _, _ = parse_statements(source)
needle = r' Z_H&=L_q-\log|ac|,&Z_K&=\log|a^3c^2|,'
assert source.count(needle) == 1
position = source.index(needle)
start = source.rfind(r'\begin{split}', 0, position)
stop = source.index(r'\end{split}', position) + len(r'\end{split}')
old_split = source[start:stop]
assert old_split.count('&') == 7
owner = [row for row in owners if row.start <= position < row.stop]
assert len(owner) == 1 and owner[0].statement_id == 'night:P3F.31'
new_split = old_split.replace(r'\begin{split}', r'\begin{aligned}', 1).replace(r'\end{split}', r'\end{aligned}', 1)
old_records = r'''The \href{\SsixPublishRecords}{records page for Paper~III} gives
the statement checks, provenance and programs. The repository
commit is \texttt{\SsixRepositoryCommit}.'''
new_records = r'''The standing address for statement checks, provenance and programs
is the \href{\SsixPublishRecords}{records page for Paper~III}.
The repository commit is \texttt{\SsixRepositoryCommit}.'''
assert source.count(old_records) == 1
changes = [
    ('III-C8-TEX-P05-RADIAL-SPLIT', 'D23', 'night:P3F.31', 'later/os49_graph_caps.tex', old_split, new_split,
     'Pass05 fails at end-split after page566. The first two rows each have two equality pairs and three outer alignment tabs. Aligned admits those pairs; only the two environment names change. Root read the complete radial matrix and following inverse/coorientation formulas. Runtime reviewer read all35 split blocks and found no other row with this outer-tab defect.'),
    ('III-C8-RECORDS-STANDING-ADDRESS', 'D18', 'methodology', 'root/front_matter.tex', old_records, new_records,
     'The exact prescribed page returns HTTP200 and the correct Paper III anchor, but its section still links checkpoint34. State the verified standing address without asserting present delivery of the current records/programs. The repository commit sentence and both prescribed macro occurrences are preserved. Submission-time updating remains a separate action; no publication has occurred.'),
]
df, ds = r.table(r.DEFECTS)
ef, es = r.table(u.ROOT / 'CHECK_EVENTS.tsv')
pf, ps = r.table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
candidate = source
updates = []
for ident, kind, sid, rel, old, new, reason in changes:
    assert not any(row['change_id'] == ident for row in ds)
    path = u.WORK / rel
    previous = path.read_text(encoding='utf-8')
    assert previous.count(old) == 1
    updates.append((path, previous.replace(old, new, 1)))
    candidate = candidate.replace(old, new, 1)
    ds.append(dict(change_id=ident, type=kind, statement_id=sid,
        old_location='radial-period display' if kind == 'D23' else 'section1.5 records sentence',
        old_page='incomplete pass05; no final PDF', new_location='same source location', new_page='pending converged PDF',
        old_text=old, new_text=new, reason=reason,
        review_status='exact root whole local reading ' + now + '; final build/PDF or provenance application remains open'))
    rows = [row for row in ps if row['paper'] == 'III' and row['unit_id'] == sid and row['defect_type'] == kind]
    assert len(rows) == 1, (sid, kind)
    rows[0].update(status='open', date_utc=now, evidence='code/S6_SERIES_PUBLISH_c8_III_radial_and_records_wording_fix.py', detail=reason + ' Successor build and final applicable gate remain.')
    print('EXACT_OLD\n' + old + '\nEXACT_NEW\n' + new + '\nOWNER ' + sid)
u.check_permanent_identifiers(source, candidate, set(), set())
eid = 'publish:c8:III:tex-radial-and-records-destination'
assert not any(row['event_id'] == eid for row in es)
event = {key: '' for key in ef}
event.update(statement_id='III:layout-and-records-destination', date='2026-11-25', who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root', type='used and rechecked in this run', outcome='Root read the complete radial split, surrounding collar/inverse formulas, current full methodology and actual prescribed-URL access output. The two exact repairs preserve all mathematical content and literal identities. Runtime all35-split syntax reading retains its bounded scope. The standing-address claim now agrees with the actually opened page; current-file delivery remains a submission action. No independent, required, mathematical-count or PDF-reading credit is added.', event_id=eid, phase='continuation8 layout and documentary repairs', source_file='code/S6_SERIES_PUBLISH_c8_III_radial_and_records_wording_fix.py', source_event_type='used and rechecked in this run', evidence_group=eid, date_utc=now, where='code/S6_SERIES_PUBLISH_c8_tex_III_final_pass05.log; code/S6_SERIES_PUBLISH_c8_III_provenance_links.stdout.txt')
es.append(event)
for path, text in updates:
    path.write_text(text, encoding='utf-8', newline='\n')
u.repairs.SOURCE.write_text(candidate, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
r.write_table(u.ROOT / 'CHECK_EVENTS.tsv', ef, es)
r.write_table(u.ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', pf, ps)
print('APPLIED_UTC', now, 'EXACT_EDITS', len(changes))
