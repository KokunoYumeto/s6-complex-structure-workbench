"""Render the exact changed-page set for build22; viewing is a separate act."""
from pathlib import Path
import hashlib
import json
import fitz
from PIL import Image,ImageDraw

R=Path(__file__).resolve().parents[1]
out=R/'build/visual_qa_22';out.mkdir(parents=True,exist_ok=True)
jobs={
 'I':[62,86,87,88]+list(range(244,253))+list(range(271,279))+[361,362,363],
 'IV':list(range(105,136))+list(range(144,149))+[1305,1312,1314,1323,1324,1325,1326,1329,1332,1333,1334,1335,1340,1353,1358,1359]+list(range(1362,1371))+[1395,1396,1434,1438],
}
for paper,pages in jobs.items():
 path=R/f'S6_SERIES_GRIND_{paper}.pdf';doc=fitz.open(path)
 pages=sorted(set(pages));sheets=[]
 for idx in range(0,len(pages),2):
  nums=pages[idx:idx+2];canvas=Image.new('RGB',(2260,1610),'#e8e8e8');draw=ImageDraw.Draw(canvas)
  for col,n in enumerate(nums):
   pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8),alpha=False)
   im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((1072,1518))
   canvas.paste(im,(29+1130*col,40));draw.text((18+1130*col,13),f'{paper}, page {n}',fill='black')
  dest=out/f'changed_{paper}_{idx//2+1:02d}.png';canvas.save(dest)
  sheets.append(dict(path=str(dest.relative_to(R)),pages=nums,sha256=hashlib.sha256(dest.read_bytes()).hexdigest()))
 data=dict(pdf_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),page_count=len(doc),pages=pages,sheets=sheets,inspection_state='rendered, not yet viewed')
 (R/f'analysis/build22_changed_render_{paper}.json').write_text(json.dumps(data,indent=2)+'\n')
 print(paper,len(pages),'pages',len(sheets),'sheets',flush=True)
