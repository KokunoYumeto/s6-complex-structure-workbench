"""Render every page, produce contact sheets, and audit PDF text bounds.

Requires PyMuPDF and Pillow. PNGs are temporary visual-review artifacts
outside the deliverable folder; the audit JSON and output are retained.
"""
from pathlib import Path
import json, re
import fitz
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'S6_02_FAMILY_qa'
OUT.mkdir(exist_ok=True)
doc=fitz.open(ROOT/'S6_02_FAMILY_paper.pdf')
report={'pages':len(doc),'metadata':doc.metadata,'boundary_violations':[],
        'statement_pages':{},'contact_sheets':[]}
thumbs=[]
for i,page in enumerate(doc,1):
    pix=page.get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False)
    p=OUT/f'page_{i:03d}.png';pix.save(p)
    image=Image.open(p).convert('RGB')
    image.thumbnail((280,396))
    card=Image.new('RGB',(300,426),'#e4e8ed')
    card.paste(image,((300-image.width)//2,8))
    ImageDraw.Draw(card).text((12,407),f'Page {i}',fill='black')
    thumbs.append(card)
    text=page.get_text()
    for ident in re.findall(r'\b[A-F]\.\d+\.\d+\b',text):
        report['statement_pages'].setdefault(ident,i)
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line.get('spans',[]):
                x0,y0,x1,y1=span['bbox']
                if x0<40 or x1>page.rect.width-35 or y0<20 or y1>page.rect.height-20:
                    report['boundary_violations'].append({'page':i,'text':span['text'],'bbox':span['bbox']})
for start in range(0,len(thumbs),16):
    sheet=Image.new('RGB',(1200,1704),'#c5cdd6')
    for n,thumb in enumerate(thumbs[start:start+16]):
        sheet.paste(thumb,((n%4)*300,(n//4)*426))
    p=OUT/f'contact_{start//16+1:02d}.png';sheet.save(p)
    report['contact_sheets'].append(str(p))
(ROOT/'evidence/pdf_layout_audit.json').write_text(json.dumps(report,indent=2)+'\n')
print('PAGES',len(doc))
print('BOUNDARY_VIOLATIONS',len(report['boundary_violations']))
print('CONTACT_SHEETS',len(report['contact_sheets']))
for key in ['A.1.1','A.5.2','B.1.1','B.4.2','C.1.1','C.2.3','C.3.3','D.1.6','D.2.3','E.1.1','E.2.1','E.2.3','F.1.1','F.2.2','F.3.3']:
    print(key,report['statement_pages'].get(key))
assert not report['boundary_violations']

