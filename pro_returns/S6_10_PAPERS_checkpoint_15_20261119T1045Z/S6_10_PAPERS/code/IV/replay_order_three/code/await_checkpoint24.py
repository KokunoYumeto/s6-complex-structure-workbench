"""Wait for the authorized hourly snapshot time; never skip the frozen copy."""
from datetime import datetime,timezone
from pathlib import Path
import subprocess,sys,time
root=Path(__file__).resolve().parents[1]
deadline=datetime.fromisoformat('2026-11-17T23:49:44+00:00')
while datetime.now(timezone.utc)<deadline:
 time.sleep(min(5,max(0,(deadline-datetime.now(timezone.utc)).total_seconds())))
while not (root.parent/'checkpoint24_ready.json').exists():
 time.sleep(2)
subprocess.run([sys.executable,str(root/'code/make_checkpoint24.py')],cwd=root,check=True)
