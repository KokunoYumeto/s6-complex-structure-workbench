"""All-page bounds/log checks and Poppler renders of every changed proof page."""
from pathlib import Path
from datetime import datetime,timezone
import fitz,hashlib,json,re,subprocess
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];p=R/'S6_06_BLIND_paper.pdf';d=fitz.open(p)
log=p.with_suffix('.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
assert not any(x>2 for x in over)
assert not re.search(r'undefined|Missing character|LaTeX Error|Label\(s\) may have changed|Rerun to get|Table widths have changed',log)
keys=['P3K.75','P3K.76','P3K.94','P3K.95','P3K.96','P3R.1'];starts={};outside=[]
for i,page in enumerate(d):
 text=' '.join(page.get_text().split())
 for key in keys:
  if 'Statement '+key+' ' in text:starts[key]=i+1
 for w in page.get_text('words'):
  if w[0]<-.5 or w[1]<-.5 or w[2]>page.rect.width+.5 or w[3]>page.rect.height+.5:outside.append({'page':i+1,'word':w[4],'box':w[:4]})
assert not outside;assert len(starts)==len(keys),starts
nums={1,3,18,len(d),starts['P3K.95']-1};nums.update(range(starts['P3K.75'],starts['P3K.76']+1));nums.update(range(starts['P3K.95'],starts['P3R.1']+1));nums=sorted(nums)
dest=R/'records/render_master73';dest.mkdir(exist_ok=False);sheets={}
for n in nums:
 prefix=dest/f'page_{n:03d}'
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-r','100','-png',str(p),str(prefix)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
for start in range(0,len(nums),6):
 sheet=Image.new('RGB',(1200,2580),'#dddddd');draw=ImageDraw.Draw(sheet)
 for j,n in enumerate(nums[start:start+6]):
  im=Image.open(dest/f'page_{n:03d}.png').convert('RGB');im.thumbnail((580,820));x=(j%2)*600+(600-im.width)//2;y=(j//2)*860+30;sheet.paste(im,(x,y));draw.text(((j%2)*600+15,(j//2)*860+8),f'Page {n}',fill='black')
 sheet.save(dest/f'contact-{start//6+1:02}.png');sheets[str(start//6+1)]=nums[start:start+6]
record={'utc':datetime.now(timezone.utc).isoformat(),'master_build':73,'status':'PASS_PENDING_DIRECT_VISUAL_REVIEW','pages':len(d),'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pdf_bytes':p.stat().st_size,'overfull_boxes':len(over),'overfull_above2pt':0,'max_overfull_pt':max(over,default=0),'out_of_page_words':outside,'statement_starts':starts,'rendered_pages':nums,'contact_sheets':sheets,'renderer':'Poppler pdftoppm at100dpi','scope':'Every integrated K95/K96 page and transitions, full revised K75 obligation register, opening/reference page18/final page. All manuscript pages checked for outside bounds; both standalone proofs have full-page direct reviews.'}
(R/'records/master73_audit.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
