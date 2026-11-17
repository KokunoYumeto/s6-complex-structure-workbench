# Closure of the two-junction degree-two configuration

Status: complete proof, independent audit requested. We use P4.55–56 and P4R.19. The other component B now has at least three generic normalization branches. Its conductor exponents are unrestricted.

## 1. The cubic zero and global genus identities

Along the smooth A choose coordinates A=(x=y=0), with z on A. The actual equation lies in (x,y)^3. Its normal cubic is q3(x,y;z). A local branch of B has a parametrization (x(t),y(t),z(t)) with first nonzero normal displacement (a,b)t^q, (a,b)≠0. The generic transverse multiplicity of B is at least three, so every ambient Hessian entry of f vanishes identically along B.

The first normal-order term of the 2×2 normal Hessian along this parametrization is

    t^q Hess_{x,y}(q3(·,·;0))(a,b).

All terms from higher normal order and from varying z have larger t-order. Thus this matrix is zero. For a homogeneous binary cubic Q, Hess(Q)(a,b)=0 with (a,b)≠0 implies that its directional derivative in that direction is the zero quadratic. In coordinates making that direction the first axis, Q is therefore a cube of the other variable, or zero. P4R.19 excludes the nonzero cube. Hence q3 vanishes at every A–B junction.

For two distinct junctions p,q, the common-zero divisor of q3 has degree b≥2. Write E=N_A/Y*, degE=2, and remove these fibre factors. The residual spectral curve is Γ_H∪Γ_R of class 3ξ−bF on P(E). Here Γ_R is the degree-one section and Γ_H has normalization H. The union and adjunction formulas give exactly

    g(H)+δ(Γ_H)+Γ_H·Γ_R=5−2b.

All terms on the left are nonnegative and g(H)≥1. Thus

    b=2,  g(H)=1,  δ(Γ_H)=0,  Γ_H·Γ_R=0.             (TJ.1)

In particular the two common cubic zeros are simple, Γ_H is smooth, and its two-sheet cover is disjoint from the third spectral section.

## 2. The graph forces B into every local hypersurface branch

Let c_B count the global normalization-conductor components over B. The graph budget is c_B+1. At either junction the contribution is at least min(r_A,r'_B), where r_A≥2 and r'_B≥c_B count normalized points over its two image branches.

If c_B=2, the two contributions are at least four, exceeding the budget three. If c_B=1, any junction with at least two B preimages costs at least two, and the other at least one, exceeding the budget two. Thus both have one B preimage. Exactly the argument in P4.56 forces the path H–V–R, with one edge at each junction. At the R–V junction the local hypersurface branch containing R contains all generic B sheets of V, regardless of its finite degree. Its intersection with the H branch or branches is a length-one or length-two thickening of the smooth A curve. P4.56's exact ribbon calculation makes it smooth, while its at least three generic B preimages make it intrinsically nonnormal. This is impossible.

Consequently c_B≥3. A junction at which A belongs to every local normalization-branch support contributes at least r'_B≥c_B. The other junction contributes at least two, exceeding the budget c_B+1. The two-element support argument therefore forces B to belong to every local hypersurface branch at both junctions. This conclusion retains B-only branches; it does not assume that every branch contains A.

## 3. A junction at which H and R have distinct normalization points

The ruling descends to a morphism r_N:N→H. Its restriction to H is the identity, and the vertical curve R maps to a fixed point b0∈H. If a point of H and a point of R have the same image in N, that H point must be b0. Such coincidences, including any produced by a contracted exceptional chain, can occur over only the A value a0=image(b0).

Choose one of p,q different from a0. The H preimages and the R preimage are then distinct points of N. Different H points are already distinct because H is embedded. We work at this chosen junction and name it p. Its actual local defining function factors into the corresponding irreducible hypersurface factors and any factors containing only B.

For a factor containing A, take its first nonzero normal term over the field of meromorphic functions on A. Its coefficients have a common z-order b_i≥0 at p. A factor not containing A restricts to a nonzero holomorphic function on A, vanishing at p with positive order c_j. Gauss's lemma over the discrete valuation ring C{z} gives

    Σ b_i + Σ c_j = 1,                               (TJ.2)

because the common cubic zero is simple. Indeed primitive homogeneous normal polynomials have a nonzero product modulo z, so common coefficient orders add exactly.

If H is unramified at p, there are three A-containing factors of generic normal order one. At most one of them can have b_i>0 by (TJ.2), so at least two have nonzero linear normal terms. Their directions are distinct by (TJ.1). The implicit-function theorem makes their local intersection exactly A. They cannot both contain the B branch, contradicting Section 2. Thus H is ramified at p.

There are now two A-containing irreducible factors: F_H, of generic normal order two, and F_R, of generic normal order one. Their residual spectral directions are distinct. Formula (TJ.2) leaves precisely three alternatives.

## 4. A B-only factor uses the simple zero

In this alternative b_H=b_R=0, and there is one B-only factor whose restriction to A has order one. The factor F_R is smooth. In coordinates with F_R=X and A=(X=Y=0), the restriction of F_H to X=0 is Y² times a unit: its residual quadratic direction differs from the R direction. Therefore F_H and F_R intersect only along A. Both contain B by Section 2, a contradiction.

## 5. The quadratic H-factor uses the simple zero

Here b_H=1,b_R=0 and there is no B-only factor. Again F_R is smooth. In its coordinates X=F_R,Y,z, exact division gives

    F_H|_{X=0}=Y² h(Y,z),

where h(0,z) has a simple zero. This follows because the residual quadratic has nonzero value on the R direction, so its common factor z survives with order exactly one in that restriction. Hence h_z(0,0)≠0. Its zero curve is the extra image branch B, with generic intersection multiplicity one between F_H and F_R.

The smooth F_R factor supplies one generic normalization branch along B. Every generic branch supplied by F_H has positive intersection multiplicity with it. Thus F_H supplies at most one, and the full generic B germ has at most two branches. This contradicts P4.56.

## 6. The linear R-factor uses the simple zero

Finally b_R=1,b_H=0, and there is no B-only factor. The quadratic normal form of F_H is nonzero and has a double root. Preparation in its squared normal variable and depression preserve A and give

    F_H=unit·[Y²+X²k(X,z)].

Its spectral curve is u²+k(0,z)=0. By (TJ.1) this curve is smooth and its double cover is ramified at p. Hence k_z(0,0)≠0. The actual finite map

    {u²+k(X,z)=0}→{F_H=0},  Y=Xu,

has smooth source, is birational and is an isomorphism away from A. It is the normalization. Therefore F_H is smooth at a generic point of the distinct B curve and supplies exactly one generic B branch.

For F_R, a simple common zero of its linear normal term means that its ordinary quadratic Taylor part contains

    z·L(X,Y)+Q2(X,Y),

with L≠0, and no z² term because F_R vanishes identically on A. Its ambient Hessian has rank at least two. A rank-three Hessian gives an isolated critical point. With rank two, the holomorphic Morse lemma with one parameter gives the exact equation U²+V²+h(W). A nonisolated critical curve forces h'≡0, and then, because the factor vanishes at the point, h=0. The equation factors as (U+iV)(U−iV), contradicting the local irreducibility of F_R. Thus F_R has at most isolated singularities and is smooth at a generic B point. It supplies one generic B branch as well.

The full B germ again has only two generic normalization branches, a contradiction. All alternatives in (TJ.2) are excluded. Therefore the two-distinct-junction image configuration cannot occur.

The remaining configuration before the separate three-point proof is a sole point with A and the two local branches of B. No assertion about that configuration is made by this note.
