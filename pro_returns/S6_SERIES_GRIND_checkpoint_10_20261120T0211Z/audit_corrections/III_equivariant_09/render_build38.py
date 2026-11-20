"""Wait for the successful III build, preserve it and render selected pages.

Rendering is preparation only.  The separate visual receipt is written after
the reviewer actually views each emitted image.
"""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import time
import fitz
from PIL import Image, ImageDraw

WORK = Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_work')
OUT = WORK / 'audit_corrections/III_equivariant_09/QA_build38'
DIAG = WORK / 'code/outputs/build_38/S6_SERIES_GRIND_III_diagnostics.json'
deadline = time.monotonic() + 55
while not DIAG.exists() and time.monotonic() < deadline:
    time.sleep(2)
if not DIAG.exists():
    raise SystemExit('PENDING: build38 III diagnostics did not appear within55seconds')
diagnostics = json.loads(DIAG.read_text())
assert diagnostics['returncode'] == 0, diagnostics
OUT.mkdir(exist_ok=True)
pdf = OUT / 'S6_SERIES_GRIND_III_build38.pdf'
shutil.copyfile(WORK / 'S6_SERIES_GRIND_III.pdf', pdf)
doc = fitz.open(pdf)
texts = [' '.join(p.get_text().split()) for p in doc]
aux = (WORK / 'S6_SERIES_GRIND_III.aux').read_text()

def label_page(label):
    pattern = r'\\newlabel\{' + re.escape(label) + r'\}\{\{[^}]*\}\{(\d+)\}'
    return int(re.search(pattern, aux).group(1))

def find(term):
    return [i + 1 for i, text in enumerate(texts) if term.lower() in text.lower()]

main = list(range(label_page('series:III:F'), label_page('series:III:G') + 1))
statement_start = label_page('maps:src:D.2.53')
statement_end = find('Together with the displayed primitive cubic')[0]
statement = list(range(statement_start, statement_end + 1))
proof = list(range(206, 213))  # Root-requested complete changed proof/QED range
final_start = find('The specified weighted OS45/default member is complete')[0]
final = [final_start, final_start + 1]
outline = find('For a period sublattice of the cusp')
pages = sorted(set([1] + main + statement + proof + final + outline))

def render(number):
    prefix = OUT / f'page_{number:03d}'
    subprocess.run(['pdftoppm', '-f', str(number), '-l', str(number),
                    '-singlefile', '-r', '105', '-png', str(pdf), str(prefix)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    return prefix.with_suffix('.png')

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    paths = list(pool.map(render, pages))
sheets = []
for offset in range(0, len(paths), 2):
    selected = paths[offset:offset + 2]
    images = [Image.open(path).convert('RGB') for path in selected]
    sheet = Image.new('RGB', (sum(im.width for im in images) + 20,
                              max(im.height for im in images) + 35), '#d8d8d8')
    draw = ImageDraw.Draw(sheet)
    x = 5
    for path, im in zip(selected, images):
        number = int(path.stem.split('_')[-1])
        draw.text((x + 10, 8), f'Build38 III - PDF page {number}', fill='black')
        sheet.paste(im, (x, 30))
        x += im.width + 10
    output = OUT / f'QA_III_{offset // 2 + 1:02d}.png'
    sheet.save(output)
    sheets.append({'path': str(output.relative_to(WORK)),
                   'pages': pages[offset:offset + 2],
                   'sha256': hashlib.sha256(output.read_bytes()).hexdigest()})
old = WORK / 'audit_corrections/III_equivariant_09/QA_build35'
comparisons = []
for number, path in zip(pages, paths):
    prior = old / path.name
    a = Image.open(path).convert('RGB')
    same = False
    if prior.exists():
        b = Image.open(prior).convert('RGB')
        same = a.size == b.size and a.tobytes() == b.tobytes()
    comparisons.append({'page': number, 'same_full_pixels_as_build35': same,
                        'prior_page_available': prior.exists()})
manifest = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Rendered only; no visual inspection is claimed by this program.',
    'pdf': str(pdf.relative_to(WORK)),
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'pdf_page_count': len(doc),
    'selection': {'abstract': [1], 'main_F': main, 'outline_F5': outline,
                  'D253_statement': statement, 'complete_new_proof': proof,
                  'final_part': final},
    'pages': [{'page': number, 'path': str(path.relative_to(WORK)),
               'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
              for number, path in zip(pages, paths)],
    'sheets': sheets,
    'full_page_pixel_comparisons': comparisons,
    'diagnostics': diagnostics,
}
(OUT / 'render_manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'pdf_sha256': manifest['pdf_sha256'], 'selection': manifest['selection'],
                  'sheets': sheets, 'pixel_comparison': comparisons}, indent=2))
