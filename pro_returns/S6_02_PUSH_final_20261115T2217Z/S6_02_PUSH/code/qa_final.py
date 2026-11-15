#!/usr/bin/env python3
"""Render every newly completed filling-proof page and changed dispositions."""
from pathlib import Path
import json, re, sys
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
tag = sys.argv[1]
doc = fitz.open(root / "S6_02_PUSH_paper.pdf")
out = root / "qa" / tag
out.mkdir(parents=True, exist_ok=True)
identities = ["B.4.1", "B.4.2", "B.4.4", "B.4.5", "B.4.30", "B.4.31",
              "B.4.32", "B.4.33", "B.5.1", "C.1.1", "C.5.1", "D.1.1",
              "E.2.24", "E.3.1"]
found = {}
for index, page in enumerate(doc):
    content = " ".join(page.get_text().split())
    for identity in identities:
        pattern = re.escape(identity) + r"(?:\s*\((?:Proved|Known|Refuted)\b|\s*;\s*(?:Proved|Known|Refuted))"
        if re.search(pattern, content):
            found[identity] = index + 1
assert all(identity in found for identity in identities), (identities, found)
pairs = [("B.4.1", "B.4.2"), ("B.4.4", "B.4.5"), ("B.4.30", "C.1.1"),
         ("C.5.1", "D.1.1"), ("E.2.24", "E.3.1")]
pages = {1}
for first, last in pairs:
    assert found[last] >= found[first], (first, last, found)
    pages.update(range(found[first], found[last] + 1))
pages = sorted(pages)
cards = []
for number in pages:
    target = out / f"page_{number:03d}.png"
    doc[number-1].get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False).save(target)
    im = Image.open(target).convert("RGB")
    im.thumbnail((480, 680))
    card = Image.new("RGB", (500, 720), "#dddddd")
    card.paste(im, ((500-im.width)//2, 15))
    ImageDraw.Draw(card).text((12, 695), f"Page {number}", fill="black")
    cards.append(card)
sheets = []
for start in range(0, len(cards), 9):
    group = cards[start:start+9]
    sheet = Image.new("RGB", (1500, 720*((len(group)+2)//3)), "white")
    for index, card in enumerate(group):
        sheet.paste(card, ((index%3)*500, (index//3)*720))
    path = out / f"final_new_proofs_{start//9+1}.jpg"
    sheet.save(path, quality=94)
    sheets.append(str(path))
record = {"build": tag, "pdf_pages": len(doc), "statement_start_pages": found,
          "additional_pages": pages, "contact_sheets": sheets,
          "scope": "Rendered pages only; actual inspection is recorded after viewing."}
(out/"additional_render_record.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
