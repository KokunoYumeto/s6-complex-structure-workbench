#!/usr/bin/env python3
"""Reproduce visual/OCR locator pages from the recovered GJ scan.
Images and OCR remain with research inputs, outside the deliverable tree.
"""
import hashlib,json,os,subprocess
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[2]
pdf=ROOT/'retrieved_sources/garey_johnson.pdf'
out=ROOT/'retrieved_sources/gj_view';out.mkdir(exist_ok=True)
doc=fitz.open(pdf);rows=[]
for k in [0,1,124,148]:
 p=out/f'page-{k+1:03d}.png';doc[k].get_pixmap(matrix=fitz.Matrix(2,2)).save(p)
 r=subprocess.run(['tesseract',str(p),'stdout'],capture_output=True,text=True,env={**os.environ,'OMP_THREAD_LIMIT':'1'},check=True)
 p.with_suffix('.txt').write_text(r.stdout)
 terms=['OPEN8','SS9','PRECEDENCE CONSTRAINED','Copyright','1979']
 rows.append({'pdf_page':k+1,'keyword_lines':{t:[i+1 for i,l in enumerate(r.stdout.splitlines()) if t.lower() in l.lower()] for t in terms}})
report={'pdf_bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'page_count':len(doc),'pages':rows,'visual_locator_check':{'pdf_page_125':'printed pp238–239; SS9 on239','pdf_page_149':'printed pp286–287; OPEN8 on287'}}
(ROOT/'Q03_DEPOSIT/code/C_gj_locator_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
