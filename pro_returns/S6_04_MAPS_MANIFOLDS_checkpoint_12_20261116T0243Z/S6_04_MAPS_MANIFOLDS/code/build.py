"""Assemble the section order and bibliography, then run LuaLaTeX/BibTeX.

The optional local TeX support is used only in the present minimal runtime;
the manuscript itself uses standard packages on a full TeX Live install.
"""
from pathlib import Path
import os,subprocess,re,json,csv,hashlib
root=Path(__file__).resolve().parents[1]
runtime=root.parent/'tex_runtime'
maps=root/'sections/maps.tex'
if maps.exists():
 text=maps.read_text(); marker=r'\subsection{B.1.'
 at=text.index(marker)
 (root/'sections/maps_A.tex').write_text('% Generated from maps.tex by code/build.py\n'+text[:at])
 (root/'sections/maps_B.tex').write_text('% Generated from maps.tex by code/build.py\n'+text[at:])
base=root/'records/base_refs.bib'
if not base.exists():base.write_text((root/'S6_04_MAPS_MANIFOLDS_references.bib').read_text())
bibs=[base]+[p for p in sorted((root/'records').glob('*refs.bib')) if p!=base]
out='\n\n'.join(p.read_text() for p in bibs)
keys=re.findall(r'@\w+\s*\{\s*([^,]+)',out)
if len(keys)!=len(set(keys)):
 raise RuntimeError('Duplicate bibliography keys: '+str([k for k in set(keys) if keys.count(k)>1]))
(root/'S6_04_MAPS_MANIFOLDS_references.bib').write_text(out)
env=os.environ.copy()
dist='/usr/share/texlive/texmf-dist';extra='/usr/share/texmf'
local=str(runtime/'package/usr/share/texlive/texmf-dist')
env.update({
 'TEXINPUTS':f'.:{local}/tex//:{dist}/tex//:{extra}/tex//:',
 'LUAINPUTS':f'{local}//:{dist}//:',
 'TFMFONTS':f'{dist}/fonts/tfm//:{extra}/fonts/tfm//:',
 'VFFONTS':f'{dist}/fonts/vf//:{extra}/fonts/vf//:',
 'T1FONTS':f'{dist}/fonts/type1//:{extra}/fonts/type1//:',
 'TEXFONTMAPS':f'{runtime}/:{dist}/fonts/map//:{extra}/fonts/map//:',
 'ENCFONTS':f'{dist}/fonts/enc//:{extra}/fonts/enc//:',
 'OPENTYPEFONTS':f'{dist}/fonts/opentype//:{extra}/fonts/opentype//:',
 'TTFONTS':f'{dist}/fonts/truetype//:{extra}/fonts/truetype//:/usr/share/fonts//:',
 'TEXMFCACHE':str(runtime/'cache'),
 'TEXMFVAR':str(runtime/'cache'),
 'BSTINPUTS':f'{dist}/bibtex/bst//:',
 'BIBINPUTS':'.:',
})
(runtime/'cache').mkdir(exist_ok=True)
# The stripped runtime has no updmap output. Standard component maps are
# combined locally; a full TeX installation does not need this step.
fontmaps=[Path(dist)/'fonts/map/dvips/amsfonts'/f for f in
          ['cm.map','cmextra.map','symbols.map','euler.map','latxfont.map']]
fontmaps += [Path(dist)/'fonts/map/dvips/rsfs/rsfs.map',
             Path(extra)/'fonts/map/dvips/lm/lm.map']
(runtime/'pdftex.map').write_text('\n'.join(p.read_text() for p in fontmaps))
stem='S6_04_MAPS_MANIFOLDS_paper'
cmd=['lualatex','-interaction=nonstopmode','-halt-on-error',
     '-fmt='+str(runtime/'lualatex.fmt'),stem+'.tex']
logs=[]
for i,command in enumerate([cmd,['bibtex',stem],cmd,cmd]):
 p=subprocess.run(command,cwd=root,env=env,text=True,capture_output=True)
 log=root/'records'/f'build_pass_{i+1}.log'
 log.write_text(p.stdout+p.stderr)
 logs.append({'pass':i+1,'returncode':p.returncode,'log':str(log.relative_to(root))})
 print(f'pass {i+1}: returncode={p.returncode}',flush=True)
 if p.returncode:
  print((p.stdout+p.stderr)[-4500:]);break
(root/'records/build_status.json').write_text(json.dumps(logs,indent=2))

if p.returncode:
 raise SystemExit(p.returncode)
