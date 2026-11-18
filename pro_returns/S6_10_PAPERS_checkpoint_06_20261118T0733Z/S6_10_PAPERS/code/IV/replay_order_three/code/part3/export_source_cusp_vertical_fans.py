#!/usr/bin/env python3
from pathlib import Path
import re,subprocess
R=Path(__file__).resolve().parents[2]
s=(R/'notes/part3_source_cusp_vertical_fans_working.md').read_text()
body='## VF.1.'+s.split('## VF.1.',1)[1]
st=r'''Retain the actual positive selected-cusp source loop, scalar, finite
cap, source periods and line maps of P3F.54/P3F.56. For every integer
\(n\), use the physical-delta-retaining periodic lattice-basis fan
\(T_n=T(e_1+ne_2,e_2)\). Its actual oriented return class is
\[
                  s(n)=1-3n(n-1)\pmod{28}.
\]
These fans, with the exact periodic relabellings proved below,
exhaust all allowed lattice-basis fans containing a physical vertical
edge. Their return classes have exact image
\[
                     \{1,7,9,11,15,21,23,25\}.
\]
The native right relative integers of the two nonfixed stars are
\(6n-6\) and \(-6n\), respectively. The proof retains both actual
adjacent-fan character and period arrows. It does not assign a full
fixed-star characteristic pair, a return on a fan with no physical
vertical edge, or a shorter source-loop endpoint.
'''
def cv(x):
 x=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',x)
 x=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),x)
 return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=x,text=True,capture_output=True,check=True).stdout
tex=r'\subsection{The source return on every physical-delta-retaining fan}'+'\n'+r'\begin{statement}{P3K.56}{Proved}'+'\n'+cv(st)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+cv(body)+r'\end{proof}'+'\n'
(R/'notes/part3_source_cusp_vertical_fans.tex').write_text(tex)
pre=(R/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k56_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_cusp_vertical_fans.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported K56; active input unchanged.')
