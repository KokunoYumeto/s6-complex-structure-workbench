#!/usr/bin/env python3
"""Export the audited marked fixed-source cap-data loop theorem K41."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,shutil,subprocess

root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_fixed_source_cap_loops_working.md'
text=source.read_text()
assert 'Proved as P3K.41' in text
certificate=json.loads((root/'code/part3/fixed_source_cap_loops.json').read_text())
assert certificate['status']=='PASS'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
shutil.copy2(source,root/'records'/f'pre_export_{stamp}_{source.name}')
body=text[text.index('## CP.1.'):text.index('## Audit status')]
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
body=re.sub(r'`(code/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
                    '-t','latex','--wrap=preserve'],input=body,text=True,
                   capture_output=True,check=True).stdout
statement=r"""
Fix a marked rational elliptic source in the whole-zero selected
\(I_1\) sphere catalogue, its actual source line, translation
\(Q=bG\), logarithmic sites, root orders \(m_i\), norm integers
\(n_i\), and an index-one periodic fan. Retain every finite line
character and every annular map. Consider loops of the actual affine
source maps and line units of P3F.44/P3F.49 with their prescribed
linear source/lattice marking, together with the scalar \(\lambda\).
Put \(M=\prod_i m_i\), including the order-one and framing-chart
norms in
\[
           \sum_i\frac{n_i}{m_i}=\frac{\varepsilon}{M},
                \qquad\varepsilon\in\{1,-1\}.
\]
The global group of extending fibrewise translations is exactly
the physical \(\mathbb C^*\) action. In particular every such
fixed-scalar cap-data loop has trivial sphere mapping class.

More generally, a closed loop in this marked scope with scalar
winding \(\ell\) satisfies
\[
                       \ell=N\frac{M}{b},\qquad N\in\mathbb Z.
\]
Its physical return is isotopic to the \(N\)-th power of the
actual shorter scalar return of P3K.35, whose parameter is
\(\lambda=w^{M/b}\). Thus the local finite kernels of \(1-D_i\)
produce no additional return class in this specified cap-data scope.
For the transported fan coordinate \(S=p^2-pq+q^2\), with
\(\gcd(p,q)=1\), write \(H=Ma^2/d\) and let \(\chi\) be the
actual page value in P3K.35. The oriented return is
\[
 [\Sigma_\Phi]
 =\frac{N}{b}\left(\chi(4-3S)+\frac{H(3S^2-7)}8\right)
                         \pmod{28}.
\]
This equality is the integer return of a constructed shorter family
and its iterates. The proof retains the inverse closing arrow in the
physical monodromy. It concerns the stated affine cap/line/annular
variations; moving logarithmic sites, source-moduli loops, arbitrary
nontranslation endpoint maps, and the component-supported OS49
model are outside this statement.
"""
out=('\\subsection{Marked fixed-source cap-data loops}\n'
     '\\begin{statement}{P3K.41}{Proved}\n'+statement+
     '\n\\end{statement}\n\\begin{proof}\n'+tex+'\n\\end{proof}\n')
(root/'notes/part3_fixed_source_cap_loops.tex').write_text(out)
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/part3_fixed_source_cap_loops_compile.tex').write_text(
 preamble+'\n'+r'\begin{document}'+'\n'+
 r'\input{notes/part3_fixed_source_cap_loops.tex}'+'\n'+r'\end{document}'+'\n')
print(f'Exported P3K.41; exact certificate {certificate["checks"]} checks PASS.')
