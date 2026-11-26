"""Apply and record the fully read 33-key reference preamble, without gate credit."""
from collections import Counter
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now = datetime.now(timezone.utc).isoformat()
source = u.repairs.SOURCE.read_text(encoding='utf-8')
boundary = source.index(r'\begin{document}')
old = source[:boundary]
new = (u.WORK/'root/preamble.tex').read_text(encoding='utf-8')
local = u.ROOT/'agents/continuation8_tex_runtime/S6_SERIES_PUBLISH_c8_tex_reference_defects.tsv'
df, ds = r.table(r.DEFECTS)
rows = r.table(local)[1]
assert len(rows) == 22
replayed = old
for row in rows:
    assert not any(x['change_id'] == row['change_id'] for x in ds)
    assert replayed.count(row['old_text']) == 1, row['change_id']
    replayed = replayed.replace(row['old_text'], row['new_text'], 1)
assert replayed == new, 'Serialized exact edits reproduce complete fragment'
candidate = new + source[boundary:]
u.check_permanent_identifiers(source, candidate, set(), set())
uses = set(re.findall(r'\\SeriesRef(?:Text)?\{([^{}]+)\}', source[boundary:]))
definitions = re.findall(r'(?m)^\\expandafter\\def\\csname SRef@([^\s]+)\\endcsname', new)
assert len(definitions) == len(set(definitions)) == 33
assert set(definitions) == uses
assert candidate[len(new):] == source[boundary:]
note = 'code/S6_SERIES_PUBLISH_c8_tex_final_build_notes.md sections 6–7'
for row in rows:
    out = {k: row.get(k, '') for k in df}
    out['new_location'] = 'canonical III preamble; same exact used-key definition'
    out['review_status'] += '; whole final198-line fragment, all active guards and complete sections6–7 read by root; exact serialized replay and canonical application at ' + now + '; no source criterion or mathematical credit'
    ds.append(out)
ef, es = r.table(u.ROOT/'CHECK_EVENTS.tsv')
eid = 'publish:c8:III:final-reference-preamble'
assert not any(x['event_id'] == eid for x in es)
event = {k: '' for k in ef}
event.update(statement_id='III:reference-preamble', date='2026-11-25', who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root', type='used and rechecked in this run', outcome='Complete198-line final preamble, all22 exact defect rows and full source-bound external-reference review read. Removed entries are verified unused lookup syntax; exact serialized guards reproduce final33-key fragment. Initial application stopped before any source/shared write because its definition query also counted the macro dispatch parameter; the corrected query selects literal definition lines. Failed output/error retained. Actual body unchanged; no new proof, independent/required check, final build/page or unit completion credit.', event_id=eid, phase='continuation8 final reference presentation', source_file=note, source_event_type='used and rechecked in this run', evidence_group=eid, date_utc=now, where=note)
es.append(event)
u.repairs.SOURCE.write_text(candidate, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
r.write_table(u.ROOT/'CHECK_EVENTS.tsv', ef, es)
print('UTC', now, 'DEFECT_ROWS', len(rows), 'USED_REFERENCE_KEYS', len(uses), 'ROOT_USED_EVENTS', 1)
print('EXACT_22_GUARDS_REPLAYED; ALL_BODY_BYTES_AND_LITERAL_IDENTITIES_PRESERVED')
print('NO_CRITERION_OR_MATHEMATICAL_CREDIT')
print('ACTUAL_BOUNDARY\n' + candidate[len(new)-200:len(new)+180])
