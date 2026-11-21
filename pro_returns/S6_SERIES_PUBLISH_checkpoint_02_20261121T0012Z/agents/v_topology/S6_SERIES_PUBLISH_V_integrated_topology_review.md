# Integrated topology-chain review of Paper V

Source reviewed: `work/S6_SERIES_PUBLISH_V.tex`, the root's integrated stage-one rewrite, on 20 November 2026. This is a post-edit read, not a pre-proof derivation. The independent arithmetic remains in the earlier scripts and outputs. No main-file edit was made by this agent.

## Mathematical result

The main chain is sound after the relocations. The marked smooth construction supplies simple connectivity, Euler number six, and an almost complex structure without using the global period calculation. The common cusp theorem supplies exactly the free stalk and primitive-image statements needed by the restriction complex. The finite signed-orbit restriction maps give the stated image sheaves and point kernels. The separately placed transgression argument has coefficient one and sends each of its three torsion classes to the nonzero global class. The final Leray/UCT/duality/Hurewicz deduction correctly gives three-connectivity and free homology of ranks 1,4,1. The new characteristic-number proposition then supplies signature two and the odd middle form. The existing characteristic-vector descent and exact normal-clutching comparison supply the smooth classification.

No new mathematical discrepancy was found in that chain. There are exact references and notation to repair after the moves, and one mathematical construction used later in the paper must be retained.

## 1. A later dependency requires retaining the support-function construction

In `maps:src:E.2.5`, the first proof item still invokes the support-function construction of `maps:src:E.1.3` in two coordinates. That construction was in the deleted second cusp proof. Its line-bundle calculation supplies the two-dimensional integral invariant cycles and is not supplied by the three-dimensional homology statement alone.

Retain the following mathematical passage as a separately numbered lemma or remark near the shared cusp result, with a new permanent label/tag chosen by root. Retarget the reference in E.2.5 to it. This preserves the unique construction without restoring the duplicate homology proof. In this passage n is two or three, and the fan is the standard n-dimensional periodic Kuhn fan.

```latex
\begin{lemma}[Integral degree-two classes on the Kuhn filling]
For the Kuhn filling with bounded correction zero, in dimension
$n=2$ or $3$, every integral symmetric matrix $S$ gives a line
bundle whose Chern class on a smooth fibre is
$\sum_{i,j}S_{ij}a_i\wedge b_j$.
Here $a_i$ are the angular classes and $b_i$ the invariant deck
classes in the marked product description.
\end{lemma}
\begin{proof}
At a fan vertex $m\in\mathbb Z^n$ put
\[
 q_S(m)=\frac{m^tSm-\sum_iS_{ii}m_i}{2}.
\]
This is integral because $m_i^2-m_i$ is even. Its interpolation
on each unimodular Kuhn simplex is an integral piecewise-linear
support function. Translation by $\lambda$ changes it by
the integral affine function
$m^tS\lambda+q_S(\lambda)$.
The Cartier data therefore have deck linearization
\[
 q^{-q_S(\lambda)}x^{-S\lambda}.
\]
The identity
$q_S(\lambda+\mu)=q_S(\lambda)+q_S(\mu)+\lambda^tS\mu$
is its cocycle condition under $x\mapsto q^\mu x$.
On the smooth fibre these factors of automorphy have Chern
class $\sum S_{ij}a_i\wedge b_j$. Restriction to the central
fibre consequently supplies the corresponding specialization
classes. The marked collapse also supplies the deck classes
$b_i$. The bounded-correction comparison transports these
integral cohomology classes and the specialization map.
\end{proof}
```

The exact cocycle computation is
`f_lambda(q^mu x) f_mu(x) = q^(-q_S(lambda)-q_S(mu)-mu^t S lambda) x^(-S(lambda+mu)) = f_(lambda+mu)(x)`.
The angular/deck convention fixes the Chern-class sign; the same convention was used in the original source passage. No positivity or polarization is claimed for a general symmetric S.

For the actual two-dimensional use in E.2.5, the invariant degree-two basis is `b1 b2, a1 b1, a2 b2, a1 b2+a2 b1`. The products `(a1 b1)b2` and `(a2 b2)b1` generate degree three, and `(a1 b1)(a2 b2)` generates degree four up to its exterior-order sign. Every coefficient is a unit. Thus the existing E.2.5 argument still has its explicit integral basis proof once the retained construction is cited.

## 2. State the restriction lemma with all its objects and kernels

The PV12 result is correct, but its statement currently refers to image sheaves before defining the map and uses “groups computed below” for the kernels. The following replaces just its statement; preserve its label and tag.

```latex
Let $f:M\to S^2$ be the map of the marked smooth gluing in
\cref{pub:V:smooth-gluing}, and let $j:U\hookrightarrow S^2$
be the complement of its three special values $p_1,p_2,p_0$.
Put $\mathcal R_q=R^qf_*\mathbb Z$,
$\mathcal L_q=\mathcal R_q|_U$,
$\mathcal S_q=\operatorname{im}(\mathcal R_q\to j_*\mathcal L_q)$,
and $\mathcal K_q=\ker(\mathcal R_q\to j_*\mathcal L_q)$.
The fibres are connected, so $\mathcal R_0=\mathbb Z$.
For $1\leq q\leq4$ the image sheaf has
$H^2(S^2,\mathcal S_q)=\mathbb Z/2$; its only nonzero groups
in base degrees zero and one are
$H^0(S^2,\mathcal S_1)=\mathbb Z$ and
$H^1(S^2,\mathcal S_3)=\mathbb Z^3$.
Writing $i_a:\{p_a\}\hookrightarrow S^2$, its kernels are
\[
\mathcal K_1=0,\qquad
\mathcal K_2=\mathcal K_3=(i_2)_*(\mathbb Z/2),\qquad
\mathcal K_4=(i_2)_*(\mathbb Z/2)\oplus(i_0)_*\mathbb Z.
\]
For $q=2,3,4$, the torsion suspension generator at $p_2$ has
nonzero image in the global coinvariant group of
$\mathcal L_{q-1}$.
```

Use the coefficient stalk `L_q=bigwedge^q Z^6` in the explicit matrix calculation while reserving `mathcal L_q` for the local system. At present the same `L_q` is used as both without an explicit identification. The degree-one zero kernel follows directly from the mapping-torus complex: its suspension group is Z and the norm in degree zero is multiplication by the nonzero affine order; it is injective. Thus `H^0(R1)=Z`, used in the final proof, is justified integrally. The `R0=Z` statement follows from all fibres being connected.

PV12 proof item 1 currently cites F.2.5 and describes vectors printed in item 1 of its proof. That proof has moved and no longer contains those vectors. Replace its opening by:

```latex
\item Use the marked smooth gluing of
\cref{pub:V:smooth-gluing}, the matrices and affine vectors of
\cref{pub:V:rank-six-data}, and the integral cusp-collapse maps
of \cref{night:P1.11}. The matrix $S$ is the explicit integral
marking in the first proof item of \cref{night:P1.1}.
Write $m_1=5$, $m_2=4$, and put ...
```

The remainder of the finite mapping-torus and integral determinant proof is unchanged. Its three global torsion witnesses now precede the transgression theorem and do not rely on the final homology result.

## 3. Exact checks of the final Leray deduction

The kernels at q=2,3,4 are respectively Z/2, Z/2, and Z plus Z/2. The first two d2 maps are isomorphisms to their Z/2 targets. On the last source the torsion summand maps isomorphically; for the free generator image epsilon its kernel consists of `(n,n epsilon)`, a free rank-one group. Therefore total cohomology degree three vanishes and degree four has two free graded groups of ranks one and three.

In total degree one, `ker(d2^(0,1):Z->Z)=H1(M;Z)=0` uses simple connectivity of the separately proved smooth gluing. Hence that differential is a rational isomorphism. Together with the explicitly computed image sheaf groups this gives rational H2=H3=0. The integral UCT identifies torsion H2 with Ext in cohomology H3, and torsion H3 with Ext in cohomology H4; these vanish. Thus H2=H3=0 integrally. Integral duality gives the remaining ranks and vanishing, and successive Hurewicz gives pi2=pi3=0. This deduction contains no use of the removed rational Betti calculation.

The dual specialization added to P1.11 is also exact: freeness and primitive image give `im(kappa*)=Ann(ker(kappa_*))`; annihilating a subgroup is equivalent to annihilating its saturation. The fixed lattice of the transpose equals the fixed lattice of the inverse transpose. Its kernel is the dual of the free collapse cokernel. The complete conclusions of E.1.3 and P1.11 are preserved by this single proof.

## 4. Further exact reference and notation repairs

- The early `maps:src:F.2.1` is already before the smooth construction. Its statement still points forward to `def:admissible`. Replace “Under the index-one condition of ...” by “Let $N=M_0-I$ satisfy $N^2=0$, $\operatorname{rank}N=3$, and let $\operatorname{im}N$ be primitive in $\Lambda=\mathbb Z^6$.” Its proof already proves precisely this assertion.
- Define `Lambda=Z^6` explicitly in the marked datum, rather than relying on its prior use inside the main-theorem-F statement.
- In the statement of `night:P1.9`, specify that C(q) is a holomorphic three-by-three matrix on a disc, bounded after shrinking, and put `s=log(q)/(2pi i)` on its universal cover. These objects were previously defined in the period section and are now used earlier.
- In PV11's first proof item choose the cusp correction C=0 explicitly. The smooth-dependence lemma then identifies every later correction with this initially defined smooth gluing.
- In P1.11's product-to-quotient proof item, replace “the ... formula in step 9” by “the ... formula in the following item.” The following item is the Alexander–Whitney formula; the added duality item is now item 9.
- In F.3.7's cusp proof item the phrase “with C3=C” is stale: the shared E.5 action now uses the generic C. State the specialization `(q,C)=(q,C_new)` in the displayed target marking, or simply refer to its bounded correction there.
- The merged compact theorem no longer introduces the symbol M_c later used in P1.13 and the deformation discussion. Introduce M_xi for the parameter in P1.8 and state the c-real subfamily convention explicitly, in agreement with the analytic agent's normalization and parameter map.
- The transgression lemma's `StatementRecord` still lists F.2.5 and F.2.6 as dependencies. Its mathematical proof now uses PV02 and PV12, not the final integral theorem. Update the dependency record accordingly. Its reference to the later equation F.6 is an equation locator, not a proof input; assigning that equation in the transgression statement itself would remove even that forward display reference while retaining the exact anchor once.
- The compact theorem's `StatementRecord` still lists the resolved-product E.1.2 and final F.2.5/F.2.6 as dependencies. Update it to the actual early shared-cusp and period inputs, otherwise the metadata records a circular or obsolete chain despite the corrected prose.

## 5. Remove the remaining repeated characteristic-number derivation

P1.13 still rederives Todd integrality, the signature equation and the classification of the rank-four form already proved in the new `sec:V-known-inputs` proposition. Retain its Chern-root identities, spin/Wu argument, and explicit characteristic-vector descent. Replace the first proof item and the opening of the second by:

```latex
\item By \cref{night:P1.12}, the integral groups in degrees two
and six vanish, so $c_1=c_3=0$.
The proposition \cref{sec:V-known-inputs} gives
$c_4[M_c]=6$, $c_2^2[M_c]=2$, $\sigma(M_c)=2$, and the
integral middle form $I_{3,1}$.
The Chern-root identities
$p_1=-2c_2$ and $p_2=c_2^2+2c_4$ then give
$p_1^2[M_c]=8$ and $p_2[M_c]=14$.
\item Since $H^2(M_c;\mathbb Z/2)=0$, its $w_2$ is zero.
```

Continue the second item with the original `w4=c2 mod2=(p1/2) mod2` and characteristic-norm argument, then retain the full integral reflection descent exactly once. In F.4.1 the repeated Hurewicz and parity explanation can be shortened to citing those proved conclusions; retain the full normal clutching morphism and oriented absorption argument, which contain the actual smooth classification data.

## 6. Retarget later references to moved proof content

The following are exact content references affected by the merger, not merely optional cross-reference style:

| Existing occurrence | New target or explicit replacement |
|---|---|
| F.2.16 identifies its v=0 matrix pair with F.2.5 | `pub:V:rank-six-data` |
| F.2.18 first matrix A “as in F.2.5” | `pub:V:rank-six-data` |
| F.2.18 relative almost-complex extension “in F.2.5” | `pub:V:smooth-gluing` |
| F.2.24 cusp normal closure “by F.2.5” | `pub:V:smooth-gluing` |
| F.2.24 invariant-two-form computation “in F.2.6” | `pub:V:integral-restrictions` |
| F.2.30 pair-of-pants extension “as in F.2.5” | `pub:V:smooth-gluing` |
| F.2.32 original-datum normal closure “proved in F.2.5” | `pub:V:smooth-gluing` |

In F.2.18, the sentence “rational exterior invariant and parabolic ranks are exactly the table there” should point to the retained explicit restriction computation and identify its intended groups. Its later Chinese-remainder sentence can replace the lost reference by the actual map: the invariant degree-one covector has residues `(1 mod5,-1 mod4)` in the two finite cokernels, and the map from Z onto `Z/5 plus Z/4` is surjective because 5 and 4 are coprime. No second long proof is needed.

In F.2.30 replace “Since H2=0, p1/2=-c2 is primitive, characteristic, and has square two” by the exact implications: H2=0 gives c1=0 and w2=0, so p1/2=-c2; the spin Wu identity gives its characteristic parity, and its square is two. A nontrivial integer multiple of a lattice vector has square divisible by the square of that integer, so the norm-two vector is primitive. This makes the stated reason precise.

## 7. Front-matter dependency updates

The dependency figure/table still has the old A-to-D arrow justified by E.1.2 supplying the cusp filling. The new shared local theorem supplies that input independently before both constructions. Remove the obsolete arrow/row or explicitly describe the common body input without presenting A as a prerequisite. The B-to-C row currently names the merged integral theorem as the source of the matrices; name the marked datum and monodromy theorem there instead.

The main B proof outline still refers to F.2.6 items 1–4, item 5, and item 6. The merged F.2.6 proof is no longer numbered that way. Retarget its restriction step to PV12, its local torsion step to the transgression lemma plus PV12's witnesses, and its final integral conclusion to the merged theorem. Retarget the van Kampen step to PV11 and the characteristic-forcing step to the new proposition. Preserve the outline step anchors.

These repairs are required before calling the integrated rewrite fully checked. The underlying mathematical deductions reviewed above agree with the independent computations.

## Guarded implementation and additional exact check

The exact proposals are in `S6_SERIES_PUBLISH_V_topology_guarded_patch.json`, generated by `S6_SERIES_PUBLISH_V_make_topology_patch.py`. Its 39 per-edit old-string guards were all unique and applied successfully in memory. Existing labels and tag hypertargets were compared with multiplicity before and after; all are preserved. The new lemma has label `pub:V:cusp-chern-generators` and tag `PV13`. The main file was not edited by this script. The common-deformation lemma is generalized to n=2,3 with a sufficiently small common disc, as verified against Yang by the analytic agent. Front matter and the analytic F.3.7/parameter naming edits are deliberately excluded from this patch.

The restored Chern-class sign received an independent analytic check: in z=u+s v coordinates the Hermitian norm stated in the patch has the exact automorphy rule and Chern form sum Sij du_i wedge dv_j. The metric is positive for every real symmetric S because it is an exponential; no positive-definiteness or polarization hypothesis is being introduced.

The fresh program `S6_SERIES_PUBLISH_V_cusp_invariant_generators.py`, with complete output in the corresponding `.out`, independently forms every product of the odd deck generators and the symmetric degree-two Chern generators up to top degree. It compares those columns against a full integral Smith kernel of each exterior monodromy operator. For n=2 the invariant ranks are (1,2,4,2,1); for n=3 they are (1,3,9,9,9,3,1). Every nonzero Smith factor of the comparison is one. This validates the exact integral generation used by the restored two-dimensional argument and the corresponding original three-dimensional construction. It does not certify the rest of the shifted-product theorem.

Eight new post-edit/proposed-passage verification events are recorded in `S6_SERIES_PUBLISH_V_integrated_topology_CHECK_EVENTS.tsv`. Their outcomes distinguish these actual reads and computations from pre-proof checks and final rendered-page reading. One patch-generator guard initially failed because the checker string had lost a literal TeX accent backslash; the string was corrected and the complete sequential guard validation then passed. This was a checker-string issue, not a mathematical manuscript error.
