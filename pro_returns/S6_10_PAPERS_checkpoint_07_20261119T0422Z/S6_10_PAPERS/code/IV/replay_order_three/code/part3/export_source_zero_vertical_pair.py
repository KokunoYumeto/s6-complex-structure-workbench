#!/usr/bin/env python3
"""Reconstructed full K89 export; every proof map is retained."""
from pathlib import Path
import re,subprocess
R=Path(__file__).resolve().parents[2]
src=(R/'notes/part3_source_zero_vertical_pair_working.md').read_text()
body='## VZ.1.'+src.split('## VZ.1.',1)[1]
statement=r'''Retain the full source-zero families, their actual finite-cap
characters and the physical vertical fans \(T_j\), \(j\in\mathbb Z\).
Set \((a,b)=(1,2),m=4p,\mu_0=1\) in the good branch and
\((a,b)=(2,1),m=4p-1,\mu_0=0\) in the reduced branch. Put
\[
 P_b(j)=2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}.
\]
The fixed-scalar source loop has physical Jin pair, native free
pair and integer index
\[
 (k_j,\ell_j)=(\mu_0+6P_b(j),4\mu_0),\qquad
 (\mu_j,\nu_j)=(\mu_0,6P_b(j)),\qquad A_j=P_b(j).
\]
For the actual coupled loop \(\lambda(v)=\lambda_0v^{cm}\), with
its realized norm sign, full Cartier and closing maps, the pair is
\[
\begin{aligned}
 k_j&=\mu_0+6P_b(j)+c[3H-3m j(j-1)],\\
 \ell_j&=4\mu_0+24cp,\qquad \mu_j=\mu_0+6cp,\\
 A_j&=P_b(j)+c\left((a-1)(3p-1)-m\binom j2\right),
\end{aligned}
\]
where \(H=2p\) in the good branch and \(H=8p-2\) in the reduced
branch. Its oriented sphere class is \(A_j\bmod28\).
With \(t=cm-1\), the actual doubled ordinary fixed entries are
\[
 V_{00}=2t-2\mu_j-12A_j,\qquad
 \delta_0=2t-2\mu_j+12A_j.
\]
The proof derives these integers by the complete relative source,
line, tangent, cap and parameter maps, before reducing the index.
'''
def cv(x):
 x=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',x)
 x=re.sub(r'(?<![A-Za-z0-9_\\])((?:code|records)/[A-Za-z0-9_./-]+)',lambda m:r'\path{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),x)
 return subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=x,text=True,capture_output=True,check=True).stdout
tex=(r'\subsection{The full integer pair on source-zero vertical fans}'+'\n'+r'\begin{statement}{P3K.89}{Proved}'+'\n'+cv(statement)+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+cv(body)+r'\end{proof}'+'\n')
for bad in [r'\textsuperscript',r'\textsubscript',r'\textbackslash']:
 assert bad not in tex,bad
assert not any(ord(c)<32 and c not in '\n\t\r' for c in tex)
(R/'notes/part3_source_zero_vertical_pair.tex').write_text(tex)
pre=(R/'code/part3/k38_standalone.tex').read_text().split(r'\begin{document}')[0]
(R/'code/part3/k89_standalone.tex').write_text(pre+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_source_zero_vertical_pair.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported reconstructed complete K89; master untouched.')
