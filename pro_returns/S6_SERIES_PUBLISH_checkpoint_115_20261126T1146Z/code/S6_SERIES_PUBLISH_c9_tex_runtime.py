"""Generate a project-local format using the installed legacy TeX distribution."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'agents/continuation9_tex_runtime'

def environment():
    e = os.environ.copy()
    e['TEXMFVAR'] = str(WORK / 'texmf-var')
    e['TEXMFCONFIG'] = str(WORK / 'texmf-config')
    e['TEXMF'] = '{' + ','.join(str(WORK / x) for x in ('texmf-config', 'texmf-var', 'texmf')) + ',/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}'
    e['TEXFORMATS'] = str(WORK / 'texmf-var/web2c') + '//:'
    e['TEXMFDBS'] = ''
    e['MKTEXFMT'] = '0'
    return e

def prepare():
    for x in ('texmf-var', 'texmf-config', 'texmf/web2c', 'texmf/tex/generic/config', 'texmf/fonts/map/pdftex'):
        (WORK / x).mkdir(parents=True, exist_ok=True)
    (WORK / 'texmf/tex/generic/config/language.dat').write_text('english hyphen.tex\n=usenglish\n=USenglish\n=american\n', newline='\n')
    config = WORK / 'texmf/web2c/fmtutil.cnf'
    config.write_text('pdflatex pdftex language.dat -translate-file=cp227.tcx *pdflatex.ini\n', newline='\n')
    parts = []
    for name in ('cm.map', 'cmextra.map', 'symbols.map', 'euler.map', 'latxfont.map', 'rsfs.map', 'lm.map'):
        q = subprocess.run(['kpsewhich', name], env=environment(), capture_output=True, text=True, check=True).stdout.strip()
        parts.append(Path(q).read_text())
        print('font map', name, q)
    (WORK / 'texmf/fonts/map/pdftex/pdftex.map').write_text('\n'.join(parts), newline='\n')
    p = subprocess.run(['fmtutil-user', '--cnffile=' + str(config), '--byfmt', 'pdflatex'], env=environment(), cwd=WORK, capture_output=True, text=True)
    (ROOT / 'code/S6_SERIES_PUBLISH_c9_tex_format.out').write_text(p.stdout, newline='\n')
    (ROOT / 'code/S6_SERIES_PUBLISH_c9_tex_format.err').write_text(p.stderr, newline='\n')
    print('format exit', p.returncode)
    if p.returncode:
        print(p.stdout[-4000:], p.stderr[-4000:])
    return p.returncode

if __name__ == '__main__':
    if sys.argv[1:] == ['prepare']:
        sys.exit(prepare())
    sys.exit(subprocess.call(['pdflatex', '-no-shell-escape', *sys.argv[1:]], env=environment()))
