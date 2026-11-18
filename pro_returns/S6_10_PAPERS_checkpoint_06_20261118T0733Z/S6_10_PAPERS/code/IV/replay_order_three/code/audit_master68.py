"""Check all page boundaries and render the new proofs and a document-wide spread."""
from pathlib import Path
from datetime import datetime,timezone
import fitz,hashlib,json,re
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
p=root/'S6_06_BLIND_paper.pdf';d=fitz.open(p)
log=p.with_suffix('.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
assert not any(x>2 for x in over)
assert not re.search(r'undefined|Missing character|LaTeX Error|Label\(s\) may have changed|Rerun to get',log)
starts={};outside=[]
keys=['P3K.75','P3K.76','P3K.79','P3K.80','P3K.81','P3K.82','P3K.83','P3K.84','P3R.1']
for i,page in enumerate(d):
 text=' '.join(page.get_text().split())
 for key in keys:
  if 'Statement '+key+' ' in text:starts[key]=i+1
 for w in page.get_text('words'):
  if w[0]<-0.5 or w[1]<-0.5 or w[2]>page.rect.width+0.5 or w[3]>page.rect.height+0.5:
   outside.append({'page':i+1,'word':w[4],'box':w[:4]})
assert not outside
assert len(starts)==len(keys),starts
nums=set([1,3,18,100,200,300,400,450,650,len(d)])
nums.update(range(starts['P3K.75'],starts['P3K.76']+1))
for begin,end in [('P3K.80','P3K.81'),('P3K.81','P3K.82')]:
 lo,hi=starts[begin],starts[end];nums.update([lo,(lo+hi)//2,hi-1,hi])
nums.update(range(starts['P3K.82'],starts['P3R.1']+1))
nums=sorted(nums)
dest=root/'records/render_master68';dest.mkdir(exist_ok=False);sheets={}
for start in range(0,len(nums),6):
 sheet=Image.new('RGB',(1200,2580),'#dddddd');draw=ImageDraw.Draw(sheet)
 for j,n in enumerate(nums[start:start+6]):
  pix=d[n-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1),alpha=False)
  im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((580,820))
  x=(j%2)*600+(600-im.width)//2;y=(j//2)*860+30
  sheet.paste(im,(x,y));draw.text(((j%2)*600+15,(j//2)*860+8),f'Page {n}',fill='black')
 sheet.save(dest/f'contact-{start//6+1}.png');sheets[str(start//6+1)]=nums[start:start+6]
r={'utc':datetime.now(timezone.utc).isoformat(),'master_build':68,
 'status':'PASS_PENDING_DIRECT_VISUAL_REVIEW','pages':len(d),
 'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pdf_bytes':p.stat().st_size,
 'overfull_boxes':len(over),'overfull_above2pt':0,'max_overfull_pt':max(over,default=0),
 'out_of_page_words':outside,'statement_starts':starts,'rendered_pages':nums,'contact_sheets':sheets,
 'scope':'Every page of K82--84 and revised K75, K80--81 transitions/midpoints after all-page standalone reviews, prior overflow page18 and a document-wide spread.'}
(root/'records/master68_audit.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
