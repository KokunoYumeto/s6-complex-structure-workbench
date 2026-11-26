#!/usr/bin/env python3
"""Record the completed human-attributed whole-source sphere publication read."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from collections import Counter
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation8_iii_later'
SOURCE = ROOT / 'agents/continuation8_iii_integration/units/later/elliptic_sphere_outputs.tex'
LIMITS = ROOT / 'agents/continuation8_iii_integration/units/later/limits_and_open_points.tex'
text = SOURCE.read_text()
assert sha256(SOURCE.read_bytes()).hexdigest() == '06701c891bda896a6cd8b5cd1c2a6e35066a5be8b9a2696f1b9cad6d7b748702'
assert sha256(LIMITS.read_bytes()).hexdigest() == '677c2e6ef0539073d4de046c0387c5bb25a068c65d3f88cc159f375983ecdb5c'
assert text.count('\\begin{proof}') == text.count('\\end{proof}') == 5
assert text.count('\\subsection{') == 5
assert text.count('\\begin{equation}') == text.count('\\end{equation}') == 30
assert not re.search(r'\\tag\{', text)
ids = re.findall(r'\\label\{([^}]+)\}', text)
assert all(v == 1 for v in Counter(ids).values())
now = datetime.now(timezone.utc).isoformat()
defects = OUT / 'S6_SERIES_PUBLISH_III_spheres_publication_defects.tsv'
with defects.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
assert len(rows) == 138
for row in rows:
    row['review_status'] = ('whole repaired input, whole final source, five complete admitted comparisons, '
                            'all exact differences and every local row read; source-local complete; '
                            'root admission, final placement and global build gates pending')
with defects.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)

events = OUT / 'S6_SERIES_PUBLISH_III_spheres_publication_CHECK_EVENTS.tsv'
assert not events.exists(), 'do not overwrite an existing event packet'
event_fields = ['statement_id','date','who','type','outcome','event_id','phase','source_file',
                'source_row','source_event_type','evidence_group','publish_input_file',
                'publish_input_row','date_utc','where']
scopes = [
    ('02KZ','maps:src:D.2.24','All eight rows, both original caps, every affine reflection offset, full boundary maps and the degree-one refinement right inverse remain.'),
    ('02L0','maps:src:D.2.25','All 62 rows, every free regular-log vector and finite site list, original-cap bridge, integral extensions, CRT inverses, specified-fan transport and all even-M oriented suspension cases remain.'),
    ('02L1','maps:src:D.2.26','All 59 patterns on 50 rows, every stated finite affine lift and unrestricted delta coefficient, regular vectors, full cap maps, CRT/root inverses and c=1 smooth reconstruction remain.'),
    ('02L2','maps:src:D.2.27','All sixteen rows and permitted fillings, the two conductor lattices, torsion-sensitive indices, additional transitive roots, order-18 example and exact two-primary obstructions remain.'),
    ('02L3','maps:src:D.2.28','All twenty-one profile conclusions, 59/50 counts, twelve unbounded families and exact oriented sphere maps remain. Its later scope overview moves with an exact inverse relocation to Q301; it is not a later premise of this proof.'),
]
with events.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    for index, (tag, sid, scope) in enumerate(scopes, 2):
        source_row = text[:text.index('\\label{' + sid + '}')].count('\n') + 1
        writer.writerow(dict(statement_id=sid, date=now[:10],
            who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
            type='used and rechecked in this run',
            outcome=('Complete repaired proof read against its complete admitted original/receiving comparison; '
                     'complete final source, all exact edits and all D01-D27 plus actual source structure inspected. '
                     + scope + ' This is source-local publication rechecking, with no new independent-proof '
                     'or inherited computation credit. Root admission, actual final placement, global links, '
                     'bibliography, counters and rendered-page reading remain separate.'),
            event_id='publish:c8:III:' + tag + ':publication-unit', phase='continuation8-later-publication',
            source_file=str(SOURCE.relative_to(ROOT)), source_row=source_row,
            source_event_type='used and rechecked in this run', evidence_group='publish:c8:III:later-unit-editing',
            publish_input_file=str(events.relative_to(ROOT)), publish_input_row=index, date_utc=now,
            where='agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_spheres_publication_review.md'))

print('UTC', now)
print('FROZEN_SOURCE', len(text.splitlines()), sha256(SOURCE.read_bytes()).hexdigest())
print('LOCAL_DEFECTS', len(rows), dict(sorted(Counter(row['type'] for row in rows).items())))
print('LOCAL_EVENTS', len(scopes), 'NO_SHARED_WRITES; NO_NEW_MATHEMATICAL_EXECUTION_CREDIT')
for name in ['S6_SERIES_PUBLISH_III_spheres_publication_review.md',
             'S6_SERIES_PUBLISH_III_spheres_actual_units.md',
             defects.name, events.name]:
    path = OUT / name
    print('PACKET', name, len(path.read_text().splitlines()), sha256(path.read_bytes()).hexdigest())
