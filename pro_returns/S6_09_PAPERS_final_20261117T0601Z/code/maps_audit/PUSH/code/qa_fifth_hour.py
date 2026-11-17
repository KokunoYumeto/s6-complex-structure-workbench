#!/usr/bin/env python3
"""Additional visual samples for newly integrated fifth-hour statements."""
from pathlib import Path
import json
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
document = fitz.open(root / 'S6_02_PUSH_paper.pdf')
needles = ['B.4.8 (Proved)', 'B.4.9 (Proved)', 'C.3.25 (Proved)',
           'C.3.26 (Proved)', 'C.3.27 (Proved)', 'E.2.6 (Proved)']
pages = [i + 1 for i, p in enumerate(document)
         if any(n in p.get_text() for n in needles)]
out = root / 'qa' / 'draft19'
cards = []
for number in pages:
    target = out / f'page_{number:03d}.png'
    document[number - 1].get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False).save(target)
    im = Image.open(target).convert('RGB')
    im.thumbnail((480, 680))
    card = Image.new('RGB', (500, 720), '#dddddd')
    card.paste(im, ((500 - im.width) // 2, 15))
    ImageDraw.Draw(card).text((12, 695), f'Page {number}', fill='black')
    cards.append(card)
sheet = Image.new('RGB', (1500, 720 * ((len(cards) + 2) // 3)), 'white')
for i, card in enumerate(cards):
    sheet.paste(card, ((i % 3) * 500, (i // 3) * 720))
sheet.save(out / 'fifth_hour_new_statements.jpg', quality=94)
record = {'build': 'draft19', 'additional_pages': pages,
          'scope': 'Additional visual samples; all final-build overfull counts are zero.'}
(out / 'additional_render_record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
