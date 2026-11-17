#!/usr/bin/env python3
"""Isolated compile, all-page render and boundary audit for the complete P3K.59."""
from pathlib import Path
from datetime import datetime,timezone
import json,os,re,subprocess
import fitz
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[2]
if (ROOT/'code/part3_fourfold/k59_standalone.pdf').exists():
    archive=ROOT/'code/part3_fourfold/attempts'/('k59_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S'))
    archive.mkdir(parents=True,exist_ok=True)
    for pattern in ('k59_standalone.*','k59_compile_*.out','k59_compile_*.err'):
        for old in (ROOT/'code/part3_fourfold').glob(pattern):
            (archive/old.name).write_bytes(old.read_bytes())
    oldqa=ROOT/'records/qa_k59.json'
    if oldqa.exists(): (archive/oldqa.name).write_bytes(oldqa.read_bytes())
with (ROOT/'records/literature_fourfold.md').open('a') as log:
    log.write('\n- '+datetime.now(timezone.utc).isoformat()+
      ' — Opened own code/part3/f48_standalone.tex and notes/part3_source_cusp_mutation_staircase.tex. '
      'Reason: isolated complete K59 compile, all-page boundary audit and rendering. '
      'Material: audited source, fan, cap, excision and return proof; no shared PDF writes.\n')
preamble=(ROOT/'code/part3/f48_standalone.tex').read_text().split(r'\begin{document}',1)[0]
src=ROOT/'code/part3_fourfold/k59_standalone.tex'
bib=r'''\begin{thebibliography}{1}
\bibitem{AtiyahBott1984} M. F. Atiyah and R. Bott,
The moment map and equivariant cohomology,
\emph{Topology} \textbf{23} (1984), no. 1, 1--28.
\end{thebibliography}
'''
src.write_text(preamble+r'\begin{document}'+'\n'+
  r'\input{notes/part3_source_cusp_mutation_staircase.tex}'+'\n'+r'\end{document}'+'\n')
runtime=ROOT.parent/'tex_runtime'
env=dict(os.environ,TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}',
 TEXFORMATS=str(runtime),TEXINPUTS=str(runtime/'packages')+'//:',
 LUAINPUTS=str(runtime/'packages')+'//:')
outs=[];errs=[]
for run in range(2):
    p=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',
       '-output-directory=code/part3_fourfold',str(src.relative_to(ROOT))],
       cwd=ROOT,env=env,text=True,capture_output=True)
    outs.append(p.stdout);errs.append(p.stderr)
    (ROOT/f'code/part3_fourfold/k59_compile_{run+1}.out').write_text(p.stdout)
    (ROOT/f'code/part3_fourfold/k59_compile_{run+1}.err').write_text(p.stderr)
    if p.returncode:
        print(p.stdout[-8000:]);raise SystemExit(p.returncode)
logtext=(ROOT/'code/part3_fourfold/k59_standalone.log').read_text()
over=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',logtext)]
pdf=fitz.open(ROOT/'code/part3_fourfold/k59_standalone.pdf')
out=ROOT/'records/render_k59';out.mkdir(exist_ok=True)
paths=[];bounds=[]
for i,page in enumerate(pdf):
    path=out/f'page_{i+1:02}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(path)
    paths.append(str(path.relative_to(ROOT)))
    for block in page.get_text('blocks'):
        if len(block)>6 and block[6]!=0: continue
        x0,y0,x1,y1=block[:4]
        if x0<15 or y0<15 or x1>page.rect.width-15 or y1>page.rect.height-15:
            bounds.append({'page':i+1,'bbox':[x0,y0,x1,y1],'text':block[4][:120]})
contacts=[]
for start in range(0,len(paths),4):
    contact=Image.new('RGB',(1700,2440),'#dddddd')
    for j,rel in enumerate(paths[start:start+4]):
        im=Image.open(ROOT/rel).convert('RGB');im.thumbnail((820,1180))
        tile=Image.new('RGB',(850,1220),'white')
        tile.paste(im,((850-im.width)//2,25))
        ImageDraw.Draw(tile).text((18,1200),f'K59 page {start+j+1}',fill='black')
        contact.paste(tile,((j%2)*850,(j//2)*1220))
    dst=out/f'contact_{start//4+1}.png';contact.save(dst)
    contacts.append(str(dst.relative_to(ROOT)))
report=dict(utc=datetime.now(timezone.utc).isoformat(),compile='PASS',pages=len(pdf),
 overflows_pt=over,overflows_gt_2pt=[x for x in over if x>2],
 missing_character=bool(re.search(r'Missing character:',logtext)),
 undefined_reference=bool(re.search(r'There were undefined references|Citation .* undefined',logtext)),
 boundary_issues=bounds,page_images=paths,contact_sheets=contacts,visual_review='pending')
(ROOT/'records/qa_k59.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
