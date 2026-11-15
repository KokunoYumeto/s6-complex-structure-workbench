#!/usr/bin/env python3
"""Render a spread of pages, plus every newly affected proof location."""
from pathlib import Path
import fitz,json,re,sys
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).resolve().parents[1]
pdf=root/'S6_05_ARITHMETIC_paper.pdf'
stage=sys.argv[1] if len(sys.argv)>1 else 'hour3'
assert re.fullmatch(r'hour[1-9][0-9]*|final',stage)
doc=fitz.open(pdf);out=root/f'build/qa_{stage}';out.mkdir(exist_ok=True)
needles=['A.4.7','A.4.8','A.5.4','A.5.6','A.5.7','A.5.8','C.6.R5','C.7.5;','C.7.9;','C.7.10;','C.7.11;','C.7.12;']
found={}
for i,p in enumerate(doc):
 t=p.get_text()
 for term in needles:
  matched=term in t
  if term=='A.5.6':matched='A.5.6 (Proved smoothed' in ' '.join(t.split())
  if term=='A.5.4':matched='Statement A.5.4 (Open:' in ' '.join(t.split())
  if term=='A.5.8':matched='A.5.8 (Proved:' in ' '.join(t.split())
  if matched and term not in found:found[term]=i+1
pages={1,len(doc),7,40,49,64,80,81,82,95}
if stage in {'hour4','final'}:pages.update({136,137})
for p in found.values():pages.update(range(p,min(p+4,len(doc))+1))
if 'A.5.8' in found:pages.update(range(found['A.5.8'],min(found['A.5.8']+6,len(doc))+1))
if 'C.7.12;' in found:pages.update(range(found['C.7.12;'],min(found['C.7.12;']+5,len(doc))+1))
pages=sorted(p for p in pages if p<=len(doc))
for p in pages:
 doc[p-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(out/f'page_{p:03d}.png')
for z in range(0,len(pages),4):
 group=pages[z:z+4];sheet=Image.new('RGB',(1260,1820),'#dddddd');dr=ImageDraw.Draw(sheet)
 for j,p in enumerate(group):
  im=Image.open(out/f'page_{p:03d}.png');im.thumbnail((610,865))
  x=10+(j%2)*630;y=30+(j//2)*910
  sheet.paste(im,(x,y));dr.text((x,y-20),f'Page {p}',fill='black')
 sheet.save(out/f'contact_{z//4+1:02d}.png')
log=(root/'build/S6_05_ARITHMETIC_paper.log').read_text()
overs=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
result={'pdf_pages':len(doc),'rendered_pages':pages,'located_statements':found,
        'overfull_count':len(overs),'overfull_above_2pt':sum(x>2 for x in overs),
        'overfull_sizes_pt':overs,'undefined_citations_or_references':bool(re.search(r'undefined|Rerun to get',log))}
(root/f'records/pdf_qa_{stage}.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
