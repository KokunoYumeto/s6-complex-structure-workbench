| Item | Statements answering the item | Outcome | Completion and precise remaining work |
|---|---|---|---|
| A.1 | A1.0–A1.3; A2.1, A2.4; A4.1 | (a) | Finished: all six cotangent direct images; independent vertical-twist/duality proof; all finite and cusp strata. |
| A.2 | A2.1–A2.4 | (a) | Finished: exact scalar with its fourth-root branch, independent 100-digit computations, geometric nonvanishing, order-three leading coefficient and full determinant divisor. |
| A.3 | A3.1–A3.2; C1.2 | (a) | Finished: complete Hodge table, actual Leray generators and independence of every admissible c. |
| A.4 | A4.1–A4.2 | (a) | Finished: local modules prove the correction to AC26; the workbench's degree-one correction is confirmed. |
| B.1 | B1.0–B1.2 | (a) | Finished: actual invariant-lattice comparison for all admissible (3,4) twists; marked dictionary and its scale ambiguity. |
| B.2 | B1.1–B1.2; B2.1–B2.2 | (a) | Finished: all coprime (3k,4l), canonical formula, full graded anticanonical ring and requested small-pair table. |
| B.3 | B1.1–B1.2; B2.2; B3.1–B3.3 | (a) | Finished: finite-fundamental-group members and their universal covers, residue torsion, Hodge and canonical invariants. |
| C.1 | C1.1–C1.2 | (a) | Finished: every nonzero d1 on a named basis and E1 ≠ E2 = E∞. |
| C.2 | C2.1–C2.2 | (a) | Finished: direct kernel/image calculation of all BC/A groups and comparison with the specified McHugh/Angella formulas. |
| C.3 | C3.1–C3.8 | (c) | **Unfinished only for an evaluated local coefficient atlas for G,Q.** Algebra, Picard map, +12 sign, non-Kähler degrees and named metric types are proved; exact global operator representatives are supplied. |
| D.1 | D1.1–D1.3 | (a) | Finished: ordinary tangent direct images, including root torsion and cusp correction; h(T) = (1,1,1,0). |
| D.2 | D2.1 | (a) | Finished: H1(T) is spanned by the parameter class; Kodaira–Spencer is an isomorphism for every admissible c. |
| D.3 | D3.1 | (a) | Finished: primary bracket zero and entire Kuranishi germ a smooth reduced line. |
| D.4 | D1.1; D4.1–D4.5 | (a) | Finished: every Picard twist, explicit jump loci, all stalk modules and lengths; nonintegral cusp exponent r = 1. |
| E.1 | E1.1 | (a) | Finished: all sufficiently small deformations retain the pencil, torus fibration and algebraic dimension one. |
| E.2 | E2.1–E2.4 | (c) | **Unfinished for the exact comb Hodge-kernel splitting, torsion support/elementary divisors and obstruction maps.** All four untwisted tangent dimensions and universal Hodge growth bounds are proved. |

# S6_01_INVARIANTS: research and verification record

AI-produced by **GPT-6 Astra (OpenAI, ChatGPT Pro mode)**, 12 November 2026.
We claim no priority and no independent human peer review. There are 47
numbered statements, with one matching CSV row for each. Fourteen prompt
items are finished at outcome (a). C.3 and E.2 retain the explicitly identified
unfinished work above; this dossier is therefore **not a complete resolution
of every requested task**. The two Refuted statements concern false assertions
in AC26/HKP, rather than a refuted workbench Hodge value, which is why the
corresponding completed local-module item is classified as (a).

## 1. Mathematical scope and independent route

We work with the actual period family and its three specified fillings,
with complex coefficients unless another coefficient ring is written.
The standard twists are v1 = (1,2,−4,0), v2 = (−1,−3,3,0) and
(l0,l1,l2) = (0,1,−1), hence p = −1. All statements for Xc hold throughout
the strict admissible range Im c < −M. They apply arbitrarily close to that
boundary from inside the range, but assert no compact complex manifold or
extension of the conclusions at equality. The u statements concern nonzero u
in the construction domain.

The cotangent proof does not reproduce the workbench's tensor-lattice
argument. We calculate O(2S1+3S2) using the full finite invariant modules,
apply relative duality to det E, and use the globally nonzero logarithmic
vertical vector to recover E. We then calculate the absolute residue maps.
The determinant identity is independently obtained from automorphy and
modular functions. The decisive scalar is independently evaluated from the
good-reduction elliptic curve and from modular Fourier series. The ordinary
tangent calculation uses the root base to retain every finite-fibre layer,
then explicitly adds the normalization normal quotient at the cusp.

The resulting direct images are

| Sheaf | R0 f* | R1 f* | R2 f* |
|---|---|---|---|
| OX | O | O ⊕ O(−1) | O(−1) |
| Ω1X | O(−2) | O ⊕ O(−1)² | O ⊕ O(−1) |
| Ω2X | O(−2) ⊕ O(−1) | O(−2) ⊕ O(−1)² | O |
| TX | O ⊕ O(−1) | O ⊕ O(−1)² | O |

Coherent Leray gives the Hodge rows, in order q = 3,2,1,0 and columns p = 0,1,2,3:

| q\p | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| 3 | 0 | 0 | 0 | 1 |
| 2 | 0 | 1 | 2 | 1 |
| 1 | 1 | 2 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 |

In particular h12 = h21 = 1 and h11 = h22 = 2. The generator statements
retain the difference between an associated-graded Leray class, a chosen
global lift, and a differential-form representative. No arbitrary lift is
declared canonical.

## 2. The scalar and the period determinant

For the explicitly fixed fourth-root branch t−1 = s4, with the imaginary
part of μs(0) positive,

\[
\mu_s(0)=i\,\frac{4\sqrt\pi}{3^{3/4}\Gamma(1/4)^2}
=i\,0.2366093140807852246877051134504496062943051340858243372192243072\ldots.
\]

Changing s to i^j s multiplies the derivative by i^(−j). The equation
t−1 = s4 alone does not choose that phase. This is also distinct from the
workbench's derivative in a locally normalized upper-half-plane coordinate.

The modular Fourier and independent Abel-period quadrature evaluations use
100 decimal digits and differ by approximately 1.7859×10^−102. A separate
Newton calculation using the Weierstrass Fourier series, evaluated at
s = 10^−5, 10^−10 and 10^−15, has final derivative error approximately
3.1211×10^−32 and Weierstrass residual below 2.9×10^−101. Gamma and
Duke–Imamoğlu hypergeometric evaluations supply additional checks.
These are numerical corroborations, not certified interval bounds.
Nonvanishing is proved exactly from the marked elliptic period and the
section at the type-III fibre.

The exact identity

\[
6\mu_z^2-\tau_z\beta_z
=\tau_z^2\frac{E_4(\tau)^2}{E_6(\tau)}
\]

gives order two at the order-three point and order zero at the order-four
point. The leading order-three coefficient was evaluated independently
using E6 Fourier series and theta constants. After the correct invariant
lattice changes, det κ0 has simple zeros exactly at p1 and p2. The proof
does not use the workbench's degree count to establish the scalar.

The Eichler–Zagier formula was checked against its original 1982 PDF,
including its coefficient and integration path, and against Duke and
Imamoğlu (2008). The rational section is identified by its automorphy,
extension and primitive height. Its tripling formula gives the exact
order-two vanishing of μ−(2−τ)/3. The joint order-three coefficient needed
for the twisted tangent calculation is 123ik/(64π), which was checked
independently before selecting its local module normal form.

## 3. Other members and covers

Translation twists act trivially on torus cohomology. At a finite point,
the comparison is an equality of invariant extensions: z^a becomes
s^(ea) under z = s^e and remains the same section of the common punctured
family. At the cusp the changes in d log xi are base logarithmic terms,
which vanish in the relative quotient. The absolute residue cancellation
is then checked separately. This proves the same Hodge table for every
admissible one-component-cusp family of multiplicities (3k,4l), including
all requested twists and all coprime higher-multiplicity sphere members.

For X_(3k,4l),

\[
K_X=f^*O(-1)\otimes O((k-1)S_1+(3l-1)S_2).
\]

Its anticanonical ring is the regraded d-Veronese of C[x,y], with
deg x = 4l, deg y = 3k and d = 4l+3k−kl. The ring is C when d < 0;
d = 0 is impossible under coprimality. The paper proves the multiplication
maps using actual divisor valuations and monomial bases, not only the
Hilbert function. The six pairs with 12kl ≤ 60 are enumerated exactly.
For the three specifically highlighted cases, the first three
antiplurigenera are (1,2,2), (0,1,1) and (1,1,1), respectively for
(k,l) = (1,1), (3,1), (1,5). Their Hodge numbers coincide even when these
canonical invariants differ.

For a finite-fundamental-group member with |p| = n > 1, the original
threefold has the same Hodge table. Its universal cover has connected
fibres and n cusp normalization components. The dual complex is an actual
degree-n cover of the dual torus, not merely a complex with suggestive
cell counts. The additional normalized residue cokernel is
C_(p0)^(n−1) in R1Ω1. Derived relative duality places its Ext1 contribution
in R2Ω2. Thus the cover has h11 = h22 = n+1, h12 = h21 = 1, and the
same remaining Hodge entries. Its canonical bundle is O(−2S2′) and its
anticanonical ring is C[U,V] with degrees (1,2).

## 4. Frölicher, Bott–Chern, Picard and metric results

The Frölicher differentials are written on the named generators. The
sequence has E1 ≠ E2 = E∞. The direct Bott–Chern/Aeppli calculation takes
kernels and images on the elementary summands of the bounded double
complex. Exact rational matrices and an independent source/sink count
agree. The specified McHugh (2018, arXiv v4) and Angella (2018) formulas
are checked afterwards; no misprint was found in the formulas used.
This is not represented as an audit of every formula in those papers.

The total-degree dimensions are

\[
h_{BC}^k=(1,0,2,2,2,2,1),\qquad
h_A^k=(1,2,2,2,2,0,1),\qquad
\Delta^k=(0,2,4,4,4,2,0).
\]

The complete bidegree tables appear in C2.1. Every product of two
positive-degree Bott–Chern classes is zero. With the stated exponential
and Chern conventions, c1,BC(exp(zg)) = zA + conjugate(z)B. Clockwise
collar transgression gives exp(12gγ) = f*O(−p); the standard p = −1
therefore gives the positive sign and exp(gγ) = O(S1−S2).

The full degreewise Bott–Chern/de Rham/Aeppli comparison holds only in
degrees 0 and 6. The weaker injectivity of BC into de Rham also holds in
degree 1, where its source is zero; these two meanings of a degreewise
∂∂bar statement are kept separate.

The exact semipositive pullback of the Fubini–Study form excludes balanced,
strongly Gauduchon, Kähler, locally conformally Kähler and Hermitian-symplectic
metrics. The actual Aeppli restriction image in bidegree (1,1) is the real
line through η = u∧w+6γ∧δ. Its complex-oriented square on a regular torus is
−12. Averaging a positive SKT form on that torus would give a positive
invariant representative of a real multiple of η, which is impossible.
This excludes SKT and, in dimension three, astheno-Kähler metrics.
Gauduchon metrics do exist, including ones with Chern–Ricci form πf*ωFS
in any chosen Gauduchon A22 class, by the explicitly applied prescribed
Chern–Ricci theorem. Chern–Ricci-flat metrics are excluded.

## 5. Tangent cohomology and every Picard twist

The ordinary tangent dimensions are h(TX) = (1,1,1,0). H1(TX) is generated
by ξ⊗γ, the derivative of the c-family. Its primary bracket vanishes.
The actual convergent family has nonzero derivative into the one-dimensional
Kuranishi tangent space, so the inverse-function theorem excludes all
higher defining equations and nilpotent structure. The germ is a smooth
line, and the family is locally semiuniversal at every admissible c.
The nonzero H2 obstruction space is not mistaken for a nonzero obstruction
map. Consequently every sufficiently small deformation retains |−2K| and
the torus fibration, and its meromorphic function field is C(t).

All integral twists Mn = O(n(S1−S2)) are computed by the root-line
descent function d(n) in D1.1; D4.1 gives all three sheaves and all four
dimensions for every integer of either sign. The hidden order-three root
torsion descends with length one exactly when 3 does not divide n. The
cusp stalk of R2 for these twists is free of rank one.

For nonintegral z, the cusp module is exactly C{q}/(q), and R1 vanishes
at that point. In particular the requested exponent r is one for every
nonintegral twist, not merely for a generic one. Let Nz count the distinct
regular resonance fibres determined by

\[
q\tau+r\mu=p,\qquad z=n-6q\mu-r\beta_c,
\quad(n,p,q,r)\in\mathbb Z^4.
\]

The finite-point lattices and their congruence weights ℓ1(z), ℓ2(z) are
given explicitly in D4.3–D4.5. Then Jz = 2Nz+ℓ1(z)+ℓ2(z) and
h(T⊗Mz) = (0,Jz,1+Jz,0). Every regular resonance contributes
(A/(s))² in R1 and A/(s²) in R2. The two finite-point contributions
are killed by their coarse parameters; at p1 their common length is
1+εn, and at p2 it is one precisely for n ≡ 1,2 mod 4.

The relative Fourier–Dolbeault comparison is proved at chain level;
the nonzero Fourier characters are contracted with uniform estimates.
The order-three calculation uses the joint Picard/period coefficient,
not just the separate determinant orders. Division polynomials through
order twelve supply exact algebraic factors for the regular resonance
fibres. At t = 32/5 the section has exact order four, giving an actual
nonintegral jump. The actual cohomology jump loci are locally discrete
analytic subsets of Pic(X) = C. Their parameterization retains βc rather
than inventing decimal values for an unspecified c.

## 6. What the comb computation settles, and what it leaves open

For every member of the specified m-tooth construction, m ≥ 12,
R1O = O(am)⊕O(bm), with am,bm ≥ 0 and am+bm = 2m−1, and
R2O = O(2m−1). We derive h0q = (1,2m+1,2m,0) from the precise
cohomological-flatness and splitting statements of Viaclovsky (2026).
The individual splitting summands are not determined here.

The root vertical and R1O bundles each have a nowhere-zero invariant
subline and determinant O(24m−1). Their tensor-invariant comparison has
one upper modification at the order-three point. The resulting exact
ordinary tangent dimensions are

\[
h^\bullet(T_{X_m})=(2m+1,\;8m+1,\;6m+1,\;0).
\]

Moreover R2T = O(2m)⊕Qm, where Qm has length 4m and no cusp support.
The canonical bundle is the pullback of root O(−24m−6), and all positive
holomorphic-form dimensions vanish. These statements are independently
checked by character descent and exhaustive nonnegative-splitting
cohomology for m = 12,13,20,100.

For the explicit rank-three bundle

\[
K_m=\ker\{\rho_*(E_m^*\otimes G_m)
\longrightarrow\rho_*(O(5)\otimes\det G_m)\},
\]

we prove h11 = 4m+1+h0(Km) and h12 = 4m+h0(Km). Its degree is
−2m−2+em, where em is the length of the displayed map's cokernel.
The smallest unresolved case is a fully specified smoothed 12-tooth
period section: one must determine that map's splitting, em and h0(K12),
the positions and elementary divisors of Q12, and the Kuranishi bracket
and higher obstruction maps. The input paper provides an existence
construction and an open set of smoothing choices, not a unique numerical
set of transitions for “X12”. We have not solved those smoothing equations
or run two numerical methods on absent matrices. This is why E.2 remains
unfinished despite the exact tangent dimensions. At m = 12 the proved
values are h(T) = (25,97,73,0), h11 ≥ 49, h12 ≥ 48, and
88 ≤ dim Def ≤ 97.

For C.3 the remaining task is different: the exact global formulas
G0 = (d*Gd f*ωFS)01 and the harmonic/Riesz formula for Q are proved.
What is missing is their evaluated coefficient functions on a common
finite atlas through the three special fibres, for one specified global
Hermitian metric, or an evaluated Čech/partition-of-unity construction.
No numerical elliptic inverse was computed. No Hodge number, algebra
product, sign, metric assertion or existence of the Leray class remains
conditional on that representation task.

## 7. Corrections and the five Leads

| Source or Lead | Finding and exact location |
|---|---|
| AC26 Remark 9.21 | The degree-one cusp torsion assertion is false. Original PDF p. 81; transcription line 4330. A4.1 computes the modules, and A4.2 proves the correction. |
| AC26 Remark 1.3 | Original PDF p. 5; transcription line 270. A degree distinction is required: Ω1 relative is torsion-free at the cusp, whereas Ω2 relative has nonzero cusp torsion. |
| AC26 Remarks 1.2 and 9.26 | The stated universal h0(T) ≤ 2 constraint fails for the comb members. Transcription lines 264 and 4396; the unconditional bound is refuted by E2.4. |
| HKP Corollary 1.3 | The verified preprint proof on p. 2 makes meromorphic vector-field coefficients constant by invoking CDP98. That premise is false in the fibred examples. E2.2 provides h0(T) = 2m+1, so this is an actual counterexample to the universal bound, not only a gap in its proof. |
| Workbench Hodge calculation | Its numerical values and direct-image tables are confirmed by the independent proof. No erroneous numerical Hodge line was found. Its scalar normalization must be converted to the specified fourth-root coordinate. |
| Workbench relative torsion | The degree-one correction in hodge_frolicher.tex, lines 984–1007 (equation 11.17f at 991–996), is correct; it must not be extended to Ω2. |
| Workbench Bott–Chern algebra | Confirmed; the square-zero proof works for the general h-table. The +12 sign is derived from the full collar convention, not from a base orientation alone. |
| Course and reader notes | Their relevant Hodge, elliptic-section, Picard, canonical and deformation leads were treated as claims and proved where used. No additional false numerical claim in the cited passages was established. Generalization from degree-one torsion or generic twisted vanishing would be invalid. |
| Engel | No correction to the particular construction, height, finite-cover or monodromy statements used was found. This is not an audit of every assertion in the paper. The scale u has the stated reference-linearization ambiguity. |
| Lead 1 | Proved: logarithmic direct images, determinant divisor, surjectivity and global rank, then absolute direct images and Hodge diamond. |
| Lead 2 | Proved with a fixed branch: μs(0) is explicitly nonzero and the global connecting-map rank is one. |
| Lead 3 | Proved: primitive Mordell–Weil identification, Weierstrass zero, original Eichler–Zagier formula and hypergeometric comparison, with periods/signs retained. |
| Lead 4 | Proved for the numerical, algebra, Picard and degeneration assertions. Only the separately requested evaluated coefficient atlas remains unfinished. |
| Lead 5 | Proved and sharpened: h1 = h2 = 1; generic twisted tuple (0,0,1,0); r = 1 for nonintegral cusp stalks; every exceptional twist also computed. The claim “only integral twists jump” would be false, and is not substituted for the actual Lead. |

## 8. What was read and searched

The forty hashes in the attached MANIFEST.tsv were verified. The original
AC26 PDF and transcription were read in the relevant local, topology,
period, canonical, cohomology and tangent sections. Original pages 5, 62–63
and 81 were visually inspected where signs or wording mattered. The
workbench files hodge_frolicher.tex, bott_chern_algebra.tex,
period_parameter_deformation.tex and analytic_canonical_ring.tex were
read in full by the corresponding analysis streams; analytic_picard.tex,
finite-filling and local-model material were inspected where used.
The course and notes were used as untrusted leads. The per-part source
records specify the chapters and statements actually read.

The attached Engel, all three Viaclovsky papers, Liu–Rollenske, Yang and
Wang papers were opened. Their relevant construction/cohomology theorems
were checked before use. The extra rank-one degenerations and different
finite monodromy pairs in the other papers are not silently covered by
Part B. Wang's attached v2 is dated 8 November 2026.

Searches on 12 November 2026 included the exact arXiv identifiers and
queries combining “complex six-spheres”, “Hodge”, “tangent cohomology”,
“Kuranishi”, “deformations” and “locally miniversal”, including a recent
forty-day window. The searches found arXiv:2610.00250v1, whose deformation
claims overlap the untwisted tangent conclusions. We opened its 107-page
PDF, especially Section 6, and the current v2, a 30-page Oka-geometry
paper dated 23 October 2026 whose deformation sections and claims are
absent. The v1 root-base strategy informed our choice of route, but its
superseded theorem is not used as established authority. Omission in v2
is not described as a refutation. This provenance prevents a priority
claim and is stated in the paper itself.

Primary Eichler–Zagier, Duke–Imamoğlu, McHugh, Angella, Stelzig,
Gauduchon, Székelyhidi–Tosatti–Weinkove, HKP and Brunella sources were
opened for the statements used or their dependencies. An attempted
Shioda PDF fetch failed; no unexamined Shioda theorem is cited as verified.
The required height calculation is instead given from the actual
intersection matrices. Every bibliography entry has an explicit verified
label, meaning opened, not certified correct in its entirety.

## 9. Executed computations and deliverable verification

The programs include exact monodromy conjugations, elliptic addition and
division polynomials, root-character descent, cotangent torsion syzygies,
weighted anticanonical monomial counts, direct BC/A kernel/image ranks,
the Picard sign and negative fibre square, all integral tangent twists,
the regular and finite equivariant Koszul complexes, and the comb
degree/splitting calculations. Their full outputs and the 100-digit
period calculations are retained. The central reproduction run executes
all mathematical programs and the source-hash check; its log records
each exit status. Exact integer and rational assertions use exact
arithmetic. Numerical output is never the sole proof of nonvanishing.

The assembly program checks that the 47 actual claim IDs and status
labels match the CSV, that every prompt item has at least one row, and
that the bibliography has no duplicate keys. The LuaLaTeX build is
separate from the mathematics and records its passes and PDF metadata.
The final PDF is rendered for layout inspection, and the package verifier
checks the file hashes, statement coverage, PDF readability and archive
integrity. The reproducible commands and environment repair are in
README.md and code/; no mathematical result depends on that repair.
