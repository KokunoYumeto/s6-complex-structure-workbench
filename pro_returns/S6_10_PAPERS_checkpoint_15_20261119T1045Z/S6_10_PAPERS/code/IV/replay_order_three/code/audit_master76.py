"""Check every master76 page and render the complete new K99/K100 block."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re
import fitz
from PIL import Image, ImageDraw

R=Path(__file__).resolve().parents[1]
p=R/'S6_06_BLIND_paper.pdf'
d=fitz.open(p)
log=p.with_suffix('.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
assert not any(x>2 for x in over),over
bad=re.findall(r'.*(?:undefined|Missing character|LaTeX Error|Label\(s\) may have changed|Rerun to get|Table widths have changed).*',log)
assert not bad,bad
keys=['P3K.98','P3K.99','P3K.100','P3R.1']
starts={};outside=[]
for i,page in enumerate(d):
    text=' '.join(page.get_text().split())
    for key in keys:
        if 'Statement '+key+' ' in text: starts[key]=i+1
    for w in page.get_text('words'):
        if w[0]<-.5 or w[1]<-.5 or w[2]>page.rect.width+.5 or w[3]>page.rect.height+.5:
            outside.append({'page':i+1,'word':w[4],'box':w[:4]})
assert not outside,outside
assert len(starts)==len(keys),starts
nums=sorted({1,3,18,len(d),*range(starts['P3K.99']-1,starts['P3R.1']+1)})
dest=R/'records/render_master76';dest.mkdir(exist_ok=False)
for n in nums:
    d[n-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(dest/f'page_{n:03d}.png')
sheets={}
for start in range(0,len(nums),6):
    sheet=Image.new('RGB',(1200,2580),'#dddddd');draw=ImageDraw.Draw(sheet)
    for j,n in enumerate(nums[start:start+6]):
        im=Image.open(dest/f'page_{n:03d}.png').convert('RGB');im.thumbnail((580,820))
        x=(j%2)*600+(600-im.width)//2;y=(j//2)*860+30
        sheet.paste(im,(x,y));draw.text(((j%2)*600+15,(j//2)*860+8),f'Page {n}',fill='black')
    sheet.save(dest/f'contact-{start//6+1:02}.png')
    sheets[str(start//6+1)]=nums[start:start+6]
record={'utc':datetime.now(timezone.utc).isoformat(),'master_build':76,'status':'PASS_PENDING_DIRECT_VISUAL_REVIEW','pages':len(d),'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pdf_bytes':p.stat().st_size,'overfull_boxes':len(over),'overfull_above2pt':0,'max_overfull_pt':max(over,default=0),'out_of_page_words':outside,'statement_starts':starts,'rendered_pages':nums,'contact_sheets':sheets,'renderer':'PyMuPDF at1.4scale','scope':'All manuscript page bounds and final log; every K99/K100 integration page and both neighbouring transitions, opening and final page. Both standalone proofs have complete direct visual reviews.'}
(R/'records/master76_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
