#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess

root=Path(__file__).resolve().parents[2]
source=(root/'notes/part3_source_cusp_characteristic_pair_working.md').read_text()
body='## SP.1.'+source.split('## SP.1.',1)[1]
proof_body,audit_body=body.split('## Audit and computation status',1)
statement=r'''
Retain the actual positive selected-cusp source loop of P3F.54 and
P3F.56, with fixed sufficiently small scalar, the III-star cap, no
logarithmic modification on the coalescing finite pair, and the
initial physical-delta-edge fan. Its parameter is one positive
\(\rho\)-loop, where \(a(u)=\rho^2\), with the literal double
source closure and the actual Cox normal product. In Jin's endpoint
and physical nonzero-vector-line conventions its characteristic pair and
first-resolution relative coordinates are
\[
       (k_M,\ell_M)=(-6,0),\qquad(k_U,\ell_U)=(6,0),\qquad
       (m_{\rm rel},n_{\rm rel},s)=(0,-6,-1).
\]
The framed local surgery has pair \((5,-4)\). The actual capped
normal sphere bundle in its source-family bordism has pair
\((1,4)\). Their oriented sum gives the meridian-one U pair; the actual physical line M is its Hermitian dual and gives the displayed negative pair.
This statement concerns only the specified initial fan. The complete physical line and Hopf-transfer correction is P3K.68.
'''

def convert(text):
    text=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',text)
    text=re.sub(r'(?<![\w{/])(code/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),text)
    return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=text,text=True,capture_output=True,check=True).stdout

tex=(r'\subsection{The actual characteristic pair of the selected-cusp source loop}'+'\n'
     +r'\begin{statement}{P3K.42}{Proved}'+'\n'+convert(statement)
     +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+convert(proof_body)
     +r'\end{proof}'+'\n'+convert('## Audit and computation status'+audit_body))
(root/'notes/part3_source_cusp_characteristic_pair.tex').write_text(tex)
preamble=(root/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(root/'code/part3/k42_standalone.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_cusp_characteristic_pair.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported full P3K.42 and standalone wrapper; master input remains unchanged pending visual QA.')
