# The other conductor has at most two generic normalization branches

Status: complete scoped proof, awaiting independent audit. This note works after P4.55: A is smooth rational, H→A has degree two, R→A has degree one, and every other normalization-conductor component maps to the other rational-normalized image component B. The point-identification graph of D⊂N is a tree. Its H and R components are smooth embedded curves. Distinct points of any normalized component of D cannot be identified, because that would create a loop in this graph.

We prove that B cannot have one or two generic normalization branches. Its transverse multiplicity, conductor exponent and tangency order are unrestricted. Write r_B for this generic branch number and c_B for the number of normalized global conductor components mapping to B; their finite degrees sum to r_B.

## 1. An exact length-two intersection lemma

Let F,G be distinct reduced hypersurface branches in the smooth ambient threefold. Suppose their scheme-theoretic intersection has support a smooth curve A and generic length m=1 or 2 along A. The ring

    Q=C{x,y,z}/(F,G)

is a one-dimensional complete intersection, hence Cohen–Macaulay. Its only associated prime is the ideal of A; there is no point-supported embedded component. Choose z a coordinate on A. The ring Q is finite and torsion-free over C{z}, hence free of rank m. Its reduction is C{z}, and this quotient splits by the chosen coordinate z.

For m=1, Q=C{z}; in particular the linear parts of F,G have rank two and both branches are smooth. For m=2, its nilradical J is a free C{z}-module of rank one. The product J² vanishes generically and thus vanishes, by torsion-freeness. Choosing a generator ε gives the actual analytic algebra isomorphism

    Q=C{z,ε}/(ε²).

Thus Q has embedding dimension two, so at least one of dF,dG is nonzero. If G has generic order two along A, it belongs to the ordinary square of the smooth curve ideal, so dG vanishes everywhere on A. Then dF is nonzero and F is smooth. These are exact assertions about the original scheme-theoretic intersection, not about a reduced replacement.

## 2. Two distinct A–B junctions

The conductor has 2+c_B normalized components, so its total graph contribution is 1+c_B. At a two-branch image point, let r_A,r_B' count the normalized conductor points over its A and B branches and let n count normalization points of S. Pairwise intersection of local hypersurface branches gives a common element in their supports in {A,B}. Consequently n≤max(r_A,r_B') and the local graph contribution is at least min(r_A,r_B'). Here r_A is two or three: one or two H points and the unique R point.

If c_B=2, both B components have degree one and r_B'=2 at either junction. Each junction costs at least two graph identifications, exceeding the total budget three. If c_B=1 and its degree is two, an unramified junction likewise costs at least two and the other costs at least one, exceeding the budget two. Thus the only remaining possibility, for either generic branch number one or two, is one conductor component V over B with exactly one normalized preimage at each junction.

At either junction, if B belongs to every normalization-branch support, there is only one normalization point, and its graph contribution is r_A≥2. This again leaves no budget for the other junction. Hence A belongs to every support. The total budget two forces contribution exactly one at each junction. Each normalization point then has exactly one A branch; the sole V point is paired with one such branch. There are no further identifications. Connectedness of the tree on H,R,V forces the path

    H — V — R,

with one edge at each junction.

At the R–V junction, let F be its local hypersurface branch. All other local branches carry only A, and are supplied by H. If the two H preimages are distinct, intersect F with either corresponding branch G: their support is A and their generic intersection length is one, since the generic full A germ is ordinary triple. The length-one lemma makes F smooth.

If the two H preimages have coalesced, their one local hypersurface branch G has generic order two along A. The intersection of F and G has support A and generic length two. The length-two lemma again makes F smooth.

Both conclusions are impossible. F contains all the local generic B preimages: either the single normalization branch of a singular reduced unibranch transverse germ, or both generic branches of B when V→B^ν has degree two and ramifies at this junction. In each case F is intrinsically nonnormal along the nearby B germ, so it cannot be smooth on a neighbourhood of the junction. This excludes the two-junction graph.

## 3. One three-branch image point: one B conductor component

Since A is smooth, the image point has branches A,B_+,B_−. Suppose c_B=1. The points of the normalized V curve over the two distinct points B_+,B_− are disjoint, and cannot be identified in N. Thus no normalization point carries both a B_+ and a B_− conductor branch. Pairwise hypersurface intersections force every B_+ point and every B_− point to carry A.

The total graph budget is two. It follows that there is precisely one preimage over each B sign, each paired with precisely one A branch, and no other graph identification. The pairs must be H–V and R–V, since the graph is a connected tree. Any extra H preimage is an A-only branch.

At the R–V point the other H branch or branches intersect its hypersurface branch only along A: their B support has the opposite sign, or is empty. Exactly the length-one/length-two argument of Section 2 makes the R–V hypersurface branch smooth. It carries all nearby generic B sheets over its sign, so it is intrinsically nonnormal there. This is again impossible.

## 4. One three-branch point: two B conductor components

Now c_B=2, and denote the two degree-one components by V and W. Let h be the number of H points over the A value; h=1 or 2. The total normalized conductor branch count at the point is

    T=(h+1)+2+2=h+5.

The graph budget is three, so the number n of normalization points satisfies n≥h+2.

No singleton image support can occur. A singleton {A} forces every point to carry A, giving n≤h+1. A singleton {B_+} or {B_−} forces n≤2. Each contradicts n≥h+2. Thus every normalization point carries at least two image labels and n≤T/2. The case h=2 is impossible. For h=1, n=3 and each normalization point has exactly two conductor branches, with different image labels. The unique incidence type, up to interchanging V,W and the B signs, consists of

    F_R: {R,B_− on V},
    F_H: {H,B_+ on W},
    F_0: {B_+ on V,B_− on W}.

The domain conductor graph is the path H–W–V–R. The sole H point has local degree two over A.

The intersection of F_R and F_H is supported only on A and has generic length two. The equation of F_H has generic A-order two. The exact ribbon lemma makes F_R smooth. Choose its equation as X, and a coordinate Y on this smooth surface cutting A, with z a coordinate on A. The equation F_H has restriction to X=0 equal to Y² times a unit. Weierstrass preparation in Y and depression, preserving (X,Y), give the actual equation

    F_H=unit·[Y²+X²k(X,z)].

The second factor X follows from generic normal multiplicity two along A: a term linear in X is absent along every nearby A point.

The finite partial normalization is

    N'={u²+k(X,z)=0},   Y=Xu.

The equation in u is monic, so this map is finite. Away from A it is an isomorphism. The branch F_H is generically smooth along B_+ (the two generic B sheets belong to F_H and F_0 separately). Therefore N' has at most an isolated singularity near its point over the junction; as a hypersurface it is Cohen–Macaulay and regular in codimension one, hence normal. It is the actual normalization of F_H.

Its divisor X=0 is reduced and supported on H; no other conductor component maps to A in this normalization branch. Its local equation is u²+k(0,z)=0. The actual H is smoothly embedded in N and has degree two with ramification over A at this point. Thus k(0,z) has a simple zero: an even zero would give two branches, and an odd zero of order≥3 would give a singular curve. Consequently k_z(0,0)≠0, and N' is smooth. The minimal normalization resolution is the identity here.

Let m≥1 be the generic intersection multiplicity of the two normalization branches along B. It is the same integer on both local B signs, because they belong to one irreducible global image component. Let G be the equation of F_0, and let

    b=ord_A(G|A)>0.

On the smooth F_R branch, G has divisor m B_−: their intersection has no other support and generic multiplicity m. Restricting to its smooth A curve gives

    b=m I_{F_R}(A,B_−)≥m.                            (DS.1)

On the smooth normalization N' of F_H, G has divisor m W, where W is the conductor branch over B_+. The globally required SNC pole support makes H and W transverse. Hence

    ord_H(G|H)=m.                                    (DS.2)

But the map H→A has local degree two, and both restrictions are restrictions of the same ambient G. Therefore the left side of (DS.2) is 2b. Combining with (DS.1) gives 2b=m and b≥m, which is impossible for m>0.

All configurations with at most two generic normalization branches over B are excluded. The remaining case therefore has at least three such branches, so its generic transverse multiplicity is at least three. No bound on their conductor exponents has been used.
