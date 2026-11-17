#!/usr/bin/env python3
"""Render primary-source pages to a private inspection directory."""
from pathlib import Path
import fitz
root=Path(__file__).resolve().parents[2]
out=root/"external_sources"/"inspection"
out.mkdir(exist_ok=True)
for name, pages in {"Cerf1970":[4],"KervaireMilnor1963":[1,2,3,28,29],"EellsKuiper1962":[8]}.items():
    d=fitz.open(root/"external_sources"/(name+".pdf"))
    for i in pages:
        dst=out/(name+"_pdfpage_"+str(i+1)+".png")
        d[i].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(dst)
        print(name, "PDF page", i+1, "rendered")
