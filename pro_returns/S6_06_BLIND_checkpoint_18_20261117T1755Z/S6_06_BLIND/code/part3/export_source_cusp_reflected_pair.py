#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[2]
s = (root/'notes/part3_source_cusp_reflected_pair_working.md').read_text()
body = '## RC.1.' + s.split('## RC.1.', 1)[1]
statement = r'''
Retain the actual selected-cusp positive \(\rho\)-loop of
P3F.54/P3F.56 and P3K.45: the scalar is fixed, the III-star cap
is unchanged, and the coalescing finite pair has no logarithmic
modification. Let \(T'=J(T)\) be the reflected initial fan, obtained
by flopping its nonfixed diagonal edge \(C_2\). Its actual Jin
characteristic pair and relative coordinates at its retained fixed
edge \(C_0\), in the specified Cox product, are
\[
 (k,\ell)=(6,0),\qquad
 (m_{C_0},n_{C_0},s)=(0,-6,1).
\]
The physical positive-parameter completion has pair \((-6,0)\).
The actual cap map below transports its meridian line, and the common
parameter reversal gives the displayed Jin pair. This statement
does not assign the separate relative integers at \(C_2\) or an
arbitrary-fan return formula.
'''


def convert(text):
    text = re.sub(r'(?m)^## (.+)$', lambda m: r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak', text)
    text = re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',
                  lambda m: r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''), text)
    return subprocess.run(['pandoc', '-f', 'markdown+tex_math_single_backslash+raw_tex',
                           '-t', 'latex', '--wrap=preserve'], input=text, text=True,
                          capture_output=True, check=True).stdout


tex = (r'\subsection{The actual characteristic pair on the reflected cusp fan}'+'\n'
       +r'\begin{statement}{P3K.46}{Proved}'+'\n'+convert(statement)
       +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+convert(body)
       +r'\end{proof}'+'\n')
(root/'notes/part3_source_cusp_reflected_pair.tex').write_text(tex)
pre = (root/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k46_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'
       +r'\input{notes/part3_source_cusp_reflected_pair.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported P3K.46 and standalone wrapper; active input unchanged.')
