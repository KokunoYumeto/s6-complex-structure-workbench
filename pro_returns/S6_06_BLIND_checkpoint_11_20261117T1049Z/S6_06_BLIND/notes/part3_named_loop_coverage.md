# Literal Part 3 named-family and scalar-loop coverage audit

Audit completed at checkpoint10 after the K33–36 proofs. Only the supplied
prompt, the allowed numerical/assertion CSV, the supplied construction
sources, and this run's own proofs were read. No earlier-run proof text
was consulted. The input CSV is unchanged; the read-only imported rows
are retained in `code/part3/stated_values_readonly.json`.

## 1. Every explicitly named construction

| Named input | Literal parameter and actual comparison | Proved return scope |
|---|---|---|
| AC26 original (3,4) | Positive `w=exp(-pi i c)` loop; `u=kappa w^2`. K33 supplies the single-loop integral cochain, all root/annular maps and simultaneous Cox endpoint. | Pair `(-1,-4)`, reference class0; every allowed fan has `(S-1)(S-3)/8 mod28`. The source's fixed reference fan has S1. |
| Viaclovsky2610.39102 coprime(3K,4L) | Positive `w_h=exp(-pi i c/(KL))`, with `u=kappa w_h^(2KL)`. K33 keeps both sphere signs and every fixed admitted delta coefficient. | Pair `(-KL,-4KL)` and all-fan class `KL(S-1)(S-3)/8`; reference class0. |
| Viaclovsky2609.33785 two-parameter construction | Theorem `main` and Proposition `family` define a proper submersion over a small **bidisc** `|mu|<eps, |lambda-lambda0|<eps'<|lambda0|`; its displayed source is `y²=x³+t x+mu t+1`, with `P=(-mu,sqrt(1-mu³))`. The source loops in that literal bidisc are contractible. Its fixed-source scalar extension is F53/K35 with `lambda=w²` at the minimal order-four cap. | Every loop contained in the stated bidisc has identity return by radial horizontal transport on the proper smooth family. For the corrected global scalar extension, pair `(-3,-12)` and all-fan class `3(S-1)(S-3)/8`; the source's reference fan has class0. No global source-braid loop is contained in the theorem's bidisc. |
| Viaclovsky2610.10451 combs | The labelled comb smoothing parameter `s` in its small punctured germ. F16 gives a single-valued actual smooth product, including each finite/cusp attachment. It does not substitute a scalar loop for this smoothing loop. | Identity return and class0. Transporting the initial smooth circle/page data by that actual product also makes the return on those data the identity. |
| Liu–Rollenske2609.33826 | Its literal scalar is `u` in `B_u=uB0`, with fixed cap `a=e4/4`. K36 proves that one positive u-turn has no holomorphic endpoint: the unique reduced multiple fibre's Albanese parameter changes from Q to -Q, and its j-invariant changes. The exact minimal correction is `u=w²`, constructed by K35. | The one-u path is not a closed holomorphic family and has no assigned return. For the corrected positive w-loop: pair `(-3,-12)` and class `3(S-1)(S-3)/8`; reference class0. This is a located parameter correction, not a proof gap. |
| OS49 `IV*+II+I2`, component line and `Q=3P` | F29–32/K34 give the actual family `lambda=r^(3k)` for every k>0 and norm coefficient n=±1, with arbitrary fixed delta character. K34 retains the line's I2 multidegrees(-1,+1), mixed period K and both norm signs. | Pair `(-6k,-24k)` and all-fan class `3k(S-1)(S-3)/4`. Both named diagonal fans have class0. K37 is separately constructing a shorter literal scalar endpoint; no division of this class is made. |
| Seven further one-log configurations in the prompt/CSV | F53's exact certificate enumerates all eight MW=Z entries,21 source profiles,16 retained whole-zero profiles,26 marked section/translation pairs, and all actual cap progressions. K35 supplies each weighted shorter parameter `lambda=w^(M/b)` through its actual source/root/line maps; for b1 this is the canonical `lambda=r^M` itself. | Actual page degree M, line square -H, chi from F53; on the K35 loop the pair is `(-3H/b,-24chi/b)` and the full fan formula is WS.5. No unnamed list of seven initial data is reconstructed from the bare CSV phrase alone. |
| Yang2609.29666 Types B/C | The exact source cap orders have gcd divisible by2 or3. F19 writes the quotient of the full attaching group onto Z/2 or Z/3. | The named constructions are not spheres; the explicit group quotient prevents an identification with S6. No Theta7 class is assigned to them. |
| Wang2609.11541 | F20 uses its actual primitive I2 rank-one collapse and order-three finite cap, with the complete integral matrices. | The named member is simply connected with H2=H3=Z/2 and is not a sphere. The stronger all-order/diffeomorphism assertions in CSV D.2.7–8 require their own exact scope checks; this audit does not promote them from the single named construction. |

Here `S=p²-pq+q²` uses the **physical** delta cocharacter in the
actual unimodular fan basis, not a relabelled period basis. Changing the
fan changes the family; it does not change the zero class of the original
fixed reference fan. K31, K33 and K34 contain the actual flop and frame
maps relating these choices.

## 2. The actual scope of the complete catalogue

F53 is the complete **whole-fibre Hom-zero** scalar catalogue in the
literal pullback-divisor setting of Engel Remark8.5, with all fixed
source coefficients, effective caps, vertical source-line choices,
finite characters, ordinary elliptic/delta clutches, and allowed fans
retained by F50–52/K32. It is not used to replace the separately named
component-supported OS49 source line; that line is handled directly in
F29–32/K34. Its finite lists and all norm progressions were independently
recomputed by the437-check `canonical_scalar_catalogue.py` certificate.

The K35 shorter quotient is an actual universal-logarithm deck quotient.
Its bth iterate is the specified canonical one-gamma endpoint before
passing to the finite r-action. The rational source lift, root line
characters, cap z-powers, and closing Cox frame are all retained. Thus
its characteristic pair is computed on an actual mapping-torus cover,
not obtained by dividing a residue in Theta7.

The source-moduli note `part3_source_moduli_loops_working.md` identifies
further loops on a **larger** marked-source parameter curve. Its selected
node branches exchange at three punctures. Those global loops are not
loops in Viaclovsky's stated bidisc; their complete fan/cap endpoints are
not assigned by F53. This distinction is witnessed by the literal
parameter inclusion of that bidisc and its labelled discriminant roots,
not by a claim that scalar and source parameters have no mathematical
relationship.

## 3. CSV comparisons promoted by this audit

The owned JSON `named_loop_coverage_results_mapping.json` updates only
complete literal assertions. It adds K33's exact original-loop endpoint
and fan scope to S6_04 B.6.2, B.6.21, B.6.24 and S6_02_PUSH C.3.24,
C.4.1. These agree for the specified original/reference construction.
The additional all-fan examples do not change those fixed-family claims.
The broad informal claim that every sphere family has zero return is
false: the actual OS45 generator family K10 and its F53/K35 data have
nonzero return, with the mapping-torus obstruction already proved in
F24/K10.

No all-n homology theorem is inferred from a sphere-only return theorem.
In particular the compound all-order assertions D.2.6, D.2.9, D.2.11
and D.2.12 are kept distinct from the proved n=±1 scalar-return scopes.
Existing independently proved topology mappings elsewhere in this run
remain in force; this audit does not replace or broaden them.

The smallest missing **named** endpoint identified in the audit was the
one-u Liu–Rollenske loop. K36 now resolves it by the intrinsic Albanese
obstruction and the exact degree-two correction. The remaining named
component-supported shorter-loop refinement is assigned as K37 and is
not silently included in K34.
