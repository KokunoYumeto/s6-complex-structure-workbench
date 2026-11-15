#!/usr/bin/env python3
"""Make one explicitly requested hourly checkpoint; never overwrite one."""
from pathlib import Path
import zipfile,hashlib,json,sys,time
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]); target=root.parent/f'S6_05_ARITHMETIC_checkpoint_{number:02d}.zip'
assert not target.exists(),target
excluded={'code/A_census_1e9.u32','code/A_census_1e9_height_multiplicity.u32.gz'}
sources={
 'C_Waldschmidt1979_translation':'https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/GDL/SigmaNoteCanada1979-eng.pdf',
 'C_Waldschmidt1975_dimension':'https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Fourier.pdf',
 'C_Waldschmidt2009_auxiliary':'https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SASTRAaftp.pdf',
 'C_Noguchi2024_author':'https://www.ms.u-tokyo.ac.jp/~noguchi/An-axsch.pdf',
 'C_Xie2024_preprint':'https://arxiv.org/pdf/2202.09032',
 'A_ChatzakosDimakis2026':'https://arxiv.org/pdf/2609.33829'
}
for stem in sources:
 for suffix in ['.pdf','.txt']:
  excluded.add(f'records/{stem}{suffix}')
manifest=[]
for p in sorted(root.rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(root))
 if rel in excluded:
  if p.stem in sources:
   entry={'path':rel,'reason':'Third-party full article or full text: source URL, access records and original proof audit retained instead of redistributing the article.','source_url':sources[p.stem]}
  else:
   entry={'path':rel,'reason':'Losslessly superseded by code/A_census_1e9.d16m8.gz and decoder'}
  entry['sha256']=hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
  manifest.append(entry)
(root/'records/checkpoint_omissions.json').write_text(json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
 for p in sorted(root.rglob('*')):
  if p.is_file() and str(p.relative_to(root)) not in excluded:
   z.write(p,'S6_05_ARITHMETIC/'+str(p.relative_to(root)))
print(json.dumps({'file':str(target),'bytes':target.stat().st_size,'sha256':hashlib.file_digest(target.open('rb'),'sha256').hexdigest()}))
