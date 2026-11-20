"""Render selected current proof pages; image viewing must be recorded separately."""
from pathlib import Path
import argparse,hashlib,json
import fitz
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--cycle',default='21');p.add_argument('--papers',nargs='+',default=['I','II','III','IV','V']);a=p.parse_args()
out=R/f'build/visual_qa_{a.cycle}';out.mkdir(parents=True,exist_ok=True)
report={}
for paper in a.papers:
 path=R/f'S6_SERIES_GRIND_{paper}.pdf';doc=fitz.open(path);labels=json.loads((R/f'analysis/current_labels_{paper}.json').read_text())
 def loc(k):return int(labels[k]['page'])
 if paper=='I':
  pages=[1,10,18,24,25,94,95]
  for lab,span in [('fam:src:F.2.1',2),('fam:src:F.3.1',3),('inv:A2.1',4),('inv:A4.1',2),('inv:C2.1',2),('wb:thm:canonical-ring-recovery',3)]:pages+=list(range(loc(lab),loc(lab)+span))
  pages+=list(range(loc('night:P5.1'),loc('inv:C3.8')+11))+[len(doc)]
 elif paper=='IV':pages=[1,10,700]+list(range(loc('night:P3F.1'),loc('night:P3F.20')+2))+list(range(loc('night:P3F.22'),loc('night:P3F.24')+2))+[len(doc)]
 elif paper=='III':
  pages=[1,10,160,len(doc)]
  for n in range(loc('maps:src:D.2.53'),min(loc('maps:src:D.2.53')+20,len(doc))+1):
   t=doc[n-1].get_text()
   if 'III_OS45_primitive' in t or 'III_weighted_OS45' in t:pages.extend([n-1,n,n+1])
 elif paper=='II':pages=[1,10,517,len(doc)]
 else:pages=[1,10,150,151,len(doc)]
 pages=sorted(set(i for i in pages if 1<=i<=len(doc)));sheets=[]
 for idx in range(0,len(pages),2):
  nums=pages[idx:idx+2];canvas=Image.new('RGB',(2260,1610),'#e8e8e8');draw=ImageDraw.Draw(canvas)
  for col,n in enumerate(nums):
   pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8),alpha=False)
   im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((1072,1518))
   canvas.paste(im,(29+1130*col,40));draw.text((18+1130*col,13),f'{paper}, page {n}',fill='black')
  dest=out/f'focused_{paper}_{idx//2+1:02d}.png';canvas.save(dest)
  sheets.append({'path':str(dest.relative_to(R)),'pages':nums,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
 report[paper]={'pdf_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'page_count':len(doc),'pages':pages,'sheets':sheets,'inspection_state':'rendered, not yet viewed'}
 dest=R/f'analysis/build{a.cycle}_focused_render_{paper}.json';dest.write_text(json.dumps(report[paper],indent=2)+'\n')
 print(paper,len(pages),'pages',len(sheets),'sheets',flush=True)
