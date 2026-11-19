"""Audit every page boundary and render the changed K75 and K79 master regions."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
import fitz
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
path=root/'S6_06_BLIND_paper.pdf';pdf=fitz.open(path)
assert len(pdf)==667
log=(root/'S6_06_BLIND_paper.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
assert not any(x>2 for x in over)
assert not re.search(r'undefined|Missing character|LaTeX Error|Label\(s\) may have changed',log)
outside=[];starts={}
for i,page in enumerate(pdf):
    txt=' '.join(page.get_text().split())
    for name in ('P3K.75','P3K.76','P3K.77','P3K.78','P3K.79','P3R.1'):
        if 'Statement '+name+' ' in txt:starts[name]=i+1
    for w in page.get_text('words'):
        if w[0]<-0.5 or w[1]<-0.5 or w[2]>page.rect.width+0.5 or w[3]>page.rect.height+0.5:
            outside.append({'page':i+1,'word':w[4],'box':w[:4]})
assert not outside
assert len(starts)==6,starts
selected=sorted(set([1,2,3,18,50,100,150,200,250,300,350,400,450,500,550,600,650,667]
                    +list(range(starts['P3K.75'],starts['P3K.76']+1))
                    +list(range(starts['P3K.79'],starts['P3R.1']+2))))
dest=root/'records/render_master64';dest.mkdir(exist_ok=False)
for n in selected:pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.15,1.15),alpha=False).save(dest/f'page-{n}.png')
sheets={}
for i in range(0,len(selected),6):
    pages=selected[i:i+6];sheet=Image.new('RGB',(1200,2580),'#dddddd');draw=ImageDraw.Draw(sheet)
    for j,n in enumerate(pages):
        im=Image.open(dest/f'page-{n}.png').convert('RGB');im.thumbnail((580,820))
        x=(j%2)*600+(600-im.width)//2;y=(j//2)*860+30
        sheet.paste(im,(x,y));draw.text(((j%2)*600+15,(j//2)*860+8),f'Page {n}',fill='black')
    sheet.save(dest/f'contact-{i//6+1}.png');sheets[str(i//6+1)]=pages
record={'utc':datetime.now(timezone.utc).isoformat(),'master_build':64,'pages':len(pdf),
 'status':'PASS_PENDING_DIRECT_VISUAL_REVIEW','pdf_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'pdf_bytes':path.stat().st_size,'overfull_boxes':len(over),'overfull_above2pt':0,
 'max_overfull_pt':max(over,default=0),'out_of_page_words':outside,
 'statement_starts':starts,'rendered_pages':selected,'contact_sheets':sheets,
 'policy':'All pages of revised K75 and new K79, neighbouring transitions, overflow page18, contents and a spread across the whole manuscript.'}
(root/'records/master64_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))

