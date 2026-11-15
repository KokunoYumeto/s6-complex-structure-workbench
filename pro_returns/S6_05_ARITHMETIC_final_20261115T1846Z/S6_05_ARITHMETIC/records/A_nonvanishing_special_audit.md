# Independent audit of the proposed A.5.8

Audited against `records/A_nonvanishing_insert.tex` on 15 November 2026. This records the independent mathematical checks; root and the count agent control the final statement status and integration.

## Exact kernel and spectral normalization

The Fourier kernel in A.4.8 agrees with an independent hypergeometric-series calculation. The full derivation and branch choices are in `A_special_resolvent_verification.tex`; direct Fourier checks at 80 decimal digits are in `code/A_special_resolvent_check.py,out`.

The complete-line spectral density has been independently derived by conjugating the transverse Fermi operator to `−d²/dr² + sech²(r)/4`, applying the full-line Green derivative jump, and explicitly using `dλ=2t dt`. The exact Green kernel is `G_s(r,0)=−f_s(|r|)/(2f_s′(0))`. Thus the density with respect to `dt` is `t/(πi)(G_(1/2−it)−G_(1/2+it))`, with leading term `cos(tr)/(π√cosh r)`. There is no extra leading phase or sign. The exact source identity is `q_t(u)=−a G_s′(τ(u),0)/cosh τ(u)`. The full normalization proof, explicit Jost denominator lower bound, and positive gamma-formula check at the source are in `A_line_spectral_verification.tex`. Ninety-digit scalar checks are in `code/A_line_spectral_check.py,out` and all pass.

DLMF equations 14.3.18, 15.8.1, and 15.8.4 were opened and their principal-branch hypotheses checked. All hypergeometric arguments in the fixed kernel calculation lie in `(0,1/289]` or `[-1/288,0)`. The connection calculation at zero uses the positive square root `sqrt(1−sech²r)=tanh r` for `r>0`.

## Endpoint estimate

The exact substitution `v=tanh u`, with `D=√(a²−v²)` and `E=Dcoshℓ−Bsinhℓ`, transforms the principal measure to `a/(2D^(3/2)E^(1/2)) dv`. The phase equation has derivatives `F_v=−N1−v sinhℓ/D` and `F_ℓ=E`. The resulting density, its first derivative, and its zero-extension jumps have total BV norm `O_J(1/|N1|)`.

For large height, `c=N0−|N1|` is positive and bounded by the phase condition, while `|N1|=(N2²−1−c²)/(2c)`. Source translates have `c_m=√(N2²−1)e^(−|u0+mL0|)`, whose contributing sum is uniformly bounded. Combining this with the proved `O(Y)` reduced-axis count gives a summable total BV norm. Fixed-height infinite translate families, including `N2=0`, have geometrically increasing `|N1|` and are summable separately. No endpoint-spacing assumption is used.

The exact outgoing amplitude has bounded first derivatives in the open `(v,ℓ)` rectangle and a uniformly bounded Lipschitz extension to the closure. This is enough for the BV product bound; endpoint continuity of derivatives is not claimed solely from the first Volterra estimate. The complete lemma is `A_endpoint_BV_insert.tex`.

## Unfolding and the frequency window

The proof first approximates the sharp-source multiplier spectrally to arbitrary order, using individual eigenfunction/period bounds and Weyl's law to bound the discarded terms before unfolding. Taylor expansion around the fixed-width window center `T` turns the retained multipliers into even entire Paley–Wiener functions. Finite propagation is therefore applied to these retained terms, not asserted for the exact gamma quotient.

On the propagation set, the target-axis sum weighted by `(cosh r)^(-1/2)` is `O(e^(τ/2))`; multiplying by the source amplitude `O(e^(−3τ/2))` gives the integrable bound `O(e^(−τ))`. This controls the line-symbol remainder and justifies the source integral after image summation. The constant eigenfunction is rapidly small in `T` with an `e^(τ/2)` factor, also integrable after the source weight.

For maximal explicitness, the positive-frequency line-symbol integrals should be extended from positive `t` to the real line after restriction to this propagation set. The negative-frequency tail is rapidly small, with the same integrable majorant (allowing a harmless fixed polynomial in `r`). The Fourier transform of the retained window then restricts the leading difference phase exactly to the fixed interval `J`. The sum phase has no support because `τ≥2d0`.

## Stationary points and leading coefficient

The critical equations give `N1=−v sinhℓ/D` and `N0=Bcoshℓ−a²sinhℓ/D`. The normal equation implies `N2²=a²(coshℓ−B sinhℓ/D)²`. Therefore the target normal has inner product `−coshℓ` with one of `(B,0,±a)`, the translated source normals. Integrality forces `coshℓ=3|z′|`. A sufficiently small window about `d0=arcosh3` has only the critical value `d0`.

At every such critical point, `ℓ″(v)=a²sinhℓ/(D³E)>0`, so the phase `d0−ℓ(v)` has the same negative Hessian sign. All principal amplitudes and axis multiplicities are positive. The exact example `(s,t,z)=(4,0,1)` has `v=0`, `D=17`, `E=3`, and curvature `2√2/51`. The endpoint cannot equal `d0`, since this would require `s∓√3 t=72−48√2`, contradicting `Q(√2)∩Q(√3)=Q`.

In fact the critical set can be completely enumerated. At `ℓ=d0`, `|N1|<sinh(d0)/B=1/6`. Since `N1=√(3/2)t` with integral `t`, it follows that `t=0`, hence `v=0`, and then `s=4`, `z=±1`. Thus exactly the two unoriented axes with normals `(4,0,±1)` occur, with the established positive stabilizer multiplicities. Each unit axis multiplicity contributes `widehatρ(0)/(4·2^(1/4)√π)` to the real positive coefficient of `e^(−iπ/4)T^(−1/2)`. If the existing oriented-normal cyclic-stabilizer convention is retained literally, each unoriented axis has multiplicity two and the total coefficient is `widehatρ(0)/(2^(1/4)√π)`; the nonvanishing argument needs only positivity.

Exact symbolic checks of the critical normal identity, translated-source inner product, second derivative, and example curvature are preserved in `code/A_endpoint_BV_check.py,out`. All residuals are exactly zero.

## Audit result

The independently checked kernel normalization, complete-line spectral normalization, endpoint BV summation, localized unfolding order, and stationary-point signs are consistent. The proposed argument yields a nonzero fixed-width spectral window of order `T^(−1/2)` with endpoint error `O(T^(−1))`. The final implication to the sharp-count oscillation signs relies on the separately proved A.5.6 and is controlled by root's integration audit.
