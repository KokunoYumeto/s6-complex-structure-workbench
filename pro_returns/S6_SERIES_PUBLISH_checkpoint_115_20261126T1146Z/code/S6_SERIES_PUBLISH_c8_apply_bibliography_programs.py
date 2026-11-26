"""Apply the wholly reviewed bibliography and one final plain-path programs table."""
from collections import Counter
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now = datetime.now(timezone.utc).isoformat()
source = u.repairs.SOURCE.read_text(encoding='utf-8')
boundary = source.index(r'\begin{thebibliography}')
old_bib = source[boundary:]
new_bib = (u.WORK/'root/bibliography.tex').read_text(encoding='utf-8')
programs = (u.WORK/'root/programs_table.tex').read_text(encoding='utf-8')
assert len(old_bib.splitlines()) == 695
assert len(new_bib.splitlines()) == 449
assert len(programs.splitlines()) == 444
assert source.count(r'\section{Programs}') == 0
candidate = source[:boundary] + programs + '\n\\clearpage\n' + new_bib
u.check_permanent_identifiers(source, candidate, set(), set())
bkeys = re.findall(r'\\bibitem(?:\[[^\n]*\])?\{([^{}]+)\}', new_bib)
assert len(bkeys) == len(set(bkeys))
uses = set()
for group in re.findall(r'\\cite[a-zA-Z*]*(?:\[[^\]]*\]){0,2}\{([^{}]+)\}', source[:boundary]):
    uses.update(x.strip() for x in group.split(','))
assert uses <= set(bkeys), sorted(uses-set(bkeys))
paths = re.findall(r'\\nolinkurl\{([^{}]+)\}', programs)
assert len(paths) == len(set(paths)) == 181
assert r'\href' not in programs and r'\url' not in programs
assert 'code/' not in source[:boundary]
df, ds = r.table(r.DEFECTS)
folder = u.ROOT/'agents/continuation8_iii_later'
bib_rows = r.table(folder/'S6_SERIES_PUBLISH_III_bibliography_publication_defects.tsv')[1]
program_rows = r.table(u.ROOT/'agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_III_programs_table_defects.tsv')[1]
assert len(bib_rows) == 74 and len(program_rows) == 53
for row in bib_rows:
    assert old_bib.count(row['old_text']) == 1, (row['change_id'], 'old bibliography guard')
    assert new_bib.count(row['new_text']) == 1, (row['change_id'], 'new bibliography owner')
for row in bib_rows + program_rows:
    assert not any(x['change_id'] == row['change_id'] for x in ds)
    out = {k: row.get(k, '') for k in df}
    out['review_status'] += '; canonical admission at ' + now + '; root read complete final source and substantive review; actual program/source-reading attribution preserved; final PDF gate remains'
    ds.append(out)
placement = 'III-C8-PLACE-FINAL-PROGRAMS-BIBLIOGRAPHY'
assert not any(x['change_id'] == placement for x in ds)
ds.append(dict(change_id=placement, type='D14', statement_id='mapsIII:programs; series:III:bibliography', old_location='canonical final clearpage/bibliography boundary', old_page='unbuilt intermediate source', new_location='same boundary: Programs then References', new_page='pending final PDF', old_text='\\clearpage\n\\begin{thebibliography}{99}', new_text='\\clearpage\n'+programs+'\n\\clearpage\n\\begin{thebibliography}{99}', reason='Place the one complete181-path programs table after final mathematical problems and before the whole449-line bibliography. All old mathematical text and literal identities are preserved; exact bibliography entries and all program preparations/refinements have their own rows.', review_status='whole444-line table,766-line substantive review,449-line bibliography and420-line review read by root; no proof/criterion increment from placement'))
ef, es = r.table(u.ROOT/'CHECK_EVENTS.tsv')
events = r.table(folder/'S6_SERIES_PUBLISH_III_bibliography_publication_CHECK_EVENTS.tsv')[1]
assert len(events) == 19
for row in events:
    assert row['type'] == 'used and rechecked in this run'
    assert not any(x['event_id'] == row['event_id'] for x in es)
    out = {k: row.get(k, '') for k in ef}
    out['outcome'] += ' Root read complete substantive review, all final bibliography lines and this actual event payload; admitted with canonical bibliography at ' + now + '.'
    es.append(out)
for key, detail, note in [
 ('III:programs-table', 'Read all444 final lines, entire766-line review, all53 defect reasons and complete19 final purpose/reference edits. Retain exact181 paths/121 rows,31 transported sources plus literal residual source, thirteen location-dependent input maps, eighteen byte identities, actual helper scopes and both KN external digest-checked inputs. No mathematical program rerun or new old-byte reading is claimed.', 'agents/continuation8_iii_weighted_units/S6_SERIES_PUBLISH_III_programs_table_review.md'),
 ('III:bibliography-final', 'Read complete449-line final bibliography, complete420-line review, all74 exact edit reasons and19 actual event payloads; actual bibliography editor/record stdout and empty outer stderr read. Each74 old entry guard occurs uniquely in current canonical old bibliography and each new owner in final bibliography. Every actually used citation key has its unique final entry.', 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_bibliography_publication_review.md')]:
    eid = 'publish:c8:III:final-apparatus:' + key
    assert not any(x['event_id'] == eid for x in es)
    out = {k: '' for k in ef}
    out.update(statement_id=key, date='2026-11-25', who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root', type='used and rechecked in this run', outcome=detail+' Canonical text applied; no independent/required proof, new final page or unit criterion credit.', event_id=eid, phase='continuation8 final programs and bibliography', source_file=note, source_event_type='used and rechecked in this run', evidence_group=eid, date_utc=now, where=note)
    es.append(out)
u.repairs.SOURCE.write_text(candidate, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
r.write_table(u.ROOT/'CHECK_EVENTS.tsv', ef, es)
print('UTC', now, 'BIBLIOGRAPHY_EDITS', len(bib_rows), 'PROGRAM_EDITS', len(program_rows), 'PLACEMENT_ROW', 1)
print('ATTRIBUTED_USED_EVENTS', len(events), 'ROOT_USED_EVENTS', 2, 'CITATION_KEYS', len(uses), 'BIB_ENTRIES', len(bkeys), 'UNIQUE_PROGRAM_PATHS', len(paths))
print('ACTUAL_START_BOUNDARY\n'+candidate[boundary-180:boundary+220])
b = candidate.index(r'\begin{thebibliography}')
print('ACTUAL_END_BOUNDARY\n'+candidate[b-260:b+120])
print('ALL_OLD_IDENTITIES_AND_MATHEMATICAL_BODY_BYTES_PRESERVED; NO_CRITERION_INCREMENT')
