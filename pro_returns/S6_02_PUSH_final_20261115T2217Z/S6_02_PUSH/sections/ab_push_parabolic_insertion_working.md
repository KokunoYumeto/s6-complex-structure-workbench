# Parabolic Kato insertion: retained constructive working note

2026-11-15, 17:37 UTC. **Unintegrated working note.** The explicit auxiliary compact family and its elliptic-axis calculations are developed below. Root and boundary_d have received the formulas; boundary_d has independently checked the normal factors, theta/Picard calculation, and failure of the marked exceptional divisor to extend. The complete attachment to the prescribed S6 family, a third central component, proper global gluing, and smoothing remain **unconstructed**. No numerical S6 invariant is inferred from this note.

## 1. What ordinary retained blow-ups cannot do

Let C* be the good-reduction punctured elliptic interface of B.4.8, with normal L_m of degree zero and nonzero mixed winding m. If a modification on one branch consists of point blow-ups on this interface, the strict transform is again the same elliptic curve and

`N_new = L_m ⊗ O_C(−D_exc)`.

Here D_exc is the **weighted total exceptional correction**, namely the sum of the restrictions of the total transforms of the exceptional divisors at every step. For n successive infinitely-near blow-ups on the strict elliptic curve at one point p it is n[p], although the reduced exceptional locus meets the final strict transform only once.

If both N_new and this Cartier correction extend on a proper semistable completion of C*, then their tensor product extends L_m, contradicting B.4.8. This remains true after arbitrary finite base changes. Negative degree and a drifting translation cannot remove the obstruction while retaining that correction divisor. A different operation must lose its Cartier extension.

## 2. Explicit Kato data

Fix n≥1, holomorphic units a(s), κ(s) on a small disc, with 0<|a(s)|<1. Initially one can take both constant. Let B_R⊂C² be a small ball. Blow up n times successively at the intersection of the newest exceptional curve with the strict transform of the axis x=0. In the last chart the composite map is

`π_n(z,w)=(z w^n,w)`.

Define embeddings into this chart by

`σ_s(z,w)=(κ(s) z, a(s)w+(1−a(s))s)`.

These are holomorphic embeddings because a and κ are units. They can be chosen on a neighborhood of the closed ball with image compactly contained in the modified ball, uniformly for small s. Indeed choose A<ρ<1 with |a|≤A and K≥|κ|. Shrink the parameter disc so that |a w+(1−a)s|≤ρR on B_R. Then

`|π_n σ_s(z,w)|² ≤ K²R²(ρR)^(2n)+ρ²R² < R²`

after shrinking R. This proves the required compact containment without requiring κ to represent a special Picard class.

Remove σ_s(B_R) from the modified ball and identify the outer and inner collars by σ_s∘π_n. The outer collar avoids the exceptional locus, so this map is a biholomorphism of collars. The same gluing in the product with the parameter disc is holomorphic. Uniformly disjoint collars give a Hausdorff smooth threefold; every fibre has a compact fundamental region, uniformly over compact parameter subsets. The projection is therefore a proper holomorphic submersion. This is the standard Kato annulus construction, with explicit moving embedding; see Istrati–Otiman–Pontecorvo–Ruggiero (2022), §2, printed1351–1353. It is established machinery, not a novelty assertion.

The contracted map f_s=π_nσ_s has the fixed point (0,s). In coordinates v=w−s it is

`f_s(x,v)=(κ(s) x(a(s)v+s)^n, a(s)v)`.

For s=0 this is the parabolic monomial germ with matrix [[1,n],[0,1]]. The indicated n-fold modification is exactly the one in Istrati et al. (2022), Example9.10. The central surface is a parabolic Inoue surface; its elliptic curve has normal degree −n and is disjoint from its rational cycle. Its fundamental group is Z and its second Betti number is n. These are auxiliary surface data, not the topology of a proposed S6 centre.

## 3. Exact elliptic marking and full tubular line

The strict axis is preserved by gluing. In the coordinate v=w−s its deck map is v↦a(s)v, so it extends as the smooth proper elliptic family

`E_s=C*/a(s)^Z`.

Choose a fixed fundamental annulus avoiding v=0, then take |s| small enough that both v+s and a(s)v+s are nonzero there. There are two useful normal frames, which must not be confused:

* in the literal last blow-up chart, σ_sπ_n gives normal factor `g_z(v)=κ(v+s)^n`;
* in the blowdown normal coordinate `x=z(v+s)^n`, it gives `g_x(v)=κ(av+s)^n`.

The two differ by the nonzero gauge x=(v+s)^n z on this annulus. Both extend over s=0. The central blowdown-frame factor is κa^n v^n; the degree of this line on E_a is −n (Istrati et al., Proposition5.6 gives precisely the factor λ v^n and Chern class −n).

There is an explicit regular gauge. On the fixed annulus set

`H_s(v)=∏_{j≥0}(1+a(s)^j s/v)^n`.

It converges locally uniformly in (v,s), is nonzero for sufficiently small |s|, and satisfies

`H_s(av)/H_s(v)=(1+s/(av))^n`.

Replacing x by x/H_s(v) changes g_x to κa^n v^n. Thus for constant a,κ the normal line is the constant family of a fixed degree−n line; for varying units it is the evident holomorphic family of such lines. The gluing is linear in the normal coordinate, so it describes an actual tubular line neighbourhood, not just its first infinitesimal normal bundle.

## 4. Exact generic Hopf blowdown

For fixed s≠0 define the entire function of v

`G_s(v)=∏_{j≥1}(1+a(s)^j v/s)^n`.

The product converges locally uniformly on C_v and obeys

`G_s(av)=G_s(v)/(1+av/s)^n`.

Consequently the holomorphic map

`Ψ_s(x,v)=(xG_s(v),v)`

satisfies `Ψ_s f_s = diag(κs^n,a) Ψ_s`. Composing Ψ_s with π_n on a Kato fundamental region and using this identity gives a holomorphic map from the compact fibre to the diagonal Hopf surface

`H_(κs^n,a)=(C²\{0})/〈(X,V)↦(κs^n X,aV)〉`.

The origin of this target is excluded: its preimage would be the attracting fixed point (0,s), which lies inside the removed embedded ball. The only contracted axis orbit is [v=−s]. The zeros of G_s are v=−s/a^j, j≥1, all in that orbit; π_n itself contracts its exceptional locus at v=−s. Near v=−s, G_s is nonzero (its factors are 1−a^j), so the local map is precisely π_n followed by a holomorphic coordinate unit. Thus the map is n successive blow-ups at that point and the indicated infinitely-near strict-axis points. This paragraph's global quotient/blowdown realization is the current additional referee target; the functional equation and local model are exact.

In particular the original Hopf axis has normal L_(κs^n), while the strict transform has

`N_s = L_(κs^n) ⊗ O_E(−n[−s])`.

This agrees with the preceding annulus calculation. With θ_a(av)=−v^−1θ_a(v), the bundle O([p]) has factor −p/v. At p=−s the displayed tensor product therefore has factor κv^n, equivalent to κa^n v^n by the gauge v^n. Boundary_d checked this Picard calculation independently.

## 5. The exceptional correction really does not extend

The effective degree-n divisor n[−s] on E_a has no limit in Sym^n(E_a). For constant a choose inequivalent classes [v_1] and [v_2] and sequences s_j=−a^j v_i→0. The divisors along the two sequences are constantly n[v_i], giving different limits. More invariantly, the Abel–Jacobi image of n[−s] has monodromy n times a primitive lattice cycle; a section extending across a disc would have zero winding. The latter proof also covers varying a(s) and every finite base change.

Adding a vertical E×{0} component cannot produce a Cartier closure: remove that vertical component, and the remaining proper degree-n horizontal divisor would be finite over the disc and yield a continuous Sym^n limit. Thus the positive normal extension does not contradict B.4.8 or §1. The normal was changed by a divisor whose Cartier extension is genuinely lost.

## 6. Elliptic complete-intersection attachment: exact first-order data

Let E be a smooth (2,2) complete intersection in P3. Put L=O_E(2), of degree8. Then N_(E/P3)=L⊕L, and the exceptional divisor D of Bl_E P3 is E×P1, with

`N_(D/Bl_E P3)=L ⊠ O_P1(−1)`

in the lines convention for projectivization. In particular the E-degree +8 must be retained; merely quoting the ruling degree−1 loses essential data.

For an unmodified Hopf-product cap, its divisor E×P1 has normal M⊠O, where deg M=0. The required triple-divisor line would be `(L⊗M)^−1 ⊠ O(1)`, whose E-degree is−8. It has no nonzero section, by the product formula for H0. Hence this bare cap cannot match even after an arbitrary effective triple divisor is supplied.

A parabolic Inoue cap with n=8 instead has an elliptic axis normal N of degree−8. Its parameter κ changes the flat factor, so, after fixing the elliptic identification, N can be chosen isomorphic to L^−1. Any class admits a sufficiently small unit representative modulo a^Z if needed for an embedding. The product cap S8×P1 then has normal L^−1⊠O on D, and the triple section E×{p} supplies O⊠O(1). The product of the two normal lines and that triple-divisor line is exactly trivial.

This is **first-order normal matching only**. A third component must meet the two existing components along surfaces whose common curve is E, and all its own normal and higher-overlap data must agree. For example a quadric containing E becomes a surface Q≅P1×P1 in Bl_E P3 with trivial normal (since O_Q(2) is cancelled by E of bidegree(2,2)); it meets D in a section. On the parabolic product side the corresponding surface is S8×{p}, also with trivial normal. Producing a compact third threefold with these two divisors and the required neighborhoods is still missing. D-semistability alone does not supply that threefold or a smoothing.

If the original toric component has other conductor divisors meeting E, their induced vertical triple fibres on D must also be included. Positive E-degree contributions must be balanced explicitly; they cannot be discarded. Likewise the q=s^n ramification used in the auxiliary Kato family is not automatically a permitted global change of the original base. These are current construction gaps.

## 7. Primary-source audit

Opened the published primary PDF `https://www.numdam.org/item/JEP_2022__9__1347_0.pdf` and the coauthor PDF `https://webusers.imj-prg.fr/~matteo.ruggiero/pub/pdf/istrati-otiman-pontecorvo-torickato.pdf`. Read §2 (Kato gluing), Proposition5.6 (negative line multiplier), Example9.10 (the exact parabolic matrix). Existing bibliography key IstratiEtAl2022Root is reused. An initial guessed JEP .206 PDF link returned403; the correct DOI is10.5802/jep.208 and the published PDF was then opened.

Opened Nakamura's original *On surfaces of class VII0 with curves,II*, Tohoku Math.J.42(1990),475–516, `https://www.jstage.jst.go.jp/article/tmj1949/42/4/42_4_475/_pdf`. Its general Hopf-deformation statement is contextual only; the marked family here is given by explicit formulas.

Reopened Fujimoto1988 original journal scan, `https://scispace.com/pdf/logarithmic-transformations-on-elliptic-fiber-spaces-1uinrvp8jj.pdf`, §3, Examples3.1/3.4. They concern elliptic fibrations; no extension to the original generic simple two-tori is inferred. Root owns that bibliography entry and comparison discussion.
