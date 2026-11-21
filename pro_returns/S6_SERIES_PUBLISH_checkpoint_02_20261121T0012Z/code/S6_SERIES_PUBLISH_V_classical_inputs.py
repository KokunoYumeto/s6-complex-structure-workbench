#!/usr/bin/env python3
from S6_SERIES_PUBLISH_editing import Editor, ROOT
import re, json

e=Editor('V')
start=e.text.index('\\section{Geometric and characteristic conventions}')
end=e.text.index('\\section{The monodromy and the marked cusp}',start)
old=e.text[start:end]
new=r'''\section{Characteristic-number conventions}\label{pub:V:sec-characteristic-conventions}
\begin{proposition}[The characteristic numbers and middle form]
\hypertarget{tag-034M}{}\label{sec:V-known-inputs}
\StatementRecord{sec:V-known-inputs}{proved}{034M}{}
Let $M$ be a closed connected almost complex manifold of real dimension
eight, with its complex orientation, with $H^2(M;\mathbb Q)=
H^6(M;\mathbb Q)=0$, $b_4(M)=4$, and $\chi(M)=6$.
Then its middle integral pairing modulo torsion is $I_{3,1}$ and
\begin{equation}
 H^4(M;\mathbb Z)/\operatorname{tors}\cong I_{3,1},\qquad
 c_4[M]=6,\qquad c_2^2[M]=2,\qquad
 \sigma(M)=2,\qquad\operatorname{Td}[M]=0.
 \hypertarget{tag-02EQ}{}\label{maps:eq:F.2}
\end{equation}
\end{proposition}
\begin{proof}
The classes $c_1,c_3$ vanish rationally. The index and signature
polynomials of \cite[equations~(1.2)--(1.4), pp.~3--4]{ffEsoleKang}
therefore reduce to
\begin{equation}
 \operatorname{Td}=\frac{3c_2^2-c_4}{720},\qquad
 \chi^1=\frac{3c_2^2-31c_4}{180},\qquad
 \sigma=\frac{3c_2^2+14c_4}{45}.
 \hypertarget{tag-02EF}{}\label{maps:eq:F.1}
\end{equation}
Here the first two numbers are elliptic-symbol indices of the
almost complex tangent bundle; their integrality follows from
\cite[Theorem~24.5.4 and its corollary, p.~184]{HirzebruchTopologicalMethods}.
Substitution of $c_4[M]=6$ gives
$\sigma(M)=16\operatorname{Td}[M]+2$.
The inequality $|\sigma(M)|\le b_4(M)=4$ forces
$\operatorname{Td}[M]=0$ and $\sigma(M)=2$, and then $c_2^2[M]=2$.
Poincar\'e duality makes the middle pairing modulo torsion
unimodular. Its signature excludes an even unimodular form,
whose signature is divisible by eight. The classification of
indefinite odd unimodular forms
\cite[Theorem~2.2.1, p.~61]{ffPetersSterk} gives $I_{3,1}$.
\end{proof}

\begin{remark}[The orientation in the connected-sum criterion]
\hypertarget{tag-PV06}{}\label{pub:V:mandal-convention}
We use the orientation in
\cite[Corollary~1.4, p.~4, and its proof in \S5]{ffMandal}:
$\ell\mathbb{HP}^2\#m(-\mathbb{HP}^2)$ admits an
orientation-compatible almost complex structure exactly for
$\ell=2m+1$ and odd $m$.
The tangent-class conventions are those of
\cite[Lemma~2.1, p.~5, and Theorem~2.4, p.~7]{ffMandal}.
\end{remark}

'''
e.replace(old,new,'D13','Give the characteristic-number input explicit hypotheses, a numbered statement, and its short specialization of the cited index formulas.','sec:V-known-inputs')

start=e.text.index('\\paragraph{The exterior-square representation of $\\mathrm{Sp}(4)$.}')
end=e.text.index('\\begin{theorem}[exclusion of three further order pairs]',start)
old=e.text[start:end]
new=r'''\begin{lemma}[Primitive exterior-square comparison]
\hypertarget{tag-PV07}{}\label{pub:V:primitive-exterior-square}
Let $E=\mathbb C^4$ have symplectic basis $e_1,e_2,f_1,f_2$,
put $\omega=e_1\wedge f_1+e_2\wedge f_2$, and give
$E_0=\omega^\perp\subset\bigwedge^2E$ the wedge pairing.
The morphism
$\rho:\operatorname{Sp}(E)\to\operatorname{SO}(E_0)$
is surjective with kernel $\{I,-I\}$
\cite[\S7.3, p.~129]{pubLieGroups2016}.
A unipotent element of Jordan type $(2,2,1)$ has as its two
lifts a symplectic transvection and its negative.
For a semisimple lift with eigenvalues $x,x^{-1},y,y^{-1}$,
the eigenvalues on $E_0$ are
\[
 1,\quad xy,\quad x/y,\quad y/x,\quad(xy)^{-1}.
\]
\end{lemma}
\begin{proof}
We use the cited primitive exterior-square morphism and compute
the two comparisons needed here.
The transvection fixing $e_1,e_2,f_2$ and sending $f_1$ to
$f_1+e_1$ acts on the primitive basis
\[
 e_1\wedge e_2,\quad e_1\wedge f_2,\quad e_2\wedge f_1,
 \quad f_1\wedge f_2,\quad e_1\wedge f_1-e_2\wedge f_2.
\]
Its difference from the identity sends the third vector to the
negative of the first and the fourth to the second, and kills
the others. Its Jordan type is $(2,2,1)$.
Conversely, an orthogonal unipotent $I+N$ of this type has
$N^2=0$ and $N^*=-N$, so its image is an isotropic plane.
Choose that plane, its dual isotropic plane, and the remaining
nondegenerate line. In this decomposition $N$ is determined by
a nonzero alternating form on the dual plane. All such forms
are equivalent under its general linear group; extending the
change by the inverse transpose on the image plane gives an
orthogonal change of basis. Its determinant is one, after the
choice of sign on the residual line. Thus these unipotents form
one special-orthogonal conjugacy class. Surjectivity of $\rho$
lifts this conjugacy, and its kernel gives the two stated lifts.
Finally, taking pairwise products of the four eigenvalues and
removing the invariant bivector gives the displayed five
eigenvalues.
\end{proof}

'''
e.replace(old,new,'D17','Cite the classical double cover; retain only the explicit unipotent and eigenvalue comparisons in the form used in the next proof.','pub:V:primitive-exterior-square')
bib=r'''\bibitem[Borcherds et al.(2016)]{pubLieGroups2016}
R.~Borcherds, M.~Haiman, N.~Reshetikhin, V.~Serganova, and T.~Johnson-Freyd.
\emph{Part I: Lie Groups}. Lecture notes, version of 5 October 2016.
\url{https://math.berkeley.edu/~serganov/261/part1.pdf}.

'''
e.replace('\\end{thebibliography}',bib+'\\end{thebibliography}',
          'D18','Add the primary lecture text opened at the exact cited section and page.','pubLieGroups2016')
e.text=e.text.replace('Theorem \\S\\ref{sec:V-known-inputs}','\\Cref{sec:V-known-inputs}')
e.record('D23','Theorem \\S\\ref{sec:V-known-inputs}','\\Cref{sec:V-known-inputs}',
         'Use the type and number of the now numbered characteristic proposition.','sec:V-known-inputs')
e.save()

bibfile=ROOT/'S6_SERIES_PUBLISH_references.bib'
with bibfile.open('a') as f:
 f.write('\n@misc{pubLieGroups2016,\n  author = {Borcherds, Richard and Haiman, Mark and Reshetikhin, Nicolai and Serganova, Vera and Johnson-Freyd, Theo},\n  title = {Part I: {Lie} Groups},\n  year = {2016},\n  note = {Version of 5 October 2016; verified: section 7.3, page 129, opened 20 November 2026},\n  url = {https://math.berkeley.edu/~serganov/261/part1.pdf}\n}\n')
(ROOT/'records/S6_SERIES_PUBLISH_classical_source_check.json').write_text(json.dumps({
 'source':'https://math.berkeley.edu/~serganov/261/part1.pdf',
 'version':'5 October 2016','locator':'section 7.3, printed page 129 (PDF page 139)',
 'checked':'Primitive exterior-square morphism Sp(4,C) to SO(5,C), surjective, kernel plus/minus identity.',
 'scope':'The two form-specific unipotent and eigenvalue calculations remain proved in the paper.',
 'date':'2026-11-20','outcome':'verified by opening the primary lecture text'
},indent=2)+'\n')
