#!/usr/bin/env python3
"""Record the completed final-part scope reading and exact LG preservation."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'agents/continuation8_iii_integration/units/later/limits_and_open_points.tex'
out = ROOT / 'agents/continuation8_iii_later'
s = source.read_text()
receiver = (ROOT / 'agents/continuation8_iii_lg_receiving/S6_SERIES_PUBLISH_III_02LG_receiving.tex').read_text()
first = 'Determine the marked integral cap maps and oriented smooth types in'
def mathematical_problem(text):
    start = text.index(first)
    end = text.index(r'\end{problem}', start) + len(r'\end{problem}')
    return text[start:end]
assert mathematical_problem(s) == mathematical_problem(receiver)
defects = out / 'S6_SERIES_PUBLISH_III_limits_publication_defects.tsv'
with defects.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    row['review_status'] = 'whole 191-line input, complete 217-line final part and every exact edit row read; actual root assembly and global gates remain'
with defects.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
event_path = out / 'S6_SERIES_PUBLISH_III_limits_publication_CHECK_EVENTS.tsv'
fields = ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
stamp = datetime.now(timezone.utc).isoformat()
owners = [
    ('Q301','maps:rem:natural-sphere-sector-scope','Complete scope remark read against the completed sphere and finite-cap comparisons: V=0 identity, 226 vertical rows, g>1 group obstruction and established finite/smooth sectors retained.'),
    ('Q30Z','mapsIII:problem:degree-zero-lines-and-multiplicities','Complete new open problem read against the exact removed KX scope paragraph: general degree-zero lines and multiplicity question preserved, identity maps on both marked section-line specializations explicit. Engel page expansion remains root D18 work.'),
    ('Q30U','mapsIII:problem:finite-cusp-cover-compactification','Complete open problem read: M>1 local cover, additional branch values, normalization/resolution of all pulled-back fibres, lifted metric, total topology and sphere question retained together; M=1 is the proved identity endpoint.'),
    ('Q30V','mapsIII:problem:raw-conical-quotient-classes','Complete open problem read: both exact raw maps and homotopy groups retained; specified target postcompositions yield the proved zero classes, without assigning either raw class a value.'),
    ('02LG','maps:src:D.2.4','Whole final LG mathematical problem and synthesis read; exact equality to the admitted receiving mathematical block verified. All four open sectors, 495/459 scopes, 162-pattern residual table, h=1/c=0 frame scope and OS45 parity/link values preserved.'),
]
events = []
for tag, sid, detail in owners:
    events.append(dict(statement_id=sid, date=stamp[:10], who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
        type='used and rechecked in this run', outcome=detail+' Exposed final-part publication reading; no new independent check, no proof claim for an open problem, and no root assembly/render/global-reference credit.',
        event_id='publish:c8:III:'+tag+':final-part-publication-recheck', phase='continuation8-later-publication', source_file=str(source.relative_to(ROOT)),
        source_row=str(s[:s.index(r'\label{'+sid+'}')].count('\n')+1), source_event_type='used and rechecked in this run',
        evidence_group='publish:c8:III:later-unit-editing', publish_input_file=str(event_path.relative_to(ROOT)), publish_input_row=str(len(events)+2), date_utc=stamp,
        where='agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_limits_publication_review.md'))
with event_path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)
print('LG mathematical block identical to admitted receiver:', len(mathematical_problem(s).splitlines()), 'lines')
print('Final scope events', len(events), 'recorded', stamp)
print('Local defects', len(rows), 'all final-part tables use LF; no canonical/shared updates or criterion credit.')
