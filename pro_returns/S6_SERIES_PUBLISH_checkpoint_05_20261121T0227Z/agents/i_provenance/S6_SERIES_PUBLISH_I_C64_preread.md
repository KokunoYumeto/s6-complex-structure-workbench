# Independent preread derivation: ari:C.6.4

The target statement and the statements of C8.5, C6.1, C6.2 and C6.3 have been opened. The target's printed proof has not been opened. Additional inputs read are the exact x(6P) and psi6 formulas already printed in fam:D.1.1, Engel's height/component calculation, and primary DeMarco–Mavraki arXiv1701.07947v2 pp.1–2 and5–6. No check of those input theorems is claimed here.

## Archimedean inequality, including strictness

C6.1 gives, with complex embeddings counted separately,

    [K:Q] hhat_O(P_t) = sum_{v finite} n_v lambda_v(P_t)
                        - sum_{sigma:K->C} log N(P_{sigma(t)}).

C8.5 bounds every displayed N by sqrt(2). Equality occurs precisely at a modular image of tau=i, whose j-invariant is1728. The fixed pointed family has j=1728t, so equality at an embedding would give sigma(t)=1. Injectivity of sigma would then give t=1, excluded by the smooth-base hypothesis. Thus every archimedean term is strictly below (1/2)log2. There are [K:Q] embeddings in this convention, so dividing the global identity proves the stated inequality, and proves that it is strict for every t in the stated smooth base. For K=Q, the definition A_t=exp(sum_p lambda_p(P_t)) identifies the finite sum with log A_t, exactly as stated. No assumption about algebraicity of exp(hhat) is used.

## The function-field height divisor

Use the arithmetic model with differential dx/(2y):

    y^2=x^3-(3/4)t^3(t-1)x+(1/4)t^4(t-1)^2,
    P=(0,t^2(t-1)/2),  Delta=27t^8(t-1)^3.

The places on the base are normalized by ord_a of a local parameter. On a minimal local Weierstrass model, an integral nonzero point in the identity component has local height v(Delta)/12 in the normalization used here. The multiplication identity consequently yields

    lambda_v(P)=v(Delta)/12
       + ((1/2)max(0,-v(x(6P)))-v(psi6(P)))/36.

This identity is the same universal division-polynomial identity over a characteristic-zero discretely valued field; DeMarco–Mavraki §2.1 permits both number fields and function fields as product-formula fields. The finite local models have types IV* and III, whose component groups have orders3 and2, so 6P lies in the identity component. The exact rational expressions already present in D1.1 give the following fresh valuation calculation:

| Place | v(Delta_min) | v(psi6_min(P)) | x_min(6P) at the place | lambda_v(P) |
|---|---:|---:|---|---:|
| t=0 |8|24|64/81|0|
| t=1 |3|9|1/16|0|
| s=1/t=0 |1|0|78409/156816|1/12|

For the last row the exact change is x_infinity=s^2x, y_infinity=s^3y, so

    Delta_infinity=27s(1-s)^3,
    psi6_infinity(P)=s^35 psi6(P_{1/s}),
    psi6_infinity(P)(0)=99/65536.

The weight35 is 6^2-1. The minimal discriminant valuation1 gives type I1, whose component group is trivial, so the same identity-component formula applies. All three displayed x_min(6P) values are finite; none is the point O. At every other base place the family has good reduction, and P has finite integral coordinates, so its local height is zero. The divisor defined by the local canonical heights is therefore exactly

    D_P=(1/12)(infinity).

Its degree is1/12. The function-field canonical-height decomposition (DeMarco–Mavraki §2.2, equation2.1, p.6) gives hhat_O(P)=1/12. This also agrees with one-half of Engel's Shioda pairing <P,P>=1/6, with the divisor-O convention kept explicit.

The valuation computations were performed symbolically with exact rational polynomials. They are a fresh computation of the three local contributions, not a rerun of an attached program. The input sixth-division polynomial and x(6P) formula are used as already proved inputs.

## Uniform variation over algebraic parameters

DeMarco–Mavraki's primary v2 introduction, equation1.1 on p.1, states Tate's bounded-error height comparison hhat_{E_t}(P_t)=h_{D_P}(t)+O(1); Theorem1.1 on p.2 strengthens it by an adelically metrized line bundle. The family is an elliptic surface over the smooth projective curve P1 over Q, and the height just computed is positive, so its nonzero-height hypothesis is met. The comparison is on all algebraic points of the fixed base, not a separate bound for each field extension.

For D_P=(infinity)/12, multiplication by12 identifies its divisor with the standard degree-one divisor at infinity on P1. The height machine therefore gives h_{D_P}(t)=(1/12)h(t)+O(1). Combining the two bounded errors proves the target's uniform O(1) for every algebraic smooth parameter. The general Call–Silverman variation theorem need not be strengthened to obtain this: the elliptic-surface result in the opened primary DeMarco–Mavraki source supplies exactly the bounded-error comparison used here.

## Preread conclusion

All mathematical clauses of the target statement have been derived before opening its printed proof. The derivation uses the cited global identity and maximum theorem, computes the complete local variation divisor independently from exact rational input formulas, and checks the uniformity of the cited elliptic-height theorem. Comparison with the target proof remains a separate next step.
