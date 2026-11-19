# Fresh prereading derivation of the P1.8 cusp height

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

Only `analysis/continuation_V/P1_8_cusp_height_statement_input_packet.md` has been read. The target proof and its earlier producing computation remain unread. This derivation concerns precisely the supplied height for an arbitrary bounded canonical splitting.

## Exact maps and nilpotents

Let d=(0,1,1,1)^t, let alpha=a_0(q), and write s=x+i y. Direct multiplication of the supplied companion matrices gives D a=alpha d and D squared zero. On the lexicographic exterior-square space the induced infinitesimal map is E(v wedge w)=D v wedge w+v wedge D w. Since D has rank one, the quadratic exterior term vanishes. Thus the actual exterior monodromy is I+E and E squared is zero.

The given invariant q_inv is killed by E. The prescribed quotient map is explicitly

pi(w01,w02,w03,w12,w13,w23)=(w02-w01,w03-w01,w12-w01,w13-w01,w23-w01).

Direct substitution gives pi E=N_W pi, where N_W is the displayed lower block of N_V. Write the first row block of N_V as n=(0,0,-1,1,-1). Its product with N_W is zero. Consequently N_V squared is zero, and I+s N_V and I+s N_W are the actual exponentials used in the canonical-frame maps.

The contraction c obeys c(q_inv)=2 and

c(a wedge d)=alpha,   n pi(a wedge d)=alpha.

These identities follow by expanding the six exterior coordinates: a wedge d has coordinates (alpha,alpha,alpha,a1-a2,a1-a3,a2-a3). No primitive representative is substituted for the given quotient without its map: the primitive representative is w-c(w) q_inv/2, whose image under pi is exactly pi(w).

The decomposable line a wedge H maps injectively to W. Indeed, a nonzero multiple of q_inv has nonzero exterior square, whereas every a wedge v has square zero; q_inv wedge q_inv equals twice the volume element. Since alpha stays nonzero near the puncture, pi(a wedge e1), pi(a wedge e2), pi(a wedge e3) are a holomorphic frame for the untwisted rank-three bundle on a small disk. In this frame the given bounded splitting has bounded coefficients. Its first component therefore defines a bounded linear functional b_q on that bundle, and its remaining five components are the prescribed inclusion into W.

## The actual real vector and its canonical coordinates

Put eta=i u wedge conjugate(u), r=pi(eta), r0=i pi(a wedge conjugate(a)), and p=pi(a wedge d). The vector eta and hence r are real in the stipulated flat frames. Because u=a+s alpha d and d wedge d=0, the exact expansion is

eta=i a wedge conjugate(a)+i conjugate(s) conjugate(alpha) a wedge d+i s alpha d wedge conjugate(a).

Set A0=i c(a wedge conjugate(a)), a bounded real quantity. Applying c and using c(a wedge d)=alpha gives the exact identity

A=A0+2 y |alpha| squared.

Since alpha(0) is nonzero, A is bounded below by a positive constant times y for all sufficiently large y. The assumed positivity is therefore compatible with the computed sign.

The exact untwisting map gives

r_can=(I-s N_W)r=r0+2 y conjugate(alpha) p.

To verify the equality, apply E to the exterior expansion: E eta=i alpha d wedge conjugate(a)+i conjugate(alpha) a wedge d. Subtracting s times its image cancels the d wedge conjugate(a) term and leaves i(conjugate(s)-s)=2y multiplying conjugate(alpha) p. Thus r_can lies in the specified canonical rank-three bundle and is O(y), uniformly as q tends to zero. Applying n, and using n N_W=0 and n p=alpha, yields

n r_can=n r=n r0+2 y |alpha| squared.

In particular this quantity is real. The exact restoration of the chosen splitting to flat frames is

sigma(r)=(I+s N_V)(b_q(r_can),r_can)=(b_q(r_can)+s n r_can,r).

The conjugate has the same real quotient component r, so their difference is entirely in the specified invariant vector e. No change of lift or quotient is involved.

## Height and uniform remainder

Taking the imaginary part of the first coordinate in that last identity, the definition of h becomes

A h=Im(b_q(r_can))+y n r0+2 y squared |alpha| squared.

Subtract y times A. The exact remainder formula is

h-y=[Im(b_q(r_can))+y(n r0-A0)]/[A0+2 y |alpha| squared].

The vector a and its conjugate are bounded on a closed smaller disk; alpha is bounded away from zero; r0, A0 and n r0 are bounded; and the bounded canonical splitting applied to r_can=O(y) is O(y). The numerator is therefore O(y) and the denominator is bounded below by a positive constant times y. It follows that h=y+O(1), uniformly on the stipulated branch strip. The displayed identities in fact contain no additional real-part growth: the x terms disappear because n r_can is real. Every bounded holomorphic choice of the canonical splitting satisfies the same estimate, with a remainder bound depending on its bounded coefficients.

This is a full derivation of the isolated asymptotic with its precise coefficient and positive sign. It uses the actual quotient, contraction, canonical untwisting and restoring maps from the statement packet. Its fresh symbolic check will verify these identities from the supplied matrices before the target proof is opened.
