"""Record only manually supplied observations of actually viewed sheets."""
from pathlib import Path
from datetime import datetime, timezone
import json,hashlib
A=Path(__file__).resolve().parents[1]
plan=json.loads((A/'II_95_layout_plan_06.json').read_text())
observations=json.loads((A/'II_QA_observations_06.json').read_text())
for row in plan['sheets']:
    key=str(row['sheet'])
    if key not in observations:
        continue
    assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()==row['sha256']
    row.update(actually_viewed=True,observation=observations[key],
       method='tools.view_image with explicit image output; manual visual inspection',
       layout_result='No clipping, missing glyphs, equation-label collision or margin overflow observed unless explicitly recorded in observation.')
count=sum(x['actually_viewed'] for x in plan['sheets'])
plan.update(recorded_utc=datetime.now(timezone.utc).isoformat(),
    inspected_sheets=count, inspected_pages=[p for s in plan['sheets'] if s['actually_viewed'] for p in s['pages']],
    inspection_state=f'{count} of {len(plan["sheets"])} sheets actually viewed; all other sheets remain uninspected.',
    mathematical_scope='This visual receipt adds no blind proof credit. Existing mathematics/source assessments retain their separate exact scopes.')
(A/'II_95_visual_QA_06.json').write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps({'sheets_viewed':count,'pages_viewed':len(plan['inspected_pages']),'complete_batch':count==len(plan['sheets'])}))
