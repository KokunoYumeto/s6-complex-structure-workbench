"""Compile reference editions from attached TeX; preserve mathematical text.

Page locators for these builds are explicitly labelled 'attached-source edition'.
DGKX's unavailable newtx fonts are replaced by Latin Modern. This is recorded
rather than representing the new pagination as the publisher's pagination.
"""
from pathlib import Path
import os,json,hashlib,subprocess,concurrent.futures,shutil,re
ROOT=Path(__file__).resolve().parents[3]
PROJECT=ROOT/'work/S6_10_PAPERS'; OUT=PROJECT/'build/literature';OUT.mkdir(exist_ok=True)
env=os.environ.copy();env.update(json.loads((PROJECT/'build/tex_runtime/environment.json').read_text()))
fonts=['cm.map','cmextra.map','symbols.map','euler.map','latxfont.map','rsfs.map','lm.map','xypic.map']
sources_old=[('DGKXv1',ROOT/'sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex'),('DGKXv2',ROOT/'sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie.tex')]
sources=[
 ('CDP20',ROOT/'sources/papers/arXiv_1904.11179v2_CDP20_corrigendum_src/main.tex'),
 ('LRS',ROOT/'sources/papers/arXiv_1912.09719_Lehn_Rollenske_Schinko_src/main.tex'),
 ('ViacCombs',ROOT/'sources/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex'),
 ('ViacTwo',ROOT/'sources/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex'),
 ('ViacLog',ROOT/'sources/papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex'),
 ('Engel',ROOT/'sources/papers/arXiv_2609.38442_Engel_src/S6.tex'),
 ('LiuRollenske',ROOT/'sources/papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex')]
def build(item):
 name,src=item;folder=OUT/name;folder.mkdir(exist_ok=True)
 text=src.read_text(encoding='utf-8',errors='strict').replace(r'\usepackage{newtxtext,microtype}',r'\usepackage{lmodern,microtype}').replace(r'\usepackage{newtxmath}','')
 # Only engine/package edits; record each explicitly. No mathematical text edits.
 edits=['explicit installed font maps','remove pdftex hyperref driver for LuaLaTeX']
 text=text.replace('backref=page,pdftex,','backref=page,').replace('bookmarks, pdftex','bookmarks').replace(r'\usepackage[latin1]{inputenc}','').replace(',extarrows}', '}').replace(r'\usepackage{soul}','').replace(r'\usepackage{bbm}','')
 edits.append('remove unused extarrows and soul imports and latin1 declaration from UTF-8 source')
 if name in ['Engel','CDP20']:
  if name=='Engel':
   assert r'\xymatrix' not in text and r'\xy ' not in text
   text=text.replace(r'\usepackage[all]{xy}','')
   edits.append('remove unused xy package')
  else:
   text=text.replace(r'\usepackage[all]{xy}',r'\usepackage{tikz-cd}').replace(r'\usepackage{xypic}','').replace(r'\xyoption{all}','')
   old=r'''\xymatrix{ 
\tilde S \ar[d]_{\tilde p} \ar[r]^{\eta} & S \ar[d]^{p}\\
B\ar[r]_{\tau} & B'.}'''
   new=r'''\begin{tikzcd}
\tilde S \arrow[d,"\tilde p"'] \arrow[r,"\eta"] & S \arrow[d,"p"]\\
B \arrow[r,"\tau"'] & B'
\end{tikzcd}'''
   assert old in text
   text=text.replace(old,new)
   edits.append('translate the sole square diagram from xypic to identical tikz-cd arrows and labels')
 for dep in src.parent.iterdir():
  if dep.suffix in ['.sty','.bbl','.png','.jpg']:
   dest=folder/dep.name
   if dep.suffix=='.bbl':dest=folder/(name+'.bbl')
   shutil.copy2(dep,dest)
   if name=='LiuRollenske' and dep.suffix=='.sty':
    dest.write_text(dest.read_text().replace('dvipsnames, pdftex','dvipsnames'))
    edits.append('remove pdftex driver from copied local color package declaration')
 end=text.index('\n',text.index(r'\documentclass'))
 text=text[:end]+''.join('\n\\pdfextension mapfile{+'+f+'}' for f in fonts)+text[end:]
 target=folder/(name+'.tex');target.write_text(text)
 record={'source':str(src.relative_to(ROOT)),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'edits':edits,'locator_convention':'attached-source edition; do not use as publisher pagination'}
 (folder/'edition_record.json').write_text(json.dumps(record,indent=2))
 for n in range(2):
  r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error',target.name],cwd=folder,env=env,capture_output=True,text=True)
  (folder/f'build_{n}.stdout').write_text(r.stdout+r.stderr)
  if r.returncode:return {'name':name,'exit':r.returncode,'tail':r.stdout[-2200:]}
 return {'name':name,'exit':0,'pdf':str(target.with_suffix('.pdf')),'tail':r.stdout[-500:]}
sources=[x for x in sources if x[0] == 'LRS']
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for r in pool.map(build,sources):print(json.dumps(r),flush=True)
