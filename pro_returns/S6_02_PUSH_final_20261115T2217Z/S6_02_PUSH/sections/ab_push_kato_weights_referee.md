# Independent Kato geometry and tangent-weight audit

Owner: limits_ab. Date:15November2026,18:08UTC. This note audits D's B.4.11 and the proposed next relative-bundle construction. The weight result below is proved; no analytic globalization theorem for the threefold bundle is inferred merely from the weight calculation.

## B.4.11 referee

The exact linear neighbourhood in B.4.10 identifies a neighbourhood of the elliptic axis with the negative line bundle N. For degree−8 its contraction is the normally generated degree-eight elliptic cone. The maximal-ideal blow-up recovers the line bundle, so the flow/functorial-blow-up argument identifies π_*T_S(−log E) with Θ_Y. The invariant dlog two-form has poles exactly E plus the rational cycle C and gives K_S=−E−C. The resulting injection Ω¹(log E)⊗K_S→Ω¹_S proves H²TlogE=0 because b1(S)=1 forces H⁰Ω¹_S=0. The Atiyah extension on E has nonzero class c1(N); H¹At(N)→H¹T_E is an isomorphism. Every higher formal graded piece has positive degree and zero H¹. Finally varying a=e^(2πiτ) changes the marked elliptic period with nonzero Kodaira–Spencer class, even at extra-automorphism elliptic curves. This makes the Leray boundary map vanish. I found no gap in these Kato/formal-neighbourhood steps. D/root separately checked the analytic local-to-global criterion against its primary source.

## Complete global-vector-field calculation

Let n≥1 and write the central contracted Kato germ as

F(x,v)=(K x v^n,av), with K=κa^n and 0<|a|<1.

A global holomorphic vector field on S_n restricts to the outer spherical annulus of the Kato construction. In the blowdown coordinates its two coefficients extend to the ball by Hartogs. They agree with the pushed-down field on the connected unmodified part of the fundamental region by the identity principle. The collar gluing therefore imposes

V(F)=DF·V.

Write V=P(x,v)∂x+Q(x,v)∂v and expand in x. The coefficient Q_i(v) satisfies

K^i v^(ni) Q_i(av)=a Q_i(v).

For i>0, comparison of the smallest nonzero v-order is impossible, so Q_i=0. For i=0, the power-series coefficients give Q_0(v)=b v, since a is not a root of unity. In the first component the x⁰ coefficient vanishes by the same lowest-order comparison. For the x¹ coefficient P_1(v), the equation is

P_1(av)=P_1(v)+nb.

Evaluation at v=0 gives b=0, and then P_1 is constant. For every i>1 the equation is

P_i(v)=K^(i−1)v^(n(i−1))P_i(av),

which again forces P_i=0. Thus H⁰(S_n,Θ)=C·x∂x. The Euler field is tangent to E, so H⁰(S_n,Flog)=C with weight zero for Flog=T_S(−log E).

The Hartogs extension is used only to establish this exact germ functional equation; no finite Taylor truncation is used to classify the vector fields.

## Fixed locus and tangent weights

The action λ·(x,v)=(λx,v) fixes E pointwise. Outside E and the rational cycle, an equality with a nontrivial Kato deck iterate would require a^k v=v, hence k=0; then λ=1. On each rational curve in the cycle the action is nontrivial and fixes its two endpoints. The quotient cycle has n nodes, counting the self-node when n=1, so for λ≠1 the fixed locus is E and these n points.

Adjacent two-dimensional toric rays are (j,1),(j+1,1). Their dual characters evaluate on the x-scaling cocharacter (1,0) as −1,+1. Thus the tangent weights at every cycle node are λ^−1,λ. The logarithmic tangent sheaf is the ordinary tangent sheaf there. On E its Atiyah extension has both fibre weights zero and Chern character2; the normal line has degree−n and weightλ.

## Exact character computation

Apply the holomorphic Lefschetz formula to any root of unity λ≠1. It requires only a compact complex manifold, an equivariant holomorphic vector bundle, and a finite group action. The original theorem is Atiyah–Singer1968III, Theorem(4.6), printedp566; existing bibliography key AtiyahSinger1968IIIE is reused. The contribution of E is

2nλ/(λ−1)²,

and each node contributes

−(λ²+1)/(λ−1)².

Their sum is identically−n. Since H²Flog=0 and H⁰Flog is one weight-zero Euler field,

H¹(S_n,Flog)=(n+1) copies of the trivial representation.

This equality for infinitely many roots of unity determines the finite-dimensional C* character. The natural surjection H¹Flog→H¹(E,T_E)=C has weight zero; the Leray kernel therefore gives

H¹(Y,Θ_Y)=C^n with trivial C* action, and H⁰(Y,Θ_Y)=C with trivial action.

Consequently for the associated Y-bundle over P1 formed with any line bundle and this genuine C* action, the direct images of the relative tangent sheaf are O in degree0, O^n in degree1, and zero in degree2. Leray then proves H² of the relative tangent sheaf is zero. Analytic globalization of an assigned local deformation along the whole singular section requires its own precise relative deformation argument; this note does not replace that step.

Exact symbolic checks, adjacent-ray inversion and the vector-field defect for n=1,...,12 are saved in code/ab_push_kato_weights.py/.out/.json.

## Opened primary sources and scope

Opened Cathelineau1978 original Numdam PDF, https://www.numdam.org/article/ASENS_1978_4_11_3_391_0.pdf, Definitionp391 and Theorem1p392. Its group acts over the deformation base, so it does not provide the required moving-base weight-one action. Opened Rim1980 original journal scan, https://scispace.com/pdf/equivariant-g-structure-on-versal-deformations-3i8iymesgm.pdf, pp217–221: its construction is formal and algebraic. Neither is silently promoted to a convergent moving-base theorem for singular compact Y.

Opened Atiyah–SingerIII at https://math.uchicago.edu/~shmuel/tom-readings/AS%20III.pdf and Atiyah–SegalII at https://webhomes.maths.ed.ac.uk/~v1ranick/papers/as2.pdf. Their scanned PDFs initially exposed only metadata; targeted primary-source search returned the complete relevant text of III Theorem(4.6), printedp566, and II Theorem(2.12), printedp540. The former is sufficient using finite cyclic subgroups, as above. An attempted opening of Doan2026 arXiv2606.09199 returned DisabledError; no theorem from it is used. The smooth-manifold-only Doan2022 Kuranishi result is likewise not applied to singular Y.
