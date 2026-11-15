# Independent referee of C.3.14

Date: 2026-11-15. Referee: boundary_d. Source reviewed: `sections/C_characteristic_cap.tex`, as present during the draft11 build. **Verdict: the proposition is proved in its stated scope.** In particular, it supplies a specified characteristic-number target for the actual six-loop monodromy; it does not evaluate that number or resolve the comparison of orientation conventions.

## Actual cap comparison

The equivariant linearization uses the known smooth orbit pair, the trivial scalar normal rank-two complex bundle over the fixed sphere, and classification of the free principal circle bundle by its signed primitive Euler class. The boundary gauge has a real logarithm because the common boundary has vanishing first integral cohomology; its extension with a collar cutoff makes the two isomorphisms agree. This is sufficient and does not use a false general assertion that arbitrary orbit diffeomorphisms lift smoothly at fixed points.

The cap is the surgery manifold of the actual orbit knot. Each of the two orbit six-discs, with its standard fixed three-disc neighbourhood removed, gives `S2 × D4` with distinct inner and outer `S2 × D3` faces. Gluing the outer faces by the actual relative diffeomorphism gives the knot exterior. Surgery attaches a third such piece along its inner faces. Combining that third piece with either original piece along the inner product face yields another `S2 × D4`; the remaining gluing is the extension of the actual relative diffeomorphism by the identity on the other half. Thus the displayed double is the required cap with a specified framing, rather than an abstract six-manifold with matching homology.

The Mayer–Vietoris, van Kampen, spin, and twisted spin-index arguments are valid. In particular, restriction in degree two is injective over both the integers and the field with two elements. The characteristic integer is

\[
J=(\langle p_1x,[M]\rangle-4\langle x^3,[M]\rangle)/24,
\]

and integrality follows directly from the index theorem, independently of six-manifold classification.

## Primary-source formula check

Wall's original Theorem 4 on page 360 was inspected visually, not merely through OCR. It states

\[
\mu(e_i,e_i,e_i)=6\varphi_i+\beta'_i,
\qquad p_1(e_i)=4\beta'_i.
\]

The proof on page 361 identifies the stable **tangent** bundle class and explains the signs. Therefore the subtraction defining `J` gives `J = −φ` exactly in that convention. The 1967 corrigendum changes Theorem 14, not Theorem 4. The source's retained fixed sign for comparison with the Davis/Eells–Kuiper generator is appropriate; this referee has not computed that sign.

* Wall, C. T. C. (1966). Classification problems in differential topology. V. On certain 6-manifolds. *Inventiones Mathematicae, 1*, 355–374. Original PDF: <https://webhomes.maths.ed.ac.uk/~v1ranick/papers/wclass5.pdf>.
* Wall, C. T. C. (1967). On certain 6-manifolds: Corrigendum. *Inventiones Mathematicae, 2*, 306. Primary PDF: <https://link.springer.com/content/pdf/10.1007/BF01425407.pdf>.
* Local visual audit: `external_sources/C_independent_primary/Wall1966V_ocr/page_06.png` and `page_07.png` (original pages 360–361); the text was compared with the image because the OCR corrupts several symbols.

## Framing and scope

The pure framing generator is represented on the relative orbit complement by a map to `SO(3)`. Its lift to `SU(2)` exists on the three-disc with prescribed identity near the boundary. Left quaternionic multiplication then gives an equivariant lift commuting with the right complex circle and extending over the seven-disc. Thus that direction maps to zero in `Theta_7`, as asserted.

The formula relating the actual six-loop clutching sphere to `J` is consequently valid with the stated fixed orientation sign. Nothing in this verification computes `J`, `k`, or a numerical monodromy class. The classical target-knot self-linking 12 and local normal Euler value −2 remain insufficient to do so without the actual global gluing calculation.

One optional terminology clarification, requiring no mathematical correction: the phrase “first Pontryagin number is six” in the discussion of the Milnor sphere refers to the evaluation of the associated oriented rank-four bundle's first Pontryagin class on `S4`, not to a Pontryagin number of a seven-manifold.
