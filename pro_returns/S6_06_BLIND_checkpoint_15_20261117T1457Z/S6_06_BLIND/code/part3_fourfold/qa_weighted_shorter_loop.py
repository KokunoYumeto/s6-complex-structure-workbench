#!/usr/bin/env python3
"""Standalone compile/render of audited P3K.35 without shared PDF writes."""
from pathlib import Path
from datetime import datetime, timezone
import json, os, re, subprocess
import fitz
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[2]
with (ROOT/'records/literature_fourfold.md').open('a') as log:
    log.write('\n- '+datetime.now(timezone.utc).isoformat()+
              ' — Opened own code/part3/f48_standalone.tex and notes/part3_weighted_shorter_loop.tex. '
              'Reason: isolated P3K.35 compile and render. Material: entire audited proof and exact equations.\n')
preamble=(ROOT/'code/part3/f48_standalone.tex').read_text().split(r'\begin{document}',1)[0]
src=ROOT/'code/part3_fourfold/k35_standalone.tex'
src.write_text(preamble+r'\begin{document}'+'\n'+r'\input{notes/part3_weighted_shorter_loop.tex}'+'\n'+r'\end{document}'+'\n')
runtime=ROOT.parent/'tex_runtime'
env=dict(os.environ,TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}',
         TEXFORMATS=str(runtime),TEXINPUTS=str(runtime/'packages')+'//:',
         LUAINPUTS=str(runtime/'packages')+'//:')
p=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',
                  '-output-directory=code/part3_fourfold',str(src.relative_to(ROOT))],
                 cwd=ROOT,env=env,text=True,capture_output=True)
(ROOT/'code/part3_fourfold/k35_compile.out').write_text(p.stdout)
(ROOT/'code/part3_fourfold/k35_standalone.err').write_text(p.stderr)
if p.returncode:
    print(p.stdout[-7000:]);raise SystemExit(p.returncode)
logtext=(ROOT/'code/part3_fourfold/k35_standalone.log').read_text()
over=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',logtext)]
pdf=fitz.open(ROOT/'code/part3_fourfold/k35_standalone.pdf')
out=ROOT/'records/render_k35';out.mkdir(exist_ok=True)
paths=[]
for i,page in enumerate(pdf):
    path=out/f'page_{i+1:02}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.65,1.65),alpha=False).save(path)
    paths.append(str(path.relative_to(ROOT)))
for start in range(0,len(paths),4):
    contact=Image.new('RGB',(1700,2440),'#dddddd')
    for j,rel in enumerate(paths[start:start+4]):
        im=Image.open(ROOT/rel).convert('RGB');im.thumbnail((820,1180))
        tile=Image.new('RGB',(850,1220),'white')
        tile.paste(im,((850-im.width)//2,25))
        ImageDraw.Draw(tile).text((18,1200),Path(rel).name,fill='black')
        contact.paste(tile,((j%2)*850,(j//2)*1220))
    contact.save(out/f'contact_{start//4+1}.png')
report=dict(utc=datetime.now(timezone.utc).isoformat(),compile='PASS',pages=len(pdf),
            overflows_pt=over,overflows_gt_2pt=[x for x in over if x>2],
            missing_character=bool(re.search(r'Missing character:',logtext)),
            page_images=paths,visual_review='pending')
(ROOT/'records/qa_k35.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
