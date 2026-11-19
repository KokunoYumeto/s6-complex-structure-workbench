#!/usr/bin/env python3
"""Render/OCR the opened author-hosted Coffman-Graham scan for locator checks.
OCR text stays with research inputs; output contains only page locators.
"""
import concurrent.futures,json,subprocess,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CACHE=ROOT/'retrieved_sources/cg_ocr';CACHE.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-r','140','-png',str(ROOT/'retrieved_sources/coffman_graham.pdf'),str(CACHE/'page')],check=True,capture_output=True)
def ocr(p):
 r=subprocess.run(['tesseract',str(p),'stdout'],capture_output=True,text=True,check=True,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
 p.with_suffix('.txt').write_text(r.stdout)
 terms=['theorem','unit','optimal','quadratic','n2','n²']
 return {'pdf_page':int(p.stem.split('-')[-1]),'keyword_lines':{t:[i+1 for i,l in enumerate(r.stdout.splitlines()) if t in l.lower()] for t in terms}}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(ocr,sorted(CACHE.glob('*.png'))))
(ROOT/'Q03_DEPOSIT/code/C_pdf_inspect_output.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r)
