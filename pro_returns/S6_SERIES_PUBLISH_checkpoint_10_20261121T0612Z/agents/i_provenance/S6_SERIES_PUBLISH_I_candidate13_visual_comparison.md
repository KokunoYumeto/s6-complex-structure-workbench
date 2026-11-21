# Candidate13: six bounded visual corrections

Complete page-reading QA and bounded full affected-text comparison; not a new mathematical certification. No theorem, hypothesis, map, equation, proof step, result scope, label or tag is changed.

Source SHA-256: `26a6f5f8b1e911de363bed7346e970bc8fb77b21cf04fe9a2ce4d1f90d95b49e`. PDF SHA-256: `519355e39d7d821a10d728d5c8dbf69a50826ee215ab98619803d44e1cae2a2b`.

## ari:C.6.3

Full current statement/tables and both proof steps read on pages266–267; attached proof read as text. Exact pointed model maps, discriminant scaling, local heights and component basis calculations unchanged.

Complete attached receiving statement and proof; prior consolidations are not re-credited.

```diff
--- current
+++ replacement
@@ -91,8 +91,7 @@
 so the local height is zero. Multiplying $p^{\lambda_p/\log p}$
 gives the listed constants $A_t$.
 
-\item We specify the component labels without relying on an
-unrecorded ordering of a resolution graph. The label $0$
+\item The component labels are defined as follows. The label $0$
 means the identity component, and $c_P$ is the class represented
 by the explicitly displayed section $P$. At an odd prime of
 type $I_0^*$ this nonidentity class is the outer component

```

## ari:C.7.6

Full current statement and all three proof steps read on page299; full attached proof read as text. Legendre decomposition, automorphy/divisor/scalar normalization, nonzero Laurent coefficient and square-lattice divisor example unchanged.

Complete attached receiving statement and proof; prior consolidations are not re-credited.

```diff
--- current
+++ replacement
@@ -62,8 +62,7 @@
 \]
 The coefficients of the rational function in this algebraic formal
 parameter are algebraic. As $\alpha^2-d\ne0$, this proves
-$s_2\in\overline{\Q}$ without an unnormalized appeal to a CM
-weight-two form. It also proves that the functions in
+$s_2\in\overline{\Q}$. It also proves that the functions in
 \eqref{ari:eq:ct-CMmult} are algebraic over the chosen field.
 At nontorsion $u$, none of the arguments $\alpha u$ is a lattice
 point; evaluating the identity proves the algebraicity implication.

```

## I:CM-compact-comparison

Full current remark read on page302 and in exact TeX. Both cited theorem/page tokens remain byte-identical, with only the conjunction inserted between citations; all exact norm and antisymmetric-to-diagonal comparisons retained.

This numbered remark was introduced during the publication edit; the complete current/replacement remark is archived. This punctuation-only change does not alter its mathematical content.

```diff
--- current
+++ replacement
@@ -20,7 +20,7 @@
 The concrete antisymmetric and diagonal extensions are
 compared by the maps in \cref{ari:C.7.10}.
 The vector-extension statements
-\cite[Theorem~3.1, p.~150]{bertrand1995}\cite[Theorem~3.1.2, p.~386]{bost2009}
+\cite[Theorem~3.1, p.~150]{bertrand1995} and \cite[Theorem~3.1.2, p.~386]{bost2009}
 use an algebraic connection, as described in
 \cref{I:Gaussian-comparison}.
 \end{remark}
```

## ari:C.7.12

Full current statement and every nested proof step read on pages311–316; full attached proof read as text. Only two existing citation locators gain spaces; every division identity, degree/height bound, translated-function argument, interpolation inequality and tangent/rank calculation is unchanged.

Complete attached receiving statement and proof; prior consolidations are not re-credited.

```diff
--- current
+++ replacement
@@ -355,7 +355,7 @@
 \Needspace{6\baselineskip}
 \item \emph{Interpolation inequalities and algebraic tangents.}\par
 The sufficient inequality in Gramain--Mignotte--Waldschmidt
-\citep[Theorem2.1,pp.101--102]{gramain1986values} has the form
+\citep[Theorem~2.1, pp.~101--102]{gramain1986values} has the form
 \[
  d(N)\prod_{j=1}^k\max\{d(N)\psi_j(N),\theta_j(R(N))\}
  \le c_0\mu(N)^{k-1}\varphi(N)^k,
@@ -420,7 +420,7 @@
 
 \item  Finally the period-refined rank comparison
 \citep[Theorem~4.1, pp.~385--386, and Corollary~4.3, p.~386]{waldschmidt1988periodrank}
-\citep[main theorem,p.363]{roy1993periodrank}
+\citep[main theorem, p.~363]{roy1993periodrank}
 has coefficient $\alpha(G)=2\dim G-2d_0(G)-d_1(G)$,
 where the last terms count additive and multiplicative
 quotients. Both vanish for $G_Q$. An additive homomorphism

```

## push:src:E.2.1

Full current consolidated theorem and proof1–10 read on pages322–326; full original attached push:E2.1 proof read as text. The new edit is solely deletion of the unused-positivity-theorem qualifier; all root/Picard maps, monomial inequalities, residue/KS/Kuranishi arguments and standard Koszul direct-image calculations remain unchanged.

Complete attached receiving statement and proof; prior consolidations are not re-credited.

```diff
--- current
+++ replacement
@@ -112,7 +112,7 @@
  \end{split}
 \]
 The second equality identifies the remaining monomials
-$x^{-i-1}y^{-j-1}$; it does not require a positivity theorem.
+$x^{-i-1}y^{-j-1}$.
 The bundles $\mathcal O(-z),\mathcal O(-2z)$ are acyclic.
 Indeed a possible degree-one monomial would give
 $m(i+1)+n(j+1)=az$, with $a=1$ or $2$.

```
