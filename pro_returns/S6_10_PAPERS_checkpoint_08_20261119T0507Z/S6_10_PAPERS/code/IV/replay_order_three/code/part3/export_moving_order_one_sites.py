#!/usr/bin/env python3
"""Export the audited actual moving regular-site theorem P3K.43."""
from pathlib import Path
from datetime import datetime,timezone
import json,re,shutil,subprocess

root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_moving_order_one_sites_working.md'
text=source.read_text()
assert 'Proved as P3K.43' in text
certificate=json.loads((root/'code/part3/moving_order_one_sites.json').read_text())
assert certificate['status']=='PASS'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
shutil.copy2(source,root/'records'/f'pre_export_{stamp}_{source.name}')
body=text[text.index('## MS.1.'):text.index('## Audit and certificate status')]
body=re.sub(r'(?m)^## (.+)$',lambda m:r'\par\medskip\noindent\textbf{'+m.group(1)+r'}\par\nobreak',body)
body=re.sub(r'`(code/[^`]+)`',lambda m:r'\path{'+m.group(1)+'}',body)
tex=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex',
                    '-t','latex','--wrap=preserve'],input=body,text=True,
                   capture_output=True,check=True).stdout
statement=r"""
Fix the marked rational elliptic source, actual line, translation
\(Q=bG\), whole-zero selected \(I_1\), effective additive caps,
and transported periodic index-one fan of P3K.41. Allow the ordinary
order-one logarithmic sites to move through the regular-source locus,
away from every fixed singular value and effective cap. Retain their
signed norms, all elliptic and delta period coefficients, finite
characters, annular maps, and prescribed linear source/lattice marking.
Consider an actual closed marked family, with its specified endpoint;
site permutations must carry the complete cap data.

There is an actual local family isomorphism from a moving-site family
to the reference-site family at the same scalar, extending through every
root and cusp chart and carrying the physical circle and normal collar.
These isomorphisms identify every fixed-scalar closed loop, including
closed braids around the fixed singular values, with a smoothly trivial
sphere bundle. More generally, if the scalar has winding \(\ell\),
then
\[
                    \ell=N\frac{M}{b},\qquad N\in\mathbb Z,
\]
and its physical return is the \(N\)-th power of the constructed
shorter scalar return of P3K.35, with parameter
\(\lambda=w^{M/b}\). In particular moving these sites contributes
no additional return class. For the transported fan coordinate
\(S=p^2-pq+q^2\), its oriented class is
\[
 \frac{N}{b}\left(\chi(4-3S)+\frac{H(3S^2-7)}8\right)
             \pmod {28},\qquad H=Ma^2/d.
\]
This is the integer value of an actual shorter family and its iterates.
The statement concerns the stated closed marked family scope; it does
not assign a return to source-moduli loops, collisions with source
singular values, arbitrary nontranslation endpoints, or the
component-supported OS49 cusp.
"""
out=('\\subsection{Moving regular order-one logarithmic sites}\n'
     '\\begin{statement}{P3K.43}{Proved}\n'+statement+
     '\n\\end{statement}\n\\begin{proof}\n'+tex+'\n\\end{proof}\n')
(root/'notes/part3_moving_order_one_sites.tex').write_text(out)
preamble=(root/'S6_06_BLIND_paper.tex').read_text().split(r'\begin{document}')[0]
(root/'records/part3_moving_order_one_sites_compile.tex').write_text(
 preamble+'\n'+r'\begin{document}'+'\n'+
 r'\input{notes/part3_moving_order_one_sites.tex}'+'\n'+r'\end{document}'+'\n')
print(f'Exported P3K.43; exact certificate {certificate["checks"]} checks PASS.')


# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    ['code/part3/results_mapping.json'], ['notes/part3_moving_order_one_sites.tex'], origin='code/part3/export_moving_order_one_sites.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
