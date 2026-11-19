"""Compile attached arithmetic sources with explicit installed font maps.
Mathematical source text is preserved; layout adaptations are in each receipt.
"""
from pathlib import Path
import os,json,hashlib,subprocess,shutil,concurrent.futures
PROJECT=Path(__file__).resolve().parents[2]
ROOT=PROJECT.parents[1]
env=os.environ.copy();env.update(json.loads((PROJECT/'build/tex_runtime/environment.json').read_text()))
items=[('Bertolin','arXiv_2010.15170_Bertolin_Philippon_Saha_Saha_src/SemiAbelianTowers-final.tex'),('DeMarco','arXiv_1701.07947_DeMarco_Mavraki_src/VCHequidistribution_arxiv_v_2.tex'),('Huber','arXiv_1805.10104_Huber_Wuestholz_src/gesamt-ams.tex')]
def build(item):
 name,rel=item;src=ROOT/'sources/papers'/rel;folder=PROJECT/'build/literature'/name;folder.mkdir(exist_ok=True)
 s=src.read_text();at=s.index('\n',s.index(r'\documentclass'))
 maps=['cm.map','cmextra.map','symbols.map','euler.map','latxfont.map','rsfs.map','lm.map','xypic.map']
 s=s[:at]+''.join('\n'+r'\pdfextension mapfile{+'+m+'}' for m in maps)+s[at:]
 for dep in src.parent.iterdir():
  if dep.suffix in ['.sty','.bbl','.png','.jpg','.pdf']:
   dst=folder/((name+'.bbl') if dep.suffix=='.bbl' else dep.name);shutil.copy2(dep,dst)
 (folder/(name+'.tex')).write_text(s)
 (folder/'edition_record.json').write_text(json.dumps({'source':str(src.relative_to(ROOT)),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'edits':['explicit installed font maps'],'locator_convention':'attached-source edition'},indent=2))
 for i in range(2):
  r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],cwd=folder,env=env,capture_output=True,text=True)
  (folder/f'build_{i}.stdout').write_text(r.stdout+r.stderr)
  if r.returncode:return {'name':name,'exit':r.returncode,'tail':r.stdout[-1800:]}
 return {'name':name,'exit':0,'tail':r.stdout[-500:]}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for result in pool.map(build,items):print(json.dumps(result),flush=True)
