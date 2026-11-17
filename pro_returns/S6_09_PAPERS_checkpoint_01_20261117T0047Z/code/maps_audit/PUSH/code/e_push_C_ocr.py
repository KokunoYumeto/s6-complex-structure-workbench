"""OCR the primary analytic Riemann--Roch statement used in the C supplement."""
from pathlib import Path
import concurrent.futures,hashlib,json,os,subprocess
root=Path(__file__).resolve().parents[1]
folder=root.parent/'external_sources/C_independent_primary/ASIII_ocr'
folder.mkdir(parents=True,exist_ok=True)
source=folder.parent/'AtiyahSinger1968III.pdf'
def page(n):
    target=folder/f'page_{n:02}'
    if not target.with_suffix('.txt').exists() or target.with_suffix('.txt').stat().st_size==0:
        subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1700','-png','-singlefile',str(source),str(target)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        env=dict(os.environ,OMP_THREAD_LIMIT='1')
        subprocess.run(['tesseract',str(target.with_suffix('.png')),str(target)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,env=env)
    return n,target.with_suffix('.txt').read_text()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    for n,txt in pool.map(page,range(19,22)):
        print(json.dumps({'pdf_page':n,'printed_page':n+544,
                          'ocr_bytes':len(txt.encode()),
                          'ocr_sha256':hashlib.sha256(txt.encode()).hexdigest(),
                          'contains_theorem_4_3':'4.3' in txt,
                          'source_location':'external_sources/C_independent_primary/ASIII_ocr'}))
