"""Render a disjoint range of the actual current PDF for manual page reading.

Rendering itself gives no reading credit. Each reader records a page only
after its image has actually been displayed and inspected.
"""
from pathlib import Path
import argparse
import subprocess
import re
import fitz

p=argparse.ArgumentParser()
p.add_argument('--pdf',required=True)
p.add_argument('--output',required=True)
p.add_argument('--first',type=int,required=True)
p.add_argument('--last',type=int,required=True)
p.add_argument('--dpi',type=int,default=120)
a=p.parse_args()
pdf=Path(a.pdf).resolve(); out=Path(a.output).resolve()
with fitz.open(pdf) as doc:
    assert 1 <= a.first <= a.last <= len(doc)
out.mkdir(parents=True,exist_ok=True)
subprocess.run(['pdftoppm','-f',str(a.first),'-l',str(a.last),'-r',str(a.dpi),'-png',str(pdf),str(out/'page')],check=True)
for file in list(out.glob('page-*.png')):
    match=re.fullmatch(r'page-(\d+)\.png',file.name)
    if match and a.first<=int(match[1])<=a.last:
        target=out/f'page-{int(match[1]):04d}.png'
        if target!=file:
            assert not target.exists(),target
            file.rename(target)
assert all((out/f'page-{page:04d}.png').is_file() for page in range(a.first,a.last+1))
print(f'Rendered physical pages {a.first}–{a.last} at {a.dpi} dpi with Poppler.')
print('No manual page-reading credit is assigned by this program.')
