from pathlib import Path
import os,subprocess
root=Path(__file__).resolve().parents[1];runtime=root.parent/'tex_runtime'
dist='/usr/share/texlive/texmf-dist';extra='/usr/share/texmf';local=str(runtime/'package/usr/share/texlive/texmf-dist')
env=os.environ.copy();env.update({'TEXINPUTS':f'.:{local}/tex//:{dist}/tex//:{extra}/tex//:',
'LUAINPUTS':f'{local}//:{dist}//:','TFMFONTS':f'{dist}/fonts/tfm//:{extra}/fonts/tfm//:',
'VFFONTS':f'{dist}/fonts/vf//:{extra}/fonts/vf//:','T1FONTS':f'{dist}/fonts/type1//:{extra}/fonts/type1//:',
'TEXFONTMAPS':f'{runtime}/:{dist}/fonts/map//:{extra}/fonts/map//:',
'ENCFONTS':f'{dist}/fonts/enc//:{extra}/fonts/enc//:',
'OPENTYPEFONTS':f'{dist}/fonts/opentype//:{extra}/fonts/opentype//:',
'TTFONTS':f'{dist}/fonts/truetype//:{extra}/fonts/truetype//:/usr/share/fonts//:',
'TEXMFCACHE':str(runtime/'cache'),'TEXMFVAR':str(runtime/'cache'),
'BSTINPUTS':f'{dist}/bibtex/bst//:','BIBINPUTS':'.:'})
cmd=['lualatex','-interaction=nonstopmode','-halt-on-error','-fmt='+str(runtime/'lualatex.fmt'),'-output-directory=code','code/manifolds_check.tex']
for i,c in enumerate([cmd,['bibtex','code/manifolds_check'],cmd,cmd],1):
 p=subprocess.run(c,cwd=root,env=env,text=True,capture_output=True)
 (root/f'code/manifolds_check_run{i}.out').write_text(p.stdout+p.stderr)
 print(i,p.returncode)
 if p.returncode:print((p.stdout+p.stderr)[-3000:]);break
