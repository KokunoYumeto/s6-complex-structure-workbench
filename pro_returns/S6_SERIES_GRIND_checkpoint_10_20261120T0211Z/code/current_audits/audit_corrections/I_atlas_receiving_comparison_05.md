# Paper I C3.8: statement-first reconstruction and complete receiving-proof comparison

## Conclusion and exposure order

The mathematical gate for `inv:C3.8` closes at its stated scope: the original standard marked family, vectors `(1,2,-4,0)^t` and `(-1,-3,3,0)^t`, original cusp fan, and each admissible c. The three displayed class identities and extension of the evaluated coefficients through both multiple fibres, all cusp doubles and both triple points are established. No mathematical defect was found in the complete receiving proof.

This conclusion has two actual routes, with their exposure order preserved:

1. **Before receiving-proof exposure:** `I_atlas_before_reading_05.md` was frozen at **22:09:48.315912 UTC**, SHA256 `9acbbd5ee546d67006b0230b14b18272b388131fc6d2c3cf32bd1a6f08114aa3`. It contains a construction via the symmetric tensor `S_t=J Z_t^{-1}`, finite averaging, explicit cusp subtraction and residue cancellation, and elementary weights. The isolated statement and the expressly permitted earlier inputs/primary scalar table were read; no C3.8 proof or `open_atlas` file had been opened. Its fresh program passes **39** exact identities in **0.428218 s**.
2. **After that commit:** the complete receiving statement and 13-step proof were extracted from `parts/I.body.linked.tex` at **22:09:59.679503 UTC**, lines 27168–27675 of that snapshot. The receiving snapshot SHA256 is `ea9e93e961438bf3f1e71365ff368158ac9af767f38ad33d609d56da56b93ca2`. All 508 lines were read. The fresh independent receiving-program `code/independent_I_atlas_receiving_05.py` passes **45** exact identities in **2.054175 s**; SHA256 `0b4201dbace905d558775221c28ffd7e267982cfc65652e29cd0fd1d74d9eb10`. It imports no author's code and is explicitly a post-reading computation.

The first route is an independent reconstruction of the isolated mathematical assertion relative to the allowed earlier theorems. The second is a complete comparison of the actual supplied construction, including its particular line factors and connections. The finite assertion counts are not counts of independent proofs.

## Exact bridges between the two constructions

### Scalar convention

For every original generator, the prereading scalar h equals the DGKX scalar eta and the receiving scalar f equals `−h`. The prereading potential is `−sum rho_j h_ij`; the receiving potential is `sum w_j f_ij`. Therefore the signs match exactly. On a common refinement, the difference of two choices of weights is the global smooth function

\[
D_i=-\sum_j(\rho_j-w_j)h_{ij}.
\]

Its chart differences vanish by the cocycle law and the two sums of weights being one. Hence the resulting G forms differ by exactly `bar-partial D`, and both have the original fibre class `gamma^(0,1)`. The injectivity in C3.1 identifies this class with `g_gamma`, without a scalar adjustment.

### Regular quadratic and line constructions

The receiving logarithmic line factor is

\[
E_\lambda=n^tK\zeta+\tfrac12n^tKZn,
\quad n=(\lambda_\gamma,\lambda_u)^t,\quad K=J^t.
\]

Its derivative is exactly the prereading lattice form

\[
dE_\lambda=\lambda_u d\zeta_1+6\lambda_\gamma d\zeta_2+
\tfrac12(\lambda_u^2d\tau+12\lambda_u\lambda_\gamma d\mu+
6\lambda_\gamma^2d\beta)=a_\lambda.
\]

Thus, for the twelfth-power line and the receiving convention `c=(i/(2pi)) d log g`, its cocycle satisfies **`c/12=−a_lambda`** on lattice arrows. The opposite signs of the two partition sums then give the same fibre normalization.

There is also an exact comparison of the regular potentials. With receiving notation `r=(u,gamma)^t`, `D=diag(1,6)`, `T=[[tau,6mu],[mu,beta]]`, `Y=Im T`, `phi=2pi r^t D Y r`, differentiation of `r=Y^{-1} Im zeta` gives

\[
\partial\varphi=-2\pi i\,r^tD\,d\zeta+
\pi i\,r^tD(dT)r,
\qquad \frac{i}{2\pi}\partial\varphi
=u\,d\zeta_1+6\gamma\,d\zeta_2
-\tfrac12(u^2d\tau+12u\gamma d\mu+6\gamma^2d\beta)=A.
\]

Therefore the receiving Chern primitive is exactly the prereading primitive A. Its exterior derivative is the original marked form `du wedge dw+6 dgamma wedge ddelta`. This verifies the sign of the semiflat representative and of the final factor 1/12.

For each ordinary generator R, direct differentiation gives

\[
R^{-1}R_t\zeta=-\frac{\zeta_1}{\tau}(\tau_t,\mu_t)^t,
\qquad S_t(\tau_t,\mu_t)^t=(1,0)^t.
\]

The quadratic-tensor difference is consequently

\[
a_R=-\frac{\zeta_1}{\tau}d\zeta_1+
\frac{\zeta_1^2}{2\tau^2}d\tau
=d\left(-\frac{\zeta_1^2}{2\tau}\right)=dF_j.
\]

This is the exact Gaussian map used by the receiving line lift.

### Finite charts

Write `E_r=F_j+E_{v_j/m_j}(R_j zeta;Z_j)` for the logarithm of the receiving affine factor divided by `12`, omitting its constant phase. Its derivative is the raw quadratic-tensor difference. The phase `kappa_j/12` has derivative zero. If `E_{r^k}` denotes the sum of these logarithms over the first k actual affine iterates, put

\[
P_j=\frac1{m_j}\sum_{k=0}^{m_j-1}E_{r^k}.
\]

The prereading averaged lift differs from the raw lift by `dt dP_j tensor partial_t`, so its one-form cocycle differs by the explicitly displayed holomorphic coboundary `r^*dP_j−dP_j`. Thus the finite averaging route and the receiving line route have an exact local transport; the original affine vector and its full m-th power are retained in both.

### Cusp coefficients

Both constructions use the same full map `x -> exp(2pi i C(q)n) q^(B0 n) x` and the same original triangles. The prereading route subtracts the explicit logarithmic quadratic residue; the receiving route uses the exact Cartier height

\[
L(i,j)=i(i-1)/2-3j^2.
\]

For an explicit comparison let `p_sigma=(2pi i)^{-1} d log f_sigma` and let `b_sigma` be the prereading logarithmic subtraction. Then

\[
e_\sigma=b_\sigma-p_\sigma-\tfrac12d\zeta_1
\]

is holomorphic at each toric stratum: its residue at a ray v is

\[
\tfrac12 B_{vv}(q)-\frac{v^t\operatorname{diag}(1,-6)v}{4\pi i},
\]

which vanishes at q=0 and hence multiplies `dz_i/z_i` to a holomorphic coefficient proportional to the product of the other two coordinates. On toric overlaps the one-form difference is the corresponding coboundary in e. On a full period arrow the exact additional horizontal term is

\[
a^{\rm quadratic}_n-(-c^{\rm line}_n/12)
=e_\sigma-\Psi_n^*e_{\sigma+B_0n}
-\tfrac12(C'(q)n)_1\,dq.
\]

This follows by using `Psi_n^*d zeta_1−d zeta_1=(n_u/(2pi i q)+(C'n)_1)dq`. It retains every C′ term. In particular the fibre classes agree by the displayed coboundary after restriction to dq=0. The assertion prescribes these fibre classes and the G exponential identity; it does not fix the horizontal ambiguity of a global Q class, already recorded in A3.2. Each route constructs a global representative satisfying exactly those stated identities.

## Complete receiving-proof review

| Step | Actual check and conclusion |
|---|---|
| 1. Domains and inverses | The finite original free quotient and cusp proper/free quotient are precisely the permitted earlier constructions. All listed inverse maps retain the actual periods, affine translation, toric integer exponents and logarithm branches. Distinct special pieces have only middle annular overlaps, so the later triple-overlap list is exhaustive. |
| 2. Regular class/sign | The explicit real inverse and `i partial phi/(2pi)=A` above give the asserted marked eta. The indefinite Chern form has the correct sign; no positive-polarization inference is used. |
| 3. Middle line | Fresh symbolic substitution confirms the four lattice defects `(24,0,1/2,0)` and `(-9,0,0,0)`, both finite Gaussian relations, and the two-then-one cusp turn `(tau+1,mu,beta−1,zeta)` with Gaussian sum zero. The ratio is a character because the difference of the actual factor cocycles is independent of zeta; its four generator values therefore suffice. |
| 4. Finite phases | The original affine power is exactly the original lattice vector. Fresh full iteration gives defects `−32` and `−81/2`; multiplying the displayed phases by 3 and 4 gives `32` and `81/2`. These cancel exactly. Integrality of `12 v_j/m_j` gives the required lattice compatibility, and all factors extend as holomorphic units through the root centre. |
| 5. Cusp Cartier lines | Fresh checks verify height interpolation at all four vertices of an arbitrary translated square, its exact quadratic polarization, and cancellation of every x and q exponent under the original period action. The remaining unit is precisely the full C(q)-dependent expression. The ratio to the ordinary factor is exactly `q^(−n_u/2)`, becoming `q^(−6n_u)` at the twelfth power. |
| 6. Annular inverse | The displayed matrix is exactly `(T'^t)^{-1}`; the source determinant theorem excludes every zero on the actual annuli. It is never inverted on a special fibre. The cusp leading coefficient is `1/(4pi^2 q^2)` with the printed sign. |
| 7. Cusp connection | The ratio factor `q^(−6n_u)` gives `l'=(-6/(2pi i q),0)^t`, yielding exactly the displayed connection. A logarithm turn fixes T′ and zeta; changing from z to the Cartier coordinate `w=z/f^12` adds `12 d log f` with the printed sign. |
| 8. Finite connections | The original collar square follows from `h(gs)=h(s)−1/m` and `Av=v`. The fresh computation retains `Pi v=T v_q+v_p`, verifies the inverse identity `(T'^t)^{-1}D T'=D`, and checks both the vertical logarithm-turn change and the entire base differential `−12pi i d((2kh+k^2)S)`. Cyclic averaging uses the exact affine line power; the final minus sign is the tensor-dual connection. No flatness is assumed. |
| 9. Global one-form cocycle | On the two-middle triple a ratio frame changes by the inverse middle factor, so its connection changes by `+d log g_*`; on the two-special triple it changes by the special factor and its connection by `−d log g_j`. Both give exactly `c_ab+c_bc=c_ac`. There are no triples of distinct special pieces. |
| 10. Weights and derivatives | A compact source support and an étale map give finitely many inverse branches near each target point: any hypothetical accumulating additional branches would have a convergent subsequence in the compact source support and violate local injectivity there. A lift in an open half-radius ball makes a_N=1 in a target neighborhood, so all later weights and their derivatives vanish there. The product telescopes to one. The displayed cutoff and quotient derivatives have the correct chain-rule signs and are smooth at zero. |
| 11. Scalar cocycle | The table is the negative of the opened DGKX scalar table, on the same original arrows under the already stated parameter translation. The additive relation follows for every complex z, including all logarithm changes. |
| 12. Forms and classes | The partition identities give `H_a−H_b=f_ab`, `B_a−B_b=c_ab`; their differences are holomorphic. The printed minus sign in Q's coefficients is the exterior-order sign. The ordinary comparison above gives fibre class eta after division by 12. At z=1 the finite characters and the `s^(−gamma(v))` collar give exactly O(S1−S2), and its twelfth power is f*O(4p1−3p2). |
| 13. Real obstruction | Reality plus bar-partial closure implies d-closure. H²(X,R)=0 then makes Q exact. On the fibre exactness gives square integral zero, whereas its asserted Dolbeault class gives −12 by bar-partial Stokes. |

## Source credit actually checked

After the prereading commit I opened the original DGKX v1 PDF page 84 image and read the extracted text of pages 82–84. The primary PDF is the shared file `audit_paper_i/open_atlas/DGKX_v1_primary.pdf`, SHA256 `7facc6e55c7a578315a981224c45f184d3033b6159773304968508aca2710ab3`; it has 107 pages. Page 84 contains the full six-arrow scalar table and Lemma 6.14 with its proof. Pages 82–83 supply the derivative convention and complete finite/cusp/connector formulas. The exact scalar map is `f=−eta_DGKX`; the already stated affine parameter transport makes `Omega_a=Pi_c` with the ordered lattice, original vectors and fan preserved.

The immediately preceding receiving paragraph, “Relation to the source constructions”, already credits AC26 §§3–6, both DGKX versions via `night:P5.7`, the scalar table/Lemma 6.14 at p84 and its conventions at pp82–83, and the cited Čech–Dolbeault conversion. No duplicate credit insertion is needed. This comparison does not assert the absence of other results in the literature.

## Explicit final line-bundle map and remaining gates

The final degree-one arrow can be made completely literal with the principal divisor

\[
\operatorname{div}\frac{t^4}{(t-1)^3}=4p_1-3p_2-p_0.
\]

Multiplication by `t^4/(t−1)^3` sends the sheaf O(4p1−3p2) to O(p0): for a meromorphic local section u, the condition `div(u)+4p1−3p2>=0` becomes exactly `div(t^4 u/(t−1)^3)+p0>=0`. Pullback gives the asserted morphism on X, and O(p0) is the hyperplane line in the original homogeneous coordinate with t=∞ at p0. A one-sentence guarded clarification is saved in `I_atlas_divisor_map_patch_05.json`; it changes no mathematical assertion.

There is no remaining mathematical proof gate for C3.8 at the stated construction scope. The parent owns source integration, the final rendered-layout check, inventory completion and the main-theorem comparison. Those fields remain unset in this branch's assessment. This report does not claim a fresh visual inspection of a newly compiled C3.8 PDF.
