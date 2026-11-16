"""Reproduce selected page images and readable overview sheets from the final PDF."""
from pathlib import Path
import argparse, json
import fitz
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
paper_dir = Path(__file__).resolve().parents[2]
pdf = fitz.open(paper_dir / 'S6_07_PAPER_paper.pdf')
args.output.mkdir(parents=True, exist_ok=True)
pages = sorted(set([1,2,3,4,8,10,12,14,16,20,24,28,32,33,34,35,36,40,44,48,52,56,58,59,62,66,70,74,76,80,84,88,90,92,95,100,103,104,105,106] + list(range(107,len(pdf)+1))))
for n in pages:
    pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.55,1.55),alpha=False).save(args.output/f'page-{n:03}.png')
for start in range(0,len(pages),4):
    group=pages[start:start+4]
    sheet=Image.new('RGB',(1440,2080),'#d6d6d6');draw=ImageDraw.Draw(sheet)
    for i,n in enumerate(group):
        im=Image.open(args.output/f'page-{n:03}.png').convert('RGB')
        im.thumbnail((700,990))
        x=(i%2)*720+(720-im.width)//2;y=(i//2)*1040+30
        sheet.paste(im,(x,y));draw.text((x, y-20),f'Page {n}',fill='black')
    sheet.save(args.output/f'sheet-{start//4+1:02}.jpg',quality=88)
(args.output/'render_manifest.json').write_text(json.dumps({'pdf_pages':len(pdf),'pages':pages,'scale':1.55,'sheet_pages':4},indent=2))
print(f'Rendered {len(pages)} selected pages and {(len(pages)+3)//4} overview sheets.')
