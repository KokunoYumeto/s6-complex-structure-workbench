# Paper I — preread derivation of push:src:D.4.6 (tag 032O)

The target compendium derivation remains unopened. The target is a statement of the role and exact scope of several results, rather than a new numerical estimate. Inputs read as statements: D.4.2, D.4.4, D.4.5, D.4.7, D.4.8 and ari:C.8.15. The published Lin–Wang primary PDF was opened at pp.912–913, equations (1.1) and Theorem 1.3 (Annals 172 (2010), 911–954; PDF pp.3–4 including its cover).

## Exact comparison maps

Lin–Wang use G_tau(z)=−(1/(2pi))log|theta_1(z,tau)|+(Im z)^2/(2 Im tau)+C(tau), with derivative −(1/(4pi))[(log theta_1)_z+2pi i Im z/Im tau]. Thus their fibre critical-point equation is exactly Z(z,tau)=0 with the convention of D.4.4. The map from the present problem to that equation is evaluation along the analytic section tau -> (mu(tau),tau), wp_tau(mu(tau))=0. This identifies the first factor exactly; it does not require claiming that the two subjects have no relationship.

Theorem 1.3 bounds, for each fixed tau, the number of z satisfying Z(z,tau)=0 by five. To determine the present first critical factor one must determine the inverse image of this zero locus under that section. The theorem's fibrewise cardinality bound alone supplies no assertion about the zero set of this inverse image as tau varies. The second factor F=3Z wp'_tau(mu)−2g_2 appears in the tau-derivative formula of D.4.4; it is absent from the equation displayed in the statement of Lin–Wang's theorem. The precise proof dependency therefore remains the present factor-zero result, not an inference from a fibrewise count.

## Composition of the stated inputs

The standard identity theta'_1/theta_1=zeta−eta_1 z identifies the W of ari:C.8.15 with Z. That result states Z=0 exactly on the modular orbits of i and rho, and F=0 exactly on the orbit of rho, for wp-zero sections. Combined with D.4.4, this excludes ordinary critical points away from the ramification/special points. D.4.5 computes the coarse t-gradient at rho: its nonzero linear term 7 Re(t)/(32pi) gives partial_t D=7/(64pi), even though both factors vanish in the ramified tau/root coordinate. This accounts for the special orbit rather than deleting it from the critical equation without a coordinate comparison.

The bound and cusp limit identify compact finite level sets; D.4.2 provides that formulation and the sign domains. D.4.7's stated root-neighbourhood/cusp exclusions and D.4.5's nonzero coarse gradient control the listed boundary pieces. The global factor-zero classification ari:C.8.15 additionally supplies the radial strict monotonicity and Jordan-level conclusion used by D.4.8. Thus the target's phrase about a completed nonvanishing certificate must be read with the explicit i,rho exceptions just stated, and with the separate global classification as input. D.4.7 by itself is not a certificate on the whole remaining compact region.

## Exact numerical work and scope

The coefficient comparison is (6/pi)(7/384)=7/(64pi), and the real linear term is twice its Wirtinger derivative, 7/(32pi). No interval cover was run for this target, and no independent proof of ari:C.8.15 is claimed. The new work checks the exact morphism between the equations, the dependency composition, the branch-point convention and the primary theorem's actual assertion. The target printed derivation has not been read at this save.

Saved UTC: 2026-11-21T00:52:53.878733+00:00
