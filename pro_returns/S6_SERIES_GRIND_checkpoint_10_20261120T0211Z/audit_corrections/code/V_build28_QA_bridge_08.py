"""Carry only actually viewed V pages to build28 by complete page-pixel equality."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import fitz
from PIL import Image, ImageDraw

root=Path(__file__).resolve().parents[2]
own=root/'audit_corrections'
dest=own/'QA_V_build28';dest.mkdir(exist_ok=True)
pdf=root/'S6_SERIES_GRIND_V.pdf'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
doc=fitz.open(pdf)
cache={}
def render(n,scale=1.8):
    key=(n,scale)
    if key not in cache:
        pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
        im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        im.thumbnail((1072,1518));cache[key]=im
    return cache[key]

bridge=[]
sources=[('audit_root/build26_V_changed_visual_QA.json','sheets',1.65),
         ('audit_paper_i/closure_07/build26_V_visual_QA.json','sheets',1.8),
         ('audit_corrections/V_build27_visual_QA_07.json','actually_viewed_new_sheets',1.8)]
for name,key,scale in sources:
    receipt=json.loads((root/name).read_text())
    for sheet in receipt[key]:
        oldfile=Path(sheet.get('file',sheet.get('path')))
        if not oldfile.is_absolute():oldfile=root/oldfile
        assert sha(oldfile)==sheet['sha256']
        old=Image.open(oldfile).convert('RGB')
        for col,n in enumerate(sheet['pages']):
            current=render(n,scale)
            prior=old.crop((29+1130*col,40,29+1130*col+current.width,40+current.height))
            h0=hashlib.sha256(prior.tobytes()).hexdigest()
            h1=hashlib.sha256(current.tobytes()).hexdigest()
            bridge.append({'page':n,'prior_receipt':name,'prior_sheet':str(oldfile.relative_to(root)),
                           'prior_pdf_sha256':receipt['pdf_sha256'],'prior_pdf_pixel_sha256':h0,
                           'current_pdf_pixel_sha256':h1,'pixel_identical':h0==h1,'scale':scale})
pages=sorted(x['page'] for x in bridge if not x['pixel_identical'])
sheets=[]
for i in range(0,len(pages),2):
    nums=pages[i:i+2];canvas=Image.new('RGB',(2260,1610),'#e8e8e8');draw=ImageDraw.Draw(canvas)
    for col,n in enumerate(nums):
        canvas.paste(render(n),(29+1130*col,40));draw.text((18+1130*col,13),f'Build28 V, page {n}',fill='black')
    path=dest/f'V_changed_{i//2+1:02d}.png';canvas.save(path)
    sheets.append({'path':str(path.relative_to(root)),'pages':nums,'sha256':sha(path),'actually_viewed':False})
out={'utc':datetime.now(timezone.utc).isoformat(),'pdf':str(pdf),'pdf_sha256':sha(pdf),'page_count':len(doc),
     'method':'Whole PDF-page pixels compared at the exact prior render scale; only external sheet caption is excluded.',
     'prior_pages':bridge,'identical_prior_pages':sum(x['pixel_identical'] for x in bridge),
     'changed_prior_pages':pages,'new_sheets':sheets,'new_inspection_state':'rendered, not yet viewed'}
(own/'V_build28_QA_bridge_08.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['pdf_sha256','page_count','identical_prior_pages','changed_prior_pages']}))
