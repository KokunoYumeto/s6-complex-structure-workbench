# Independent derivation: 02WN / night:P4.16

The target proof and prior programs remain unopened. The exact statement packet and empty cited-input supplement have been read. The following construction is independent of the printed proof. It proves every positive common multiplicity, using only the actual local-to-nearby-fibre maps.

## The compact spherical class

Let M_n be the smooth affine surface `x²-zy^n=1`. Smoothness follows because y=0 forces x=±1, where the x derivative is nonzero; at y≠0 the z derivative is nonzero. There is a finite holomorphic map of degree n

    p_n:M_n→Q,       (x,y,z)↦(x,v=y^n,z),
    Q={x²-vz=1}.

On Q take the real sphere K defined by x real in [-1,1], z=-conjugate(v), and |v|²=1-x². It is a smoothly embedded S². It is Lagrangian for the restriction of the standard Kähler form of C³: the x coordinate has only one real direction and the v,z contributions cancel. The complex structure sends its tangent bundle to its normal bundle. Comparing `(e1,e2,Je1,Je2)` with the complex orientation `(e1,Je1,e2,Je2)` changes the sign once, so the oriented normal Euler number is minus the tangent Euler number, namely -2. Thus K²=-2.

The inverse image Σ_n=p_n^-1(K) is given by x real, `z=-conjugate(y)^n`, and `|y|^(2n)=1-x²`. It is a smooth sphere: away from its two endpoints it is a circle over an interval; near each endpoint, x is the smooth real function `±sqrt(1-|y|^(2n))` and z is the displayed smooth function of y. The restriction Σ_n→K has degree n, ramified only at the two endpoints. The induced map of normal bundles is an isomorphism to the pullback normal bundle, including at those endpoints: in the source coordinates (y,z), the tangent plane of Σ_n is the y plane when n>1, while the z direction maps isomorphically to the normal quotient of the graph `z=-conjugate(v)` in Q. Therefore

    Σ_n² = n K² = -2n.

Equivalently this is the proper-degree formula for the pullback of the compactly supported Poincaré dual of K. In particular the class of this explicitly mapped sphere has nonzero self-intersection for every n≥1.

## The local embedding, including the unit and the common multiplicity

Set g=x²-zy^n. It is weighted homogeneous for positive integer weights `(n+1,2,2)` and weighted degree D=2(n+1). A local defining function for a fibre whose reduced germ is the stated one and whose common multiplicity is m has the form `F=u g^m`, with u a holomorphic unit. On a sufficiently small simply connected neighbourhood choose the holomorphic root `lambda=u^(1/(mD))`. The map

    phi(x,y,z)=(lambda(x,y,z)^(n+1)x,
                 lambda(x,y,z)^2 y,
                 lambda(x,y,z)^2 z)

has invertible derivative at the origin, since its linear part is diagonal with nonzero entries. It is a local biholomorphism and weighted homogeneity gives `(g∘phi)^m=u g^m=F`. This is the exact coordinate morphism absorbing the unit.

For a positive real ε, the weighted scaling `(x,y,z)↦(ε^(n+1)x,ε²y,ε²z)` sends g=1 to g=ε^D and shrinks the entire compact Σ_n, together with a compact normal neighbourhood, into any prescribed coordinate ball. Composing with phi^-1 embeds it in the actual fibre F=ε^(mD). All maps are holomorphic local isomorphisms on those neighbourhoods and preserve the intersection number -2n.

That actual nearby fibre is a complex two-torus. Its universal cover is C², so π2 is zero. The composite map S²→Σ_n→the nearby torus is nullhomotopic; its integral homology class is therefore zero. The self-intersection of a compact cycle is preserved by this open embedding: extension by zero of its compactly supported Poincaré dual equals the dual of its pushed-forward class. Its square in the torus must consequently be both -2n and zero, a contradiction.

This proves the exclusion for every n and m. The case n=2 is the Whitney umbrella. The proof uses only this local map into a smooth torus fibre; no Betti number of a compact total space enters.

## Fresh computation

The independently written `code/S6_SERIES_PUBLISH_II_A_group05_local_certificate.py` was run before release. Its residue-ring charts and the a=2 incidence-vector Gram calculation verify the arithmetic -2n and the nonzero determinant at the printed finite test scope. The preceding sphere and normal-bundle proof establishes the formula for every integer n. The computation receipt binds source/output hashes and its 19:48:15 UTC run. No old target code was opened.
