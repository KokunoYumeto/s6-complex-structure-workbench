"""Run the independent standalone restore after checkpoint24 is immutable."""
from pathlib import Path
import subprocess,sys,time
root=Path(__file__).resolve().parents[1]
while not (root.parent/'checkpoint24_encoding/checkpoint24_creation.json').exists():
 time.sleep(3)
subprocess.run([sys.executable,str(root/'code/verify_checkpoint24.py')],cwd=root,check=True)
