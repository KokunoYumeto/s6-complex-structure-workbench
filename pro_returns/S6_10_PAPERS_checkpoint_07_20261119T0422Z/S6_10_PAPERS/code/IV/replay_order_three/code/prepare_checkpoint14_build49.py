"""Preserve the first assembled K50–56 PDF before its inline-math repair."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil

root=Path(__file__).resolve().parents[1]
dest=root/'records/checkpoint14_inline_math_attempt_build48'
dest.mkdir(exist_ok=True)
record={'utc':datetime.now(timezone.utc).isoformat(),'master_build':48,
 'reason':'Direct rendering exposed plain-text inline math inherited from the K55 Markdown export. The formulas are being delimited without changing their content.', 'files':{}}
for name in ['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log']:
    source,target=root/name,dest/name
    assert not target.exists(),target
    shutil.copy2(source,target)
    record['files'][name]={'bytes':source.stat().st_size,'sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(dest/'preservation.json').write_text(json.dumps(record,indent=2)+'\n')
print('Preserved build48 PDF and log for the K55 inline-math correction.')
