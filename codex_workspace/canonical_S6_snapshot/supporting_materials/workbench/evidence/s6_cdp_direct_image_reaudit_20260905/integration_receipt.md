# CDP direct-image audit integration receipt

Date: 2026-09-05. The parent task independently read and approved all three staged replacement spans. Only canonical supporting_materials/workbench/research/cdp_program.tex and integral_leray.tex were edited. The evidence directory contains copies and receipts; no other canonical source was edited.

## Exact replacements

- cdp_program.tex original lines 375–429: replaced the five-term matching argument with the actual analytic-duality pairing and hypersurface Ext calculation. Final replacement lines 375–425.
- cdp_program.tex original lines 900–916: replaced the complex scalar in real coordinates by the exact real translation and proved its clockwise mixed cohomology class. Final replacement lines 896–985.
- integral_leray.tex original lines 801–820: proved complex-structure covariance from the period identity, checked both original invariant translation vectors, and established the precise based endpoint relation. Final replacement lines 801–871.

The third staged span originally named 801–819, but its old display closes on line 820. The span metadata was corrected to 801–820 before applying it; the approved mathematical replacement text was unchanged. This avoids leaving a duplicate closing display delimiter.

## Preservation and verification

Before editing, both canonical SHA-256 hashes matched the audited input hashes. The before snapshots were made by byte-preserving copies and their hashes matched those inputs. The source patch was applied with apply_patch. The final canonical text was compared against the original text with exactly the three staged replacements substituted; both comparisons were equal. After snapshots were made by byte-preserving copies and matched the final canonical hashes. Original source line endings were LF. No build, publication, or worker run was performed.

The two source files are frozen by this subagent after these corrections. The parent task handles current-status prose, independent diff review, and serial builds. The mathematical scope limits in AUDIT.md remain: these corrected local proofs do not themselves certify the entire S6 construction or refute CDP20 Theorem 2.2.

## Source hashes

- cdp_program.tex
  - Before: 2BD54198AE3E8969DD8FE690556BF9E07E335A6ECE024A1C45A3DD296C6DB073 (60816 bytes)
  - After: B58CC45A20F4CF928EFB295F38798093B4E37207DF793CBECFA112B9B5DE08F1 (63623 bytes)
- integral_leray.tex
  - Before: 69863126EED80CA895CA71E550BD12E1E51AF514649247DD582709ED5819D355 (34487 bytes)
  - After: 0D489E1EF56C73DA08528D68BD990CB4C70C3A6884BBA62D1DAB110A168A7ED1 (35987 bytes)

Machine-readable source hashes and verification scope are in source_hashes.json. Full input hashes for the audit are in INPUT_HASHES.md.

## Full diff

```diff
diff --git before/cdp_program.tex after/cdp_program.tex
index dcc66f0..389e81b 100644
--- before/cdp_program.tex
+++ after/cdp_program.tex
@@ -373,59 +373,55 @@ $W$ is used.
 \end{theorem}
 
 \begin{proof}
-The Cartier divisor gives two short exact sequences
-\[
-0\to E(-W)\to E\to i_*F\to0
-\tag{5.12}
-\]
-and, by adjunction,
-\[
-0\to E^\vee\otimes\omega_X
-\to E^\vee\otimes\omega_X(W)
-\to i_*(F^\vee\otimes\omega_W)\to0.
-\tag{5.13}
-\]
-Smooth Serre duality on the compact threefold gives functorial isomorphisms
-\[
-H^r(X,G)^\vee\simeq H^{3-r}(X,G^\vee\otimes\omega_X)
-\tag{5.14}
-\]
-for every vector bundle $G$
-\cite[Theorem~9.37]{Lee2024}.  Naturality of the trace pairing says that the
-dual of the map on cohomology induced by $E(-W)\to E$ is the map induced by
-$E^\vee\otimes\omega_X\to E^\vee\otimes\omega_X(W)$.
-
-Fix $q\in\{0,1,2\}$.  Dualize the relevant five terms of the long exact
-sequence of (5.12) and use (5.14).  They become
-\[
-\begin{split}
-H^{2-q}(X,E^\vee\otimes\omega_X)
-&\longrightarrow H^{2-q}(X,E^\vee\otimes\omega_X(W))\\
-&\longrightarrow H^q(W,F)^\vee\\
-&\longrightarrow H^{3-q}(X,E^\vee\otimes\omega_X)
-\longrightarrow H^{3-q}(X,E^\vee\otimes\omega_X(W)).
-\end{split}
-\tag{5.15}
-\]
-The long exact sequence of (5.13) is the same five-term sequence with its
-middle group replaced by
-$H^{2-q}(W,F^\vee\otimes\omega_W)$.  Naturality supplies a commutative
-diagram whose four outer vertical arrows are identities.  The five lemma
-(or exactness at the three middle terms) gives the unique middle isomorphism
-(5.11).  Finite dimensionality makes the pairing perfect.
-
-For $q=3$, the map
-$H^3(X,E(-W))\to H^3(X,E)$ is dual under (5.14) to the injective map
-\[
-H^0(X,E^\vee\otimes\omega_X)
-\hookrightarrow H^0(X,E^\vee\otimes\omega_X(W)).
-\]
-It is therefore surjective.  The long exact sequence of (5.12) gives
-$H^3(W,F)=0$.  For $q>3$ both adjacent ambient cohomology groups vanish by
-the dimension-three Dolbeault resolution, so (5.12) gives
-$H^q(W,F)=0$.  This also agrees with analytic duality for the Gorenstein
-hypersurface $W$ in Ramis--Ruget
-\cite[Theorems~1--2 and Proposition~2]{RamisRuget1970}.
+Let \(i:W\hookrightarrow X\) be the given Cartier inclusion.  The
+length-one locally free resolution
+\[
+ 0\longrightarrow\mathcal O_X(-W)
+ \xrightarrow{\;\cdot g\;}\mathcal O_X
+ \longrightarrow i_*\mathcal O_W\longrightarrow0
+\]
+is locally defined by a nonzerodivisor \(g\); changing \(g\) by a unit
+gives the usual transition functions for \(\mathcal O_X(W)\).
+Applying sheaf Hom into \(\omega_X\), the degree-zero map is
+injective and its cokernel is
+\[
+ \mathcal E xt^1_X(i_*\mathcal O_W,\omega_X)
+ =i_*\bigl((\omega_X\otimes\mathcal O_X(W))|_W\bigr)
+ =i_*\omega_W.
+\]
+The other sheaf Ext groups vanish.  Equivalently, \(W\) is a
+two-dimensional Cohen--Macaulay Gorenstein complex space and its
+analytic dualizing complex is
+\[
+ K_W^\bullet\simeq\omega_W[2].
+\]
+This is the hypersurface calculation in
+\cite[Proposition~2 and pp.~90--91]{RamisRuget1970}; no normality or
+reducedness of the Cartier divisor is used.
+
+For the locally free sheaf \(F=E|_W\), the analytic duality trace of
+\cite[Theorem~2, pp.~82--83]{RamisRuget1970} supplies the actual
+functorial pairing, and identifies the dual of \(H_c^q(W,F)\) with
+\[
+ \operatorname{Ext}^{-q}_W(F,K_W^\bullet)
+ =\operatorname{Ext}^{2-q}_W(F,\omega_W)
+ =H^{2-q}(W,F^\vee\otimes\omega_W).
+\]
+The last equality follows because the positive sheaf Ext groups
+of a locally free first argument vanish.  Since \(W\) is compact,
+\(H_c^q(W,F)=H^q(W,F)\); coherent cohomology is finite-dimensional,
+so this pairing is perfect in the ordinary algebraic sense.
+It is this trace pairing, rather than an unspecified arrow between
+two matching five-term sequences, that constructs the isomorphism
+(5.11).  Its contravariance in \(F\) is precomposition in the Ext
+argument.
+
+For \(q>2\), the displayed Ext degree \(2-q\) is negative.  The
+derived Hom of the locally free sheaf \(F\), concentrated in degree
+zero, into the sheaf \(\omega_W\), concentrated in degree zero, has
+no negative cohomology.  Hence the duality theorem gives
+\(H^q(W,F)=0\).  This also follows directly from coherent
+cohomological dimension on the compact surface \(W\).
 \end{proof}
 
 \begin{proposition}[absolute duality on a compact Cartier fibre]
@@ -897,23 +893,96 @@ quotient $J^*$.  Thus
  \simeq h_j^*(L|_{J^*}).
 \tag{5.17l'''}
 \]
-The same $h_j$ is translation in flat coordinates by $\alpha v_j$, where
+The logarithmic overlap is the holomorphic translation
+\[
+ h_j[s,\zeta]=[s,\zeta+\alpha(s)\Pi(s)v_j],
+ \qquad \alpha(s)=\frac{\log s_j}{2\pi i}.
+\]
+To compute its effect on a real cohomology class, retain the exact
+real marking
+\[
+ \Xi(s,x+\Lambda)=[s,\Pi(s)x],\qquad
+ J_s=\Pi(s)^{-1}\circ i\circ\Pi(s)
+ \quad\text{on }\Lambda_{\mathbb R}.
+\]
+The period matrix \(\Pi(s)\) is a real isomorphism by (2.2)--(2.4);
+thus \(J_s\) is a well-defined smooth family of real complex
+structures.  On a branch of the logarithm the actual real
+translation vector is
 \[
- \alpha=\frac{\log s_j}{2\pi i}.
+ a_j(s)=\operatorname{Re}\alpha(s)\,v_j+
+        \operatorname{Im}\alpha(s)\,J_s v_j.
+ \tag{5.17m}
 \]
-For any constant vertical two-form, direct substitution gives
+Indeed, applying \(\Pi(s)\) gives precisely
+\(\alpha(s)\Pi(s)v_j\).  A different logarithm branch changes
+\(a_j\) by an integral multiple of \(v_j\), so its torus translation
+is branch-independent.  Complex multiplication by \(\alpha\) is
+not multiplication by a real scalar in this marking.
+
+Write \(E=\frac12\sum_{a,b}E_{ab}\,dx^a\wedge dx^b\) in the
+ordered real coordinates dual to the marked lattice; the matrix
+\((E_{ab})\) is alternating and is constant over the covering
+disc.  Direct substitution in the real map
+\(h_j(s,x)=(s,x+a_j(s))\) gives
 \[
+ \begin{split}
  h_j^*\Omega_E-\Omega_E
- =d\alpha\wedge\iota_{v_j}E.
-\tag{5.17m}
-\]
-Along a clockwise loop in the $s_j$-plane one has
-$\int d\alpha=-1$.  Thus the cross component contributed by (5.17m) is
-$-\iota_{v_j}E$.  The remaining cross component is precisely (5.17l),
-while the total class extends over the disc and has zero cross component.
-Therefore $N_{T_j}d_j-\iota_{v_j}E=0$, which is the first identity in
-(5.17k).  In $V_G$ every $T_j$ is the identity, so the norm becomes
-multiplication by $m_j$ and the second identity follows.
+  ={}&\sum_{a,b}E_{ab}\,d a_j^a\wedge dx^b\\
+    &+\frac12\sum_{a,b}E_{ab}\,d a_j^a\wedge d a_j^b.
+ \end{split}
+ \tag{5.17m'}
+\]
+The last term has both arguments in the base directions.
+In particular, it restricts to zero when the base is an oriented
+circle.
+
+Take one full clockwise circle in the \(s_j\)-cover,
+\[
+ s_j(\theta)=r e^{-2\pi i\theta},\qquad 0\le\theta\le1.
+\]
+Choose the logarithm continuously along that circle, so
+\(\alpha(1)=\alpha(0)-1\).  The endpoints represent the same
+point of the covering disc.  The marking is defined on the full
+disc, and therefore \(J_{s_j(1)}=J_{s_j(0)}\).  Consequently
+\[
+ a_j(1)-a_j(0)=-v_j.
+ \tag{5.17m''}
+\]
+For any \(\lambda\in\Lambda\), restrict (5.17m') to the sweep of
+the marked circle \(x(u)=u\lambda\), using the base-first
+orientation \(d\theta\wedge du\).  Its integral is exactly
+\[
+ \int_0^1 E\!\left(\frac{d a_j}{d\theta},\lambda\right)d\theta
+ =E(a_j(1)-a_j(0),\lambda)
+ =-E(v_j,\lambda).
+\]
+The horizontal term contributes zero.  Since marked lattice
+circles span \(H_1(F;\mathbb R)\), these integrals determine the
+mixed component in
+\[
+ H^1(S^1;\mathbb R)\otimes H^1(F;\mathbb R).
+\]
+Thus the mixed component of \(h_j^*\Omega_E-\Omega_E\) is
+\(-\iota_{v_j}E\), with \((\iota_{v_j}E)(\lambda)=E(v_j,\lambda)\).
+
+The pullback of the defect
+\(c_1(L|_{J^*})-[\Omega_E]\) has zero fibre component and mixed
+component \(N_{T_j}d_j\) by (5.17l).  Translation by \(h_j\) does
+not change this mixed component: on the covering circle such
+a fibre-zero class is represented by
+\(d\theta\wedge\beta\), with \(\beta\) a constant fibre one-form,
+and substituting \(dx\mapsto dx+d a_j\) adds only a base two-form,
+which vanishes on the circle.  Equations (5.17l'') and
+(5.17l''') state that the total pulled-back class extends over
+the covering disc and has zero mixed component.  It follows that
+\[
+ N_{T_j}d_j-\iota_{v_j}E=0.
+\]
+In the global coinvariants every \(T_j\) acts as the identity,
+so \(m_j\bar d_j=[\iota_{v_j}E]\).  This proves (5.17k), with the
+original clockwise convention and no change to either translation
+vector.
 \end{proof}
 
 \begin{lemma}[the cusp boundary defect and Chern-class specialization]

diff --git before/integral_leray.tex after/integral_leray.tex
index 1912f4b..caab0af 100644
--- before/integral_leray.tex
+++ after/integral_leray.tex
@@ -798,25 +798,76 @@ It splits the homotopy sequence over the pair of pants, giving
  \pi_1(f^{-1}(B^\circ))=
  \Lambda\rtimes F(\widehat\rho_1,\widehat\rho_2),
 \]
-with conjugation actions \(A_1,A_2\).  The clockwise meridian at \(p_j\)
-lifts to the affine generator in (2.9), including its sign and based
-translation.  Indeed, on a logarithm branch put
-\(\alpha=\log(s_j)/(2\pi i)\).  The overlap map \(h_j\) translates flat
-coordinates by \(+\alpha v_j\), so the inverse image of the period-family
-zero section is \(x(z)=-\alpha(z)v_j\).  Clockwise continuation takes
-\(z\) to \(g_jz\) and
-\(\alpha(g_jz)=\alpha(z)-1/m_j\).  Because \(A_jv_j=v_j\), the affine
-generator sends the initial point to
-\[
- A_j(-\alpha v_j)+v_j/m_j
-   =-(\alpha-1/m_j)v_j,
-\]
-exactly the continued endpoint.  Thus the based zero-section meridian is
-the affine generator, not its inverse or a translated conjugate.  Formula
-(2.8f) gives
+with conjugation actions \(A_1,A_2\).  The clockwise meridian at
+\(p_j\) lifts to the affine generator in (2.9), with its exact
+sign and based translation.  To verify this in the actual
+real marking, put
+\[
+ \alpha(s)=\frac{\log s_j}{2\pi i},\qquad
+ J_s=\Pi(s)^{-1}i\Pi(s),\qquad
+ a_j(s)=\operatorname{Re}\alpha(s)\,v_j+
+        \operatorname{Im}\alpha(s)\,J_s v_j.
+\]
+The overlap translation by
+\(\alpha(s)\Pi(s)v_j\) is translation by \(a_j(s)\) in the real
+marking.  Thus the inverse image of the period-family zero section
+is \(x(s)=-a_j(s)\).
+
+The covariance of \(J_s\) is a consequence of the proved period
+identity (2.8e), not an additional assumption.  That identity is
+\[
+ R_{g_j}(s)\Pi(s)=\Pi(g_js)A_j.
+\]
+The map \(R_{g_j}(s)\) is complex linear.  Hence
+\[
+ \begin{split}
+ J_{g_js}A_j
+ &=\Pi(g_js)^{-1}i\,\Pi(g_js)A_j\\
+ &=\Pi(g_js)^{-1}i\,R_{g_j}(s)\Pi(s)\\
+ &=\Pi(g_js)^{-1}R_{g_j}(s)i\,\Pi(s)
+ =A_jJ_s.
+ \end{split}
+\]
+The original vectors are
+\[
+ v_1=(1,2,-4,0)^{\mathsf t},\qquad
+ v_2=(-1,-3,3,0)^{\mathsf t},
+\]
+in the basis
+\((\widehat\gamma,\widehat u,\widehat w,\widehat\delta)\).
+Multiplication by the printed matrices gives
+\[
+ A_1v_1=(1,\,6-4,\,-6-2+4,\,-2+2)^{\mathsf t}
+        =(1,2,-4,0)^{\mathsf t},
+\]
+\[
+ A_2v_2=(-1,\,-3,\,6-3,\,-3+3)^{\mathsf t}
+        =(-1,-3,3,0)^{\mathsf t}.
+\]
+Thus \(A_jv_j=v_j\) exactly.  Clockwise continuation by \(g_j\)
+changes the chosen logarithm to
+\(\alpha(g_js)=\alpha(s)-1/m_j\).  Using this real change, the
+unchanged imaginary part, and \(J_{g_js}A_j=A_jJ_s\), one obtains
+\[
+ a_j(g_js)=A_ja_j(s)-v_j/m_j.
+\]
+Therefore the affine generator sends the initial lift of the
+zero section to its actual continued endpoint:
+\[
+ A_j(-a_j(s))+v_j/m_j=-a_j(g_js).
+\]
+Changing the logarithm branch by an integer changes the initial
+lift by an integer multiple of \(v_j\).  Such a translation
+commutes with the affine generator because \(A_jv_j=v_j\), so the
+endpoint identification does not introduce a translated conjugate.
+The fixed zero-section whiskers retain the based generator.
+After \(m_j\) clockwise iterations, the coordinate returns to the
+same point and \(\alpha\) has decreased by one.  Thus the endpoint
+of \(-a_j\) has increased by \(v_j\), in agreement with (2.8f).
+Consequently
 \[
  \widehat\rho_j^{m_j}=t_{v_j}.
-\tag{5.23b}
+ \tag{5.23b}
 \]
 The radial model of \cref{lem:finite-filling-stalk-map} shows that attaching
 \(N_j\) imposes exactly this relation.  Since the global and local whiskers
```

