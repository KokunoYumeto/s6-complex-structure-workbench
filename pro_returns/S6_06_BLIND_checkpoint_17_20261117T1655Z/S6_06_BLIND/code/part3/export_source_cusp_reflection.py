#!/usr/bin/env python3
from pathlib import Path
import re,subprocess
root=Path(__file__).resolve().parents[2]
s=(root/'notes/part3_source_cusp_reflection_working.md').read_text()
body='## RF.1.'+s.split('## RF.1.',1)[1]
statement=r'''
Retain the selected-cusp source family and positive \(\rho\)-loop
of P3F.54/P3F.56, with fixed scalar, the actual III-star cap, and no
logarithmic modification on the coalescing finite pair. For every
allowed cusp fan \(T\), put \(J=\operatorname{diag}(-1,1)\)
on its marked two-dimensional lattice. The actual returns for
\(T\) and \(J(T)\) are conjugate by an orientation-preserving
diffeomorphism, through the literal half-source family map.
For the initial fan of P3F.56, \(J(T)\) is its nonfixed
diagonal-edge flop, and its positive return has oriented class
\[
                 [\Sigma_{\Phi,J(T)}]=1\in\mathbb Z/28.
\]
This gives neither a once-u endpoint on one fixed fan nor the
individual characteristic pair or integer derivative of the
reflected fan. The different fixed-edge flop has class23 by
P3K.40.
'''
def conv(t):
    t=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',t)
    t=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),t)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=t,text=True,capture_output=True,check=True).stdout
tex=r'\subsection{Actual half-source transport and the reflected cusp fan}'+'\n'+r'\begin{statement}{P3K.45}{Proved}'+'\n'+conv(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+conv(body)+r'\end{proof}'+'\n'
(root/'notes/part3_source_cusp_reflection.tex').write_text(tex)
pre=(root/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k45_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_cusp_reflection.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported P3K.45 and standalone wrapper; active input unchanged.')
