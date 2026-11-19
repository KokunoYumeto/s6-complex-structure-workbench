from pathlib import Path
import os,json,subprocess,concurrent.futures,sys
W=Path(__file__).resolve().parents[2]
env=os.environ.copy();env.update(json.loads((W/'build/tex_runtime/environment.json').read_text()))
def run(paper):
 p=W/f'analysis/{paper}/preview';p.mkdir(exist_ok=True)
 front=W/f'papers/{paper}/frontmatter.tex'
 s=(W/'preamble.tex').read_text()+'\n\\begin{document}\n'+(front.read_text()+'\n' if front.exists() else '')+(W/f'papers/{paper}/opening.tex').read_text()+'\n'+(W/f'papers/{paper}/body.tex').read_text()+'\n\\end{document}\n'
 (p/'preview.tex').write_text(s)
 with (p/'stdout.txt').open('w') as f:r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','preview.tex'],cwd=p,env=env,stdout=f,stderr=subprocess.STDOUT)
 print(paper,r.returncode,flush=True)
 return {'paper':paper,'exit_code':r.returncode,'folder':str(p.relative_to(W))}
papers=sys.argv[1:] or ['IV','V']
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:out=list(ex.map(run,papers))
(W/'analysis/V/preview_build_results.json').write_text(json.dumps(out,indent=2))
