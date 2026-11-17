"""Render all newly included K57--60 pages and a sample of the full master."""
from datetime import datetime,timezone
from pathlib import Path
import json,re
import fitz
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parents[1]
pdf=fitz.open(root/'S6_06_BLIND_paper.pdf')
log=(root/'S6_06_BLIND_paper.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
assert not any(x>2 for x in over),over
assert 'Output written on' in log
selected={1,18,85,154,len(pdf)}|set(range(25,len(pdf)+1,25))
starts=[]
for i,page in enumerate(pdf,1):
    text=' '.join(page.get_text().split())
    for match in re.finditer(r'Statement\s+(P\d[A-Z]?\.\d+)',text):
        starts.append((match[1],i))
new_ids={f'P3K.{i}' for i in range(57,64)}
modified_ids=set(json.loads((root/'records/scalar_fan_correction_scope.json').read_text())['scope'])
ranges={}
modified={}
for j,(sid,start) in enumerate(starts):
    if sid in new_ids:
        end=starts[j+1][1] if j+1<len(starts) else len(pdf)
        ranges[sid]=[start,end]
        selected.update(range(start,end+1))
    if sid in modified_ids:
        end=starts[j+1][1] if j+1<len(starts) else len(pdf)
        modified[sid]=[start,end]
        selected.update(range(max(1,start-1),min(end,start+2)+1))
assert set(ranges)==new_ids,ranges
dest=root/'records/render_checkpoint15'
dest.mkdir(exist_ok=True)
pages=sorted(selected)
for p in pages:
    pdf[p-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(dest/f'page_{p:03d}.png')
contacts={}
for start in range(0,len(pages),8):
    batch=pages[start:start+8]
    sheet=Image.new('RGB',(1240,920),'#dddddd')
    draw=ImageDraw.Draw(sheet)
    for j,p in enumerate(batch):
        im=Image.open(dest/f'page_{p:03d}.png')
        im.thumbnail((300,425))
        x=(j%4)*310+(310-im.width)//2
        y=(j//4)*460+25
        sheet.paste(im,(x,y))
        draw.text(((j%4)*310+12,(j//4)*460+7),f'Page {p}',fill='black')
    number=start//8+1
    sheet.save(dest/f'contact_{number}.png')
    contacts[str(number)]=batch
record={
 'utc':datetime.now(timezone.utc).isoformat(),'checkpoint':15,'master_build':51,
 'pages':len(pdf),'overfull_boxes':len(over),'overfull_over_2pt':sum(x>2 for x in over),
 'max_overfull_pt':max(over,default=0),'before_over_2pt':sum(x>2 for x in over),
 'after_overfull_over_2pt':sum(x>2 for x in over),'rendered_pages':pages,
 'rendered_page_count':len(pages),'new_proof_ranges':ranges,'modified_proof_ranges':modified,
 'contact_sheets':contacts,
 'sample_policy':'Every page of K57--63, every corrected statement opening and its neighbouring pages, the existing overflow page18, and a sample across the entire paper.',
 'visual_inspection':'pending direct image review','source_log':'S6_06_BLIND_paper.log'
}
(root/'records/typesetting_checkpoint15.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
