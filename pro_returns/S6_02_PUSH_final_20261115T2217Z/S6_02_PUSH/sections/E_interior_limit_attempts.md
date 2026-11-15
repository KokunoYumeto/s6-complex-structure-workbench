# Interior smooth limits after E.2.10: exact reductions and open steps

Working note, 15 November 2026. This file is not an additional proved result registry and is not input in the paper. E.2.9–E.2.12 are integrated separately. The former extra-central-critical-value gap is now resolved by the explicit good-Jacobian argument of E.2.11–E.2.12. The remaining objective is uniqueness of a smooth completion at an interior period, or persistence on every deformation branch through such a completion. No such conclusion is claimed here.

## 1. Setup supplied by the proved results

For a one-sided smooth specialization of fixed multiplicities (3k,4l), E.2.10 gives an actual proper flat map g:mathcal X→P1×Delta. Its central restriction is the intrinsic algebraic reduction. The line L is the actual pullback of O(1), and K_rel^A=L^D with A=12kl and D=kl−3k−4l. E.2.7 gives an interior limiting normalized period. After choosing its local logarithm, c(s) extends holomorphically to s=0.

The three punctured critical sections have intrinsically distinguished finite orders3,4 and cusp monodromy. Their closures are degree-one branches over the disc, hence define holomorphic P1-valued functions. The corresponding normalization A_s∈PGL2 is meromorphic in s. It can have a degenerate limit; interiority of c does not itself exclude that.

## 2. Cartier multiplicity preservation

Let Gamma_j be the graph of a labelled critical section in P1×Delta. The pullback g^*Gamma_j is an effective Cartier divisor on the smooth total space. On the punctured family it equals m_j Z_j, where m_1=3k and m_2=4l and Z_j is the reduced multiple-fibre family. Its irreducible closure is a prime Cartier divisor. There can be no extra component equal to X0: g0 is nonconstant, so it does not map the whole central threefold into the single point Gamma_j(0). Consequently g^*Gamma_j=m_j overline Z_j as actual divisors on the total space.

Restriction to X0 gives g0^*(p_j)=m_j(overline Z_j|X0). If the two finite critical sections collide, every coefficient of the resulting central fibre is divisible by lcm(3k,4l)=12kl. The argument allows the restricted divisor to be reducible or nonreduced; it makes no claim about its normalization or singularities.

## 3. What a degenerate target normalization would imply on regular fibres

A meromorphic PGL2 matrix with degenerate limit maps a generic fixed central target point, in the original normalized source coordinate, toward one constant point t*. For a fixed target point at which the central fibre is regular, the actual torus family extends smoothly over the parameter disc. Its degree-one integral monodromy in s is the identity. Since the period logarithm c has no winding, the calculation of E.2.7 leaves only the peripheral monodromy associated with t*.

Approach to the cusp with nonzero order is impossible: the rank-two cusp nilpotent has nonzero u→w part and no parameter shift is present to cancel it. At a finite source value, the approach order must be divisible by3 or4, respectively. After taking the corresponding local root, the reference torus family has a smooth limit. Comparison of the actual and reference integral local systems gives the same limiting marked torus. This uses separation for marked complex tori, not separation for the entire threefold moduli problem.

Thus in the collapsed-target scenario the central smooth regular torus fibres are all isomorphic. If t* is 0 or1, this is the finite root torus at c(0), an abelian surface: the finite linear automorphism has one complex eigenvalue1 and one primitive cube or fourth root, and its rational idempotent decomposition splits the torus up to isogeny into two elliptic factors. If t* is ordinary, it is the ordinary torus at (c(0),t*), which need not be abelian. An earlier shorthand incorrectly omitted this ordinary case; the integrated E.2.12 explicitly distinguishes the two. Neither case supplies a global polarization on the total central threefold.

## 4. The former extra-critical-value gap, now resolved

It is not justified to say that the central map has at most two critical values solely from the collision of the three punctured critical sections. The proper analytic critical image can also have isolated points supported at s=0. Smoothness of the total space and flatness alone do not give purity of the discriminant for arbitrary families of surfaces. A general purity assertion would need proof in this particular torus setting.

The gap has now been closed under the actual period hypotheses, without invoking a general purity theorem. Near a hypothetical extra value, E.2.12 constructs the smooth Jacobian over a bidisc from the ordinary or finite-root period model. The finite-root order divides the parameter approach order by the actual identity H1 return, and the remaining unit has a holomorphic root. The punctured bidisc is simply connected, so its actual marked period subbundle agrees with that reference Jacobian. E.2.11 then extends the torus action by Hartogs and proves smoothness at the allegedly exceptional value. Therefore the central critical values are exactly the labelled limits.

If the image is the nontrivial group generated by A1 or A2, its invariant H1 has dimension2. Alexander duality and the correct invariant-space formula give r=s+1, where r counts the components of the actual critical fibres. In the degenerate-target case E.2.12 now proves s=2 in this nontrivial-monodromy case, so one fibre has two components and the other is irreducible. If all punctured critical sections cluster together, their product has trivial monodromy; then s=1 and r=s+3=4. The count now has the needed purity justification. It does not classify the singularities or normalizations of these fibres.

## 5. Restrictions from the six-sphere and the canonical root

E.2.8, with its final companion, proves that every component of a reducible fibre has normalization outside Fujiki class C. Therefore ordinary blowups of a projective good model, which introduce rational or ruled Kähler components, do not provide the required central map on a complex S6.

The identity K_X0^A=g0^*O(D) is also stronger than merely having tori on the smooth locus. Every singular-fibre neighbourhood has torsion canonical bundle. Fujimoto's isotrivial examples below do not automatically satisfy this extra condition. In particular their components of positive Kodaira dimension cannot simply be transferred into a proposed torsion-canonical model without checking adjunction and the normal line.

There is a further exact conditional Chern calculation. If a component has a smooth normalization nu:S→X0 that is a holomorphic immersion, then

0→TS→nu^*TX0→N→0

is an exact sequence of bundles. Since c1(TX0)=c2(TX0)=0, it gives c1(N)=−c1(S) and c2(S)=c1(S)^2. For a non-Kähler surface, chi(O_S)=0, so Noether gives c1(S)^2+c2(S)=0; both Chern numbers are therefore zero. In particular an immersed class-VII normalization cannot have positive b2. The smooth-branch or normal-crossing hypotheses are essential to this immediate argument. Divisorial ramification of a normalization, cusp-type conductors, or exceptional curves in a resolution alter the differential sequence; no positivity assertion for their correction terms has been proved here.

## 6. Why ordinary good reduction does not finish the argument

Fujimoto's original 1988 journal article was independently opened, printed pp.98–99, Example3.1 Step4 and Example3.4(1):

Fujimoto, Y. (1988). Logarithmic transformations on elliptic fiber spaces. *Journal of Mathematics of Kyoto University, 28*(1), 91–110.

Primary article scan, mirror host: https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf

The punctured family in the construction is a product. Starting from a fixed elliptic product or an appropriate finite-order extension gives an abelian-surface example, while logarithmic transformations produce non-Kähler central components. Thus finite linear monodromy, constant complex period, and an available reference good model do not alone identify every proper analytic completion with that model. The example does not itself give the present six-sphere topology, the fixed canonical root, or the required component count.

The standard torus/abelian degeneration classifications examined in the searches impose Kähler, projective, or polarization-extension hypotheses. None was applied without those hypotheses. The needed comparison remains an actual theorem for this non-Kähler, torsion-canonical, marked completion, rather than a general assertion that finite monodromy gives a unique proper filling.

## 7. New-branch obstruction remains separate

The cohomology complex of the canonical pencil can have a determinant whose zeros persist under small deformations. That does not preserve a two-dimensional section space: a double kernel can split into distinct simple effective classes. The familiar loss of an elliptic Hopf pencil under nonresonant deformation illustrates the logical failure of that inference. An S6-specific argument would be required to prevent it. E.2.10 excludes common limits of two known pairs, but does not prove that every small branch at an unconstructed limit retains the two canonical-root sections.

The exact remaining tasks are therefore to control the possible one- or two-critical-value isotrivial completion, prove uniqueness for a noncollapsed interior completion, or find an invariant that survives every new deformation branch. The former central-only critical fibres have been excluded. No completion theorem or full deformation-chain separation is inferred in this note.
