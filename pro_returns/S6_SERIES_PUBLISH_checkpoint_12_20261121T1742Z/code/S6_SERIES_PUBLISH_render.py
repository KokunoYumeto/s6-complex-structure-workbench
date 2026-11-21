"""Render all final-reading pages and bind each image to its PDF byte hash."""
from pathlib import Path
import argparse, hashlib, json
import fitz

p=argparse.ArgumentParser()
p.add_argument('pdf',type=Path)
p.add_argument('--output-dir',type=Path,required=True)
p.add_argument('--scale',type=float,default=1.6)
a=p.parse_args()
a.output_dir.mkdir(parents=True,exist_ok=True)
sha=hashlib.sha256(a.pdf.read_bytes()).hexdigest()
doc=fitz.open(a.pdf)
rows=[]
for i,page in enumerate(doc):
    image_path=a.output_dir/f'page_{i+1:03d}.png'
    pix=page.get_pixmap(matrix=fitz.Matrix(a.scale,a.scale),alpha=False)
    pix.save(image_path)
    text_path=a.output_dir/f'page_{i+1:03d}.txt'
    text_path.write_text(page.get_text())
    rows.append({'page':i+1,'image':str(image_path.resolve()),
                 'image_sha256':hashlib.sha256(image_path.read_bytes()).hexdigest(),
                 'text':str(text_path.resolve()),'width':pix.width,'height':pix.height})
manifest={'pdf':str(a.pdf.resolve()),'pdf_sha256':sha,'pages':len(doc),'scale':a.scale,'rendered_pages':rows,
          'reading_status':'rendering is not a reading; page inspection must be recorded separately'}
(a.output_dir/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({k:v for k,v in manifest.items() if k!='rendered_pages'}))
