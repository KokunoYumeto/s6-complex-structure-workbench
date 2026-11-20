"""Snapshot and render the 95-row Paper II review; rendering is not inspection."""
from pathlib import Path
import hashlib
import json
import shutil
from datetime import datetime, timezone
import fitz
from PIL import Image, ImageDraw

A = Path(__file__).resolve().parents[1]
W = A.parent
out = A / 'II_95_QA_06'
out.mkdir(exist_ok=True)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
source = W / 'S6_SERIES_GRIND_II.pdf'
pdf = out / 'S6_SERIES_GRIND_II_build23.pdf'
if pdf.exists():
    assert sha(pdf) == sha(source), 'Existing immutable snapshot differs from current PDF'
else:
    shutil.copyfile(source, pdf)
labels_path = W / 'analysis/current_labels_II.json'
labels = json.loads(labels_path.read_text())
old = json.loads((A / 'II_completion_eligibility.json').read_text())
doc = fitz.open(pdf)
pages = set()
records = []
for row in old['records']:
    label = row['label']
    start = int(labels[label]['page'])
    nxt = row['next_statement']
    end = max(start, int(labels[nxt]['page'])) if nxt in labels else min(len(doc), start+3)
    requested = {start, end}
    if end-start >= 6:
        requested.add((start+end)//2)
    assert all(1 <= p <= len(doc) for p in requested)
    pages |= requested
    records.append({'label':label, 'number':labels[label]['number'],
        'statement_page':start, 'next_statement':nxt,
        'upper_enclosing_page':end, 'requested_pages':sorted(requested),
        'prior_eligibility':row['eligibility'],
        'prior_remaining_gates':row['remaining_before_whole_row_completion']})
pages = sorted(pages)
sheets = []
for ix in range(0,len(pages),2):
    nums = pages[ix:ix+2]
    canvas = Image.new('RGB',(2260,1610),'#e8e8e8')
    draw = ImageDraw.Draw(canvas)
    for col,n in enumerate(nums):
        pix = doc[n-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8),alpha=False)
        im = Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        im.thumbnail((1072,1518))
        canvas.paste(im,(29+1130*col,40))
        draw.text((18+1130*col,13),f'Paper II build23, page {n}',fill='black')
    dest = out / f'II_95_{ix//2+1:02d}.png'
    canvas.save(dest)
    sheets.append({'sheet':ix//2+1,'path':str(dest),'pages':nums,
        'sha256':sha(dest),'actually_viewed':False})
report = {'date_utc':datetime.now(timezone.utc).isoformat(),
    'reviewer':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited and not separately exposed; S6_SERIES_GRIND/sign_theorem_audit',
    'pdf':str(pdf),'pdf_sha256':sha(pdf),'page_count':len(doc),
    'label_map_sha256':sha(labels_path),
    'body_sha256':sha(W/'parts/II.body.tex'),
    'linked_body_sha256':sha(W/'parts/II.body.linked.tex'),
    'prior_eligibility_sha256':sha(A/'II_completion_eligibility.json'),
    'records':records,'requested_pages':pages,'sheets':sheets,
    'inspection_state':'Rendered, not yet viewed. Actual visual inspections will be recorded individually.',
    'scope':'Statement and next-statement boundary pages for each of the95 previously scoped mathematical reviews, with one middle page for long blocks. This is a sampled spread, not a claim to have visually inspected every intervening page.'}
(A/'II_95_layout_plan_06.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'rows':len(records),'pages':len(pages),'sheets':len(sheets),
    'pdf_sha256':report['pdf_sha256'],'page_count':len(doc)},indent=2))
