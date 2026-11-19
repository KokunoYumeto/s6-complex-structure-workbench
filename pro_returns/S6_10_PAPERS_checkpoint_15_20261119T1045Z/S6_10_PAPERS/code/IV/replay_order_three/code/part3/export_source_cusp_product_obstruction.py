#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[2]
s = (root/'notes/part3_source_cusp_product_obstruction_working.md').read_text()
body = '## PO.1.' + s.split('## PO.1.', 1)[1]
statement = r'''
Retain the actual selected-cusp positive \(\rho\)-loop of
P3F.54/P3F.56 and its initial fan. Its three-curve plumbing has no
periodic smooth product which intertwines the physical delta
action and carries all three labelled complex curves, their two
labelled vertices and their positive complex orientations to
constant copies. The obstruction is the actual relative normal
determinant winding
\[
 \operatorname{wind}\kappa+2\operatorname{wind}\alpha
                  -\operatorname{wind}\eta=-6.
\]
This concerns that simultaneous marked product. It does not obstruct
the separate single-star products or the actual reflected fixed-edge
cap map of P3K.46, and it does not assign a nonfixed relative integer
or an arbitrary-fan return formula.
'''


def convert(text):
    text = re.sub(r'(?m)^## (.+)$', lambda m: r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak', text)
    text = re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',
                  lambda m: r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''), text)
    return subprocess.run(['pandoc', '-f', 'markdown+tex_math_single_backslash+raw_tex',
                           '-t', 'latex', '--wrap=preserve'], input=text, text=True,
                          capture_output=True, check=True).stdout


tex = (r'\subsection{The determinant obstruction to a labelled equivariant cusp product}'+'\n'
       +r'\begin{statement}{P3K.47}{Proved}'+'\n'+convert(statement)
       +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+convert(body)
       +r'\end{proof}'+'\n')
(root/'notes/part3_source_cusp_product_obstruction.tex').write_text(tex)
pre = (root/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k47_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'
       +r'\input{notes/part3_source_cusp_product_obstruction.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported P3K.47 and standalone wrapper; active input unchanged.')
