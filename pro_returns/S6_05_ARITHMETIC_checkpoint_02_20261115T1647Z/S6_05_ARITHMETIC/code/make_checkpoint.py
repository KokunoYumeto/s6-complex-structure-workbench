#!/usr/bin/env python3
"""Make one explicitly requested hourly checkpoint; never overwrite one."""
from pathlib import Path
import zipfile,hashlib,json,sys,time
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]); target=root.parent/f'S6_05_ARITHMETIC_checkpoint_{number:02d}.zip'
assert not target.exists(),target
excluded={'code/A_census_1e9.u32','code/A_census_1e9_height_multiplicity.u32.gz'}
manifest=[]
for p in sorted(root.rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(root))
 if rel in excluded:
  manifest.append({'path':rel,'reason':'Losslessly superseded by code/A_census_1e9.d16m8.gz and decoder','sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest()})
(root/'records/checkpoint_omissions.json').write_text(json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
 for p in sorted(root.rglob('*')):
  if p.is_file() and str(p.relative_to(root)) not in excluded:
   z.write(p,'S6_05_ARITHMETIC/'+str(p.relative_to(root)))
print(json.dumps({'file':str(target),'bytes':target.stat().st_size,'sha256':hashlib.file_digest(target.open('rb'),'sha256').hexdigest()}))
