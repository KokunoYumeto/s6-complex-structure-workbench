# Paper I: independent re-proof of ari:C.1.2

**The full statement is proved, including the continued logarithm phases. One sentence in the printed proof misidentifies a lattice point as a nonzero half-period; an exact correction is supplied. No theorem value or hypothesis changes.**

The checked source is the frozen snapshot with SHA256 `d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169`. The target statement's SHA256 is `89415dfb5c10f1df1abc1c75e0ae974b81d01d4ef2f2614c4e3e3912510e2a49`.

## Derivation written before reading the proof

`S6_SERIES_PUBLISH_I_C12_preread_derivation.md` was frozen at 00:55:57 UTC on 21 November 2026, SHA256 `eb4d37f774996d252cfb718dc177b342529cf01ea6cb55282143e6a881c4ec52`. The authoritative full hash is in the preread receipt; the comparison generator below verifies that receipt against the file before recording the event.

The prior exposure is recorded there: the target statement, the already checked C.1.1 input, and the parent's warning that the continuation requires more than endpoint norm calculations. The parent also mentioned an E6 bound in the printed proof, without giving its expression. I did not open the target proof until the alternative continuation argument and new exact finite arithmetic had been saved.

The independent argument controls the entire two paths by real Weierstrass segments. On τ=iT, the theta-constant signs put the unique lower zero between the real and diagonal half-periods. On τ=1/2+iT, the vertical segment from 1/2 to 1−τ has no critical point, starts at a positive wp value, and ends at a pole with value tending to minus infinity. A rational Fourier bound proves the positive initial value for the whole path. The unique zero stays strictly inside the segment. Every Jacobi factor is consequently positive after removing the known factor exp(πiτ/6). This determines the actual continued arguments, zero and π/12, without an E6 bound or a numerical winding estimate.

For completeness, the cusp identification used in the preread text can be read as a direct squeeze: choose fixed b−<b∞<b+; the limiting expressions π²sech²(πb±)−π²/3 have opposite signs, uniformly for sufficiently large T. The unique zero lies between b− and b+, proving b(T)→b∞. This spells out the compactness implicit in the saved cusp-limit argument, without changing its method.

## Comparison with the printed proof

| Printed component | Comparison |
|---|---|
| Degree-three kernel at ρ | The matrix, kernel points and image `(1+ρ)p=1` agree exactly with the preread derivation and the newly written rational arithmetic. |
| Degree-two kernel at i | The printed proof uses 1+i; the preread derivation uses 1−i. Their kernels are equal because 1+i=i(1−i), multiplication by i is a lattice automorphism, and both have absolute value √2. This explicit unit relates the two computations. |
| Endpoint product phases | The product factors and Gaussian exponents agree with the preread derivation. The derivation additionally fixes the arguments along the entire two paths. |
| Rhombic continuation by E6 | The printed E6 estimate is a valid alternative after interpreting the series in Lambert form. For n≥2, n⁵≤32·8^(n−2), and the denominator is at least 1−r². Thus the tail is bounded by 504·32r²/((1−r²)(1−8r)). At r≤1/200 this is less than 1/2, while the n=1 contribution to E6 is positive. This estimate was checked after opening the proof and is not described as part of the preread derivation. |
| Boundary y=T | The printed sentence calls this “another half-period zero”. In fact μ=1/2−iT=1−τ is a lattice point, where wp has a pole. The needed exclusion follows from that pole. The guard replaces only this reason and keeps the valid y=0 half-period argument. |
| β and D values | Substituting the fixed logarithms gives the four stated identities, and subtraction of the Gaussian determinant terms gives the two exact D values. All constants, signs and factors agree. |

The proof's first paragraph also contains an incomplete grammatical join and the process phrase “requested parallel calculation”. A second guard rewrites those sentences as the two explicit endomorphism calculations; their kernel and norm identities are retained.

## New exact arithmetic

`code/S6_SERIES_PUBLISH_I_C12_exact_check.py` was written without importing earlier code. Its output `S6_SERIES_PUBLISH_I_C12_exact_check.json` verifies the two integral endomorphism matrices and determinants, their marked kernel-point images, and the rational bound

\[
e^5>\sum_{k=0}^{6}\frac{5^k}{k!}=\frac{16289}{144}>100,
\qquad
\frac23-16\frac{1/100}{(1-1/100)^2}=\frac{4934}{9801}>0.
\]

These finite calculations support the preread proof. They are not an interval or numerical certificate for the analytic continuation, which is established by the preceding argument.

## Event and correction scope

One event of type `independent re-proof` records the complete alternate derivation, comparison and the precise proposed proof repair. No second computation event is claimed for its supporting finite arithmetic. The statement is correct, so no “refuted statement” event is appropriate. No applied-source rereading is claimed before the parent integrates the guards. Canonical counts remain untouched.
