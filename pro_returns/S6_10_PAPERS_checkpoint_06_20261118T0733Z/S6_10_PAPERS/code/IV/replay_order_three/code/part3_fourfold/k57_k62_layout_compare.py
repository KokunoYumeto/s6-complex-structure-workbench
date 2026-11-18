#!/usr/bin/env python3
"""Identify every layout change from the narrow K62 dependency insertion."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,fitz
ROOT=Path(__file__).resolve().parents[2]
before=ROOT/'records/k57_pre_k62_dependency/k57_standalone.pdf'
after=ROOT/'code/part3_fourfold/k57_standalone.pdf'
with (ROOT/'records/literature_fourfold.md').open('a') as log:
 log.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened the preserved pre-K62 and refreshed K57 standalone PDFs. Reason: identify all exact raster changes after the narrow C2 scalar-comparison insertion. Material: equality of page rasters and every changed page.\n')
old=fitz.open(before);new=fitz.open(after)
same=[];changed=[]
for i in range(len(new)):
 b=new[i].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).samples
 a=old[i].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).samples if i<len(old) else b''
 (same if hashlib.sha256(a).digest()==hashlib.sha256(b).digest() else changed).append(i+1)
result=dict(utc=datetime.now(timezone.utc).isoformat(),same_pages=same,changed_pages=changed,
 old_page_count=len(old),new_page_count=len(new),
 previous_review='All 22 pages were directly reviewed and recorded PASS before the K62 dependency repair.',
 pdf_sha256=hashlib.sha256(after.read_bytes()).hexdigest())
(ROOT/'records/k57_k62_layout_compare.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
