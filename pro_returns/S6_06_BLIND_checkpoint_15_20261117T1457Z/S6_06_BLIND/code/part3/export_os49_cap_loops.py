#!/usr/bin/env python3
"""Export audited P3K.44, retaining the actual component-supported cusp."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,shutil,subprocess

root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_os49_cap_loops_working.md'
text=source.read_text()
assert 'Proved as P3K.44' in text
certificate=json.loads((root/'code/part3/os49_cap_loops.json').read_text())
assert certificate['status']=='PASS'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
shutil.copy2(source,root/'records'/f'pre_export_{stamp}_{source.name}')
body=text[text.index('## OC.1.'):text.index('## Audit and certificate status')]
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
body=re.sub(r'`(code/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
                    '-t','latex','--wrap=preserve'],input=body,text=True,
                   capture_output=True,check=True).stdout
statement=r"""
Fix the actual OS49 source and component line
\(M=\mathcal O(G-O)\), suspension by \(-3G\), selected
\(I_2\) cusp, good IV-star cap of order \(m=3k\), \(k>0\),
norm \(n=\pm1\), finite delta character \(d\), and an actual
periodic index-one fan. Retain the prescribed linear source/lattice
marking and every annular map. For the actual affine source and line
variations on these fixed charts, the global group of extending fibre
translations is precisely the physical \(\mathbb C^*\) action.
Every closed fixed-scalar cap-data family in this marked scope has
trivial sphere return.

More generally, the scalar winding of a closed family satisfies
\[
                          \ell=Nk,\qquad N\in\mathbb Z.
\]
Its physical return is the \(N\)-th power of the actual shorter
OS49 return of P3K.37, whose parameter is \(\lambda=w^k\).
For the same transported fan with primitive physical-delta coordinate
norm \(S=p^2-pq+q^2\), its oriented class is
\[
                       N\frac{k}{4}(S-1)(S-3)\pmod{28}.
\]
The statement keeps the component divisor, both mixed cusp period
orders, the finite root kernel and character, and the inverse endpoint
in the physical monodromy. It concerns the fixed source and marked
cap/line/annular data above; no added ordinary logarithmic clutches,
source-moduli loops, moving cap sites, or arbitrary nontranslation
endpoints are assigned a return here.
"""
out=('\\subsection{Cap-data loops at the component-supported OS49 cusp}\n'
     '\\begin{statement}{P3K.44}{Proved}\n'+statement+
     '\n\\end{statement}\n\\begin{proof}\n'+tex+'\n\\end{proof}\n')
(root/'notes/part3_os49_cap_loops.tex').write_text(out)
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/part3_os49_cap_loops_compile.tex').write_text(
 preamble+'\n'+r'\begin{document}'+'\n'+
 r'\input{notes/part3_os49_cap_loops.tex}'+'\n'+r'\end{document}'+'\n')
print(f'Exported P3K.44; {certificate["checks"]} exact checks PASS.')
