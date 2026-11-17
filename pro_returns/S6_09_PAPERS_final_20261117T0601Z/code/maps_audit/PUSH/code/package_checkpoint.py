#!/usr/bin/env python3
"""Create a new hourly ZIP, never replacing an earlier checkpoint."""
from pathlib import Path
import sys,zipfile,hashlib,json,datetime
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1])
dest=root.parent/f"S6_02_PUSH_checkpoint_{number:02d}.zip"
assert not dest.exists(), "Checkpoint already exists"
paths=sorted(p for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
record={"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"files":[{"path":str(p.relative_to(root)),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]}
manifest=root/"code"/f"checkpoint_manifest_{number:02d}.json"
manifest.write_text(json.dumps(record,indent=2))
with zipfile.ZipFile(dest,"x",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in paths+[manifest]:
        z.write(p,Path(root.name)/p.relative_to(root))
print(dest)
print("Files",len(paths)+1,"bytes",dest.stat().st_size,"sha256",hashlib.sha256(dest.read_bytes()).hexdigest())
