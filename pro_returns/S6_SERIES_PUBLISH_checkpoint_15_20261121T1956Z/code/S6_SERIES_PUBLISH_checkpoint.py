#!/usr/bin/env python3
"""Create a new immutable, hash-manifested checkpoint at an authorized checkpoint time."""
from pathlib import Path
import argparse,hashlib,csv,io,zipfile,json,datetime,os
p=argparse.ArgumentParser();p.add_argument('number',type=int);a=p.parse_args()
R=Path(__file__).resolve().parents[1];out=R.parent/'deliverables';out.mkdir(exist_ok=True)
z=out/f'S6_SERIES_PUBLISH_checkpoint_{a.number:02d}.zip'
if z.exists():raise SystemExit('Refusing to overwrite an earlier checkpoint')
exclude_dirs={'vendor','tex-runtime','__pycache__','render'}
files=[]
for path in sorted(R.rglob('*')):
 if not path.is_file():continue
 rel=path.relative_to(R)
 if any(x in exclude_dirs for x in rel.parts):continue
 if path.suffix.lower() in {'.png','.jpg','.jpeg','.gif','.whl','.pyc','.fmt','.synctex','.gz'}:continue
 if path.suffix.lower()=='.pdf':
  # Only certified, current top-level deliverable PDFs are distributable.
  receipt=R/'records'/f'{path.stem}_final_pdf_receipt.json'
  if path.parent!=R or not receipt.is_file():continue
  approved=json.loads(receipt.read_text())
  if not approved.get('all_pages_read') or approved.get('pdf_sha256')!=hashlib.sha256(path.read_bytes()).hexdigest():continue
 if 'checkpoint_' in path.name or path.name.endswith('_filelist.tsv'):continue
 # Snapshot bytes once: a running agent may finish another record while the
 # ZIP is written, but the manifest must describe these exact bytes.
 files.append((rel.as_posix(),path.read_bytes()))
rows=[]
for rel,b in files:
 rows.append({'path':rel,'size':len(b),'sha256':hashlib.sha256(b).hexdigest()})
buf=io.StringIO();w=csv.DictWriter(buf,fieldnames=['path','size','sha256'],delimiter='\t');w.writeheader();w.writerows(rows)
temporary=z.with_suffix('.zip.pending')
with zipfile.ZipFile(temporary,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as f:
 for rel,b in files:f.writestr(rel,b)
 f.writestr(f'S6_SERIES_PUBLISH_checkpoint_{a.number:02d}_filelist.tsv',buf.getvalue())
assert temporary.stat().st_size<500_000_000
with zipfile.ZipFile(temporary) as f:
 for r in rows:
  b=f.read(r['path']);assert len(b)==r['size'] and hashlib.sha256(b).hexdigest()==r['sha256']
os.link(temporary,z) # refuses an existing immutable checkpoint name
temporary.unlink()
print(json.dumps({'path':str(z),'files':len(files),'size':z.stat().st_size,'sha256':hashlib.sha256(z.read_bytes()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
