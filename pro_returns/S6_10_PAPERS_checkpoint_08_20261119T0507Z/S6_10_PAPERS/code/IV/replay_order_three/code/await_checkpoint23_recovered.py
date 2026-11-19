from pathlib import Path
from datetime import datetime, timezone
import time, subprocess, sys
root=Path(__file__).resolve().parents[1]
due=datetime.fromisoformat("2026-11-17T22:49:44+00:00")
ready=root.parent/"checkpoint23_ready.json"
while datetime.now(timezone.utc)<due or not ready.exists():time.sleep(2)
subprocess.run([sys.executable,str(root/"code/make_checkpoint23_from_base22.py")],cwd=root,check=True)
