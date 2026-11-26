#!/usr/bin/env python3
"""Record exposed whole readings and bounded prose edits; no criterion credit."""
from pathlib import Path
import csv
from datetime import datetime, timezone
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'agents/continuation8_iii_integration/units/later/fixed_target_metrics.tex'
out = ROOT / 'agents/continuation8_iii_later'
defects = out / 'S6_SERIES_PUBLISH_III_metrics_publication_defects.tsv'
s = source.read_text()
assert hashlib.sha256(s.encode()).hexdigest() == 'cdac69ea11588ca422a5a8e1efe02161c5d6dabc4452045442eca29ef40471cc'
with defects.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
for before, after, sid in [
    ('Retain one of the following slice and ambient metrics,', 'Choose one of the following slice and ambient metrics,', 'wb:sphere-metric-scaling-trichotomy'),
    ('Write the established period matrix and residual as', 'Write the period matrix and residual as', 'wb:sphere-metric-scaling-trichotomy'),
    ('the exact inherited markings are invertible', 'the markings are invertible', 'wb:sphere-metric-scaling-trichotomy'),
    ('define the actual slice markings', 'define the slice markings', 'wb:sphere-metric-scaling-trichotomy'),
    ('to the actual slices', 'to the slices', 'wb:sphere-metric-scaling-trichotomy'),
    ('boundary coordinate uses the established map', 'boundary coordinate uses the map', 'wb:sphere-metric-scaling-trichotomy'),
    ('the actual residual argument satisfies', 'the residual argument satisfies', 'wb:sphere-metric-scaling-trichotomy'),
    ('takes the straight chord to an actual\nambient path', 'takes the straight chord to an\nambient path', 'wb:sphere-metric-scaling-trichotomy'),
    ('The actual target path is', 'The target path is', 'wb:sphere-metric-scaling-trichotomy'),
    ('under the actual coordinate maps.', 'under the displayed coordinate maps.', 'wb:sphere-metric-scaling-trichotomy'),
    ('exhaustion apply without a further rate assumption.', 'exhaustion apply to these parameter values.', 'wb:sphere-metric-fixed-realization'),
    ('with the actual target slices.', 'with the target slices.', 'wb:cusp-cone-sharp-global-R4-scope'),
]:
    assert s.count(before) == 1, (before, s.count(before))
    row = s[:s.index(before)].count('\n') + 1
    rows.append(dict(type='D02/D08', statement_id=sid,
        old_location='fixed_target_metrics.tex bounded prose line ' + str(row), old_page='pending final concordance',
        new_location='same mathematical owner', new_page='pending final build', old_text=before, new_text=after,
        reason='State the displayed maps and proved parameter relation directly; no mathematical assertion or scope changes.',
        review_status='exact replacement read with its complete mathematical passage'))
    s = s.replace(before, after)
    print('PROSE', row, repr(before), '=>', repr(after))
source.write_text(s)
for row in rows:
    row['review_status'] = 'whole input, admitted comparison, complete first rewrite and all final changed passages read; source-local only; root placement/render/global-reference gates remain'
with defects.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)

event_path = out / 'S6_SERIES_PUBLISH_III_metrics_publication_CHECK_EVENTS.tsv'
event_fields = ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
stamp = datetime.now(timezone.utc).isoformat()
owner_rows = [
    ('Q30W','mapsIII:def:fixed-target-metric-data','Full numbered data read: fixed cusp interval, residual, target/source maps, period and angle markings with inverses.'),
    ('03DG','wb:sphere-metric-uniform-collapse','Whole admitted and final proof read; identical compact-parameter map transfer to 036W, Hausdorff formula, GH bound and fixed-ball distortion retained.'),
    ('Q30X','mapsIII:lem:fixed-conical-metrics','Complete construction/exact-form proof read against 03D6: all global extensions, full C core collar, all-T radial distance, product/fat-wedge maps, exact pullbacks and strict paths retained.'),
    ('03DC','wb:sphere-metric-scaling-trichotomy','Whole admitted and final proof read: every positive scale, all three beta regimes, inverse lattice/chart maps, every derivative order, whole-ball control, finite-positive gaps and fixed-vertex packing. Exact missing display closer repaired.'),
    ('03D6','wb:sphere-metric-fixed-realization','Whole original and revised statement/proof read: constructive clauses assigned Q30X; native beta=T or ell_T follows from 03DC through exact coordinate maps and inverse; all original limits/categories retained.'),
    ('03DH','wb:sphere-metric-unit-volume','Whole original and final proof read: exact volume scales and inverses; beta=T/sqrt(det Y_T) or 1 identifies the finite regime; compact torus limits and diameter obstruction retained.'),
    ('03DF','wb:sphere-metric-tangent-scope','Whole admitted and final proof read: suspension/join and C boundary quotient inverses, product collar, complete local homology bases, cone metrics/volume obstruction and compact blow-down retained.'),
    ('Q30Y','mapsIII:rem:source-and-moving-metrics','Full numbered remark read: exact differential kernels and source frame inverse, radial quotient maps and inverse representatives, midpoint distances and identity-map isometry obstruction.'),
    ('037J','wb:cusp-cone-sharp-global-R4-scope','Whole admitted and final proof read: earlier three realization maps with exact inverses, induced slice factors, compact-image bound, identity modulus, sphere-target collapse and finite-T diameter obstruction.'),
]
events = []
for tag, sid, detail in owner_rows:
    line = s[:s.index(r'\label{' + sid + '}')].count('\n') + 1
    events.append(dict(statement_id=sid, date=stamp[:10], who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
        type='used and rechecked in this run', outcome=detail + ' Exposed source-local publication reading only; no independent derivation, historical-output credit, required-row closure or global/render/placement credit.',
        event_id='publish:c8:III:' + tag + ':metrics-publication-recheck', phase='continuation8-later-publication',
        source_file=str(source.relative_to(ROOT)), source_row=str(line), source_event_type='used and rechecked in this run',
        evidence_group='publish:c8:III:later-unit-editing', publish_input_file=str(event_path.relative_to(ROOT)),
        publish_input_row=str(len(events) + 2), date_utc=stamp,
        where='agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_metrics_publication_review.md'))
with event_path.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(events)
print('Source', len(s.splitlines()), hashlib.sha256(s.encode()).hexdigest())
print('Local defects', len(rows), 'events', len(events), 'time', stamp)
for i, line in enumerate(s.splitlines(), 1):
    if line.startswith(r'\subsection'):
        print('Unit', i, line)
for path in (defects, event_path):
    assert b'\r' not in path.read_bytes()
print('All metric TSV rows use LF; no central tables or criterion counts changed.')
