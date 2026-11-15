"""Render the final five-page independent A proof record for visual QA."""
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parents[1]
out=root/'records/A_special_render'
out.mkdir(exist_ok=True)
pdf=root/'build/A_special_qa.pdf'
subprocess.run(['pdftoppm','-png','-r','110',str(pdf),str(out/'page')],check=True)
for p in sorted(out.glob('page-*.png')):
    print(p.name,p.stat().st_size)
print('Rendered all pages for visual inspection.')
