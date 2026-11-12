#!/usr/bin/env python3
"""Render all PDF pages with Poppler and create labelled QA contact sheets.

Full page PNGs are temporary, outside the deliverable. Contact sheets and
page text diagnostics are retained. Visual inspection is performed by the
assistant after this program; the script does not claim visual approval.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import fitz
from PIL import Image,ImageDraw,ImageFont

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--directory',type=Path,default=ROOT.parent/'pdf_qa')
args=parser.parse_args()
qa=args.directory.resolve()
(qa/'pages').mkdir(parents=True,exist_ok=True)
(ROOT/'outputs/visual_qa').mkdir(parents=True,exist_ok=True)
pdf=ROOT/'S6_01_INVARIANTS_paper.pdf'
subprocess.run(['pdftoppm','-r','85','-png',str(pdf),str(qa/'pages/page')],check=True)
paths=sorted((qa/'pages').glob('page-*.png'))
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15)
contacts=[]
for start in range(0,len(paths),12):
    subset=paths[start:start+12]
    canvas=Image.new('RGB',(4*360,3*535),'#d7dbe0')
    draw=ImageDraw.Draw(canvas)
    for j,path in enumerate(subset):
        im=Image.open(path).convert('RGB')
        im.thumbnail((344,493))
        x=(j%4)*360+(360-im.width)//2
        y=(j//4)*535+26
        canvas.paste(im,(x,y))
        draw.text(((j%4)*360+12,(j//4)*535+5),f'Page {start+j+1}',font=font,fill='black')
    target=ROOT/'outputs/visual_qa'/f'contact_{start//12+1:02}.jpg'
    canvas.save(target,quality=91)
    contacts.append(str(target.relative_to(ROOT)))
doc=fitz.open(pdf)
ids={}
boundary=[]
texts=[]
for number,page in enumerate(doc,1):
    txt=page.get_text()
    texts.append(f'\n\n--- PDF PAGE {number} ---\n'+txt)
    for match in re.finditer(r'Statement\s+([A-E]\d+\.\d+)\s*\[',txt):
        ids.setdefault(match.group(1),[]).append(number)
    for block in page.get_text('blocks'):
        x0,y0,x1,y1,*_=block
        if x0<18 or x1>page.rect.width-18 or y0<12 or y1>page.rect.height-12:
            boundary.append({'page':number,'bbox':[x0,y0,x1,y1],'text':str(block[4])[:160]})
(ROOT/'outputs/paper_text.txt').write_text(''.join(texts),encoding='utf-8')
record={'pages':len(doc),'claim_pages':ids,'contact_sheets':contacts,'extreme_boundary_blocks':boundary,
        'visual_inspection':'Pending manual image inspection; see visual_review.md once completed.'}
(ROOT/'outputs/pdf_qa.json').write_text(json.dumps(record,indent=2)+'\n')
print(f'Rendered {len(doc)} pages; found {len(ids)} numbered statement headings.')
print(f'Contact sheets: {len(contacts)}; extreme boundary blocks: {len(boundary)}.')
