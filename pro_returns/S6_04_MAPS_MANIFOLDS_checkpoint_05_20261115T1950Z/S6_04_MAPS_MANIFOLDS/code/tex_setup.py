"""Provision the missing LuaLaTeX support package locally, without system writes."""
from pathlib import Path
from urllib.request import urlopen
import subprocess,hashlib
root=Path(__file__).resolve().parents[2]/'tex_runtime'
root.mkdir(exist_ok=True)
name='texlive-luatex_2024.20250309-1_all.deb'
url='https://deb.debian.org/debian/pool/main/t/texlive-base/'+name
dest=root/name
if not dest.exists():
 with urlopen(url,timeout=45) as src,dest.open('wb') as out:
  while chunk:=src.read(1024*1024):out.write(chunk)
subprocess.run(['dpkg-deb','-x',str(dest),str(root/'package')],check=True)
out=f'URL: {url}\nSHA256: {hashlib.sha256(dest.read_bytes()).hexdigest()}\nExtracted locally.\n'
print(out,end='');Path(__file__).with_suffix('.out').write_text(out)
