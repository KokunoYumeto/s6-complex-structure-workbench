"""Create checkpoint18 at the next hourly deadline, never earlier."""
from datetime import datetime,timezone
from pathlib import Path
import subprocess,sys,time
root=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,17,17,49,44,tzinfo=timezone.utc)
while True:
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
    if remaining<=0:
        break
    time.sleep(min(20,remaining))
subprocess.run([sys.executable,str(root/'code/make_checkpoint.py'),'18'],cwd=root,check=True)
