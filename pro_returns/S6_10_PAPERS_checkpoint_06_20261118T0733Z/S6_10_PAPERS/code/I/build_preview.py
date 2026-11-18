"""Typeset the current Paper I receiving fragments; no proof certification."""
from pathlib import Path
import os,json,subprocess
OUT=Path(__file__).resolve().parents[2];DEST=OUT/'build/I_preview';DEST.mkdir(parents=True,exist_ok=True)
parts=['opening','00_conventions','model_comparison','01_periods','02_moduli','03_monodromy_and_fibres','figures','06_ends','11_uniform_end','04_hodge','05_twisted_tangent','08_higher_multiplicities','09_integral_circle','07_arithmetic','10_interval_certificate','90_credited_appendices','91_credited_night','99_open_questions']
body='\n'.join((OUT/'papers/I'/f'{x}.tex').read_text() for x in parts)
text=(OUT/'preamble.tex').read_text()+'\n\\begin{document}\n\\title{The $(3,4,\\infty)$ family: periods, moduli and the two ends}\n\\author{AI-produced mathematical text}\n\\date{18 November 2026}\n\\maketitle\n'+body+'\n\\end{document}\n'
(DEST/'preview.tex').write_text(text)
env=dict(os.environ);env.update(json.loads((OUT/'build/tex_runtime/environment.json').read_text()))
with (DEST/'stdout.txt').open('w') as f:
 r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','preview.tex'],cwd=DEST,env=env,stdout=f,stderr=subprocess.STDOUT)
print(json.dumps({'returncode':r.returncode,'output':str(DEST),'tail':(DEST/'stdout.txt').read_text()[-5000:]}))
