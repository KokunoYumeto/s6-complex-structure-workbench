#!/usr/bin/env python3
"""Build with pdfLaTeX twice and record boxes/references; local TeX bootstrap optional.

Usage: python code/build_pdf.py SOURCE.tex OUTDIR [--render]
The bootstrap only compensates for this execution image's missing generated
format/font-map databases. A normal TeX installation builds the standalone
source with two ordinary pdflatex invocations.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def tex_environment():
    env = os.environ.copy()
    probe = subprocess.run(['kpsewhich', 'pdflatex.fmt'], capture_output=True, text=True)
    if probe.returncode == 0 and probe.stdout.strip():
        return env, []
    runtime = ROOT / 'work/tex_runtime'
    runtime.mkdir(parents=True, exist_ok=True)
    env['TEXMF'] = '{./,/usr/share/texmf,/usr/share/texlive/texmf-dist}'
    fmt = runtime / 'pdflatex.fmt'
    if not fmt.exists():
        with (runtime/'format_build.txt').open('w') as log:
            subprocess.run(['pdftex', '-ini', '-etex', '-jobname=pdflatex',
                            '-interaction=nonstopmode', '-halt-on-error',
                            '-output-directory='+str(runtime), 'pdflatex.ini'],
                           env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
    mapfiles = [
        '/usr/share/texmf/fonts/map/dvips/lm/lm.map',
        '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/cm.map',
        '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/cmextra.map',
        '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/symbols.map',
        '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/latxfont.map',
        '/usr/share/texlive/texmf-dist/fonts/map/dvips/rsfs/rsfs.map',
    ]
    (runtime/'pdftex.map').write_text('\n'.join(Path(p).read_text() for p in mapfiles))
    env['TEXFONTMAPS'] = str(runtime)+'//:'
    return env, ['-fmt='+str(fmt)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=Path)
    parser.add_argument('outdir', type=Path)
    parser.add_argument('--render', action='store_true')
    args = parser.parse_args()
    source = args.source.resolve()
    outdir = args.outdir.resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    env, extra = tex_environment()
    command = ['pdflatex', *extra, '-interaction=nonstopmode', '-halt-on-error',
               '-file-line-error', '-output-directory='+str(outdir), str(source)]
    for run in (1, 2):
        with (outdir/f'console_{run}.txt').open('w') as log:
            completed = subprocess.run(command, cwd=source.parent, env=env,
                                       stdout=log, stderr=subprocess.STDOUT)
        if completed.returncode:
            print((outdir/f'console_{run}.txt').read_text()[-5000:])
            raise SystemExit(completed.returncode)
    log = (outdir/(source.stem+'.log')).read_text()
    overfull = []
    for match in re.finditer(r'Overfull \\([hv])box \(([^)]+)\)(.*?)(?=\n\n|\Z)', log, re.S):
        amount = re.search(r'([0-9.]+)pt', match.group(2))
        overfull.append({'axis':match.group(1), 'points':float(amount.group(1)) if amount else None,
                         'message':match.group(0)})
    pdf = outdir/(source.stem+'.pdf')
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
    result = {'source':source.name, 'pdf':pdf.name, 'pages':pages,
              'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
              'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
              'overfull_count':len(overfull),
              'overfull_over_2pt':sum(x['points'] is None or x['points']>2 for x in overfull),
              'max_overfull_pt':max([x['points'] or 0 for x in overfull], default=0),
              'overfull':overfull,
              'undefined_reference_warning':bool(re.search(r'(undefined references|Reference .+ undefined|Citation .+ undefined)', log)),
              'latex_warnings':re.findall(r'^LaTeX Warning:.*(?:\n(?!\n).*)?', log, re.M)}
    (outdir/'build_check.json').write_text(json.dumps(result, indent=2))
    if args.render:
        render = outdir/'pages'
        render.mkdir(exist_ok=True)
        subprocess.run(['pdftoppm','-r','85','-png',str(pdf),str(render/'page')], check=True)
    print(json.dumps({k:v for k,v in result.items() if k not in ('overfull','latex_warnings')}, indent=2))


if __name__ == '__main__':
    main()
