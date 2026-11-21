# Paper V: actual rendered-page reading, topology range

## Fixed candidate and reading scope

- Candidate: `V_candidate_01`.
- PDF: `/workspace/scratch/653608133b22/work/build/V_candidate_01/S6_SERIES_PUBLISH_V.pdf`.
- PDF SHA-256: `8b2d18bb43fedda842510e01967074589e0439c491fa3bb53928ab1d7eeedc2d`.
- Source SHA-256 at build: `ca6b2dd8860b1d31bf4b8f5cd5165dc48c8dd08ac22ba47ce9a98bed6f6d35bb`.
- Render manifest SHA-256: `f6556b465d2b035a91d1fcd931085667fd9662dc95d6676723d9d4ec30c62f37`.
- Assigned and actually viewed/read: **every page55–96 inclusive,42 pages**.
- Reading completed: 2026-11-21 00:08:17 UTC.
- Reader: GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), topology-check agent.

Every page image was displayed and read. The review considered all24 defect-register types where applicable, together with mathematical wording, references and page layout. No text sidecar substituted for visual reading. The JSON companion binds each individual page to both the exact PDF hash and its own image hash. All42 image hashes were recomputed and matched the render manifest.

The35 proposed source guards preserve every existing label and tag. Two additional bibliographic guards add the exact Engel section/page locators on pages63 and67, using the provenance agent's official-PDF verification. These files do not edit the main manuscript. This candidate remains the object of this record; altered rendered images will need a subsequent reading record.

## Concrete findings and proposed repairs

The main reference/structure repairs are the stale PartI reference to the relocated resolved-product construction, the distinction between citing the self-duality theorem and the general Leray step inside its proof, and the use of a later resolved-product equation in the order-six obstruction. For the latter, the replacement explicitly identifies
`H²(B,j_*L)=H²_c(B°,L)=H_0(B°,L)=L_Γ`
using the point-supported quotient `j_*L/j_!L` and integral Poincare duality; the finite-by-finite extension argument is preserved.

The local-complex-compatibility proposition and fixed-rank proposition are moved, with complete proofs and unchanged labels, before the involutory-order exclusion which uses them. The acyclic dependency order is orbifold quotient → local compatibility → fixed-rank pattern → involutory exclusion. Other changes remove repeated defensive/scope sentences while retaining their positive mathematical statements.

The finite integral example's boolean peripheral flags become explicit zero/nonzero restriction statements in the same first finite/second finite/cusp order. The rational-normal-form proof directly names its eight equations `YX=0,YRX=I2` and describes the ten solution coordinates by `E^{-1}b`.

No clipped, overlapping, illegible or otherwise defective page layout was identified in the assigned range.

## Cleared concerns: no source faults

Two small-word concerns were false alarms and are explicitly excluded from the guards:

1. On page78, a3x render confirms **“The abelianized van Kampen presentation now shows.”** The article was already present in the candidate and the source.
2. On page94, a3x render confirms **“its cokernel is”**, with ten unit Smith factors, one factor2 and `Z^9⊕Z/2`. The corrected original and integrated source are identical on this point, and no prior topology patch touched the sentence. The reader initially misread this word. No source refutation is recorded, and no new exterior-cube computation was run.

The page88 zoom confirms the actual D02 sentence: “No lattice splitting over a localization or semisimplification modulo a prime is used here.” It is a genuine proposed deletion, not a cleared concern.

## Proof-edit comparison scope

The attached corrected original already contains the correct page94 cokernel assertion. It also contains the boolean flags, the “first eight” reference and the linear-system coordinate operation; their replacements preserve the supplied mathematical maps and make their meaning explicit. The stale PartI and later resolved-equation dependencies arise from moving the resolved construction after the headline. The proposed reorder changes the placement of two complete existing proofs and does not add hypotheses or alter their conclusions.

The page-by-page review checks the displayed arguments and their wording; it is not a fresh independent derivation of every matrix and Smith table encountered. The new coinvariant passage gives the exact standard sheaf/duality argument at the required integral coefficients. The visual page review itself adds no mathematical events. After the35 guards were applied, five actual changed-proof rereads were recorded separately in `S6_SERIES_PUBLISH_V_page_rewrite_CHECK_EVENTS.tsv`, all as used and rechecked. The previous41 rows remain unchanged, giving **46 total topology-agent rows**. No independent-check or refutation event was added for page QA.

## Per-page record

Every row below belongs to the fixed PDF hash above; the JSON repeats that full PDF hash in every page record.

### Page 55

- Image SHA-256: `f0504db0ebc65ecc4e8aba246fec1385e4ac7a0bf6c06465fac2449efef95fc1`.
- Read: Read the end of the parameter-family extension proof, including the punctured-disc torsor argument and Cartan Theorem B; Part II and section10 opening; admissible-data definition10.1; cusp Euler theorem10.2 and proof; diagonal obstruction10.3 statement.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 56

- Image SHA-256: `d71473002eaf747c0504a7fd585043fb1df8e39bf4704b894ea5eb0dfb7896a5`.
- Read: Read diagonal obstruction proof; complete finite-order filter10.4, cyclotomic enumeration and real-complex parity criterion; self-dual parity obstruction10.5 and its first two Leray steps.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02, Proposition10.3 proof: not only to integral or invariant choices Proposed repair: Delete this appended contrast; the fixed-point argument already covers every translation.
  - D11, Proposition10.4 statement/proof ending: These are necessary types, not 38 or 19 conjugacy classes ...; It does not bound affine multiplicities ... Proposed repair: Keep the precise statement about linear orders and characteristic-polynomial counts; remove redundant negative scope commentary.

### Page 57

- Image SHA-256: `eecf61526b652b592734ab33c6a45575a7a652dc97cca7f0d84a765d20ab09df`.
- Read: Read final self-duality/Euler parity argument of10.5; all of remaining-rank-pattern proposition10.6; section11 and orbifold quotient theorem11.1 through the initial van Kampen argument.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D14/D24, Theorem10.5 proof final sentence: the fibre-product example of Part I Proposed repair: Point to the moved resolved-product part via its part label.
  - D11, Proposition10.6 proof final sentence: No existence of a tuple or of a period family with these ranks is asserted. Proposed repair: Delete; the proposition already states a necessary rank restriction.

### Page 58

- Image SHA-256: `c00045ae0d4326d28ce637b715118b28dcf7ce00116b25e809b677a7d48f5cfd`.
- Read: Read the orbifold quotient proof through the triangle-group representation; all of involutory-order exclusion11.2; statement of first-cohomology pattern11.3.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 59

- Image SHA-256: `35fce1137da134ffb2a0e4a8c76b00342ea0718c01a2a3b0ce84269f2951b25c`.
- Read: Read all four steps of the first-cohomology pattern proof; primitive exterior-square comparison11.4 and its explicit basis/transvection proof; beginning of order-pair exclusion11.5.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D06/D23, Proposition11.3 proof first sentence: Theorem10.5 gives a=1, vanishing first parabolic cohomology ... Proposed repair: Cite the Leray argument in the proof of Theorem10.5; its stated theorem has the extra self-duality hypothesis and does not assert these intermediate conclusions.

### Page 60

- Image SHA-256: `b086dd83fa5e19c1e3f9f25ffffdc95fd5a72d8c73c61ee6ef1c90a583348f97`.
- Read: Read all of order-pair exclusion11.5, including the End(W)=Q argument, invariant-Hom Euler calculation, alternating-map vanishing and exterior-square contradiction; beginning of rational-extension uniqueness11.6.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 61

- Image SHA-256: `c8c9ad309da0b6e66f18bc8c52c02afcda9315c3cec232a81ec3b462adb0a7c0`.
- Read: Read the complete rational-extension uniqueness11.6, including finite norm constraints, exact cusp-restriction isomorphism, square-zero extension line and scaling action; read matrices and first part of integral obstruction11.7.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 62

- Image SHA-256: `822c25655336bfc6c9fe79703a6462f152c54176af0eae60eb77b24f99927c25`.
- Read: Read the integral-obstruction conclusion and its first two proof steps: 31-word determinant, localized stable-lattice form, primitive cusp restriction and full clutch/twist fundamental-group determinant.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D12, Theorem11.7 proof item1 closing paragraph: The determinant argument applies to every stable lattice. Proposed repair: Delete this immediate repetition of the preceding conclusion for every stable lattice.

### Page 63

- Image SHA-256: `2f43d68d62896569a0c7c64fd1f82955819f4237621cb8ebc4d2f2bee1f802bb`.
- Read: Read finite-cap transfer and norm computation over Z_(3), the primitive idempotent and horizontal restriction quotient, exact cusp input and start of integral specialization-sheaf complex with oriented cellular maps.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02, Theorem11.7 proof item3: No choice of lifts of the vertical Wang classes changes this quotient or its kernel. Proposed repair: Delete after the exact horizontal quotient formula; the well-defined quotient has already been proved.
  - D18, Engel citation: replace the bare section title with section7, pp.17–21, whose exact official-v1 boundaries were verified by the provenance agent.

### Page 64

- Image SHA-256: `0622413758d8767dd3e018fc45da065d9a8f84593be14f35b7e98b7cf3e5f350`.
- Read: Read integral-obstruction Smith table, constructible-sheaf quotient and total-degree3 argument; standard-lattice example with explicit twists, determinant1 and rational Betti vector.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 65

- Image SHA-256: `d391b1e8b5b82aff940734bfeeacf43b8c2609cad9b9c265d36f8055d20300b4`.
- Read: Read two excluded rational families11.8, their precise torsion statements, quotient/exterior marking, two rational block models and matrix-word algebra determinants.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 66

- Image SHA-256: `cffe179be0ad5185f40912e89b334ba3280044829747aea00eaf3b6a76eb7b21`.
- Read: Read localized stable-lattice reduction, exact affine conjugation formula and fundamental-group determinant; finite cap prime-to3 cover and beginning of its Wang comparison.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D11, Theorem11.8 proof item2 closing sentence: This proves the assertion for all invariant lattices, with no bound on their indices. Proposed repair: Remove the repeated closing scope sentence; the statement already quantifies over every invariant lattice.

### Page 67

- Image SHA-256: `edfd77c803dd0eb09ccfcb3df8fd7e598652625b8469dc0897abc497ee46a4cd`.
- Read: Read finite-cover norm and its exact quotient map; case-A primitive invariant basis and Smith coordinate change, case-B invariant line, and oriented base-sheaf complex.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02, Theorem11.8 proof item4 final sentence: Thus no choice of a Wang splitting changes this quotient. Proposed repair: Delete after the exact horizontal quotient and kernel explanation.
  - D18, Engel citation: replace the bare section title with section7, pp.17–21, whose exact official-v1 boundaries were verified by the provenance agent.

### Page 68

- Image SHA-256: `232e21b8e2df1ab8b4926ceba9b998fdb0bb85b2f0f2f60cbad6cc1cf66af7b9`.
- Read: Read inverse-generator chain comparison, full Smith table and proper-base-change application; sheaf and Leray derivations of both torsion groups; beginning of explicit smooth realizations and primitive cusp.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 69

- Image SHA-256: `3420e0d13e426612b0b2986ea44cbd825451a0b13f7ab108a24a2a60a7a381ed`.
- Read: Read the integral cusp marking, affine vectors, all nonidentity-power freeness, collar translation maps, full cap fundamental-group maps and group-level triviality argument with determinant1.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D23, Theorem11.8 proof item9 cusp-gluing sentence: the ... Kuhn cap of theorem2.4, theorem2.6 Proposed repair: Use one combined cleveref so that the phrase reads 'theorems2.4 and2.6'.

### Page 70

- Image SHA-256: `9ece20014e95a862c9fb3b3f7ca6f46afb7d1d58a26de28c79ce36428a82aa5e`.
- Read: Read rational Betti calculation completing11.8; complete statement/table of spectral-pair theorem11.9 and first two steps proving vanishing exterior invariants and the alternating-form bound.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D11, Theorem11.9 statement final sentence: The table gives necessary conditions only. Proposed repair: Delete; the statement has already introduced the table as necessary possibilities.

### Page 71

- Image SHA-256: `c5f0f284c0f1c42a42c56a47814e72f75c3b05c49a963fa42d64ef11146bcd96`.
- Read: Read exterior-square Euler bound and complete finite spectral enumeration; all of automatic local complex compatibility11.10, including determinant, even eigenspaces and explicit commuting structures.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D11/D02, Proposition11.10 statement and proof ending: This assertion concerns the individual finite actions and does not produce simultaneous global periods.; ... without this argument. Proposed repair: Remove repeated negative scope commentary; retain the explicit local statement and construction.
  - D14, Placement of Proposition11.10: Its evenness conclusion is used by11.2,11.3 and11.9 before its proof appears. Proposed repair: The dependency graph is acyclic: place11.10 after11.1, then11.3 before11.2. Preserve labels/tags and every proof.

### Page 72

- Image SHA-256: `085d393d17c7b163125d34800496284e12b980c03921d92f7a1211964919d0f1`.
- Read: Read unbounded integral family12.1 statement, rank-two nilpotent formulas, determinant identity, exact finite orders, rational lattice change and start of integrality verification.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 73

- Image SHA-256: `e3449348f3dbd863197eaa4799155ad2e177e7cee4e2f03f4ec8365fa59dd879`.
- Read: Read hatted-lattice unit witness, finite orders, explicit rational change to integral polynomial matrices, all three primitive-cusp minors and exact homology cusp formula.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 74

- Image SHA-256: `f639590051f396b036722bcb486de375f2fdd068555ab446fd689c5017b109a6`.
- Read: Read explicit rank-five quotient map, irreducibility argument, trace obstruction to self-duality, strictly decreasing rational-conjugacy invariant and affine lifts for parameters in20Z.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 75

- Image SHA-256: `7e831952a06a78739f6104e49c14df3b1074fabcf78e2e63411000905682a5e7`.
- Read: Read parameter-zero identification with the main marking; odd-torsion obstruction12.2 through coinvariants, Leray source analysis, surviving torsion and UCT.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02, Theorem12.1 proof item7 final phrase: without a further change of basis Proposed repair: State the equality in the fixed marking positively; the substitution already identifies both matrices and affine numerators.

### Page 76

- Image SHA-256: `7b26b63a4a89df6d779a3682eff6c786b13ab81c286ce37aca41e58cfdfcb4d6`.
- Read: Read non-self-dual three-connected example12.3 through its explicit matrix, fundamental group, integral restriction data, peripheral torsion and order-four mapping-torus marking.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D09, Theorem12.3 proof item3: Its torsion class has peripheral triviality flags (true,false,true) Proposed repair: Replace boolean bookkeeping by the explicit mathematical restrictions: zero at the first finite boundary and cusp, nonzero at the order-four boundary.

### Page 77

- Image SHA-256: `742ad6c87809b4c431baeb29288110a3a1af72caa6231fa9177cfcc193d86152`.
- Read: Read torsion transgression witnesses and integral homology of12.3, almost-complex/smooth classification and rational nonselfduality; residual lattice obstruction12.4 statement and semisimplification comparison.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02, Theorem12.3 proof item6 final sentence: No integrability at the finite punctures is used for this smooth classification. Proposed repair: Delete after the positive application of the almost-complex and smooth classification theorems.

### Page 78

- Image SHA-256: `0a8a829799464f5f268d817bd918d52b26ade9fc1b177589018622045e627897`.
- Read: Read the residual obstruction proof: mod-p fundamental-group rank bound, quotient torsion alternative, characteristic-independent absolute irreducibility; beginning of complete rational(5,4) normal form12.5.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.
- Cleared concern: A3x render of the actual candidate PDF confirms 'The abelianized van Kampen presentation now shows'. Source also contains 'The'. This was the reader's visual misread; no source correction or refutation.

### Page 79

- Image SHA-256: `21c09aee94f586938f7f4bdea79c004454dee50e2aa7d4abdd35658f91123cfc`.
- Read: Read rational normal-form parameter space and discriminant; canonical cyclotomic block, exact rank-two conditions, plane centralizer action and projective parameter/stabilizer argument.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 80

- Image SHA-256: `74612898a44917c106f13af9755596860231a74eb5ae067e47b6c5f0f28cce5e`.
- Read: Read the ten-equation linear system, determinant D/4, exceptional cubic locus and both projective points, affine solution family and complete irreducibility argument.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D23/D06, Theorem12.5 proof item3 second sentence: The first eight are(12.15). Proposed repair: State directly that the first eight are YX=0 and YRX=I2; display12.15 also contains a geometric plane-intersection condition.
  - D09, Theorem12.5 proof item4: Y=reshape(E^{-1}b) Proposed repair: Describe E^{-1}b as the column of the ten row-ordered entries of Y, avoiding an undefined program-like reshape operation.

### Page 81

- Image SHA-256: `04b8879743f4b70373274505712169b5b7662a6d9405bbb2c8ea67b2d1b9613b`.
- Read: Read normal-form bijection conclusion; complete good-prime lattice statement12.6; residual composition-factor analysis, involutory identity, quotient-lattice uniqueness and start of integral extension comparison.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 82

- Image SHA-256: `369a0ecbe6862e6076112df1ee7850599cd45b33576ea677dfa13a3218789c73`.
- Read: Read final good-prime extension-lattice homothety argument; terminating lattice algorithm12.7 statement and cyclic/cocyclic word bases, trace-dual sandwich and order-stabilization bound.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02/D11, Theorem12.7 statement final phrase: and lose no lattice Proposed repair: Keep 'The bounds below depend on the input rational pair' and delete the redundant negative completeness phrase.

### Page 83

- Image SHA-256: `11f45f6b59652c7acf160eb17cd7e0c4145935ff168a4517625962734660a829`.
- Read: Read integral conductor bound, finite lattice enumeration, quotient primitivity filter, extension equations, exact kappa homomorphism and complete extension classification.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 84

- Image SHA-256: `1c81ebec1291e630a768e20d5d29c6fc29897aa4000f39659cf8d1d66970f848`.
- Read: Read two-member lattice classification12.8 and its full proof, including all374 F2-subspaces, extension torsion classes, divisibility table and sole eligible class; all-twist classification12.9 statement and determinant criterion.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 85

- Image SHA-256: `f2d9581a24a44c10d6d8e04a2717e07e385985aaa98ac8d71b68097fb9c33ca8`.
- Read: Read all-twist proof through explicit fixed-basis decomposition, exact fundamental-group determinant, mapping-torus suspension periods and larger-multiplicity torsion obstruction.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02, Theorem12.9 proof item4 last clause: there is no omitted period condition Proposed repair: Delete after the affirmative Wang-sequence generation argument.

### Page 86

- Image SHA-256: `c432f1ff87b9e1085c4a2190a20f40ed2fc2325d27adbf832a3fc27a417297dc`.
- Read: Read norm-surjectivity proof, explicit translation vector and boundary mismatch, relative pair-of-pants obstruction map, normalized numerator congruences and start of orientation-preserving inversion.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 87

- Image SHA-256: `57a6a751543f18affbfdc6e909bcdf438c8b1c9b7af3bd2b7cd95f4b64e8ec87`.
- Read: Read extension of simultaneous inversion over the Kuhn fan and completion of all-twist classification; section13 and universal suspension obstruction13.1 statement; exact fixed-lattice splitting and positive invariant pairing.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D11, Theorem13.1 statement final sentence: There is no multiplicity search bound in this statement: the only possible affine multiplicities are the two displayed pairs. Proposed repair: Delete the repeated negative-scope sentence; the quantified statement and table already give the exact possibilities.

### Page 88

- Image SHA-256: `1b69242f158cfdf6915185820a6a38cc37f504cf6341eaa14007e762cab9c47c`.
- Read: Read integral norm/polynomial image divisibilities, exact suspension quotient, sheaf injection and universal multiplicity equality; checked all eight printed spectrum rows and their elementary values at1 while reading.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02, Theorem13.1 proof item3 final sentence: No lattice splitting over a localization or semisimplification modulo a prime is used here. Proposed repair: Delete; the preceding integral operator calculation is complete.
  - D02, Theorem13.1 proof item4: Torsion ... is a specialization kernel, not an additional restriction on these free periods. Proposed repair: Retain the positive kernel assertion and the following Wang generation statement; delete the appended contrast.

### Page 89

- Image SHA-256: `7c8d07c6ad0361eca9ba9e81a0ab3401afaf183d18ff3961ce5306f9878be6c1`.
- Read: Read the entire rational(5,6) parameter statement and proof through the exceptional affine line: linear system, characteristic polynomial, conic/cubic separation, positive quartic identity and explicit exceptional matrix.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 90

- Image SHA-256: `1875ff674b07bccda264192701b195bd325128b54c16ed527824b8bd0d96a701`.
- Read: Read end of13.2; order-six exclusion13.3 statement and local Z3 representation proof, idempotent decomposition, Jordan-block/cyclic-basis map and complete invariant degree3 basis/pairing.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02, Theorem13.3 proof item2: We have proved, without a global lattice classification, that ... Proposed repair: State the resulting finite representation positively and remove the methodological contrast.

### Page 91

- Image SHA-256: `ff39af3275863fbe77f9d5540083ac22c970339e848f2349fa29a6d1b7fc63f9`.
- Read: Read order-six covering-index pairing, invariant exterior vanishings, local torsion injection and finite-filtration extension argument; universal fundamental-group/twist theorem13.4 through exact determinant and torsion criterion.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D14, Theorem13.3 proof item7: it is the coinvariant module, as in(17.5) Proposed repair: Give the general identity H²(B,j_*L)=H²_c(B°,L)=L_Γ from the point-supported quotient and integral Poincare duality here, avoiding the later resolved-product dependence.
  - D02, Theorem13.3 proof item7: There is one extension issue, and it cannot remove this torsion.; in particular it cannot be absorbed as a finite quotient of a free filtration kernel. Proposed repair: Retain the exact finite-by-finite extension argument and delete these two defensive clauses.

### Page 92

- Image SHA-256: `5c73839769d4eaab9ff2d52c459fdf37e45d54ffc769df13ab78e63550e5214a`.
- Read: Read normalized-twist statement and full proof13.4: nonabelian reduction, triangular integral presentation including T, cap norm map, relative obstruction and orientation map; beginning of finite three-connectivity criterion13.5.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D11, Theorem13.4 statement final clause: no affine-twist enumeration remains Proposed repair: Delete; the positive unique-normalized-filling conclusion already states the result.

### Page 93

- Image SHA-256: `73c5daf70ec1da860583e061f616edf4bbcd014226e28b9407bbb263300a09de`.
- Read: Read full six-test table of13.5 and local integral proof through p-adic permutation decompositions, explicit order-four extension splitting and prime-to-p equivariant comparison maps.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.

### Page 94

- Image SHA-256: `4b07cce32d89a35a548eee1efad0c901e78b05a7d1f9a3f88c8c0803e12beb24`.
- Read: Read integral finite-cap torsion, covering-index pairings, exact finite-boundary transgression maps and cusp-boundary Wang/duality argument.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.
- Cleared concern: The3x PDF render, current source and attached corrected original all say 'cokernel' and give ten unit factors, one factor2 and cokernel Z^9⊕Z/2. No earlier topology guard touched this sentence. The concern was the reader's visual misread. No source edit, refutation or new mathematical event. No new Smith computation was run.

### Page 95

- Image SHA-256: `06e0ce2ef5d4743095e3bfb294ad95e7e28d139adae861286ceeae897008c216`.
- Read: Read global exterior vanishings, integral sheaf-kernel table, all associated-graded terms in H3/H5, UCT/duality equivalence and exact parabolic integer-kernel algorithm.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings:
  - D02/D08, Theorem13.5 proof item11 opening sentence: For reproducibility, no sheaf calculation is left as a black box in the integer test. Proposed repair: Delete the production/defensive sentence; retain the explicit integer-kernel formula and quotient calculation.
  - D02, Theorem13.5 proof item11 final paragraph: This uses the integral images of peripheral differences, not their saturations. Proposed repair: Retain the positive instruction to use the integral images and remove the appended contrast.

### Page 96

- Image SHA-256: `534412f34736636d14f6857de8c5ecfbde2a77cead623284ac0c2b0ec96767c6`.
- Read: Read v=0,1 and v=2 test outputs, exact reversed-peripheral-generator convention map, all of the three-connected-data classification13.6 statement and initial proof item through unbounded rational enumeration.
- Layout: No clipping, overlap, unreadable equation, stranded heading or other layout defect identified.
- Findings: clear.
