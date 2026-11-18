#!/usr/bin/env python3
"""Export only the actual P3K.30 proof and standalone wrapper."""
from pathlib import Path
from datetime import datetime,timezone
import re,subprocess,shutil
root=Path(__file__).resolve().parents[2]
p=root/'notes/part3_general_cap_framing.md'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
shutil.copy2(p,root/'records'/f'pre_export_{stamp}_{p.name}')
text=p.read_text()
proof=text[text.index('## '):]
proof=re.sub(r'(?m)^## (.+)$',
 lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',proof)
proof=re.sub(r'(?<![A-Za-z])(?:code|notes|records)/[A-Za-z0-9_./-]+',
 lambda m:r'\path{'+m.group(0).rstrip('.')+'}'+('.' if m.group(0).endswith('.') else ''),proof)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],
 input=proof,text=True,capture_output=True,check=True).stdout
statement=r"""
For every actual page of P3K.26 and P3K.28, let \(M\) be its page-cover degree,
\(h(G)=1/d\), and \(aG\) its marked line point. Write
\(H=Ma^2/d\) and \(\chi=\chi(\mathcal O_{S_{\rm page}})\).
Use the actual vertical-edge Cox normal product transported by the
extending signed cusp origin. For one positive loop in the actual
parameter \(r\), with \(\lambda=r^M\), the individual Jin pair and
the K23 relative coordinates are
\[
 \begin{aligned}
 k&=-3H,&\ell&=-24\chi,\\
 m_{\rm rel}&=6\chi,&n_{\rm rel}&=3H-6\chi,\\
 s&=\chi-H/2\pmod{28}.
 \end{aligned}
\]
This holds for both one-cap norms \(n=\pm1\) and both joint determinants
\(D=\pm1\). The comparison fixes the actual initial Cox quaternion
frame; a possible extending constant rotation loop changes neither
integer. No different fan edge's relative four-cycle is assigned here.
"""
out=r'\subsection{The rotating and Cox pair for the additive pages}'+'\n'+r'\begin{statement}{P3K.30}{Proved}'+'\n'+statement+'\n'+r'\end{statement}'+'\n'+r'\begin{proof}'+'\n'+tex+'\n'+r'\end{proof}'+'\n'
(root/'notes/part3_general_cap_framing.tex').write_text(out)
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/part3_general_cap_framing_compile.tex').write_text(preamble+'\n'+r'\begin{document}'+'\n'+r'\input{notes/part3_general_cap_framing.tex}'+'\n'+r'\end{document}'+'\n')
print('Exported separate K30 include and wrapper; master untouched.')

