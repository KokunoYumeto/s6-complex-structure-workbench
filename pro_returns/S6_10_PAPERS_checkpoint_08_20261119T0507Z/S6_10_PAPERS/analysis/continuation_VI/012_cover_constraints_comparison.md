# Cover, lattice and group constraints: printed comparison

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

The twelve statements in this receipt were extracted without their proofs. The written prederivations are in `011_cover_constraints_prederivations.md`. The complete printed proofs were then read and compared, including the two separate arguments printed under UN.22. No mathematical fault was found in this batch. A prereading gate is part of the provenance and is never retroactively erased by a successful comparison.

## UN.22

The printed elliptic-first-integral argument has eight steps and its completion has ten. The vertical translation field makes a horizontal polar divisor of the other field impossible: a finite intersection with a smooth elliptic fibre cannot be invariant under the full translation field. The projected nonzero base field is semicomplete. The proof explicitly lifts an inverse-time loop near a proposed base pole using properness of the elliptic fibration and local holomorphic ODE continuation; the one-dimensional branching contradiction therefore applies to the actual field, not merely to a formal quotient. It gives base genus at most one.

The transverse commuting flow transports the vertical time form on whole compact smooth fibres. Its periods give an injective map from integral first homology to one fixed copy of C. Continuation preserves these complex numbers, so the integral monodromy is the identity. The Kodaira list reduces a singular fibre to a possible multiple of I_b; the actual normalized root cover is étale and relatively minimal, and identity monodromy forces I_0. Contraction with a meromorphic base form gives a meromorphic canonical form with vertical divisor. The resulting K²=0 and Euler number zero imply χ(O)=0.

The completion treats algebraic dimension zero, one and two. For dimension one the algebraic reduction gives an actual equality of meromorphic function fields; proportional projected fields give a vertical linear combination. For the projective dense-leaf branch, an invariant polar multisection is normalized, and finite base change plus the finite Aut(E,0) torsor gives an actual product model. The lifted field is tangent to the marked zero section; its fibre coefficient vanishes, contradicting the dense-leaf alternative. This closes the prerequisite for the first argument. The exact period-transport construction was a prereading gate, so this is a targeted proof check.

## UN.23

The affine lift to C² follows because its derivative is periodic. Pulling a pluricanonical section through the resolved quotient graph produces a constant torus form. A branch curve would force a positive zero divisor, which this form cannot have. The free one-eigenvalue case is the actual product-isogeny bielliptic quotient. In the isolated fixed-point case, translating the fixed point gives a linear action. After choosing a generator, the local weights are (1,r). A ray in the quotient lattice of height less than one gives the negative valuation of a pulled-back pluricanonical form, exactly as in the prereading derivation. For determinant one the height-one subdivision is crepant. The printed proof also computes the quotient fundamental group by killing the fixed-point affine elements; the prereading proof instead used the resulting trivial canonical line and invariant b₁=0 in the surface classification. Both give K3 and exclude an Enriques quotient. This is a complete independent re-proof of the stated classification, with an alternative final K3 identification.

## UN.26

The printed construction uses a meromorphic section of the relative dualizing direct image and its dual vertical field. The prereading construction used the generic rank-one coherent direct image of the relative tangent sheaf. On the smooth locus the explicit morphism is contraction: the relative differential ω and the field V satisfy ω(V)=1 after multiplying by the chosen meromorphic base scalar. These give the same meromorphic line of fibre translations. Closedness of the uniformizability locus supplies semicompleteness at remaining regular points. The ratio h∘q has Stein factor q, and finite character projection plus an invariant h gives the equivariant span. Every assertion was derived before reading, so an independent re-proof is recorded.

## UN.28

The proof constructs compact cycles from the exact sequence of the boundary pair, rather than identifying lattices without a map. On an actual multiplicity-one root component the compact neighbourhoods are displaced by smooth real horizontal fields for the base coordinate into a fixed nearby torus. Complex orientation gives the same intersection forms, and the neighbourhoods for different components are disjoint. Holomorphic two-forms give positive real two-planes orthogonal to all boundary curves, so the signature (3,3) gives 2Σp_g≤3. The finite-base-change assertion uses the same map on the resolved model. This agrees with the complete prereading construction and supports an independent re-proof.

## UN.29

All thirteen numbered steps and the intervening return-map calculations were compared. The crucial proof uses actual flow returns. In a flow box the fields are V₁=∂_u and V₂=h(z,s)∂_u+A(z,s)∂_z, with h(z,0)=H(z), A=s^d(a+O(s)), a≠0 and H′≠0. A representative time path for each elliptic period avoids the discrete set of removed boundary points. A compact chain of ambient flow charts gives a genuine germ

Φ_i(u,z,s)=(u+δ_i(z,s),φ_i(z,s),s),

with φ_i(z,0)=z and δ_i(z,0)=c_i−λ_i(z). Preservation of V₂ gives A(φ_i)=Aφ_i′ and h(φ_i)=h+Aδ_i′. The second identity and invertibility of H′ first imply φ_i−z=O(s^d). Writing its leading coefficient as ψ_i, the coefficient of s^(2d) in the first identity is a′ψ_i−aψ_i′=0; the coefficient of s^d in the second is H′ψ_i=−aλ_i′. Thus ψ_i=k_i a and λ_i=d_i−k_iH for constants k_i,d_i. Analytic continuation on the universal cover uses the global function H itself, proving that the periods are single-valued; this gives identity integral monodromy. No extension of the component first integral to the ambient threefold is asserted or needed.

The period ratio lies in the upper half plane; its bounded Cayley transform extends to the compact base and is constant. The root-cover and Kodaira argument gives only smooth multiple fibres. Translation transition maps, including the free translation model at a multiple fibre, give R¹q_*O=O. Coherent Leray gives p_g=g and q=g+1, and UN.28 gives g≤1. The actual stabilizer quotient preserves the intrinsic Iitaka map, with its quotient singular fibres retained. This resolves the explicit prereading gate, but the check remains targeted.

## UN.31

The actual generically finite root component pulls back pluricanonical forms, giving the claimed Kodaira-dimension restriction. The unique nonruled minimal model carries the finite stabilizer action. The intrinsic Iitaka or algebraic-reduction map descends, and a rational quotient fibre would contradict the pulled-back pluricanonical section by restriction. In the bielliptic case the printed proof also uses the intrinsic orbit fibration of Aut⁰; that case was not fully developed in the prereading note, so this check is targeted. On the original minimal model, the relation 0=ρ*K_Z·F+Σa_E E·F, with all summands nonnegative, proves that exceptional curves are vertical. The χ values and base genus then follow from the stated invariants. The subsequent UN.32 result still requires its own review.

## UN.33

The twelve-step local/global argument was compared. Quotienting a smooth multiple-fibre chart (F′×Δ_z)/〈(v,z)↦(v+τ,ζ_m z)〉 by a fibre translation group leaves the actual residual translation τ̄ of order m′. The subgroup acting only on the disc is removed by w=z^(m/m′), so the residual model has multiplicity m′. This justifies keeping every smooth multiple fibre.

At a branch point with nontrivial elliptic linear part β of order s, commutation forces βτ=τ and hence m divides s. A lift fixing a point has its s-th power equal to the identity deck element, while its disc character has primitive base order; this gives gcd(m,s)=1 and therefore m=1. A finite affine cocycle is removed by the displayed finite averaging formula. The remaining local quotient has weights (r,1), with d∈{2,3,4,6} and r=1 or d−1. The actual invariant coordinates T=z^d, X=z^(2r)x and Y=z^(3r)y yield the asserted minimal Weierstrass equations and discriminant orders. These identify II/II*, III/III*, IV/IV*, I₀* without suppressing a translation kernel.

The two branch points over a rational covering base give the four complementary pairs. For an elliptic covering base, fixed-point determinants give signatures (2,2,2,2), (3,3,3), (4,4,2), (6,3,2); every fibre character is enumerated, including characters with a nontrivial kernel. The resulting eleven distinct configurations have Euler number 12 or 24. The canonical character and the p_g bound give the χ values. The detailed local quotient identification was a prereading gate; this is a targeted check.

## UN.36

The printed compact-core transfer retains the exact multiplicities m_i in the pairing Σm_iQ_i. A compact family over the whole base disc proves invariance under the actual base-changed monodromy. A kernel vector lies in the radical because it pairs trivially with every transported source vector. Full-rank discriminant is the square of the lattice index in the unimodular torus lattice. The boundary-dimension inequalities follow by intersecting negative definite subspaces with boundary orthogonals. The oriented Λ² calculations give signatures (3,3,0), (1,1,2), (1,2,1), (2,1,1); the last two retain their orientation signs. The proof agrees with the complete prereading construction. Its use of UN.11 for N²=0 is separately pending.

## UN.38

The adjunction and full-fibre identities give the asserted actual local trivialization of a positive power of K. On a diagonal primary Hopf surface, torsion of an axis normal bundle gives β^n=α^j with j>0 and a meromorphic monomial, contradicting algebraic dimension zero. On the nonlinear contraction the printed proof uses a local divisor trivialization with leading coefficient c z^(−k); comparison of the resonant Laurent coefficient in degree w^(j+r) has zero left coefficient and nonzero right coefficient. The prereading canonical-trivialization equation is the same identity after multiplying by the axis defining section to the relevant power. The printed proof additionally establishes the complete axis description of compact curves using extension across the origin and the contraction eigenfunction equation. This extra step makes the boundary conclusion exact. That step was not fully written before exposure, so this is a targeted check. Finite primary covers pull back the actual local trivialization and boundary complement.

## UN.39

The SNC stratum Euler calculation, A’Campo average and every blowup correction match the prereading derivation. Averaging first over a common multiple of all component multiplicities and the semisimple order is essential and is done in the proof. The result e(S)=j(T)−2I_π proves resolution independence. The nineteen cyclotomic cases and the quartic-centre example were rerun independently. The latter has five rational double curves, one genus-three double curve and four triple points, giving index one and Euler number −2; removing the actual resolution-centre contribution recovers zero for the original smooth-torus model. This is an independent re-proof, subject to the separately tracked A’Campo source check.

## UN.44

All fifteen steps were compared. The printed proof first constructs a tube retraction by a Łojasiewicz gradient length bound. It then uses the punctured torus bundle and general-position meridians, exactly as in the prereading presentation argument. The meridian relations kill x^{v_i}t^{m_i}; projection gives Z/d. The normalized root f=u h^d, w^d=u, s=wh is genuinely étale at the entire support. The proof constructs inverse maps between the lifted presentation with generator w=t^d and the four-generator lattice presentation, rather than merely comparing their abelianizations. Conjugation and Bézout eliminate w and give the precise relation lattice R_d.

The actual SNC mapping-cylinder model maps to the dual complex and kills each vertex group. Pullback of H¹ through the finite-index image A is injective, and the exterior algebra of the torus forces cup-product injectivity on the dual complex. The finite cover corresponding to the image of A gives the rank-at-most-two conclusion for the virtually abelian dual group. Equal multiplicities and no-eigenvalue-one conclusions use the stated root model and trace formula. The group/lattice/dual-complex assertions were fully rederived before reading; the printed gradient construction of the retraction was a supplementary step not developed in the prereading note. The conservative whole-row classification is targeted proof check.

## UN.47

Every finite group quotient is realized by an actual finite étale cover of the tube. Stein factorization gives the disc base change and connected nearby finite torus cover. Component lifts are indexed by the precise cosets of the component image; induced covers of their smooth resolutions are étale. Applying UN.28 to all lifted components gives the positive-p_g surjectivity statement. Subgroup separability of the finitely generated virtually abelian tube group is proved by reduction of a finite-index free abelian subgroup modulo n. The dual-complex map kills the component group, giving the asserted trivial dual group; for K3 it also gives the trivial tube group.

For χ=2, the inequalities for all lifted components force every finite quotient to be trivial. For χ=1 with nontrivial image, the same count gives quotient degree and induced component degree exactly two. Residual finiteness, applied also to product quotients, forces the full group to be Z/2. Its induced double-cover component has χ=2,p_g=1,q=0. Two such components would violate the total p_g bound. This agrees with the complete prereading finite-cover argument and supports an independent re-proof.

## New computation and exact scope

`code/continuation_VI/cover_lattice_return_checks.py` was newly authored without reading the old computation implementations. It uses only the Python standard library, exact rational Gaussian elimination, determinant expansion, congruence reduction, divisor arithmetic and an independently implemented truncated polynomial algebra. Its saved result is `cover_lattice_return_results.json`; every assertion passed.

The program independently enumerates all nineteen degree-four cyclotomic patterns allowed by the stated parity restrictions, computes their Lefschetz averages from integer companion matrices, and obtains j∈{0,4,6,8}. Repeated-factor companions are used only to compute eigenvalue-dependent determinants, not asserted to represent semisimple geometric monodromy. It recomputes the four oriented invariant lattice signatures; every cyclic elliptic base/fibre character giving the eleven positive-Euler configurations; fifteen sample Smith-group comparisons by gcds of minors; and the return-germ leading coefficient identities for d=1,…,8. The finite samples supplement the written universal arguments and are not represented as proofs for all group presentations or analytic germs. UN.11 receives a computation event only when its own proof comparison is recorded.

## UN.5 fresh-review closure

The parent reviewer, who had not read the printed UN.5 proof, supplied a complete prereading derivation in `analysis/continuation_root/UN5_before_read.md`, followed by the full seven-step comparison in `D3_UN5_comparisons.md`. Its new `UN5_characters_fresh.py` checks all 47 surjective canonical characters, primitive CRT lifts and finite elliptic unit orders; the accompanying proof treats every multiplicity. Buchdahl p.297 and Catanese v2 pp.9,13–14 were reopened. Those three events live in `records/continuation_root_events.tsv`. Our original after-exposure targeted check remains labelled as such.
