#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess

root=Path(__file__).resolve().parents[2]
s=(root/'notes/part3_source_cusp_ordinary_product_working.md').read_text()
body='## OP.1.'+s.split('## OP.1.',1)[1]
statement=r'''
The actual selected-cusp family of P3F.54/P3F.56 admits a periodic
orientation-preserving ordinary smooth product of its labelled
three-curve plumbing, based at its initial fibre and retaining its
two labelled vertices and complex curve orientations.
In the explicitly constructed product, after the actual based
unit-logarithm contraction, the physical circle on the fixed-curve
normal coordinate has axis
\[
 \nu(s,\theta)=H(s,\theta)iH(s,\theta)^{-1},\qquad
 \deg\nu=+3,
\]
where the domain is the cylinder with each end circle collapsed,
oriented by \(ds\wedge d\theta\), and the target sphere has its
outward orientation. The closed fixed-curve normal-frame comparison has
factor degrees \(6,0\) in complex-curve-times-parameter orientation,
and \((-6,0)\) in the Hopf-sphere orientation of P3K.23.
The full-unit circle action is displayed in
the proof. This product is not delta-equivariant. No circle-trace
correction, common-exterior variation matrix, nonfixed relative
integer or additional fan return is assigned here.
'''
def convert(text):
    text=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',text)
    text=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),text)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=text,text=True,capture_output=True,check=True).stdout
tex=(r'\subsection{The ordinary cusp product and its physical-circle axis}'+'\n'
     +r'\begin{statement}{P3K.48}{Proved}'+'\n'+convert(statement)
     +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+convert(body)+r'\end{proof}'+'\n')
(root/'notes/part3_source_cusp_ordinary_product.tex').write_text(tex)
pre=(root/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k48_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'
      +r'\input{notes/part3_source_cusp_ordinary_product.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported P3K.48 and standalone wrapper; active input unchanged.')
