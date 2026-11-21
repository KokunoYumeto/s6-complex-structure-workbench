#!/usr/bin/env python3
"""Produce guarded suggestions only; do not mutate the main TeX file."""
from pathlib import Path
import hashlib
import json
import re

folder = Path('/workspace/scratch/653608133b22/work/agents/v_topology')
source = folder.parents[1] / 'S6_SERIES_PUBLISH_V.tex'
text = source.read_text()
patches = []

def add(identifier, old, new):
    global text
    count = text.count(old)
    assert count == 1, (identifier, count)
    patches.append(dict(id=identifier, expected_count=1, old=old, new=new))
    text = text.replace(old, new)

add('resolved_datum_base_and_markings', r'''Let $X$ be a canonical marked member of the $(3,4,\infty)$
family, with sphere twists
$v_1=(1,2,-4,0)^t$, $v_2=(-1,-3,3,0)^t$ and the untwisted
cusp collar. Write $S_1,S_2$ for the reduced multiple fibres,
of multiplicities three and four, and $W$ for the cusp divisor.''', r'''Let $f:X\to B=\mathbb P^1_t$ be a canonical marked member of the
$(3,4,\infty)$ family, with $p_1=0$, $p_2=1$, $p_0=\infty$,
sphere twists $v_1=(1,2,-4,0)^t$, $v_2=(-1,-3,3,0)^t$,
and the untwisted cusp collar. Put $B^\circ=B\setminus\{p_0,p_1,p_2\}$.
Write $S_1,S_2$ for the reduced multiple fibres, of multiplicities
three and four, and $W$ for the cusp divisor.
Let $S\to B$ be the smooth relatively minimal elliptic surface
whose Weierstrass model is
\[
 y^2=x^3-3t^3(t-1)x+2t^4(t-1)^2.
\]
It has $j=1728t$ and singular fibres of types $IV^*$, $III$, and
$I_1$ at $p_1,p_2,p_0$, respectively \cite[\S2, p.~3]{E26}.

Use the homology bases $(\widehat\gamma,\widehat u,
\widehat w,\widehat\delta)$ for $X$ and $(e_1,e_2)$ for $S$,
with dual basis $(\gamma,u^*,w^*,\delta^*,e_1^*,e_2^*)$ for
their direct sum. The marked homology monodromies are
\[
 A_1=\begin{pmatrix}
 1&0&0&0\\6&0&1&0\\-6&-1&-1&0\\-2&1&0&1
 \end{pmatrix},\qquad
 A_2=\begin{pmatrix}
 1&0&0&0\\0&0&-1&0\\-6&1&0&0\\3&0&1&1
 \end{pmatrix},\qquad A_0=(A_1A_2)^{-1},
\]
\[
 C_1=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},\qquad
 C_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 C_0=(C_1C_2)^{-1}=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Write $\Pi_c$ for the period matrix of $X$ in this canonical
marking; its last two columns are $I_2$, as in
\SeriesRef{def:common-conventions}.''')

add('resolved_construction_dependencies',
    r'\StatementRecord{maps:src:E.1.2}{proved}{02M5}{\eqref{maps:eq:E.1}, \eqref{maps:eq:E.4}, \eqref{maps:eq:E.3}}',
    r'\StatementRecord{maps:src:E.1.2}{proved}{02M5}{\cref{def:V:resolved-product-data}, \cref{night:P1.9}, \eqref{maps:eq:E.1}, \eqref{maps:eq:E.4}, \eqref{maps:eq:E.3}}')

add('resolved_cusp_matrix_name',
    r'\(A_1\oplus C_1,A_2\oplus C_2,M_0\oplus C_0\).',
    r'\(A_1\oplus C_1,A_2\oplus C_2,A_0\oplus C_0\).')

add('resolved_integral_c1_map', r'''\item Since $L$ is pulled from a line on $S^6$, its integral first Chern
class vanishes, so $c_1(Z)=0$.  Riemann--Roch and the signature''', r'''\item Since $H^2(X;\mathbb Z)=0$, we have $c_1(L)=0$.
The canonical formula gives $c_1(Z)=5\Pi^*c_1(L)=0$.
Riemann--Roch and the signature''')

add('resolved_headline_morphism_scope', r'''The fibre product $X\times_{\mathbb P^1}S$ has the small
crepant resolution $\Pi:Z\to X$ of that theorem.''', r'''The Weierstrass model $\mathscr W\to X$ of that theorem has a
small crepant resolution $r:Z\to\mathscr W$.
Its composition $\Pi:Z\to X$ is proper, and $Z$ is
bimeromorphic to $X\times_{\mathbb P^1}S$.''')

add('resolved_abstract_morphism_scope', r'''class $\mathcal C$ as a small crepant resolution of the fibre product of
a complex six-sphere with an elliptic surface; give an effective''', r'''class $\mathcal C$ as a small crepant resolution of a Weierstrass model,
bimeromorphic to the fibre product of a complex six-sphere with an
elliptic surface; give an effective''')

original = source.read_text()
for pattern in (r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}'):
    assert sorted(re.findall(pattern, original)) == sorted(re.findall(pattern, text)), pattern

payload = dict(
    source=str(source),
    source_sha256=hashlib.sha256(original.encode()).hexdigest(),
    instruction='Apply sequentially only when each old string occurs exactly once. These are notation/dependency/morphism-scope suggestions after rereading the four resolved-product proofs against the corrected original; the main TeX file has not been edited. Existing labels and tags are preserved.',
    patches=patches,
)
target = folder / 'S6_SERIES_PUBLISH_V_resolved_guarded_patch.json'
target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(f'Wrote {len(patches)} guarded patches: {target}')
print('Verified every guard occurs once, all existing labels/tags are preserved, and main source was not changed.')
