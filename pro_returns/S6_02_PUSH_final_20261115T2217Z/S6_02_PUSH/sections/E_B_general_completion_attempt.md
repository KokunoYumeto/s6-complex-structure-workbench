# The actual origin: general analytic completion audit

Owner: classification_e. Date: 15 November 2026. This is an uninput main-question attempt, not a numbered completion or nonexistence theorem for the six-sphere family.

## 1. Exact problem and permitted completions

B.4.19 constructs the actual family after `w=r^6` over `(P1 × Δ_r) \ {(∞,0)}`. Its finite-place and cusp overlap maps are exact, including the scalar `K(t)=t^4/(t−1)^3` and component shifts `4,−3,−1`. Locally the missing base point is the origin of `B=Δ_q × Δ_r`. A desired completion may have compact three-dimensional components over this origin and need only be flat over `r`. Joint flatness over `B`, Kählerness, projectivity, or membership of all normalizations in Fujiki class C cannot be added. B.4.15 already supplies non-Kähler vertical components in the actual simple-torus family.

The present route asks whether a general analytic extension theorem supplies that missing cap, or whether its hypotheses produce a verifiable obstruction. It is independent of the explicit Kato-interface construction pursued by AB and D.

## 2. A general Hartogs completion principle is false, even with trivial monodromy

Here is an explicit instance of the obstruction treated by Nakayama. Set `U=B\{0}` and fix an elliptic curve `E=C/Λ`. Cover U by

`U_q=Δ*×Δ`, `U_r=Δ×Δ*`.

Glue the trivial E-bundles on these sets by translation by the E-valued holomorphic function `[1/(qr)]` on their intersection. This is a smooth proper holomorphic principal E-bundle `Y→U`; compactness of E and local triviality establish properness, with no global compactification assumed. It is locally projective and its integral local system is constant.

Its torsor class is nonzero and nontorsion. The base U retracts onto S3, so `H1(U,Λ)=H2(U,Λ)=0`. The sequence `0→Λ→O_U→E_U→0` consequently gives `H1(U,E_U)=H1(U,O_U)`. The displayed two-open cover is acyclic for O. A holomorphic function on U_q has no negative r powers, and one on U_r has no negative q powers. Thus the coefficient of `q^(−1)r^(−1)` survives in the Laurent-series quotient computing H1(O); it is nonzero after multiplication by every nonzero integer.

Nakayama's **Theorem 7.1.3**, in the original published paper on **p.604**, says that an LBP elliptic fibration over the complement of a codimension-at-least-two set in a polydisc, smooth outside the specified coordinate boundary, has a proper analytic elliptic extension (even up to bimeromorphic equivalence on that complement) exactly when it is globally BP. Here LBP means locally bimeromorphically projective and BP means bimeromorphically projective over the entire stated base. The preceding discussion of Ueno's problem on the same page identifies the smooth sectionless case above with a nontorsion class and gives its negative answer. Equivalently, the torsion characterization in Theorem 6.3.8 applies.

Crucially, this is **not** merely a theorem forbidding Kähler extensions. Step 3 of the proof, printed p.605, begins with an arbitrary putative proper extension and uses Hironaka flattening. It therefore accommodates nonflat fibres and vertical components over the missing origin before reaching the obstruction. The example disproves an automatic analytic completion theorem under the bare properties proper, smooth over U, compact fibres, and trivial cohomological monodromy. It does not by itself obstruct our two-dimensional torus fibres.

## 3. The hidden elliptic-quotient reduction fails for the actual periods

The precise failure can be proved directly from the actual period matrix, rather than inferred only from a generic-simplicity assertion. On the logarithmic cover of `(Δ_q*)×(Δ_r*)` use

`s=log(q)/(2πi)`, `v=log(r)/(2πi)`,

and the marked period columns

`γ=(6μ(q), C(q)−s−12v)`, `u=(τ(q), μ(q))`, `w=(1,0)`, `δ=(0,1)`.

The actual bounded units satisfy `τ=s+τ_hol(q)` and `μ(q)→μ0`, where `Im μ0≠0` (the specified unit has modulus `5+2√6`). The functions μ and C are holomorphic at q=0. These are the periods used in B.4.18–B.4.19, with all affine gauges retained separately.

Suppose two independent rational lattice vectors `z_i=(a_i,b_i,c_i,d_i)` had collinear complex periods throughout a nonempty open base set. An analytic family of elliptic subtori would supply exactly such a flat rank-two integral subsystem locally. On the connected logarithmic cover the determinant identity continues analytically. Write

`A_i=6a_i μ+b_i τ+c_i`,

`B_i=a_i(C−s−12v)+b_i μ+d_i`.

The coefficient of v in `A_1 B_2−A_2 B_1=0` is

`12[(a_1 b_2−a_2 b_1)τ+(a_1 c_2−a_2 c_1)]`.

Since τ is nonconstant, both rational coefficients vanish. If, say, `a_1≠0`, it follows that `a_1 z_2−a_2 z_1` is a pure δ vector. It is nonzero by independence. Collinearity would then force `A_1=0`. Let q tend to zero along the positive real ray. The unbounded τ term first forces `b_1=0`; the imaginary part of the remaining equality at μ0 forces `a_1=0`, a contradiction. Thus both a_i vanish.

In that remaining case the determinant identity is

`(b_1d_2−b_2d_1)τ+(c_1b_2−c_2b_1)μ+(c_1d_2−c_2d_1)=0`.

The same limit forces the τ coefficient to vanish. Because μ0 is nonreal and the other two coefficients are rational real numbers, both remaining coefficients vanish. All two-by-two minors of the vectors `(b_i,c_i,d_i)` are zero, contradicting independence.

Therefore the actual two-parameter torus family admits no analytic family of elliptic subtori over any nonempty open base set. It has no family of nonconstant elliptic quotients either: a holomorphic map from a complex two-torus to an elliptic curve is a translation of a homomorphism, whose connected kernel supplies the forbidden rank-two subsystem. A meromorphic map from a smooth two-torus to an elliptic curve is also holomorphic: near an isolated indeterminacy point, lift the map from the simply connected punctured ball to C and apply Hartogs. Thus replacing holomorphic quotient maps by meromorphic ones does not repair the reduction.

Finite base changes do not evade this argument. On a sufficiently small open subset where such a cover is unramified, it is a local analytic isomorphism, and the same rational period vectors and determinant identity apply. The result excludes the proposed passage from this actual family to Nakayama's relative-dimension-one theorem. It does **not** exclude an unrestricted proper origin cap.

The determinant coefficients are independently checked in `code/e_push_completion_diagnostics.py` and its output. The cusp-limit argument proves the statement for all rational vectors, not a finite list.

## 4. What the full weight-one variation does and does not supply

The actual linear period matrix has only logarithmic terms s and v, with bounded holomorphic remaining entries. Its two marked linear monodromies are commuting unipotent matrices: `u↦u+w`, `γ↦γ−δ` around q and `γ↦γ−12δ` around r. It therefore does not exhibit the elementary non-quasi-unipotent-monodromy obstruction to a proper analytic degeneration. Nor is its period matrix an essential-singularity map into the period Grassmannian. Such elementary natural-boundary tests do not decide this case.

The affine comparison between the two axial models is more data than that weight-one variation. In the positive-rotation convention B.4.18 it is represented by

`F(s,v)=(μ(q)(s+12v)/2, C(q)(s+12v)/12−(s+12v)^2/24+6v)`,

with `F(s+1,v)−F(s,v)=γ/12−δ/24` and `F(s,v+1)−F(s,v)=γ`.

Its quadratic logarithms are not a single-valued O-valued Čech cocycle on U. They cannot be identified with the additive class `1/(qr)` above, and their exponentials cannot be labelled an essential-singularity obstruction merely from their appearance. Integral-period changes and the singular group models on the axes must be retained. The actual fractional deck class, component rotation and reduced q-boundary are precisely the information missing from a test on the linear Gauss–Manin system alone.

### 4.1. The actual Jacobian pairing does extend as a log complex torus

This is stronger than merely observing unipotent monodromy. Put `Z=exp(2πiζ1)`, `W=exp(−2πiζ2)`, let X be their character lattice, and let `Y=Zu⊕Zγ`. Write `A=exp(2πi(τ−s))`, `a=exp(2πiμ)`, and `D=exp(−2πiC)`; all three are holomorphic units on the full q disc. The multiplicative period pairing, with rows `(Z,W)` and columns `(u,γ)`, is

```
             u              γ
 Z           q A            a^6
 W           a^(−1)         q r^12 D.
```

The base has the standard fine saturated log structure from qr=0. Its sharp monoid at the origin is N², written additively with generators q and r. The pairing modulo units is `diag(q,q+12r)`. Here is the complete face test in Kajiwara–Kato–Nakayama (2008a), Definition 1.2.3, printed pp.77–78. For the full face, a nonnegative functional `N(q)=h,N(r)=k` gives `diag(h,h+12k)`. If h>0 this is nondegenerate. If h=0<k, its kernel on both lattices is the first basis line, exactly the lattice associated with the face generated by q; the quotient pairing is multiplication by 12k. The zero functional gives zero-dimensional quotients. For the q face, both face lattices are the first basis line and the nontrivial quotient pairing is multiplication by h. For the r face and the zero face both face lattices vanish. These exhaust all faces and establish admissibility.

Definition 1.2.6, printed p.79, also requires nondegeneracy of the residual unit pairing. At q=0 no residual lattice remains. At r=0,q≠0 the residual lattices are `Ze1` and `Zu`, with pairing `log|qA(q)|≠0` after shrinking the q disc. At ordinary points the real logarithmic matrix has determinant

`log|qA| · log|q r^12 D| + 6(log|a|)^2 > 0`

after shrinking both discs so the first two logarithms are negative. Thus the stated pairing is nondegenerate everywhere on the bidisc. Definition 1.3.4, printed pp.81–82, therefore produces a log complex torus extending the actual Jacobian on the ordinary locus. No polarization is assumed or needed for this conclusion.

The precise existence inputs for proper models are Theorem 5.2.1, printed pp.171–172 (an admissible pairing admits a complete invariant fan with finitely many Y-orbits), and Theorem 5.3.2, printed pp.180–181 (the associated model is represented by a log-smooth fs log analytic space and is proper for a complete fan). Theorem 5.1.3 on p.170 summarizes these results; its unpolarized proper-model clause applies here. This establishes proper local models of the **Jacobian**, without identifying them with the two prescribed axial models of the actual affine family.

### 4.2. Full overlap, rejected short obstruction, and the remaining log-torsor test

The actual overlap must retain B.4.9's affine section σ and B.4.19's ordinary gauge. With `κ=κ0(q)`, one has `k=−s+12κ`, `σ1=6μv`, `σ2=−6v²+v(C−12κ)`. The exact identity is

`F−σ−kvδ = G(s)+6vδ`,

`G(s)=(μs/2, Cs/12−s²/24)`.

In particular the r-loop of the **full** overlap is only the integral period 6δ; its first coordinate has no log r term. A proposed obstruction obtained from the γ-valued r-loop of F alone is not an obstruction to this raw actual overlap. The analogous essential-orbit claim in `D_cusp_origin_attempts.md` was already withdrawn. No such analytic obstruction is asserted here. The polynomial cancellation is included in the exact diagnostic program.

There is a narrower log-torsor calculation still requiring an explicit check of the chosen axial origins. After q=Q^12, F by itself has Y-valued lift monodromies γ around Q and γ around r, since its additive differences are γ−6δ and γ. For the standard Jacobian log torus, a section on `Δ_Q×Δ_r*` has zero r-loop Y-monodromy: applying the q-ghost valuation to local multiplicative lifts sends that class by the injective map `Y→Z²`, `diag(12,12)`, while a section's transition coboundary has zero class. A section on `Δ_Q*×Δ_r` has zero r-loop Y-monodromy by contractibility of that loop in the base. Consequently F cannot be split into two sections of those standard axial log tori, and further finite Kummer covers do not kill this particular calculation.

To apply that calculation to the actual family one must establish both axial log-torsor identifications, with their origins and full descent: B.4.9's σ does give an actual section and fan-unit trivialization on `Δ_q×Δ_r*`; on the other axis the rotating quotient after q=Q^12 has period-valued twelfth deck, but its precise log-group origin and comparison still require verification. The ordinary gauge kvδ is not an extending section on the q-axis, so its cancellation cannot be silently treated as an allowed change of both log origins. Conversely, without proving the two identifications one cannot silently replace the actual overlap by F. This is a **working diagnostic**, not a claimed obstruction to the actual log torsor and still less to an unrestricted analytic cap.

### 4.3. Why arbitrary analytic caps do not automatically enter this category

Kajiwara–Kato–Nakayama's construction starts with a specified log torus and admissible pairing. It is not a theorem that an arbitrary two-torus torsor on this punctured bidisc extends across the corner, and it does not assert that every analytic cap with non-Kähler vertical components is such a log model. Flattening an unknown cap also does not produce that assertion.

Their separate *Analytic Log Picard Varieties* (2008b) makes the missing hypotheses explicit. Definition 7.1, printed pp.164–165, requires the log de Rham comparison, strict Hodge filtration properties, and an actual log Hodge structure (their term is “good for H^m”). The main comparison in §8 additionally assumes properness, separatedness, log smoothness, exactness, torsion-free characteristic cokernels, and the degree-one invariant-cycle isomorphism in Assumption 8.1, p.166. Section 9.3, pp.173–174, supplies goodness under locally projective or log-Kähler hypotheses; it does not supply it for an arbitrary non-Kähler filling. Section 9.3 explicitly says that log-Kählerness of every model of a log complex torus had not been proved there. Therefore that paper gives no automatic cap-to-log-torsor comparison under the permitted hypotheses here.

The exact unresolved step for this route is therefore an extension or obstruction theorem for the **full marked two-torus torsor and its two different axial models**, allowing vertical threefolds. No theorem with those hypotheses was located in the present searches. This is a search result and an exact failure of the proposed reductions, not a priority claim or a nonexistence proof for the actual cap.

## 5. Opened sources and access record

- Nakayama, N. (2002). Global structure of an elliptic fibration. *Publications of the Research Institute for Mathematical Sciences, 38*(3), 451–649. https://doi.org/10.2977/PRIMS/1145476270. Original published PDF: https://ems.press/content/serial-article-files/40808?nt=1. Its text extraction has a broken font encoding; printed pp.604–606 were rendered and read visually. The original author manuscript https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1322.pdf has readable text, with the corresponding theorem and seven-step proof on manuscript pp.140–144. The published numbering and actual flattening step were verified, rather than inferred from metadata. Local copies and rendered pages are outside the deliverable at `/workspace/scratch/20a906f0fadd/external_sources/E_completion`.
- Schröer, S., & Siebert, B. (2002). *Irreducible degenerations of primary Kodaira surfaces*. Original author manuscript opened at https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/kodaira.pdf. Section 6 supplies an instructive punctured-corner construction for its own positive-degree elliptic bundles; its Kodaira nearby surfaces are not the actual two-tori here. AB is independently investigating its explicit interface, so that construction is not duplicated in this note.
- Okano, T. (1967). A remark on complex analytic families of complex tori. *Publications of the Research Institute for Mathematical Sciences, 3*(3), 289–297. https://doi.org/10.2977/PRIMS/1195195452. Original journal PDF opened through https://ems.press/content/serial-article-files/41606?nt=1. Theorem 3 concerns an abelian quotient under a positive algebraic-dimension hypothesis; it is not a completion theorem and gives no elliptic quotient in the actual period situation proved above.
- Kajiwara, T., Kato, K., & Nakayama, C. (2008a). Logarithmic abelian varieties, Part I: Complex analytic theory. *Journal of Mathematical Sciences, the University of Tokyo, 15*, 69–193. Original journal PDF opened and downloaded: https://www.ms.u-tokyo.ac.jp/journal/pdf/jms150104.pdf. Definitions 1.2.3, 1.2.6, 1.3.4 and Theorems 5.2.1, 5.3.2 were read in their original text; the exact page locations and application are given above. Local external copy: `external_sources/E_completion/KKN2008LogTori.pdf`.
- Kajiwara, T., Kato, K., & Nakayama, C. (2008b). Analytic log Picard varieties. *Nagoya Mathematical Journal, 191*, 149–180. https://doi.org/10.1017/S0027763000025940. Original publisher PDF opened and downloaded through https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E8B336E3252DE1F448583CC5865DB1DA/S0027763000025940a.pdf/analytic_log_picard_varieties.pdf. Sections 7–9 were read for their actual comparison and goodness hypotheses; local external copy: `external_sources/E_completion/KKN2008LogPicard.pdf`.

Search metadata, without full retrieved article bodies, is saved in `evidence/E_B_completion_search_log.json`. Broad web results pointing to unverified AI-generated course pages were not used as mathematical authorities. No numbered result or global B status is changed by this note.
