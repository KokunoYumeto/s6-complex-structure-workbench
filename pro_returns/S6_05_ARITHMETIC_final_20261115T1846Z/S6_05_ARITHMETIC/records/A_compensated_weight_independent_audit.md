# Independent audit of the full compensated delta weight

Auditor: count agent; 15 November 2026.

Result: **PASS**, within the stated scope.

The following points of records/B_A5_compensated_weight.tex were checked
directly, independently of its symbolic certificate.

- The cone and its z=1 face are exactly the sharp region in the (s,t,z)
  variables, apart from measure-zero endpoint conventions. Multiplication
  by chi(F(y)) leaves every counted F(Xy)=−2 lattice point unchanged for
  X≥16.
- The displayed Heath-Brown kernel is flat exactly, not asymptotically:
  on r in [2/3,3/4] its first sum contains only j=1 and the second sum is
  zero throughout |F(y)|≤1/64, including the shift 2/X².
- The substitution s=zu,t=zv has Jacobian z² and the stated triangular
  domain. The radial integration by parts has the correct negative
  upper-face sign. Both the amplitude and its first derivative vanish
  at z=0, so the error is uniform O(k⁻²).
- Rotation by e((33/8)/r) confines the top-face phase to an interval
  of half-width 3pi/8. The rational rectangle is contained in that face
  and in the region chi=1. This proves the uniform positive lower bound
  for A(r) without a floating-point nonvanishing inference.
- The Euler differentiation formula has the correct signs. Angular cone
  faces have zero Euler flux. The radial face supplies the only leading
  term. J'_k and W'_k follow without differentiating an uncontrolled
  asymptotic remainder.
- Differentiating the exact integral twice, then integrating once in z,
  proves W''_k=O(k). This supplies the mesh comparison with error
  O((1+k)/X). Summing gives O(log H+H²/X).
- The L1 smoothing error gives both the stated zeroth-order difference
  and the O((1+k)/H) derivative difference. Comparing variations via the
  integral of this derivative difference avoids any unsupported uniform
  bound on the second derivatives of the smoothed cutoff. Choosing a
  sufficiently small fixed fraction k≤eta H retains a positive variation.
- In the Poisson normalization,
  X⁻²q⁻³S_q(c)I_q(c) becomes
  X^(1/2)(T_q(c)/q)W_k(q/X), up to the fixed residue-class Gauss factor.
  The harmless overall delta-method normalizing constant does not change
  the power or variation conclusion.
- For c=(1,0,k), the dual value is k²−18, nonsquare for k≥10. The proof
  correctly does not infer the vanishing of the complete, as-yet-unmatched
  unary-theta projector from this observation alone.

The record proves a linear growth of the **analytic variation norms**
that occur in termwise Abel summation. It does not give a lower bound
for the arithmetic remainder. The balance sqrt(X)*H + X/H has minimum
at H=X^(1/4), of scale X^(3/4), but the record explicitly does not claim
a complete X^(3/4) theorem: the other frequencies and local factors
remain to be analyzed. It also makes no claim that the full arithmetic
content of Sun's conjecture cannot imply the desired bound by another
method.
