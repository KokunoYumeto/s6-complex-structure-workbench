# 02Y2 / night:P4R.1 — independent derivation before target release

Checker: /root/ii_check_a, GPT-6 Astra, inherited reasoning setting, continuing publication run, 2026-11-21. This document is written while the target proof, its outline, and any historical target routine remain closed. The immutable statement packet and empty cited-input supplement are the manuscript inputs. The newly opened primary input is S. Łojasiewicz, *Triangulation of semi-analytic sets*, Annali della Scuola Normale Superiore di Pisa, ser. 3, 18(4) (1964), 449–474, Theorem 2 on p. 464. The primary-reading receipt records the exact PDF, images and reading scope. No required manuscript proof is an input to this derivation.

## 0. Exact target and the maps to be constructed

The statement says:

> For a proper holomorphic degeneration of complex two-tori with smooth total threefold and central fibre mS, where S is irreducible and reduced, the group π1(S) has an abelian normal subgroup with cyclic quotient of order dividing m.

Write the degeneration as f:X→Δ, where Δ is a sufficiently small open disk with coordinate t, f is proper, X is a smooth complex threefold, and f:X\S→Δ* is a smooth proper map with connected complex two-torus fibres. This is the punctured-disk scope of a degeneration in the statement. The central scheme divisor is f*{0}=mS. All neighborhoods below are neighborhoods of the actual compact reduced analytic support S in the actual smooth total space X. There is no change of base, normalization of X or S, or replacement of the fibre by a cover.

We construct an outer neighborhood N retracting to S, a smaller punctured tube U=f^{-1}(Δ_δ*) contained in N, and a surjection

    p: π1(U,q) → π1(N,q) ≅ π1(S,s).

The torus bundle gives a normal subgroup Λ≅Z^4 in π1(U,q), with quotient Z measured by the winding of f. We prove surjectivity of p using a second retracting neighborhood N' inside f^{-1}(Δ_δ). At a smooth point of S, a small normal circle has winding m and becomes trivial in π1(N,q). Therefore the quotient of π1(S,s) by p(Λ) is a quotient of Z/mZ. The definitions, basepoints and each implication are supplied below.

## 1. Primary triangulation theorem with its precise input map

Theorem 2 on printed p. 464 of the opened 1964 paper applies to a countable real analytic manifold M and a locally finite family of semi-analytic subsets. It gives a locally finite simplicial complex K in an affine space and a homeomorphism τ:|K|→M. On every open simplex σ, τ(σ) is an analytic submanifold and τ|σ is an analytic isomorphism; every τ(σ) is either contained in, or disjoint from, each specified subset. The theorem is deduced there from Theorem 1 and the cited real analytic embedding theorem. I read this deduction and the complete main triangulation proof in §4, printed pp. 464–473, including the topographic family, projected triangulation, prismatic stratification, matching rectilinear cells, and final subdivision. I do not claim to have independently reconstructed the embedding theorem or to have read all the preliminary lemma pages of this article.

Here M=X considered as a real analytic six-manifold, and the family is the singleton {S}. This is a legitimate semi-analytic subset: in each complex coordinate chart, the local defining holomorphic functions of the analytic hypersurface S have real and imaginary parts real analytic, and their simultaneous zero set is S. X has a countable atlas, as a complex manifold. The singleton family is locally finite. Thus the theorem gives the stated τ and K for this actual pair (X,S).

Let L consist of the simplices whose images are contained in S. Because S is closed, every face of such a simplex is also carried into S: its image lies in the closure of that image, hence in S. Therefore L is a subcomplex and τ(|L|)=S. Properness makes S compact. Local finiteness of K and compactness of |L| imply that L is finite: cover |L| by finitely many neighborhoods, each meeting only finitely many simplices. A simplex in L has real dimension at most four, because its analytic image is contained in the complex surface S. One can include Sing(S) among the compatible analytic sets to see this also by separating the smooth real-four-dimensional part from its lower-dimensional analytic part; no chosen stratum has dimension larger than S. Equivalently local analytic dimension bounds the dimension of every embedded analytic submanifold contained in the set.

S is connected: an irreducible analytic space cannot be the disjoint union of two nonempty open and closed subsets, since those subsets would be closed analytic subspaces locally given by the whole space or the empty set. Its finite triangulation is consequently connected and path connected.

## 2. Explicit cofinal retracting neighborhoods

Take a barycentric subdivision of K and of L. The new L is a full subcomplex: a simplex of the subdivision is a chain of faces of the old complex; all its vertices lie in subdivided L exactly when all the faces in that chain belong to old L, and then the entire simplex belongs to subdivided L. Retain the notation K,L for this subdivision.

For x in a simplex of K, write its barycentric coordinates as λ_v(x), and set

    Q(x)=Σ_{v a vertex of L} λ_v(x).

Local finiteness makes this piecewise affine function continuous. Define V={Q>0}. It is an open neighborhood of |L|. Fullness of L means that all L-vertices of the simplex span a face belonging to L. Hence the following map is defined in that face:

    r(x)=Σ_{v in L} (λ_v(x)/Q(x)) v.

It is continuous on V and fixes |L|. The formula

    H(x,u)=(1-u)x+u r(x),        0≤u≤1,

uses the same simplex as x. Its total L-coordinate weight is

    Q(H(x,u))=(1-u)Q(x)+u>0.

Thus H remains in V, starts at x, ends at r(x), and fixes |L| throughout. This is an explicit strong deformation retraction. Its transport to X is

    R=τ∘r∘τ^{-1},   H_X=τ∘H∘(τ^{-1},id).

This is the exact morphism between the polyhedral neighborhood and the analytic support used here; τ need not be differentiable across simplex faces.

These neighborhoods can be taken inside any prescribed open neighborhood O of S. Indeed the closed star of finite L is a finite union of compact simplices. On this fixed finite union τ is uniformly continuous. Repeated barycentric subdivision has mesh tending to zero on that union. To check the last assertion, a simplex in one barycentric subdivision has vertices given by barycentres of nested faces. In a d-simplex the distance between two such barycentres is at most d/(d+1) times the diameter: for face sizes a≤b, write the larger barycentre as (a/b) times the smaller plus the barycentre of the remaining vertices with coefficient (b-a)/b≤d/(d+1). Iterating this bound over the finitely many dimensions proves mesh→0. Every simplex in the open star of the newly subdivided L has a vertex on |L|, so every point of that simplex lies within its mesh diameter of |L|. Compactness of S, uniform continuity and the positive separation from the complement of O now put the star inside τ^{-1}(O) after enough subdivisions. The full-subcomplex property continues to hold. Applying the same formulas gives a strong deformation retraction in every such smaller neighborhood.

Choose one such open connected neighborhood N⊂X of S. It retracts to S. By properness there is δ>0 with

    f^{-1}(Δ_δ) ⊂ N.

Here is the compactness argument. Choose a closed disk contained in Δ. Were arbitrarily small inverse-image disks not contained in N, there would be points x_j∉N with f(x_j)→0. Properness over the chosen closed disk gives a convergent subsequence x_j→x∈S; since N is open and contains S, the points of that subsequence eventually lie in N, a contradiction. Now take a second cofinal retracting neighborhood N' satisfying

    S ⊂ N' ⊂ f^{-1}(Δ_δ) ⊂ N.

Both inclusions of S are homotopy equivalences. For any q∈N'\S, choose a path β in N' from q to a point s∈S, for example the N'-retraction path followed by a path in S if a different s is selected. The induced maps from π1(S,s) into π1(N',q) and π1(N,q), using this same β, are isomorphisms. The inclusion N'→N consequently induces an isomorphism at q. No assertion that the whole inverse-image tube retracts to S has been made or is needed.

## 3. A complete loop-avoidance argument

We need only surjectivity of the map from the complement. Every based loop in N' is based-homotopic, within N', to a loop avoiding S. The following elementary construction proves this without assigning differentiability to τ along its simplex boundaries.

In a real coordinate ball B of the smooth six-manifold X, S∩B is covered by countably many smooth parametrized patches of dimension at most four. This follows from the finite or locally finite analytic open simplices furnished above: cover each of their parameter domains by countably many compact sets on which the analytic parametrization and its derivative are bounded. For any p∈B\S, the set of points w for which the straight segment [p,w] meets S is contained in the union, over these patches, of the sets

    p+a(x-p),    x∈S∩B, a∈[1,∞).

With a restricted to each compact interval, these are images of locally Lipschitz maps of spaces of dimension at most five into R^6. Their six-dimensional measure is zero. An elementary proof is to cover a bounded five-dimensional parameter cube by O(h^{-5}) cubes of side h. A Lipschitz map carries them into balls of radius Ch, whose total six-volume is O(h); let h→0. Lower-dimensional domains give the same conclusion. Countable patches and intervals preserve measure zero.

Consequently, for two endpoints p,p' in a convex coordinate ball outside S, one can choose an interior point w outside the two exceptional sets. The two segments [p,w] and [w,p'] avoid S and lie in the ball. The original path between the same endpoints in that ball is homotopic relative endpoints to this two-segment path, since the ball is convex.

For a continuous based loop in N', cover its compact image by finitely many convex coordinate balls whose closures lie in N', and subdivide its parameter so each short arc lies in one ball. Perturb each subdivision vertex into the relevant overlap outside S, leaving the basepoint q fixed. Such choices exist since S has empty interior; each overlap is open. Connect old and new vertices by short paths in the overlap. Each adjusted arc is still a path in its original ball. Replace it by the two-segment path constructed in the preceding paragraph. The replacements and the short vertex paths give a based homotopy inside N'. The final loop avoids S.

Put U=f^{-1}(Δ_δ*)=f^{-1}(Δ_δ)\S. The new loop lies in N'\S⊂U. Every class of π1(N,q) is represented by a loop in N', because N'→N induces an isomorphism. Therefore the actual inclusion U→N gives a surjection

    p:π1(U,q)↠G:=π1(N,q).

The proof establishes surjectivity. It does not discard possible relations introduced by disks crossing S.

## 4. The punctured torus bundle and its exact group sequence

The map f:U→Δ_δ* is a proper smooth submersion. A Riemannian metric gives a horizontal complement to its vertical tangent bundle. Horizontal lifting along paths in the base exists for their entire finite parameter intervals: the path image is compact in the punctured disk, and its inverse image is compact by properness, so the ordinary differential equation for the lift cannot escape. In local base neighborhoods the lifts and their inverses depend smoothly on their starting point and on the base parameter. This proves the bundle local triviality needed here directly.

Let H be the half-plane {Im w>-(log δ)/(2π)} and e:H→Δ_δ* the universal covering e(w)=exp(2πiw). Form the actual pullback

    U_H={(x,w)∈U×H : f(x)=e(w)},
    c:U_H→U, (x,w)↦x.

For a chosen w_0 over f(q), the straight segments joining w_0 to each w∈H lie in H. Lift their images under e horizontally. The resulting maps yield a smooth trivialization

    F×H → U_H,
    (a,w) ↦ (transport along e((1-u)w_0+u w) of a, w),

where F=f^{-1}(e(w_0)); its inverse transports back along the reversed path. Thus U_H is connected and its fundamental group is π1(F). The map c is a connected regular covering with deck action (x,w)↦(x,w+n), n∈Z. Its homomorphism on fundamental groups is injective, and its image is the kernel of the integer obtained by lifting a loop and recording its change in w. That integer is the winding of f along the loop. Every deck shift is attained by a lifted path because U_H is connected, so the winding homomorphism is surjective. Hence

    1 → Λ → Π:=π1(U,q) → Z → 1,

where Λ=c_*π1(U_H,(q,w_0))≅π1(F,q)≅Z^4. The last isomorphism comes from the defining lattice covering C^2→F=C^2/Γ, with Γ≅Z^4. The path-lifting description also shows that Λ is precisely the image of the inclusion of F into U. All groups use the displayed maps; no splitting or choice of a monodromy matrix is required.

Because p:Π↠G is surjective and Λ is normal and abelian, A=p(Λ) is a normal abelian subgroup of G. Normality is explicit: for p(g)∈G and p(λ)∈A, their conjugate is p(gλg^{-1})∈p(Λ). Commutators of elements of A vanish since they are images of commutators in Λ. The quotient G/A is the image of Π/Λ≅Z, and so it is cyclic, possibly still infinite at this stage.

## 5. The local normal circle and the exact exponent m

Choose a smooth point a of the nonempty irreducible reduced surface S. Since the central divisor is mS, there are holomorphic coordinates (z,z_2,z_3) in a sufficiently small neighborhood of a with S={z=0} and

    f(z,z_2,z_3)=u(z,z_2,z_3) z^m,

where u is a nowhere-zero holomorphic function. Shrink this coordinate neighborhood to lie in N'. It has a holomorphic logarithm of u. The map

    (z,z_2,z_3) ↦ (z'=z exp((log u)/m), z_2,z_3)

has nonzero complex Jacobian at a, namely u(a)^{1/m}; it is a holomorphic coordinate change after shrinking. Under this exact map,

    f=(z')^m.

Fix z_2,z_3 at the values of a and take the small closed normal disk D={|z'|≤r}. Its positively oriented boundary γ lies in U∩N' and f∘γ has winding m: in the parameter θ, z'=r exp(2πiθ), its image is r^m exp(2πimθ). The disk itself lies in N', so γ is null-homotopic in N.

Connect q to the boundary basepoint of γ by a path α in U. Such a path exists because U is a bundle over a connected punctured disk with connected fibre, or directly from the connected covering U_H. Then the based loop α γ α^{-1} maps under the winding homomorphism Π→Z to m and maps under p to the identity: α and the disk both lie in N. This proves that m lies in the kernel of the induced surjection Z↠G/A.

Every subgroup of Z containing mZ is dZ for a positive divisor d of m. To verify the divisibility rather than assuming it, take the least positive element d of that kernel; it exists because m>0 belongs to it. Divide m=qd+r with 0≤r<d. Since r=m-qd is also in the kernel, its minimality forces r=0. The induced map Z/dZ→G/A is bijective because its kernel has just been identified. Thus G/A is cyclic of order d dividing m.

Finally use the strong retraction N→S and the basepoint path β from §2 to identify G with π1(S,s). The transported subgroup A is abelian and normal, and the quotient order is unchanged by that isomorphism. This is exactly the asserted conclusion.

## 6. Computational scope and prerelease completion

The geometric argument above proves the topology. A new program, `code/S6_SERIES_PUBLISH_II_A_02Y2_neighborhood_certificate.py`, was written independently before any target release. It certifies the displayed barycentric formulas as identities in Q[Q,u] by integer coefficient convolution, and certifies the formal Laurent derivative of z^m for symbolic m by affine exponent arithmetic. It uses no numerical samples. In particular its output verifies total barycentric weight one, Q(H)=(1-u)Q+u, the cleared identity r∘H=r, and d(z^m)/z^m=m z^{-1}dz. The winding integral is then the explicitly parametrized circle calculation in §5. The run receipt binds the code and complete output. No historical program or target computation has yet been inspected, and no method comparison with an unidentified routine is claimed.

The target's claimed group conclusion has now been derived in full from its statement, the opened primary triangulation theorem, explicit local coordinates, ordinary differential equations and covering/path constructions given here. This file is ready for the embargo freeze. The comparison with the printed target can begin only after that freeze and release.
