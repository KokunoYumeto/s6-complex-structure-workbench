#!/usr/bin/env python3
"""Build the paper with LuaLaTeX, using a local Debian TeX tree if needed."""
import os
import pathlib
import subprocess
import shutil
import sys

root = pathlib.Path(__file__).resolve().parents[1]
runtime = root.parent / '.apt/runtime/usr/share'
build = root / 'build'
build.mkdir(exist_ok=True)
env = os.environ.copy()
env['BIBINPUTS'] = str(root)+';'
if runtime.exists():
    env.update(TEXMFROOT=str(runtime/'texlive'),
               TEXMFDIST=str(runtime/'texlive/texmf-dist'),
               TEXMFDEBIAN=str(runtime/'texmf'),
               TEXMFCNF=str(runtime/'texlive/texmf-dist/web2c'),
               TEXMFVAR=str(build/'texvar'),
               TEXMFCONFIG=str(build/'texconfig'),
               TEXMF=str(build/'texvar')+','+str(runtime/'texmf')+','+str(runtime/'texlive/texmf-dist'))
    env['TEXMF'] = '{'+env['TEXMF']+'}'
    env['TEXFORMATS'] = str(build)+';'
    env['OPENTYPEFONTS'] = str(runtime/'texmf/fonts/opentype')+'//;'+str(runtime/'texlive/texmf-dist/fonts/opentype')+'//;'
    env['TTFONTS'] = str(runtime/'texmf/fonts/truetype')+'//;'+str(runtime/'texlive/texmf-dist/fonts/truetype')+'//;'
for name in ['texvar','texconfig']:
    (build/name).mkdir(exist_ok=True)
with open(root/'records/build_setup.out','w') as out:
    if not (build/'lualatex.fmt').exists():
        subprocess.run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',
                        '--jobname=lualatex','--progname=lualatex','lualatex.ini'],
                       cwd=build,env=env,stdout=out,stderr=subprocess.STDOUT,check=True)
resume='--resume' in sys.argv
latex_only='--latex-only' in sys.argv
aux=build/'S6_05_ARITHMETIC_paper.aux'
if aux.exists():
    aux.write_text('\n'.join(x for x in aux.read_text().splitlines()
                             if 'NAT@force@numbers' not in x)+'\n')
if not resume and not latex_only and (build/'S6_05_ARITHMETIC_paper.bbl').exists():
    (build/'S6_05_ARITHMETIC_paper.bbl').unlink()
with open(root/'records/paper_build.out','w') as out:
    for step in (['latex'] if latex_only else ['bibtex','latex','latex'] if resume else ['latex','bibtex','latex','latex']):
        cmd=(['bibtex','S6_05_ARITHMETIC_paper'] if step=='bibtex' else
             ['lualatex','--interaction=nonstopmode','--halt-on-error',
              '--output-directory=build','S6_05_ARITHMETIC_paper.tex'])
        subprocess.run(cmd,cwd=build if step=='bibtex' else root,
                       env=env,stdout=out,stderr=subprocess.STDOUT,check=True)
shutil.copyfile(build/'S6_05_ARITHMETIC_paper.pdf',root/'S6_05_ARITHMETIC_paper.pdf')
print(root/'S6_05_ARITHMETIC_paper.pdf')
