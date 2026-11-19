"""Render a spread sample for actual visual inspection; rendering is no check."""
from pathlib import Path
import argparse,hashlib,json
import fitz
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('papers',nargs='+');ap.add_argument('--output',default='analysis/standalone_visual_checkpoint04');a=ap.parse_args()
out=P/a.output;out.mkdir(parents=True,exist_ok=True)
f=out/'samples.json';records=json.loads(f.read_text()) if f.exists() else {}
for paper in a.papers:
 pdf=P/f'S6_10_PAPERS_{paper}.pdf';d=fitz.open(pdf);pages=sorted(set([0,len(d)//2,len(d)-1]));imgs=[]
 for n in pages:
  page=d[n];pix=page.get_pixmap(matrix=fitz.Matrix(600/page.rect.width,600/page.rect.width),alpha=False);im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);imgs.append((n,im))
 w=sum(im.width for _,im in imgs);h=max(im.height for _,im in imgs)+28
 canvas=Image.new('RGB',(w,h),'#d0d0d0');draw=ImageDraw.Draw(canvas);x=0
 for n,im in imgs:canvas.paste(im,(x,28));draw.text((x+12,8),f'Paper {paper}: PDF page {n+1} of {len(d)}',fill='black');x+=im.width
 path=out/f'{paper}_spread.png';canvas.save(path)
 records[paper]={'pdf':pdf.name,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':[n+1 for n in pages],'page_count':len(d),'render':str(path.relative_to(P)),'status':'rendered for visual inspection; no visual or mathematical check assigned yet'}
f.write_text(json.dumps(records,indent=2));print({p:r['pages'] for p,r in records.items()})
