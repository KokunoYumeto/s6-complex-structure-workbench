#!/usr/bin/env python3
"""Create numbered contact sheets from the final PDF renders for visual review."""
import json
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'work/build_final'
OUT = BUILD / 'contacts'
OUT.mkdir(exist_ok=True)
pages = sorted((BUILD / 'pages').glob('page-*.png'))
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 19)
width, height = 680, 930
sheets = []
for offset in range(0, len(pages), 6):
    batch = pages[offset:offset+6]
    sheet = Image.new('RGB', (2*width, 3*height), '#dce1e5')
    draw = ImageDraw.Draw(sheet)
    for i, page in enumerate(batch):
        im = Image.open(page).convert('RGB')
        im.thumbnail((width-24, height-42), Image.Resampling.LANCZOS)
        x, y = (i%2)*width, (i//2)*height
        sheet.paste(im, (x+(width-im.width)//2, y+32))
        draw.text((x+14, y+7), 'Final post — page '+str(offset+i+1), fill='#1a2834', font=font)
    destination = OUT / f'contact-{offset//6+1:02d}.png'
    sheet.save(destination)
    sheets.append({'path':str(destination.relative_to(ROOT)),
                   'pages':list(range(offset+1, offset+len(batch)+1))})
subprocess.run(['pdftotext', '-layout', str(BUILD/'Q03_DEPOSIT_post.pdf'),
                str(BUILD/'post_text.txt')], check=True)
text_pages = (BUILD/'post_text.txt').read_text().split('\f')
headings = [{'page':i+1, 'first_lines': '\n'.join(p.splitlines()[:5])}
            for i,p in enumerate(text_pages) if p.strip()]
result = {'rendered_pages':len(pages), 'contact_sheets':sheets, 'page_headings':headings}
(ROOT/'code/render_review_output.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'rendered_pages':len(pages),'contact_sheets':sheets},indent=2))
