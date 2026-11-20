#!/usr/bin/env python3
"""Prepare guarded Paper I publication edits; do not edit a shared source."""
from pathlib import Path
import hashlib,json,re

HERE=Path(__file__).resolve().parent
BODY=HERE.parent/'parts/I.body.linked.tex'
source=BODY.read_text()
patches=[]


def add(label,purpose,old,new):
    assert source.count(old)==1,(label,purpose,source.count(old))
    patches.append(dict(label=label,purpose=purpose,old=old,new=new))


def proof(label):
    start=source.index(r'\label{'+label+'}')
    a=source.index(r'\begin{proof}',start)
    b=source.index(r'\end{proof}',a)+len(r'\end{proof}')
    return source[a:b]


add('inv:A2.1','Replace absent symbolic checker by supplied fresh exact calculation',
r'''The symbolic residuals
of all three identities are zero in \texttt{a\_calculations.py}.''',
r'''Rational differentiation and cancellation verify these three
identities in
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py};
the exact residual checks are saved beside it in
\path{priority_rows_exact.output.json}.''')

add('night:P5.1','Credit the permitted re-derivations without an unsupported blindness claim',
r'''\subsection{The blind control: local charts and coherent direct images}

The proof in this section was written before opening either version of
arXiv:2610.00250.  Only the construction data of AC26 are used for the
threefold.  Write''',
r'''\subsection{Credited re-derivations: local charts and coherent direct images}

For the standard marked data, the vertical splitting and structure
direct images are re-derived from
\cite[Proposition~6.6, pp.~77--78; Lemma~6.7, p.~78;
Proposition~6.10, pp.~79--80]{DuEtAl2026v1}.
The tangent dimensions and Kuranishi germ are re-derived from its
Theorem~6.12, pp.~81--82, and Proposition~6.16, p.~85.
The full automorphism and period comparison, including the exact
parameter transport, is given in \cref{night:P5.7}.
The proofs below retain their stated ranges of affine twists.
Write''')

add('night:P5.3','Name the current exact degree and incidence calculation',
r'''The bundle and incidence computations are independently recomputed in
\texttt{code/part5/bundle\_cohomology.py}.''',
r'''The root-floor degree calculation and the two cusp incidence matrices
are evaluated over the integers in
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py}.
Its output \path{priority_rows_exact.output.json} records all five
direct-image rows and the resulting two cohomology tuples.''')

add('night:P5.5','Name the current exact centralizer calculation',
r'''the complete rational linear elimination is in
\texttt{code/part5/centralizer.py}.''',
r'''rational elimination of the two complete commutator systems in
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py}
has rank fourteen, and verifies the two displayed independent
basis matrices.''')

add('night:P5.5','Replace absent integral-complex executable assertion',
r'''The independent total-complex
calculation in \texttt{code/part5/orbifold\_lattice\_complex.py} prints
every differential and checks the same vanishing.''',
r'''The integral mapping-cone calculation in
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py}
constructs every differential from the cyclic resolutions and the
three overlap restrictions, then checks the same vanishing by Smith
decomposition with unimodular basis changes. All differential,
integral-kernel and image matrices are saved in
\path{priority_rows_exact.output.json}.''')

add('night:P5.6','Replace the last absent orbifold_lattice_complex.py assertion',
r'''The script \texttt{orbifold\_lattice\_complex.py} prints its three
integer differentials, checks their zero products, and computes
$H^0=\mathbb Z$, $H^1=0$, $H^2=\mathbb Z\oplus\mathbb Z/2$.''',
r'''The program
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py}
forms the resulting $28\times14$, $20\times28$ and $8\times20$
integer differentials and verifies both zero products.
Smith decompositions with unimodular changes of basis identify each
integral kernel before quotienting by the preceding image, giving
$H^0=\mathbb Z$, $H^1=0$, $H^2=\mathbb Z\oplus\mathbb Z/2$.
The matrices and quotient invariants are in
\path{priority_rows_exact.output.json}.''')

add('inv:A4.1','Specify the supplied polynomial module verifier',
r'''All matrix identities have also been checked over $\Z[x,y,z]$ by
the supplied exact program.''',
r'''The polynomial maps and all six annihilator identities are also
verified over $\Z[x,y,z]$ in
\path{code/current_audits/audit_paper_i/code/priority_rows_exact.py};
its output retains both presentation matrices.''')

a4=proof('inv:A4.2')
add('inv:A4.2','Keep the full source correction and remove source-reading workflow',a4,
r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item The double and triple charts in \cref{inv:A4.1} exhaust the
singular strata of $W$. Their injections into free logarithmic
modules prove absence of degree-one cusp torsion. Their degree-two
presentations have a nonzero torsion generator at every general
point of a double curve. At a multiple fibre the finite etale
comparison
\[
q^*\Omega^1_{N_j/B}=\Omega^1_{J'_j/B}
\]
is an isomorphism; its summand $R/(s^{m_j-1})\,ds$ is nonzero
for $m_j=3,4$. Faithful flatness descends both the torsion and its
support. There are no other critical fibres, and ordinary relative
differentials are locally free on their complement. Thus the
degree-one support is exactly $S_1\cup S_2$, whereas degree two
also has cusp torsion, as asserted.
\end{enumerate}
\end{proof}''')

c2=proof('inv:C2.1')
add('inv:C2.1','Short cited specialization, retaining the exact arrow table and new supplied verifier',c2,
r'''\begin{proof}
\begin{enumerate}[label=\arabic*.,leftmargin=*]
\item Apply \cite[Theorem~3, p.~7; Proposition~6, p.~16;
Lemma~8, p.~17]{Stelzig2021} to the bounded-bidegree complex of
smooth forms. The theorem permits arbitrary cardinal dimensions.
Its odd zigzags contribute to total cohomology; the sphere Betti
groups and the single extreme bidegrees therefore leave only dots
at $(0,0)$ and $(3,3)$. By \cref{inv:C1.1} and conjugation,
both spectral sequences have no differential after $d_1$, so every
remaining zigzag is an arrow. The horizontal arrows are exactly
\begin{equation}\label{inv:eq:C-arrows}
\begin{array}{c|c|r}
\text{source}&\text{target}&\text{multiplicity}\\\hline
(0,1)&(1,1)&1\\
(1,1)&(2,1)&h\\
(1,2)&(2,2)&h\\
(2,2)&(3,2)&1.
\end{array}
\end{equation}
The vertical arrows are their reflections in $p=q$.

\item Under the cited decomposition, an arrow contributes its target
to Bott--Chern cohomology and its source to Aeppli cohomology;
a dot contributes to both and a square to neither. The induced
isomorphisms in Lemma~8 respect the two definitions in the statement.
Counting the displayed arrows and their reflections gives every
entry of \eqref{inv:eq:C-BC-A}. Kernels, images and these quotients
commute with direct sums, including the possible infinite sum of
squares.

\item The program
\path{code/current_audits/audit_paper_i/code/main_D_double_complex.py}
uses rational Gaussian elimination with Python fractions to compute
both cohomologies directly from their kernels and images. For each
$h=0,\ldots,5$, it includes an anticommuting acyclic square,
computes the induced $d_1$ on column cohomology and the total
cohomology, and compares with a separate corner count. All
54 checks pass; its matrices and tables are saved in
\path{main_D_double_complex.output.json}. These finite calculations
corroborate the universal decomposition argument above.
\end{enumerate}
\end{proof}''')

a2=proof('inv:A2.2')
start=a2.index(r'\item Here are the numerical methods actually run.')
end=a2.rindex(r'\end{enumerate}')
old=a2[start:end]
new=r'''\item The real period also has the integral expression
\[
\Omega_R=\frac{\sqrt2}{3^{1/4}}
\int_0^{\pi/2}(1-\tfrac12\sin^2\theta)^{-1/2}\,d\theta,
\qquad C_4=\frac{\sqrt2}{3\Omega_R}.
\]
It follows by the elliptic-integral substitution for the three roots
$\sqrt3,0,-\sqrt3$ of $Y^2=X^3-3X$ and the differential
$dX/(2Y)$. The beta-integral evaluation gives the gamma expression
in \eqref{inv:eq:A-mu-value}.

For the displayed numerical values,
\path{code/current_audits/audit_paper_i/code/a2_scalar_arb.py}
evaluates the divisor-sum series of $E_4(i)$ and $E_6(\rho)$
with 100 terms at 120 decimal working digits in Arb, and independently
evaluates the gamma expression for $C_4$.
The elementary inequalities $\sigma_3(n)\le n^4$,
$\sigma_5(n)\le n^6$, $e^{-2\pi}<1/500$ and
$e^{-\pi\sqrt3}<1/200$ give respective tail bounds
\[
250(N+1)^4 500^{-N-1},\qquad
1024(N+1)^6 200^{-N-1}\quad(N=100).
\]
The ratios of successive majorant terms are less than $1/480$
and $1/180$, respectively, which proves these tail estimates.
All arithmetic roundoff is included in the balls. The two $C_4$
enclosures overlap, and the resulting strict rational enclosures are
\[
\begin{aligned}
0.2366093140807852&<C_4<0.2366093140807853,\\
0.0801022110875382&<\operatorname{Re}K_2<0.0801022110875383,\\
0.1387410994022233&<\operatorname{Im}K_2<0.1387410994022234.
\end{aligned}
\]
All twelve checks, the narrower balls and their full inputs are
saved in \path{a2_scalar_arb.output.json}. The exact nonvanishing
and orders were proved in the preceding steps.
'''
add('inv:A2.2','Replace unavailable numerical diagnostics by supplied rigorous Arb route, preserving the analytic period evaluation',old,new)

updated=source
for patch in patches:
    assert updated.count(patch['old'])==1
    updated=updated.replace(patch['old'],patch['new'])
labels_before=re.findall(r'\\label\{([^}]+)\}',source)
labels_after=re.findall(r'\\label\{([^}]+)\}',updated)
assert sorted(labels_before)==sorted(labels_after),'Label set changed'
assert 'orbifold\\_lattice\\_complex.py' not in updated
assert r'\subsection{The blind control:' not in updated
out=HERE/'priority_closure_patches.json'
out.write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
receipt={'body':str(BODY),'body_read_sha256':hashlib.sha256(source.encode()).hexdigest(),
         'patch_count':len(patches),'all_guards_unique':True,'label_multiset_unchanged':True,
         'shared_body_written':False,'patch_file_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
         'old_C2_1_proof_words':len(c2.split()),
         'new_C2_1_proof_words':len(next(p['new'] for p in patches if p['label']=='inv:C2.1').split()),
         'note':'Every removed historical numerical/program claim is preserved verbatim as old text in the guarded patch file. No absent historical program is called a replay.'}
(HERE/'priority_closure_patches_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
