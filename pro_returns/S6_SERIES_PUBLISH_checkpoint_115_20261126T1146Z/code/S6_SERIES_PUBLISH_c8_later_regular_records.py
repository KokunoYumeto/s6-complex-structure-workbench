#!/usr/bin/env python3
"""Record completed exposed 039U reading and bounded dependency follow-ups."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'agents/continuation8_iii_later'
regular = ROOT / 'agents/continuation8_iii_integration/units/root/regular_quotients.tex'
carriers = ROOT / 'agents/continuation8_iii_integration/units/later/further_cusp_carriers.tex'
metrics = ROOT / 'agents/continuation8_iii_integration/units/later/fixed_target_metrics.tex'
kummer = ROOT / 'agents/continuation8_iii_integration/units/root/local_kummer.tex'
for path, expected in [
    (regular, '0052514d908a0fd8cd945395953bb01e3ac269bd6cb060cc48fe33cbd971762a'),
    (carriers, '7ff5743e27b8ccac6d5256ff73dd457b18549fe4f482b6cd22dccaf44f8ae2f7'),
    (metrics, '8be29e790bcbdb2ce289d6ce57d9adaa54bd3190ff0b4f13255013325dd7fdb0'),
]:
    text = path.read_text()
    assert hashlib.sha256(text.encode()).hexdigest() == expected
    print('Read source', path.name, len(text.splitlines()), expected)

defects = out / 'S6_SERIES_PUBLISH_III_regular_publication_defects.tsv'
with defects.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
assert len(rows) == 33
for row in rows:
    row['review_status'] = 'exact old/new fields and complete owning proof read; final changed passages read; exposed source-local publication review only; root placement/reference/render gates remain'
with defects.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)

event_path = out / 'S6_SERIES_PUBLISH_III_regular_publication_CHECK_EVENTS.tsv'
event_fields = ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
stamp = datetime.now(timezone.utc).isoformat()
readings = [
    (regular, 'Q310', 'mapsIII:def:regular-quotient-data', 'Whole numbered data read against the original fixed three-fibre family, same marking and unrescaled metric; no parameter restriction introduced.'),
    (regular, 'Q311', 'mapsIII:lem:collapsed-subset-distance', 'Whole statement and full generic proof read; the exact proof is relocated from 036J. The quotient distance, length, quotient topology and off-basepoint inverse are retained.'),
    (regular, '039U', 'wb:cusp-spec-globalization-obstruction', 'Whole 926-line input, entire 131-line prior comparison, entire 994-line first rewrite and all five final refinements read. All invariant, radial, finite-cap, normalization, cusp and sphere clauses retained; exact cover, period, rotation and compactification maps displayed.'),
    (carriers, '036J', 'wb:cusp-cone-angle-forgotten-sphere-carriers', 'Bounded follow-up after the prior whole-proof publication reading: full generic proof moved to earlier Q311 and replaced by all four exact quotient identity maps/inverses. The successive-collapse and whole-ball proofs remain unchanged.'),
    (metrics, 'Q30X', 'mapsIII:lem:fixed-conical-metrics', 'Bounded follow-up after the prior whole-proof publication reading: the same explicit identity-quotient application now cites Q311 as its sole proof owner; every tensor, construction and metric estimate remains unchanged.'),
    (metrics, 'Q30Y', 'mapsIII:rem:source-and-moving-metrics', 'Bounded follow-up after the prior whole-remark publication reading: the shared distance formula cites Q311 and the native period estimates still cite 036J. All maps and bounds remain unchanged.'),
    (kummer, '02K6', 'maps:src:C.1.5', 'Bounded support review requested by root: the complete current statement/proof at lines 478-600 was read to identify the finite-flat-normal owner used by Q30U. Item 3 gives the explicit fractional-monomial free basis and unique overlap extensions. No full local-Kummer-unit review is claimed.'),
]
events = []
for path, tag, sid, detail in readings:
    text = path.read_text()
    line = text[:text.index(r'\label{' + sid + '}')].count('\n') + 1
    events.append(dict(statement_id=sid, date=stamp[:10],
        who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
        type='used and rechecked in this run',
        outcome=detail + ' Exposed reading only; no independent derivation, historical-output credit, required-row closure or global placement/render credit.',
        event_id='publish:c8:III:' + tag + ':regular-publication-recheck',
        phase='continuation8-later-publication', source_file=str(path.relative_to(ROOT)),
        source_row=str(line), source_event_type='used and rechecked in this run',
        evidence_group='publish:c8:III:later-unit-editing',
        publish_input_file=str(event_path.relative_to(ROOT)), publish_input_row=str(len(events) + 2),
        date_utc=stamp, where='agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_regular_publication_review.md'))
with event_path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)
for path in (defects, event_path):
    assert b'\r' not in path.read_bytes()
print('Readings', len(events), 'exact edits', len(rows), 'at', stamp)
for match in re.finditer(r'\\begin\{(definition|lemma|theorem|proof)\}', regular.read_text()):
    print('Regular block', match[1], regular.read_text()[:match.start()].count('\n') + 1)
print('No manuscript, canonical table, criterion count or independent-check status changed by this recorder.')
