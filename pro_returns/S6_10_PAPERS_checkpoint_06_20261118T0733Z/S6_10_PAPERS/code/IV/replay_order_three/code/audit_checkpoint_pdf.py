"""Render the current manuscript and retain its exact overflow audit."""
from pathlib import Path
import re,json,sys
import fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
n=int(sys.argv[1])
pdf=fitz.open(ROOT/'S6_06_BLIND_paper.pdf')
log=(ROOT/'S6_06_BLIND_paper.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
selected={1,18,22,27,34,44,45,50,60,70,len(pdf)}
needles=['Statement P1.18','Statement P1.19','Statement P4.20','Statement P4R.1','Statement P5.7']
if n>=3:
    needles += [f'Statement P3F.{i}' for i in range(21,26)]
    needles += [f'Statement P3K.{i}' for i in range(1,9)]
    needles += [f'Statement P4.{i}' for i in range(21,27)]
    needles += [f'Statement P4R.{i}' for i in range(3,10)]
if n>=4:
    needles += [f'Statement P1B.{i}' for i in range(1,3)]
    needles += [f'Statement P3R.{i}' for i in range(1,3)]
    needles += [f'Statement P3F.{i}' for i in range(26,31)]
    needles += [f'Statement P3K.{i}' for i in range(9,13)]
    needles += [f'Statement P4.{i}' for i in range(27,40)]
    needles += [f'Statement P4R.{i}' for i in range(10,14)]
if n>=5:
    needles += [f'Statement P3F.{i}' for i in range(31,36)]
    needles += [f'Statement P3K.{i}' for i in range(13,20)]
    needles += [f'Statement P4.{i}' for i in range(39,50)]
    needles += [f'Statement P4R.{i}' for i in range(13,17)]
if n>=6:
    needles += [f'Statement P3F.{i}' for i in range(34,40)]
    needles += [f'Statement P3K.{i}' for i in range(17,26)]
    needles += [f'Statement P4.{i}' for i in range(47,60)]
    needles += [f'Statement P4R.{i}' for i in range(16,22)]
for i,page in enumerate(pdf):
    page_text=' '.join(page.get_text().split())
    if any(s in page_text for s in needles):selected.add(i+1)
if n>=6:
    starts=[]
    for i,page in enumerate(pdf):
        txt=' '.join(page.get_text().split())
        for match in re.finditer(r'Statement\s+(P\d[A-Z]?\.\d+)',txt):starts.append((match[1],i+1))
    new_ids={f'P3F.{j}' for j in range(34,36)}|{f'P3K.{j}' for j in range(17,22)}|{f'P4.{j}' for j in range(47,54)}|{f'P4R.{j}' for j in range(16,19)}
    if n>=7:
        new_ids |= {f'P3K.{j}' for j in range(22,24)}|{f'P4.{j}' for j in range(54,59)}|{f'P4R.{j}' for j in range(19,21)}
    if n>=8:
        new_ids |= {f'P3F.{j}' for j in range(36,41)}|{f'P3K.{j}' for j in range(24,26)}
    if n>=9:
        new_ids |= {f'P3F.{j}' for j in range(41,50)}|{f'P3K.{j}' for j in range(26,31)}
    if n>=10:
        new_ids |= {f'P3F.{j}' for j in range(50,55)}|{f'P3K.{j}' for j in range(31,37)}
    if n>=11:
        new_ids |= {f'P3F.{j}' for j in range(55,57)}|{f'P3K.{j}' for j in range(37,39)}
    for k,(sid,start) in enumerate(starts):
        if sid in new_ids:
            end=starts[k+1][1] if k+1<len(starts) else len(pdf)
            selected.update(range(start,end+1))
dest=ROOT/f'records/render_checkpoint{n:02d}'
dest.mkdir(exist_ok=True)
for p in sorted(selected):
    pix=pdf[p-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False)
    pix.save(dest/f'page_{p:03d}.png')
pages=sorted(selected)
for start in range(0,len(pages),8):
    batch=pages[start:start+8]
    sheet=Image.new('RGB',(4*310,2*460),'#dddddd')
    draw=ImageDraw.Draw(sheet)
    for j,p in enumerate(batch):
        im=Image.open(dest/f'page_{p:03d}.png')
        im.thumbnail((300,425))
        x=(j%4)*310+(310-im.width)//2;y=(j//4)*460+25
        sheet.paste(im,(x,y));draw.text(((j%4)*310+12,(j//4)*460+7),f'Page {p}',fill='black')
    sheet.save(dest/f'contact_{start//8+1}.png')
record={'checkpoint':n,'pages':len(pdf),'overfull_boxes':len(over),
        'overfull_over_2pt':sum(x>2 for x in over),'max_overfull_pt':max(over,default=0),
        'rendered_pages':pages,'visual_inspection':'pending direct image review',
        'source_log':'S6_06_BLIND_paper.log'}
(ROOT/f'records/typesetting_checkpoint{n:02d}.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
