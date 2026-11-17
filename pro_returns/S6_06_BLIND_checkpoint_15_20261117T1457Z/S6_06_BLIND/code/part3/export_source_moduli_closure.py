#!/usr/bin/env python3
"""Export only the completed F54 marked source-loop closure theorem."""
from pathlib import Path
from datetime import datetime,timezone
import re,shutil,subprocess
root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_source_moduli_loops_working.md'
text=source.read_text()
assert "Root's independent full SM.5 audit PASS" in text
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
shutil.copy2(source,root/'records'/f'pre_export_{stamp}_{source.name}')
body=(text[text.index('## SM.1.'):text.index('## SM.4.')]+
      text[text.index('## SM.5.'):text.index('## SM.6.')])
body=re.sub(r'(?m)^## (.+)$',
 lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
 '-t','latex','--wrap=preserve'],input=body,text=True,capture_output=True,check=True).stdout
statement=r"""
For the marked E7 source
\[
 y^2=x^3+3r x^2+t x+1,\qquad G=(0,1),
\]
the source together with its selected finite nodal zero has the exact
parameter
\[
 U=\mathbb C^*\setminus\{u:u^3=-1\},\qquad
 r=\frac{1-2u^3}{3u^2},\quad t_0=u^2-\frac2u .
\]
Fix an actual E7 sphere datum of P3F.41 whose only logarithmic cap
is at \(III^*\), a sufficiently small nonzero scalar, and a marked
index-one unimodular periodic fan. In particular no additional
logarithmic disc meets either member of the coalescing finite-node pair.
Over every sufficiently small disc in \(U\) the full construction
extends as a proper holomorphic submersion. The return on its boundary
is therefore isotopic to the identity, including a collision of two
unselected nodes to a type II fibre.

At a selected-cusp puncture \(u_*^3=-1\), one positive source loop has
the exact Tate and source-Cartier transition
\[
 (Z,V,q_T)\longmapsto(q_T/Z,V,q_T),\qquad
 (v_Z,v_V,h)\longmapsto(-v_Z+h,v_V,h).
\]
Its reflection on edge directions preserves no index-one unimodular
three-edge periodic fan. Thus this specified marked source, line and
annular transport does not close the chosen completion after one turn.
Its twofold cover \(a(u)=u+u^{-2}=\rho^2\) has literally closed source,
line, toric and finite-cap charts and gives the marked holomorphic
family there. This statement assigns no mapping-class return to the
closed \(\rho\)-loop.
"""
out=('\\subsection{Marked source loops at a selected E7 cusp}\n'
     '\\begin{statement}{P3F.54}{Proved}\n'+statement+
     '\n\\end{statement}\n\\begin{proof}\n'+tex+
     '\nThe exact algebraic certificate is '
     '\\path{code/part3/source_moduli_nodes.py} with its saved outputs.'
     '\n\\end{proof}\n')
(root/'notes/part3_source_moduli_closure.tex').write_text(out)
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/part3_source_moduli_closure_compile.tex').write_text(
 preamble+'\n'+r'\begin{document}'+'\n'+
 r'\input{notes/part3_source_moduli_closure.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported completed F54 only; SM4/SM6 and the uncomputed return remain outside the manuscript include.')
