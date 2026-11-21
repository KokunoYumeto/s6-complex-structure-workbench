# Exact consolidation passages for Paper V

These changes remove repeated proofs while retaining all mathematical conclusions. All theorem/equation labels and tag hypertargets mentioned below must remain exactly once in the surviving source. No new computational or mathematical hypothesis is introduced.

## 1. The integral homology proof, torsion step

In the proof of `maps:src:F.2.6`, replace the part of item 5 from “We compute the torsion differential on the boundary” through “The coefficient is one because the loop t has degree one over the coarse-base circle” by the following. Keep the existing explicit representatives, detecting rows, and witnesses following it, from “For k=1,2,3 ...” through the end of that item, exactly once.

```latex
\item The boundary comparison in
\cref{mapsaudit:order-four-torsion-transgression} gives
\[
 d_2[w]=\pm[w]\in L_{q-1}/\operatorname{im}\Delta_{q-1}.
 \hypertarget{tag-02FA}{}\label{maps:eq:F.6}
\]
Here $[w]$ is a torsion suspension class of the order-four
mapping torus, and its image on the right is induced by the
marked vertical inclusion into the six-dimensional fibre.
We now evaluate this homomorphism on the three local generators.
```

Use the paper's new automatic equation environment rather than the literal display markup above, so the existing equation label has an actual number. The geometric coefficient-one argument occurs only in the transgression lemma. The matrices proving the global image is nonzero occur only here. The lemma's final proof item should refer to these explicitly identified integer matrices, without re-displaying or re-proving their identities.

The local comparison lemma's statement includes its three global nonvanishing conclusions. Its proof may point to these finite matrix identities, but must not appeal to the integral-homology conclusion. The logical input is the explicit relation matrix, not the theorem being proved. Placing the finite restriction and coinvariant calculation before the local lemma, as a numbered preparatory lemma, makes this dependence entirely forward-free.

## 2. Remove the rational homology calculation from the smooth construction

The complete rational restriction calculation in item 3 of `maps:src:F.2.5` is obtained by tensoring the integral stalk complex of `maps:src:F.2.6` with Q. Its independent determinant tables should go to the checks, not remain as a second proof. Keep construction and van Kampen exactly once in F.2.5. Keep the almost-complex extension argument exactly once there, as it is needed for the generic input classification F.2.30 even when no compact integrable periods are claimed.

To avoid using the deleted rational calculation in F.2.6, replace its final item after the sentences proving H^3=0 and H^4=Z^4 by this self-contained deduction:

```latex
The degree-one row of the same Leray sequence is
\[
 H^0(\mathcal R_1)=\mathbb Z
 \xrightarrow{d_2^{0,1}}
 H^2(\mathcal R_0)=\mathbb Z.
\]
Its kernel is $H^1(M;\mathbb Z)$, which vanishes by simple
connectivity.  Hence it has nonzero degree and is an
isomorphism after tensoring with $\mathbb Q$.
The displayed sheaf groups now give
$H^2(M;\mathbb Q)=H^3(M;\mathbb Q)=0$.
The universal coefficient sequence identifies the torsion of
$H_2(M;\mathbb Z)$ with the $\operatorname{Ext}$ subgroup of
$H^3(M;\mathbb Z)$ and the torsion of $H_3(M;\mathbb Z)$
with the $\operatorname{Ext}$ subgroup of $H^4(M;\mathbb Z)$.
Both subgroups vanish.  Their rational ranks also vanish,
so $H_2(M;\mathbb Z)=H_3(M;\mathbb Z)=0$.
Integral Poincar\'e duality then gives precisely the displayed
homology groups.  Hurewicz applied successively gives
$\pi_2(M)=\pi_3(M)=0$.
```

The fact H^0(R1)=Z follows from the already computed H^0(S1)=Z and zero degree-one stalk kernel; R0=Z follows from connected fibres. This does not use any conclusion of the deleted rational proof. The only input from the smooth construction is its construction, orientation and simple connectivity.

The characteristic-number calculation currently repeated in item 5 of F.2.5 is exactly `night:P1.13`; retain that one proof. The construction theorem can state its topological/characteristic consequences with references to the surviving integral homology and characteristic-number results, or its theorem label can be attached to a combined final conclusion. A construction definition with all marked matrices and caps is preferable before the proof chain, so later results refer directly to its data rather than to consequences inside a proof.

## 3. Compact realization: use the established smooth model

The last item of `night:P1.10` repeats the full van Kampen calculation. Replace it by:

```latex
\item The finite affine actions, the marked Kuhn cusp and the
punctured overlap maps are those of
\cref{maps:src:F.2.5}.  The bounded-correction comparison and
the fixed real local-system marking identify the underlying
smooth fillings, including their collars.  The construction
therefore has the fundamental group and integral homology
of \cref{maps:src:F.2.6}.  In particular its fundamental
group is trivial and its Euler number is six.
```

The stronger consolidation is to merge `night:P1.10` into `maps:src:F.3.7` by preserving both labels/tags on the single compact-realization theorem and adding the specified parameter range to its statement. The evaluations, finite root quotients, logarithmic translations, cusp model and proper gluing are already proved there. Its final item should cite the established topological theorem as above, without another van Kampen presentation.

## 4. Merge E.1.3 with P1.11: exact statement and dual specialization

Add tag `02M6` and label `maps:src:E.1.3` beside tag `02QK` and label `night:P1.11` on the surviving early cusp theorem. The identification is the marked dense-torus identity with the same Kuhn fan and bounded correction, already supplied by the common local filling theorem. Thus the fibre called W_3 in the resolved-product construction is this same C, with C specialized to its matrix C_3.

In the surviving statement, number its homology rank display and attach tag `029T` and label `maps:eq:E.6`. After the collapse assertion append:

```latex
Dually, the specialization
\[
 \kappa^*:H^k(C;\mathbb Z)\longrightarrow
 H^k(T^6;\mathbb Z)
\]
has image equal to the full monodromy-invariant lattice.
Its kernel is zero except in degree four, where it is
isomorphic to $\mathbb Z$.
```

Append this final proof item to P1.11 after the primitive collapse/kernel argument:

```latex
\item Every homology group just computed is free, so the
universal coefficient maps identify cohomology with the
integral duals of homology.  The transpose of the collapse
therefore has image
\[
 \operatorname{im}\kappa^*
 =\operatorname{Ann}(\ker\kappa_*)
 =\operatorname{Ann}\bigl(
   (\bigwedge^k M_0-I)\bigwedge^k\Lambda\bigr)
 =\ker\bigl((\bigwedge^k M_0)^t-I\bigr).
\]
The first equality uses the primitive image of $\kappa_*$:
an integral functional on that image extends to the free
central-fibre group.  Passing from the monodromy image to
its saturation does not change its annihilator, which gives
the second equality.  The last group is the full integral
cohomology invariant lattice; using inverse transpose gives
the same fixed subgroup.  The kernel of $\kappa^*$ is the
integral dual of $\operatorname{coker}\kappa_*$, which is
$\mathbb Z$ in degree four and zero otherwise.
```

Delete the later E.1.3 theorem and its second homology proof. Preserve that whole independent branch-resolution/line-bundle proof in the check file. This mathematically proves every assertion of both statements in one proof.

## 5. Preserve E.7 as a numbered mathematical remark

The E.7 normalization table contains an additional description of the branch resolution, so retain it once in a numbered remark immediately after the common cusp proof. The original ray/restriction recipes (E.1.3 proof items 1–3) specify its maps and can be retained concisely there. It should not run a second homology/specialization proof. A precise comparison paragraph is:

```latex
The branch resolution and the moment-cell complex are linked
by the following augmentation.  Over a dual cell $D_\eta$
of the Kuhn decomposition, every branch-intersection term
has angular lattice $Q_\eta=\mathbb Z^3/L_\eta$.
Its branch indices form the simplex on the vertices of
$\eta$.  Tensor the augmented integral simplex chain
complex with $\bigwedge^qQ_\eta$ and sum over the dual
cells.  The degree-zero augmentation adds the branch
coefficients, and all higher branch terms map to zero.
The cellular incidence maps are the quotient maps
$Q_\eta\to Q_\tau$ for cofaces $\tau\supset\eta$;
they commute with this augmentation.  Each augmented
simplex complex is exact, with contraction given by
inserting its least vertex.  The resulting augmentation
is therefore a quasi-isomorphism to the moment-cell
complex used in the proof above.  Taking cohomology of
the compact toric branch intersections first instead
gives the following normalization table.
```

Then keep E.7 with tag 029U and label maps:eq:E.7, and its exact three-ray restriction and curve-degree rules. This records a concrete morphism between the two complexes. The complete second calculation, its spectral-sequence purity argument and line-bundle generators of invariants belong in the check file, as an independent check of the single printed proof.

The branch remark's table and ranks were already in the source; the new comparison states the augmentation that identifies its underlying cellular resolution. It does not infer the individual branch differential ranks merely from the final homology ranks.
