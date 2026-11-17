#!/usr/bin/env python3
"""Compare the already reviewed pages across the sole heading-break repair."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,fitz
ROOT=Path(__file__).resolve().parents[2]
before=ROOT/'code/part3_fourfold/attempts/k57_20261117T141001/k57_standalone.pdf'
after=ROOT/'code/part3_fourfold/k57_standalone.pdf'
with (ROOT/'records/literature_fourfold.md').open('a') as log:
 log.write('\n- '+datetime.now(timezone.utc).isoformat()+' — Opened the archived and final K57 standalone PDFs. Reason: identify exact raster changes after keeping IE.2 with its first paragraph; material: page raster equality and changed-page list.\n')
old=fitz.open(before);new=fitz.open(after)
assert len(old)==len(new)==22
same=[];changed=[]
for i in range(len(new)):
 a=old[i].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).samples
 b=new[i].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).samples
 (same if hashlib.sha256(a).digest()==hashlib.sha256(b).digest() else changed).append(i+1)
result=dict(utc=datetime.now(timezone.utc).isoformat(),same_pages=same,changed_pages=changed,
 first_review='All22 pages inspected through six contact sheets before the heading-break repair.',
 final_full_size_review=[1,8,13,15,16,19,22])
(ROOT/'records/k57_final_layout_compare.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
