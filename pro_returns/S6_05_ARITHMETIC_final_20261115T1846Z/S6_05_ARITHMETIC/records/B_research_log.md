# Part B live research record

## Status at 16:24 UTC, 15 November 2026: Part B mathematically complete

Statements B.1–B.9 now settle every requested item B.1–B.4. The global B.2 classification is proved: exactly129 Co0-orbits, with106 classes having an A2^12 neighbor,20 additional classes having an A1^24 neighbor, and3 classes with eight Leech extensions. All129 representatives are given as two-by24 reduced matrices in one explicit integral Leech basis. Exact isometries identify the two rooted marked models with that basis. The original intersection J is explicitly mapped to row4 by `B_identify_specific_plane.py`.

Full group certificates now exceed the originally planned Schreier recipe. `B_plane_stabilizer_recipe.py` produces full integral generators for all126 rooted classes and independently computes their orders in the faithful action on the union of the roots in the eight extensions. `B_rare_plane_groups.py` reconstructs Schreier generators from the exhaustive rare flag trees, verifies their faithful class-flag orders, and adds all necessary changes of mark. The129 JSON group files contain654 integral generators in the common Leech basis. `B_final_group_audit.py` rereads every file, checks every determinant, Gram identity and plane action, and recomputes the total orbit mass from those independently generated full-group records. Its stdout is:

```
Distinct supplied reduced plane representatives: 129
Exact integral group generators independently rechecked: 654
Sum of orbit lengths from independently generated FULL group certificates: 61549107892647466000
Direct split-quadratic incidence count: 61549107892647466000
Rational stabilizer mass: 14703561369481/1986515435520
RESIDUAL PLANES: 0
RESIDUAL MASS: 0
PASS: all 129 full group records verified; NO RESIDUAL MASS REMAINS.
```

The two rare full line-group upper bounds were independently strengthened. The552-vector Co3 Gram graph has order991533312000; a displayed graph symmetry fails lattice integrality, while the verified lattice subgroup has index2. The891-vector U6 Gram graph has order55180984320; exactly1 of6 cosets over the verified pointwise triangle subgroup preserves the Leech lattice. Thus neither rare full line-group order is inferred merely from a generated subgroup or a software orbit-name table.

The rare plane orders are52254720,15925248,35389440, with orbit lengths159134976000,522161640000,234972738000. Their sum916269354000 is the exact residual after the126 rooted classes. Discovery used seeded candidates, but completeness uses exhaustive closed flag orbits, all changes of mark, full group upper bounds, and the exact total mass. All24 rare extensions are independently enumerated and rootless. All10 rare mark-changing matrices are checked as integral Leech isometries.

B.8 now computes both full embedding-dependent cubic value groups. In the ordinary Albert sum metric, the embedding E8^3=L^3 has group(1/2)Z; rotating the first real/imaginary plane by pi/4 gives group(1/2)Z+(sqrt(2)/4)Z. All512 basis triples are evaluated exactly as rational pairs. The metric conversion from Wilson's half-sum metric is explicitly stated, and the arithmetic criterion does not claim a canonical or unique embedding.

### Additional literature opened after the first checkpoint

- Brouwer, *Uniqueness of the Leech lattice*, author notes: Theorem1.1 (rootless even unimodular rank24 uniqueness and Co0 order), Theorem1.4 (Golay coordinate construction), Section2 (norm-six stabilizer Co3). Opened in full.
- Fairbairn2010, *Some design theoretic results on the Conway group .0*, Electronic Journal of Combinatorics17,R18: Section5,p10, unnumbered assertion immediately preceding Corollary7. The pointwise stabilizer of a triangle of three minimal vectors summing to zero is U6(2), and its setwise stabilizer is U6(2):S3. The hypotheses match the difference triangle constructed here; our graph calculations independently check the numerical orders.
- Rios2018, arXiv1307.1554v2: Theorem2.2, Corollary2.3 and Section4, equation(8), opened. The map to the Albert algebra is quadratic, v maps to vv*, and identifies v with minus v. It does not establish preservation of our fixed linear off-diagonal cubic; the literature comparison now states that distinction.
- Conway–Sloane third-edition author updates, https://neilsloane.com/doc/splag3.pdf:112-page collection of updates, not the full book. Visually read the Niemeier glue table16.1 and relevant Chapter17 pages420–423. Chapter17 concerns index-two even neighbors of odd unimodular lattices.
- Conway–Sloane1982, *Twenty-three constructions for the Leech lattice*, full9-page author-hosted journal scan https://neilsloane.com/doc/Me86.pdf. Opened all relevant pages, Figure3 (including A5^4D4 and A2^12), unnumbered holy-construction assertion p275 and proof pp281–283. This is the source revised as Chapter24. It establishes the known holy constructions, not the determinant81 intersection or the129 plane classification.
- Additional searches used exact phrases involving129 plane orbits,52254720,23058,1849032,2099520, totally isotropic/singular2-spaces modulo3. No primary publication of this exact configuration or complete table was located. No priority claim is made.

### Further failed attempts and corrections retained

- The initial A1 fusion run was killed by memory exhaustion: repeated access to a compressed NPZ array inside a dictionary comprehension decompressed the entire array per iteration and retained large views. The corrected program loads each array once and uses the759 octads for code graphs. `B_A1_fusion.out` is retained as the failed run; `B_A1_fusion_fixed.out` is the complete successful run.
- The first A2 quotient setup mistakenly used a non-echelon nullspace basis as if it were reduced. An assertion caught the error; it was corrected by reducing the basis before selecting pivots. All final orbit maps and lifted matrices use the corrected quotient.
- The15:36 record below described the all-Leech residual as if four rootless3-neighbors alone already implied eight rootless extensions. That implication was not used in the proof. The final three representatives have all eight extensions separately checked, and exact mass closure proves that they exhaust the residual.
- `B_rare_setup.py` chooses generating group words by a random discovery routine. The saved exact words and matrices are the certificate, and all later audits are deterministic on those saved inputs. Rerunning discovery can produce different valid generators; rerunning the complete downstream pipeline remains valid. No proof relies on the random search having exhausted a space.

## Status at 15:36 UTC, 15 November 2026

Statements B.1–B.8 are written in `sections/B.tex`, with their exact code and outputs. B.1, B.3 and B.4 of the prompt are settled by the stated proofs and computations. The specific lattice invariants, theta series, full automorphism group and its Co0 plane stabilizer in B.2 are settled. The global B.2 plane classification is actively advancing and is not yet asserted complete.

### Exact global classification advance

The A2^12-marked flag problem reduces to the full line stabilizer `C2 × (3^6 : 2.M12)`, of order277136640. In the ternary Golay model, its four codeword orbits have weights0,6,9,12 and sizes1,264,440,24. Each remaining fibre is an affine16-space overF3 with one quadratic equation. Four exhaustive finite searches, each covering all43046721 fibre vectors, give16,54,64,14 orbits, respectively. The zero orbit is removed, giving147 nonzero flag orbits. Their weighted orbit lengths sum exactly to5230235650, the number of isotropic lines in the22-dimensional split quotient. `B_A2_flags.py` has constructed all147 lattices and their8 extensions and exhaustively enumerated every root. `B_A2_fusion.py` checks explicit rational isometries of marked Niemeier lattices, checks that each maps the Leech lattice exactly to itself, and fuses the147 flags into106 Co0-plane orbits having at least one A2^12 3-neighbour.

The A1^24 flag problem reduces to M24 acting on unordered3-colour partitions of24 points whose three sizes are divisible by3. Only9 size patterns occur. The binary subset orbits have been exhausted; exact fusion of colour labels and construction of their8 extensions are running. The residual task is to fuse these with the106 A2-containing orbits and classify planes with neither A1^24 norA2^12 among their four3-neighbours (all eight extensions then Leech). Those residual planes have only the two line types traditionally called3 and6_22. A vector orbit table alone is insufficient; no global completeness claim is made before this residual enumeration and a total mass check.

Dense orbit maps have lossless gzip replacements, with uncompressed SHA256 in `B_orbit_map_manifest.json`. The uncompressed arrays are working cache only. The compressed arrays are complete exact certificates, not samples.

## Corrections and refinements

- Lead6 is verified: six Leech and twoA2^12 extensions, two length3 cycles and two fixed points forr.
- The twoA2^12 extensions share the same72 ambient roots. An abandoned initial graph search assumed144 distinct roots and failed an assertion; `B_root_graph.py` is retained as a failed approach, superseded by `B_autJ.py`.
- The code controllingAut(J) has one repeated projective column. An initial independent enumeration incorrectly assumed all12 columns distinct and returned0. It was corrected to11 projective classes with one repeated fibre; the exhaustive search now gives1440 linear maps and2880 signed coordinate permutations, all checked in the displayed group. Only the corrected output is used.
- The Weyl divisor h/d assertion has11 counterexamples among96 pairs. The complete corrected table is retained, with every lattice and root set.
- The Wilson subgroup252 is the full cubic stabilizer, proved by a projection upper bound, a complete triality lift, and two exact orbit stabilizers, then exclusion of odd block permutations.
- E8^3 admits an explicit isometric embedding with cubic value group(1/2)Z; rotating one block gives an irrational cubic value. Thus integrality is an embedding property, not an invariant of the abstract lattice.

## Sources opened and exact uses

1. Chenevier–Lannes, attached author source arXiv1409.7616: ChapterII Corollary3.14; ChapterIII Propositions4.2.1,4.2.5,4.2.11 and Theorem4.2.10. These give the Niemeier root classification, Weyl-vector membership and norm, and the h-neighbour holy construction. Their hypotheses are checked in B.tex. They do not imply the false h/d rule.
2. Borcherds, *The Leech lattice* (1985), author PDF https://math.berkeley.edu/~reb/papers/leech/leech.pdf: Lemmas2.3,2.4,2.6 opened and checked. Common Coxeter number, rho norm, rho membership, holy-construction and uniqueness background.
3. Nebe–Sloane catalogue, index and all23 rooted Niemeier Gram pages downloaded. This supplies input data only; determinant, parity, positivity and complete roots are independently checked.
4. Wilson, *Octonions and the Leech lattice*, revised author PDF, https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/octoLeech1rev.pdf. Definition and octonion convention checked. Wilson, *Conway's group and octonions*, https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/octoConway.pdf, Definition1, Section2 and Theorem1 checked. Neither is used as a claim that all lattice generators preserve the cubic.
5. Martinet, *Reduction modulo2 and3 of lattices*, https://jamartin.perso.math.cnrs.fr/Publications/Latmod.pdf, pages1,15–18,20–22 visually checked because the PDF text encoding is corrupted. Proposition4.2 and Table4.2 classify vector residues. This is not a plane classification.
6. Primary mmgroup C-interface documentation, `gen_leech_reduce_mod3` section, opened. Exact vector orbit table and transporter API checked. The phrase “automorphism group of Λ/3Λ” there means the induced Conway group; the full orthogonal group of the quadratic space is larger.
7. ATLAS primary Co1 page https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/Co1/ opened. Co1 order4157776806543360000, its double coverCo0, and the Co3/U6(2):S3/3^6:2.M12 stabilizer orders checked.
8. Elkies–Gross, *Cubic rings and the exceptional Jordan algebra*, author PDF https://people.math.harvard.edu/~gross/preprints/rings.pdf opened; first page and equations(1.4)–(1.7) visually checked. This is pertinent existing Albert/Niemeier literature, not a new claim of an Albert connection. Our explicit E8^3 value-group proof is independent.
9. Conway1968PNAS primary full-text request hit an access check; the bibliography marks its full text unverified. Its numerical order is independently obtained from the opened ATLAS source.

## Searches and scope

Searched exact combinations of “Leech”, “isotropic planes”, “totally singular2-spaces”, “modulo3”, “determinant81”, “23058”, “1849032”, “2099520”, and ternary[12,5,6] group2880; also Chenevier–Lannes, Borcherds, Wilson, Conway–Sloane and Martinet references. Current-date broad and authoritative search engines were both used. No primary publication of the specific J configuration or complete plane table was located. No priority claim follows from that absence. The newly constructed global table is an exact independent computation still being completed.
