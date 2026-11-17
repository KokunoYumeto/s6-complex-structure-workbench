#!/usr/bin/env python3
"""Export the audited arbitrary-source proof as a separate F51 include."""
from pathlib import Path
from datetime import datetime, timezone
import re
import shutil
import subprocess

root = Path(__file__).resolve().parents[2]
source = root/'notes/part3_generic_source_models.md'
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
text = source.read_text()
if 'Root independently passed' not in text:
    raise SystemExit('Root full-text audit has not yet been recorded; export stopped.')
shutil.copy2(source, root/'records'/f'pre_export_{stamp}_{source.name}')
body = text[text.index('## S1.'):text.index('## Certificate and audit state')]
body = re.sub(r'(?m)^## (.+)$',
              lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',
              body)
body = re.sub(r'(?<![A-Za-z])(?:code|notes|records)/[A-Za-z0-9_./-]+',
              lambda m:r'\path{'+m.group(0).rstrip('.')+'}'+
                       ('.' if m.group(0).endswith('.') else ''), body)
tex = subprocess.run(
    ['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
     '-t','latex','--wrap=preserve'],
    input=body,text=True,capture_output=True,check=True).stdout
statement = r"""
Every fixed marked rational elliptic source with Mordell--Weil group
\(\mathbb Z\) in the surviving source profiles is covered by the
source, line, cap, integral topology and actual scalar-return
comparisons of P3F.36--49 and P3K.26--30. In the two starred
Mordell--Weil entries, the full marked forms are
\[
\begin{aligned}
 E_7:\quad &y^2=x^3+3r x^2+t x+1,\qquad G=(0,1),\\
 E_6+A_1:\quad &y^2=x^3+3r x^2+A t x+t^2,\qquad G=(0,t).
\end{aligned}
\]
The explicit coordinate, finite-root, resolved-quotient and
Cartier-line maps below retain all allowed coefficients.
The ordinary III, IV, II and \(I_1^*\) cap proofs already retain
the full analytic coefficients, and their integral source-pair
maps are the actual maps on each source's marked divisor basis.
Thus the stated sphere criteria, page-line squares and signed
scalar-return integers hold for every such fixed source, with
the specified parameter \(\lambda=r_{\rm par}^{\,M}\).
No transport around a loop varying the source in its moduli
space is inferred from this fixed-source assertion.
"""
out = ('\\subsection{Arbitrary marked sources in the additive sectors}\n'
       '\\begin{statement}{P3F.51}{Proved}\n'+statement+
       '\n\\end{statement}\n\\begin{proof}\n'+tex+
       '\nThe executed exact certificate is '
       '\\path{code/part3/generic_source_models.py}; its JSON and text '
       'outputs record all 43 identities.\n\\end{proof}\n')
(root/'notes/part3_generic_source_models.tex').write_text(out)
preamble = (root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/part3_generic_source_models_compile.tex').write_text(
    preamble+'\n'+r'\begin{document}'+'\n'+
    r'\input{notes/part3_generic_source_models.tex}'+'\n'+
    r'\end{document}'+'\n')
print('Exported separate F51 include and standalone wrapper; master untouched.')
