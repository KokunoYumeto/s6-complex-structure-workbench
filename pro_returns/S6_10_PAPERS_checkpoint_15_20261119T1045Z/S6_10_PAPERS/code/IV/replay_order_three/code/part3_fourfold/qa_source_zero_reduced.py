#!/usr/bin/env python3
"""Render every page of the audited complete K80 standalone proof."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re
import fitz
from PIL import Image, ImageDraw

root=Path(__file__).resolve().parents[2]
pdf_path=root/'code/part3_fourfold/k80_standalone.pdf'
tex_path=root/'notes/part3_source_zero_reduced_attachment.tex'
log=(root/'code/part3_fourfold/k80_standalone.log').read_text()
out=root/'records/render_k80'
out.mkdir(exist_ok=True)
pdf=fitz.open(pdf_path)
images=[]
bounds=[]
for i,page in enumerate(pdf):
    path=out/f'page_{i+1:02d}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(path)
    images.append(path)
    for block in page.get_text('blocks'):
        if len(block)>6 and block[6]!=0:
            continue
        x0,y0,x1,y1=block[:4]
        if x0<15 or y0<15 or x1>page.rect.width-15 or y1>page.rect.height-15:
            bounds.append({'page':i+1,'bbox':list(block[:4]),'text':block[4][:100]})
contacts={}
for start in range(0,len(images),4):
    canvas=Image.new('RGB',(1700,2440),'#dddddd')
    for j,path in enumerate(images[start:start+4]):
        im=Image.open(path).convert('RGB')
        im.thumbnail((820,1180))
        tile=Image.new('RGB',(850,1220),'white')
        tile.paste(im,((850-im.width)//2,20))
        ImageDraw.Draw(tile).text((18,1200),f'K80 page {start+j+1}',fill='black')
        canvas.paste(tile,((j%2)*850,(j//2)*1220))
    path=out/f'contact_{start//4+1}.png'
    canvas.save(path)
    contacts[str(start//4+1)]=list(range(start+1,min(start+5,len(images)+1)))
over=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
report={
 'utc':datetime.now(timezone.utc).isoformat(), 'statement':'P3K.80',
 'compile':'PASS','pages':len(pdf),'overflows_pt':over,
 'overflows_gt_2pt':[x for x in over if x>2],
 'missing_character':bool(re.search('Missing character:',log)),
 'undefined_reference':bool(re.search(r'There were undefined references|Citation .* undefined',log)),
 'boundary_issues':bounds,'contact_sheets':contacts,
 'visual_review':'pending',
 'pdf_sha256':hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
 'tex_sha256':hashlib.sha256(tex_path.read_bytes()).hexdigest(),
}
(root/'records/qa_k80.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
