#!/usr/bin/env python3
"""Compile C.7.9 independently of the shared master build."""
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
section = sys.argv[1] if len(sys.argv)>1 else 'C_diagonal_obstruction'
labels = {'C_diagonal_obstruction':'Cdiagonal',
          'C_cm_enlargement':'Cenlargement',
          'C_complexified':'Ccomplexified',
          'C_cm_transcendence':'Ccmtranscendence'}
label = labels[section]
job = label+'_qa'
build = root / 'build'
runtime = root.parent / '.apt/runtime/usr/share'
env = os.environ.copy()
env.update(TEXMFROOT=str(runtime/'texlive'),
           TEXMFDIST=str(runtime/'texlive/texmf-dist'),
           TEXMFDEBIAN=str(runtime/'texmf'),
           TEXMFCNF=str(runtime/'texlive/texmf-dist/web2c'),
           TEXMFVAR=str(build/'texvar'),
           TEXMFCONFIG=str(build/'texconfig'),
           TEXMF='{'+str(build/'texvar')+','+str(runtime/'texmf')+','+
                 str(runtime/'texlive/texmf-dist')+'}',
           TEXFORMATS=str(build)+';',
           OPENTYPEFONTS=str(runtime/'texmf/fonts/opentype')+'//;'+
                         str(runtime/'texlive/texmf-dist/fonts/opentype')+'//;',
           TTFONTS=str(runtime/'texmf/fonts/truetype')+'//;'+
                   str(runtime/'texlive/texmf-dist/fonts/truetype')+'//;')
preamble = (root/'S6_05_ARITHMETIC_paper.tex').read_text().split(r'\begin{document}')[0]
source = preamble+'\n'+r'\begin{document}'+'\n'+f'\\input{{sections/{section}.tex}}\n'+r'\end{document}'+'\n'
(build/(job+'.tex')).write_text(source)
with (root/'records'/(label+'_typeset_check.out')).open('w') as out:
    subprocess.run(['lualatex','--interaction=nonstopmode','--halt-on-error',
                    '--output-directory=build','build/'+job+'.tex'],
                   cwd=root,env=env,stdout=out,stderr=subprocess.STDOUT,check=True)
log = (build/(job+'.log')).read_text()
for line in log.splitlines():
    if 'Overfull' in line or 'Output written' in line:
        print(line)
print('Section compilation passed.')
