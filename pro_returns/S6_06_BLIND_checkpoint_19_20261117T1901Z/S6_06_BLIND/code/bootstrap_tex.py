"""Recover the LuaLaTeX runtime used for this audit from archived CTAN sources."""
from pathlib import Path
import os,subprocess,zipfile
root=Path(__file__).resolve().parents[1]
runtime=root.parent/'tex_runtime';runtime.mkdir(exist_ok=True)
packages=runtime/'packages';packages.mkdir(exist_ok=True)
for archive in (root/'records/tooling').glob('*.zip'):
    with zipfile.ZipFile(archive) as z:z.extractall(packages)
env=os.environ.copy();env['TEXMF']='/usr/share/texlive/texmf-dist'
subprocess.run(['luahbtex','-ini','-jobname=lualatex','-progname=lualatex',f'-output-directory={runtime}','lualatex.ini'],env=env,check=True)
subprocess.run(['luahbtex','--ini','--interaction=nonstopmode',r'\input plain \input lualibs.dtx'],cwd=packages/'lualibs',env=env,check=True)
env['TEXFORMATS']=str(runtime)
subprocess.run(['luahbtex','--fmt=lualatex','--interaction=nonstopmode','luatexbase.ins'],cwd=packages/'luatexbase',env=env,check=True)
print('Runtime restored. Run bash code/build_paper.sh from the artifact directory.')
