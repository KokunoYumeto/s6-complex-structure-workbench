#!/usr/bin/env python3
"""Compile and render only the audited K29 include."""
from pathlib import Path
from datetime import datetime, timezone
import json, os, re, subprocess
import fitz
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).resolve().parents[2]
with (ROOT/"records/literature_fourfold.md").open("a") as log:
    log.write("\n- "+datetime.now(timezone.utc).isoformat()
              +" — Opened own code/part3/f48_standalone.tex and notes/part3_common_exterior_meridians.tex; "
              "reason: isolated K29 PDF quality assurance; material: known preamble and complete audited proof.\n")
preamble=(ROOT/"code/part3/f48_standalone.tex").read_text().split(r"\begin{document}",1)[0]
standalone=ROOT/"code/part3_fourfold/k29_standalone.tex"
standalone.write_text(preamble+r"\begin{document}"+"\n"
                      +r"\input{notes/part3_common_exterior_meridians.tex}"+"\n"
                      +r"\end{document}"+"\n")
runtime=ROOT.parent/"tex_runtime"
env=dict(os.environ,TEXMF="{/usr/share/texlive/texmf-dist,/usr/share/texmf}",
         TEXFORMATS=str(runtime),TEXINPUTS=str(runtime/"packages")+"//:",
         LUAINPUTS=str(runtime/"packages")+"//:")
cmd=["lualatex","-interaction=nonstopmode","-halt-on-error",
     "-output-directory=code/part3_fourfold",str(standalone.relative_to(ROOT))]
hyperref_out=ROOT/"code/part3_fourfold/k29_standalone.out"
if hyperref_out.exists() and "Lua" in hyperref_out.read_text(errors="replace")[:300]:
    hyperref_out.rename(ROOT/"code/part3_fourfold/k29_previous_capture.out")
p=subprocess.run(cmd,cwd=ROOT,env=env,text=True,capture_output=True)
(ROOT/"code/part3_fourfold/k29_compile.out").write_text(p.stdout)
(ROOT/"code/part3_fourfold/k29_standalone.err").write_text(p.stderr)
if p.returncode:
    print(p.stdout[-5000:])
    raise SystemExit(p.returncode)
logtext=(ROOT/"code/part3_fourfold/k29_standalone.log").read_text()
overflow=[float(x) for x in re.findall(r"Overfull \\hbox \(([0-9.]+)pt too wide\)",logtext)]
pdf=fitz.open(ROOT/"code/part3_fourfold/k29_standalone.pdf")
out=ROOT/"records/render_k29"
out.mkdir(exist_ok=True)
pagepaths=[]
for i,page in enumerate(pdf):
    pix=page.get_pixmap(matrix=fitz.Matrix(1.65,1.65),alpha=False)
    path=out/f"page_{i+1:02}.png"
    pix.save(path)
    pagepaths.append(str(path.relative_to(ROOT)))
for start in range(0,len(pagepaths),4):
    thumbs=[]
    for rel in pagepaths[start:start+4]:
        im=Image.open(ROOT/rel).convert("RGB")
        im.thumbnail((820,1180))
        tile=Image.new("RGB",(850,1220),"white")
        tile.paste(im,((850-im.width)//2,25))
        ImageDraw.Draw(tile).text((18,1200),rel.split("/")[-1],fill="black")
        thumbs.append(tile)
    contact=Image.new("RGB",(1700,2440),"#dddddd")
    for j,im in enumerate(thumbs):
        contact.paste(im,((j%2)*850,(j//2)*1220))
    contact.save(out/f"contact_{start//4+1}.png")
report={"utc":datetime.now(timezone.utc).isoformat(),"compile":"PASS",
        "pages":len(pdf),"overflows_pt":overflow,
        "overflows_gt_2pt":[x for x in overflow if x>2],
        "missing_character":bool(re.search(r"Missing character:",logtext)),
        "page_images":pagepaths,"visual_review":"pending"}
(ROOT/"records/qa_k29.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
