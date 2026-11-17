"""Record page-boundary and final-log checks for the current checkpoint PDF."""
from pathlib import Path
import json
import re
import sys
import fitz

ROOT = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
pdf = fitz.open(ROOT / 'S6_06_BLIND_paper.pdf')
outside = []
for number, page in enumerate(pdf, 1):
    for word in page.get_text('words'):
        x0, y0, x1, y1 = word[:4]
        if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width + 0.5 or y1 > page.rect.height + 0.5:
            outside.append({'page': number, 'word': word[4], 'bbox': list(word[:4])})
log = (ROOT / 'S6_06_BLIND_paper.log').read_text(errors='replace')
record = {
    'checked_pages': len(pdf),
    'out_of_page_words': outside,
    'undefined_reference_warnings': re.findall(r'.*(?:undefined|Undefined).*', log),
    'missing_character_warnings': re.findall(r'.*Missing character.*', log),
}
target = ROOT / f'records/page_boundaries_checkpoint{n:02d}.json'
target.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
if outside or record['undefined_reference_warnings'] or record['missing_character_warnings']:
    raise SystemExit(1)
