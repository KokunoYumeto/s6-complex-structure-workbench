"""Render the new statements and both repaired lines in checkpoint06."""
from pathlib import Path
import json, re, subprocess
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
pdf = root/'S6_04_MAPS_MANIFOLDS_paper.pdf'
out = root/'records/pdf_qa'
textfile = root/'records/checkpoint_06_paper.txt'
if not textfile.exists():
    subprocess.run(['pdftotext','-layout',str(pdf),str(textfile)],check=True)
pages = textfile.read_text().split('\f')
tags = ['B.6.22','B.6.23','B.6.24','B.6.25','D.2.21','D.2.22',
        'E.2.10','E.2.11','E.2.12','F.2.25','F.2.26','F.2.27',
        'F.2.28','F.2.29','F.2.30']
locations = {}
for tag in tags:
    pat = re.compile(r'(?:Theorem|Proposition|Corollary)\s+'+re.escape(tag)+r'\s+\(Proved')
    found = [i+1 for i,p in enumerate(pages) if pat.search(p)]
    assert len(found)==1, (tag,found)
    locations[tag] = found[0]
repaired = [i+1 for i,p in enumerate(pages)
            if 'manifolds_mapping_general.py' in p or 'fourfolds_relative_six_probe.py' in p]
selected = sorted(set(locations.values()) | set(repaired)
                  | {locations['D.2.22']+1,locations['D.2.22']+2,
                     locations['D.2.22']+3,locations['D.2.22']+4,
                     locations['F.2.30']+1})
for p in selected:
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','100',
                    '-singlefile','-png',str(pdf),str(out/f'extra_{p:03}')],check=True)
for group in range((len(selected)+7)//8):
    part = selected[8*group:8*group+8]
    sheet = Image.new('RGB',(1100,790*((len(part)+1)//2)),'#dddddd')
    for i,p in enumerate(part):
        im=Image.open(out/f'extra_{p:03}.png').convert('RGB')
        im.thumbnail((530,750))
        x,y=550*(i%2),790*(i//2)
        sheet.paste(im,(x+(550-im.width)//2,y+25))
        ImageDraw.Draw(sheet).text((x+12,y+6),f'Page {p}',fill='black')
    sheet.save(out/f'extra_contact_{group+1}.png')
record={'statement_pages':locations,'repaired_line_pages':repaired,
        'extra_rendered_pages':selected}
(out/'checkpoint_06_extra_pages.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
