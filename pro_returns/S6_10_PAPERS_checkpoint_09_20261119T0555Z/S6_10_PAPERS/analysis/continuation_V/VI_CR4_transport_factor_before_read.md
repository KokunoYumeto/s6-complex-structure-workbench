# Fresh isolated CR4/UN9 transport and reduced-support derivations

19 November2026. Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation. Only the parent's two clean isolated assertions and their stated inputs have been read. No VI CR4/UN9 target proof or review has been opened.

## 1. Uniform convergence of critical values on the full parameter segment

Let K be the stipulated fixed closed ball. The functions h_p are holomorphic on a common neighbourhood of K and depend holomorphically on p, so both h_p and their first derivatives converge uniformly on K to h_0 as p tends to0. The reduced critical set of h_0 in this neighbourhood is the given smooth curve and h_0 vanishes on it.

I claim the supremum of |h_(theta p)(x)| over theta in[0,1], x in K with dh_(theta p)(x)=0 tends to0. If it did not, there would be epsilon>0, parameters p_j->0, numbers theta_j in[0,1], and critical points x_j in K with |h_(theta_j p_j)(x_j)|>=epsilon. Compactness gives a subsequence x_j->x in K. Since theta_j p_j->0, uniform derivative convergence yields dh_0(x)=0. The given critical-set hypothesis then gives h_0(x)=0. Uniform function convergence and continuity imply h_(theta_j p_j)(x_j)->h_0(x)=0, contradicting the lower bound. This proves the requested uniform statement on the whole segment, including possible critical points approaching the boundary of K.

Fix t1 nonzero in the common small target neighbourhood where the stated boundary transversality holds. Choose p so small that every critical value from every h_(theta p) in K has absolute value less than |t1|/2. Then t1 is a regular value for all theta. Form

    X={(x,theta) in K times[0,1]: h_(theta p)(x)=t1}.

This is compact. At an interior point, the differential in x is surjective onto C. Given a desired theta velocity, one can solve the differentiated level equation by an x velocity, so projection X->[0,1] is a submersion. At a point of the boundary sphere the given transverse-boundary condition says the same equation can be solved with x velocity tangent to the sphere; equivalently the level and sphere meet transversely. Thus the projection is also a submersion on its boundary strata. The proper submersion theorem with boundary gives transport diffeomorphisms from the t1-level of h_p to the t1-level of h_0.

For clarity the boundary transport can also be constructed directly: choose local solutions for a vector field on X projecting to the unit theta vector and tangent to its boundary. A partition of unity preserves these two linear conditions. Compactness gives a complete flow for theta in[0,1], whose time maps are the desired diffeomorphisms. This gives the actual transport map used on homotopy groups.

## 2. Transport from the local regular level to t1

For fixed sufficiently small p there are only finitely many critical values in the chosen compact-ball neighbourhood. Locally the analytic critical set has finitely many irreducible components; on the regular locus of each component dh_p=0 forces h_p to be constant. Continuity extends that value to the component. Compactness of K permits a finite collection of such analytic neighbourhoods, giving finitely many values. This statement permits positive-dimensional critical components as well as isolated critical points.

Let t_local be the regular value carrying the specified small local sphere, and retain t1 from Section1. A small target disk with its finitely many critical values removed is path-connected. Choose a piecewise smooth path from t_local to t1 avoiding them; it may also avoid0 whether or not0 is critical. Stay within the common target disk on which the transverse-boundary condition was supplied. The compact pullback of h_p over this path is a proper submersion with boundary by exactly the differential argument above. Its transport gives a diffeomorphism Phi from the full t_local-level inside K to the full t1-level inside K.

If i includes the local fibre into the first full level and sigma:S^k->local fibre is the supplied sphere, the transported class is represented by Phi composed with i composed with sigma. Composing further with the segment transport Psi of Section1 gives Psi composed with Phi composed with i composed with sigma in the t1-level of h_0. These are the exact two transport legs. The induced maps Phi_* and Psi_* on the full-level homotopy groups are isomorphisms. Any assertion that i_*[sigma] is nonzero is a separate local-to-global input; transport preserves that class and does not by itself prove the injectivity of i_*.

## 3. Singularity of the reduced support of y^3 u

Now take the supplied germ f=X^2+y^3 u(y,z), where u(0,z) is not identically zero and u(0,0)=0. The latter condition makes u a nonunit. The former says y does not divide u in C{y,z}. Factor u into its unit and irreducible analytic factors, using Weierstrass preparation and the resulting unique factorization. At least one irreducible factor vanishes at0; none is associated to y. Let v be the product of the distinct nonunit irreducible factors of u. Then v(0,0)=0, v has no repeated irreducible factor, and y does not divide v.

The reduced support of y^3u has the exact reduced local equation F=y v: removing the unit and repeated powers preserves precisely the vanishing set, and y and v share no irreducible component. The derivatives are

    F_y=v+y v_y,  F_z=y v_z.

Both vanish at0. Since F is reduced and defines a plane curve, the hypersurface Jacobian criterion proves that its reduced support is singular there. Equivalently its distinct component y=0 meets at least one other reduced component through0. This is a statement about that actual reduced equation; it does not infer a singular support merely from the multiplicity three in y^3.

All requested assertions have now been derived before the target excerpts were opened. The exact map on the local spherical class is recorded so that no stronger local-to-global injectivity claim is silently introduced.
