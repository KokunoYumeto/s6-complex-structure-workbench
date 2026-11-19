"""Snapshot current authoring fragments, build previews, then standalone papers.

This is source assembly and typesetting only. It grants no proof check.
"""
from pathlib import Path
import concurrent.futures,hashlib,json,os,subprocess
P=Path(__file__).resolve().parents[2]
env=os.environ.copy();env.update(json.loads((P/'build/tex_runtime/environment.json').read_text()))
spec={
 'I':('build/I_preview',['opening','00_conventions','model_comparison','01_periods','02_moduli','03_monodromy_and_fibres','figures','06_ends','11_uniform_end','04_hodge','05_twisted_tangent','08_higher_multiplicities','09_integral_circle','07_arithmetic','10_interval_certificate','90_credited_appendices','91_credited_night','99_open_questions']),
 'II':('build/sign_II',['frontmatter','opening','body']),
 'III':('build/III_preview',['opening','00_conventions','01_maps','02_kummer','03_manifolds','03b_os49','04_fibre_products','05_carriers','06_collision','07_receiving_applications','08_open_points']),
 'IV':('analysis/IV/preview',['frontmatter','opening','body']),
 'V':('analysis/V/preview',['frontmatter','opening','body']),
 'VI':('build/sign_VI',['frontmatter','opening','body'])}
titles={'I':r'The $(3,4,\infty)$ family: periods, moduli and the two ends',
 'III':'Maps, manifolds and cusp carriers'}
receipts={}
for paper,(folder,names) in spec.items():
    B=P/folder;B.mkdir(parents=True,exist_ok=True)
    files=[P/'preamble.tex']+[P/'papers'/paper/(n+'.tex') for n in names]
    data=[f.read_text() for f in files]
    front=(r'\title{'+titles[paper]+r'}\author{AI-produced mathematical text}\date{19 November 2026}\maketitle'+'\n') if paper in titles else ''
    body='\n'.join(data[1:])
    if r'\maketitle' not in body and paper not in titles:
        front=r'\title{Paper '+paper+r'}\author{AI-produced mathematical text}\date{19 November 2026}\maketitle'+'\n'
    text=data[0]+'\n'+r'\begin{document}'+'\n'+front+body+'\n'+r'\end{document}'+'\n'
    text=text.replace(r'\date{18 November 2026}',r'\date{19 November 2026}')
    (B/'preview.tex').write_text(text)
    receipts[paper]={'sources':{str(f.relative_to(P)):hashlib.sha256(s.encode()).hexdigest() for f,s in zip(files,data)},'preview_sha256':hashlib.sha256(text.encode()).hexdigest()}
def preview(paper):
    B=P/spec[paper][0]
    with (B/'continuation_preview.stdout').open('w') as f:
        r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','preview.tex'],cwd=B,env=env,stdout=f,stderr=subprocess.STDOUT)
    receipts[paper]['preview_exit']=r.returncode
    print(paper,'preview',r.returncode,flush=True)
    return r.returncode
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    codes=list(pool.map(preview,spec))
(P/'analysis/continuation_root/current_build_batch.json').write_text(json.dumps(receipts,indent=2)+'\n')
if any(codes):raise SystemExit('Preview failed; inspect exact per-paper logs')
run=subprocess.run(['python3',str(P/'code/build_standalone.py'),'--jobs','3'],cwd=P,env=env)
raise SystemExit(run.returncode)
