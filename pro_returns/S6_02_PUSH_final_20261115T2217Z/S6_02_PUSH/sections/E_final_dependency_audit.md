# Final dependency and scope audit

**Verdict: PASS.** Classification_e, 15 November 2026. This audit covers the integrated B.4.24, B.4.27, B.4.30–33, their strengthened B.4.4 input, and the closing B.4.1/B.5.1/C.5.1 statements. The current source and registry rows were read. No shared master or main report was edited.

## 1. The proof dependencies are acyclic

| Result | Mathematical inputs actually used | Scope check |
|---|---|---|
| B.4.4 | R1's intrinsic bi-anticanonical pencil; Grauert coherence; the standard analytic base-change input audited in E.3.1; explicit proper graph and labelled critical-value argument | Requires a smooth dominating fourfold, not a reduced or semistable central divisor. E.3.1's base-change theorem is independent of the later deformation-closure and noncompletion results. |
| B.4.24 | The explicit closing C.3.5, affine section B.4.9, axial presentations B.4.18–19, and the specified KKN definitions/exact sequence | Constructs the fixed associated log torus and its nontrivial axial clutching. Does not assume that an arbitrary cap is a log torsor. |
| B.4.27 | B.4.24's period pairing; direct blowup/Picard/ghost cohomology; KKN base change | Proves H1(S,A)=0 for the specified sheaf after any permitted point blowups. Does not classify arbitrary caps. |
| B.4.30 | B.4.24/26/27; analytic log de Rham comparison; direct coefficient-ideal equidimensionalization; explicit local roots, subdivisions, norms and Hartogs | Its conclusion remains restricted to the prescribed partial filling. Its extending-section lemmas and constructions are proved before being reused in B.4.32–33; the final noncompletion conclusion is not assumed in those arguments. |
| B.4.31 | B.4.4, analytic resolution, compact branch-stratum transport, and the actual peripheral matrices | Starts from a hypothetical arbitrary proper filling and retains central multiplicities. Uses no B.4.30 or B.4.33 conclusion and no semistable-reduction theorem. |
| B.4.32 | B.4.31's integral meridians; the local saturation/primitive/chart-chain arguments of B.4.30; B.4.19's exact reference-origin overlaps; the quotient fixed-space calculation | Controls a normalized radial-loop class only. Does not assume bounded comparison with the old origin or invoke B.4.33. |
| B.4.33 | B.4.4/24/27/30/31/32 | Constructs the cap-derived torsor from multiplied trace differences, obtains a global origin, and derives the positive-integer contradiction. No existence or topology assertion in B.4.1, B.5.1 or C.5.1 is an input. |

The closing references from the scope paragraphs of B.4.24, B.4.27 and B.4.31 to the later results are explanatory forward references, not premises of their proofs. Likewise B.4.1 is deliberately stated before B.4.33 and proved by that later theorem. The dependency is one-way. C.3.5's “cusp filling” means the q-cusp neighbourhood inside an already constructed nonzero-parameter member; its explicit closing calculation does not assume an r-parameter filling.

## 2. No relative-dimension-three semistable reduction is hidden

An arbitrary proper filling is first reduced to its main component, normalized and resolved, unchanged over the puncture. Its smooth dominating fourfold is flat over the parameter because the parameter is a nonzero divisor. B.4.4 then extends the marked map, and its graph and central support are resolved with multiplicities retained.

B.4.31 directly treats the local equation r=x^a y^b and its higher-crossing analogues. The only semistable constructions in B.4.30, B.4.32 and B.4.33 occur near a generic boundary curve of a **two-dimensional base**, with a transverse parameter retained. Their transverse fibres are surfaces. After deleting the proper images of closed bad strata, the charts have t=product(x_i^m_i), with at most three factors. The height-one slice therefore has dimension at most two, where the stated lattice subdivision gives unimodular triangles. This is not a claimed semistable-reduction theorem for arbitrary threefold degenerations.

The external analytic input is IKN2005 Theorems 6.2–6.3, not its algebraic Hodge-degeneration Theorem 7.1. The original text and the erratum were checked; no Kähler or projectivity assumption is dropped. The equidimensionalization uses the reproduced Parusiński preprint argument. Enokizono–Hashizume Lemma 2.14 supplies analytic toroidal gluing; their projective main theorem is not used.

## 3. Roots, traces, and the whole modified base

The compact set K=beta^{-1}(0) includes the no-blowup case. Properness makes a finite neighbourhood cover of K cover the entire inverse image of a smaller bidisc. This supplies finitely many trace degrees. Resolution over a relatively compact neighbourhood supplies finitely many boundary multiplicities. A product of their common multiple with lcm(1,...,d_max) works for the **local transverse** covers; splitting is done before the final toric subdivision. No global root along an exceptional curve or the full marked P1 base is asserted.

Norms return multiplied differences to the original base. Other branch-curve intersections and meromorphic-lift indeterminacy occur at isolated points near the compact set. The Hartogs argument extends A-sections, using H1 of a punctured bidisc with constant Y coefficients equal to zero; it does not assert Hartogs extension of torsors. Unique section extensions preserve cocycles. Thus Q is constructed on all of S, rather than only near a generic exceptional divisor.

At the unknown strict r axis, B.4.31 supplies delta-only angular meridians. This gives exactly the bounded sheaf whose first character has zero r-order. The proof never replaces the rank-one monodromy kernel by a rank-two kernel. Along the actual q axis, the sigma comparison uses projection to the known fan and the finite-character norm, so an unproved global holomorphic lift of sigma is unnecessary.

The ordinary-to-rotating correction G(s)+6v delta is explicitly inserted before using sigma−o_rot=F. B.4.32 kills only the loop defect; common essential translations remain allowed. The final gamma evaluation is 0=Dn with D,n positive. All finite covers and norms preserve the nonzero sign-independent integer obstruction. The untwisted identity-closing family has F=0 and is therefore not excluded.

## 4. Closing statements and registries

B.4.24, B.4.27 and B.4.30–33 remain **Proved** with their respective scopes. The strengthened B.4.4 source and CSV both cover resolution of an arbitrary proper filling. B.4.1 and B.5.1 are correctly **Refuted** as proposed-object premises: no positive least filling exponent exists, and the requested central topology and nearby-cycle data are undefined, not zero. Their registry rows agree with the source.

C.5.1 is also correctly **Refuted** for the specified analytic filling premise. It refuses to assign c1, c2, p1, relative lifts, intersection form or characteristic numbers to that nonexistent analytic object. It retains the proved actual smooth monodromy [Phi]=0 and the two stated determinations through C.3.24 and C.3.25–27. Those smooth arguments do not depend on B.4.33 or on the existence of an analytic parameter filling. Their shared annular characteristic inputs and distinct boundary-invariant arguments are stated accurately.

Finally, C.5.1 explicitly distinguishes the constructed smooth spin-c eight-dimensional coboundary from the nonexistent analytic W. It neither asserts an almost-complex structure on that smooth coboundary nor identifies its determinant class with the first Chern class of an almost-complex tangent bundle. No scope error or circularity was found in these closing statements.
