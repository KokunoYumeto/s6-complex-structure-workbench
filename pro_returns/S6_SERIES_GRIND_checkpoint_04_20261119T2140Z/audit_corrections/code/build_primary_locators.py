"""Compile attached primary TeX without changing its body, only for locators.

No successful typesetting or visual-verification claim is inferred from this
script. Each compiler exit code and exact source hash is retained.
"""
from pathlib import Path
import argparse, hashlib, json, os, subprocess

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parents[1] / 'primary_builds'
out.mkdir(exist_ok=True)
lit = root / 'S6_SERIES_GRIND_source/S6_GRIND_6_literature/papers'
items = {
    'DGKXv1': lit / 'arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex',
    'DGKXv2': lit / 'arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex',
    'Mandal': lit / 'arXiv_2609.27929_Mandal_src/FINAL.tex',
    'Yang2026': lit / 'arXiv_2609.29666_Yang_src/Compact_Complex_Threefolds_REPAIRED_v4_5.tex',
}
parser = argparse.ArgumentParser()
parser.add_argument('--engine', default='pdflatex')
args = parser.parse_args()
records = []
build_env = dict(os.environ)
if args.engine == 'lualatex':
    build_env['TEXMFHOME'] = str(root / 'S6_SERIES_GRIND_work/build/texlive-luatex/usr/share/texlive/texmf-dist')
    build_env['TEXMFCACHE'] = '.'
for key, source in items.items():
    target = out / (key+'_'+args.engine)
    target.mkdir(exist_ok=True)
    cmd = [args.engine, '-interaction=nonstopmode', '-file-line-error',
           '-output-directory='+str(target), '-jobname='+key, str(source)]
    result = subprocess.run(cmd, cwd=target, env=build_env, capture_output=True, text=True)
    (target / 'build.stdout').write_text(result.stdout + result.stderr)
    record = {'key': key, 'source': str(source),
              'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'command': cmd, 'exit_code': result.returncode,
              'pdf_present': (target / (key+'.pdf')).exists(),
              'aux_present': (target / (key+'.aux')).exists()}
    records.append(record)
    print(json.dumps(record), flush=True)
(out / ('build_results_'+args.engine+'.json')).write_text(json.dumps(records, indent=2)+'\n')
