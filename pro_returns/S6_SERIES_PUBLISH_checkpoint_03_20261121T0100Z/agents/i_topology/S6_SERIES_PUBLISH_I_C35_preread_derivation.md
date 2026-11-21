# Paper I — preread derivation of push:src:C.3.5 (tag 0322)

The target's compendium derivation has not been opened. Inputs read: its statement, fam:src:A.3.1 and A.2.1 statements; the exact period, monodromy, twist and cusp marking definitions; DGKX v1's proposition statements p2:prop:global-even-shift and p2:prop:strict-even-shift-action. The definition search incidentally exposed a few lines of the different proof of fam:A.3.1; that exposure is logged separately and is not represented as statement-only reading. The calculations below are reconstructed directly from the displayed matrices and the target formula.

## Exact maps and finite descent

Write g=gamma-hat, d=delta-hat, e=Pi_c d, E=d tensor gamma. The displayed period matrix gives Pi_(c+h)=Pi_c(I+hE), Pi_(c+h)g=Pi_cg+h e and R_j e=e. Thus the proposed additive translation

b_(h,c)=−(h/12) Pi_cg+(h ell−h²/24)e

has composition defect

b_(h,c)+b_(k,c+h)−b_(h+k,c)
= [−kh/12+((h+k)²−h²−k²)/24]e=0.

The correction −h²/24 is therefore exactly the correction required by the parameter dependence of Pi_cg. Taking k=−h also proves the inverse law.

For clockwise finite generators, ell(g_1 z)−ell(z)=−1/3 and ell(g_2 z)−ell(z)=1/4. From the displayed columns of A_1,A_2, the period-coordinate defects of b are

(h/12)(A_1−I)g−(h/3)d=(h/2)(0,1,−1,−1),
(h/12)(A_2−I)g+(h/4)d=(h/2)(0,0,−1,1).

They are integral for every even h and have gamma-coordinate zero, so Pi_c and Pi_(c+h) have identical images on these defect vectors. This proves core descent with the actual source and target period markings.

On a finite cap the ordinary-to-root collar translation is sigma_(j,c)=w_j Pi_c v_j, w_j=(2pi i)^−1 log s_j, gamma(v_1)=1 and gamma(v_2)=−1. Consequently the root expression of the map is b_(h,c)−h w_1 e at the first cap and b_(h,c)+h w_2 e at the second. The quantities ell−w_1 and ell+w_2 are, respectively, −(2pi i)^−1 log G and (2pi i)^−1 log F. They are holomorphic on the respective full root discs. The remaining period-vector term is holomorphic there as well. This proves extension in the actual finite charts, including the stated root markings.

## Cusp extension and the exact deck comparison

Put q=1/t, s=(2pi i)^−1 log q and Pi_cg=(6mu,−s+C_(c,21))^t. The root identity gives

ell=−s/12−(8pi i)^−1 log(1−q),

up to the fixed integral branch choice. Hence the full additive translation b_(h,c) has cusp representative

(−h mu/2,
 −h C_(c,21)/12−h log(1−q)/(8pi i)−h²/24)^t.

Each coordinate is holomorphic at q=0. Exponentiating gives a holomorphic (C*)²-valued unit. Its multiplication extends to every toric chart and stratum of the fixed periodic cusp fan. The integer shift changes C_c lambda by (0,h lambda_1), so its exponential is unchanged; the same unit map therefore descends under the exact cusp deck group.

For h=12 the ordinary representative after dropping the integral period −Pi_cg is

exp(2pi i(12ell−6))=(F/G)^12=t^4/(t−1)^3=K(t).

The two finite representatives are K s_1^−12=(t−1)^−3 and K s_2^12=t^4, which are units at t=0 and t=1 respectively. At the cusp,

K=q^−1(1−q)^−3=q^−1 H(q), H(q)=(1−q)^−3.

The full holomorphic cusp unit for h=12 is

U=(exp(−12pi i mu), exp(−2pi i C_(c,21)) H(q)).

The gamma-hat deck multiplier is

Psi_g=(exp(12pi i mu), q^−1 exp(2pi i C_(c,21))).

Their componentwise product is exactly Psi_g U=(1,K). Thus the two representatives differ by the stated gamma-hat deck map, with its sign fixed: multiplication by Psi_g takes the holomorphic full representative to the scalar ordinary representative.

## Orientation of the closing loop

The relation w=exp(−pi i c) gives c=(i/pi) log w. A positive w circuit changes c by −2, so six circuits end at c_0−12. The closing isomorphism to the initial fibre is Ftilde_(12,c_0−12). Its scalar cusp exponent is −1 as above. This is a map between the endpoint fibres; no smooth parallel-transport trivialization has been introduced, so this calculation alone supplies no equation for the smooth mapping class of a transported loop.

## Computation scope and next comparison

All constants, integer defects, composition terms, finite powers and cusp multipliers have been recomputed above by explicit algebra. A fresh exact-arithmetic script will independently check the finite defects and polynomial/cusp identities before the target derivation is compared. No retained program has been read or reused. The external proposition numbers/pages will be verified from the cited primary PDF separately; their attached TeX statement labels were read here.

Saved UTC: 2026-11-21T00:51:00.584669+00:00
