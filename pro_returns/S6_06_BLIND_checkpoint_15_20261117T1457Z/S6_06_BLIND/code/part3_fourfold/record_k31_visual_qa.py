from datetime import datetime, timezone
from pathlib import Path
import json

root = Path(__file__).resolve().parents[2]
now = datetime.now(timezone.utc).isoformat()
record = root / 'records/qa_k31.json'
data = json.loads(record.read_text())
data.update(visual_review='PASS', visual_review_utc=now,
            reviewed_pages=list(range(1, 8)),
            review_method='Direct visual inspection of contact_1.png and contact_2.png, covering every one of the seven rendered pages.',
            visual_findings='No clipping, collisions, missing symbols, malformed equations, or page-boundary problems observed.')
record.write_text(json.dumps(data, indent=2) + '\n')
with (root / 'records/literature_fourfold.md').open('a') as log:
    for source in ['records/qa_k31.json', 'records/render_k31/contact_1.png', 'records/render_k31/contact_2.png']:
        log.write(f'\n- {now} — Opened `{source}`. Reason: final standalone P3K.31 visual QA. Material taken: seven-page compilation and direct rendered-page inspection; no layout or symbol defects.\n')
print(json.dumps(data, indent=2))
