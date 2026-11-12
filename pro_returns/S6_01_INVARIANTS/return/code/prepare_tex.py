#!/usr/bin/env python3
"""Repair an incomplete TeX installation without editing system files.

This runtime supplied TeX trees but no search databases, LuaLaTeX format,
combined font map, Luaotfload or Lualibs. Full TeX Live needs no repair.
Usage: python code/prepare_tex.py PATH
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from zipfile import ZipFile

parser=argparse.ArgumentParser()
parser.add_argument('directory',type=Path)
args=parser.parse_args()
rt=args.directory.resolve()
for d in ['home','var','config','downloads','var/web2c/luahbtex','var/fonts/map/pdftex/updmap']:
    (rt/d).mkdir(parents=True,exist_ok=True)
sources=[]
for name in ['luaotfload','lualibs','lua-uni-algos']:
    url=f'https://mirrors.ctan.org/macros/luatex/generic/{name}.zip'
    archive=rt/(name+'.zip')
    if not archive.exists():
        subprocess.run(['curl','--fail','--location','--max-time','45','--retry','2','--output',str(archive),url],check=True)
    sources.append({'name':name,'url':url,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()})
    with ZipFile(archive) as z:
        assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
        z.extractall(rt/'downloads')
dist=Path('/usr/share/texlive/texmf-dist')
env=os.environ.copy()
env['TEXMF']=str(dist)
unpack=subprocess.run(['luahbtex','--ini','--interaction=nonstopmode',r'\input plain \input lualibs.dtx'],
                      cwd=rt/'downloads/lualibs',env=env,capture_output=True,text=True)
(rt/'lualibs_unpack.txt').write_text(unpack.stdout+unpack.stderr)
assert unpack.returncode==0
for name in ['luaotfload','lualibs','lua-uni-algos']:
    dst=rt/'home/tex/luatex'/name
    dst.mkdir(parents=True,exist_ok=True)
    for p in (rt/'downloads'/name).rglob('*'):
        if p.is_file() and p.suffix in ['.lua','.sty','.luc']:
            shutil.copy2(p,dst/p.name)
env.update(TEXMFVAR=str(rt/'var'),TEXMFCONFIG=str(rt/'config'),TEXMFHOME=str(rt/'home'))
fmt=rt/'var/web2c/luahbtex/lualatex.fmt'
if not fmt.exists():
    cmd=['luahbtex','--ini','--jobname=lualatex','--progname=lualatex',f'--output-directory={fmt.parent}','lualatex.ini']
    result=subprocess.run(cmd,env=env,capture_output=True,text=True)
    (rt/'format_build.txt').write_text(result.stdout+result.stderr)
    assert result.returncode==0
maps=list((dist/'fonts/map/dvips/amsfonts').glob('*.map'))
maps+=list((dist/'fonts/map/dvips/rsfs').glob('*.map'))
maps+=[Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map')]
(rt/'var/fonts/map/pdftex/updmap/pdftex.map').write_text('\n'.join(p.read_text() for p in maps))
record={'downloaded_dependencies':sources,'format':str(fmt),'map_sources':[str(p) for p in maps],
        'system_files_modified':False}
out=Path(__file__).resolve().parents[1]/'outputs/tex_environment.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print('Prepared a local TeX search/format/font tree; no system files changed.')
