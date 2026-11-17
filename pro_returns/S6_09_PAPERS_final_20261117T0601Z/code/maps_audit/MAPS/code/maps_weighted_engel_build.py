"""Compile only the weighted Engel invariant proof for local mathematical layout checking."""
from pathlib import Path
import os, subprocess

root=Path(__file__).resolve().parents[1]
runtime=root.parent/'tex_runtime'
target=runtime/'maps_weighted_engel_audit'
target.mkdir(exist_ok=True)
preamble=(root/'S6_04_MAPS_MANIFOLDS_paper.tex').read_text().split(r'\begin{document}')[0]
source=preamble+r'''\begin{document}
\input{code/maps_weighted_engel_invariants_proof.tex}
\begin{thebibliography}{9}
\bibitem{mapsKaplan79} S. J. Kaplan, Constructing framed 4-manifolds with given almost framed boundaries, Transactions of the American Mathematical Society 254 (1979), 237--263.
\bibitem{manZhubr75} A. V. Zhubr, Classification of simply connected six-dimensional spinor manifolds, Math. USSR Izvestija 9 (1975), 793--812.
\bibitem{ffThomas56} E. Thomas, A generalization of the Pontrjagin square cohomology operation, Proc. Nat. Acad. Sci. USA 42 (1956), 266--269.
\bibitem{mapsWhitehead50} J. H. C. Whitehead, The secondary boundary operator, Proc. Nat. Acad. Sci. USA 36 (1950), 55--60.
\end{thebibliography}
\end{document}
'''
(target/'maps_weighted_engel_audit.tex').write_text(source)
env=os.environ.copy()
dist='/usr/share/texlive/texmf-dist'; extra='/usr/share/texmf'
local=str(runtime/'package/usr/share/texlive/texmf-dist')
env.update({'TEXINPUTS':f'.:{local}/tex//:{dist}/tex//:{extra}/tex//:',
 'LUAINPUTS':f'{local}//:{dist}//:',
 'TFMFONTS':f'{dist}/fonts/tfm//:{extra}/fonts/tfm//:',
 'VFFONTS':f'{dist}/fonts/vf//:{extra}/fonts/vf//:',
 'T1FONTS':f'{dist}/fonts/type1//:{extra}/fonts/type1//:',
 'TEXFONTMAPS':f'{runtime}/:{dist}/fonts/map//:{extra}/fonts/map//:',
 'ENCFONTS':f'{dist}/fonts/enc//:{extra}/fonts/enc//:',
 'OPENTYPEFONTS':f'{dist}/fonts/opentype//:{extra}/fonts/opentype//:',
 'TTFONTS':f'{dist}/fonts/truetype//:{extra}/fonts/truetype//:/usr/share/fonts//:',
 'TEXMFCACHE':str(runtime/'cache'),'TEXMFVAR':str(runtime/'cache')})
cmd=['lualatex','-interaction=nonstopmode','-halt-on-error',
     '-fmt='+str(runtime/'lualatex.fmt'),'-output-directory='+str(target),
     str(target/'maps_weighted_engel_audit.tex')]
for i in range(2):
    process=subprocess.run(cmd,cwd=root,env=env,text=True,capture_output=True)
    (root/'records'/f'maps_weighted_engel_build_{i+1}.log').write_text(process.stdout+process.stderr)
    print('pass',i+1,'returncode',process.returncode)
    if process.returncode:
        print((process.stdout+process.stderr)[-4000:]);raise SystemExit(process.returncode)
print('PDF:',target/'maps_weighted_engel_audit.pdf')
