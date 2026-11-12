# Independent Mathematical Proof Audit

## Manuscript audited

**Claim:** a compact complex threefold constructed as a torus fibration over \(\mathbb P^1\) is diffeomorphic to \(S^6\), yielding an integrable complex structure on the six-sphere.

**Source audited:** `s6_canonical_full_108_pages.tex` and the matching 108-page canonical PDF.

**Audit standard:** every indispensable implication must either be checked exactly, reduced to a cited standard theorem with its hypotheses verified, or marked unresolved. Numerical agreement, internal consistency, and absence of an obvious contradiction are not treated as proof.

## Disposition

> **MAJOR REVISION - MAIN THEOREM NOT CERTIFIED.**

I found **no explicit arithmetic contradiction** and **no concrete local analytic error** in the construction through the gluing of the three local fillings. The exact finite algebra in Sections 2, 5, 7, and Appendix A is reproducible and passes independent computer-algebra checks.

The proof nevertheless does not yet meet a certification standard because the global topology depends on geometric maps whose asserted integral effect has not been independently established in the supplied argument at chain level. In particular, the proof of the \(S^6\) identification requires all of the following to be correct simultaneously:

1. the cusp filling has the asserted homotopy/collapse model;
2. the specialization map \(H_q(F;\mathbb Z)\to H_q(W;\mathbb Z)\) is the stated quotient, integrally and with the stated orientations;
3. the overlap inclusions used by van Kampen impose exactly the displayed twist relations;
4. the Mayer--Vietoris or Leray differentials are represented by the displayed integral matrices in the claimed geometric bases.

The downstream Smith-normal-form calculations are correct **after those identifications are granted**. They do not themselves prove the identifications.

## 1. Claim chain and audit result

| Manuscript stage | Pages | Audit result | Reason |
|---|---:|---|---|
| Lattice and monodromy data | 8-13 | **Exact pass** | Integer matrices, invariant lattices, coinvariants, exterior powers, and alternating form checked exactly. |
| Period family | 14-23 | **Reviewed; no error found** | Transformation laws, torsor construction, cusp asymptotics, determinant identity, and equivariance are internally coherent. This is not a formal verification of the analytic existence arguments. |
| Toric cusp filling | 24-31 | **Reviewed; no local error found** | Fan smoothness, free proper action estimate, compact quotient, central fibre, and overlap map are coherent. The later topological collapse is a separate issue. |
| Logarithmic fillings | 31-35 | **Exact/local pass** | Finite-order action, fixed-point criterion, freeness for the chosen twists, and local quotient structure check out. |
| Global complex gluing | 36-39 | **Reviewed; no error found** | The quotient atlas, Hausdorff argument, properness, and connectedness are coherent once the local models are accepted. |
| Fundamental group and homology | 40-62 | **Not certified** | Algebraic reductions pass conditionally, but the geometric overlap and specialization maps require an independent integral chain-level proof. |
| Recognition as \(S^6\) | 63-66 | **Conditional pass** | Standard once simple connectivity and integral homology-sphere status are established. |
| Complex-analytic invariants | 64-94 | **Conditional/consistency pass** | No topological, Hodge, or Riemann--Roch contradiction found; all conclusions remain conditional on existence and topology of \(X\). |
| Appendices | 95-108 | **Supporting exact checks; topology still conditional** | Matrix and cell computations are useful evidence, but the crucial identification of their algebraic maps with the actual geometric maps remains the unresolved point. |

## 2. Exact calculations that pass

### 2.1 Monodromy matrices

Using the matrices printed in Section 2, exact integer arithmetic verifies:

\[
\det T_1=\det T_2=1,\qquad T_1^3=I,\qquad T_2^4=I,\qquad T_2^2\ne I.
\]

With \(T_0=(T_1T_2)^{-1}=I+N\),

\[
N^2=0,\qquad \operatorname{rank}N=2.
\]

For the contragredient matrices

\[
A_j=(T_j^{-1})^{\mathsf t},\qquad M_0=(T_0^{-1})^{\mathsf t},
\]

one obtains exactly

\[
A_1A_2M_0=I.
\]

The Smith normal forms of \(A_1-I\), \(A_2-I\), and \(M_0-I\) have nonzero diagonal entries \((1,1)\). The combined coinvariant block has nonzero Smith entries \((1,1,1)\), giving a free rank-one coinvariant group.

### 2.2 Distinguished lattices and twists

The computations verify

\[
\ker(M_0-I)=\operatorname{im}(M_0-I)=\langle\widehat w,\widehat\delta\rangle,
\]

\[
\Lambda^{A_1}=\langle\varepsilon,\widehat\delta\rangle,
\qquad
\Lambda^{A_2}=\langle\varepsilon',\widehat\delta\rangle,
\]

where

\[
\varepsilon=\widehat\gamma+2\widehat u-4\widehat w,
\qquad
\varepsilon'=\widehat\gamma+3\widehat u-3\widehat w.
\]

For the manuscript's choices

\[
v_1=\varepsilon,\qquad v_2=-\varepsilon',
\]

one has

\[
(\ell_0,\ell_1,\ell_2)=(0,1,-1).
\]

The freeness criteria in Proposition 5.6 are therefore satisfied:

\[
3\nmid\gamma(v_1),\qquad \gamma(v_2)\text{ is odd}.
\]

### 2.3 Invariant alternating form

Solving the integral invariance equations

\[
T_j^{\mathsf t}QT_j=Q\quad(j=1,2)
\]

for alternating \(Q\) gives a rank-one lattice generated by the form

\[
Q_0(\gamma,\delta)=1,\qquad Q_0(u,w)=6,
\]

with all other independent pairings zero. This agrees with Lemma 2.8. The induced form \(Q_0(x,Ny)\) on \(V/\ker N\) has matrix \(\operatorname{diag}(6,-1)\).

### 2.4 Conditional fundamental-group arithmetic

The exact group and lattice algebra gives the manuscript's order formula

\[
|p|=|12\ell_0-4\ell_1-3\ell_2|.
\]

For \((0,1,-1)\),

\[
p=-1,
\]

so the resulting cyclic group is trivial. The base-orbifold elimination is also exact: once the cusp meridian and the two elliptic meridians are related as claimed by the overlap inclusions, the relations of orders \(3\) and \(4\) force the remaining generator to be trivial because \(\gcd(3,4)=1\).

This is a **conditional certificate**: it verifies the algebra after the geometric maps are supplied; it does not prove that the actual inclusions of the overlaps induce precisely those relations.

### 2.5 Downstream consistency checks

The displayed integral matrices in the topology computation have the claimed ranks and Smith normal forms. Under the manuscript's asserted geometric identifications they produce

\[
H_k(X;\mathbb Z)=
\begin{cases}
\mathbb Z,&k=0,6,\\
0,&0<k<6.
\end{cases}
\]

The complex-analytic invariants are also numerically consistent with a complex structure on a homology six-sphere:

- \(H^2(X;\mathbb Z)=H^4(X;\mathbb Z)=0\) gives \(c_1=c_2=0\);
- \(\int_Xc_3=e(X)=2\);
- Hirzebruch--Riemann--Roch gives \(\chi(\mathcal O_X)=c_1c_2/24=0\), matching the stated \(h^{0,q}\);
- the same calculation gives \(\chi(T_X)=\tfrac12\int_Xc_3=1\), matching the manuscript's stated value.

These checks rule out several easy inconsistencies. They do not establish existence.

## 3. Critical unresolved proof obligations

### 3.1 Cusp-neighbourhood homotopy model

**Relevant manuscript material:** Proposition 7.2 and Lemmas 7.5--7.10, pages 40-50; toric construction, pages 24-31.

The proof uses a sequence of straightening, polar decomposition, positive-part retraction, phase spreading, and fixed-fibre collapse maps. For certification, one must prove that the composite:

1. is continuous across every toric stratum, including double and triple loci;
2. is equivariant for the full \(\bar\Lambda\)-action;
3. descends to the quotient \(N_0\);
4. yields the claimed map of pairs and the claimed specialization map on integral homology.

The manuscript provides geometric formulas and local arguments, but the audit did not obtain a complete independent chain homotopy or cellular model verifying all four properties simultaneously. This is indispensable because later calculations use the exact induced map, not merely its rational rank.

### 3.2 Integral specialization map

**Relevant manuscript material:** Proposition 7.12, pages 50-52; Appendix B, pages 100-108.

The claimed formula is

\[
\ker\bigl(c_*:H_q(F;\mathbb Z)\to H_q(W;\mathbb Z)\bigr)
=(\bigwedge^qM_0-I)\bigwedge^q\Lambda,
\]

with \(c_*\) surjective.

An integral proof must control:

- saturation of every image;
- torsion, not only ranks over \(\mathbb Q\);
- identification of the nearby-cycle edge map with the geometric collapse map;
- orientations and signs in degree three;
- compatibility with the bases later used in Mayer--Vietoris.

Appendix B supplies a sophisticated nearby-cycle calculation and rank arguments. The remaining certification burden is the exact integral identification of those spectral-sequence maps with the geometric maps used in Section 7. Until that identification is independently reproduced, the homology-sphere conclusion is conditional.

### 3.3 van Kampen inclusion maps

**Relevant manuscript material:** Theorem 7.17 and its preparatory lemmas, pages 52-57; zero-section drift, pages 38-40.

The final group simplification is correct once the inclusion maps from the three boundary mapping tori are granted. What still requires independent proof is that the actual inclusions encode exactly:

- the monodromy relations \(A_1,A_2,M_0\);
- the logarithmic drifts \(-v_1,-v_2\);
- the cusp gluing class \(\ell_0\);
- the manuscript's meridian-orientation convention.

A sign error changes \(p=12\ell_0-4\ell_1-3\ell_2\), and a primitive-versus-multiple error changes the group itself. The executable certificate therefore labels the result conditional rather than treating the correct final simplification as evidence for the geometric inputs.

### 3.4 Mayer--Vietoris and Leray boundary maps

**Relevant manuscript material:** Sections 7.6-7.7, pages 57-62; Appendices A-B, pages 95-108.

The manuscript presents two routes to the homology calculation. They are valuable cross-checks, but they are not fully independent at the point that matters: both use the same monodromy and specialization geometry. The finite matrices pass exact verification. Certification still requires a complete geometric derivation of those matrices in the actual integral bases of the overlaps, including transfer indices, orientations, and primitivity.

A satisfactory revision would include either:

- an explicit finite CW model for \(X\) with all cellular boundary matrices printed and derived from the attaching maps; or
- a fully functorial nearby-cycle/Mayer--Vietoris proof that identifies every edge and boundary map integrally, with a separate chain-level check of the van Kampen maps.

## 4. Steps that are valid once topology is established

### 4.1 Recognition of the smooth manifold

If \(X\) is a closed smooth simply connected integral homology six-sphere, the recognition argument in Section 8 is standard: Hurewicz and Whitehead make it a homotopy sphere, and the vanishing of the group of smooth homotopy six-spheres identifies it diffeomorphically with the standard \(S^6\). I found no issue in this conditional step.

### 4.2 Complex-analytic calculations

The Neron--Severi, algebraic-dimension, direct-image, canonical-bundle, holomorphic-form, vector-field, and fixed-locus calculations are internally consistent with the earlier construction. I found no numerical contradiction. They cannot rescue an unproved topology step, and the discussion of a conflict with previously published work is not evidence that the construction is correct; the construction must stand on its own.

## 5. Theorem-level audit classification

The accompanying CSV ledger assigns each theorem-like statement one of the following statuses:

- **VERIFIED-EXACT:** independently checked by exact algebra or a complete elementary argument;
- **REVIEWED-NO-ERROR-FOUND:** read for hypotheses and logical coherence, with no concrete defect found, but not formalized;
- **CONDITIONAL-PASS:** correct after an earlier unresolved statement is granted;
- **CRITICAL-UNRESOLVED:** indispensable to the main theorem and not independently certified;
- **SECONDARY:** not needed for the existence or \(S^6\) identification.

The ledger deliberately does not convert “no error found” into “proved.”

## 6. Evidence and reproducibility

The evidence bundle contains:

1. the canonical TeX and PDF reviewed;
2. this report in Markdown and PDF;
3. an audit-annotated copy of all 108 manuscript pages;
4. a PDF of the critical evidence pages;
5. page-range source and text extracts;
6. theorem and proof-risk ledgers;
7. exact matrix, lattice, exterior-power, chain-matrix, Hodge, and topology checks;
8. a portable `reproduce_core_checks.py` script;
9. checksums and a clean verification script.

The exact checks are deterministic. Running `run_all_checks.sh` in the evidence bundle verifies the static checksums and reruns the core algebraic audit.

## 7. Final peer-review recommendation

The manuscript contains a detailed and mathematically serious construction. The exact algebra and local models survive substantial checking, so rejection on the basis of an elementary matrix or parity error is not supported by this audit.

The claimed complex structure on \(S^6\), however, is **not established to a rigorous certification standard by the supplied evidence**. The paper should receive **major revision** centered on a self-contained, independently checkable integral topology package for Section 7 and Appendix B. Until that package is supplied and verified, the proper status of the main theorem is **unconfirmed**, not proved and not disproved.
