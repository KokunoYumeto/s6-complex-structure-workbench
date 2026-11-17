#!/usr/bin/env python3
"""Record direct visual inspection of the assigned immutable build-44 pages."""
from pathlib import Path
from datetime import datetime, timezone
import json
ROOT=Path(__file__).resolve().parents[2]
groups={
31:[361,363,364,365,367,368,369,370],
32:[372,373,375,376,378,379,382,383],
33:list(range(384,392)),
34:list(range(392,400)),
35:list(range(400,408)),
36:[408,409,410,412,413,414,415,417],
37:[418,419,421,422,425,428,429,430],
38:list(range(431,439)),
39:[439,440,441,442,443,449,456]
}
pages=[p for g in groups.values() for p in g]
assert len(pages)==71 and len(set(pages))==71
data={
 'utc':datetime.now(timezone.utc).isoformat(),
 'reviewer':'fourfold',
 'build':'immutable build44, checkpoint11, 456-page master',
 'status':'PASS',
 'method':'Direct image-tool visual inspection of all nine contact sheets and four full-size pages.',
 'contact_sheets':{str(k):v for k,v in groups.items()},
 'page_count_reviewed':len(pages),
 'full_size_pages':[390,437,443,456],
 'findings':{
   'clipping':'None observed.',
   'collisions':'None observed.',
   'missing_symbols':'None observed.',
   'malformed_equations':'None observed.',
   'dense_displays':'Pages390 and437 remain readable with aligned formulas and complete margins.',
   'tables_and_endmatter':'Page443 direct-image table and page456 final bibliography render cleanly.'
 },
 'scope':'Visual layout review only; no mathematical claim is promoted by this record.'
}
(ROOT/'records/checkpoint11_visual_fourfold.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+data['utc']+' — Opened own checkpoint11 render contact sheets31–39 and full-size pages390,437,443,456. Reason: assigned direct visual QA. Material: layout only; 71 rendered pages reviewed, no clipping/collision/missing glyph/malformed equation observed. Full record checkpoint11_visual_fourfold.json.\n')
print(json.dumps(data,indent=2))
