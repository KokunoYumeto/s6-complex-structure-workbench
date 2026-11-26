#!/usr/bin/env python3
"""Record exposed whole readings of three newly formalized statements."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv

ROOT = Path(__file__).resolve().parents[1]
REL = Path('agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_formal_publication_CHECK_EVENTS.tsv')
OUT = ROOT / REL
assert not OUT.exists()
FIELDS = ['statement_id','date','who','type','outcome','event_id','phase',
          'source_file','source_row','source_event_type','evidence_group',
          'publish_input_file','publish_input_row','date_utc','where']
WHO = 'GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed'
TYPE = 'used and rechecked in this run'
NOW = datetime.now(timezone.utc).isoformat()
ITEMS = [
    ('Q300','maps:def:complex-flag-threefold','elliptic_additive_profiles.tex',480,
     'The complete definition and its use in the complete three-component cusp proof were read. The incidence variety, its two projections and complex orientation are the existing flag model used in the admitted proof; formalizing the definition preserves that model.',
     'S6_SERIES_PUBLISH_III_additive_publication_review.md'),
    ('Q301','maps:rem:natural-sphere-sector-scope','limits_and_open_points.tex',3,
     'The complete remark was read after its exact relocation from the completed sphere synthesis. The V=0 map and inverse are the identity on the line, linearization and marked filling; the 226-row, g>1, homology and smooth-classification scopes retain their cited theorem hypotheses. The whole unchanged LG receiver was also read. Final structural placement of the limits unit remains a separate root gate.',
     'S6_SERIES_PUBLISH_III_spheres_publication_review.md'),
    ('Q302','maps:def:marked-filling-pattern','elliptic_sphere_outputs.tex',1780,
     'The complete definition and the complete sixteen-profile theorem and proof were read. Its ordered profile, section pair, zero position and permitted additive choices preserve the proved 59 patterns on 50 rows; logarithmic orders and affine powers remain parameters of each specified filling.',
     'S6_SERIES_PUBLISH_III_spheres_publication_review.md'),
]
rows = []
for tag, label, name, line, scope, review in ITEMS:
    source = Path('agents/continuation8_iii_integration/units/later') / name
    text = (ROOT/source).read_text()
    assert text.count('\\label{' + label + '}') == 1
    assert text.count('\\hypertarget{tag-' + tag + '}') == 1
    assert '\\label{' + label + '}' in text.splitlines()[line-1]
    rows.append(dict(statement_id=label,date=NOW[:10],who=WHO,type=TYPE,
        outcome=scope + ' This records an exposed source-local publication recheck only, with no independent proof, prior-computation, global-reference, bibliography or rendered-page credit.',
        event_id='publish:c8:III:' + tag + ':formal-publication-recheck',
        phase='continuation8-later-publication',source_file=str(source),source_row=line,
        source_event_type=TYPE,evidence_group='publish:c8:III:later-unit-editing',
        publish_input_file=str(REL),publish_input_row=len(rows)+2,date_utc=NOW,
        where='agents/continuation8_iii_later/' + review))
with OUT.open('w',newline='') as handle:
    writer = csv.DictWriter(handle,fieldnames=FIELDS,delimiter='\t',lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print('UTC', NOW)
print('EVENTS', len(rows), 'Q300 Q301 Q302', TYPE)
print('OUTPUT', str(REL), len(OUT.read_text().splitlines()), sha256(OUT.read_bytes()).hexdigest())
print('NO_SHARED_WRITES; NO_INDEPENDENT_PROOF_CREDIT; FINAL_PLACEMENT_SEPARATE')
