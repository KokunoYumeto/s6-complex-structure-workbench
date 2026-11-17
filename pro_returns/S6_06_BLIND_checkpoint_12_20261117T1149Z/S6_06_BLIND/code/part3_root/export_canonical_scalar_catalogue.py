"""Export the fully mapped fixed-source scalar classification and its catalogue."""
from pathlib import Path
import re
import subprocess

root=Path(__file__).resolve().parents[2]
body=(root/'notes/part3_canonical_scalar_catalogue.md').read_text()
body=body.split('## C1.',1)[1]
body='## C1.'+body
body=re.sub(r'(?m)^## (.+)$',
    lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
    '-t','latex','--wrap=preserve'],input=body,text=True,
    capture_output=True,check=True).stdout
statement=r"""
The fixed-source canonical scalar sphere families in the literal
whole-fibre construction of E26 Remark~8.5, with rational elliptic
source and Mordell--Weil group \(\mathbb Z\), are exactly the
sixteen profiles and twenty-six source pairs in the two tables below.
Their root table has thirty-one branches; the good/good
\(III^*+II\) branch has no sphere solution, and the other thirty
have precisely the displayed coprimality and determinant conditions.
All fixed source coefficients, allowed vertical source lines,
primitive effective cap actions and order-one clutches are included
through the comparison maps in the proof.

For the actual canonical scalar parameter \(\lambda=r^M\), put
\[
 M=m_\infty m_0,\qquad H=Ma^2/d,\qquad
 \chi=\frac{M(12-e_\infty-e_0)+m_0e'_\infty+m_\infty e'_0}{12}.
\]
The specified complex page, source section and relative line have
height \(H\), relative square \(-H\), and tangent number
\(-24\chi\). Both determinant signs give the reference characteristic
pair \((-3H,-24\chi)\) and return index \(A=\chi-H/2\).
On the actual fan \(T(v_1,v_2)\), with
\(\delta=pv_1+qv_2\) and \(S=p^2-pq+q^2\), the class is
\[
 [\Sigma_{\Phi,T}]
       =\chi(4-3S)+H(3S^2-7)/8\quad\hbox{in }\mathbb Z/28.
\]
The actual shorter original loop, component-supported OS49 loop,
and general weighted shorter scalar loop are accounted for through
K33--35 and their explicit endpoint maps.
"""
(root/'notes/part3_canonical_scalar_catalogue.tex').write_text(
    r'\subsection{The complete fixed-source canonical scalar catalogue}'+'\n'
    +r'\begin{statement}{P3F.53}{Proved}'+'\n'+statement
    +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex
    +r'\end{proof}'+'\n')
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/f53_standalone.tex').write_text(
    preamble+'\n'+r'\begin{document}'+'\n'
    +r'\input{notes/part3_canonical_scalar_catalogue.tex}'+'\n'
    +r'\end{document}'+'\n')
print('Exported P3F.53 and standalone wrapper.')
