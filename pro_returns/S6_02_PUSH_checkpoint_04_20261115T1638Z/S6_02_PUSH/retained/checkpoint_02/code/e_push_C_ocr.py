"""OCR the primary analytic Riemann--Roch statement used in the C supplement."""
from pathlib import Path
import concurrent.futures,subprocess
root=Path(__file__).resolve().parents[1]
folder=root/'evidence/C_independent_primary/ASIII_ocr'
folder.mkdir(exist_ok=True)
source=folder.parent/'AtiyahSinger1968III.pdf'
def page(n):
    target=folder/f'page_{n:02}'
    if not target.with_suffix('.txt').exists():
        subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1700','-png','-singlefile',str(source),str(target)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        subprocess.run(['tesseract',str(target.with_suffix('.png')),str(target)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    return n,target.with_suffix('.txt').read_text()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for n,txt in pool.map(page,range(13,25)):
        if '4.3' in txt or 'Riemann' in txt:
            print(f'PDF PAGE {n}\n{txt}')
