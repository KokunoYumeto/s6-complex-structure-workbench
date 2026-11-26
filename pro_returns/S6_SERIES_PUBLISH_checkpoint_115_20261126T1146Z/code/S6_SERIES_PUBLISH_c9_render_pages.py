#!/usr/bin/env python3
"""Render actual PDF pages at150dpi; rendering gives no reading credit."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import re
import subprocess

p = argparse.ArgumentParser()
p.add_argument('--pdf', required=True, type=Path)
p.add_argument('--out', required=True, type=Path)
p.add_argument('--first', type=int, default=1)
p.add_argument('--last', type=int)
a = p.parse_args()
pdf = a.pdf.resolve()
out = a.out.resolve()
info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
total = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
last = a.last or total
assert 1 <= a.first <= last <= total
out.mkdir(parents=True, exist_ok=True)
assert not list(out.glob('page-*.png')), 'Choose a fresh image directory; existing page images are not overwritten.'
identity = hashlib.sha256(pdf.read_bytes()).hexdigest()
print('UTC start', datetime.now(timezone.utc).isoformat(), flush=True)
print('PDF', pdf, 'SHA256', identity, 'total physical pages', total, flush=True)
print('Requested pages', a.first, last, 'image directory', out, 'dpi150', flush=True)

def render(first, stop):
    result = subprocess.run(['pdftoppm', '-r', '150', '-png', '-f', str(first), '-l', str(stop), str(pdf), str(out / 'page')], capture_output=True, text=True)
    return first, stop, result

batches = [(n, min(n + 49, last)) for n in range(a.first, last + 1, 50)]
with ThreadPoolExecutor(max_workers=4) as pool:
    futures = [pool.submit(render, first, stop) for first, stop in batches]
    for future in as_completed(futures):
        first, stop, result = future.result()
        print('Rendered', first, stop, 'exit', result.returncode, flush=True)
        if result.stderr:
            print(result.stderr, flush=True)
        assert result.returncode == 0
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == identity, 'PDF changed during rendering.'
pages = {int(path.stem.split('-')[-1]) for path in out.glob('page-*.png')}
assert pages == set(range(a.first, last + 1))
print('UTC complete', datetime.now(timezone.utc).isoformat(), 'images', len(pages), flush=True)
print('No actual page reading is claimed by this rendering program.', flush=True)
