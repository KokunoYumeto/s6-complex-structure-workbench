#!/usr/bin/env python3
"""Locate original supplied cusp-topology pages; keep scans outside the package."""
from pathlib import Path
import json,re
import fitz
root=Path(__file__).resolve().parents[1]
source=root.parent/'background'/'original'/'AC26_original_manuscript.pdf'
private=root.parent/'external_sources'/'root_cusp_topology'
private.mkdir(parents=True,exist_ok=True)
doc=fitz.open(source)
records=[]
for i,page in enumerate(doc):
    content=' '.join(page.get_text().split())
    if 'Corollary 4.8' in content:
        target=private/f'ac26_page_{i+1:03d}.png'
        page.get_pixmap(matrix=fitz.Matrix(1.7,1.7),alpha=False).save(target)
        (private/f'ac26_page_{i+1:03d}.txt').write_text(page.get_text())
        records.append({'pdf_page':i+1,'local_scan':str(target),
                        'located':'Corollary 4.8 or a page explicitly referring to it'})
print(json.dumps({'source':'Supplied AC26 original manuscript; not republished',
                  'pages':records},indent=2))
