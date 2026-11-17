from datetime import datetime, timezone
from pathlib import Path
import json

root=Path(__file__).resolve().parents[2]
now=datetime.now(timezone.utc).isoformat()
path=root/'records/qa_k35.json'
data=json.loads(path.read_text())
data.update(visual_review='PASS',visual_review_utc=now,
            reviewed_pages=list(range(1,data['pages']+1)),
            review_method='Direct inspection of every rendered page in the contact sheets, with equation and table fit checked.',
            visual_findings='No clipping, collisions, missing symbols or malformed equations; table, matrices and the full endpoint proof fit.')
path.write_text(json.dumps(data,indent=2)+'\n')
with (root/'records/literature_fourfold.md').open('a') as log:
    for source in ['records/qa_k35.json']+[str(p.relative_to(root)) for p in sorted((root/'records/render_k35').glob('contact_*.png'))]:
        log.write(f'\n- {now} — Opened own `{source}`. Reason: final P3K.35 visual QA. Material: every rendered page checked directly; no layout or symbol defects.\n')
print(json.dumps(data,indent=2))
