"""Render every new proof page in the eighth frozen manuscript."""
from pathlib import Path
import json,re,subprocess
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
pdf=root/'S6_04_MAPS_MANIFOLDS_paper.pdf'
out=root/'records/pdf_qa';out.mkdir(exist_ok=True)
textfile=root/'records/checkpoint_08_paper.txt'
subprocess.run(['pdftotext','-layout',str(pdf),str(textfile)],check=True)
pages=textfile.read_text().split('\f')
tags=['D.2.27','D.2.28','D.2.29','D.2.30','E.2.16','E.2.17',
      'F.2.33','F.2.34','F.2.36','F.2.37','F.2.38']
locations={}
for tag in tags:
    pat=re.compile(r'(?:Theorem|Proposition|Corollary)\s+'+re.escape(tag)+r'\s+\(Proved')
    found=[i+1 for i,p in enumerate(pages) if pat.search(p)]
    assert len(found)==1,(tag,found)
    locations[tag]=found[0]
assert locations=={'D.2.27':129,'D.2.28':133,'D.2.29':134,'D.2.30':137,
                  'E.2.16':175,'E.2.17':179,'F.2.33':229,'F.2.34':231,
                  'F.2.36':232,'F.2.37':234,'F.2.38':236},locations
selected=sorted(set(range(129,140))|set(range(175,184))|set(range(229,239)))
for p in selected:
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','100','-singlefile',
                    '-png',str(pdf),str(out/f'cp08_{p:03}')],check=True)
for group in range((len(selected)+7)//8):
    part=selected[group*8:group*8+8]
    sheet=Image.new('RGB',(1100,790*((len(part)+1)//2)),'#ddd')
    for i,p in enumerate(part):
        im=Image.open(out/f'cp08_{p:03}.png').convert('RGB');im.thumbnail((530,750))
        x,y=550*(i%2),790*(i//2);sheet.paste(im,(x+(550-im.width)//2,y+25))
        ImageDraw.Draw(sheet).text((x+12,y+6),f'Page {p}',fill='black')
    sheet.save(out/f'cp08_contact_{group+1}.png')
record={'statement_pages':locations,'extra_rendered_pages':selected,
        'repaired_regions':['E.2.17 definition display and program path',
                            'F.2.33 program paths','F.2.36 display delimiters'],
        'repaired_line_pages':[179,181,230,232]}
(out/'checkpoint_08_extra_pages.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
