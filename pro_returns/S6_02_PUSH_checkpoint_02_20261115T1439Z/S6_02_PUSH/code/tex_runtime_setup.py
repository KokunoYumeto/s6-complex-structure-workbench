#!/usr/bin/env python3
"""Create a workspace-local LuaLaTeX runtime without changing /usr or HOME.

The image has TeX Live trees but dangling system ls-R/format links and lacks
the texlive-luatex files.  Extract the distribution-matched Debian package
locally, search all trees without database-only (!!) restrictions, and build
the genuine LuaHBTeX lualatex format in a writable local directory.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request

PACKAGE = Path(__file__).resolve().parents[1]
RUNTIME = PACKAGE.parent / 'tex_runtime'
ENV_FILE = PACKAGE / 'code' / 'tex_runtime_environment.json'

def run(args, *, cwd=None, env=None, logfile=None):
    print('RUN', args, flush=True)
    p = subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True)
    output = p.stdout + p.stderr
    if logfile:
        Path(logfile).write_text(output)
    print(output[-12000:], end='', flush=True)
    print('RETURN', p.returncode, flush=True)
    if p.returncode:
        raise RuntimeError(f'Command failed: {args}')
    return output

def fetch(url, dest):
    if dest.exists() and dest.stat().st_size:
        print('CACHED', dest, dest.stat().st_size, flush=True)
        return
    print('FETCH', url, flush=True)
    req=urllib.request.Request(url, headers={'User-Agent':'Research-document-build/1.0'})
    with urllib.request.urlopen(req, timeout=45) as response:
        data=response.read()
    dest.write_bytes(data)
    print('DOWNLOADED', len(data), 'SHA256', hashlib.sha256(data).hexdigest(), flush=True)

def runtime_environment():
    for name in ['downloads','deb','home','var','config','sysvar','sysconfig','cache','formats','logs']:
        (RUNTIME/name).mkdir(parents=True, exist_ok=True)
    local_dist=RUNTIME/'deb/usr/share/texlive/texmf-dist'
    trees=[str(RUNTIME/'home'),str(RUNTIME/'var'),str(RUNTIME/'config'),
           str(local_dist),str(RUNTIME/'deb/usr/share/texmf'),
           '/usr/share/texmf','/usr/share/texlive/texmf-dist']
    values={
        'TEXMFHOME':str(RUNTIME/'home'),
        'TEXMFVAR':str(RUNTIME/'var'),
        'TEXMFCONFIG':str(RUNTIME/'config'),
        'TEXMFSYSVAR':str(RUNTIME/'sysvar'),
        'TEXMFSYSCONFIG':str(RUNTIME/'sysconfig'),
        'TEXMFCACHE':str(RUNTIME/'cache'),
        # LuaHBTeX obeys the existing openout_any=p policy for Lua io.open.
        # Declare the intended cache output directory rather than weakening it.
        'TEXMFOUTPUT':str(RUNTIME/'cache'),
        'TEXMF':'{'+','.join(trees)+'}',
        'TEXMFDBS':str(RUNTIME/'home'),
        'TEXFORMATS':str(RUNTIME/'formats')+'//:',
        'VARTEXFONTS':str(RUNTIME/'var/fonts'),
    }
    ENV_FILE.write_text(json.dumps(values,indent=2)+'\n')
    return {**os.environ,**values}

def main():
    env=runtime_environment()
    if '--maps-only' in sys.argv:
        install_font_maps(env)
        return
    base='https://deb.debian.org/debian/pool/main/t/texlive-base/'
    listing=RUNTIME/'downloads/texlive-base-index.html'
    fetch(base,listing)
    candidates=sorted(set(re.findall(r'href="(texlive-luatex_[^"]+_all\.deb)"',listing.read_text())))
    print('AVAILABLE_LUATEX_PACKAGES',candidates,flush=True)
    matching=[p for p in candidates if p.startswith('texlive-luatex_2024.20250309')]
    if not matching:
        matching=[p for p in candidates if p.startswith('texlive-luatex_2024.')]
    if not matching:
        raise RuntimeError('No package matching the installed TeX Live 2025/dev distribution')
    name=matching[-1]
    archive=RUNTIME/'downloads'/name
    fetch(base+name,archive)
    run(['dpkg-deb','-x',str(archive),str(RUNTIME/'deb')],logfile=RUNTIME/'logs/extract.txt')
    # The image also has a dangling system updmap.cfg/pdftex.map.  Generate
    # local outline-font maps so ordinary mathematical fonts embed as Type 1.
    install_font_maps(env)
    for filename in ['lualatex.ini','latex.ltx','luaotfload-main.lua','lualibs.lua','fontspec.sty']:
        run(['kpsewhich',filename],env=env,logfile=RUNTIME/'logs'/('kpse_'+filename+'.txt'))
    run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',
         '--jobname=lualatex','--progname=lualatex','lualatex.ini'],
        cwd=RUNTIME/'formats',env=env,logfile=RUNTIME/'logs/format.txt')
    test=RUNTIME/'runtime_check.tex'
    test.write_text(r'''\documentclass{article}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage{amsmath,amssymb,amsthm,mathtools,microtype,booktabs,longtable,array,enumitem}
\usepackage[authoryear,round]{natbib}
\usepackage[hidelinks,unicode]{hyperref}
\usepackage{xurl}
\begin{document}
LuaLaTeX runtime: $H^q(X,T_X)=(1,1,1,0)$.
\end{document}
''')
    run(['lualatex','--interaction=nonstopmode','--halt-on-error',test.name],
        cwd=RUNTIME,env=env,logfile=RUNTIME/'logs/runtime_check.txt')
    print('ENVIRONMENT',ENV_FILE,flush=True)
    print('FORMAT',RUNTIME/'formats/lualatex.fmt',flush=True)
    print('VERIFIED_PDF',RUNTIME/'runtime_check.pdf',flush=True)

def install_font_maps(env):
    map_config=RUNTIME/'config/web2c/updmap.cfg'
    map_config.parent.mkdir(parents=True,exist_ok=True)
    ams_maps=sorted(Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts').glob('*.map'))
    map_config.write_text(''.join('MixedMap '+p.name+'\n' for p in ams_maps)+'Map lm.map\n')
    run(['updmap','--user','--cnffile',str(map_config),'--nohash'],
        env=env,logfile=RUNTIME/'logs/updmap.txt')
    pdfmap=RUNTIME/'var/fonts/map/pdftex/updmap/pdftex.map'
    content=pdfmap.read_text()
    for name in ['eufm10','msam10','msbm10','cmmi10','cmsy10','cmex10']:
        assert re.search(r'^'+name+r'\s',content,re.M), name+' absent from map'
    print('VERIFIED_ALL_AMS_MAPS', [p.name for p in ams_maps],flush=True)

if __name__=='__main__':
    main()
