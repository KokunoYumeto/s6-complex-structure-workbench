# Fresh complete certificate for Paper V, P1.18

**Conclusion.** The newly executed interval computation and a separate saved-data verifier establish the unique global minimum of the printed, normalized height function at the infinity root. They also enclose the minimum and both components of the specified splitting constant. The computational validation gate is closed by these supplied programs and outputs.

This work is by **GPT-6 Astra, ChatGPT Pro mode, inherited effort**, 19 November 2026. The printed P1.15–P1.18 proofs were read before implementation. The appropriate events are fresh computation/formal certificate and targeted proof check. This is not a prereading independent derivation, a different-family review, or an execution of an absent historical program. No historical coefficient arrays or leaves are inputs.

## 1. Inputs and exact coordinate maps

The inputs are the rational right connection `Y′=YΓ6` printed at `night:P1.16`, the integral monodromy matrices A and B and normalized intertwiner existence/uniqueness at `night:P1.15`, and the actual real quotient-intersection characterization at `night:P1.8`. All rational matrices are reproduced literally in the executable source. The program derives the root connections symbolically, rather than importing their printed coefficient arrays.

At zero set λ=u⁴ and D₀=diag(1,u⁶,u³,1,u⁻³,u⁻⁶). At infinity set λ=u⁻⁵ and D∞=diag(1,u⁻⁸,u⁻⁴,1,u⁴,u⁸). The regular frame is YD, and its exact right connection is D⁻¹λ′Γ6D+D⁻¹D′. Its denominators are 3125u⁴+256 and 3125+256u⁵. Every derived rational coefficient is saved in `fresh_root_connections.json`.

For U(0)=I and a root rotation ζ, set T=diag(ζ^{dᵢ}). Uniqueness of the regular equation gives U(ζu)=T⁻¹U(u)T. Consequently (UD⁻¹)(ζu)=T⁻¹(UD⁻¹)(u). Since D(1)=I, the based monodromies are U₀(1)⁻¹T₀⁻¹U₀(1) and U∞(1)⁻¹T∞⁻¹U∞(1). The system solved is XH₀=BX, XH∞=AX, Xe₀=e₀. Approximate QR chooses 30 equations only; Arb certifies the inverse and solution of that square subsystem. All other equations are checked to contain zero. **The exact existence of the common solution comes from P1.15.** Residual containment alone would not establish exact consistency of arbitrary overdetermined interval data.

The limiting frames are F₀=XU₀(1)⁻¹ and F∞=XU∞(1)⁻¹. The finite deck characters force the two coefficient variables to vanish at either centre. Thus h(center)=−96 Re(F₀₃)/(625π). The independent zero-root transport follows the positive real root axis from u=1/4 to 1; the infinity solution is evaluated directly at u=1. No closed meridian integration is needed to recover X.

The actual numerical root coordinates are v=a⁻¹/⁴u at zero and w=a¹/⁵u at infinity, where a=256/3125. Thus λ=av⁴ and λ=aw⁻⁵, respectively. Both root gauges have third indexed entry one; they scale only the two free complex coefficient columns and preserve the normalized w₀ column and the height.

## 2. Rigorous Taylor errors

For a shifted rational connection P(t)/Q(t), the program verifies the strict positive bound

`d = |Q₀| − Σ_{j≥1}|Qⱼ|Rʲ > 0`.

For positive weights w, use the induced maximum row-sum norm of diag(w)⁻¹M diag(w). It is submultiplicative, and entry ij is bounded by its norm times wᵢ/wⱼ. Put M=Σⱼ‖Pⱼ‖w Rʲ/d. Ordered integration of the actual right equation bounds a normalized transition on the radius-R disc by exp(MR). Cauchy's coefficient integral then bounds its omitted degree-N tail at modulus at most r<R by

`exp(MR) (r/R)^(N+1)/(1−r/R)`.

The program adds this error, times wᵢ/wⱼ, to both real and imaginary component radii. This rectangle contains the required complex error disc. The existing input, coefficient and matrix-product radii are retained. The zero-axis steps use exact rational centres and radii; complex collar steps use enclosed centres, strict denominator bounds, and their actual enclosure radii in the same formula.

For a scaled root equation U′=U(Σⱼ₌₀^{m−1}Bⱼzʲ)/(1+zᵐ), direct comparison yields

`(n+1)Uₙ₊₁ = Σⱼ Uₙ₋ⱼBⱼ − (n−m+1)Uₙ₋ₘ₊₁`,

with the last term absent for n<m. The product order is essential. With w=(1,1/128,1/128,1/32,1/64,1/32), let b=maxᵢΣⱼ,ₖ |(Bₖ)ᵢⱼ|wⱼ/wᵢ. The calculated b is below 1.447 at infinity and 1.135 at zero. On a radial segment the norm is at most b/(1−rᵐ). The elementary inequality

`1/(1−rᵐ) ≤ 1/[m(1−r)] + (m−1)/m`

follows from Σⱼ₌₁^{m−1}rʲ≥(m−1)rᵐ. Integration therefore gives the bound

`K(R)=exp(b[−log(1−R)/m +(m−1)R/m])`.

The degree-N root error is K(R)(r/R)^{N+1}/(1−r/R), with R=999/1000 and coefficients stored through degree 3000. A shorter evaluated prefix uses its own degree in this same bound. Blocked evaluation is exactly p(z)=Σ z^{32j}pⱼ(z); it prevents excessive rectangular interval wrapping without changing the polynomial or tail.

## 3. Entire rectangles and the actual height

At the centre of each outer rectangle, the program applies the real invertible matrix T of P1.18 step1, computed from that actual centre frame. T fixes e₀. For a vector with real lower five coordinates, its change in top coordinate is real. Thus this is an exact height-preserving map, including for the new centre-dependent choice.

If ρ is the half-diagonal and A is a nonnegative entrywise bound on the right connection throughout the rectangle, every segment from its centre stays in the rectangle. The kth ordered integral is bounded entrywise by |Ycentre|ρᵏAᵏ/k!. Hence

`|Y(z)−Ycentre| ≤ |Ycentre| [exp(ρA)−I]`

simultaneously on the whole rectangle. Ball matrix exponentiation and outward radii retain all rounding. This estimate is not a sample test.

The normalized real intersection is determined by four selected lower-row equations Mv=b, where row i is (Im Yᵢ₁,Re Yᵢ₁,Im Yᵢ₂,Re Yᵢ₂) and bᵢ=Re Yᵢ₃. The actual fifth equation follows from the geometric existence/uniqueness statement P1.8. A certified invertible four-row minor computes that same vector. With c the corresponding top row and d=Re Y₀₃, the height is (96/(625π))(cv−d). Interval inversion and evaluation give bounds on every point of the rectangle.

## 4. Central strict minimum

The four closed quadrants of Q=[−1/10,1/10]² are evaluated directly in the infinity-root chart. The code differentiates the implicit system, retaining both cross terms in repeated-index second derivatives. It uses Yx=YG, Yy=iYG, Yxx=Y(G²+G′), Yxy=iY(G²+G′), Yyy=−Yxx. In each closed quadrant,

`min(hxx,hyy)−|hxy| > 1/4`.

The fivefold deck map forces the gradient at zero to vanish. Integrating the positive Hessian along the segment from zero yields h(w)−h(0)≥|w|²/8 throughout Q. Thus its centre is the unique minimum on Q. The separate saved-data verifier recomputes the Hessian lower inequalities from the fully serialized entry balls and checks the four-square exact area 1/25.

## 5. Cusp series, branch, and exact transport to the prior marking

Put λ*=−a, q=λ/λ*−1 and Dλ=diag(1,λ²,λ,1,λ⁻¹,λ⁻²). Exact symbolic calculation gives the right connection of YDλ as R/q+A₀/(1+q), with R²=0. Write YDλ=Hc(I+R log q)P(q), P(0)=I, and ad(M)=MR−RM. Then

`(nI−ad)Pₙ = Σⱼ₌₀^{n−1}(−1)^{n−1−j}PⱼA₀`.

Since ad³=0, its inverse is (I+ad/n+ad²/n²)/n. With cusp weights (100,1,1,1,1,1), the exact values are r₀=5103/8000, a₀=367/512 and γ=(1+2r₀+4r₀²)a₀=22920107503/8192000000. Thus ‖Pₙ‖≤(γ/n)Σⱼ<ₙ‖Pⱼ‖. The scalar majorant is (1−s)⁻γ, and the degree-600 tail on |q|≤r<2/5 is

`(3/5)^−γ (r/(2/5))^601 /(1−r/(2/5))`.

The exact fresh anchor is qa=1/4, λa=−5a/4, wa=(4/5)^{1/5}exp(πi/5), ua=a⁻¹/⁵wa. Its constant frame is

`Hc=Yroot,∞(wa) D∞(ua)⁻¹ Dλa P(1/4)⁻¹ (I−R log(1/4))`.

The certified logarithmic monodromy is Nnew=2πiHcRHc⁻¹=B⁻¹A⁻¹−I. The former displayed monodromy is Nold=A⁻¹B⁻¹−I. The exact comparison is **Nnew=A Nold A⁻¹**. The map z↦Az fixes e₀ and adds z₃−z₄+z₅ to the top coordinate, which is real on the normalized vector; it preserves the height exactly. Both integral matrices and the exact change between the two nilpotent-adapted markings are saved. The marking change has block form (D,E;0,D), so a graph Z changes to DZD⁻¹+ED⁻¹ and its imaginary part by a real similarity. The new anchor is not silently identified with the former branch.

An explicit unimodular J gives J⁻¹NnewJ=(0,I₃;0,0) and J⁻¹e₀=e₀. At c*=−h∞, form the actual columns of J⁻¹HcP as V₁,V₂,V₃−(625π/96)c*e₀. Their lower block is invertible on the whole closed disc |q|≤1/100. The upper/lower quotient is C(q), and the actual graph is log(q)I/(2πi)+C(q). Coefficient absolute sums and the cusp tail give lower bounds greater than 1.7115,4.6510,3.8702 for the first three coefficients of det(tI+y₀I+Im C); the leading coefficient is one, y₀=log100/(2π), t≥0. All coefficients are positive. The graph is transverse throughout the punctured inner disc. At q=1/100, h=−0.45044220…>h∞, so connectedness gives h>h∞ throughout it.

For each fixed real M, the graph coefficient for c in the compact interval from c* to −M is bounded on a sufficiently small closed disc. The term −log|q|/(2π) tends to +∞ and gives a uniform Neumann inverse. The sign cannot cross zero along that interval, so h>M near the cusp. This proves the required limit h→+∞.

## 6. Complete coverage and independent finite validation

Let R=49/50 and S=103/100. Infinity and zero use their first-quadrant closed discs of radius R. Infinity contains a full 2π/5 sector and maps onto |λ|≥aR⁻⁵; zero maps onto |λ|≤aR⁴. The collar is R≤|w|≤S in the first quadrant, covering aS⁻⁵≤|λ|≤aR⁻⁵. The exact rational inequality R⁴≥S⁻⁵ proves overlap. Its discarded cusp boxes satisfy |−w⁻⁵−1|≤1/4. The cusp upper half-disc is covered by the rectangle [−1/4,1/4]×[0,1/4], and the exact integral conjugation matrix K of P1.18 sends it to the lower half and preserves h. These closed sets cover all regular base points and both finite roots; the inner cusp disc and central root square have the preceding proofs.

| Region | Strict leaves | Geometric leaves | Total | Exact weaker bound on all strict leaves |
|---|---:|---:|---:|---:|
| Infinity root | 335 | 89 | 424 | −1.094216 |
| Zero root | 200 | 77 | 277 | −1.083056 |
| Cusp annulus | 113 | 8 | 121 | −1.083777 |
| Collar | 440 | 338 | 778 | −1.030556 |
| **Total** | **1088** | **512** | **1600** | |

Every strict bound exceeds the exact rational threshold U=−1.0945402503114027801162682630549457037, itself strictly above the certified h∞. Every geometric leaf has a verified exclusion or an explicitly already covered region. The output includes all rational rectangles and all quadtree addresses. There are no pending leaves. The central proof adds four closed Hessian squares.

The separate `verify_saved_certificate.py` uses exact Fraction arithmetic to reconstruct each rectangle from its address, check prefix freeness, check Σ4⁻depth=1, and verify exact total areas. It rechecks each geometric reason, every serialized strict inequality, the central Hessian bounds and cusp coefficient positivity. It recomputes the normalized finite monodromy residuals and the endpoint values from the saved interval matrices. This second program validates the finite partition and the saved arithmetic conclusions; the first program supplies the actual interval ODE enclosures. Both were run successfully from the exported package.

## 7. Results and splitting comparison

The fresh endpoint values enclose

- h∞=−1.094540250311402780116268263054945703725533269405330897770522063712646972012, radius <4×10⁻⁷⁶;
- h₀=−0.931793376356523505430795105796011114990828200516519412438798244146481016929, radius <4×10⁻⁷⁶;
- h₁=−1.034276622416321799494248845378346052594964777902188211320859963181231557893, radius <7×10⁻⁷⁶.

The specified upper-half-plane continuation to λ*/2 is represented in the zero-root chart by v=2⁻¹/⁴exp(πi/4). Its path is homotopic to the stated upper polygon in the upper half-plane, relative endpoints, and the root gauge preserves column3. Therefore the computed a_split=(96/(625πi))Y₀₃(λ*/2) uses the requested normalization exactly. Its components are

- Re a_split=−0.709988567912642777172347345501230814862723373155147078835184685291921721466;
- Im a_split=−0.913401705936415336214322922382837326921918064986662117881160238051816558746,

each with outward radius <8×10⁻⁷⁶. The exact morphism of families is ξb=ξoriginal−a_split; the original height is hb−Im a_split. The minimum in that splitting is −0.181138544374987443901945340672108376803615204418668779889361825660830413266, radius <8×10⁻⁷⁶, at the same base point.

## Confidence and remaining reliance

**High confidence in P1.18's computational global-minimum gate: closed.** There is a complete fresh execution, independent saved-partition validation, exact gauge and branch maps, a strict central Hessian, a uniform inner-cusp determinant, and numerical enclosures agreeing with the printed constants. The proof depends on the printed rational connection's geometric identification, the exact normalized intertwiner existence/uniqueness of P1.15, and the real-intersection characterization P1.8; these are explicit mathematical inputs, not inferred from interval residuals. It also relies on the tested Arb/python-flint arithmetic implementation. No formal proof-assistant verification or different-family review is claimed. The original named programs remain absent; their historical events are retained, and this new certificate supplies its own complete files.
