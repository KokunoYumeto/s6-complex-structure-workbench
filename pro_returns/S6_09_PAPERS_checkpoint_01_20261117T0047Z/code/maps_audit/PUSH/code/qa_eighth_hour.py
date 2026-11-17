#!/usr/bin/env python3
"""Render all newly integrated proof pages; do not yet claim inspection."""
from pathlib import Path
import json, re, sys
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
tag = sys.argv[1]
doc = fitz.open(root / 'S6_02_PUSH_paper.pdf')
out = root / 'qa' / tag
out.mkdir(parents=True, exist_ok=True)
ids = ['B.4.19', 'B.4.20', 'B.4.21', 'C.1.1', 'E.2.4']
ids += [f'E.2.{i}' for i in range(20, 25)] + ['E.3.1']
found = {}
for i, page in enumerate(doc):
    content = ' '.join(page.get_text().split())
    for identity in ids:
        pattern = re.escape(identity) + r'(?:\s*\((?:Proved|Known)\b|\s*;\s*Proved)'
        if re.search(pattern, content):
            found[identity] = i + 1
assert all(i in found for i in ids), (ids, found)
pages = set(range(found['B.4.19'], found['C.1.1'] + 1))
pages.update(range(found['E.2.20'], found['E.3.1'] + 1))
pages.update([found['E.2.4'], found['E.2.4'] + 1])
pages = sorted(p for p in pages if p <= len(doc))
cards = []
for number in pages:
    target = out / f'page_{number:03d}.png'
    doc[number - 1].get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False).save(target)
    im = Image.open(target).convert('RGB')
    im.thumbnail((480, 680))
    card = Image.new('RGB', (500, 720), '#dddddd')
    card.paste(im, ((500-im.width)//2, 15))
    ImageDraw.Draw(card).text((12, 695), f'Page {number}', fill='black')
    cards.append(card)
sheets = []
for start in range(0, len(cards), 9):
    group = cards[start:start+9]
    sheet = Image.new('RGB', (1500, 720*((len(group)+2)//3)), 'white')
    for j, card in enumerate(group):
        sheet.paste(card, ((j%3)*500, (j//3)*720))
    path = out / f'eighth_hour_new_statements_{start//9+1}.jpg'
    sheet.save(path, quality=94)
    sheets.append(str(path))
record = {'build': tag, 'pdf_pages': len(doc), 'statement_start_pages': found,
          'additional_pages': pages, 'contact_sheets': sheets,
          'scope': 'Rendered pages only; inspection is recorded after viewing.'}
(out/'additional_render_record.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
