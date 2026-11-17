"""Render the rebuilt K88/K90 sections and record exact pre-visual checks."""
from pathlib import Path
import fitz,re,json,hashlib
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
for n in (88,90):
    pdf=ROOT/f'code/part3_root/k{n}_standalone.pdf'
    log=(ROOT/f'code/part3_root/k{n}_standalone.log').read_text()
    over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
    missing=[l for l in log.splitlines() if 'Missing character' in l or ('Warning' in l and ('undefined' in l or 'Rerun' in l)) or 'Label(s) may have changed' in l]
    assert max(over,default=0)<=2 and not missing,(n,over,missing)
    folder=ROOT/f'records/k{n}_recovered_qa';folder.mkdir(exist_ok=True)
    doc=fitz.open(pdf); thumbs=[];outside=[]
    for i,page in enumerate(doc):
        for word in page.get_text('words'):
            if word[0]<0 or word[1]<0 or word[2]>page.rect.width or word[3]>page.rect.height:outside.append([i+1,word])
        pix=page.get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False)
        out=folder/f'page_{i+1:02d}.png';pix.save(out)
        im=Image.open(out).convert('RGB');im.thumbnail((700,1000));thumbs.append(im)
    assert not outside
    sheet=Image.new('RGB',(1440,2060),'#dddddd');draw=ImageDraw.Draw(sheet)
    for i,im in enumerate(thumbs):
        x=10+(i%2)*720;y=30+(i//2)*1020;sheet.paste(im,(x,y));draw.text((x,y-20),f'K{n} page {i+1}',fill='black')
    contact=folder/'all_pages.png';sheet.save(contact)
    rec={'status':'PENDING_DIRECT_VISUAL_REVIEW','reconstruction':True,'pages':len(doc),'pdf':str(pdf.relative_to(ROOT)),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'overfull_boxes':len(over),'overfull_above_2pt':0,'max_overfull_pt':max(over,default=0),'missing_undefined_rerun':missing,'page_boundaries':'PASS','rendered_pages':list(range(1,len(doc)+1)),'contact_sheet':str(contact.relative_to(ROOT))}
    (ROOT/f'records/k{n}_standalone_visual_qa.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(n,len(doc),contact)
