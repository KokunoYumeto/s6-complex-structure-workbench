# Independent derivation: 01F7 / cdp:st:C.3.12

Checker: restore_build. This document is written before opening the target proof or any old target check. The exact statement/input packet is `agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_01F7_statement_inputs.tex`. The primary-source reading and image hashes are bound in `S6_SERIES_PUBLISH_II_01F7_primary_inputs_receipt_v2.json`, SHA256 `4d731595c22eaea48f6b0af9552817f8b189a7fba074dbfd1c7ae0900c8cafdf`.

The target has two claims. The stronger claim concerns a proper holomorphic map from a compact connected complex manifold to a compact curve whose fibres outside finitely many points are Inoue surfaces. It asserts a real degree-one cohomology class nonzero on every regular fibre. The first claim excludes a very general Inoue fibre under the already checked, explicitly smooth scope of C.3.1. I establish the stronger claim first, then justify the passage from very general to every fibre of the regular locus. I use no forward-dependent exclusion from C.3.1's final list.

## 1. Primary inputs and their precise scope

Inoue's original journal paper is the actual Göttingen digitization of Inventiones Mathematicae 24 (1974), 269–310. The extracted article has SHA256 `ffad28a6f47531583213403f7df559d3f905db6a0c5409ff44d8df605f21fb7d`. I viewed the complete pages containing Proposition 2 (p.274), Proposition 4 and its proof (pp.278–279), and Proposition 5 (p.280), as well as the relevant group formulas on pp.276 and279. Proposition 2 gives rigidity of the first type; Proposition 5 gives rigidity of the third type. Proposition 4 gives a locally complete analytic deformation family for the second type, with fixed discrete parameters and variable complex parameter t.

All three types have universal cover U=H×C, where H is the upper half-plane. The first-coordinate actions of their deck generators are w↦αw for a distinguished generator g0, and w↦w+a_i or w↦w for the remaining generators, with α>1 and a_i real. For the second type the variable deformation parameter enters only the second coordinate: g0(w,z)=(αw,z+t). The other two types are locally constant families. These facts give local holomorphic families of universal-cover charts, not merely individual-fibre descriptions.

Khaled–Teleman, arXiv:2406.15158v4, 13 July 2026, PDF SHA256 `a02fcbbe234e2065d796e183c2a62dbfe895f63c120492dc7a57b2c36001af86`, Theorem 4.1 and its entire proof on p.18 show that every biholomorphism of Inoue surfaces lifts to an affine automorphism of U. Remark 1.1, p.5, gives the precise form

\[
(w,z)\longmapsto (a w+b,\lambda w+\nu z+\zeta),
\qquad a>0,\quad b\in\mathbb R,\quad \nu\ne0.
\]

The form of the first coordinate can also be checked directly: an affine first coordinate with a nonzero z coefficient would take values of arbitrary imaginary part as z ranges over C. An affine automorphism of H has positive real slope and real translation. The inverse has first coordinate a^{-1}(w-b), so it also preserves H.

For the later propagation step I use the compact-surface classification input recorded in Biswas–Mj–Seshadri, author PDF dated 27 October 2011, Theorem 3.2 (p.16), and the initial elliptic-fibration structure discussion in §3.3 (pp.17–18). Its SHA256 is `1bfc9f90846000474ae1c6377850513e2ce85a74942b5f8fcc48e0a08a6addb6`. These inputs classify an odd-first-Betti surface as elliptic or class VII and supply the elliptic fundamental-group sequence. I do not use their Theorem 3.8 or its separate three-manifold quotient argument. Khaled–Teleman's introduction, pinned-v4 p.2, records the class-VII, b2=0 classification into Hopf and Inoue surfaces, with the precise Bogomolov–Teleman/Kodaira references. All classifications below are connected to the actual fibre by explicit topological/group maps.

## 2. Holomorphic transverse charts on the regular part

Write B*=B\S and Y*=f^{-1}(B*). The regular fibres in the stronger claim are smooth Inoue surfaces, so the map over B* is a proper holomorphic submersion. Take small simply connected base discs V. By the local completeness and rigidity statements above, the family over a smaller such disc is isomorphic to a pullback of the explicit second-type family, or to the constant first/third-type family. In each case its local universal-cover model is U×V with the displayed deck transformations, whose first-coordinate coefficients are independent of the base variable.

Compare two such descriptions over a connected component of a sufficiently small overlap. Lift the family isomorphism locally to the universal covers. A lift exists after choosing one lift of a point; covering-space path lifting extends it over a simply connected overlap, and the covering maps are local biholomorphisms, so the lift is holomorphic. On each fibre its first coordinate has the form a(s)w+b(s) by Theorem 4.1. The coefficients are holomorphic in s: they can be obtained by evaluating the first coordinate at two fixed distinct w-values. Since a(s) is positive real and b(s) real, the open mapping theorem makes both constant on the connected overlap. The z-coordinate may depend holomorphically on s; no constancy of that coordinate or of the family itself is asserted.

Consequently Y* has a transverse atlas of holomorphic functions w_j:O_j→H with overlap identities

\[
w_j=a_{jk}w_k+b_{jk},\qquad a_{jk}>0,\quad b_{jk}\in\mathbb R,
\]

where the coefficients are locally constant. On triple overlaps these are genuine affine cocycle identities, because the coordinate functions agree on an open subset of H. This is the precise transport from the three individual quotient models to the total family.

Analytically continue one chart along paths in Y*. On the universal cover this produces a holomorphic developing map D:\widetilde{Y*}→H and a holonomy homomorphism

\[
\rho:\pi_1(Y*)\longrightarrow\operatorname{Aff}^{+}(\mathbb R),
\qquad D(\gamma x)=a_\gamma D(x)+b_\gamma.
\]

For a direct cocycle construction, transport the initial chart using the inverse overlap transformations along a chain of chart domains. Triple-overlap identities make the result unchanged by subdivisions; a homotopy gives the same result by subdivision into small squares. Thus the construction is single valued on the universal cover. Every affine transformation used in the continuation maps H bijectively to H, so the developing map retains that range. No completeness assertion about this transverse structure is needed.

The slope homomorphism gives an additive character

\[
\chi(\gamma)=\log a_\gamma\in\mathbb R.
\]

Changing the initial chart conjugates holonomy by w↦cw+d. Its conjugated slope is still a_γ, since c a_γ c^{-1}=a_γ. Therefore χ does not depend on that choice. On any fibre the quotient charts identify its restricted holonomy with the explicit deck action, up to this conjugation. Its distinguished deck generator has χ(g0)=logα≠0. The restriction is therefore nonzero on each regular fibre, without an unproved assertion that the entire fibre fundamental group injects into π1(Y*).

## 3. The exact punctured-disc estimate

Let F:H→H be a holomorphic map satisfying

\[
F(\tau+1)=aF(\tau)+b,\qquad a>0,\quad b\in\mathbb R.
\]

The Poincaré distance on H satisfies

\[
\cosh d_H(z,z')=1+\frac{|z-z'|^2}{2\Im z\Im z'}.
\]

For z=x+iv and z'=az+b this gives the exact estimate

\[
\begin{aligned}
\cosh d_H(z,az+b)
&=1+\frac{((1-a)x-b)^2+(1-a)^2v^2}{2av^2}\\
&\ge 1+\frac{(1-a)^2}{2a}
=\frac{a+a^{-1}}2
=\cosh|\log a|.
\end{aligned}
\]

Thus d_H(z,az+b)≥|log a|. Schwarz–Pick applied to F gives

\[
|\log a|\le d_H(F(iy),F(iy+1))
\le d_H(iy,iy+1),\qquad
\cosh d_H(iy,iy+1)=1+\frac1{2y^2}.
\]

Letting y tend to infinity proves a=1. The calculation allows arbitrary real b and does not assert that the complete affine holonomy is trivial. It proves exactly the vanishing of the logarithmic slope needed below.

## 4. Actual divisor meridians, including multiplicities

The complement E=Y\Y* is the reduced support of finitely many fibre divisors. At a smooth point of an irreducible component, away from every other component, choose a small holomorphic transverse disc j:Δ→Y meeting E only at its centre. Its punctured disc lies in Y*. Lift the universal covering map τ↦exp(2πiτ) of Δ* and compose with D. This gives F:H→H satisfying the equation of §3 with (a,b) the affine holonomy of the actual transverse meridian in Y*. Therefore χ vanishes on that meridian.

This construction takes place in the total space. A fibre component of multiplicity m has a transverse base function u(z)z^m with u(0)≠0; the meridian in the total space then maps to m turns in the base. I have not replaced it by one base loop, divided a loop by m, or assumed a reduced fibre. The estimate applies directly to j and so kills the actual meridian for every positive multiplicity. Singular points of E need no transverse-disc argument: they form a subset of complex codimension at least two in the smooth manifold Y and are avoided by the general-position argument in the next section.

## 5. Descent to the compact total space

The map π1(Y*)→π1(Y) is surjective. A loop in the real manifold Y can be perturbed off a real-codimension-two complex divisor. Its kernel is the normal subgroup generated by the meridians above. Indeed, take a nullhomotopy disc in Y for a loop in Y*. Perturb it relative to its boundary to miss the singular locus of E and to be transverse to the smooth divisor strata. The singular locus has real codimension at least four, so a two-dimensional disc can avoid it. There are finitely many transverse intersections with the smooth strata. Removing small disjoint discs around those points gives a punctured disc mapping to Y*. Its oriented boundary relation expresses the original loop as a product of conjugates of the corresponding meridians and their inverses. Conversely every such meridian bounds its original transverse disc in Y. This proves the exact kernel statement.

Since χ kills all these generators and is invariant under conjugation, it factors uniquely through

\[
\overline\chi:\pi_1(Y)\longrightarrow\mathbb R.
\]

Abelianization and the universal-coefficient isomorphism give

\[
\operatorname{Hom}(\pi_1(Y),\mathbb R)
=\operatorname{Hom}(H_1(Y;\mathbb Z),\mathbb R)
\simeq H^1(Y;\mathbb R).
\]

Naturality of this isomorphism identifies restriction of the resulting cohomology class to a fibre with the already calculated restricted character. That restriction takes the nonzero value logα on g0. Hence the class is nonzero and b1(Y)>0. This establishes the full stronger statement, with arbitrary omitted fibre singularities and multiplicities, at exactly its smooth-total-space hypothesis.

## 6. From a very general Inoue fibre to the regular-locus hypothesis

Under the intended smooth C.3.1 hypotheses, the critical-value set is finite by properness and the analytic discriminant over a curve. Its complement is connected. Ehresmann's theorem identifies the smooth fibres along any path by diffeomorphisms; in particular their fundamental groups, b1 and b2 agree. If a very general fibre is Inoue, every regular fibre has b1=1,b2=0 and the same fundamental group G as an Inoue surface. Each regular fibre is minimal: an exceptional curve of self-intersection −1 would give a nonzero rational degree-two class, contradicting b2=0.

Here is an explicit group check of the remaining classification possibilities. The Inoue universal cover H×C is contractible. Thus G is a torsion-free Poincaré duality group of real dimension four, and every finite-index subgroup has cohomological dimension four. It is solvable. It is not virtually nilpotent: for the first type, the group is Z^3⋊_M Z, where M has real eigenvalue α>1. For the second/third types, quotient by the normal subgroup generated by the central-direction generator g3 gives the actual quotient map onto Z^2⋊_N Z, where N has an eigenvalue α>1. The deck-generator relations and unique normal forms establish these exact semidirect products. In any finite-index subgroup of such a semidirect product, the intersection with Z^r is a full-rank lattice L and some element above k∈Z acts on L by M^k or N^k. Iterated commutation with that element acts by (M^k−I)^j or (N^k−I)^j. Nilpotence would make one such power zero on L⊗Q, whereas its eigenvalue (α^k−1)^j is nonzero. A quotient of a nilpotent group is nilpotent, so this also excludes virtual nilpotence of each Inoue group itself.

For an elliptic regular fibre with b1=1, the elliptic structure input gives the exact sequence from its elliptic fibre group to G and then onto the base-orbifold group. A singular elliptic fibre would force the rational cohomological dimension to be at most three, as in the initial §3.3 structure discussion; that contradicts the dimension-four Poincaré duality group just identified. With smooth, possibly multiple elliptic fibres, the fibre image is abelian of rank at most two. The base-orbifold quotient is solvable because G is. A hyperbolic orbifold group has a finite-index surface group of genus at least two, which has a nonabelian free quotient and is not solvable, so that case is excluded. A finite orbifold group would make G virtually abelian of rank at most two, again contradicting dimension four. The remaining Euclidean orbifold has a finite cover by a torus. Pull back the elliptic family by that orbifold cover. It has no multiple fibres; its j-map is holomorphic on a compact curve with values in C and is constant. Its fibrewise linear automorphism group is finite, so a further finite base cover kills that action. The resulting bundle has translation structure group and therefore the exact central extension

\[
1\longrightarrow\mathbb Z^2\longrightarrow G'
\longrightarrow\mathbb Z^2\longrightarrow1.
\]

The fibre injection follows also from the homotopy sequence because π2 of the base torus is zero. The commutator subgroup of G' lies in the central fibre subgroup, so G' is nilpotent of class at most two. This contradicts the explicit non-virtual-nilpotence calculation above. Thus the regular fibre cannot be elliptic.

The odd-b1 classification now places it in class VII. At b2=0 the classification input gives Hopf or Inoue. A Hopf surface group is virtually infinite cyclic, which has cohomological dimension one; it cannot be the identified Inoue group of dimension four. Hence every regular fibre is Inoue. This proves the exact hypothesis needed for §§2–5, without assuming a very-general statement automatically extends to all regular fibres. Their conclusion b1(Y)>0 contradicts C.3.1's b1(Y)=0.

## 7. Result and exposure declaration

Both assertions of the supplied 01F7 statement have now been derived. The maps used are explicit: quotient-family charts to a transverse affine cocycle; the cocycle to developing map/holonomy; slope to an additive character; actual transverse discs to the Schwarz–Pick estimate; the meridian-normal-closure quotient to π1(Y); and abelianization/UCT to H1-cohomology. The regular-locus propagation is checked through exact fibre diffeomorphisms and group quotients rather than an unproved identification of surface types.

No target proof or historical target computation was read while producing this derivation. No numerical experiment is needed: the distance estimate and iterated-commutator formula are exact identities. Any later comparison, edit, or extra computation will be recorded after this freeze and cannot change its time or content.
