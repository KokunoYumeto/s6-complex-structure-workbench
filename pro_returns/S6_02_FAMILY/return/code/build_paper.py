"""Rebuild the supplied paper with LuaLaTeX and BibTeX.

The complete compiler output is saved to build_lualatex.out.
Run from any directory: python3 code/build_paper.py
"""
from pathlib import Path
import subprocess
import re
from tex_environment import environment

ROOT=Path(__file__).resolve().parents[1]
stem='S6_02_FAMILY_paper'
env=environment()
commands=[['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',stem+'.tex'],
          ['bibtex',stem],
          ['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',stem+'.tex'],
          ['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',stem+'.tex']]
with (ROOT/'code/build_lualatex.out').open('w',encoding='utf-8') as log:
    for command in commands:
        log.write('COMMAND '+repr(command)+'\n'); log.flush()
        p=subprocess.run(command,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        log.write(p.stdout); log.write('\nEXIT '+str(p.returncode)+'\n'); log.flush()
        print(command[0], 'exit',p.returncode,flush=True)
        if p.returncode:
            print(p.stdout[-10000:]); raise SystemExit(p.returncode)
final=(ROOT/(stem+'.log')).read_text(encoding='utf-8',errors='replace')
warnings=[line for line in final.splitlines() if re.search(r'Undefined control|undefined|Overfull|Missing character|LaTeX Warning',line)]
print('FINAL_WARNINGS',len(warnings))
for line in warnings: print(line)
print('PDF_BYTES',(ROOT/(stem+'.pdf')).stat().st_size)
