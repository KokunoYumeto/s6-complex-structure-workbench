"""Start the final PDF audits immediately after all three final build passes."""
from pathlib import Path
from datetime import datetime, timezone
import concurrent.futures
import subprocess
import sys
import time

root=Path(__file__).resolve().parents[1]
log=root/'records/build_fortythird.out'
deadline=datetime(2026,11,17,9,45,tzinfo=timezone.utc)
marker='Transcript written on S6_06_BLIND_paper.log.'
while True:
    text=log.read_text(errors='replace') if log.exists() else ''
    if text.count(marker)>=3:
        break
    if datetime.now(timezone.utc)>=deadline:
        raise SystemExit('Final three-pass build not finished before audit deadline.')
    time.sleep(1)

def run(name):
    target=root/'records'/f'checkpoint10_{name}.out'
    with target.open('w') as out:
        result=subprocess.run(
            [sys.executable,str(root/'code'/f'{name}.py'),'10'],
            cwd=root,stdout=out,stderr=subprocess.STDOUT)
    if result.returncode:
        raise RuntimeError(f'{name} failed with exit {result.returncode}')
    return str(target.relative_to(root))

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    futures=[pool.submit(run,name) for name in
        ('audit_checkpoint_pdf','audit_pdf_boundaries')]
    for f in futures:
        print(f.result(),flush=True)
print('Final checkpoint10 PDF rendered and all-page boundaries audited.',flush=True)
