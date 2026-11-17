"""Download cache is outside deliverable; OCR chosen primary-source pages."""
from pathlib import Path
import subprocess
p=Path('/workspace/scratch/e7a4d66da343/external_source_cache')
for n in [5,6,7,9,10,11,12,13]:
 stem=p/f'Wall_page_{n}'
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','110','-png','-singlefile',str(p/'Wall_1962.pdf'),str(stem)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 subprocess.run(['tesseract',str(stem)+'.png',str(stem)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 print(n,stem.with_suffix('.txt'),stem.with_suffix('.txt').stat().st_size,flush=True)
