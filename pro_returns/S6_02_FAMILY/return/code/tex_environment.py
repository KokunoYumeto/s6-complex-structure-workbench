"""Supply workspace-local TeX search paths and formats on minimal installations.

A normally configured TeX Live installation needs none of this bootstrap.
The document uses native TeX metric fonts (Latin Modern), not OpenType fonts.
No system directory is changed.
"""
from pathlib import Path
import os
import subprocess
import hashlib

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'tex_workspace_cache'

def environment():
    env=os.environ.copy()
    found=subprocess.run(['kpsewhich','latex.ltx'],env=env,text=True,capture_output=True)
    if not found.stdout.strip():
        CACHE.mkdir(exist_ok=True)
        env['TEXMF']='{'+str(CACHE)+',/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}'
        env['TEXMFVAR']=str(CACHE)
        env['TEXMFCONFIG']=str(CACHE)
        env['TEXMFCACHE']=str(CACHE)
        env['TEXFORMATS']=str(CACHE)+':'
        env['TEXFONTMAPS']=str(CACHE)+':'
        maps=[Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map')]
        maps += [Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts')/n
                 for n in ['cm.map','cmextra.map','symbols.map','latxfont.map','euler.map']]
        (CACHE/'pdftex.map').write_text('\n'.join(p.read_text() for p in maps),encoding='utf-8')
    # The minimal image has LuaHBTeX and the LaTeX kernel, but omits the
    # optional OpenType loader. Configure the kernel's existing OT1 fallback
    # before creating the local format. The document subsequently selects
    # T1/Latin Modern through native metric fonts. The standard system kernel
    # is not modified; full TeX Live installations do not enter this branch.
    loader=subprocess.run(['kpsewhich','luaotfload-main.lua'],env=env,text=True,capture_output=True)
    rebuild=False
    if not loader.stdout.strip():
        CACHE.mkdir(exist_ok=True)
        env['TEXFORMATS']=str(CACHE)+':'
        original=Path('/usr/share/texlive/texmf-dist/tex/latex/base/latex.ltx').read_text()
        patched=original.replace("if xpcall(function ()%", "if kpse.find_file('luaotfload-main.lua') and xpcall(function ()%",1)
        patched=patched.replace("texio.write_nl('Error in luaotfload: reverting to OT1')%", "texio.write_nl('Native TeX metric font mode; OpenType hook unused')%",1)
        assert patched!=original
        target=CACHE/'tex/latex/base/latex.ltx'
        target.parent.mkdir(parents=True,exist_ok=True)
        if not target.exists() or target.read_text()!=patched:
            target.write_text(patched); rebuild=True
        (CACHE/'kernel_source.sha256').write_text(hashlib.sha256(original.encode()).hexdigest()+'\n')
    found=subprocess.run(['kpsewhich','lualatex.fmt'],env=env,text=True,capture_output=True)
    if not found.stdout.strip() or rebuild:
        CACHE.mkdir(exist_ok=True)
        env['TEXFORMATS']=str(CACHE)+':'
        p=subprocess.run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',
                          '--jobname=lualatex','lualatex.ini'],cwd=CACHE,env=env,
                         text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (ROOT/'code/tex_bootstrap.out').write_text(p.stdout,encoding='utf-8')
        if p.returncode:
            print(p.stdout[-12000:]); raise RuntimeError('LuaLaTeX format bootstrap failed')
    return env

if __name__=='__main__':
    e=environment()
    print('LuaLaTeX format and native metric-font search paths ready.')
    print(subprocess.run(['kpsewhich','lualatex.fmt'],env=e,text=True,capture_output=True).stdout.strip())
