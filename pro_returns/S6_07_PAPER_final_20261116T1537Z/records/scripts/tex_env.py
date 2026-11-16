from pathlib import Path
import os

ROOT=Path(__file__).resolve().parents[3]
TEXROOT=ROOT/'work/texruntime'

def tex_environment():
    env=os.environ.copy()
    for name in ['var','config','cache','formats','fonts']:(TEXROOT/name).mkdir(parents=True,exist_ok=True)
    env['TEXMF']='{'+str(TEXROOT)+',/usr/share/texlive/texmf-dist,/usr/share/texmf}'
    env['TEXMFVAR']=str(TEXROOT/'var')
    env['TEXMFSYSVAR']=str(TEXROOT/'var')
    env['TEXMFCONFIG']=str(TEXROOT/'config')
    env['TEXMFSYSCONFIG']=str(TEXROOT/'config')
    # Restricted LuaTeX accepts a positive relative cache path; invoke TeX from
    # the same directory as this call. The cache is a build artifact only.
    (Path.cwd()/'tex-cache').mkdir(exist_ok=True)
    env['TEXMFCACHE']='./tex-cache'
    env['VARTEXFONTS']=str(TEXROOT/'fonts')
    env['TEXINPUTS']='.:'+str(TEXROOT/'tex')+'//:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//:'
    env['LUAINPUTS']='.:'+str(TEXROOT/'tex')+'//:'+str(TEXROOT/'scripts')+'//:/usr/share/texlive/texmf-dist/scripts//:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/scripts//:/usr/share/texmf/tex//:'
    env['TEXFORMATS']=str(TEXROOT/'formats')+'//:'
    env['TFMFONTS']='/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm//:'
    env['VFFONTS']='/usr/share/texlive/texmf-dist/fonts/vf//:/usr/share/texmf/fonts/vf//:'
    env['TEXFONTMAPS']=str(TEXROOT/'fonts/map')+'//:/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:'
    env['ENCFONTS']='/usr/share/texmf/fonts/enc//:/usr/share/texlive/texmf-dist/fonts/enc//:'
    env['T1FONTS']='/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1//:'
    env['OPENTYPEFONTS']='/usr/share/texlive/texmf-dist/fonts/opentype//:/usr/share/texmf/fonts/opentype//:'
    return env
