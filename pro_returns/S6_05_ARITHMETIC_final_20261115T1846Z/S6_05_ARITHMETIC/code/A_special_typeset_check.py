"""Compile the independent endpoint and resolvent verification records."""
from pathlib import Path
import os
import subprocess

root=Path(__file__).resolve().parents[1]
build=root/'build'
runtime=root.parent/'.apt/runtime/usr/share'
env=os.environ.copy()
env.update(TEXMFROOT=str(runtime/'texlive'),
           TEXMFDIST=str(runtime/'texlive/texmf-dist'),
           TEXMFDEBIAN=str(runtime/'texmf'),
           TEXMFCNF=str(runtime/'texlive/texmf-dist/web2c'),
           TEXMFVAR=str(build/'texvar'),TEXMFCONFIG=str(build/'texconfig'),
           TEXMF='{'+str(build/'texvar')+','+str(runtime/'texmf')+','+str(runtime/'texlive/texmf-dist')+'}',
           TEXFORMATS=str(build)+';',
           OPENTYPEFONTS=str(runtime/'texmf/fonts/opentype')+'//;'+str(runtime/'texlive/texmf-dist/fonts/opentype')+'//;',
           TTFONTS=str(runtime/'texmf/fonts/truetype')+'//;'+str(runtime/'texlive/texmf-dist/fonts/truetype')+'//;')
preamble=(root/'S6_05_ARITHMETIC_paper.tex').read_text().split(r'\begin{document}')[0]
job='A_special_qa'
source=preamble+'\n'+r'\begin{document}'+'\n'
for part in ['A_special_resolvent_verification','A_endpoint_BV_insert']:
    source+=f'\\input{{records/{part}.tex}}\n'
source+=r'\end{document}'+'\n'
(build/(job+'.tex')).write_text(source)
with (root/'records/A_special_typeset_check.out').open('w') as out:
    subprocess.run(['lualatex','--interaction=nonstopmode','--halt-on-error',
                    '--output-directory=build','build/'+job+'.tex'],cwd=root,env=env,
                   stdout=out,stderr=subprocess.STDOUT,check=True)
log=(build/(job+'.log')).read_text()
for line in log.splitlines():
    if 'Overfull' in line or 'Output written' in line:
        print(line)
print('Independent A proofs compiled successfully.')
