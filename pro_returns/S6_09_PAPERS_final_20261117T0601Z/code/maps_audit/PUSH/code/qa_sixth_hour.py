#!/usr/bin/env python3
"""Render the new sixth-hour proofs; inspection is recorded separately."""
from pathlib import Path
import sys,json
import fitz
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parents[1]
tag=sys.argv[1] if len(sys.argv)>1 else 'draft23'
doc=fitz.open(root/'S6_02_PUSH_paper.pdf')
out=root/'qa'/tag
out.mkdir(parents=True,exist_ok=True)
needles=[f'B.4.{i} (Proved)' for i in range(10,15)]
needles += [f'E.2.{i} (Proved)' for i in range(7,11)]
found={}
for i,p in enumerate(doc):
    normalized=' '.join(p.get_text().split())
    for n in needles:
        if n in normalized: found[n]=i+1
assert len(found)==len(needles),(needles,found)
pages=set(found.values())
for needle in ['B.4.12 (Proved)','E.2.9 (Proved)']:
    pages.update(p for p in [found[needle]+1,found[needle]+2] if p<=len(doc))
pages=sorted(pages)
cards=[]
for number in pages:
    target=out/f'page_{number:03d}.png'
    doc[number-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False).save(target)
    im=Image.open(target).convert('RGB');im.thumbnail((480,680))
    card=Image.new('RGB',(500,720),'#dddddd')
    card.paste(im,((500-im.width)//2,15))
    ImageDraw.Draw(card).text((12,695),f'Page {number}',fill='black')
    cards.append(card)
sheets=[]
for start in range(0,len(cards),9):
    group=cards[start:start+9]
    sheet=Image.new('RGB',(1500,720*((len(group)+2)//3)),'white')
    for j,card in enumerate(group):sheet.paste(card,((j%3)*500,(j//3)*720))
    path=out/f'sixth_hour_new_statements_{start//9+1}.jpg'
    sheet.save(path,quality=94);sheets.append(str(path))
record={'build':tag,'pdf_pages':len(doc),'statement_start_pages':found,
        'additional_pages':pages,'contact_sheets':sheets,
        'scope':'Rendered sample only; visual inspection must be recorded after viewing.'}
(out/'additional_render_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
