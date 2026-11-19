"""Run the hourly check, one immutable snapshot, and standalone verification."""
from pathlib import Path
from datetime import datetime, timezone
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
check_time = datetime.fromisoformat('2026-11-18T00:48:44+00:00')
freeze_time = datetime.fromisoformat('2026-11-18T00:49:44+00:00')


def until(deadline):
    while True:
        remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
        if remaining <= 0:
            return
        time.sleep(min(20,remaining))


until(check_time)
with (ROOT/'records/checkpoint25_progress_update.out').open('a') as out, (ROOT/'records/checkpoint25_progress_update.err').open('a') as err:
    subprocess.run([sys.executable,str(ROOT/'code/update_checkpoint25_progress.py')],
                   cwd=ROOT,stdout=out,stderr=err,check=True)
print('Hourly mathematical progress check completed: CONTINUE.',flush=True)
until(freeze_time)
subprocess.run([sys.executable,str(ROOT/'code/make_checkpoint25.py')],cwd=ROOT,check=True)
subprocess.run([sys.executable,str(ROOT/'code/verify_checkpoint25.py')],cwd=ROOT,check=True)
print('Checkpoint25 created and independently verified; persistent save remains.',flush=True)
