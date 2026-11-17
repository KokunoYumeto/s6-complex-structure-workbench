#!/usr/bin/env python3
from pathlib import Path
import re,subprocess
R=Path(__file__).resolve().parents[2];s=(R/'notes/part3_source_cusp_first_flops_working.md').read_text();body='## FF.1.'+s.split('## FF.1.',1)[1]
body+='\nThe exact certificate is code/part3/source_cusp_first_flops.py, with its JSON and captured output.\n'
st=r'''Retain exactly the positive selected-cusp source loop, scalar, finite cap,
source periods and line maps of P3F.54/P3F.56. In its initial fan,
the actual first periodic flops at the fixed vertical curve \(C_0\),
the horizontal curve \(C_1\), and the diagonal curve \(C_2\) have
oriented return classes
\[
 23,\qquad23,\qquad1\quad\text{in }\mathbb Z/28,
\]
respectively. The proof retains each native family product and its
actual exterior boundary arrow. No subsequent ordinary-product
reset or general fan formula is assigned by this statement.
'''
def cv(x):
 x=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',x)
 x=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),x)
 return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=x,text=True,capture_output=True,check=True).stdout
tex=r'\subsection{The three actual first-flop source-loop classes}'+'\n'+r'\begin{statement}{P3K.54}{Proved}'+'\n'+cv(st)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+cv(body)+r'\end{proof}'+'\n'
(R/'notes/part3_source_cusp_first_flops.tex').write_text(tex)
pre=(R/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k54_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_cusp_first_flops.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported K54; active input unchanged.')
