**Superseded development record:** the fully refereed proof is now in `B_fixed_partial_noncompletion.tex` (B.4.30). Its direct coefficient-ideal equidimensionalization replaces the flattening dependency below, and its simultaneous product-root construction incorporates the final referee corrections. The earlier text is retained for provenance.

# Working proof: two extending sections at a maximal torus degeneration

Status: uninput working proof, 15 November 2026. No numbered result or CSV is promoted by this file. The one-parameter argument has independent preliminary review by boundary_d. The uniform argument and final trace construction require full-source review. This concerns completion of the fixed partial family B.4.19; it does not yet exclude arbitrary r-only fillings whose r=0 axial completion differs.

## 1. Exact primary input and the erratum

Illusie, L., Kato, K., & Nakayama, C. (2005). Quasi-unipotent logarithmic Riemann–Hilbert correspondences. Journal of Mathematical Sciences, the University of Tokyo, 12, 1–66. Original publisher PDF: https://www.ms.u-tokyo.ac.jp/journal/pdf/jms120101.pdf . Opened and read Theorem 6.2 on printed p.32 and Theorem 6.3 on p.34. For a proper separated log-smooth analytic morphism, with log-smooth base or exact morphism, and torsion-free cokernels of characteristic groups, Theorem 6.3 gives locally free ordinary relative log-de Rham cohomology and its identification, with Gauss–Manin connection, with the nilpotent logarithmic Riemann–Hilbert extension of log Betti cohomology. No projective or Kähler hypothesis occurs. The constant sheaf is the coefficient system used here.

Illusie, L., Kato, K., & Nakayama, C. (2007). Erratum to “Quasi-unipotent logarithmic Riemann–Hilbert correspondences.” Journal of Mathematical Sciences, the University of Tokyo, 14, 113–116. Original publisher PDF: https://www.ms.u-tokyo.ac.jp/journal/pdf/jms140105.pdf . Opened in full. It repairs the proof of the algebraic Hodge-to-de-Rham statement Theorem 7.1, not Theorem 6.3. This proof does not use Theorem 7.1 or general analytic Hodge degeneration.

Kajiwara, Kato and Nakayama, Analytic log Picard varieties (2008), Definition 7.1(i), pp.164–165, and §9.2, p.173, explicitly make the same distinction: the comparison condition follows from IKN6.3 without projectivity, whereas their further Hodge conditions have additional hypotheses. Full PDFs are saved outside the deliverable under external_sources/E_completion/IKN2005LogRH.pdf and IKN2007Erratum.pdf; searchable text files accompany them. Web opens: turn639view0, turn639view1; exact theorem reads: turn640view0 and turn641view0/1. These identifiers are an audit trail, not substitutes for bibliographic citations.

## 2. The semistable setup, including a transverse parameter

Let f:Z→Δ_t×V be proper, with connected fibres, where V is a small disc (or a point). Assume Z is smooth and the map is semistable relative to V. Thus at every central point there are coordinates

    (x_1,...,x_k,z_1,...,z_{3-k},u),   t=x_1...x_k,   u=u,

with k≤3 and u the coordinate of V; suppress u when V is a point. The noncentral fibres are two-dimensional complex tori, viewed as torsors under a specified Jacobian family. Its integral H_1 lattice is Λ of rank four; the monodromy T=1+N has N²=0 and rank N=2. Suppose

    ker(N:Λ→Λ)=W=Zw_1⊕Zw_2

is the primitive cocharacter lattice used in a multiplicative presentation of the specified Jacobian. Its normalized invariant forms ω_1,ω_2 have integrals 2πi δ_ij on w_j. Suppose their span is a holomorphic rank-two subbundle F_A of the canonical nilpotent extension H of H¹ over Δ×V.

For the actual family, these hypotheses hold at every generic exceptional divisor of a point-blown-up base: q=t^a times a unit and r=t^b times a unit, with a,b>0. The two diagonal valuation entries are positive, and the kernel is exactly Zw⊕Zδ. In the actual period matrix, subtracting the logarithmic N-columns leaves the bounded holomorphic unit periods. The w,δ columns remain the identity, so the normalized form span F_A is indeed a subbundle. No assertion of full log-Hodge goodness of an unknown cap is needed.

### 2.1 Saturation supplies the normalized logarithmic forms

Write K•=Ω•_(Z/(Δ×V))(log), and H=R¹f_*K•. IKN6.3 applies to this semistable morphism: the characteristic map sends 1 to (1,...,1), whose cokernel is torsion-free. It identifies H with the canonical nilpotent extension of the known ordinary H¹ local system and makes H locally free. The log Betti system restricts to the ordinary system and is locally constant on the real oriented blowup of the base, so this is the same extension as that used to define F_A.

Set F=ker(f_*Ω¹_log→f_*Ω²_log). This is coherent because the displayed differential is O_base-linear between coherent direct images. The triangle K^{≥1}→K•→O_Z and its low-degree direct-image exact sequence give

    0 → F → H → R¹f_*O_Z.

The connecting map f_*O_Z→F is zero because f_*O_Z=O_base and the differential is relative. This argument does not invoke degeneration of the Hodge spectral sequence.

The quotient H/F has no t-torsion. Indeed D=f^{-1}(t=0) is reduced and each of its compact connected fibres over V has only constant holomorphic functions. Consequently f_*O_D=O_V. Apply f_* to

    0→O_Z --t--> O_Z → O_D →0.

The map O_base→O_V is surjective, so multiplication by t is injective on R¹f_*O_Z. Thus F is t-saturated in H. The specified F_A is also t-saturated, since H/F_A is locally free. Both have the same restriction after inverting t: holomorphic one-forms on a compact torus are closed and are exactly the invariant one-forms. Hence

    F = H ∩ F_A[t^{-1}] = F_A.

This equality holds with the transverse parameter u present. In particular the normalized ω_1,ω_2 are actual closed relative logarithmic forms on Z, not merely meromorphic cohomology classes. No base change theorem for H¹(O) at the centre, and no Kähler property of a component, is being assumed.

### 2.2 Local meridians have integral normalized periods

In a semistable chart, a small fibre retracts to (S¹)^{k−1}. Its angular generators are invariant under the local monodromy; the inclusion into the global fibre intertwines monodromy. Their images in Λ therefore belong to ker N=W. It follows that every local angular period of ω_j/(2πi) is an integer. These periods are constant in t and u: they pair the fixed integral class in W with the normalized forms. This is where maximal rank is essential. If rank N=1, ker N has rank three and can contain an additional elliptic period whose normalized value is not an integer.

### 2.3 Convergent relative logarithmic primitives

A closed relative logarithmic one-form on the chart has the form

    ω = Σ_(i<k) a_i(x,z,u) dlog x_i + Σ b_l(x,z,u) dz_l,

modulo dlog t. First integrate the ordinary z directions by the usual holomorphic homotopy formula. The remaining coefficients depend on x and u. Expand them as convergent series in x. For a monomial x^α, its relative weight is

    (α_1−α_k,...,α_(k−1)−α_k).

Closedness says that the coefficient vector of this monomial is proportional to that integer weight. If the weight is nonzero, divide by one nonzero weight entry to obtain a holomorphic primitive for that monomial. The denominator has absolute value at least one, so the primitive series converges on every sufficiently smaller polydisc. If the weight is zero, α_1=...=α_k and the monomial is t^n. These resonant terms give base-dependent dlog coefficients. Their angular periods are exactly those coefficients; since the periods of ω are constant integers, all nonconstant resonant coefficients vanish and the constant coefficients are integers.

Thus, after shrinking the chart,

    ω_j = d_rel h_j + Σ_(i<k) n_ij dlog x_i,    n_ij∈Z,

with h_j holomorphic in all variables, including u. The exponentiated primitive

    χ_j = exp(h_j) ∏_(i<k) x_i^{n_ij}

is a genuine meromorphic function whose divisor is supported on the central coordinate branches. Its logarithmic differential is ω_j relatively. Negative integer exponents are allowed: these are log characters, not necessarily holomorphic functions on the whole chart.

### 2.4 Difference of two extending sections

Let a,b be holomorphic sections of f over Δ×V. Fix u_0. The central fibre is compact and connected. Choose finitely many semistable charts whose central intersections form a chain joining a(0,u_0) to b(0,u_0). Shrink V so the same chain works for every u. Every nonempty open intersection with the reduced NC fibre contains a smooth central point. At such a point f is a submersion; choose a holomorphic transverse auxiliary section in the intersection. Thus the endpoints and all auxiliary sections are holomorphic, with no new root required at this stage.

Within one chart, evaluating χ_j at its two sections and taking the ratio gives a monomial in t times a holomorphic unit. Each section avoids all central coordinate branches when t≠0; consequently the pullback of each x_i is t^m times a unit, with an integer m≥0. Multiplying these character ratios along the finite chart chain gives a pair of log characters. On each ordinary fibre this pair is the exponential of the integral of (ω_1,ω_2) along a path from a to b, so its class modulo the specified period lattice is exactly b−a in the Jacobian. Changing the path adds an integral period. Since the pairing has full positive rank along t=0, every integral ghost vector is bounded in the KKN sense. Therefore b−a extends as a section of the specified associated logarithmic torus A.

This is a relative statement in u, obtained from holomorphic chart functions and holomorphic auxiliary sections. It does not follow merely by testing separate transverse discs. It also explains why B.4.29 is not a counterexample: in that example the reference origin does not extend under the new affine marking; the difference of two genuinely extending sections is insensitive to their common essential translation.

## 3. Obtaining this setup generically along an exceptional curve

Suppose a proper analytic completion of the fixed partial family B.4.19 exists over the bidisc. Flatten its map by a modification of the base supported at the origin. Resolve the modified surface base and dominate its modification by a finite sequence of point blowups. Flatness is preserved by further base change. Retain the strict transform of the component dominating the base. The resulting map has relative dimension two; the exceptional base locus is a compact tree of rational curves.

At the generic part of one exceptional curve E, resolve the total space and the inverse image of E, preserving the ordinary torus locus. There are finitely many components and strata over the compact exceptional set. Delete from E the images of the critical loci of the strata maps to E and any nondominating strata. These are discrete analytic sets, hence finite on the compact curve. Around any remaining point, the total divisor and the transverse parameter u have local equations

    t = unit·x_1^{m_1}...x_k^{m_k},    u=u,    k≤3.

The unit can be absorbed in one local coordinate after taking a root locally. Choose a common multiple M of the finitely many m_i. After t=τ^M and normalization, the local model is toroidal, with integral height-one vertices. A compatible triangulation of the height-one lattice polygons, using all their lattice points, has unimodular triangles: a lattice triangle with no extra boundary or interior lattice point has area 1/2. The subdivisions agree on shared edges after inserting all edge lattice points. They give a proper smooth toric modification with reduced normal-crossing τ-fibre. These operations are uniform in u and are unchanged on τ≠0. No projective or Kähler assumption on the original cap is used; only analytic resolution and these finite local toric modifications are used. The polynomial local toric modifications glue because their ideals are monomials in the globally marked divisor branches; a common refinement handles overlaps. This paragraph needs final referee attention to its compatibility and source scope.

Local finite multisections of the flat map split into honest holomorphic sections after an additional finite cyclic root at a generic point of E. A proper modification has a meromorphic lift of each such section; its indeterminacy on the two-dimensional section base is isolated, so deleting finitely many further points of E makes the lift holomorphic. Equivalently, resolve the finite section surface and restrict away from the exceptional images. Only finitely many multisections and exceptional curves are used below, so a single finite bound on all required root degrees is available after stratifying those curves.

On this semistable cover, §2 applies to any two resulting extending sections. Therefore the difference of the two traces extends as an A-section after the cyclic root. Taking its multiplicative norm gives a positive integer multiple of the difference on the original base. Explicitly, for a character τ^k u(τ,u_0) on a cover t=τ^e, its norm is

    ∏_(j=0)^(e−1) (ζ_e^j τ)^k u(ζ_e^j τ,u_0)
      = (−1)^{k(e−1)} t^k · unit.

Changing a character lift by a period changes the norm by an integral period; the periods themselves descend from the original base. Thus the norm gives an actual A-section downstairs and equals e times the original ordinary Jacobian section. At a generic exceptional divisor all character ghosts are bounded. This norm argument is on ordinary analytic sites and does not presume Kummer descent for the quotient sheaf.

## 4. Hartogs for sections of A, with the Y ambiguity retained

Let p be a point of the smooth modified base and take a sufficiently small bidisc V_p about p, with its normal-crossing boundary. Put V_p^*=V_p\{p}. The period lattice sheaf Y=Z² is constant here, and H¹(V_p^*,Y)=0 because the punctured bidisc retracts to S³. The usual-topology exact sequence

    0→Y→T_log^(Y)→A→0

therefore lifts every A-section on V_p^* to a section of T_log^(Y).

B.4.27 identifies the exact bounded sheaf on the modified base as M_(D_Q+E)^gp × M_(D_Q+D_R+E)^gp. For either lifted character, its divisor order along each boundary branch is a fixed integer. Divide by the corresponding local boundary monomial. The result and its inverse are holomorphic on the punctured bidisc, so ordinary Hartogs extends both. Their product remains one. Restoring the monomial gives an extending bounded character; the forbidden strict-r order of the first character stays zero. Hence the A-section extends across p.

The extension is unique. Locally lift the difference of two extensions to T_log^(Y). On the punctured connected bidisc this lift is an integral Y-period, locally constant and therefore constant. Subtract that period and use the identity theorem for its two characters. Thus the A-section is zero on the whole bidisc. This uniqueness also preserves all cocycle identities across the missing points. The result concerns A-sections; H¹ of A on a punctured bidisc can be nonzero and torsors need not extend.

## 5. Gluing multiplied trace origins and the fixed-partial-family contradiction

Choose a finite open cover U_i of a neighbourhood of the compact exceptional tree in the modified base S. Flatness supplies on each U_i a finite multisection V_i→U_i of positive degree d_i, obtained by a transverse local analytic slice and a finite representative. Let d be a common positive multiple of the finitely many d_i. On U_i minus the exceptional tree, the trace of V_i, multiplied by d/d_i, is a section t_i of the d-fold contracted product P^d of the actual punctured A-torsor P. Along the strict transforms of the two original punctured axes, the prescribed fan models make this trace a genuine log section by the character-norm proof of B.4.26.

On an overlap, t_i−t_j is an ordinary A-section away from the exceptional tree. By §3, a positive integer multiple of every such difference extends across the generic part of every exceptional curve. Choose one common positive multiplier m for the finite collection of curves, multisections and local ramification types. Replace all t_i by m t_i; now they are sections of P^(dm). Their differences extend across every exceptional curve apart from finitely many points. Section 4 extends them across all those points, including crossings. Uniqueness makes the cocycle equations hold everywhere.

Glue trivial A-torsors on U_i, using these extended differences, to P^(dm) off the exceptional tree using the trace identifications. This constructs an A-torsor on S extending P^(dm). B.4.27 gives H¹(S,A)=0, so its restriction must be trivial. But B.4.24 proves every positive multiple of the actual punctured torsor nontrivial: its r-loop connecting class is dm·γ, which cannot be split by the two extending axial origins. This is a contradiction.

If all preceding generic-reduction and uniformity steps pass, the conclusion is: the particular actual partial filling B.4.19 has no proper analytic completion over its missing origin, even allowing a purely three-dimensional origin fibre and modifications of the base. No Kähler or projective hypothesis has entered.

## 6. Scope which must not be silently enlarged

An arbitrary smooth r-semistable filling of the original six-sphere family has a meromorphic extension of the intrinsically marked f by B.4.4. Resolving its graph makes the fixed (q,r) map holomorphic, but can replace the r=0,q≠0 axial completion. Along that strict r-axis the linear monodromy has rank one. Its kernel contains an extra elliptic period, so §2.2 does not force integral residues there. The existing Hopf insertions are compatible with this distinction.

Accordingly the final contradiction currently uses the prescribed B.4.19 fan model on that axis. It cannot yet be stated as nonexistence of every r-only filling. To reach that stronger result one must either compare arbitrary r-axis caps to the prescribed log origin, or replace the fixed-A trace construction by a category controlling the extra invariant elliptic direction. This is an actual remaining gap, not a consequence of the one-parameter lemma or Hartogs.

## 7. Current audit and next checks

- IKN2005 Theorem6.3 opened directly; 2007 erratum read and scoped.
- Low-degree saturation and the local integer-weight primitive have independent preliminary D review.
- Parent independently proposed the multiplied-trace/Hartogs construction; the full written proof awaits review.
- Check generic analytic resolution/semistable reduction uniformly in u, including gluing the toric subdivisions and a common finite norm multiplier.
- Obtain a directly opened primary flattening theorem statement, in addition to Nakayama's published use of analytic flattening in Theorem7.1.3 Step3.
- Do not update a CSV, input, or global nonexistence claim until these checks are complete.

### Further primary audit before checkpoint09

Enokizono and Hashizume, *Semistable reduction for complex analytic spaces*, arXiv:2404.05124v3 (12 October 2024), original https://arxiv.org/pdf/2404.05124, was opened. Lemma2.14 on manuscript pp.6–7 proves the correspondence between proper toroidal analytic modifications and subdivisions; that lemma has no projectivity hypothesis and supports gluing the local lattice subdivisions in §3. Their full Theorem1.1 does require projectivity and is expressly not used. The introductory sentence credits one-dimensional analytic semistable reduction to KKMS; the local surface-fibre construction above is retained explicitly rather than importing the higher-dimensional projective theorem.

The original Hironaka1975 JSTOR article, DOI10.2307/2373721, was searched and its stable and PDF links were opened, but they returned an error/empty wrapper. It has not been read directly. Nakayama's original published Theorem7.1.3 Step3 already read at p.605 uses analytic flattening without adding a projectivity assumption to the putative extension. A directly readable primary flattening statement is still being sought.
