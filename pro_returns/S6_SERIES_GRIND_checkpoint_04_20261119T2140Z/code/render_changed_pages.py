"""Render the changed dependency figures and selected long-proof levels."""
from pathlib import Path
import hashlib,json
import fitz
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];out=R/'build/changed_qa';out.mkdir(parents=True,exist_ok=True)
targets={'I':[],'II':[],'III':['maps:src:D.2.51'],'IV':['iv:source_transports','night:P3F.35','night:P3K.109','night:P3K.117','night:P3K.119','night:P3K.111','night:P3K.112'],'V':[]}
records=[]
for paper in targets:
 pdf=R/f'S6_SERIES_GRIND_{paper}.pdf';doc=fitz.open(pdf);labels=json.loads((R/f'analysis/current_labels_{paper}.json').read_text());pages={}
 def add(page,why):
  if 1<=page<=len(doc):pages.setdefault(page,[]).append(why)
 for i in range(min(30,len(doc))):
  text=doc[i].get_text()
  if 'Reuse of the indicated body arguments' in text or 'Supplying and receiving arguments' in text:add(i+1,'dependency figure and legend')
 for lab in targets[paper]:
  page=int(labels[lab]['page']);add(page,lab);add(page+1,lab+' proof')
  if lab in ['night:P3K.117','night:P3K.119']:add(page+5,lab+' numbered levels')
 for start in range(0,len(pages),4):
  batch=sorted(pages)[start:start+4];canvas=Image.new('RGB',(1400,1920),'#e8e8e8');draw=ImageDraw.Draw(canvas)
  for j,page in enumerate(batch):
   pix=doc[page-1].get_pixmap(matrix=fitz.Matrix(1.15,1.15),alpha=False);im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((680,910));x=(j%2)*700+(700-im.width)//2;y=(j//2)*960+35;canvas.paste(im,(x,y));draw.text(((j%2)*700+12,(j//2)*960+10),f'{paper} p{page}: '+','.join(pages[page])[:80],fill='black')
  path=out/f'changed_{paper}_{start//4+1:02d}.png';canvas.save(path)
  records.append({'paper':paper,'pages':batch,'file':str(path),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'inspection':'pending'})
(R/'analysis/changed_pages_QA.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'sheets':len(records),'pages':sum(len(x['pages']) for x in records),'files':[x['file'] for x in records]}))
