"""Render every post10 proof, current scope paragraph and bibliography page."""
from pathlib import Path
import json
import re
import subprocess
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
pdf = ROOT / "S6_04_MAPS_MANIFOLDS_paper.pdf"
out = ROOT / "records/pdf_qa"
out.mkdir(exist_ok=True)
textfile = ROOT / "records/checkpoint_11_paper.txt"
subprocess.run(["pdftotext", "-layout", str(pdf), str(textfile)], check=True)
pages = textfile.read_text().split("\f")
count = len(pages) - (not pages[-1].strip())
head = re.compile(r"(?:Theorem|Proposition|Corollary|Lemma|Problem|Conclusion|Computation|Resolved conclusion|Remaining task)\s+([A-F]\.\d+\.\d+)\s+\(")
starts = {}
for i, page in enumerate(pages):
    for match in head.finditer(page):
        starts.setdefault(match[1], i + 1)
tags = sorted(tag for tag in starts
              if tag.startswith("D.2.") and int(tag.split(".")[2]) >= 44)
assert {"D.2.44", "D.2.45", "D.2.46"} <= set(tags)
selected = set()
locations = {}
for tag in tags + ["D.2.4"]:
    begin = starts[tag]
    later = [p for p in starts.values() if p > begin]
    end = min(later) if later else count
    locations[tag] = {"start": begin, "through": end}
    selected.update(range(begin, end + 1))
bibliography = [i + 1 for i, page in enumerate(pages)
                if re.search(r"^\s*References\s*$", page, re.M)]
assert bibliography
bib_start = bibliography[-1]
selected.update(range(bib_start, count + 1))
selected = sorted(selected)
for page in selected:
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "100",
                    "-singlefile", "-png", str(pdf), str(out / f"cp11_{page:03}")], check=True)
contacts = []
for group in range((len(selected) + 7) // 8):
    part = selected[group * 8:group * 8 + 8]
    sheet = Image.new("RGB", (1100, 790 * ((len(part) + 1) // 2)), "#ddd")
    for i, page in enumerate(part):
        im = Image.open(out / f"cp11_{page:03}.png").convert("RGB")
        im.thumbnail((530, 750))
        x, y = 550 * (i % 2), 790 * (i // 2)
        sheet.paste(im, (x + (550 - im.width) // 2, y + 25))
        ImageDraw.Draw(sheet).text((x + 12, y + 6), f"Page {page}", fill="black")
    name = f"cp11_contact_{group + 1}.png"
    sheet.save(out / name)
    contacts.append(name)
record = {"statement_pages": locations, "extra_rendered_pages": selected,
          "bibliography_start": bib_start, "pages": count,
          "contact_sheets": contacts, "changed_scope_paragraphs": ["D.2.4"],
          "preflight_repaired_regions": []}
(out / "checkpoint_11_extra_pages.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
