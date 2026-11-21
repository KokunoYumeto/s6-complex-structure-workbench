# Paper V topology and classification checks

Status: completed for the scope below against the attached corrected source. Final rewritten source comparison remains a separate check.

## Findings

No error in the paper was found in the checked monodromy arithmetic, integral Leray calculation, cusp cellular calculation, characteristic numbers, or smooth-classification chain. The two required third checks, `maps:src:F.2.28` (tag 02NI) and `maps:src:F.2.30` (tag 02NL), agree with derivations written before reading their proof bodies. The explicit source and computation records below delimit each conclusion.

## Independent exact computations

`S6_SERIES_PUBLISH_V_exact_topology.py` transcribes the displayed A, B, S, v1, v2, C1, C2 and constructs exterior powers by minors. It uses full integer Smith transformations to compute invariant lattices, norm-image lattices, the kernels of the global relation maps, and the quotient by stalk relations. This uses neither the earlier checking code nor its selected determinant minors. Results:

- Finite linear orders 5,4; the printed characteristic polynomials; cusp square-zero rank three with Smith factors 1,1,1; both cap markings and the cusp marking are unimodular.
- Homology global coinvariants Z and cohomology global coinvariants Z/2. The common homology fixed lattice is zero and the common cohomology fixed lattice has rank one. Every nonidentity affine power is obstructed from fixing a point by the displayed primitive covector.
- The simple-connectivity presentation has determinant -1. The two finite caps have H1=Z^2 and Z^2 plus Z/2.
- The sheaf groups in degrees q=1,2,3,4 are respectively (H0,H1,H2)=(Z,0,Z/2),(0,0,Z/2),(0,Z^3,Z/2),(0,0,Z/2), all H1 torsion-free.
- Automatically chosen generators of the local order-two torsion, obtained from Smith transformations rather than copied from the paper, have zero norm and map to the nonzero global order-two coinvariant in each of vertical degrees 1,2,3.
- The pencil discriminant is lambda^15(3125lambda+256), and the unique nodal root at lambda=-256/3125 is x=64/625. Both root substitutions and their Hodge line degrees agree.
- The reflection matrix is an integral isometry squaring to the identity; the quaternionic clutching map and its inverse agree.

`S6_SERIES_PUBLISH_V_cusp_cellular.py` generates the six Kuhn tetrahedra and all faces modulo Z^3, then computes quotient lattices by complete Smith transformations. It reconstructs 26 simplex classes and 74 codimension-one incidences. All compositions vanish. The integral E2 ranks, in rows q and columns base degree d, are

| q / d | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| 0 | 1 | 3 | 3 | 1 |
| 1 | 0 | 6 | 8 | 3 |
| 2 | 0 | 0 | 7 | 3 |
| 3 | 0 | 0 | 0 | 1 |

Every E2 group is free. The only supported higher differential starts at the base fundamental class, which survives through the angular identity section. The program separately forms the Alexander–Whitney/Poincare-duality collapse maps and computes their integral Smith forms. All nonzero factors are one; the sole graded cokernel is Z at (d,q)=(2,2). Thus the central homology ranks are (1,3,9,9,10,3,1), the collapse image ranks are (1,3,9,9,9,3,1), and the only collapse cokernel is Z in degree four. The image ranks agree with the exact monodromy coinvariant ranks. The paper's block-triangular unit-pivot argument therefore proves primitivity for the full filtered collapse map.

`S6_SERIES_PUBLISH_V_required_exact.py` verifies the determinant 20kappa+4r1+5r2, the two twist-gauge identities, the vertical norm identity, and the characteristic-number forcing used for every retained classification datum.

## B: geometric and integral proof comparison

The finite-cap mapping-torus model explicitly specifies its map to the coarse base: q=W^m exp(2pi i theta). In the order-four boundary the basis change (v,t)=(g^4 h^-1,g) has determinant one. A torsion prism representative pulls back to (Nw,w)=(0,w), so its base component has coefficient one. The relative-base connecting map is therefore the stated Leray differential on the global coinvariant class. The new Smith computation verifies that this class is nonzero in each relevant degree. The three torsion differentials and the free cusp generator give H3=0 and H4=Z^4. Together with pi1=0, universal coefficients and duality give the integral homology and three-connectivity.

The central-fibre moment-map model and the collapse marking in `night:P1.11` have been read against the source. The explicit face quotient map sends [(a,k)] to a-kv0 modulo L_sigma; its inverse sends a to [(a,0)]. The toric gluing identifies the shared character functions and positive sections, and the period-translation map preserves the component marking. These are the actual morphisms needed for the product-to-quotient topological model. The independent cell reconstruction verifies its finite integer calculation. The analytic existence/properness of the cusp is checked by the analytic agent against Yang's theorem.

## D: characteristic numbers and exact smooth type

The pre-read derivation agrees with the body proof. Todd integrality yields c2^2=2+240k, while the signature is 2+16k. Rank four forces k=0. The resulting odd unimodular form is I_(3,1). The norm-two characteristic vector is reduced by the explicit integral reflection and coordinate sign changes: positive odd last coordinate d strictly decreases until d=1. This produces the isometry carrying p1/2 to (1,1,1,1).

The quaternionic clutching homomorphism (a,b)->(a-b,a+b) is injective, with inverse ((e+p1/2)/2,(p1/2-e)/2). In the paper's fixed orientation conventions it identifies the stable normal homomorphism with evaluation of p1/2. The Poincare-duality transport carries this full datum. The primary classification source, checked at its exact theorem, is the oriented almost-diffeomorphism classification. Kramer–Stolz absorbs the resulting homotopy eight-sphere in a positive HP² summand. The middle-square evaluation proves the absorption diffeomorphism has degree +1, so the connected-sum comparison preserves orientation.

## Required third checks

### F.2.28 (02NI)

The pre-read derivation records the complete abelian group presentation, its torsion-sensitive determinant calculation, the primitive fixed lifts u_i, removal of vertical numerators using the rank-one norm, and the relative translation obstruction on the pair of pants. The body proof agrees. Its first step gives an even shorter abelianity argument: quotienting by the normal fibre subgroup yields the trivial coprime two-point orbifold group, so the total group equals the fibre image and is abelian. The geometric normalization uses H^2(P,boundary;Lambda)=Lambda_Gamma integrally. Under simple connectivity this is exactly Z, so zero free winding means the full obstruction vanishes. The cap translations and total fibre inversion preserve orientation. No unresolved step was found.

### F.2.30 (02NL)

The pre-read derivation records both directions of the retention rule, exhaustive rational and integral enumeration, normalized affine fillings, the Euler/duality argument, smooth almost-complex compatibility, and the exact smooth classification. The printed proof agrees. The period statement is scoped to the punctured base with the specified bounded cusp. The proof does not infer good reduction at the other punctures from the Oka period theorem. A minor expository improvement is to state that p1/2 is primitive because its square is two: a divisibility d>1 would make d^2 divide two. The displayed mathematical claim is correct.

## Primary sources opened

1. Conway–Crowley–Powell–Sixt, authors' v3 (2021), `https://www.maths.gla.ac.uk/~mpowell/large-homotopy-stable-class-v3.pdf`: §3.3 pp.11–12; Definition 3.6 p.12; Theorem 3.7(1) pp.13–14. Exact hypotheses, orientation, stable normal invariant and homotopy-sphere ambiguity agree with the use in F.4.1. Web references turn901269071view0 and turn400369641view0.
2. Kramer–Stolz, JDG 77 (2007), `https://www.uni-muenster.de/AGKramer/linuspub/27.pdf`: Theorem A, published p.178. Every homotopy sphere is absorbed by a simply connected projective-plane-like manifold in this dimension. Applied specifically to HP². Web reference turn400369641view1. The DOI resolver itself was inaccessible; the authors' institutional copy opened successfully.
3. Peters–Sterk, June-2024 manuscript, `https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf`: Theorem 2.2.1 p.61. Rank at most four is either odd diagonal or the even hyperbolic possibilities, so signature two gives I_(3,1). Also inspected Theorem 2.3.1 p.62 and Theorem 2.4.2 p.63. Web reference turn691985216view0.
4. Mandal, attached primary TeX `S6_GRIND_6_literature/papers/arXiv_2609.27929_Mandal_src/FINAL.tex`: Lemma `firstp1` (the cited Lemma 2.1) and Theorem `prop:p1ConnectedSum` (the cited Theorem 2.4), together with the intervening cohomology and stable tangent formulas. These give p1(HP²)=2alpha and p1 on the oriented connected sum as 2 sum x_i. The TeX statements and proofs were opened; page numbers were not independently recovered from a new rendering.
5. Esole–Kang, attached primary TeX `S6_PUBLISH_literature_arxiv/1807.08755/ChernClassFinal.tex`, displayed holomorphic Euler and signature polynomials near the start (the cited equations (1.2) and (1.4)). The coefficients used above agree. The polynomial identities were independently recomputed in the proof; the extension of Todd integrality to an almost complex tangent bundle is the symbol-index fact stated in the common conventions.

## Checker corrections and record accuracy

My pre-read pencil derivation contained a sign error in solving for the double root: it wrote r=5lambda/4. The equation gives r=-5lambda/4, hence +64/625. Comparison and exact resultant/substitution computation corrected this checker error. The paper's printed value is correct. The pre-read file is retained unchanged to document the sequence.

An initial symbolic-program assertion used structural expression equality for two differently arranged identical expressions. It was changed to a zero-difference symbolic check. This was a checker implementation issue and did not change any mathematical input or output.

The global B proof and several body proofs were read before the complete new computations were written. Their read-through is recorded as “used and rechecked in this run”; the independent exact arithmetic is recorded as “computation or formal certificate.” Only the derivations actually written before proof-body access are recorded as targeted proof checks. Nothing here certifies a rendered-page reading or the final edited text.

## Editorial guidance already delivered

`S6_SERIES_PUBLISH_V_common_cusp_move.md` gives the exact shared-cusp relocation, the labels to preserve, and a fully written smooth-dependence lemma. This removes the headline construction's forward dependency on the resolved fibre product. The source's repeated integral homology statement can be merged by retaining all aliases on the single theorem, followed by the marked-model identification for the holomorphic realization.
