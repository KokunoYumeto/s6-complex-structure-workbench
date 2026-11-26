"""Admit completed whole sections and their exact previously pending source gates."""
from collections import Counter
from datetime import datetime, timezone
import re
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

now = datetime.now(timezone.utc).isoformat()
note = 'agents/continuation8_iii_root/S6_SERIES_PUBLISH_III_final_apparatus_admission.md'
source = u.repairs.SOURCE.read_text(encoding='utf-8')
for key in ['preamble','bibliography','programs_table']:
    fragment = (u.WORK/'root'/(key+'.tex')).read_text(encoding='utf-8')
    assert source.count(fragment) == 1, key
body = source[source.index(r'\begin{document}'):]
labels = set(re.findall(r'\\label\{([^{}]+)\}', source))
refs = []
for group in re.findall(r'\\(?:ref|eqref|cref|Cref|autoref|pageref)\*?\{([^{}]+)\}', body):
    refs.extend(x.strip() for x in group.split(','))
assert not set(refs)-labels
pf, ps = r.table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv')
front = {'the-series-and-this-paper','series:III:main-theorems','the-proofs-in-outline','known-and-new','methodology','how-the-paper-is-organized'}
closed = Counter()
for row in ps:
    if row['paper'] != 'III' or row['status'] != 'open':
        continue
    kind = row['defect_type']
    selected = kind in {'D04','D06','D09'} or (kind == 'D18' and row['unit_id'] not in front)
    if selected:
        row.update(status='done', date_utc=now, evidence=row['evidence']+'; '+note, detail=row['detail']+' Final common source hold completed after complete reference, bibliography and program-table admission; exact scope and separate final gates in the appended review.')
        closed[kind] += 1
assert closed == Counter(D04=109,D06=109,D09=100,D18=103), closed
for ident,title in [('programs','Programs'),('references','References')]:
    assert not any(x['paper']=='III' and x['unit_id']==ident for x in ps)
    for kind in [f'D{i:02d}' for i in range(1,28)]+['']:
        ps.append(dict(paper='III',unit_id=ident,unit_title=title,row_kind='defect' if kind else 'structure',defect_type=kind,status='done',date_utc=now,evidence=note,detail='Actual complete section, with full source and substantive comparison read; criterion-specific findings in root review. New registration supplies no title/helper/proof credit; these completed source criteria follow the whole-section assessment. Actual PDF and joint gates remain separate.'))
ef, es = r.table(u.ROOT/'CHECK_EVENTS.tsv')
for ident in ['III:common-reference-bibliography-program-gates','programs','references']:
    eid = 'publish:c8:III:final-apparatus-admission:'+ident
    assert not any(x['event_id']==eid for x in es)
    event = {k:'' for k in ef}
    event.update(statement_id=ident,date='2026-11-25',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; continuation eight root',type='used and rechecked in this run',outcome='Whole final source/reviews and exact actual outputs read; complete criterion-by-criterion section assessment and existing common-hold resolution in '+note+'. No new independent/required proof, program execution or rendered-page credit.',event_id=eid,phase='continuation8 final whole-source apparatus admission',source_file=note,source_event_type='used and rechecked in this run',evidence_group=eid,date_utc=now,where=note)
    es.append(event)
r.write_table(u.ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv',pf,ps)
r.write_table(u.ROOT/'CHECK_EVENTS.tsv',ef,es)
current = [x for x in ps if x['paper']=='III']
print('UTC',now,'EXISTING_CRITERIA_CLOSED',dict(closed),'NEW_ACTUAL_SECTIONS',2,'WHOLE_SECTION_CRITERIA',56)
print('III_DONE',sum(x['status']=='done' for x in current),'III_OPEN',sum(x['status']=='open' for x in current),'III_ROWS',len(current),'III_ACTUAL_UNITS',len(set(x['unit_id'] for x in current)))
for row in current:
    if row['status']=='open': print('REMAINING',row['unit_id'],row['defect_type'])
print('ACTUAL_BUILD_ALL_PAGES_FINAL_COUNTS_PROVENANCE_RECORDS_AND_JOINT_GATES_REMAIN')
