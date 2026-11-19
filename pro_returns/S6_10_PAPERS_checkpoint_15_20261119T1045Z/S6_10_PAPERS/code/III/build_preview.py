"""Compile the complete current Paper III draft without conferring proof credit."""
from pathlib import Path
import os,json,subprocess,datetime
B=Path(__file__).resolve().parents[2];D=B/'build/III_preview';D.mkdir(parents=True,exist_ok=True)
parts=['opening','00_conventions','01_maps','02_kummer','03_manifolds','03b_os49','04_fibre_products','05_carriers','06_collision','07_receiving_applications','08_open_points']
s=(B/'preamble.tex').read_text()+'\n\\usepackage{tikz-cd}\n\\begin{document}\n\\title{Maps, manifolds and cusp carriers}\n\\author{AI-produced mathematical text}\n\\date{18 November 2026}\n\\maketitle\n'+'\n'.join((B/'papers/III'/f'{p}.tex').read_text() for p in parts)+'\n\\end{document}\n'
(D/'preview.tex').write_text(s)
env=dict(os.environ);env.update(json.loads((B/'build/tex_runtime/environment.json').read_text()))
with (D/'stdout.txt').open('w') as f:r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','preview.tex'],cwd=D,env=env,stdout=f,stderr=subprocess.STDOUT)
out={'returncode':r.returncode,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tex':str(D/'preview.tex'),'pdf':str(D/'preview.pdf'),'scope':'Complete receiving draft; cross-paper reference and bibliography resolution belong to parent integration. Typesetting does not imply a mathematical check.','tail':(D/'stdout.txt').read_text()[-5000:]}
(B/'analysis/III_preview_build.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
