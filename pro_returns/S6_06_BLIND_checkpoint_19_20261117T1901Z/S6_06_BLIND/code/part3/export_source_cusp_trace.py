#!/usr/bin/env python3
"""Export the audited selected-cusp source return, P3F.56, separately."""
from pathlib import Path
from datetime import datetime, timezone
import re
import shutil
import subprocess

root = Path(__file__).resolve().parents[2]
source = root / 'notes/part3_source_cusp_trace_working.md'
text = source.read_text()
assert 'Proved as P3F.56' in text
assert 'P3F.55 Kummer normalization comparison' in text
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
shutil.copy2(source, root / 'records' / f'pre_export_{stamp}_{source.name}')
body = text[text.index('## SC.1.'):text.index('## Audit and preservation record')]
body = re.sub(r'(?m)^## (.+)$',
              lambda m: r'\par\medskip\noindent\textbf{' + m.group(1)
              + r'}\par\nobreak', body)
body = re.sub(r'`(code/[^`]+)`', lambda m: r'\path{' + m.group(1) + '}', body)
tex = subprocess.run(
    ['pandoc', '-f', 'markdown+tex_math_single_backslash+raw_tex',
     '-t', 'latex', '--wrap=preserve'],
    input=body, text=True, capture_output=True, check=True).stdout

statement = r"""
Use the exact marked E7 source of P3F.54,
\[
 y^2=x^3+3r(u)x^2+t x+1,\qquad G=(0,1),\qquad
 r(u)=\frac{1-2u^3}{3u^2},\quad t_0(u)=u^2-\frac2u.
\]
Fix either actual one-cap sphere datum of P3F.41:
\[
 \begin{array}{c|c|c}
 (M,Q)&\text{order at }III^*&\text{root fibre}\\ \hline
 (\mathcal O(2G-O),G)&m=4l+3,\ l\ge0&III\\
 (\mathcal O(G-O),2G)&m=4l,\ l\ge1&\text{smooth}.
 \end{array}
\]
Keep its norm numerator \(n=\pm1\), its line lift and finite character,
and its sufficiently small nonzero scalar fixed. There is no additional
logarithmic disc on either member of the coalescing finite-node pair.
Use the standard vertical-edge toric fan of this construction.

Let \(u_*^3=-1\), and take the actual closed twofold source family
\[
 u+u^{-2}=\rho^2,\qquad u(0)=u_*.
\]
For one positive \(\rho\)-loop its forward physical return \(\Phi\)
has
\[
 A_{M,\rm Jin}(f)=-1,\qquad [\Phi]=-1\in\Theta_7\cong\mathbb Z/28.
\]
Here \(f\) is the quotient of that physical return with the orientations
and physical-line Hopf transfer of P3F.22 as explicitly identified in P3K.68. This is two positive turns about \(u_*\)
in the marked source parameter; the scalar has zero winding.
The actual sphere mapping torus is
\((S^1\times S^6)\mathbin{\#}\Sigma_{-1}\). Both its spin structures
have Eells--Kuiper invariant \(-1/28\), so it is not diffeomorphic to
\(S^1\times S^6\), including without an orientation requirement.

This particular full \(\rho\)-family has no descent as an oriented
smooth sphere bundle through the actual degree-two cover
\(p:D_\rho^*\to D_a^*\), \(a=\rho^2\), with \(u\) the analytic
inverse of \(a(u)=u+u^{-2}\) near \(u_*\). Indeed its clutch class
minus one cannot be twice a class in \(\Theta_7\).

The selected-node separation has braid \(\sigma^{12}\), and its
retained elliptic boundary map is the once-punctured-torus relation
\((gh)^6=T_{\partial}\). The proof below gives the actual ambient,
line, normal and cap morphisms carrying the local lifted link to this
return. It assigns no return to another fan or another source puncture.
"""
out = ('\\subsection{The actual selected-cusp double source return}\n'
       '\\begin{statement}{P3F.56}{Proved}\n' + statement
       + '\n\\end{statement}\n\\begin{proof}\n' + tex
       + '\n\\end{proof}\n')
(root / 'notes/part3_source_cusp_trace.tex').write_text(out)
preamble = (root / 'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root / 'records/part3_source_cusp_trace_compile.tex').write_text(
    preamble + '\n' + r'\begin{document}' + '\n'
    + r'\input{notes/part3_source_cusp_trace.tex}' + '\n'
    + r'\end{document}' + '\n')
print('Exported P3F.56 with the literal source/cap/line/fan scope and the F55 normalization bridge.')
