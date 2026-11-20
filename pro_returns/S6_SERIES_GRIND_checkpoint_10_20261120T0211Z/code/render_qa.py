"""Render all repaired-display pages and a document-wide sample for inspection."""
from pathlib import Path
import json,hashlib,fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'build/visual_qa';OUT.mkdir(parents=True,exist_ok=True)
report={}
for paper in ['I','II','III','IV','V']:
 pdf=ROOT/f'S6_SERIES_GRIND_{paper}.pdf';doc=fitz.open(pdf)
 labels=json.loads((ROOT/f'analysis/current_labels_{paper}.json').read_text());reasons={}
 def add(p,why):
  if 1<=p<=len(doc):reasons.setdefault(p,[]).append(why)
 for label,meta in labels.items():
  if (label.startswith('layout:') or label.startswith('fig:I:')) and label.endswith('@cref') is False:
   try:add(int(meta['page']),label)
   except ValueError:pass
 for label in {'I':['wb:thm:canonical-ring-recovery'],
               'II':[], 'III':['maps:src:D.2.51'],
               'IV':['iv:source_transports','night:P3F.22','night:P3K.109','night:P3K.116','night:P3K.117','night:P3K.119','night:P3K.112'],
               'V':[]}[paper]:
  if label in labels:
   page=int(labels[label]['page'])
   for offset in [0,1,2]:add(page+offset,'current edited statement/proof: '+label)
 # The new numbered levels are checked at their actual authored headings,
 # including an appendix proof whose theorem is stated elsewhere.
 if paper in ['I','II','III']:
  hp=ROOT/f'analysis/proof_hierarchy_{paper}.json'
  for entry in json.loads(hp.read_text()):
   title=entry['heading_map'][0]['original_heading']
   needle=' '.join(title.split())
   for i,page in enumerate(doc):
    if needle in ' '.join(page.get_text().split()):
     add(i+1,'new numbered levels: '+entry['statement_label']);break
 if paper=='IV':
  for label in ['night:P3F.1','night:P3F.2','night:P3F.5','night:P3F.10','night:P3F.13','night:P3F.15','night:P3F.18','night:P3F.21','night:P3F.23','night:P3K.106','night:P3K.111']:
   if label in labels:add(int(labels[label]['page'])+1,'new exact source/formula/level repair: '+label)
 for p in [1,2,3,max(1,len(doc)//4),max(1,len(doc)//2),max(1,3*len(doc)//4),len(doc)-1,len(doc)]:add(p,'spread sample')
 for i,page in enumerate(doc):
  text=page.get_text()
  if 'Exact source relationship' in text:add(i+1,'repaired source-table heading')
  if 'Reuse of the indicated body arguments' in text:add(i+1,'main theorem dependency figure')
  if 'Supplying and receiving arguments' in text:add(i+1,'dependency legend')
  if paper=='I' and 'two terms in the last parentheses' in text:add(i+1,'repaired Weierstrass estimate')
  if paper=='I' and 'The exact numerical and tangent checks.' in text:add(i+1,'repaired numbered-heading overflow')
  if paper=='V' and 'selection merely chooses a minor' in text:add(i+1,'repaired nested Hessian display')
  if paper=='V' and 'Fresh normalization from the two finite roots.' in text:add(i+1,'new nested analytic claims')
  if paper=='IV' and 'winding group' in text:add(i+1,'repaired ordinary-forward map table')
  if paper=='V' and i<30 and '1.094540250' in text:add(i+1,'repaired parameter constant display')
  if '1 Results and their proofs in outline' in text and i>1:add(i+1,'introduction sample')
 pages=sorted(reasons);contacts=[]
 for start in range(0,len(pages),4):
  batch=pages[start:start+4];canvas=Image.new('RGB',(1400,1920),'#e8e8e8');draw=ImageDraw.Draw(canvas)
  for idx,p in enumerate(batch):
   pix=doc[p-1].get_pixmap(matrix=fitz.Matrix(1.15,1.15),alpha=False)
   im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
   im.thumbnail((680,910));x=(idx%2)*700+(700-im.width)//2;y=(idx//2)*960+35
   canvas.paste(im,(x,y));draw.text(((idx%2)*700+15,(idx//2)*960+10),f'Paper {paper}, page {p}: '+', '.join(reasons[p])[:65],fill='black')
  path=OUT/f'QA_{paper}_{start//4+1:02d}.png';canvas.save(path);contacts.append(str(path))
 report[paper]={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(doc),'rendered_pages':reasons,'contact_sheets':contacts,'inspection_state':'rendered; human-model visual inspection pending'}
(ROOT/'analysis/rendered_qa.json').write_text(json.dumps(report,indent=2));print(json.dumps({p:{'pages_rendered':len(r['rendered_pages']),'sheets':len(r['contact_sheets'])} for p,r in report.items()}))
