"""Compile the manuscript with the recorded local LuaLaTeX runtime.

The runtime repair is in prepare_tex_runtime.py.  This script retains every
pass log and extracts actual TeX errors and all overfull boxes.  A successful
exit requires no TeX errors, no unresolved references, and no overflow >2pt.
Visual inspection of rendered pages is recorded separately.
"""
from pathlib import Path
from datetime import datetime, timezone
import os
import re
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
build = root / 'build'
build.mkdir(exist_ok=True)
history=build/'history'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
history.mkdir(parents=True,exist_ok=True)
for prior in build.glob('certify_pass_*.out'):
    shutil.copy2(prior,history/('previous_'+prior.name))
prior_log=build/'S6_03_CDP_paper.log'
if prior_log.exists():
    shutil.copy2(prior_log,history/'previous_paper.log')
env = os.environ.copy()
env['TEXMF'] = '{' + str(build/'texmf') + ',/usr/share/texmf,/usr/share/texlive/texmf-dist}'
env['TEXFORMATS'] = str(build)
env['BIBINPUTS'] = str(root) + ':'
env['BSTINPUTS'] = '/usr/share/texlive/texmf-dist/bibtex/bst//:'
base = 'S6_03_CDP_paper'
subprocess.run([sys.executable,str(root/'code'/'assemble_catalog.py')],cwd=root,check=True)
subprocess.run([sys.executable,str(root/'code'/'assemble_manuscript.py')],cwd=root,check=True)
commands = [
    ['lualatex','-interaction=nonstopmode','-output-directory=build',base+'.tex'],
    ['bibtex','build/'+base],
    ['lualatex','-interaction=nonstopmode','-output-directory=build',base+'.tex'],
    ['lualatex','-interaction=nonstopmode','-output-directory=build',base+'.tex'],
]
results = []
for i, cmd in enumerate(commands, 1):
    path = build / f'certify_pass_{i}.out'
    with path.open('w') as f:
        result = subprocess.run(cmd, cwd=root, env=env, stdout=f, stderr=subprocess.STDOUT)
    results.append(result.returncode)
    shutil.copy2(path,history/path.name)
    print(f'pass {i}: exit {result.returncode}; {path.relative_to(root)}', flush=True)
    if result.returncode:
        print(path.read_text()[-5000:], flush=True)
        break
log = (build/(base+'.log')).read_text(errors='replace')
errors = re.findall(r'^!.*$',log,re.M)
overflows = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt too',log)]
unresolved = re.findall(r'^LaTeX Warning: (?:There were undefined references|Citation .* undefined|Reference .* undefined).*$',log,re.M)
missing_glyphs = re.findall(r'^Missing character:.*$',log,re.M)
print('TeX errors:',len(errors),errors)
print('Overfull boxes:',len(overflows),overflows)
print('Overflows above 2pt:',sum(x>2 for x in overflows))
print('Unresolved reference warnings:',len(unresolved))
print('Missing glyph warnings:',len(missing_glyphs))
shutil.copy2(build/(base+'.log'),history/'paper.log')
good = len(results)==4 and all(x==0 for x in results) and not errors and not unresolved and not missing_glyphs and not any(x>2 for x in overflows)
if good:
    shutil.copy2(build/(base+'.pdf'),root/(base+'.pdf'))
    print('Build checks passed; PDF copied to project root. Visual QA remains separately recorded.')
sys.exit(0 if good else 1)
