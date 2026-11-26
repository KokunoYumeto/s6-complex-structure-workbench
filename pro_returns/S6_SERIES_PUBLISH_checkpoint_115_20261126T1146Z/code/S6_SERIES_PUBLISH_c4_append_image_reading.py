"""Append the caller's explicit observations after actual page-image viewing.

This program hashes named images and writes supplied observations. It does
not inspect an image, infer a clear disposition, or provide reading credit.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--pdf',type=Path,required=True)
p.add_argument('--log',type=Path,required=True)
p.add_argument('--source-hash',required=True)
a=p.parse_args()
observations=json.load(sys.stdin)
assert observations
pdf=a.pdf.resolve()
log=a.log.resolve()
pdf_hash=hashlib.sha256(pdf.read_bytes()).hexdigest()
source_hash=hashlib.sha256((ROOT/'S6_SERIES_PUBLISH_II.tex').read_bytes()).hexdigest()
assert a.source_hash==source_hash
if log.exists():
    text=log.read_text()
    assert pdf_hash in text and source_hash in text
else:
    text=('# Paper II: root actual-image reading of changed pages\n\n'
        'Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; effort setting not separately exposed; fourth-continuation root.\n\n'
        f'PDF SHA-256: {pdf_hash}.\nSource SHA-256: {source_hash}.\n\n'
        'Poppler 120 dpi full-page images were actually displayed and read before each observation was supplied. '
        'This log records typography/layout and reference checks; it supplies no independent proof credit.\n\n'
        '| Physical page | Content read | Finding | Image SHA-256 | Read UTC | Disposition |\n'
        '| --- | --- | --- | --- | --- | --- |\n')
existing={int(x) for x in re.findall(r'(?m)^\| (\d+) \|',text)}
for page,content,finding,disposition in observations:
    assert isinstance(page,int) and page not in existing
    assert content and finding and disposition in ('clear','OPEN')
    image_hash=hashlib.sha256((pdf.parent/'pages_120dpi'/f'page-{page:04d}.png').read_bytes()).hexdigest()
    clean=lambda s:s.replace('|',r'\|').replace('\n',' ')
    text+=f'| {page} | {clean(content)} | {clean(finding)} | {image_hash} | {datetime.now(timezone.utc).isoformat()} | {disposition} |\n'
    existing.add(page)
log.write_text(text,newline='\n')
print('Appended explicit actual-image observations:',len(observations))
