"""Extract official Debian arithmetic packages into a local runtime.

No system packages or system configuration are changed. The manifest records
the exact official URL, SHA256, control fields, and extraction destination.
"""
from pathlib import Path
import concurrent.futures,hashlib,json,subprocess,urllib.request

OUT=Path(__file__).resolve().parents[2]
DEST=OUT/'build/arithmetic_runtime'
PACKAGES=[
 ('pari','pari-gp_2.17.2-1_amd64.deb'),
 ('pari','libpari-gmp-tls9_2.17.2-1_amd64.deb'),
 ('pari','libpari-dev_2.17.2-1_amd64.deb'),
 ('eclib','libec14_20250122-2_amd64.deb'),
 ('eclib','libec-dev_20250122-2_amd64.deb'),
 ('eclib','eclib-tools_20250122-2_amd64.deb'),
 ('mpfr4','libmpfr-dev_4.2.2-1_amd64.deb'),
 ('ntl','libntl44_11.5.1-1+b3_amd64.deb'),
 ('ntl','libntl-dev_11.5.1-1+b3_amd64.deb'),
 ('gf2x','libgf2x3_1.3.0-3_amd64.deb'),
]

def download(item):
 package,name=item
 url=f'https://ftp.debian.org/debian/pool/main/{package[0]}/{package}/{name}'
 path=DEST/'packages'/name
 if not path.exists():
  with urllib.request.urlopen(url,timeout=60) as r:path.write_bytes(r.read())
 control=subprocess.check_output(['dpkg-deb','-f',str(path)],text=True)
 return {'url':url,'file':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size,'control':control}

def main():
 (DEST/'packages').mkdir(parents=True,exist_ok=True)
 (DEST/'root').mkdir(exist_ok=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  records=list(pool.map(download,PACKAGES))
 for rec in records:
  subprocess.run(['dpkg-deb','-x',str(DEST/'packages'/rec['file']),str(DEST/'root')],check=True)
 (DEST/'package_manifest.json').write_text(json.dumps(records,indent=2))
 print(json.dumps([{'file':r['file'],'bytes':r['bytes'],'sha256':r['sha256'],'depends':next((s for s in r['control'].splitlines() if s.startswith('Depends:')),'')} for r in records],indent=2))
 for p in ('usr/bin/gp','usr/lib/x86_64-linux-gnu/libec.so.14'):
  subprocess.run(['ldd',str(DEST/'root'/p)])

if __name__=='__main__':main()
