# E17: exact old/new computation comparison

The isolated prior routine and its binding receipt were read after the
new E17 derivation had frozen and the target proof had been released.
Only the E17 slice was opened. The complete shared program and the
remaining embargoed routines were not read.

The old routine computes Gröbner reductions for the ideal
`(z*e,e**2,z**N)` for `N=1,...,12`. It checks that `e` survives those
truncations and that the listed monomials are normal forms. It then
inserts the stated maximum formulas for P1 cohomology and checks the
Euler difference at five selected integers. I reran that exact slice.

The new local calculation uses a representation instead of ideal
reduction. Send `z` to the zero two-by-two matrix and `e` to `E21`.
For a convergent germ f, the exact homomorphism is

    rho(f)=f(0,0) I + (partial f/partial e)(0,0) E21.

The product rule and E21²=0 prove multiplicativity. It kills z e,
e² and z^N for every N≥1, while rho(e) sends the first basis vector
to the nonzero second basis vector. This proves the required
nonmembership for every truncation by an explicit algebra map,
without relying on a finite Gröbner range.

For the global dimensions, the new program constructs the actual
two-chart Laurent Čech boundary for O_P1(−k). The finite-chart
monomials have exponents n≥0, and the infinity-chart image has
exponents n≤−k under the exact transition z^(−k). Every excluded
tail monomial pairs with its unique chart preimage, so removing
those pairs gives a finite complex with the same cohomology. Its
kernel is the overlap 0≤n≤−k; its cokernel is the gap −k<n<0.
The square-zero skyscraper adds one zero-differential degree-zero
generator. Choosing one pivot per image exponent proves the ranks
for all integer k. The program also computes seventeen actual
matrices to check these universal pivot formulas, without treating
that sample as the proof.

Both new algorithms were carried out after target-proof release.
The representation was added after the isolated old routine was
read. They supplement the independently frozen mathematical
derivation and add no separate independent-check event.
