# Paper V: rereading the proof passages altered after candidate01

## Scope and identity

Date: 21 November 2026. Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), topology-check agent.

This record covers actual proof passages altered by the35 guarded suggestions following the visual reading of candidate01 pages55–96. I read the applied passages against both the guarded pre-edit text and the attached `source/S6_series_V_corrected_20261120.tex`. The integrated source read for this comparison had SHA-256 `e32aa6f1d12658e5fa4cb28ad48ead75c28d48fafe29a8779568e41c93ff0a2c`. The parent had previously confirmed application of every guard and preservation of all516 labels and484 tags. Later unrelated source changes do not change the scope of the passages read here.

Five new rows are recorded, all **used and rechecked in this run**. They give no targeted or independent pre-read proof credit. The previous41-row topology ledger remains unchanged. No event is added merely for page movement, typography or image inspection.

## `maps:src:F.2.9`, tag `02O0`: cite the Leray proof step

The original refers to the self-duality theorem itself for intermediate conclusions which were derived inside its proof before self-duality was used. The applied sentence points to that Leray argument. The required deductions use only the current hypotheses:

- Simple connectivity gives `H1(M;Q)=0`, so the degree-one transgression from the `a`-dimensional invariant space to `H2(B;Q)=Q` is injective.
- `b2=0` makes that transgression surjective and makes the permanent term `H1(B,j_*V)` vanish. Consequently `a=1`.
- Euler additivity gives `chi(B,j_*V)=−6+f1+f2+3=f1+f2−3`. The same Euler characteristic is `a+b=1+b`, giving `f1+f2=4+b`.

No self-duality conclusion is imported. The remainder of the original argument is unchanged. Moving the separate local-evenness proposition before its uses preserves its complete proof and labels; movement alone receives no event.

## `maps:src:F.2.18`, tag `02N7`: explicit peripheral restrictions

The source's boolean triple is replaced by its mathematical meaning in the ordered peripheral list `(order5, order4, cusp)`: zero, nonzero, zero. I checked this conversion by an exact post-proof-read calculation saved as `S6_SERIES_PUBLISH_V_page_rewrite_peripheral_check.py/.out`.

For each exterior degree `q=2,3,4`, put `P=Lambda^q A`, `Q=Lambda^q B1`, and `delta=(P−I;Q−I)`. A complete Smith decomposition produces the unique global torsion generator by an integral vector `z` with cocycle `delta(z)/2`. If its two components are `c1,c2`, the cusp generator `T=(PQ)^(-1)` has the exact restriction cocycle

\[
c_0=-T(c_1+Pc_2)=(T-I)z/2.
\]

Full integer image tests at the three peripheral differences give `(true,false,true)` in every degree, exactly as in the original. The program prints an explicit `z` in each degree. It reuses the Smith-transform method of the earlier checker and is not called an independent check or a complete rerun of the fourfold's homology.

The removed integrability disclaimer does not alter the smooth-classification argument: the applied proof still invokes the earlier relative almost-complex extension and then the characteristic-vector/normal-invariant classification. The punctured analytic assertion in the theorem retains its stated scope.

## `maps:src:F.2.20`, tag `02NA`: the ten scalar equations

The applied proof names the first eight scalar equations exactly: four entries of `YX=0` and four of `YRX=I2`. The original referenced a display which also contained a plane-intersection condition. The two trace equations and all subsequent characteristic-polynomial reasoning are unchanged.

The solution formula now uses the explicit linear bijection

\[
\operatorname{Mat}_{2\times5}(\mathbb Q)\longrightarrow\mathbb Q^{10},\qquad
Y\longmapsto(y_{11},\ldots,y_{15},y_{21},\ldots,y_{25})^t.
\]

Its inverse places the first five coordinates in the first row and the last five in the second. Thus the old `reshape(E^{-1}b)` and the applied equation for the column of ten row-ordered entries give exactly the same matrix. The determinant `D/4` and the exceptional-locus formulas remain the original inputs; they were not freshly recomputed in this passage reread.

## `maps:src:F.2.27`, tag `02NH`: the integral coinvariant identity

The original proof cited the resolved-product identity, which preceded it in the corrected original. Moving the resolved part after the headline made that reference forward. The replacement proves the required integral-coefficient variant at this use.

Let `L=Lambda^2 V_R` on the punctured oriented sphere `U`, with `R=Z3` as fixed in this proof. The natural map `j!L→j*L` is injective on every stalk. Its quotient is supported at the punctures, so its positive cohomology vanishes. The long exact sequence therefore gives

\[
H^2(B,j_*L)\cong H^2(B,j_!L)=H_c^2(U,L).
\]

Cap product with the oriented fundamental class is Poincare duality with these local coefficients and identifies the last group with `H0(U,L)`. Parallel transport from a base point identifies that group with the explicit coinvariant quotient

\[
L_b/\sum_{\gamma\in\pi_1(U,b)}(\rho(\gamma)-I)L_b.
\]

Point-supported changes from the specialization sheaf leave the same degree-two group. It is finitely generated over `R`; the previously proved rational vanishing makes it torsion, and therefore finite. The full positive finite-extension argument remains: the inverse image of `R/3R` in the Leray filtration is an extension by the finite term `Einf(2,2)`, hence a nonzero finite three-primary subgroup of `H4(M;R)`. UCT then gives the asserted three-primary torsion of `H3(M;Z)`. Only redundant defensive sentences were removed.

## `maps:src:F.2.29`, tag `02NJ`: the exact integral parabolic image

The removal of the black-box preface and saturation contrast preserves the integral maps. A free-group cocycle is a pair `(p,q)` in `L⊕L`. Its restrictions at the two finite generators vanish precisely when

\[
p=(A-I)x,\qquad q=(B-I)y
\]

for integral `x,y`. Its cusp restriction vanishes precisely when `p+Aq=(AB-I)z` for an integral `z`. Hence the displayed integer kernel maps onto exactly the parabolic cocycle lattice by `(x,y,z)↦((A-I)x,(B-I)y)`. The coboundaries are `((A-I)u,(B-I)u)`, obtained inside this kernel by `x=y=z=u`. The quotient remains exactly the printed `P_q`.

The applied instruction explicitly says to use the integral images of the peripheral differences. It does not change these images to saturated lattices. This is a reread of the altered computational prescription, not a new independent proof of every test in the theorem.

## Cleared visual concerns

The apparent missing article on candidate page78 and apparent `kernel` word on page94 were both visual misreads. Enlarged candidate-PDF crops and exact source comparisons confirm the original correct text. No source refutation, correction or new exterior-cube computation was made for either concern.
