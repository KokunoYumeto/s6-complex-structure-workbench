# Exact two-period action on the repaired collar: working calculation

Status: exact identities proved; a global complementary cap and proper period quotient are unconstructed. This note is not a numbered result.

Use the B.4.21 convention `a=exp(-2*pi*i*mu)`, with `0<|a|<1`, and

`G_a(H)=product_(j>=1)(1+a^j H)`.

On a sufficiently small fixed H-disc this converges uniformly, is nonzero, and obeys `G_a(aH)=G_a(H)/(1+aH)`. In the actual repaired coordinates `Z=x G_a(H)`, the first period is

`A:(Z,H) -> (kappa(q) q Z, a(q) H)`.

The desired second period in these linear collar coordinates is

`B:(Z,H) -> (c(q) Z, b(q,r) H)`,

where `c=a^-6` is the retained translation by `6P` in this convention and `b=q r^12 D(q)` for the actual holomorphic unit `D`. It therefore has the exact expression

`B:(x,H) -> (c x G_a(H)/G_a(bH), bH)`.

This commutes with A wherever both expressions are defined. The functional identity proves commutation before any analytic continuation. It gives the actual local second-period action, but it does not extend it automatically through the full Kato complement.

For fixed `a`, `G_a` extends to an entire function of H, with simple zeros `H=-a^-j`, `j>=1`. Hence the formula defines a meromorphic conjugacy on larger charts; it need not define a holomorphic automorphism there. In particular it cannot be used to assert a quotient is Hausdorff or proper, nor can all of its zero divisors simply be retained in ordinary torus fibres.

## The F=0 corner

In the B.4.22 third chart,

`q=u v F`, `H=(1-F)/F`, `r=g(1-F)`.

The first Kato period becomes

`F' = F/(a+(1-a)F)`,

`u' = kappa u^2 v (a+(1-a)F)`,

`v' = 1/(kappa u)`.

It preserves q exactly. With `g'=r/(1-F')` it also preserves r on the relevant overlap. Thus this is an explicit meromorphic expression, not a globally regular automorphism of the local resolution. Its leading expression along F=0 is parabolic and may motivate another quotient construction; none is claimed here.

The apparent denominator in `bH` cancels:

`bH = r^12 D(q) u v (1-F)`.

Consequently `G_a(bH)` is holomorphic near F=0 on bounded small-coordinate regions, while the numerator `G_a(H)` still has its accumulating zero pattern at the omitted end. This cancellation is a useful exact compatibility target. It does not resolve the numerator, the exceptional-curve persistence, the original q-deck descent, or properness at the missing base origin.

The expression `W_test=1+H=1+r/f` should not be confused with the marked multiplicative normal coordinate H. If one separately requires `W_test -> b W_test`, then `f -> r f/((b-1)f+b r)`. That Möbius identity is conditional and is not the actual first-period action, which scales H.

Finite symbolic identities are verified by `code/ab_push_full_period.py`; its output is retained beside the script.
