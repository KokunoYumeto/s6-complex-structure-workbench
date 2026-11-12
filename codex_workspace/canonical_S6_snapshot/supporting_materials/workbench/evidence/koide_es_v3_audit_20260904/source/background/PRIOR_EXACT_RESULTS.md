# Exact mathematical conclusions

## Fixed-prime incidence

For a prime `p = 1 (mod 4)`, define `R=4j+3`, `a=(p+R)/4`. Then
`ES(p)` is equivalent to the existence of `epsilon in {0,1}` and positive
integers `u,v` such that

```text
uv=a^2,
R T - 4u = p^epsilon,
T = 3 (mod 4).
```

Writing

```text
ell_0=(T+1)/4,
ell_1=u-jT,
ell_2=1,
```

gives

```text
12 ell_0 - 4 ell_1 - 3 ell_2 = p^epsilon.
```

The exact terminal row operation is

```text
[1 -j; 0 1] [R -u; 4 -T] = [3 -ell_1; 4 1-4ell_0].
```

The divisor equation is the determinant-zero matrix

```text
Gamma=[u a; a v], det Gamma=0.
```

## Primitive ray

There is a unique factorization

```text
u=h r^2, a=h r s, v=h s^2, gcd(r,s)=1.
```

The two channels are exactly

```text
E: R divides pr+s,
M: R divides r+s.
```

For all hard primes, the full conjecture is equivalent to existence of
`h,r,s` with

```text
p/4 < hrs < p/2,
R=4hrs-p,
gcd(r,s)=1,
R divides pr+s or R divides r+s.
```

## Koide/S6 map

The selector matrix maps to the native S6 coefficient triple

```text
(t,m,b)=(u/2,a/2,3v)
```

and hence to

```text
G(t,m,b)=[u a; a v].
```

It lies on the determinant-zero Koide boundary, not on a regular S6 torus
fibre.

## Terminal topology

- `epsilon=0`: terminal determinant `-1`, trivial terminal group, and the
  source all-degree `S6` homology package.
- `epsilon=1`: terminal determinant `-p`, terminal group `Z/p`, and `Z/p`
  terminal homology in degrees 1 through 4.

## Exact channel dynamics

On Lorentz coordinates of the selector rank-one matrix, the exterior channel is

```text
B_p = p exp((log p) K_HY)
```

where `K_HY` is the standard boost generator in the H-Y plane. The middle
channel is the pure dilation `p I_3`. Thus the exterior primitive slope
`theta=s/r` maps to `theta/p`, while the middle channel retains `theta`; the
quarter coordinates satisfy `zeta_E(theta)=zeta_M(theta/p)`.

The hard-prime criterion can eliminate the content variable: for each
`p = 1 (mod 12)`, one needs `0<R<p`, `R=3 (mod 4)`, coprime positive `r,s`,
`4rs | p+R`, and `R | pr+s` or `R | r+s`. In the middle channel, if
`r+s=kappa R`, then

```text
p+4-(4 kappa-1)R = 4((h-1)rs+(r-1)(s-1)) >= 0.
```

## What remains

The full conjecture is exactly the nonemptiness assertion for the coupled
integral incidence at every prime `p = 1 (mod 12)`. Neither determinant
condition alone forces the other.
