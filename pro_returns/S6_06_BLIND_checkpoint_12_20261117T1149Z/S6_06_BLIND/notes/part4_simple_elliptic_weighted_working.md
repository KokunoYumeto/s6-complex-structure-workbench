# Reduced weighted leading obstructions at a simple elliptic point

The exact valuation-coordinate lemma is being written independently by blind_control. This file gives the complete three reduced weighted-hypersurface calculations and the explicit original-coordinate comparison. No assertion about the final remaining global case is marked complete before that lemma is audited.

## A. The actual coordinate comparison

Let r,s_old,v_old be the strict-transform coordinates in the ambient blowup chart, so the original coordinates are (x_old,y_old,z)=(r s_old,r v_old,r), after an ordinary linear change centering the exceptional point. The actual original equation is r³f1.

The independently derived section-ring computation gives d=1,2,3, where −d is the self-intersection of the sole elliptic exceptional curve, and graded generators as follows:

- d=3: weights(1,1,1), relation degree3, a smooth projective elliptic cubic.
- d=2: weights(1,1,2), relation degree4, a smooth elliptic weighted curve.
- d=1: weights(1,2,3), relation degree6, a smooth elliptic weighted curve.

The given r has valuation one and is retained exactly. The other coordinates may be chosen by linear changes in (r,s_old,v_old), with only a possible subtraction of αr² from the third coordinate in the d=1 case. Here is the finite-degree justification. Let I_j be the exceptional valuation ideals. I1=m and m²⊂I2. For d=2, choose linear r,s mapping to a basis of H0(L). A remaining linear coordinate v maps to zero there. Since I2/I3=H0(L²) has dimension4 while Sym²H0(L) has dimension3, the Taylor expansion modulo m³ forces v to have valuation exactly2 and an initial class independent of those products. For d=1, r spans H0(L); I2/I3 has dimension2, so one linear complement s has leading class independent of r². Change the last linear complement v by a multiple of s and then αr² to obtain valuation at least3. The dimension3 of I3/I4, together with the Taylor expansion modulo m⁴, forces valuation exactly3 and a leading class independent of r³,rs.

These changes descend to the original ambient germ. Multiplying the new s,v by r gives new x,y which are linear combinations of x_old,y_old plus multiples of z²,z³. The 2×2 linear block is invertible because (r,s,v) are coordinates retaining r. Thus (x,y,z) is an actual holomorphic coordinate system at the original point, by the inverse function theorem.

The resulting original weights and degrees are respectively

(2,2,1), degree6; (2,3,1), degree7; (3,4,1), degree9.

For a strict-transform monomial r^a s^b v^c, multiplication by r³ gives x^b y^c z^(3+a−b−c). Its original weighted degree is three plus its strict-transform weighted degree. Analyticity of the original equation guarantees that any negative-power coefficient vanishes. Consequently its actual weighted leading polynomial is a polynomial of the stated degree. Its normalized projective component contains the same elliptic residue-field curve as the section ring: on z≠0, the ratios x/z^(1+w_s), y/z^(1+w_v) identify it with the strict-transform elliptic relation on r≠0. This is an explicit birational map of curves, and hence an isomorphism of their smooth normalizations.

Anisotropic scaling with these weights and the compact-cycle comparison of P4.52 therefore transports every pairing of the weighted leading fibre into the actual torus fibre. Such pairings must vanish by P4.51.

## B. Degree six, weights(2,2,1)

In this case the leading polynomial is exactly

P6(x,y,z)=G3(x,y,z²),

where G3(X,Y,Z) is a smooth homogeneous cubic. The map {P6=1}→{G3=1}, (x,y,z)↦(x,y,z²), is a finite double cover branched over

B={G3(x,y,0)=1}.

The homogeneous cubic fibre has Euler number9, since it is an unramified threefold cover of P² minus a smooth elliptic cubic, whose Euler number is3. Let r be the number of distinct zeros of the binary cubic G3(x,y,0) on P¹. Since the cubic curve is smooth, that binary cubic is nonzero and r∈{1,2,3}. Its level-one fibre is a threefold cover of P¹ minus those r points, so χ(B)=3(2−r). Additivity for the branched double cover gives

χ({P6=1})=18−χ(B)=12+3r.

The weighted monodromy has order6. Its only nonidentity element with a fixed set is its cube, which sends z to−z and fixes x,y; its fixed set is precisely B. The other four nonidentity elements have no fixed points on the level-one fibre. Choose an invariant semialgebraic compact core large enough for both the fibre and B. The finite-order Lefschetz character of H0−H1+H2 is χ(F) at the identity, χ(B) at the cube, and zero elsewhere. Its trivial-character multiplicity is

(χ(F)+χ(B))/6=18/6=3.

Since H0 has only the trivial character, the sum of nontrivial H2 multiplicities is at least χ(F)−3=9+3r≥12.

All nonzero critical orbits of P6 lie on z=0 at tangencies of the cubic with Z=0. If the tangency orders are e_i, then sum e_i=3 and the exact transverse germ is u^(e_i)+z², up to units and holomorphic coordinates. Smoothness of G3 makes the Z derivative a unit at every tangency, which proves this identification. Hence the transverse Milnor-number sum is

M=sum(e_i−1)=3−r<=2.

The variation inequality(4.52b) contradicts the lower bound at least12. Therefore this weighted leading fibre has a nonzero intersection form and cannot occur in the actual degeneration.

The polynomial is reduced: a nonreduced factor would produce a codimension-one critical set, while the displayed derivative calculation gives only the finitely many critical orbits just listed. This also justifies connectedness of its Milnor fibre.

## C. Two elementary weighted-curve facts

For P(a,b,c)=Proj C[u,v,w] and a reduced equation of weighted degree e, the exact graded-module sequence sheafifies to

0→O_P(−e)→O_P→O_D→0.

The three affine charts give the Čech complex. Its middle cohomology vanishes, and its top cohomology has basis the Laurent monomials u^(−i)v^(−j)w^(−k), i,j,k≥1, of total weighted degree−e. Thus

h1(O_D)= number of monomials of nonnegative weighted degree e−(a+b+c).

Also H0(O_D)=C. In particular the arithmetic genus is0 below degree a+b+c, and is1 in degree a+b+c and degree a+b+c+1 when there is exactly one variable of weight one.

We also need a quotient-vertex observation. At a cyclic quotient point of prime order p=2 or3 with no invariant linear ambient coordinate, a smooth coarse curve has a smooth plane pullback. Indeed its normalized branches form one group orbit. If there is a single singular branch of multiplicity m≥2, the normalization action is faithful of order p, and every invariant ambient function has order at least2m>p, whereas a regular quotient curve requires a function of normalization order p. If there are p branches permuted transitively, their stabilizer is trivial, and every invariant function has order at least2 on a normalized branch, whereas regularity requires order one. Both are impossible. A single remaining branch is smooth. Its reduced defining equation has the character of a nonzero linear ambient coordinate. Thus a smooth coarse curve with a defining semi-invariant of incompatible character cannot pass through that vertex.

All assertions use analytic invariant rings: functions on the quotient curve lift to invariant ambient functions by averaging, because the finite-group invariants functor is exact in characteristic zero.

## D. Degree seven, weights(1,2,3)

Let D be the weighted projective curve of a degree-seven polynomial with an elliptic normalization component. The Čech formula gives arithmetic genus zero for every component of degree at most5 and arithmetic genus one in degrees6 and7. Thus the elliptic component has degree6 or7. Its multiplicity is one, and there is at most one additional degree-one factor. The polynomial is reduced.

If its degree is7, D is irreducible, has arithmetic genus one and normalization genus one, so its total delta invariant is zero: it is a smooth coarse elliptic curve. At the vertices of orders2 and3, the preceding quotient observation gives a smooth plane lift. Away from those vertices the ambient space is smooth. Hence the affine cone has no nonzero critical orbit, and M=0.

If its degree is6, write D=E∪{z=0}, with z the weight-one coordinate. The curve E is again smooth coarse elliptic. It cannot pass through either quotient vertex: its defining degree-six equation has trivial character there, while both local coordinate characters are nontrivial, so a smooth lift would have an impossible invariant linear equation. Therefore the intersections with z=0 occur in the smooth part of the weighted plane. The genus normalization formula for D gives total delta one. Consequently E and the rational line have one transverse intersection, and M=1; there are no other critical orbits.

The weighted plane has Euler number3, from its affine-cell stratification. In the two cases e(D)=0 or1, so its complement has Euler number3 or2. All nontrivial stabilizers of the weighted C* action are at the two quotient vertices, and both vertices lie in D (degree7 is divisible by neither2 nor3). Thus {P7=1} is an unramified sevenfold cover of the complement, and every nonidentity μ7 monodromy element acts freely. The character formula gives nontrivial H2 rank at least18 or12, whereas zero form would give rank at most M=0 or1. This is impossible.

## E. Degree nine, weights(1,3,4)

The same Čech formula gives arithmetic genus zero below degree8 and arithmetic genus one in degrees8 and9. An elliptic component of a reduced weighted degree-nine polynomial must therefore have degree8 or9, and multiplicity one. A possible residual factor has degree at most one.

A degree-eight elliptic curve is impossible. It necessarily passes through the weight-three vertex, since8 is not divisible by3. In its plane chart the two coordinates have characters1,1 modulo3, while its equation has character2. The prime-order quotient observation forces a smooth lift, whose equation must have character1, a contradiction.

Thus the entire degree-nine curve D is irreducible and smooth coarse elliptic. It does not meet the weight-three vertex: there its equation has character0, incompatible with a smooth plane lift. At the weight-four vertex the plane characters are1,3 and the equation has character1. We check smoothness of its lift directly. The transitive orbit of normalized branches has size1,2,or4.

For four branches the stabilizer is trivial, while every invariant maximal-ideal function has order at least2 on a branch, contradicting a smooth quotient. For two branches the stabilizer has order2. A singular branch again gives invariant orders at least4>2. Two smooth branches would have a quadratic leading equation, but the quadratic characters of the ambient action are only0 and2, never1. This is impossible. For one branch the normalization action is faithful of order4. Both ambient coordinate orders are odd, because their characters are1 and3. A singular branch therefore has multiplicity at least3; all invariant functions have order at least6>4, again contradicting smoothness of the quotient. The only remaining lift is a smooth branch.

The degree-nine cone is consequently smooth away from its vertex. It is singular at the vertex, since none of its variables has weight nine. Its hypersurface singularity is isolated. The isolated-point Morse transport in P4.52 gives a nonzero-square spherical class in its Milnor fibre, contrary to the zero pairing transported from the actual torus.

## F. Exact scope after combining with the valuation lemma

These three weighted calculations eliminate all three section-ring types once the independently written lemma identifies the actual strict-transform associated graded ring and proves that r remains a valuation-one coordinate. The original-coordinate map in A is explicit and holomorphic. The only remaining global ruled sector would then have a noncontracted H, whose image is generic D4 by P4R.18; no transverse restriction on its other conductor component is introduced.
