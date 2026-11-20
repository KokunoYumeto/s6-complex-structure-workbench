# Source comparison for the coefficient atlas

Author: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family. Date: 19 November 2026. This comparison was undertaken after deriving the new local-line/connection route. It is not a before-reading derivation of the published statements. No Library, Space or prior-conversation search was used. This is a separate post-cutoff draft; canonical events and row assessments were not modified.

## Exact relationships in the supplied primary sources

| Source and opened locus | Relation to the proposed coefficient construction |
|---|---|
| AC26 authoritative original PDF, pp. 65, 78–81: Lemma 9.2, finite/cusp coefficient transport in Lemma 9.16, Proposition 9.20, Remark 9.21 | The integral class is exactly eta = u wedge w + 6 gamma wedge delta in the same ordered marking. The original finite collar map is translation by log(s)/(2 pi i) Pi v; the cusp map is (exp(2 pi i zeta1), exp(2 pi i zeta2), q). These are the maps used by the new connection proof, with all base derivatives retained. Remark 9.21 leaves the middle Hodge integer undetermined. The proposition and remark supply the credited cohomological context; the displayed global one-form cocycle is not supplied by these specific passages. |
| DGKX v1, Section 6.2, Proposition 6.10, source lines 9150–9308; Section 6.4, scalar formula and Lemma 6.14 with its complete proof, lines 9510–9797 | The source already constructs the gamma class on the entire cusp, compares it to the full lattice quotient, and writes the scalar cocycle on all generating arrows. Our scalar f is exactly its negative on the same arrows, as proved below. This input receives direct credit; evaluating it with the specified weights is a specialization of the usual Dolbeault conversion. The original scalar input is not a new result of this audit. |
| DGKX v2, source-comparison lemma `lem:alpoge-member` and its proof, lines 2078–2161 | The comparison identifies the same ordered periods, finite affine vectors, logarithmic translations and untranslated two-triangle square fan. Their beta0 and our beta_part differ by the constant delta. The explicit maps are a = c + delta and c = a − delta, yielding Omega_a = Pi_c and identical local gluing after common restrictions of discs. This retained geometry supports the atlas transport. Version 2 omits the v1 deformation section containing the scalar cocycle above; the version-specific credit is therefore retained. |
| E26 attached `S6.tex`, Section 1.2, lines 260–275, and the already opened Definition 2.3 / elliptic-surface quotient | Engel expressly describes the relation of the four period columns to the elliptic-surface construction and states that Dolbeault computations were omitted. The exact previously verified quotient map is [xi,eta] -> [xi,exp(2 pi i eta)]; the residual period acts by (xi,W) -> (xi+6 mu, exp(2 pi i beta_c) W), while Engel uses its inverse. Thus this source supplies a related geometric presentation through a proved quotient morphism. It is not cited for a global coefficient formula absent from the opened passages. |

The DGKX numbering was checked directly against the supplied shared theorem counter: the scalar-cocycle lemma is 6.14, followed by Proposition 6.15 (Kodaira–Spencer isomorphism) and Proposition 6.16 (Kuranishi line). No page number was guessed from TeX line numbers.

## The scalar transport, including its sign

Write the source's scalar cocycle as eta_D. Its values on lattice, linear, finite affine, finite collar, cusp-period and exponential connector arrows are respectively

    gamma(lambda), 0, gamma(v_j)/m_j,
    gamma(v_j) log(s_j)/(2 pi i), gamma(lambda), 0.

The proposed line-coordinate factors are exp(2 pi i z f), with f the negative of each of those six values. The maps of the underlying family are equal after a=c+delta. Therefore f = −eta_D as an actual groupoid cochain, and the scalar cocycle identities are transported by the additive homomorphism x -> −x. On a fixed regular fibre, the receiving convention is f_ab = r_gamma(a)−r_gamma(b); the partition formula has H_a−H_b=f_ab and produces the class of bar-partial r_gamma. This is the exact sign comparison, including the choice of arrow direction, rather than an assertion that two unnamed conventions agree. The finite-root factors give O(S1−S2); their twelfth power gives f*O(4p1−3p2)=f*O(1), retaining the original factor 12.

## General method: opened primary source and exact convention

Abate–Bracci–Suwa–Tovena, *Localization of Atiyah classes*, author manuscript dated 7 May 2010, was opened from the first author's institutional page. Read Remark 1.6, formulas (1.4), (1.7), Theorem 3.1 and its proof, and Section 4.1. Theorem 3.1 gives the standard partition formula for converting a two-chart cocycle to a global Dolbeault form. Taking its overlap component to be c01/12 gives −bar-partial(w0) wedge c01/12 = bar-partial(w1 c01)/12. Taking f01 gives the scalar formula. This is exactly the proposed sign convention. The local connection transformation and (1,1)-curvature calculation are standard inputs; the proposed proof evaluates their family-specific factors and derivatives.

Primary URL: https://pagine.dm.unipi.it/abate/articoli/artric/files/LocalAtiClasses.pdf

Opened web refs: `turn834510951view0`, `turn952935641view0`, `turn952935641view1`, `turn843922220view0`. The arXiv abstract request for 1005.1482 returned DisabledError and is not counted as an opened source. The author PDF was successfully opened independently of that failure. Bibliography additions are staged in `additional_reference.bib` and `additional_reference.bbl`.

## Scope of the paper-specific verification

The construction verifies the actual twelfth-power theta factors, corrected finite affine phases, full cusp Cartier units, all annular inverse matrices and logarithm turns, the holomorphic one-form cocycle, and the evaluated locally finite coordinate partition. It proves that this one-form cocycle need not be obtained by gluing a global line. Indeed a global line with the asserted nonzero fibre Chern class would contradict H2(X,Z)=0 after restriction. The complex Dolbeault representative is obtained directly from the one-form cocycle. A real bar-partial-closed representative with this fibre class is ruled out by the separate integral-square proof.

The received sources and the bounded searches below did not supply these exact displayed family-specific one-form coefficients and connections at the loci examined. This is a statement about the comparison performed, not an assertion of worldwide priority or absence of any related result. The generic Cech-to-Dolbeault method, scalar gamma cocycle, family charts and local Chern interpretation are all explicitly credited.

## Searches actually run

Search service system2:

1. `complex structure six sphere Dolbeault representatives Cech partition unity Akhiezer Catanese 2026`
2. `Du Gong Kim Xu 2026 complex six sphere cohomology explicit representative`
3. `holomorphic connections Atiyah class Cech Dolbeault partition unity first Chern class local connection cocycle`

The first two discovery queries contained incorrect candidate names. They were not used as source attributions. The returned primary DGKX record supplied the correct authors; the attached editions were read directly.

System1, recency 180 days:

4. `"Alpöge" "Dolbeault" "representatives"`
5. `"Du" "Guo" "Kusakabe" "Xie" "Čech"`
6. `"complex structures" "Engel" "Dolbeault"`

The first set located the primary Atiyah-class paper and the DGKX abstract. The second set did not locate another exact matching coefficient theorem. Secondary press reports, seminar pages and discussion boards were not used as mathematical sources. In addition, the attached four core editions were searched for Cech, Dolbeault, partition, harmonic, theta, Atiyah, connection and curvature, and the actual relevant passages listed above were opened. Search hits alone do not establish an absence theorem.
