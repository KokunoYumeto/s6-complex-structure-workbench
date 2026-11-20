from pathlib import Path
import fitz,json,hashlib
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent
R=P.parents[1]
out=P/'QA_build26';out.mkdir(exist_ok=True)
jobs={'V':list(range(116,130)), 'IV':list(range(1193,1213))+[1229,1239,1297]}
for paper,pages in jobs.items():
 f=R/f'S6_SERIES_GRIND_{paper}.pdf';d=fitz.open(f);sheets=[]
 for i in range(0,len(pages),2):
  nums=pages[i:i+2];c=Image.new('RGB',(2260,1610),'#e8e8e8');dr=ImageDraw.Draw(c)
  for col,n in enumerate(nums):
   pix=d[n-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8),alpha=False)
   im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((1072,1518))
   c.paste(im,(29+1130*col,40));dr.text((18+1130*col,13),f'Build26 {paper}, page {n}',fill='black')
  q=out/f'{paper}_{i//2+1:02}.png';c.save(q)
  sheets.append({'file':str(q),'pages':nums,'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
 m={'paper':paper,'pdf':str(f),'pdf_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'page_count':len(d),'pages':pages,'sheets':sheets,'state':'rendered; awaiting actual viewing'}
 (P/f'build26_{paper}_render_manifest.json').write_text(json.dumps(m,indent=2)+'\n')
 print(paper,len(pages),'pages',len(sheets),'sheets',flush=True)
