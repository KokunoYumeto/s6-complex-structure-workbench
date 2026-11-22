#!/usr/bin/env python3
"""Build the standalone papers with pdfLaTeX and report concrete log defects.

The local runtime repair only supplies missing generated TeX Live databases,
format and font-map files. Paper sources need standard TeX Live packages only.
"""
from pathlib import Path
import argparse, json, os, re, subprocess, hashlib

ROOT = Path(__file__).resolve().parents[1]

def environment(engine='pdflatex'):
    runtime = ROOT / 'tex-runtime'
    env = os.environ.copy()
    env['TEXMFCNF'] = str(runtime / 'web2c') + ':/usr/share/texlive/texmf-dist/web2c'
    for sub in ('web2c', 'tex/generic/config', 'fonts/map/pdftex'):
        (runtime / sub).mkdir(parents=True, exist_ok=True)
    (runtime / 'web2c/texmf.cnf').write_text(
        f'TEXMF = {{{runtime},/usr/share/texmf,/usr/share/texlive/texmf-dist}}\n'
        f'TEXMFVAR = {runtime}\nTEXMFCONFIG = {runtime}\n')
    (runtime / 'tex/generic/config/language.dat').write_text('english hyphen.tex\n')
    mapdirs = ['/usr/share/texmf/fonts/map/dvips/lm',
               '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts',
               '/usr/share/texlive/texmf-dist/fonts/map/dvips/rsfs']
    maps = [p for d in mapdirs for p in sorted(Path(d).glob('*.map'))]
    (runtime / 'fonts/map/pdftex/pdftex.map').write_text('\n'.join(p.read_text() for p in maps))
    env['TEXMFCACHE'] = str(runtime / 'lua-cache')
    env['OSFONTDIR'] = '/usr/share/texmf/fonts/opentype:/usr/share/fonts'
    if not (runtime / ('web2c/'+engine+'.fmt')).exists():
        with (runtime / (engine+'_format_build.out')).open('w') as log:
            binary = ['pdftex', '-ini', '-etex'] if engine == 'pdflatex' else ['luahbtex', '-ini']
            subprocess.run(binary + ['-interaction=nonstopmode',
                            '-halt-on-error', '-jobname='+engine, '-progname='+engine,
                            '-output-directory='+str(runtime/'web2c'), '*'+engine+'.ini'],
                           env=env, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True)
    return env

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tex', type=Path)
    ap.add_argument('--output-dir', type=Path)
    ap.add_argument('--passes', type=int, default=3)
    ap.add_argument('--engine', choices=['pdflatex', 'lualatex'], default='pdflatex')
    ns = ap.parse_args()
    tex = ns.tex.resolve()
    out = (ns.output_dir or ROOT/'build'/tex.stem).resolve()
    out.mkdir(parents=True, exist_ok=True)
    env = environment(ns.engine)
    for i in range(1, ns.passes+1):
        with (out/f'build_pass{i}.out').open('w') as log:
            result = subprocess.run([ns.engine, '-interaction=nonstopmode', '-halt-on-error',
                                     '-no-shell-escape', '-synctex=1', '-output-directory='+str(out), str(tex)],
                                    cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
        if result.returncode:
            print((out/f'build_pass{i}.out').read_text()[-6000:])
            raise SystemExit(result.returncode)
    log = (out/(tex.stem+'.log')).read_text(errors='replace')
    overfull = []
    for m in re.finditer(r'Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)', log):
        overfull.append({'pt': float(m[1]), 'context': log[max(0,m.start()-100):m.end()+500]})
    summary = {
        'source': str(tex), 'source_sha256': hashlib.sha256(tex.read_bytes()).hexdigest(),
        'pdf_sha256': hashlib.sha256((out/(tex.stem+'.pdf')).read_bytes()).hexdigest(),
        'engine': 'pdfLaTeX' if ns.engine == 'pdflatex' else 'LuaLaTeX', 'shell_escape': False,
        'overfull_total': len(overfull),
        'overfull_above_2pt': sum(x['pt'] > 2 for x in overfull),
        'undefined_references': len(re.findall(r'Reference .*? undefined', log)),
        'undefined_citations': len(re.findall(r'Citation .*? undefined', log)),
        'missing_characters': len(re.findall(r'Missing character:', log)),
        'missing_fonts': len(re.findall(r'Font .*?not found|font .*?not loadable',log)),
        'multiply_defined': len(re.findall(r'multiply defined',log)),
        'duplicate_destinations': len(re.findall(r'destination with the same identifier',log)),
        'overfull': overfull,
    }
    (out/'build_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='overfull'},indent=2))

if __name__ == '__main__':
    main()
