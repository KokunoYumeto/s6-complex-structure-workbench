#!/usr/bin/env python3
from pathlib import Path
import re,subprocess
ROOT=Path(__file__).resolve().parents[2]
items=[('50','ordinary_relative','The fixed-curve return in the ordinary plumbing product','OR.1.',r'''
In the actual ordinary plumbing product of P3K.48, the positive
selected-cusp source return restricted to the exterior of the
original fixed curve has relative coordinates
\[
 (m_0,n_0,s)=(6,-6,1),\qquad V_{00}=0,\qquad\delta_0=-12.
\]
The derivative is \(+12\) on the product cycle \([D^3_h]\) and
\(-12\) on its ambient relative dual \(D_0=-[D^3_h]\).
The native-to-ordinary product change at each of the two nonfixed
stars likewise adds the explicit pure-left relative class \(L^6\)
and leaves its right integer unchanged. This statement computes
those comparison maps; it assigns no native nonfixed integer or
further fan return.
'''),('51','circle_trace','The full source-cusp variation from actual circle traces','CT.1.',r'''
Retain the actual ordinary plumbing product of P3K.48 and the
positive selected-cusp source loop. In the positive complex normal
meridians \((m_0,m_1,m_2)\) and their integral relative dual cycles
\((D_0,D_1,D_2)\), its common-exterior variation is exactly
\[
 V=\begin{pmatrix}0&6&-6\\6&0&0\\-6&0&0\end{pmatrix}.
\]
The matrix is computed by the actual orbit-trace maps, generic
normal sections, vertex-link paths and signed relative chain
homotopy. No nonfixed stable derivative or further fan return is
assigned by this statement.
''')]
def conv(s):
 s=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',s)
 s=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),s)
 return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=s,text=True,capture_output=True,check=True).stdout
pre=(ROOT/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
for num,name,title,head,statement in items:
 p=ROOT/f'notes/part3_source_cusp_{name}_working.md';s=p.read_text();body='## '+head+s.split('## '+head,1)[1]
 body+='\nThe exact certificate is code/part3/source_cusp_'+name+'.py, with its JSON and captured output.\n'
 tex=r'\subsection{'+title+'}\n'+r'\begin{statement}{P3K.'+num+'}{Proved}\n'+conv(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+conv(body)+r'\end{proof}'+'\n'
 (ROOT/f'notes/part3_source_cusp_{name}.tex').write_text(tex)
 (ROOT/f'code/part3/k{num}_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_cusp_'+name+'.tex}\n'+r'\end{document}'+'\n')
 print('Exported P3K.'+num+'; active input unchanged.')
