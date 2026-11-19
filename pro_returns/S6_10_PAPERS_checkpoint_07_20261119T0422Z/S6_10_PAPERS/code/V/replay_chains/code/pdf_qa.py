"""Render a spread of manuscript pages and record exact log overflows."""
from pathlib import Path
import re,json,hashlib,subprocess
from PIL import Image, ImageOps, ImageDraw
root=Path(__file__).resolve().parents[1]
pdf=root/'S6_04_MAPS_MANIFOLDS_paper.pdf'
out=root/'records/pdf_qa';out.mkdir(exist_ok=True)
info=subprocess.check_output(['pdfinfo',str(pdf)],text=True)
n=int(re.search(r'Pages:\s+(\d+)',info).group(1))
pages=sorted(set([1,2,6,7,10,18,25,34,38,39,43,49,n]
                 +[1+round(i*(n-1)/10) for i in range(11)]))
pages=[p for p in pages if p<=n]
for p in pages:
 subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','80',
                 '-singlefile','-png',str(pdf),str(out/f'page_{p:03}')],check=True)
thumbs=[]
for p in pages:
 im=Image.open(out/f'page_{p:03}.png').convert('RGB')
 im.thumbnail((400,566))
 tile=Image.new('RGB',(420,596),'#ddd');tile.paste(im,((420-im.width)//2,22))
 ImageDraw.Draw(tile).text((10,5),f'Page {p}',fill='black')
 thumbs.append(tile)
sheet=Image.new('RGB',(420*3,596*((len(thumbs)+2)//3)),'white')
for i,im in enumerate(thumbs):sheet.paste(im,((i%3)*420,(i//3)*596))
sheet.save(out/'contact_sheet.png')
log=(root/'records/build_pass_4.log').read_text()
overflow=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)',log)]
record={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'pages':n,'rendered_pages':pages,'overfull_boxes':len(overflow),
        'overflows_over_2pt':sum(x>2 for x in overflow),'max_overflow_pt':max(overflow,default=0),
        'unresolved_citations':re.findall(r"Citation `([^']+)'[^\n]*undefined",log),
        'visual_review':'Awaiting image inspection by the research assistant.'}
(out/'qa.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
