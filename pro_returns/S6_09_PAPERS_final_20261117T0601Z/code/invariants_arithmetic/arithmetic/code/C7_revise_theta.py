from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'sections/C_cm_transcendence.tex';s=p.read_text();(root/'records/C_cm_transcendence_before_lift_audit.tex').write_text(s)
a=s.index(r'\begin{statement}[C.7.7;');b=s.index(r'\paragraph{The archimedean term',a)
new=r'''\begin{statement}[C.7.7; Known with derivation: two unconditional normalized values]
Let $E/\overline{\Q}$ have an algebraic invariant differential,
and let $u$ be an elliptic logarithm of an algebraic nontorsion
point $P$. Then
\[
 \sigma(u)\exp\left(-\frac12u\zeta(u)\right)
\]
is transcendental. If $E$ has CM and $s_2$ is normalized as in
C.7.6, then $\zeta(u)-s_2u$ is also transcendental. The first
assertion concerns the displayed holomorphic normalization;
it does not assert transcendence of either $N(P)$ or
$\theta(u)=\sigma(u)e^{-s_2u^2/2}$.
\end{statement}
\begin{proof}
We use \citet[Theorem 1 and Corollary 1]{waldschmidt1979sigma},
whose complete proof was opened in the translation hosted by its
author. Its Theorem 1 states that, for algebraic invariants
$g_2,g_3$, algebraic elliptic points $\exp_Eu$, $\exp_Ev$, and
$\beta\in\overline{\Q}$, the number
\[
 \frac{\sigma(u+v)}{\sigma(u)\sigma(v)}
                      \exp((\beta-\zeta(v))u)
\]
is transcendental if $\exp_Ev$ is nontorsion and $u,u+v$
are not lattice points. Here ``algebraic elliptic point''
means that the Weierstrass coordinates are algebraic; it does
not mean that its logarithm is algebraic. Take $v=u$ and
$\beta=0$. All hypotheses hold because $P$ is nontorsion.
The sigma duplication formula identifies the displayed number
with
\[
 -\wp'(u)\sigma(u)^2e^{-u\zeta(u)}.
\]
The factor $-\wp'(u)$ is nonzero and algebraic. Therefore
$\sigma(u)e^{-u\zeta(u)/2}$ is transcendental, as also stated
explicitly after Corollary 1 of the cited paper.

For the second assertion we apply the analytic subgroup theorem
in \citet[Theorem 6.1]{huber2022}. In the algebraic universal
vector extension $\widetilde E$ a logarithm of an algebraic lift
of $P$ has coordinates $(u,\zeta(u)-b)$, where $b$ is an algebraic
fibre coordinate, with a possible algebraic linear change of the
second coordinate. If $b=\zeta(u)-s_2u$ were algebraic, this
logarithm would belong to the algebraic line
$\{(z,s_2z):z\in\C\}$. The theorem applies to the connected
commutative algebraic group $\widetilde E$ over
$\overline{\Q}$ and this line, defined over $\overline{\Q}$ by
C.7.6; its exponential contains a nonzero algebraic lift.
It would provide a connected one-dimensional algebraic subgroup
whose Lie algebra is that line. Its projection to $E$ is
nontrivial. A one-dimensional affine algebraic group has no
nonconstant algebraic-group homomorphism to an elliptic curve,
so the subgroup is an elliptic curve isogenous to $E$.
Its inclusion would split the universal vector extension after
that isogeny. This is impossible: the nonzero extension class in
$\operatorname{Ext}^1(E,\mathbb G_a)=H^1(E,\mathcal O_E)$
remains nonzero under isogeny, since pullback is invertible in
characteristic zero.
\end{proof}

\paragraph{A theta criterion requiring its original normalization.}
An earlier draft applied the pointwise criterion printed in
\citet[final slide, comment (c)]{bertrand2017} to
$g(u,v)-s_2uv$, where
$g(u,v)=\log(\sigma(u+v)/(\sigma(u)\sigma(v)))$.
It inferred transcendence of $\theta(u)$ by taking $v=u$.
We withdraw that inference pending verification of the original
lift conventions in \citet[Corollary 3]{bertrand1984}.
Indeed replacing $v$ by $v+\omega$, $\omega\in\Lambda$,
changes $g(u,v)-s_2uv$, modulo $2\pi i\Z$, by
\[
 (\eta(\omega)-s_2\omega)u=\frac{\pi\bar\omega u}{A},
\]
whereas the condition $N\exp_Ev=f(\exp_Eu)$ with $f$
Rosati-antisymmetric depends only on the elliptic points.
Thus the two-sided statement cannot be used with unrestricted
lifts without checking its normalization. The author's slide
and the original paper's first two pages were accessible;
the full original Corollary 3 was not. We use neither direction
of that criterion here. The status of the stronger holomorphic
CM theta assertion in this package is therefore unresolved;
C.7.7 supplies the fully checked replacement above. The
withdrawn text and the lift audit are retained in the records.

'''
s=s[:a]+new+s[b:]
old='It follows from C.7.1 and the real-linear decomposition of\n$\\eta$. C.7.7 does not exclude algebraicity of this product.'
new2=r'''It follows from C.7.1 and the real-linear decomposition of
$\eta$. The normalization proved transcendental in C.7.7 instead
gives the exact identity
\[
 N(P)=|\Delta|^{1/12}
 \left|\sigma(u)e^{-u\zeta(u)/2}\right|
 \exp\left(\frac12\Re\{u(\zeta(u)-\eta(u))\}\right).
\]
Neither formula excludes algebraicity of $N(P)$: transcendence
of one complex factor does not control its absolute value or
its product with the remaining exponential.'''
assert old in s;s=s.replace(old,new2)
p.write_text(s)
bib=root/'references_Croot.bib'
entry=r'''
@article{waldschmidt1979sigma,
 author={Waldschmidt, Michel},
 title={Nombres transcendants et fonctions sigma de {Weierstrass}},
 journal={Comptes Rendus Mathematiques de l'Academie des Sciences, Canada},
 volume={1}, number={2}, pages={111--114}, year={1979},
 url={https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/GDL/SigmaNoteCanada1979-eng.pdf},
 note={verified: complete author-hosted English translation by K. Senthil Kumar and S. Kannappan, June 2015, opened; Theorem 1, its full Schneider--Lang proof, Corollary 1 and the following sigma normalization checked. Original journal metadata independently opened at mathreports.ca}
}
'''
with bib.open('a') as f:f.write(entry)
print('Replaced C.7.7 with the verified Waldschmidt and AST statements; recorded the withdrawn criterion and exact normalization gap; added primary reference.')
