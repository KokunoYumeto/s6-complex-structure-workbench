"""OCR the primary Wall V scan for source verification, outside deliverables."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import os
import subprocess

HERE = Path(__file__).resolve()
BASE = HERE.parents[2] / 'external_sources' / 'C_independent_primary'
OUT = BASE / 'Wall1966V_ocr'
OUT.mkdir(exist_ok=True)
ENV = dict(os.environ, OMP_THREAD_LIMIT='1')

def one(page):
    prefix = OUT / f'page_{page:02d}'
    subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page),
                    '-r', '145', '-singlefile', '-png', str(BASE/'Wall1966V.pdf'),
                    str(prefix)], check=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    subprocess.run(['tesseract', str(prefix.with_suffix('.png')), str(prefix),
                    '--psm', '3'], env=ENV, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return page, prefix.with_suffix('.txt').read_text()

with ThreadPoolExecutor(max_workers=4) as pool:
    rows = list(pool.map(one, range(1,21)))
combined='\n\n'.join(f'PAGE {page} (journal page {354+page})\n{text}' for page,text in rows)
(BASE/'Wall1966V_ocr.txt').write_text(combined)
print('PASS: 20 pages OCRed outside the deliverable package.')
print('Output:', BASE/'Wall1966V_ocr.txt')
