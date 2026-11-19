"""Immutable self-contained checkpoint, excluding base inputs and render caches."""
from pathlib import Path
import argparse,hashlib,json,zipfile,csv,io
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('number',type=int);args=parser.parse_args()
name=f'S6_SERIES_GRIND_checkpoint_{args.number:02d}.zip';dest=ROOT.parent/name
assert not dest.exists(),str(dest)
files=[]
for path in ROOT.rglob('*'):
 if not path.is_file():continue
 rel=path.relative_to(ROOT);parts=rel.parts
 if '__pycache__' in parts or '.git' in parts or 'node_modules' in parts:continue
 if parts[0]=='build' and parts[1]!='library_helpers':continue
 if path.suffix in ['.aux','.toc','.out','.log','.synctex','.gz'] and len(parts)==1:continue
 if 'checkpoint_' in path.name or path.name.startswith('S6_SERIES_GRIND_final'):continue
 if path.suffix.lower() in ['.png','.jpg','.jpeg'] and 'problem_screenshots' not in parts:continue
 if parts[0] in ['.cache','luatex-cache']:continue
 files.append(path)
manifest=[]
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for path in sorted(files):
  content=path.read_bytes();rel=str(path.relative_to(ROOT));z.writestr(rel,content)
  manifest.append({'path':rel,'size':len(content),'sha256':hashlib.sha256(content).hexdigest()})
 buf=io.StringIO();w=csv.DictWriter(buf,fieldnames=['path','size','sha256'],delimiter='\t');w.writeheader();w.writerows(manifest)
 z.writestr('S6_SERIES_GRIND_filelist.tsv',buf.getvalue())
with zipfile.ZipFile(dest) as z:
 for r in manifest:
  data=z.read(r['path']);assert len(data)==r['size'] and hashlib.sha256(data).hexdigest()==r['sha256']
receipt={'path':str(dest),'files':len(manifest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'manifest_verified':True}
(ROOT/f'analysis/checkpoint_{args.number:02d}_receipt.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt))
