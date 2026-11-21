# Cusp line bundles: exact cocycle and Chern convention

This is a supplementary check of `pub:V:cusp-chern-generators` (PV13), shared with the topology checker before its new proof was integrated. It independently differentiates an explicit Hermitian metric. The earlier source's line-bundle assertion and cocycle paragraph had already been read, so this is not described as a blind re-proof of the entire lemma.

Let S be an integral symmetric n by n matrix, n=2 or 3, and set

q_S(lambda) = (lambda^t S lambda - sum_i S_ii lambda_i)/2.

The value is integral: each lambda_i^2-lambda_i is even, and each off-diagonal contribution occurs twice. The identity

q_S(lambda+mu)=q_S(lambda)+q_S(mu)+lambda^t S mu

gives the exact factor-of-automorphy cocycle

f_lambda(q^mu x,q) f_mu(x,q) = f_(lambda+mu)(x,q),

where f_lambda(x,q)=q^(-q_S(lambda)) x^(-S lambda). The integral vertex values interpolate on each unimodular Kuhn simplex to integral Cartier data. Translation changes the interpolant by the stated integral affine function; equality at the vertices proves equality on every simplex. The data therefore descend to the period quotient.

For the sign of the Chern class, write q=exp(2 pi i s), y=Im(s)>0, x_i=exp(2 pi i z_i), and z=u+s v. Thus the angular classes are a_i=du_i and the deck classes are b_j=dv_j. The factor becomes

f_lambda(z)=exp[-2 pi i (s q_S(lambda)+lambda^t S z)].

The positive Hermitian squared norm

h(z)=exp[-(2 pi/y)(Im z)^t S(Im z)+2 pi diag(S) dot Im z]

satisfies h(z+s lambda)|f_lambda(z)|^2=h(z). This identity follows by expanding the quadratic form and substituting the displayed formula for q_S. It does not require S to be positive definite.

The linear term in Im z has zero curvature. The Chern form of this metric is

(i/(2y)) sum_ij S_ij dz_i wedge d(conjugate(z_j)).

Since S is symmetric, its du-du and dv-dv terms cancel. The remaining term is (conjugate(s)-s) sum_ij S_ij du_i wedge dv_j = -2iy sum_ij S_ij du_i wedge dv_j. Multiplication by i/(2y) gives precisely

c_1 = sum_ij S_ij a_i wedge b_j.

This proves the positive sign in the paper's angular/deck convention. It also shows explicitly that the extra diagonal character in the factor of automorphy changes the Hermitian norm by a curvature-free linear term. The specialization and invariant-algebra generation parts of PV13 remain within the topology checker's scope.
