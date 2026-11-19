from datetime import datetime, timezone
from pathlib import Path
import json

root=Path(__file__).resolve().parents[2]
now=datetime.now(timezone.utc).isoformat()
path=root/'records/qa_k33.json'
data=json.loads(path.read_text())
data.update(visual_review='PASS',visual_review_utc=now,reviewed_pages=list(range(1,7)),
            review_method='Direct inspection of both contact sheets, covering all six full rendered pages.',
            visual_findings='No clipping, collisions, missing symbols, malformed equations or page-boundary problems; all displays and the cap dictionary fit.')
path.write_text(json.dumps(data,indent=2)+'\n')
with (root/'records/literature_fourfold.md').open('a') as log:
    for source in ['records/qa_k33.json','records/render_k33/contact_1.png','records/render_k33/contact_2.png']:
        log.write(f'\n- {now} — Opened own `{source}`. Reason: final P3K.33 visual QA. Material: all six pages checked directly; no layout or symbol defects.\n')
print(json.dumps(data,indent=2))
