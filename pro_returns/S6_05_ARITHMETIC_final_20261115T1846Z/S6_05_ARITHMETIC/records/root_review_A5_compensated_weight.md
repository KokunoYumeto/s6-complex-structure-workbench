# Root review of the compensated delta-weight test

The proof is an exact test of one analytic route, not an arithmetic-error lower bound. Root independently checked the actual polytope P, the scaled norm F, the cutoff preserving every solution for X>=16, and the Heath-Brown kernel flatness h=omega(r)/r for r in [2/3,3/4].

The radial substitution has Jacobian z^2 and a fixed triangle. Its upper face coefficient cannot cancel: all phases lie within 3pi/8 of a common direction, and the displayed rational rectangle lies inside the triangle with |f|<1/128. The two integrations by parts give the stated 1/k amplitude. The Euler divergence identity differentiates the full integral, not an unqualified asymptotic, and gives the correct negative top-face term. The derivative therefore has a nonzero limiting modulus. The second derivative is O(k), giving the discrete-mesh error O((1+k)/X).

The L1 boundary smoothing error controls the derivative difference by O((1+k)/H); choosing a sufficiently small fixed eta preserves a positive variation bound for k<=eta H. The exact Poisson normalization is X^-2 q^-3 S_q I_q with S_q=q^(3/2) times its Salié factor. Writing that factor divided by q leaves q^-1/2 I_q=X^(5/2)W_k, hence the direct absolute Abel bound has X^(1/2+epsilon)H scale. The possible 3/4 balancing exponent is explicitly a route envelope, not a proved full counting theorem.

The discriminant-square observation for c=(1,0,k) is correctly distinguished from a complete identification of the half-integral multiplier and its unary-theta projection. The record does not claim that Sun's conjecture cannot imply the requested result by a different transformation or a method retaining cross-frequency cancellation.

Verdict: PASS. The exact algebra and Arb output were read; no numerical integration is needed for the strictly positive lower constant.

Source SHA256: bc1a22db6cad92581b9ffd1f63d73dc7c4ddab75217e9aa10dba6da7440bdc4b
Reviewed: 2026-11-15T18:18:13.600939+00:00
