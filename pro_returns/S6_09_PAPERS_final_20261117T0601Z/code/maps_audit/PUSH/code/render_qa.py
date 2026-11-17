#!/usr/bin/env python3
"""Render representative pages and every page flagged for visual review."""
from pathlib import Path
import sys,json,math
import fitz
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).resolve().parents[1]
tag=sys.argv[1] if len(sys.argv)>1 else "draft03"
d=fitz.open(root/"S6_02_PUSH_paper.pdf")
pages=sorted(set([1,2,3,12]+[1+round(i*(len(d)-1)/7) for i in range(8)]))
out=root/"qa"/tag
out.mkdir(parents=True,exist_ok=True)
thumbs=[]
for p in pages:
    pix=d[p-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False)
    dst=out/f"page_{p:03d}.png";pix.save(dst)
    im=Image.open(dst).convert("RGB")
    im.thumbnail((400,566))
    card=Image.new("RGB",(420,606),"#dddddd")
    card.paste(im,((420-im.width)//2,25))
    ImageDraw.Draw(card).text((10,585),f"Page {p}",fill="black")
    thumbs.append(card)
sheet=Image.new("RGB",(420*3,606*math.ceil(len(thumbs)/3)),"white")
for i,im in enumerate(thumbs):sheet.paste(im,((i%3)*420,(i//3)*606))
sheet.save(out/"contact_sheet.jpg",quality=90)
record={"pdf_pages":len(d),"rendered_pages":pages,"contact_sheet":str(out/"contact_sheet.jpg")}
(out/"render_record.json").write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
