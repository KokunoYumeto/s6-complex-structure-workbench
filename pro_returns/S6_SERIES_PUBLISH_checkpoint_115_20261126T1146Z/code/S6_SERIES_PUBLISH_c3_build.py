from pathlib import Path
import argparse
import subprocess
import re
from S6_SERIES_PUBLISH_build import environment

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--paper', default='II')
parser.add_argument('--folder', default='II_c3_working')
parser.add_argument('--rounds', type=int, default=3)
args = parser.parse_args()
folder = ROOT / 'build' / args.folder
folder.mkdir(parents=True, exist_ok=True)
source = ROOT / f'S6_SERIES_PUBLISH_{args.paper}.tex'
tex_env = environment('pdflatex')
for turn in range(1, args.rounds+1):
    command = ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
               '-file-line-error', '-output-directory=' + str(folder), str(source)]
    result = subprocess.run(command, cwd=ROOT, env=tex_env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (folder / f'pass_{turn}.txt').write_text(result.stdout, newline='\n')
    print(f'pdfLaTeX pass {turn}: exit {result.returncode}')
    if result.returncode:
        print(result.stdout[-5000:])
        raise SystemExit(result.returncode)
log = (folder / (source.stem + '.log')).read_text(errors='replace')
over = re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)', log)
print('Overfull boxes:', len(over), '; exceeding 2pt:', sum(float(x)>2 for x in over))
for name, pattern in [
    ('undefined references/citations', r'(?:LaTeX|Package natbib) Warning: (?:Reference|Citation).*?undefined'),
    ('undefined summary', r'There were undefined (?:references|citations)'),
    ('missing glyphs', r'Missing character:'),
    ('missing fonts', r'Font .*? not found|mktexpk.*?failed'),
    ('multiply defined labels', r'Label .*?multiply defined|There were multiply-defined labels'),
    ('duplicate destinations', r'destination with the same identifier'),
    ('rerun requests', r'Label\(s\) may have changed|Rerun to get cross-references right')]:
    print(name + ':', len(re.findall(pattern, log, re.S if False else 0)))
print(re.search(r'Output written on .*?\([0-9]+ pages[^\n]*', log, re.S).group(0))
import fitz
with fitz.open(folder / (source.stem + '.pdf')) as pdf:
    unresolved_pages = [n+1 for n, page in enumerate(pdf)
                        if 'UNRESOLVED' in page.get_text()]
print('rendered unresolved-reference fallback pages:', len(unresolved_pages))
if unresolved_pages:
    print('Fallback page numbers:', unresolved_pages)
