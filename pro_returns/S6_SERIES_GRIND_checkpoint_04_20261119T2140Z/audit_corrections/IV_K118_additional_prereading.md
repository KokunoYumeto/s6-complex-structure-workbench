# Further K118 derivations before opening its supplied proof

The K118 statement and earlier K109–115 endpoint/page arguments have been read. No K118 proof block has yet been opened by this auditor. The following derivations extend the frozen IV_open_prereading.md record; their remaining geometric inputs are stated explicitly.

Put M=mh and b=6/a. The proposed canonical page has base degree M, with m points over the finite cap (ramification h), h points over infinity (ramification m), and M unramified selected nodal points. The actual page morphism producing these ramification data still needs to be checked in K118. With those stated geometric data, the Euler sum is

`12 chi = M + 3m*(finite root is III) + 4h*(infinity root is IV)`.

The source height is1/6, so the actual pullback height would be `H=M a²/6`. The primitive family is a degree-b quotient of the canonical family, and the proposed literal family morphism must be established before using that fact. Characteristic naturality then gives `k0=Ma²/(2b)` and `ell0=24chi/b`. Substitution yields exactly the four printed pairs:

| (a,b) | M | chi | (k0,ell0) |
|---|---|---|---|
| (1,6) |12kl|kl|(kl,4kl)|
| (2,3) |3l(4k+1)|l(k+1)|(2l(4k+1),8l(k+1))|
| (3,2) |4k(3l+2)|k(l+2)|(9k(3l+2),12k(l+2))|
| (6,1) |(3l+2)(4k+1)|kl+l+2k+1|(18(3l+2)(4k+1),24(kl+l+2k+1))|

For the endpoint, the sphere equation `h n_inf + m n_0 = epsilon` makes gcd(m,h)=1 and each local norm coprime to its root order. It also gives the integrality of `d=(3epsilon−mn_0)/b`: for b=3 it is direct; for b=6 or2 the parity follows from h divisible by4 and m odd. The proposed map is

`E_r=gamma0 r^(−epsilon J0) t^d U^epsilon`, `J0=mh/b`, `gamma0^b=c0 C_a^(−epsilon)`.

The b chronological root phases contribute `exp(−pi i epsilon J0(b−1))=1`: b odd gives an even(b−1), and b even has even J0 in the stated progressions. Its full source coefficient telescopes by the literal identity `U^b=(C_a q/t³)B0^(−1)` to

`E_(zeta_b^(b−1)r)...E_r = c0 q^epsilon t^(−mn_0) B_lambda^(−epsilon)`.

The claimed K67 phase is transported by the actual scalar function `F_r=r^(epsilon J0(b−1)/2)`, whose exponent is integral and whose ratio under r→zeta_b r is precisely that phase. Extension of this family map through both cap graphs remains a geometric check.

The full divisor necessity should read

`ord_0 H=3j/b−n_0 J/h`, `ord_inf H=−2j/b−n_inf J/m`, `ord_selected H=−k`.

Its degree gives `j=bk+epsilon J/J0`, hence J0 divides J. This retains both independent root-reference integers. The negative-lift obstruction at infinity remains nonzero because gcd(m,n_inf)=1 and m≥2, so `n_inf+m nu` cannot be zero for any integer nu. The actual single-valued covers and both entire reference maps must still be checked.

This record is an independent derivation of the proposed arithmetic and endpoint word, not a pre-emptive claim that the two-cap geometry or all-fan image is proved.
