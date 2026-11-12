# Master map of the consolidated mathematics

## 1. Evidence layers

The consolidation has four layers that must remain distinct.

| Layer | Object | What it establishes |
|---|---|---|
| Custody | Nine verified ZIP archives, exact member hashes, nested-package hashes, and source snapshots | The registered bytes are preserved and recoverable. |
| Structural catalogue | `catalogue/CORPUS_CATALOGUE_V2_PUBLIC.sqlite`, `catalogue/ARCHIVE_MEMBER_COVERAGE_V2_PUBLIC.jsonl.gz`, and `catalogue/CATALOGUE_V2_PUBLIC_RECEIPT.json` | Files, package versions, every package placement, recursive logical occurrences, lexical TeX structures, literal references, and topic routes can be queried. |
| Source reading | `literature/SOURCE_READING_LEDGER.jsonl` | Particular lines of particular exact versions were actually read for a stated receiving calculation. |
| Mathematical acceptance | R1--R8 in `MATHEMATICAL_NOTE.md`, the tomography appendix, and the claim ledger | Only the statements supplied with complete arguments are accepted in this consolidation. |

Compilation receipts, historical review notes, and symbolic scripts can support one of these layers. They do not merge the layers.

## 2. Object chain

The corpus is not one linear proof. Its strongest coherent chain is the following collection of exact maps and receiving problems.

### 2.1 Analytic and topological candidate

The canonical workbench contains a candidate assembled through local gluing, topology reduction, integral Leray data, algebraic-dimension calculations, analytic Picard arguments, Hodge and Frölicher calculations, nearby-cycle material, and local repairs. The principal sources in local custody are routed under `../canonical_S6_snapshot/supporting_materials/workbench/research/`, including `candidate_geometry.tex`, `topology_reduction.tex`, `integral_leray.tex`, `algebraic_dimension.tex`, `analytic_picard.tex`, and `hodge_frolicher.tex`, with earlier alternatives retained under `workbench_history/`.

The structural route is

$$
\text{local analytic pieces}
\longrightarrow \text{glued candidate}
\longrightarrow \text{Leray and nearby-cycle data}
\longrightarrow \text{cohomological and topological tests}
\longrightarrow \text{global recognition problem}.
$$

The first arrows are source claims with mixed historical review status. The final recognition arrow is unresolved in this consolidation. No file count, build receipt, or local compatibility check proves that the global candidate is the intended S6 object.

### 2.2 Cusp and spectral lane

The cusp lane includes the native cusp metric, toric cover, fixed-metric and sphere routes, spectral geometry, magnetic and flux constructions, radial reductions, worldline comparisons, and SU(2)/SU(N) extensions. Entry files include `cusp_spectral_geometry.tex`, `cusp_sphere_fixed_metric.tex`, `cusp_toric_cover_completion.tex`, `cusp_su2_magnetic.tex`, and the `cusp_native_full_flux_*` family in the canonical workbench.

Its intended chain is

$$
\text{cusp coordinates and metric}
\longrightarrow \text{operators and boundary data}
\longrightarrow \text{spectral or magnetic reductions}
\longrightarrow \text{global geometric or gauge interpretation}.
$$

The catalogue routes 371 distinct versions into this lane. Eight entered through the first exact cue-reading tranche because their TeX metadata identifies the retained cusp, spatial refinement, and spectral measure of the magnetic vacuum translation. That is routing coverage, not proof acceptance. Every operator domain, boundary condition, self-adjoint realization, measure, and global receiving map must be checked before a spectral conclusion can propagate.

### 2.3 Arithmetic selector and Jordan/lattice lane

The arithmetic route begins with Erdős--Straus selector data and Koide-related exact parametrizations and audits, then passes through the `p1201` selector/Jordan bridge into Niemeier, Leech, triality, cubic, rank-six, rank-nine, 24-dimensional, and umbral constructions. Principal entry files include `erdos_straus_selector_crosswalk.tex`, `erdos_straus_koide_s6_bridge.tex`, `p1201_selector_jordan_bridge.tex`, `koide_exact_parametrization.tex`, `koide_exact_census.tex`, `es_niemeier_triality_bridge.tex`, `es_niemeier_leech.tex`, and `niemeier_umbral_shadow.tex`.

The intended maps are not identities. Each step must retain the selector domain, arithmetic congruences, multiplicities, support labels, lattice form, Jordan product, and group action. The catalogue routes 1,243 versions to the arithmetic-selector lane and 354 to the lattice/Jordan lane, with overlap allowed. The current consolidation has not performed a complete theorem-by-theorem audit of this chain.

The recovered original TeX of Ichiro Yokota's *Exceptional Lie groups* is now decoded losslessly and routed to the lattice/Jordan and quaternionic lanes. Its 282 manual statement headings and 216 manual proof headings are locators only; the book has not received a semantic audit here.

### 2.4 Quaternionic carrier and measured fibres

The quaternionic lane contains the marked Hermitian carrier, the original Moore cubic, the 4+4+1 reconciliation, the observation map, residual action, Gaussian finite measure, and information-geometric quantities. Source entry points include `quaternionic_4441_reconciliation.tex`, `koide_quaternion_bridge.tex`, the retained Gaussian contribution, and `chapters/residual_measure.tex` in the Nolan bridge snapshot.

This lane now has a proved comparison:

$$
H
\xrightarrow{\;\Psi=X^{-1}HX^{-*}\;}
\Psi,
\qquad
H
\xrightarrow{\;B=X^*HX\;}
B,
\qquad
B=D\Psi D,
$$

with $D=X^*X=\operatorname{diag}(C^{-1},3)$, unit real Jacobians, preserved positivity, and preserved original cubic. The same proof separates:

- the four-dimensional affine sample fibre $P^{-1}(y)$;
- the nine-dimensional parameter fibre of $H\mapsto S_H$, parametrized by $(c,\ell)$;
- the six-dimensional data-processing equality family for relative entropy, $H+P^*TP$, parametrized by $T\in\operatorname{Herm}_2(\mathbb H)$.

R1--R4 in `MATHEMATICAL_NOTE.md` contain the complete argument. This exact morphism repairs the earlier risk of treating different fibres or different markings as one object.

### 2.5 Residual action and integration

The residual source keeps

$$
N(H_\theta)=m-\rho\delta e^{2i\theta}-\overline{\rho\delta}e^{-2i\theta}
=m-\beta\cos t,
\qquad \beta=2|\rho||\delta|.
$$

R3 proves three distinct loci:

$$
\begin{array}{ll}
m+\beta\le0 &: \text{no positive matrix on the orbit},\\
-\beta<m\le\beta &: \text{a positive part exists but its conditional Gaussian-mass integral diverges},\\
m>\beta &: \text{the whole orbit is positive and the mass integral is finite}.
\end{array}
$$

On the finite locus the exact average is

$$
\frac{\pi^6m}{(m^2-\beta^2)^{3/2}},
$$

which is strictly larger than the value obtained by substituting the mean cubic into the nonlinear mass. This creates an exact integrability-defect space rather than discarding the failing locus.

R8 continues this calculation for every exponent $p>0$. On $m\le-\beta$, the positive set is empty, so the unnormalized moment is zero and the conditional moment is undefined. At a simple boundary crossing $-\beta<m<\beta$, the positive-part integral of $N^{-p}$ is finite exactly for $p<1$. At the tangency $m=\beta$, it is finite exactly for $p<1/2$. On $m>\beta$, R8 evaluates every moment by a convergent hypergeometric series and, for integer $p$, by derivatives of $(m^2-\beta^2)^{-1/2}$.

### 2.6 Finite quantum dynamics built from the full Gaussian law

R4 embeds every normalized law in the common space $L^2(\mathbb R^{12},d^{12}x)$. R5 adds specified finite-system data $(e_a,E_a,b_a)$ and proves a completely positive, trace-preserving phase channel. Its coherence multiplier retains the full covariance:

$$
C^H_{ab}(\tau)=e^{-i\tau(E_a-E_b)/\hbar}
\exp\!\left[-\frac{\tau^2}{4}b_{ab}^{T}\mathscr L(H)^{-1}b_{ab}\right].
$$

The exact Schur-coordinate factorization keeps both contributions,

$$
\alpha_{ab}^{T}\mathscr L(S)^{-1}\alpha_{ab}+\frac{|\gamma_{ab}|^2}{c}.
$$

Observation-only coefficients kill the second term and see only $S_H$. R7 proves that one six-level channel with fifteen pair-coherence magnitudes recovers the full $H$; both the magnitude count and the level count are minimal for this measurement class. One four-level observation-only channel recovers $S_H$ from six pair magnitudes, with the minimum possible counts, while retaining exactly the nine-dimensional $(c,\ell)$ ambiguity. The family

$$
H_r=I+\frac{r-1}{3}uu^*,\qquad r>0,
$$

is an explicit witness: every member has the same observed $S=C^{-1}$, while $N(H_r)=r$, $Z(H_r)=\pi^6/r^2$, and a specified hidden probe has damping $e^{-3\tau^2/(4r)}$.

R6 proves that the static $\tau^2$-damping family is generally not a homogeneous semigroup, but it is CP-divisible. The separately defined integrated phase variable $Y_\tau$, with covariance $\tau_c\tau\Sigma_H$, supplies the homogeneous GKLS clock and has units $TQ$, distinct from the static parameter's units $Q$. These results do not select the pointer basis, energies, coefficients, field commutation relations, environmental fragments, or a histories functional.

### 2.7 Zeta and heat cross-references

The catalogue routes 1,022 versions into the zeta/heat lane, including marked arithmetic action, three-point heat packets, Connes-related material, and historical RH bridge documents. Six entered through exact headings that identify a nonstandard Riemann-hypothesis bridge in original GCT sources. These sources remain cross-references. The recovered Connes--Marcolli TeX is decoded losslessly and structurally indexed.

No normalized or completed zeta object is accepted as a replacement for the original zeta function. Before any historical heat, trace, determinant, or positivity conclusion can be carried forward, the exact comparison must restore the original zeta function, the full completion multiplier, Gamma factors, powers of pi, endpoint factors, zeros, poles, trivial-zero terms, every derivative contribution, domains, and exceptional points. That reconstruction is still pending.

### 2.8 Protected programme boundaries

Finite-quantum and Yang--Mills-related files appear in the custody corpus because source tasks cross-referenced them. The first cue-reading tranche now names 8 Yang--Mills cross-reference versions and 2 Navier--Stokes cross-reference versions without accepting their mathematical claims. It also identifies 7 GCT/arithmetic versions and 23 primary S6 versions by exact source lines. The current mathematical note proves only the stated finite-dimensional channel. It does not take over the continuing Yang--Mills or Navier--Stokes programmes and does not propagate historical claims into those mains. Withdrawn timeline and identity-square material remains excluded from current reading paths.

## 3. Current proved results and proof locators

| Result | Exact content | Proof |
|---|---|---|
| R1 | Moore cubic, realification determinant, Gaussian mass, real covariance, quaternionic moment | `MATHEMATICAL_NOTE.md`, Section 1 |
| R2 | Two markings, Jacobians, Schur coordinates, disintegration, and three distinct fibres | Section 2 |
| R3 | Residual positivity and integrability classification, exact orbit average, exact examples | Section 3 |
| R4 | Common Hilbert lift, affinity, derivative metric, local coefficient | Section 4 |
| R5 | CPTP phase channel, environment dilation, observed/conditional factorization | Section 5 |
| R6 | Static-law obstruction, CP-divisibility, Brownian GKLS law, noiseless blocks, units | Section 6 |
| R7 | Minimal six-level full tomography, minimal four-level observed tomography, exact ambiguity and witness family | Section 7 and `TOMOGRAPHY_DESIGN.md` |
| R8 | All residual negative-power moments, exact no-crossing values, and sharp simple-zero/tangency thresholds | Section 8 |

The proofs retain the original coordinates and formulas. `checks/MATHEMATICAL_CHECKS_V2.json` separates exact symbolic checks from numerical evidence and records the figure-generation inputs. The checks support the arguments and do not replace them. The earlier `MATHEMATICAL_CHECKS.json` remains a superseded historical receipt.

## 4. Coherent status

The measured-fibre lane is the most advanced part of this consolidation because its connecting maps and new consequences now have complete proofs. The analytic candidate, cusp/spectral, arithmetic-selector, lattice/Jordan, and original-zeta lanes have complete custody and structural routing but only bounded semantic reading. The correct global object is therefore a source-indexed research programme with one newly completed mathematical component, not a single completed theorem.
