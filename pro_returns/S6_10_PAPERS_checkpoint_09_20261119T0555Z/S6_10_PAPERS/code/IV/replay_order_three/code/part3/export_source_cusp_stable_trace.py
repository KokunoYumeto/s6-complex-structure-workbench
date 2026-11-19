#!/usr/bin/env python3
from pathlib import Path
import re,subprocess
R=Path(__file__).resolve().parents[2]
s=(R/'notes/part3_source_cusp_stable_trace_working.md').read_text();body='## ST.1.'+s.split('## ST.1.',1)[1]
body+='\nThe exact certificate is code/part3/source_cusp_stable_trace.py, with its JSON and captured output.\n'
statement=r'''
In the actual ordinary plumbing product of P3K.48, use the ambient
stable frame and integral relative dual cycles of P3K.51. The
positive selected-cusp source return has stable-derivative vector
\[
 \delta=(-12,-12,0)^T.
\]
Its three ordinary single-curve relative pairs are
\[
 (m_0,n_0)=(6,-6),\qquad(m_1,n_1)=(6,-6),\qquad
 (m_2,n_2)=(0,0).
\]
Their central coordinate is one. The actual native nonfixed products
have pairs \((0,-6)\) at \(C_1\) and \((-6,0)\) at \(C_2\).
These are computed from the literal derivative action and its
closed Spin lifts; no subsequent fan-product reset or general fan
return is asserted here.
'''
def conv(s):
 s=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',s)
 s=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),s)
 return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=s,text=True,capture_output=True,check=True).stdout
tex=r'\subsection{The source-cusp stable derivative from the actual circle trace}'+'\n'+r'\begin{statement}{P3K.52}{Proved}'+'\n'+conv(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+conv(body)+r'\end{proof}'+'\n'
(R/'notes/part3_source_cusp_stable_trace.tex').write_text(tex)
pre=(R/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k52_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_cusp_stable_trace.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported P3K.52; active input unchanged.')
