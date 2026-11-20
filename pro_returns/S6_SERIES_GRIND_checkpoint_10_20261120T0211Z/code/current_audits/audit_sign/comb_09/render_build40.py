"""Render the assigned complete build40 Paper II scopes after build completion."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re
import unicodedata
import fitz

HERE=Path(__file__).resolve().parent
WORK=HERE.parents[1]
OUT=HERE/'build40_visual_QA'
OUT.mkdir(exist_ok=True)
pdf=WORK/'S6_SERIES_GRIND_II.pdf'
aux=WORK/'S6_SERIES_GRIND_II.aux'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pdf_sha=sha(pdf)
aux_text=aux.read_text()

def groups(text):
    result=[];depth=0;start=None
    for i,c in enumerate(text):
        if c=='{':
            if depth==0:start=i+1
            depth+=1
        elif c=='}':
            depth-=1
            if depth==0:result.append(text[start:i])
            if depth<0:break
    return result

def label_page(label):
    line=next(x for x in aux_text.splitlines() if x.startswith('\\newlabel{'+label+'}'))
    fields=groups(line[len('\\newlabel{'+label+'}') :])
    record=groups(fields[0]);return int(record[1])

doc=fitz.open(pdf)
page_text=[page.get_text() for page in doc]
def norm(t):return re.sub('[^a-z0-9]','',unicodedata.normalize('NFKC',t).lower())
normalized=[norm(x) for x in page_text]
def find_pages(phrase,limit=None):
    key=norm(phrase)
    return [i+1 for i,t in enumerate(normalized[:limit]) if key in t]

pages={}
def add_range(a,b,why):
    assert 1<=a<=b<=len(doc),(a,b,len(doc))
    for n in range(a,b+1):pages.setdefault(n,[]).append(why)

add_range(1,1,'Entire changed abstract/title page')
f0,f1=label_page('series:II:F'),label_page('series:II:G')
add_range(f0,f1,'Complete main F, including transition to main G')
outline_first=find_pages('At a smooth fibre the boundary',80)
outline_last=find_pages('each central node',80)
assert len(outline_first)==1 and len(outline_last)==1,(outline_first,outline_last)
add_range(max(1,outline_first[0]-1),outline_last[0]+1,
          'Complete F outline, including preceding/following page transitions')
e0,e1=label_page('inv:E2.5'),label_page('inv:E2.4')
add_range(max(1,e0-1),e1,'Complete new E2.5 statement, seven-step proof, source comparison and transitions')
open0=label_page('inv:E2.3')
open_last=find_pages('Their upper endpoints have not been shown')
assert len(open_last)==1,open_last
add_range(open0,open_last[0],
          'Complete revised E2.3 statement/proof and attained-lower-endpoint paragraph')

records=[]
for n in sorted(pages):
    out=OUT/f'II_build40_page_{n:04d}.png'
    doc[n-1].get_pixmap(matrix=fitz.Matrix(5/3,5/3),alpha=False).save(out)
    records.append({'page':n,'path':str(out.relative_to(WORK)),
                    'sha256':sha(out),'reasons':pages[n]})
assert sha(pdf)==pdf_sha,'PDF changed during render'
manifest={
 'utc':dt.datetime.now(dt.timezone.utc).isoformat(),
 'state':'rendered; actual image inspection still required',
 'pdf_path':str(pdf.relative_to(WORK)),'pdf_sha256':pdf_sha,'page_count':len(doc),
 'aux_sha256':sha(aux),
 'source_sha256':{str(p.relative_to(WORK)):sha(p) for p in
   [WORK/'parts/II.body.linked.tex',WORK/'audit_sign/frontmatter_II.tex',
    WORK/'S6_SERIES_GRIND_II.tex',WORK/'audit_sign/frontmatter_II_map.json']},
 'label_pages':{x:label_page(x) for x in ['series:II:F','series:II:G','inv:E2.5','inv:E2.4','inv:E2.3']},
 'outline_range':[outline_first[0],outline_last[0]],
 'pages':records}
(OUT/'render_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({k:manifest[k] for k in ['pdf_sha256','page_count','label_pages','outline_range']}))
print(json.dumps({'rendered_pages':[x['page'] for x in records],
                  'manifest_sha256':sha(OUT/'render_manifest.json')}))
