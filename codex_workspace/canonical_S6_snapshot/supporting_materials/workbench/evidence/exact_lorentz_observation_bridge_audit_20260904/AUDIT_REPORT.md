# Independent audit of the Exact Lorentz Observation Bridge packet

Date: 2026-09-04  
Audit root: `C:\Users\user\Documents\math\agent_work\lorentz_bridge_intake_20260904`  
Canonical comparison root: `C:\Users\user\Documents\math\output\s6_consolidated_canonical_2026-08-26`

## 1. Exact verdict

The packet is intact, its displayed finite-dimensional algebra is correct, its orbit-space and compactification theorems are correct, and its unconstrained and fixed-((\lambda_0,\omega_0)) multiplication-operator spectra are correct in their stated kinematic/free scope.  All 11 internal file checksums pass.  The packet verifier replays 33/33 identities, and the independent verifier in this audit passes 30/30 exact checks.  A fresh LaTeX rebuild gives 23 pages with a zero-hit final warning/error scan; independent raster inspection finds no layout defect.

There is no genuinely new result relative to the current canonical tree.  The packet TeX is byte-for-byte identical to the canonical evidence copy, both with SHA-256

`2be16e1dc71b2e5dc04238f0fbe440138258d0825a4841ab2f29662587681599`.

One dynamical overreading must be rejected.  The first-order action does not make the strict-interior states into ordinary propagating free particles, and the observer multiplication operator (H_n) is not the Hamiltonian generating its (\tau)-evolution.  Exact variation gives

\[
w\ne0:\quad \dot p=0,\qquad\dot x=0,
\]

whereas at the threshold (w=0),

\[
\dot p=0,\qquad\dot x\in\mathbb Rp.
\]

The canonical worldline module already contains this correction.  The packet's separately defined multiplication/Fock spectrum and its externally constraint-selected positive endpoint remain valid; they are not a dynamically generated interacting mass gap.

Four exact research seams remain open: a pointwise toroidal-total-space map into (\mathcal Y_3), the global analytic overlap cocycle at the finite elliptic fillings, an interacting Yang--Mills transfer with an energy-form intertwiner, and a globally compatible single-spin projector.

## 2. Immutable inputs and hashes

### 2.1 Source inputs

| Input | Bytes | SHA-256 |
|---|---:|---|
| `C:\Users\user\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Exact_Lorentz_Observation_Bridge_20260904.zip` | 490,633 | `efc0705a9fed54b91fb607662d0e10de4a655583ee964ddae2592f947d641582` |
| `C:\Users\user\.codex\attachments\61d2cce4-5306-4c4c-b5c3-732b1dfb4828\pasted-text.txt` | 12,818 | `205343a15d7f2f58823a50ff6509ed62b1a0ee550f38bc197508f3c00d4a96c4` |

The ZIP digest exactly matches the digest printed at pasted-source lines 630--632.

### 2.2 Extracted packet

The archive contains no rooted path and no `..` traversal component.  It was extracted only below this audit root.  Actual hashes are:

| File | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 1,189 | `7f1a4568805c03030af56331a6f7ec59ffb31c22e49a40f3e5c2b29db599a117` |
| `exact_lorentz_observation_bridge.md` | 10,434 | `2565d0ff88a8dce168fe577ffaf5ab42ff75f02d8577e0a619fd485d0401c12b` |
| `exact_lorentz_observation_bridge.pdf` | 469,780 | `90b8897aae12c18c89bcab3284606f6e6f86e7420ed8a2ad9a8be0557aa6d841` |
| `exact_lorentz_observation_bridge.tex` | 53,061 | `2be16e1dc71b2e5dc04238f0fbe440138258d0825a4841ab2f29662587681599` |
| `manifest.json` | 1,792 | `895edb7521617575e36ee2687d6859244d9e61f1e2bdc45affb558befe8a4896` |
| `pdf_preflight.txt` | 135 | `92536af74aa9b839727321e6888e2b30dad986eab10662a98fabf968a601753c` |
| `remaining_maps.md` | 2,369 | `2c705011ee5ff65e798179dbdeac8f50205b402fc499d77197dbb64424fa7254` |
| `validation_receipt.json` | 1,376 | `4966d7f1e5ec3ed03073231de478bef327d7f5495762aed12e9db749e4ac8149` |
| `verification_output.json` | 2,460 | `af77cd255445f29116425824d9a980ad24afe4355dbb6f348496565a2e271aaa` |
| `verification_output.txt` | 983 | `9e4ffef20fea7a91e1fdb24218c39310cee97168d23a74e80fa822ca8a6e222b` |
| `verify_lorentz_observation_bridge.py` | 9,085 | `2411784bb8772fcb9eedb91540ddd7ea6584610e7a696ef77596b7fc3ac1aa1e` |
| `CHECKSUMS.sha256` | 1,006 | `35e3eb32667ec3dfac259fa0c5686a2aa17178588ebcfe71b0ebd29593ab214a` |

Every one of the 11 entries listed in `CHECKSUMS.sha256` matches its extracted file.  The checksum file itself is the twelfth archive entry and is not self-listed.

### 2.3 Pasted source versus packet handoff

The pasted text is not byte-identical to `exact_lorentz_observation_bridge.md`; a line diff has 490 inserted and 335 deleted lines because the pasted response uses more display-math line breaks and a different exposition order.  Its eight mathematical sections restate the same objects and results found in the TeX:

1. adapted (9=4+4+1) coordinates;
2. positive fibres and determinant identities;
3. the (SL_2(\mathbb C)) action;
4. the phase-retaining (SU(3)) quotient;
5. the bounded torus/cone relationship;
6. the unconstrained momentum quotient;
7. the fixed-((\lambda_0,\omega_0)) topology and threshold;
8. the action and separate multiplication/Fock spectrum.

No mathematical definition or conclusion in the pasted source is absent from the packet TeX.  Its sentence “That calculation is now complete” is valid only for the finite-dimensional quotient and free multiplication-operator result, not for the four open seams listed above.

## 3. Canonical comparison and exact duplication

The following canonical files were read but not edited:

| Canonical file | SHA-256 at audit | Relevant content |
|---|---|---|
| `workbench.tex` | `c8a755efc9e95b4d090ab17c06a11cd0816d1c269c21ebd88fab1dcb8d8ad6b2` | lines 815--931 already summarize the quotient, Lorentz bridge, momentum model, and corrected constrained dynamics |
| `supporting_materials/workbench/research/higher_rung_lorentz_observation_bridge.tex` | `68bdb0825113d61836cb8dab494b25be5159b35094d3fac2522d24508f7b287c` | lines 12--673 prove the splitting, fibres, spin action, compactification, and phase carrier; lines 748--829 prove the colour momentum quotient |
| `supporting_materials/workbench/research/higher_rung_toroidal_elliptic_bridge.tex` | `c9cf123c5fa6cd3fb562e9ece981bdcb24289d4727039068a6f01b5ff6a8aaf7` | lines 38--78, 145--199, and 255--298 type and prove the filling square; lines 1057--1105 state the remaining global obstruction |
| `supporting_materials/workbench/research/worldline_presymplectic_reduction.tex` | `c3b36ed5688e915eeb18c1d3543c72c558e2974af2ef11dafb57e3a3852998b8` | lines 756--977 audit this exact packet and prove the omitted action equations |
| `supporting_materials/workbench/evidence/worldline_presymplectic_reduction_20260904/exact_lorentz_observation_bridge.tex` | `2be16e1dc71b2e5dc04238f0fbe440138258d0825a4841ab2f29662587681599` | byte-identical copy of the packet's complete TeX |
| `workbench_and_manuscript_overview.tex` | `802e89ba3f84b37a8b19ea57f728fb434127c596db114d114dd1baa2078b5f5e` at closure | overview already names the Lorentz observation bridge and filling identities; this secondary file changed concurrently during the audit |

The comparison is stronger than phrase matching: the packet's full TeX byte string equals the canonical evidence file's byte string.  Thus none of C01--C31 in `CLAIM_LEDGER.md` is new to the canonical repository.  The whole canonical tree changed concurrently while this audit was running; `CANONICAL_READONLY_RECEIPT.md` records all three tree snapshots and establishes that the exact packet copy and the principal Lorentz/worldline sources stayed hash-stable.  This audit made no canonical write.

## 4. Complete independent algebraic proof

All maps and domains are typed in `DEFINITIONS_AND_MAPS.md`.  This section proves the packet's mathematical assertions without appealing to its verifier.

### 4.1 The adapted frame

Direct multiplication gives

\[
PP^*=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}=C,
\qquad
C^{-1}=\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]

Therefore

\[
R_P=P^*C^{-1}
=\frac13\begin{pmatrix}2&1\\-1&1\\-1&-2\end{pmatrix}.
\]

Since (PR_P=PP^*C^{-1}=I_2), (R_P) is a right inverse.  The range of (P^*) is ((\ker P)^\perp=u^\perp), so (R_PP=P^*C^{-1}P) is the orthogonal projection onto (u^\perp).  As (u^*u=3), this projection is (I_3-uu^*/3).  The column sums of (R_P) vanish, and (Pu=0), hence (u^*R_P=0).  Consequently

\[
\begin{pmatrix}P\\u^*/3\end{pmatrix}(R_P\;u)
=\begin{pmatrix}I_2&0\\0&1\end{pmatrix}.
\]

Both factors are square, so they are mutual inverses.  Expanding

\[
X=\begin{pmatrix}
2/3&1/3&1\\
-1/3&1/3&1\\
-1/3&-2/3&1
\end{pmatrix}
\]

gives (\det X=1).

### 4.2 Unique block coordinates and determinant

For (H=H^*), put (M=X^{-1}HX^{-*}).  There is a unique decomposition

\[
M=\begin{pmatrix}G&z\\z^*&\lambda\end{pmatrix}
\]

with (G=G^*), (z\in\mathbb C^2), and (\lambda\in\mathbb R).  Substituting (X^{-1}=(P;u^*/3)) gives, without normalization changes,

\[
G=PHP^*,\qquad z=\frac13PHu,\qquad
\lambda=\frac19u^*Hu.
\]

Inverting yields

\[
H=R_PGR_P^*+R_Pzu^*+uz^*R_P^*+\lambda uu^*.
\]

Since (\det X=1), (\det H=\det M).  For

\[
G=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad z=\begin{pmatrix}r\\s\end{pmatrix},
\qquad z^*=\begin{pmatrix}\bar r&\bar s\end{pmatrix},
\]

expansion of the last row gives

\[
\det M
=\lambda(ad-bc)
-\begin{pmatrix}\bar r&\bar s\end{pmatrix}
\begin{pmatrix}d&-b\\-c&a\end{pmatrix}
\begin{pmatrix}r\\s\end{pmatrix}
=\lambda\det G-z^*\operatorname{adj}(G)z.
\]

This is a polynomial identity and therefore includes singular (G).

### 4.3 Positivity and every fibre

Invertible congruence by (X) preserves positive semidefiniteness, so it is enough to analyze (M).  If (M\succeq0), then (G\succeq0).  For (v\in\ker G), restrict the quadratic form to vectors ((tv,s)\in\mathbb C^2\oplus\mathbb C).  Its (2\times2) coefficient matrix is

\[
\begin{pmatrix}0&v^*z\\z^*v&\lambda\end{pmatrix}.
\]

A positive semidefinite Hermitian matrix with a zero diagonal entry has the corresponding row and column zero; hence (v^*z=0).  Thus (z\perp\ker G), which for Hermitian (G) is (z\in\operatorname{im}G).

Under this range condition (GG^\dagger z=z), and exact multiplication gives

\[
M=
\begin{pmatrix}I_2&0\\z^*G^\dagger&1\end{pmatrix}
\begin{pmatrix}G&0\\0&\rho\end{pmatrix}
\begin{pmatrix}I_2&G^\dagger z\\0&1\end{pmatrix},
\qquad
\rho=\lambda-z^*G^\dagger z.
\]

The outer factors are mutual adjoints and invertible.  Hence

\[
M\succeq0
\Longleftrightarrow
G\succeq0,\quad z\in\operatorname{im}G,\quad\rho\ge0,
\]

and

\[
\operatorname{rank}M
=\operatorname{rank}G+\begin{cases}1,&\rho>0,\\0,&\rho=0.\end{cases}
\]

For fixed rank-(r) (G\succeq0), the parameters are exactly (z\in\operatorname{im}G\cong\mathbb C^r) and (\rho\in[0,\infty)).  If (G=0), then (z=0) and (H=X\operatorname{diag}(0,0,\lambda)X^*=\lambda uu^*).  This proves every claimed fibre, including the zero fibre.

### 4.4 Spin action and invariant cubic

Using (X^{-1}=(P;u^*/3)),

\[
X(g\oplus1)X^{-1}=R_PgP+\frac{uu^*}{3}=T_P(g).
\]

Conjugation by a fixed invertible matrix proves

\[
T_P(g_1g_2)=T_P(g_1)T_P(g_2),\qquad
\det T_P(g)=\det g=1,
\]

and injectivity.  It also gives

\[
T_P(g)X=X(g\oplus1),
\]

so congruence sends

\[
\begin{pmatrix}G&z\\z^*&\lambda\end{pmatrix}
\longmapsto
\begin{pmatrix}gGg^*&gz\\z^*g^*&\lambda\end{pmatrix}.
\]

For a (2\times2) matrix and (\det g=1), polynomial continuation from invertible (G) gives

\[
\operatorname{adj}(gGg^*)
=(g^*)^{-1}\operatorname{adj}(G)g^{-1}.
\]

Therefore (z^*\operatorname{adj}(G)z) and (\det G) are invariant.  In Pauli coordinates (\det G=(p^0)^2-\sum_i(p^i)^2), proving the Lorentz-vector identification.  Finally (-I_2) fixes (G) under congruence and sends (z\mapsto-z), proving that the full representation does not factor through (SO^+(1,3)).

### 4.5 The (e_2) coefficient, determinant opening, and ranks

For a (3\times2) matrix (A) and a (2\times2) matrix (G), Cauchy--Binet applied to the three principal (2\times2) minors gives

\[
e_2(AGA^*)=\det G\,\det(A^*A).
\]

Taking (A=R_P),

\[
R_P^*R_P=C^{-1},\qquad\det C^{-1}=\frac13,
\]

so

\[
e_2(\jmath_P(G))=\frac13\det G.
\]

In adapted coordinates,

\[
\jmath_P(G)=X\operatorname{diag}(G,0)X^*,
\]

\[
uu^*+\varepsilon\jmath_P(G)
=X\operatorname{diag}(\varepsilon G,1)X^*.
\]

Thus

\[
\det(uu^*+\varepsilon\jmath_P(G))
=\varepsilon^2\det G,
\]

and the ranks are (\operatorname{rank}\jmath_P(G)=\operatorname{rank}G) and (\operatorname{rank}a_\varepsilon(G)=1+\operatorname{rank}G).

### 4.6 Topological models and properness

For (A\in\mathfrak p=\operatorname{Herm}_3^0(\mathbb C)), (A-\lambda_{\min}(A)I_3) is positive semidefinite with minimum eigenvalue zero.  For (Q\in\mathcal C_{\mathrm{sing}}), (\lambda_{\min}(Q)=0), so (A=Q-(\operatorname{tr}Q/3)I_3) has minimum eigenvalue (-\operatorname{tr}Q/3).  Substitution proves that the two maps in the definition ledger are mutual inverses.  Eigenvalues depend continuously on a Hermitian matrix, so both maps are continuous.  Therefore (\mathcal C_{\mathrm{sing}}\cong\mathfrak p\cong\mathbb R^8).

For (H\succeq0), let (A=H-(\operatorname{tr}H/3)I_3) and

\[
r=\frac{\operatorname{tr}H}{3}+\lambda_{\min}(A)=\lambda_{\min}(H)\ge0.
\]

Then (H=A+(r-\lambda_{\min}(A))I_3), giving the homeomorphism (\mathcal J_+\cong\mathbb R^8\times[0,\infty)).  The stated one-point compactifications follow, and the compactified rank-deficient cone is the boundary (S^8) of (B^9).

Because (\mathcal O_P\jmath_P=\operatorname{id}), any norm satisfies

\[
\|G\|\le\|\mathcal O_P\|\,\|\jmath_P(G)\|.
\]

Thus (jmath_P) is proper.  Multiplication by (\varepsilon>0) and addition of the fixed (uu^*) preserve escape to infinity, so (a_\varepsilon) and its null-cone restriction are proper.  Conversely,

\[
H_n=nuu^*,\qquad K_n=\jmath_P(nI_2)
\]

both escape in (\mathcal C_{\mathrm{sing}}), while

\[
\mathcal O_P(H_n)=0,\qquad
\mathcal O_P(K_n)=nI_2\to\infty.
\]

At a one-point compactification both source sequences approach the same point, but their images do not; therefore no continuous extension exists.

### 4.7 Phase carrier and its standard binding

Let (A\in\mathfrak p) have eigenvalues (a_1\le a_2\le a_3).  For (\tau\ge-a_1),

\[
f_A(\tau)=\det(A+\tau I_3)=\prod_{j=1}^3(\tau+a_j)
\]

is nonnegative, is zero at (-a_1), tends to infinity, and is strictly increasing for (\tau>-a_1).  Indeed,

\[
f_A'(\tau)=
(\tau+a_2)(\tau+a_3)
+(\tau+a_1)(\tau+a_3)
+(\tau+a_1)(\tau+a_2)>0
\]

away from the initial zero.  Hence (f_A(\tau)=|\omega|^2) has a unique solution, continuously depending on ((A,|\omega|^2)).  This proves

\[
\mathcal Y_3\cong\mathfrak p\times\mathbb C\cong\mathbb R^{10}.
\]

When (\omega=0), the solution is (\tau=-\lambda_{\min}(A)), so the locus is (\mathfrak p\times\{0\}).  Its one-point compactification is the standard linear (S^8\subset S^{10}), not merely an abstract embedded sphere.

### 4.8 Complete colour quotient

If (B\mapsto(B^*B,\det B)), both components are left-(SU(3))-invariant and satisfy (\det(B^*B)=|\det B|^2).  Conversely, for (M\succeq0) and (\omega) with (|\omega|^2=\det M), begin with (M^{1/2}).  If (\omega\ne0), multiply on the left by a unitary matrix of determinant (\omega/|\omega|); if (\omega=0), no phase correction is needed.  This proves surjectivity onto (\mathcal Y_3).

If (B_1^*B_1=B_2^*B_2), the correspondence (B_1v\mapsto B_2v) is a well-defined isometry between their ranges.  It extends to (U_0\in U(3)).  In rank three, (\det B_2=\det B_1) forces (\det U_0=1).  In smaller rank, the orthogonal complement of the range is nonzero, so multiplying (U_0) on that complement by the inverse determinant leaves (U_0B_1) unchanged and produces (U\in SU(3)).  Hence (B_2=UB_1), and the fibres are exactly the orbits.

Finally, (|B|_F^2=\operatorname{tr}(B^*B)).  A compact set in (\mathcal Y_3) bounds (B^*B), hence bounds (B); its preimage is closed and bounded in finite dimension, so the quotient map is proper.  Properness proves

\[
S^{18}/SU(3)\cong\mathcal Y_3^+\cong S^{10}.
\]

### 4.9 Exact torus/cone relationship and filling square

The columns of (P) generate (\mathbb Z^2), and solving (Px=0) gives (x_1=x_2=x_3).  Thus the torus kernel is ((\mathbb Ru)/(\mathbb Zu)).  For every (A\in\operatorname{Mat}_{3\times k}(\mathbb C)),

\[
\mathcal O_P(AA^*)=PAA^*P^*=(PA)(PA)^*.
\]

The strongest exact map between the two kernel presentations is

\[
q:\mathbb Cu\to\mathbb R_{\ge0}uu^*,\qquad tu\mapsto|t|^2uu^*.
\]

It is surjective and has (U(1))-orbits as nonzero fibres.  The angular kernel circle maps isomorphically onto the fibre (q^{-1}(uu^*)) by ([su]\mapsto e^{2\pi is}u).  Thus the circle records phase while the ray records squared radius; neither is discarded and they are not identified without the quotient map (q).

The packet's filling equality is only fully typed after restoring the canonical (B_0,M_3,M_F).  With (Q=B_0^{-1}P),

\[
\Phi M_3(a,b)=\Phi(a+b,b)=(P(a+b),Qb),
\]

whereas

\[
M_F\Phi(a,b)=M_F(Pa,Qb)
=(Pa+B_0Qb,Qb)=(Pa+Pb,Qb).
\]

These are identical, and

\[
c_F\Phi(a,b)=Qb=Qc_3(a,b).
\]

This proves the local lattice/filling morphism.  It does not define a pointwise map from the toroidal total space to (\mathcal Y_3).

### 4.10 Momentum quotient and unconstrained spectra

For (p(Z)=\alpha Z^*Z), surjectivity follows from

\[
Z_p=\alpha^{-1/2}
\begin{pmatrix}
(p^{1/2})_{11}&(p^{1/2})_{12}\\
(p^{1/2})_{21}&(p^{1/2})_{22}\\
0&0
\end{pmatrix},
\qquad
\alpha Z_p^*Z_p=p,
\]

where the notation means the two rows of (p^{1/2}) followed by a zero row.  Equality of two-column Gram matrices gives an isometry between column spans, and because the colour complement is nonzero, it extends with corrected determinant to (SU(3)).  Thus fibres are exactly colour orbits.  Properness follows from

\[
\operatorname{tr}p(Z)=\alpha\|Z\|_F^2.
\]

Cauchy--Binet gives

\[
\det p(Z)=\alpha^2\sum_{1\le a<b\le3}
|Z_{a1}Z_{b2}-Z_{b1}Z_{a2}|^2.
\]

The range is ([0,\infty)) because (Z_r=r(e_1,e_2)) gives (\alpha^2r^4).  The real Jacobian of (Z\mapsto Zg^*) is (|\det_{\mathbb C}g|^{2\cdot3}=1), so pullback is unitary.  The translation multipliers and this Lorentz action satisfy the semidirect covariance relation because (p(Zg^*)=gp(Z)g^*).

Let (\nu=p_*d^{12}Z).  If (U) is a nonempty relatively open subset of the future cone, (p^{-1}(U)) is a nonempty open subset of the ambient matrix space and therefore has positive Lebesgue measure.  Hence (\nu) has full support.  The spectrum of a real multiplication operator is its essential range.  The mass-squared and observer-energy maps have exact ranges ([0,\infty)), so their spectra equal that interval.  Each level set is the zero set of a nonconstant real polynomial, hence has Lebesgue measure zero; therefore there is no point spectrum.  Adding a vacuum or applying free symmetric Fock quantization cannot create a positive first-excitation gap because one-particle energies approach zero.

### 4.11 Fixed determinant and scalar norm

For (B=[Z\ \phi]),

\[
|\omega|^2=\det(B^*B)
=\lambda\det G-z^*\operatorname{adj}(G)z.
\]

Since (p=\alpha G) and (\operatorname{adj}(\alpha G)=\alpha\operatorname{adj}(G)), for (\lambda>0),

\[
\det p
=\frac{\alpha^2|\omega|^2}{\lambda}
+\frac{\alpha}{\lambda}z^*\operatorname{adj}(p)z.
\]

For (p\succeq0), (\operatorname{adj}(p)\succeq0).  If (\omega\ne0), then (B) is invertible, hence (G>0) and (\operatorname{adj}(p)>0); equality therefore holds exactly at (z=0).

On the exact constraint level, (B) is invertible and the quotient matrices satisfy

\[
\det\begin{pmatrix}G&z\\z^*&\lambda_0\end{pmatrix}
=|\omega_0|^2.
\]

Put (\mu=\sqrt{\det G}) and (w=G^{-1/2}z).  Since (\operatorname{adj}(G)=\det(G)G^{-1}),

\[
z^*\operatorname{adj}(G)z=\mu^2\|w\|^2,
\]

so

\[
\mu^2(\lambda_0-\|w\|^2)=|\omega_0|^2,
\qquad
\mu(w)=\frac{|\omega_0|}{\sqrt{\lambda_0-\|w\|^2}}.
\]

Also (\det(\mu^{-1}G)=1), and the positive logarithm

\[
A=\log(\mu^{-1}G)
\]

is traceless Hermitian.  Exponential and logarithm are smooth inverses between (\operatorname{Herm}_2^0(\mathbb C)) and positive determinant-one matrices.  This proves the global quotient diffeomorphism and the inverse (G=\mu(w)e^A,z=G^{1/2}w).

For (M=\begin{psmallmatrix}G&z\\z^*&\lambda_0\end{psmallmatrix}), (\det M^{1/2}=|\omega_0|).  Thus

\[
s_{\omega_0}(G,z)
=\operatorname{diag}(\omega_0/|\omega_0|,1,1)M^{1/2}
\]

has Gram matrix (M) and determinant (\omega_0).  It is a smooth global section; hence the principal (SU(3))-bundle is trivial.

The mass formula is

\[
\det p(A,w)=\alpha^2\mu(w)^2
=\frac{\alpha^2|\omega_0|^2}{\lambda_0-\|w\|^2}.
\]

It takes every value in

\[
\left[\frac{\alpha^2|\omega_0|^2}{\lambda_0},\infty\right)
\]

and has equality exactly at (w=0), equivalently (z=0).  The explicit representatives in the packet verify sharpness with the original phase, not only its modulus.

### 4.12 Associated bundle, orbit space, and little group

Every (G>0) with (\det G=\mu^2) can be written (G=\mu gg^*) with (g\in SL_2(\mathbb C)).  Two such factors differ uniquely by (k\in SU(2)).  The simultaneous replacement

\[
(g,w)\mapsto(gk,k^{-1}w)
\]

leaves

\[
G=\mu(w)gg^*,\qquad z=\sqrt{\mu(w)}gw
\]

unchanged.  This proves the associated-ball model.  (SU(2)) acts transitively on each nonzero sphere in (\mathbb C^2), and the stabilizer of a nonzero vector is trivial; hence the Lorentz orbits are classified by (|w|), equivalently by mass.  At (w=0) the stabilizer is all of (SU(2)).

For fixed (G), the little group is

\[
K_G=G^{1/2}SU(2)G^{-1/2},
\]

because (gGg^*=G) is equivalent, after (g=G^{1/2}kG^{-1/2}), to (kk^*=I_2) and (\det k=1).  The fibre equation becomes (\|w\|=r).  The action (w\mapsto kw) is free and transitive for (r>0), so every strict fibre is a (K_G)-torsor and the threshold fibre is a point.  Peter--Weyl then gives

\[
L^2(SU(2))\cong
\widehat\bigoplus_{j\in\frac12\mathbb Z_{\ge0}}V_j\otimes V_j^*,
\]

with multiplicity (2j+1).  This proves that all spins occur and proves, equally, that no unique spin is selected by this geometry.

### 4.13 Fixed-sector multiplication spectra

The constraint map is a submersion on (\omega_0\ne0), so the delta prescription defines a smooth positive measure class with full support on the (15)-manifold.  Both group actions preserve ambient measure and the three constraint functions; therefore the measure class and invariant (L^2) subspace are preserved.

On the quotient (\mathbb H^3\times\mathbb B^4), the mass multiplier has the exact range proved above.  For a future unit timelike (n), reverse Lorentz Cauchy--Schwarz gives

\[
n\cdot p\ge\sqrt{\det p},
\]

with equality when (p) is in the rest direction of (n).  Boosting the lowest mass shell realizes every larger observer energy.  Hence

\[
\operatorname{Spec}(H_n)
=\left[\frac{c\alpha|\omega_0|}{\sqrt{\lambda_0}},\infty\right).
\]

The quotient is connected.  Each multiplier is real analytic and not constant on any open subset; therefore every exact level is a proper real-analytic subset and has zero smooth measure.  Both point spectra are empty.  After adjoining a vacuum, the distance from zero to the excitation spectrum is exactly the lower endpoint; symmetric Fock space has the same first-excitation gap.

This proof concerns the explicitly defined multiplication operators.  It does not identify them with the (\tau)-generator of the packet action.

## 5. Exact variational correction

The packet proves only the multiplier constraints and the (x)-equation.  To obtain the full dynamics, restrict to the smooth constrained quotient and retain

\[
p(A,w)=\alpha\mu(w)e^A,
\qquad
\mu(w)=\frac{|\omega_0|}{\sqrt{\lambda_0-\|w\|^2}}.
\]

Because the constraint map is a submersion, varying the intrinsic action

\[
S_{\mathrm{red}}=\int\langle p(A,w),\dot x\rangle_Ld\tau
\]

against every tangent direction is equivalent to the ambient multiplier equations.  Variation of (x) gives (\dot p=0).  Variation of (q=(A,w)) gives

\[
\langle Dp_q(\delta q),\dot x\rangle_L=0
\quad\text{for every }\delta q.
\]

For fixed (w), variations of (A) move (p) through the determinant-one Lorentz hyperboloid and span the three-dimensional Lorentz-orthogonal space (p^{\perp_L}).  Direct differentiation preserves the exact constant:

\[
D\mu_w(\delta w)
=\frac{|\omega_0|\operatorname{Re}\langle w,\delta w\rangle}
{(\lambda_0-\|w\|^2)^{3/2}}.
\]

If (w\ne0), a radial variation makes (D\mu\ne0) and supplies the fourth, scale direction transverse to (p^{\perp_L}).  Hence (Dp) is surjective.  The variational equation forces (\dot x=0).  Its kernel is the three-dimensional tangent space to the constant-radius (S^3) momentum fibre; motion within that fibre is presymplectically null while (p) remains constant.

If (w=0), (D\mu_0=0) in every one of the four real (w)-directions.  Thus (Dp) has rank three, image (p^{\perp_L}), and four-dimensional kernel.  Nondegeneracy of the Lorentz pairing gives

\[
\dot x\in(p^{\perp_L})^{\perp_L}=\mathbb Rp.
\]

The momentum fibre at a fixed threshold (p) is a singleton, so (A,w) are constant on every threshold solution.  This completes the action's actual equations and refutes any identification of its strict-interior dynamics with the ordinary massive free particle.

## 6. Externally selected threshold, not generated gap

The positive endpoint depends on two fixed inputs.  If only (\omega_0\ne0) is fixed, the exact family

\[
B_R=\operatorname{diag}\bigl((\omega_0/R)^{1/2},
(\omega_0/R)^{1/2},R\bigr)
\]

satisfies

\[
\det B_R=\omega_0,\qquad
\lambda_R=R^2,\qquad
\det p_R=\frac{\alpha^2|\omega_0|^2}{R^2}\to0.
\]

If only (\lambda_0) is fixed, then

\[
B_\varepsilon=\operatorname{diag}(\varepsilon,\varepsilon,\sqrt{\lambda_0})
\]

has

\[
\lambda=\lambda_0,\qquad
\omega=\varepsilon^2\sqrt{\lambda_0},\qquad
\det p=\alpha^2\varepsilon^4\to0.
\]

Thus the packet proves exactly an endpoint selected by a lower bound on (|\omega|) together with an upper bound on (\lambda), or by fixing both.  It does not derive either scale from an interaction.  The finite-dimensional local colour redundancy is not a spacetime gauge field and supplies no interacting Yang--Mills Hamiltonian.

## 7. Exact novelty assessment

No packet theorem is novel relative to the current canonical tree:

1. C01--C08 are already proved in `higher_rung_lorentz_observation_bridge.tex`.
2. C09--C12 are already present in the canonical (SU(3)) Gram and Lorentz modules and summarized in `workbench.tex`.
3. C13 is already a typed theorem in `higher_rung_toroidal_elliptic_bridge.tex`.
4. C14 is already the canonical colour-momentum theorem.
5. C15--C26 occur verbatim in the canonical evidence copy, are classified by the canonical worldline claim ledger, and are summarized with the correct scope in `workbench.tex`.
6. C23's missing dynamics have already been computed more strongly in the canonical worldline module.
7. C27--C30 are open seams already recorded by the canonical sources.

The pasted source is therefore an exposition variant, not a new mathematical source.

## 8. Precise integration recommendations

1. **Do not import the ZIP or TeX again.**  Its TeX is already byte-identical to the canonical evidence copy.  A second copy would add no theorem and would create provenance ambiguity.

2. **Keep the primary linear-algebra source unchanged.**  The authoritative integrated statements are already in `supporting_materials/workbench/research/higher_rung_lorentz_observation_bridge.tex`.  The packet does not improve or correct them.

3. **Keep the canonical dynamical qualification adjacent to every mention of the fixed-sector gap.**  The minimum wording that must survive is: the lower endpoint is an externally fixed-((\lambda_0,\omega_0)) multiplication/Fock threshold; for the displayed action, (\dot x=0) when (w\ne0), (\dot x\in\mathbb Rp) only at (w=0), and (H_n) is not the action's (\tau)-Hamiltonian.

4. **Do not integrate the phrases “dynamically generated gap,” “interacting mass gap,” or “Yang--Mills mass gap.”**  They are false for this construction.  “Free vacuum gap” is acceptable only when explicitly attached to the separately defined direct-sum or Fock multiplication operator.

5. **If a concise theorem is promoted from evidence into a primary module, promote only the validated algebraic package:** the quotient diffeomorphism, associated-ball model, sharp determinant inequality, momentum fibres/little group, and multiplication spectra.  Include the complete variational correction in the same module, not in a later footnote.

6. **Restore types whenever the filling square is quoted.**  The packet omits (B_0,M_3,M_F).  Cite or repeat their canonical definitions so (\Phi M_3=M_F\Phi) is a typed equality rather than an imported slogan.

7. **Preserve the strict boundary on the toroidal claim.**  The proved morphisms are (P), (\overline P), Gram naturality, the orbit map (q:\mathbb Cu\to\mathbb R_{\ge0}uu^*), and the filling square.  Do not claim a total-space map to (\mathcal Y_3) until a Hermitian/Gram assignment is constructed and checked on every overlap and filling.

8. **Leave the four research seams OPEN.**  No human audit should be treated as a proof substitute: each seam requires the exact missing map, cocycle, interacting operator/intertwiner, or global spin projector.

9. **Provenance-only retention is sufficient.**  If an intake record is wanted, retain the ZIP and pasted-source hashes plus this audit path; no canonical theorem source needs changing.

## 9. Verification coverage and limitations

The packet's 33-check program verifies rational matrix identities, polynomial determinant identities, Cauchy--Binet, the Gram phase relation, constrained scalar formulas, a gauge-section test, and the two degenerating sequences.  It does not prove orbit classification, properness, compactification topology, spectral measure claims, or the full action equations.  Those are proved independently above.

The independent 30-check program adds an independent implementation of the core identities and checks the constrained momentum differential ranks (4) and (3), the four-dimensional threshold kernel, and nondegeneracy of the Lorentz pairing.  The remaining topological, measure-theoretic, and variational arguments are exact written proofs, not claims inferred from passing code.

## 10. Reproduction artifacts

- `DEFINITIONS_AND_MAPS.md`: complete typed object and map ledger.
- `CLAIM_LEDGER.md`: C01--C32 PROVED/REFUTED/OPEN classifications with canonical cross-references.
- `independent_verifier.py`: independently authored exact checker.
- `independent_verification.json`: 30/30 machine-readable result.
- `packet_verifier_replay.json`: replay of the inspected packet checker, redirected outside the extracted packet.
- `tmp/latex_rebuild/`: independent three-pass LaTeX rebuild and final log.
- `tmp/pdfs/`: 23 rasterized source-PDF pages, a contact sheet, and extracted text used for PDF QA.
- `LOGBOOK.md`: durable work and decision log.
- `USER_INPUTS.md`: verbatim user-input transcript required by the workspace instructions.

The final SHA-256 manifest and canonical read-only receipt are in `AUDIT_SHA256SUMS.txt` and `CANONICAL_READONLY_RECEIPT.md`.
