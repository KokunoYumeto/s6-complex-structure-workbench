"""Typeset an individual sign-paper draft; does not certify mathematics."""
from pathlib import Path
import os,json,subprocess,sys
from fix_verified_legacy_locators import fix_legacy_locators
ROOT=Path(__file__).resolve().parents[1]
paper=sys.argv[1]
out=ROOT/'build'/('sign_'+paper)
out.mkdir(parents=True,exist_ok=True)
env=os.environ.copy()
env.update(json.loads((ROOT/'build/tex_runtime/environment.json').read_text()))
head=(ROOT/'preamble.tex').read_text()
parts=[(ROOT/'papers'/paper/name).read_text() for name in ['frontmatter.tex','opening.tex','body.tex']]
text=head+'\n\\begin{document}\n\\title{Paper '+paper+': working proof and layout review}\n\\author{}\n\\date{19 November 2026}\n\\maketitle\n'+'\n'.join(parts)+'\n\\end{document}\n'
(out/'preview.tex').write_text(fix_legacy_locators(text, 'build_sign_preview.'+paper)[0])
with (out/'stdout.txt').open('w') as f:
    p=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','preview.tex'],cwd=out,env=env,stdout=f,stderr=subprocess.STDOUT)
print(json.dumps({'paper':paper,'returncode':p.returncode,'output':str(out),'log_tail':(out/'stdout.txt').read_text()[-5000:]}))
