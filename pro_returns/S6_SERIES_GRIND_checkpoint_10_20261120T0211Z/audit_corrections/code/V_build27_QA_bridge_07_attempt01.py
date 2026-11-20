"""Transfer previously viewed PDF pixels and render additional current pages.
Pixel equality is recorded separately from actual new image inspection.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import fitz
from PIL import Image, ImageDraw

root=Path(__file__).resolve().parents[2]
own=root/'audit_corrections'
dest=own/'QA_V_build27';dest.mkdir(exist_ok=True)
pdf=root/'S6_SERIES_GRIND_V.pdf';pdf_hash=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert pdf_hash=='557f711522ed16fc3d2873e9ab38c0de26baf0aed7b1fbc1c3d375caecd85ddf'
doc=fitz.open(pdf)
receipts=['audit_root/build26_V_changed_visual_QA.json','audit_paper_i/closure_07/build26_V_visual_QA.json']
cache={}
def render(n):
    if n not in cache:
        pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8),alpha=False)
        im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((1072,1518));cache[n]=im
    return cache[n]
bridge=[]
for name in receipts:
    receipt=json.loads((root/name).read_text())
    for sheet in receipt['sheets']:
        oldfile=Path(sheet.get('file',sheet.get('path')))
        if not oldfile.is_absolute():oldfile=root/oldfile
        assert hashlib.sha256(oldfile.read_bytes()).hexdigest()==sheet['sha256']
        old=Image.open(oldfile).convert('RGB')
        for col,n in enumerate(sheet['pages']):
            current=render(n)
            prior=old.crop((29+1130*col,40,29+1130*col+current.width,40+current.height))
            h0=hashlib.sha256(prior.tobytes()).hexdigest();h1=hashlib.sha256(current.tobytes()).hexdigest()
            bridge.append({'page':n,'prior_receipt':name,'prior_sheet':str(oldfile.relative_to(root)),
                           'prior_pdf_sha256':receipt['pdf_sha256'],'prior_pdf_pixel_sha256':h0,
                           'current_pdf_pixel_sha256':h1,'pixel_identical':h0==h1})
pages=sorted(set([80]+list(range(86,90))+list(range(112,116))+list(range(130,143))+[208,209,210]+[x['page'] for x in bridge if not x['pixel_identical']]))
sheets=[]
for i in range(0,len(pages),2):
    nums=pages[i:i+2];canvas=Image.new('RGB',(2260,1610),'#e8e8e8');draw=ImageDraw.Draw(canvas)
    for col,n in enumerate(nums):
        canvas.paste(render(n),(29+1130*col,40));draw.text((18+1130*col,13),f'Build27 V, page {n}',fill='black')
    path=dest/f'V_{i//2+1:02d}.png';canvas.save(path)
    sheets.append({'path':str(path.relative_to(root)),'pages':nums,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'actually_viewed':False})
out={'utc':datetime.now(timezone.utc).isoformat(),'pdf':str(pdf),'pdf_sha256':pdf_hash,'page_count':len(doc),
     'method':'Actual PDF-pixel crops from previously viewed two-page sheets compared byte-for-byte with current same-page rendering, excluding only the external contact-sheet caption; the entire PDF page including its header/footer is compared.',
     'prior_pages':bridge,'identical_prior_pages':sum(x['pixel_identical'] for x in bridge),'changed_prior_pages':[x['page'] for x in bridge if not x['pixel_identical']],
     'new_pages':pages,'new_sheets':sheets,'new_inspection_state':'rendered, not yet viewed'}
(own/'V_build27_QA_bridge_07.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'identical_prior_pages':out['identical_prior_pages'],'changed_prior_pages':out['changed_prior_pages'],'new_pages':pages,'new_sheets':len(sheets)}))
