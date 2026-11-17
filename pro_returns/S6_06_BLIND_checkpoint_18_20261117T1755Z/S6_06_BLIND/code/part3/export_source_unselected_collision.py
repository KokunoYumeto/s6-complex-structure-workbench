#!/usr/bin/env python3
"""Export audited K53; the global rho relation remains a separate task."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,shutil,subprocess

root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_source_unselected_collision_working.md'
text=source.read_text()
assert 'Proved after root and independent fourfold audits' in text
cert=json.loads((root/'code/part3/source_unselected_collision.json').read_text())
assert cert['status']=='PASS'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
shutil.copy2(source,root/'records'/f'pre_export_{stamp}_{source.name}')
body=text[text.index('## UI.1.'):text.index('## Audit record')]
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout
statement=r"""
Use the marked source
\[
 Y^2=X^3+(1-2v)X^2+TX+v^2,\qquad G=(0,v),
 \qquad T_0(v)=v^2-2v.
\]
Retain one III-star cap, the selected whole-zero \(I_1\) cusp,
its chosen periodic fan, and all source, Cartier line, finite
character and annular data of P3K.49. The cap is the good
\(m=4p\) branch for \((a,b)=(1,2)\), or the reduced
\(m=4p-1\) branch for \((a,b)=(2,1)\), with the signed norm
\(n=\pm1\). There is no added logarithmic disc on the two
unselected fibres that collide at \(v_*=1/8\).

The canonical continuation with the literal scalar
\(\lambda(v)=v^N\lambda_0\), \(N=km\), extends to an actual
smooth proper holomorphic family over a disc around \(v_*\).
The root, line and annular maps are the continuation of their
full reference data; no additional cap-data loop is inserted.
The scalar is in the common contracting range, with its
actual radial comparison retained. Consequently the positive
local return has oriented class zero in \(\Theta_7\), and
its mapping torus is oriented-diffeomorphic to \(S^1\times S^6\).
An averaged connection gives the corresponding smooth
trivialization carrying the physical circle.

This result supplies the unselected-collision disc in the
global marked-source problem. It assigns neither a
source-zero return nor an infinity endpoint.
"""
out=r'\subsection{The actual unselected-collision disc and its zero return}'+'\n'+r'\begin{statement}{P3K.53}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n'
(root/'notes/part3_source_unselected_collision.tex').write_text(out)
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/part3_source_unselected_collision_compile.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_unselected_collision.tex}'+'\n'+r'\end{document}'+'\n')
print(f'Exported P3K.53; {cert["checks"]} exact identities PASS.')
