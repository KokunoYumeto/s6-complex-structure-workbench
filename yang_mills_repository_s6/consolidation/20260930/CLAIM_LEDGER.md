# Claim, correction, and strengthening ledger

This ledger records source claims whose status changes in the consolidation. A correction is propagated only as far as its proof warrants. A strengthening is not attributed to the historical source unless the source contains it. No novelty claim is made.

## MC-001 — marking conventions and fibre separation

**Risk in the received material.** The Jordan marking $\Psi=X^{-1}HX^{-*}$, sample precision $B=X^*HX$, affine sample fibre, parameter fibre, and data-processing equality family for relative entropy could be read as different presentations of one fibre.

**Exact correction.** R2 proves

$$
B=D\Psi D,\qquad D=X^*X=\operatorname{diag}(C^{-1},3),
\qquad \xi=X^*q=D(X^{-1}q).
$$

All changes have real Jacobian one and preserve positivity and the original cubic. The affine sample fibre has dimension four, the parameter fibre of $H\mapsto S_H$ has dimension nine, and the equality family $H+P^*TP$ has dimension six.

**Proof locator.** `MATHEMATICAL_NOTE.md`, R2.

**Propagation.** Every discussion of measured fibres, conditional densities, information loss, and tomography must state which of these three fibres it uses. The exact surface Jacobian nine on $P^{-1}(y)$ and the full conditional normalization are retained. The scalar vacuum maps to $B=vD$ and $\Psi=vD^{-1}$, so neither marked vacuum is replaced by $vI$.

**Status.** Correction proved and propagated into R2, R5, R7, the map figure, and the master map.

## MC-002 — nonlinear residual averaging

**Risk in the received material.** Replacing the residual cubic by its orbit mean before evaluating $Z(H)=\pi^6/N(H)^2$ discards the nonlinear fluctuation and can hide divergence at the positivity boundary.

**Exact correction and strengthening.** With the original residual action,

$$
N(H_\theta)=m-\beta\cos t,\qquad \beta=2|\rho||\delta|.
$$

A positive point exists exactly when $m+\beta>0$. The whole orbit is positive and the conditional mass average is finite exactly when $m>\beta$. On that locus,

$$
\mathcal A Z=\frac{\pi^6m}{(m^2-\beta^2)^{3/2}}>\frac{\pi^6}{m^2}.
$$

For $-\beta<m\le\beta$, the positive part has nonzero measure but the conditional mass integral diverges. R8 strengthens the calculation for every exponent $p>0$: on $m\le-\beta$, the positive set is empty and the unnormalized moment is zero while no conditional moment is defined; at a simple crossing $-\beta<m<\beta$, the positive-part integral of $N^{-p}$ is finite exactly for $p<1$; at the tangency $m=\beta$, it is finite exactly for $p<1/2$. On $m>\beta$, R8 gives the complete hypergeometric value and an exact derivative formula for every integer exponent.

**Proof locator.** `MATHEMATICAL_NOTE.md`, R3 and R8.

**Propagation.** Any residual-orbit calculation involving $N^{-2}$, a squared potential, or another singular nonlinear function must integrate the original function on its actual domain. The source's nonempty-positive-image criterion remains correct; it is now separated from whole-orbit positivity and integrability. The divergence locus is retained as the integrability-defect space.

**Status.** Correction and underclaimed consequences proved. Exact examples and figures added.

## MC-003 — static dephasing and CP-divisibility

**Risk in the received material.** Failure of the static Gaussian $\tau^2$ law to satisfy a homogeneous semigroup identity could be treated as failure of every Markovian divisibility property.

**Exact strengthening.** R6 proves that the static family is a homogeneous semigroup exactly when all coupling vectors $b_a$ coincide. For every $\tau\ge s\ge0$, however, the ratio channel is completely positive and uses the stochastic clock $\sqrt{\tau^2-s^2}$ and deterministic phase clock $\tau-s$. Thus the family is CP-divisible. Its time-local dissipative coefficient is proportional to $\tau$.

**Further exact construction.** The separately defined integrated phase variable $Y_\tau$, with covariance $\tau_c\tau\Sigma_H$, gives a homogeneous Gaussian convolution semigroup with a complete GKLS generator. Its units are $[Y_\tau]=TQ$, distinct from the static parameter units $[x]=Q$. The parameter $\tau_c$ and every factor are retained.

**Proof locator.** R5--R6.

**Propagation.** Static-variable dephasing and Brownian phase noise must no longer be interchanged. Any semigroup assertion must name its clock and covariance law. The finite channel remains an added model; no existing S6 action is relabelled as dynamics.

**Status.** Underclaim strengthened and the overbroad inference corrected.

## MC-004 — identifiability and observation loss

**Risk in the received material.** Covariance injectivity of the full Gaussian law could be conflated with identifiability from the observation map alone.

**Exact correction and strengthening.** The earlier 78-probe construction treated the real covariance as an unrestricted symmetric $12\times12$ matrix and therefore missed the fifteen-dimensional quaternionic Hermitian structure. R7 replaces it with one six-level channel whose fifteen pair-coherence magnitudes recover $H^{-1}$, hence $H$. The displayed integer measurement matrix has determinant $-2^{12}$. Fifteen scalar magnitudes and six levels are both minimal in this measurement class. If every coefficient factors through $P_{\mathbb R}^T$, one four-level channel with six pair magnitudes recovers exactly $S_H$; its measurement determinant is $-2^4$, and the remaining ambiguity is precisely the nine parameters $(c,\ell)$.

The witness

$$
H_r=I+\frac{r-1}{3}uu^*,\qquad r>0,
$$

has constant observed $S=C^{-1}$, while its mass, affinity, relative entropy, and a hidden-probe coherence all depend explicitly on $r$.

**Proof locator.** R7 and `TOMOGRAPHY_DESIGN.md`.

**Propagation.** Every recovery claim must specify the available coefficient vectors. “The law determines $H$” applies to the full law or an informationally complete probe design. “Observation determines $S$” leaves exactly the proved parameter fibre.

**Status.** Scope correction and constructive strengthening proved.

## MC-005 — finite measure versus normalized probability

**Risk in the received material.** Normalizing the Gaussian could suppress the parameter-dependent mass and make different measures appear equivalent after whitening.

**Exact correction.** R1 proves and retains both

$$
d\mu_H=e^{-q^*Hq}d^{12}q,\qquad
Z(H)=\frac{\pi^6}{N(H)^2},\qquad
dp_H=Z(H)^{-1}d\mu_H.
$$

The fixed-coordinate covariance is $\frac12\mathscr L(H)^{-1}$, and $\mathbb E_H[qq^*]=2H^{-1}$. R4 embeds the normalized laws in one common Hilbert space rather than using a parameter-dependent reference space.

**Proof locator.** R1 and R4.

**Propagation.** Both $Z(H)$ and $p_H$ accompany every later comparison. Whitening may be used only with its explicit change of variables and Jacobian.

**Status.** Proved and propagated through R3--R8.

## MC-006 — global S6 recognition remains a source claim

**Risk in the corpus.** Local gluing, cohomological checks, compilation, and repeated historical summaries could be read as a completed global recognition theorem.

**Exact status.** The current audit has structural routes and bounded readings, but no complete chain proving that the glued global candidate is the intended S6 object. Local compatibility and numerical checks do not supply the missing global morphism or recognition theorem.

**Required continuation.** Fix one exact candidate version; reconstruct its cover, transition maps, cocycles, singular or boundary loci, global topology, and every recognition invariant from the original formulas. Prove the maps between analytic, topological, and group-action presentations. Record any obstruction as the definition of its exact defect space and continue from that object.

**Status.** Unresolved; no theorem accepted or rejected.

## MC-007 — original-zeta reconstruction is pending

**Risk in the corpus.** Historical heat, trace, determinant, or positivity formulas may use a completed, rescaled, or normalized zeta object as the working replacement for the original zeta function.

**Exact status.** The zeta/heat lane is indexed and retained. No affected conclusion is carried forward as established until its calculation is reconstructed with the original zeta function explicit, including the full completion multiplier, Gamma factors, powers of pi, endpoint factors, zeros, poles, trivial-zero contributions, derivative terms, domains, exceptional points, and support data.

**Required continuation.** Choose each receiving heat or determinant statement by dependency order, recover its exact source definition, prove the comparison map without replacing the original object, and propagate every restored term through the receiving formula.

**Status.** Open audit obligation.

## MC-008 — corpus counts are not mathematical acceptance

**Risk in the audit.** Structural totals can create an appearance of exhaustiveness.

**Exact correction.** The V2.1 catalogue proves coverage of registered bytes, explicit nested-package placements, recursive logical member occurrences, and specified lexical structures. It does not prove a theorem, choose an authoritative historical branch, establish literature novelty, or recover the 2,039 missing original histories.

**Propagation.** Every master-map entry carries one of the evidence statuses defined in `README.md`. Source claims remain distinguishable from current proofs.

**Status.** Audit rule applied throughout this reader.

## MC-009 — nested-package multiplicity and a direct-member collision

**Failure in the first consolidation.** The first catalogue expanded each distinct nested ZIP byte version once and called its 12,822 file definitions “nested member occurrences.” Repeated placements were counted but not represented. Its global key $(\text{outer archive},\text{member name})$ was also mutable during nested expansion. A nested 4,078-byte `MANIFEST.json` therefore overwrote the binding for a later 52,910,440-byte direct `MANIFEST.json`, and V1 assigned the nested file's SHA-256 to the direct entry.

**Exact correction.** `catalogue/CORPUS_CATALOGUE_V2_PUBLIC.sqlite` separates package versions, direct package placements, package-member definitions, containment edges, and recursively expanded logical occurrences. It contains 214 direct package placements, 56 distinct package byte versions, 12,822 package-file definitions, and 29,324 logical nested entry occurrences, of which 24,564 are text occurrences. Every outer archive SHA-256 was recomputed. All 41,695 direct text mappings were compared with their ZIP byte count and CRC32; the single mismatch was reread from the outer archive and assigned the exact SHA-256 `cc0bc89d33fd580a51a1239ba7a9c875098b43dbc327d33bdbc14312dae16b0d`. No mismatch remains.

**Proof locator.** `catalogue/CATALOGUE_V2_PUBLIC_RECEIPT.json`, `checks/DIRECT_TEXT_MAPPING_AUDIT.json`, `catalogue/ARCHIVE_MEMBER_COVERAGE_V2_PUBLIC.jsonl.gz`, and the V2 database relations.

**Propagation.** The 12,822 value may be described only as distinct-package file definitions. Reader totals use the 29,324 logical-entry and 24,564 logical-text occurrence counts when multiplicity matters. The V1 database and receipts remain historical evidence and are marked superseded for occurrence claims.

**Status.** Catalogue defect reproduced, corrected, and independently validated by SQLite integrity and foreign-key checks.
