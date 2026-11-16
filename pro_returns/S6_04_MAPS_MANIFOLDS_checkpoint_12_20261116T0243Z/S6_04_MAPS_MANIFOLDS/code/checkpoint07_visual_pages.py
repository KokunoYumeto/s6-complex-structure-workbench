"""Render all newly added mathematical pages and both repaired regions."""
from pathlib import Path
import json,re,subprocess
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
pdf=root/'S6_04_MAPS_MANIFOLDS_paper.pdf'
out=root/'records/pdf_qa'
textfile=root/'records/checkpoint_07_paper.txt'
subprocess.run(['pdftotext','-layout',str(pdf),str(textfile)],check=True)
pages=textfile.read_text().split('\f')
tags=['D.2.23','D.2.24','D.2.25','D.2.26','E.2.13','E.2.14','E.2.15','F.2.31','F.2.32']
locations={}
for tag in tags:
    pat=re.compile(r'(?:Theorem|Proposition|Corollary)\s+'+re.escape(tag)+r'\s+\(Proved')
    found=[i+1 for i,p in enumerate(pages) if pat.search(p)]
    assert len(found)==1,(tag,found)
    locations[tag]=found[0]
selected=sorted(set(range(119,130))|set(range(156,165))|set(range(204,211)))
for p in selected:
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','100','-singlefile','-png',str(pdf),str(out/f'cp07_{p:03}')],check=True)
for group in range((len(selected)+7)//8):
    part=selected[group*8:group*8+8]
    sheet=Image.new('RGB',(1100,790*((len(part)+1)//2)),'#ddd')
    for i,p in enumerate(part):
        im=Image.open(out/f'cp07_{p:03}.png').convert('RGB');im.thumbnail((530,750))
        x,y=550*(i%2),790*(i//2);sheet.paste(im,(x+(550-im.width)//2,y+25))
        ImageDraw.Draw(sheet).text((x+12,y+6),f'Page {p}',fill='black')
    sheet.save(out/f'cp07_contact_{group+1}.png')
record={'statement_pages':locations,'extra_rendered_pages':selected,'repaired_line_pages':[125,126,207]}
(out/'checkpoint_07_extra_pages.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
