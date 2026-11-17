"""Export the independently audited inverse-action proof without editing master."""
from pathlib import Path
import re, subprocess

root=Path(__file__).resolve().parents[2]
p=root/'notes/part3_expanding_action_comparison.md'
body=p.read_text().split('The source data',1)[1]
body='The source data'+body
body=body.split('The proof accounts for both uniform-action alternatives')[0]
body=re.sub(r'(?m)^## (.+)$',
 lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',
 body)
tex=subprocess.run(
 ['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
  '-t','latex','--wrap=preserve'],input=body,text=True,
 capture_output=True,check=True).stdout
statement=r"""
Every sphere family obtained from a rational elliptic source with
Mordell--Weil group \(\mathbb Z\) in the uniformly expanding case
of E26 Remark~8.5 has the following exact inverse-action comparison.
The parameter map \(\mu=\lambda^{-1}\), the identity on the original
line complement, the unchanged root-cap groups and the identity on
the same physical Mumford charts give a biholomorphic contracting
family. Its cap norms and base framing are
\(n_i^\vee=-n_i\) and \(b_0^\vee=-b_0\).
For a counterclockwise large-\(\lambda\) scalar circle, its return is
the inverse of the positive small-\(\mu\) return:
\[
 [\Phi_{\lambda,+}]=-[\Phi_{\mu,+}]\quad\hbox{in }\Theta_7.
\]
On the K23 reference products the transported individual characteristic
pair and relative integers are negated as well.
The physical fan and line circle are retained.
The same statement holds on each specified root-parameter cover;
no additional shorter-loop descent is asserted.
"""
target=root/'notes/part3_expanding_action_comparison.tex'
target.write_text(
 r'\subsection{The exact comparison for uniformly expanding actions}'+'\n'
 +r'\begin{statement}{P3F.50}{Proved}'+'\n'+statement
 +r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex
 +r'\end{proof}'+'\n')
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/f50_standalone.tex').write_text(
 preamble+'\n'+r'\begin{document}'+'\n'
 +r'\input{notes/part3_expanding_action_comparison.tex}'+'\n'
 +r'\end{document}'+'\n')
print('Exported P3F.50 and standalone wrapper; master unchanged.')
