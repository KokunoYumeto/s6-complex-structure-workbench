#!/usr/bin/env python3
"""Render seventh-hour proof pages, without claiming they have been inspected."""
from pathlib import Path
import json,re,sys
import fitz
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parents[1]
tag=sys.argv[1]
doc=fitz.open(root/'S6_02_PUSH_paper.pdf')
out=root/'qa'/tag
out.mkdir(parents=True,exist_ok=True)
ids=[f'B.4.{i}' for i in range(15,19)]
ids += [f'E.2.{i}' for i in range(11,20)]
found={}
for i,p in enumerate(doc):
    content=' '.join(p.get_text().split())
    for identity in ids:
        pattern=re.escape(identity)+r'(?:\s*\(Proved\)|\s*;\s*Proved)'
        if re.search(pattern,content):found[identity]=i+1
required=ids[:-1]
assert all(i in found for i in required),(required,found)
pages=set(found.values())
for identity in ['E.2.11','E.2.14','E.2.15','E.2.17','E.2.19']:
    if identity in found:
        pages.update(p for p in [found[identity]+1,found[identity]+2] if p<=len(doc))
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
    path=out/f'seventh_hour_new_statements_{start//9+1}.jpg'
    sheet.save(path,quality=94);sheets.append(str(path))
record={'build':tag,'pdf_pages':len(doc),'statement_start_pages':found,
        'additional_pages':pages,'contact_sheets':sheets,
        'scope':'Rendered sample only; inspection must be recorded after viewing.'}
(out/'additional_render_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
