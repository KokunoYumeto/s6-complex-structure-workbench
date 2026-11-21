# Paper I — preread derivation of push:src:E.3.1 (tag 033I)

The target compendium derivation and target E.2.1 proof have not been opened. Their statements cite one another. The derivation below starts from the actual local models rather than from E.2.1's asserted splitting. Inputs: normalized finite torus root charts (fam:A.1.2 statement), the fixed rank-two periodic cusp fan and local semistable charts, and general analytic base-change/duality statements. The attached DGKX v1 general base-change and relative-duality lemmas were read, including their exact conventional-source references; no result specific to its six-sphere theorem is needed.

## Fibre dimensions without E.2.1

1. Pass to an analytic étale atlas U of the root curve P(3k,4l). At an ordinary point the fibre is a complex two-torus. At a finite stacky point, the full normalized root chart removes the multiple fibre and gives a smooth torus family. Each such geometric fibre has (h^0,h^1,h^2)(O)=(1,2,1).

2. At the unchanged cusp, use the fixed periodic toric triangulation modulo its deck lattice. The normalization of the central surface is a complete smooth rational toric surface; the three normalized double curves are P^1, and there are two triple points. Its semisimplicial normalization resolution is

0 -> O_W -> O_(W[0]) -> O_(W[1]) -> O_(W[2]) -> 0.

Every term in positive stratum-cohomological degree vanishes because the strata are complete rational toric varieties or points. The global-section complex is exactly the cellular cochain complex of the triangulated real two-torus. Orient a square fundamental domain with diagonal, use its one vertex, three oriented edges a,b,d and its two oriented triangles. Its degree-zero map is zero and, with oriented triangle boundaries a+b−d and −a−b+d, its degree-one map is

C -> C^3 -> C^2,
0, [ [1,1,−1], [−1,−1,1] ].

The latter has rank one; hence the cohomology dimensions are (1,2,1). The branch identifications may change signs in both rows under another orientation convention, but the displayed complex fixes an explicit convention and computes the same maps. This checks the needed singular fibre directly. The finite logarithmic parameters do not alter this cusp model.

## Base change and exact hypotheses

3. On each atlas chart p:Y->U is proper and flat. At the cusp it is locally q=z_0 z_1 z_2, or the corresponding two-factor smooth stratum chart. At other points it is a submersion. The total atlas space is smooth, the fibres are Cartier hypersurfaces in it, and their structure sheaves are flat over the disc. The fibre dimensions from steps1–2 are constant on geometric points.

4. Grauert's constant-dimension criterion now gives R^q p_*O_Y locally free of ranks1,2,1 and canonical pointwise base-change maps that are isomorphisms. Exact primary reading: Grauert1960 §7 Satz5 printedp64 (PDF63), assumptions preceding it onp63(PDF62); the1963 corrigendum pp35–36 does not alter that conclusion. The modern book locators opened are Bănică–Stănăşilă III.4.12(ii), pp134–135, for the constancy criterion and III.4.10, pp132–133, for arbitrary analytic base change. Its III.4.1p124 constructs the finite free complex used in the proof of these results; it does not state the trace duality.

## Relative duality and descent

5. The smooth total space and smooth base curve make p a flat Gorenstein morphism of relative dimension two. Thus the relative dualizing complex is omega_(Y/U)[2]. The canonical relative analytic trace induces

Rp_* omega_(Y/U)[2] -> RHom_U(Rp_*O_Y,O_U),

which is a quasi-isomorphism by relative analytic duality. Since all the cohomology sheaves R^q p_*O_Y are locally free, the local hyper-Ext spectral sequence has only its sheaf-Hom terms. Taking degree−2 gives

p_*omega_(Y/U) = (R^2 p_*O_Y)^dual.

In particular this constructs the isomorphism canonically; equality of ranks alone would not construct it. Equivalently, its fibre map is the perfect Serre trace pairing H^2(O) times H^0(omega)->C.

6. On the double overlap U×_B U, both projections are local biholomorphisms. The canonical base-change maps commute with these projections, and the relative trace commutes with their pullback. They satisfy the groupoid cocycle law by functoriality. Consequently the vector bundles, geometric-point comparison maps and trace isomorphism descend to the analytic root curve, with the original stabilizer actions retained.

## Exact dependency repair

State and prove the constant fibre dimensions from the normalized torus and cusp charts before E.3.1. Then E.3.1 can depend on those local-model statements plus Grauert and analytic relative duality. E.2.1 may subsequently invoke E.3.1 for local freeness, base change and the top-degree duality. Remove the mathematical dependency E.3.1 -> the direct-image conclusions of E.2.1; referring to E.2.1 solely to identify the class of morphisms should be replaced by explicit local-model hypotheses. The final application to fam:A.5.2 is then a specialization k=l=1 after the general calculation.

## Independent work and source boundary

The cusp cochain calculation above is a fresh derivation from a square and its two oriented triangles, not a retained program. A new exact program will verify ranks and explicit kernel generators. The relative-duality source mentioned by the attached DGKX lemma is Ramis–Ruget–Verdier1971 pp261,264–266, together with Ramis–Ruget1970 §3Th1p81 and Prop2p91. The latter primary PDF has been opened; the former exact page opening is still in progress, so this preread note does not claim that primary-source audit complete. The target proofs remain unopened.

Saved UTC: 2026-11-21T00:54:04.849866+00:00
