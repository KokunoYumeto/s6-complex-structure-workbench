# Part C source and computation record

## Read

- Full development prompt, 12 November 2026.
- `workbench/hodge_frolicher.tex`, opening Hodge/Frolicher argument and lines 1189 onward.
- `workbench/bott_chern_algebra.tex`, entire file.
- `notes/B_notes.md`, B-2/B-3/B-17 and sign/factor12 discussion.
- `original/AC26_transcription.tex`, Propositions 7.12, 7.14, 7.26, 7.27, including exact collar-period formulas on PDF pages 62-63. Both pages62 and63 of the authority PDF were rendered and visually inspected: clockwise meridians, differences Theta_i-Theta_V, and sum -p agree with the transcription.
- Attached McHugh PDF, arXiv:1708.03251v4 (November 2018), pp. 18-25, especially Theorems6.1-6.3, Proposition6.4, equation(7), and Section7.1. The cited key is McHugh2018; no unverified later publication date is assigned.
- Attached Angella PDF, pp. 13-16, Section4 and Figure5.
- Stelzig, arXiv:1812.00865v3, opened PDF, Theorem3, Proposition6, Corollary7, Lemma8. Bibliographic publication confirmed at the author's university record: Journal of the London Mathematical Society 104(2), 956-988 (2021), DOI10.1112/jlms.12453.
- Gauduchon (1985), author's primary article, opened https://numdam.org/item/AST_1985__126__129_0.pdf, Theorem2 and proof on printed pp.132-133. The 1977 announcement itself was not opened and is not cited as verified.
- Szekelyhidi, Tosatti, and Weinkove, arXiv:1503.04491v2, opened PDF, Theorem1.3 pp.3 and its conventions. Provides the precise prescribed Chern-Ricci Gauduchon existence theorem applied here.
- Cavalcanti, arXiv:1203.0493v5, opened PDF, Corollary5.13 and Theorems5.14/5.16. Its elementary theorem5.16 would exclude SKT if h21=0; it does not exclude SKT at h21=1. Not needed in the final proofs and should not be represented as doing so.

## Searches

Web searches on 12 November 2026: exact title of Stelzig's double-complex structure theorem; `pluriclosed six-sphere`; `S6 SKT complex sphere metric`; `Cavalcanti SKT even cohomology dimension Euler characteristic obstruction b3 torsion class exact`; `pluriclosed metric b3 b2`; `Gauduchon 1977 Le theoreme de l'excentricite nulle numdam`; `Gauduchon metrics with prescribed volume form`. These searches establish source access, not priority. No novelty claim is made.

## Computed

`code/c_double_complex.py`: two exact independent calculations, rational matrix kernels/images and source/sink counting, for h=0 through5. Includes an acyclic square and signs. All agree. Full output in `outputs/c_double_complex.txt`.

`code/c_sign_and_fibre.py`: exact integer lift conditions and lcm12; sum of clockwise collar periods -p; radial curvature integral; symbolic determinant of fibre Hermitian matrix and real period matrix; rational sample eigenvalues and LDL pivots. Full output in `outputs/c_sign_and_fibre.txt`.

These computations do not determine h or construct the missing coherent eta extension.

## Corrections and limitations

The workbench's Bott-Chern algebra admits a proof for every h, so its truth does not require accepting the claimed h=1 calculation. The factor12 sign can be fixed by curvature/Stokes rather than by declaring a spectral-sequence sign. Under AC26's clockwise lifts, exp(12g_gamma)=f*O(-p). It is positive for the standard p=-1 and negative for p=1. Calling base orientation alone a proof would omit the fibre generator and collar difference convention, but this is a gap in sign justification, not a refutation of the standard +12 value.

No correction was found to the particular McHugh or Angella formulas used. Part A now establishes h=1 and the actual Leray extension of eta, so the numerical BC/A values and the SKT/astheno obstruction apply to X. The root-stack tangent argument D1-D3 was independently audited: vertical transition comparison, root-character cokernel, normal quotient, cusp conormal kernel, and the analytic Kuranishi inverse-function argument all agree with direct independent calculations.

The global G in C3.1 is an exact Green-operator formula, not a finite elementary coefficient atlas. C3.8 also gives a harmonic/Riesz formula for Q normalized by its fibre integral. The coefficient functions of these elliptic constructions were not evaluated on a finite atlas; this precise representation task remains marked Open.

## Independent audits of the other Parts

The residue comparison of A1.3 was checked against the finite-character lattices and the normalization residue sequence. The global relative eta tensor of A2.4 extends on each root cover and at the cusp, lies in the actual coherent kernel, and lifts through the curve Leray edge map; this supplies the particular geometric input needed by C3.7.

For the later D4 calculation, the chain-level Fourier comparison was checked in explicit real marked coordinates: write zeta=Z(s)x+y, put G_j=(dx_j)^{0,1}, e_i=partial/partial zeta_i, and h=partial/partial s+(Z'(s)x)e. Then barpartial G=0, barpartial e=0, and barpartial h=Z'(s)eG exactly. A smooth flat-character frame has holomorphic relative Dolbeault coefficients because (dy)^{0,1}=-Z(s)G. Uniform contraction of all nonresonant Fourier modes, followed by the base-form filtration, identifies the actual derived direct image with the finite Koszul-plus-tangent complex. The finite deck action normalizes the compact translation torus, so the comparison preserves its action. This removes the previously unidentified chain-level extension map.

The simultaneous-normal-form issue at the order-three point was separately checked. Separate orders of the Picard section and the Kodaira--Spencer determinant would not suffice. The actual leading coefficients satisfy nu_2^2=9F_2^2/512, tau_1=i*pi*F_2^2/2, K_2=3F_2^2/4, and b_3=7i/(32*pi); the joint transverse coefficient is 123ik/(64*pi), which is nonzero for every nonintegral resonance k. The invariant cubic normalization is F^6*g_3=-4B=-8t^4(t-1)^2. The exact local module generators then give H1=A/(s^2) plus A/(s^3) and H2=A/(s^2) plus A/(s^3) at the order-three point; the actual cyclic characters yield the coarse lengths recorded in Part D.

For E2, Viaclovsky's comb paper, Proposition6.1, printed pp.19-21, explicitly gives tau_s=(log t)/(2*pi*i)I+H_s(t), preserving an invertible cusp Kodaira--Spencer matrix. The invariant real lattice classes extend as nonvanishing sublines of the two root bundles. Their determinants have weight 24m-1, so the coarse vertical bundle has an exact sequence 0 to O to rho_*E_m to O(2m-1) to 0 and h0(T)=2m+1. Independent character-degree calculations give the cotangent connecting cokernel length4m, the rank-three cup-kernel degree -2m-2+e_m, and h11=4m+1+h0(K_m), h12=4m+h0(K_m). No invalid universal bound on automorphism dimension is used.

The subsequent exact tangent refinement for the combs also passes this audit. The bundles rho_*E_m and rho_*G_m have nonnegative splittings: a negative summand would force their nowhere-zero section of O into the other positive-degree summand, where it would have a zero. Their tensor product has H1=0. Its natural injection into rho_*(E_m tensor G_m) has a length-one quotient at the order-three point, since the two variable invariant factors s^2 multiply to s^4=t*s, and no quotient at the order-four point, where s*s=s^2. Hence rho_*(E_m tensor G_m) has rank4, degree8m-3, H1=0 and h0=8m+1. The next tangent cup map is generically invertible by the cusp calculation, so its sheaf kernel is zero. The first tangent cokernel therefore is the actual degree-one direct image, unaffected by the normal quotient, and the horizontal line descends to the acyclic O(-1). This proves h1(T)=8m+1 and h2(T)=6m+1. The exact m=12 values are97 and73.

