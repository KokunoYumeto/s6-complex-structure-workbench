# C.7.1: sigma–theta normalization, targeted independent check

## Scope and exposure

This record checks only the normalization substep of `ari:C.7.1`: the exact sigma–theta constant with sigma'(0)=1; the lattice discriminant; the real-linear quasiperiod term; and the differential/lattice changes between the displayed arithmetic, Engel, and AC models. It supplies no new independent credit for the branch-transport or algebraic-extension/relative-period portions of that proposition.

The statement was extracted without its proof at 2026-11-21T01:25:50.145787+00:00. The complete derivation was frozen at 2026-11-21T01:27:59.919305+00:00, SHA256 `72ea7e8381479abc036ca2df95e424447fe3d0ecee93a25442f09380d373314f`. Before the freeze I had read the N definition and explicit pointed model maps and had independently checked C.1.1–C.1.2. The parent disclosed that another checker had excluded a normalization substep from independent credit, but I did not open that checker's correction or comparison before freezing this derivation.

The printed proof was extracted after the freeze at 2026-11-21T01:28:12.599120+00:00. The first tool output exceeded the context limit; I subsequently opened and actually read the saved 2,872-character proof in a bounded call. Only its normalization paragraph and surrounding lattice/differential convention were compared mathematically here. The relative-period part was visible in the same bounded excerpt and creates no independent credit.

## Derivation and comparison

For Lambda=omega_1 Z+omega_2 Z, tau=omega_2/omega_1 and v=u/omega_1, the Jacobi product gives theta_1'(0,tau)=2 pi eta_D(tau)^3. The entire function

    omega_1 theta_1(v,tau) exp(eta_1 u^2/(2 omega_1)) / (2 pi eta_D(tau)^3)

has the sigma zero divisor, its full quasiperiod law, and derivative one at zero. Their quotient is entire and elliptic, and its value at zero is one. Thus the displayed function is sigma_Lambda(u).

The Eisenstein normalizations give g_2=(4 pi^4/(3 omega_1^4)) E_4, g_3=(8 pi^6/(27 omega_1^6)) E_6 and

    Delta_Lambda=(2 pi/omega_1)^12 eta_D(tau)^24.

Legendre's relation gives eta(u)=eta_1 u/omega_1−(2 pi i/(omega_1 Im(tau))) Im(v). Consequently Re(u eta(u))=Re(eta_1 u^2/omega_1)+2 pi Im(v)^2/Im(tau). Substitution cancels the entire quadratic exponential and yields exactly

    N(P)=|Delta_Lambda|^(1/12) |sigma_Lambda(u)| exp(−Re(u eta(u))/2).

Twice its logarithm is the asserted formula, since Lambda_1+u(zeta(u)−eta(u))=2 log sigma(u)−u eta(u). The printed unit-lattice identities agree term by term. Its final homogeneity assertion is justified by the following explicit transports, all independently frozen before the proof was opened:

    sigma_(r Lambda)(ru)=r sigma_Lambda(u),
    zeta_(r Lambda)(ru)=r^(-1) zeta_Lambda(u),
    eta_(r Lambda)(ru)=r^(-1) eta_Lambda(u),
    Delta_(r Lambda)=r^(-12) Delta_Lambda.

These identities cancel the factors |r| in the exact expression for N.

For the arithmetic short model, omega_M=dx/(2y), x=wp(u), y=wp'(u)/2 and Delta_M=27 t^8(t−1)^3. The displayed map (x,y) -> (2x,−2 sqrt(2)y) to Engel's equation pulls its invariant differential back to −omega_M/sqrt(2), and Delta_Engel=64 Delta_M. The factors in N are therefore 2^(1/2) from Delta and 2^(−1/2) from sigma. The displayed AC map (x_0,y_0) -> (−x_0,y_0/(2i)) pulls omega_M back to −i dx_0/y_0, and its discriminant is unchanged. These are the exact model morphisms; no comparison based solely on j-invariants is used.

## Result and credit

**Pass for the specified normalization scope.** The current printed paragraph states the correct constant and its general-lattice consequence. No source correction is proposed by this check. The complete frozen derivation is retained beside this report. This produces one narrowly scoped `targeted proof check` association for `ari:C.7.1`, with one evidence group. It does not certify the full proposition by itself and is not also counted as a computational check or independent re-proof. The remaining proposition scope belongs to the analytic agent's separately recorded check.

No metadata or bibliography scan contributes a mathematical event.
