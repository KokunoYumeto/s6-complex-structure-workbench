# Independent axis and normal-line audit for the new Kato family candidate

Owner: boundary_d. Date: 15 November 2026. This records exact local calculations for AB's proposed family; it is not a claim to have constructed the S6 filling. AB owns the global annulus domains and the eventual numbered proposition.

## Two normal frames must be distinguished

The last blow-up chart is pi_n(z,w)=(z w^n,w), and sigma_s(z,w)=(kappa z,a w+(1−a)s), with 0<|a|<1. The actual Kato boundary identification is sigma_s composed with pi_n. Write v=w−s on the strict axis z=0. In the strict-transform normal frame z it gives

`v' = a v, z' = kappa (v+s)^n z`.

On an annulus avoiding w=0, use instead the blowdown normal frame x=z(v+s)^n. Then

`v' = a v, x' = kappa (a v+s)^n x`.

Thus AB's multiplier g_s(v)=kappa(a v+s)^n is correct in the blowdown frame. The two expressions differ by the explicit unit x=(v+s)^n z. On a fixed annulus |a|R<|v|<R and its gluing collars, this unit is nonzero for sufficiently small s, including s=0. This prevents a false sign or shifted-centre discrepancy between pi sigma and sigma pi.

The contraction pi_n sigma_s has fixed point (0,s), or v=0. The original blow-up centre w=0 corresponds to v=−s, not to the contraction fixed point. For s≠0 the germ can be diagonalized without a resonance hypothesis: the convergent product

`psi_s(v)=product_{k>=1}(1+a^k v/s)^n`

is nonzero near v=0 and satisfies psi_s(av)/psi_s(v)=(1+av/s)^(−n). The coordinate x_new=psi_s(v)x makes the normal multiplier kappa s^n and leaves v unchanged. This identifies the local Hopf marking exactly.

## Constant marked elliptic curve and normal family

The axis quotient has the fixed marking [v] in E_a=C*/a^Z, since v maps to av under the gluing. The point v=0 lies in the removed contraction ball, so the annulus marking is defined. Its central elliptic curve is the same marked E_a.

For the blowdown normal multiplier, the product

`H_s(v)=product_{k>=0}(1+a^k s/v)^n`

converges uniformly on the fixed annulus and its gluing collars. If, for example, |s|<|a|^2 R/2 after fixing sufficiently narrow collars, it is a nonzero holomorphic unit there. Its exact ratio is

`H_s(av)/H_s(v)=(1+s/(av))^n=g_s(v)/g_0(v)`.

This gives a genuine family isomorphism of the annulus-defined normal line with its central line. The fact that the product has zeros elsewhere in C* is immaterial: those points lie outside the chosen fundamental annulus and its gluing collars; one must not pretend g_s is a globally invertible automorphy factor on all of C*.

The central multiplier is kappa a^n v^n, of degree −n. One can check its relation with the blown-up Hopf description by a theta identity. With theta_a(av)=−v^(−1)theta_a(v), the divisor line O([p]) has multiplier −p/v. Hence, for p=−s,

`L_{kappa s^n} tensor O(−n[−s])`

has multiplier `kappa s^n (v/s)^n = kappa v^n`. This is equivalent to kappa a^n v^n by the nowhere-zero gauge v^n. The moving degree-zero Hopf normal factor and the moving exceptional-point divisor therefore cancel exactly in the marked normal class.

## The exceptional intersection divisor does not extend

The proposed punctured intersection divisor n[−s] on E_a has no limit in Sym^n(E_a). For any two distinct classes [v_1],[v_2], the sequences s_j=−a^j v_i tend to zero and give the distinct constant divisor limits n[v_i]. Consequently no analytic Cartier divisor on E_a times the disc can restrict to n[−s] on the punctured disc, even if a vertical component is allowed: remove its finite multiplicity along E_a times {0}; the remaining proper divisor would be finite of degree n over the disc and would define a continuous, indeed holomorphic, map to Sym^n(E_a), contradicting those limits.

This is precisely compatible with extension of the curve and its normal bundle. It forbids extension of the individual marked intersection divisor, not extension of its tensor product with the Hopf normal factor. To conclude the full global assertion that the noncentral Kato members are the n successive blow-ups of the corresponding Hopf surface, one still needs AB's global developing/blowdown comparison, not only this local normal calculation.
