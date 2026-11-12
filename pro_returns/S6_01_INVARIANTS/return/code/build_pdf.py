#!/usr/bin/env python3
"""Build with LuaLaTeX/BibTeX and reject document errors and warnings.

Usage: python code/build_pdf.py [--tex-runtime PATH]
The optional local TeX tree contains home/, var/, config/ prepared by
prepare_tex.py. A complete TeX Live installation needs no override.
"""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--tex-runtime',type=Path)
args=parser.parse_args()
env=os.environ.copy()
if args.tex_runtime:
    rt=args.tex_runtime.resolve()
    env.update(TEXMF='{'+','.join(str(p) for p in [rt/'home',rt/'var',Path('/usr/share/texlive/texmf-dist'),Path('/usr/share/texmf')])+'}',
               TEXMFVAR=str(rt/'var'),TEXMFCONFIG=str(rt/'config'),TEXMFHOME=str(rt/'home'))
logs=ROOT/'logs'
logs.mkdir(exist_ok=True)
stem='S6_01_INVARIANTS_paper'
records=[]
commands=[['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',stem+'.tex'],['bibtex',stem]]
commands += [commands[0]]*2
for i,cmd in enumerate(commands,1):
    result=subprocess.run(cmd,cwd=ROOT,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (logs/f'build_{i}.txt').write_text(result.stdout)
    records.append({'command':cmd,'returncode':result.returncode,'log':f'logs/build_{i}.txt'})
    if result.returncode:
        print(result.stdout[-5000:])
        raise SystemExit(result.returncode)
    print(f'Pass {i}: {cmd[0]} succeeded',flush=True)
text=(ROOT/(stem+'.log')).read_text(errors='replace')
bad=[line for line in text.splitlines() if re.search(r'Undefined control sequence|LaTeX Error|Missing character|Overfull \\[hv]box|undefined references|undefined citations|luaotfload: reverting',line)]
warnings=[line for line in text.splitlines() if 'Warning:' in line]
assert not bad,'\n'.join(bad)
assert not warnings,'\n'.join(warnings)
info=subprocess.run(['pdfinfo',str(ROOT/(stem+'.pdf'))],check=True,capture_output=True,text=True).stdout
page_match=re.search(r'^Pages:\s+(\d+)',info,re.M)
record={'engine':'LuaHBTeX / LuaLaTeX','passes':records,'document_errors':bad,'warnings':warnings,
        'pages':int(page_match.group(1)) if page_match else None,'pdf_bytes':(ROOT/(stem+'.pdf')).stat().st_size}
(ROOT/'outputs/build_pdf.json').write_text(json.dumps(record,indent=2)+'\n')
(ROOT/'outputs/pdfinfo.txt').write_text(info)
print(json.dumps({k:v for k,v in record.items() if k!='passes'},indent=2))
