# Common cusp result: precise move and replacement

Move the existing theorem `night:P1.9` (tag 02R0) to the section of common local conventions, before the integral eight-manifold. Its input is a bounded holomorphic matrix C(q), independently of the later global period construction. Use C=0 to build the smooth cusp initially. Place the two shared displays `maps:eq:E.4` (tag 029R) and `maps:eq:E.5` (tag 029S) here, each exactly once. Use C in the general action; the resolved fibre product specializes C to its explicitly defined C_3. Preserve those labels and hypertargets.

The published source cited by night:P1.9 is the direct local existence theorem. Thus the later global filling can cite night:P1.9 rather than maps:src:E.1.2. The source permits a bounded holomorphic correction with no symmetry requirement; the analytic checker is verifying this exact scope. The source's n=3 specialization and the identity of the period order/action must remain in the proof.

For the deformation comparison currently borrowed from maps:src:E.1.3, put the following numbered lemma immediately after the common local filling, assigning a new permanent tag through the series registry. A proof is supplied so that neither global construction depends on the other.

```latex
\begin{lemma}[Smooth dependence on the bounded cusp correction]
Let $C_t(q)$, $0\leq t\leq1$, be a smooth family of holomorphic
$3\times3$ matrix functions on a disc, uniformly bounded on a
smaller closed disc.  The marked Kuhn fillings with periods
$[I_3\mid (\log q/(2\pi i))I_3+C_t(q)]$ are diffeomorphic over
that smaller disc.  The diffeomorphisms preserve the central-fibre
strata and the marked angular and deck lattices.  They can be chosen
on the outer collar to extend a smooth marked trivialization of the
regular torus bundles.
\end{lemma}
\begin{proof}
The toric charts have coordinates $(z_0,z_1,z_2,z_3)$ with
$q=z_0z_1z_2z_3$.  Their changes of coordinates depend smoothly
on $t$ and are toric monomials multiplied by the holomorphic units
$\exp(2\pi iC_t(q)\lambda)$.  They therefore define a smooth
family of manifolds with the same coordinate-stratum charts.
The parameter vector field in each chart lifts $\partial/\partial t$,
fixes $q$, and is tangent to every coordinate stratum.  Differences
of these lifts are vertical fields with the same properties.
A partition of unity gives a global lift with these properties;
on an outer collar take the prescribed lift from the regular marked
torus bundle and use a partition subordinate to that collar and the
interior charts.

For $y=\operatorname{Im}(\log q/(2\pi i))$, uniform boundedness
of the corrections gives, after shrinking the disc,
\[
 \tfrac12\|\lambda\|\leq
 \|(I_3+y^{-1}\operatorname{Im}C_t(q))\lambda\|
 \leq\tfrac32\|\lambda\|,
 \qquad 0\leq t\leq1.
\]
The same fundamental-domain estimate as in the local filling theorem
therefore gives a proper family over the closed disc times $[0,1]$.
The lifted field has a flow for the entire parameter interval.
That flow fixes $q$, preserves each stratum, and has the specified
collar restriction.  Since the parameter interval is contractible
and the lattice marking is constant there, its induced lattice map
is the identity.
\end{proof}
```

This is an expanded proof of the deformation step already used in maps:src:E.1.3, not a change in the claimed smooth type. Interpolating C_t=tC identifies each correction with C=0. The finite-cap comparisons already printed in maps:src:F.3.7 identify their underlying real local-system torus bundles. This supplies the required smooth gluing comparison with no reference to the resolved fibre product.

## Exact edits in maps:src:F.3.7

- Replace `the fan \eqref{maps:eq:E.4} and the action \eqref{maps:eq:E.5} with C_3=C` by the shared equations now placed in night:P1.9; retain the references.
- Replace the paragraph beginning `The proof of Theorem \SeriesRef{maps:src:E.1.2} used only...` by: `The local filling theorem \cref{night:P1.9} applies to this bounded holomorphic correction.  It supplies smoothness, proper discontinuity and properness in the prescribed marking.  We glue with zero additional cusp translation.`
- Replace the last reference to the parameter fields and properness estimate in maps:src:E.1.3 by the new smooth-dependence lemma.
- Replace maps:src:E.1.2 step 4 by a direct invocation of the shared local theorem after its period matrix C_3 is defined. Its integral product-morphism calculation and crepant-resolution step remain in that theorem.
- Replace maps:src:E.1.3 step 4's bounded-correction homotopy argument by the same smooth-dependence lemma. Its polarization and spectral-sequence argument remain there.

## Homology merger

The statement `night:P1.12` is exactly the integral homology conclusion of `maps:src:F.2.6` for the holomorphic realization. Retain its label and tag as aliases at the surviving statement or a numbered corollary with a one-sentence proof by the local-model identification. A single combined theorem is the cleaner fit with the prompt's one-statement rule. Retain all existing aliases in the tag map and regenerate cross-paper references from the resulting number.
