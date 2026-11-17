"""Export the fully audited invariant-divisor and actual-root-line comparison."""
from pathlib import Path
import re
import subprocess

root=Path(__file__).resolve().parents[2]
body=(root/'notes/part3_vertical_line_exhaustion.md').read_text()
body=body.split('The source',1)[1]
body='The source'+body
body=re.sub(r'(?m)^## (.+)$',
    lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
    '-t','latex','--wrap=preserve'],input=body,text=True,
    capture_output=True,check=True).stdout
statement=r"""
Fix one of the whole-fibre sphere source tuples of K20--21 and
F36--51, its marked translating point \(Q=bG\), its generic line
point \(aG\), a selected simple \(I_1\) zero, and its effective
cap data. Every source line satisfying the literal Hom condition
is related to the displayed representative by the actual
meromorphic line map \(\mathcal M=\mathcal M_0\otimes\mathcal O(D)\),
where \(t_Q^*D=D\) as divisors.
Its canonical section, the actual root-line evaluation, and the
explicit cone-height map below identify the resulting family
with the constructed family carrying the retained base factors,
finite characters and integral collar windings.
For the canonical scalar loop, these maps preserve the individual
characteristic pair, the relative index and the all-fan formula
in the transported Cox product.
"""
(root/'notes/part3_vertical_line_exhaustion.tex').write_text(
    r'\subsection{Exhaustion of the vertical source-line choices}'+'\n'
    +r'\begin{statement}{P3F.52}{Proved}'+'\n'+statement
    +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex
    +r'\end{proof}'+'\n')
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/f52_standalone.tex').write_text(
    preamble+'\n'+r'\begin{document}'+'\n'
    +r'\input{notes/part3_vertical_line_exhaustion.tex}'+'\n'
    +r'\end{document}'+'\n')
print('Exported P3F.52 and standalone wrapper.')
