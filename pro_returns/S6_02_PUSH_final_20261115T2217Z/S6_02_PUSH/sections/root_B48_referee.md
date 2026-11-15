# Independent root check of B.4.8

Checked on 15 November 2026 against the explicit line-factor construction, without using a conjectural analytic filling.

The chosen logarithm of the contracting unit gives a smooth marked torus family over the full parameter disc. The normal line has fibre degree zero and clutching factor `q^m b(q)` along the second lattice generator. Its mixed first Chern class evaluates to `m` on the second generator swept around the positive parameter circle and to zero on the first. Under `q=s^N epsilon(s)` this becomes `mN`, since a holomorphic unit on the disc has zero winding. This proves an integral obstruction, independently of any divergent representative of a logarithm.

For a proper connected semistable genus-one curve family, the normalization sequence gives `1=sum genera+b1(dual graph)`. An all-rational centre consequently has a unique graph cycle. Each cycle neck contributes a positive Dehn twist about the same primitive genus-one class. Their product is `T^k`, with `k>0`, and cannot have the identity homological monodromy of the given good-reduction elliptic family. Separating rational tails contribute no homological transvection. Thus the centre must have an elliptic core and rational trees.

Two loops on that core can avoid its finite set of attaching points and have intersection one. The submersion near those compact loops transports them over a small full disc. Each resulting boundary torus bounds a solid torus in the total interface. The first Chern class of an extending line bundle therefore pairs to zero with both. Under an arbitrary isomorphism of the punctured elliptic families, their mixed projections are an integral basis; translation winding can add fibre classes but these have zero pairing with the degree-zero line. The nonzero covector `(0,mN)` cannot vanish on both. This checks both the rational-tail extension and the unmarked-translation qualification.

An additional tensor factor extending on the same interface has zero pairings by the same bounding argument. This includes Cartier divisors already defined on that interface. It does not include a replacement interface that is singular or non-flat outside the stated semistable-curve category. Cancellation of opposite windings in a product of normal lines does not extend either individual factor.

The diagonal Hopf axis and its derivative give exactly this line factor. The actual cusp's nonzero contracting period unit is sufficient for good reduction of the axis. No claim that every possible filling contains this axis has been established or used.

The independent rerun of `code/ab_push_hopf_winding.py` is retained as `code/root_ab_push_hopf_winding_rerun.out`. It passes the exact transvection, common-invariant lattice, Smith-form and cusp-unit algebra. Those finite checks supplement the preceding geometric proof; they do not prove the existence or nonexistence of an unrestricted S6 filling.
