# P1.18 — shifted polynomial numerator majorant, before target reading

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation.

Input is only VI's clean finite-index assertion: positive weights w_i, the given matrices B_0,...,B_4, the centre z_0, radius R>0, and the shifted coefficients specified below. The P1.18 receiving collar proof and producer are unopened. No surrounding collar theorem or whole-row proof is claimed.

Let i,j run from 1 to the common matrix size n, and let

B(z)=sum_(k=0)^4 B_k z^k,
Bt_l=sum_(k=l)^4 binom(k,l) B_k z_0^(k-l),  0<=l<=4.

The coefficient formula itself is the actual polynomial translation map: substitute z=z_0+zeta in each term B_k z^k and apply the binomial identity. The coefficient of zeta^l is exactly Bt_l, including every contribution indexed by k>=l. Thus no unshifted coefficient is identified with a shifted one.

Fix a row i. Since each weight ratio w_j/w_i and each R^l is positive, the triangle inequality on the explicit coefficient sum gives

sum_(j=1)^n sum_(l=0)^4 |(Bt_l)_(ij)| (w_j/w_i) R^l
<= sum_(j=1)^n sum_(l=0)^4 sum_(k=l)^4
   binom(k,l) |(B_k)_(ij)| |z_0|^(k-l) (w_j/w_i) R^l.

The finite indexing set on the right is

{(j,l,k): 1<=j<=n, 0<=l<=k<=4}.

The permutation (j,l,k)->(k,j,l), with inverse (k,j,l)->(j,l,k), identifies it exactly with

{(k,j,l): 0<=k<=4, 1<=j<=n, 0<=l<=k}.

All summands are the same after this index permutation. Factoring the factors independent of l and using the binomial identity yields

sum_(k=0)^4 [sum_(j=1)^n |(B_k)_(ij)| (w_j/w_i)]
             [sum_(l=0)^k binom(k,l)|z_0|^(k-l) R^l]
= sum_(k=0)^4 [sum_(j=1)^n |(B_k)_(ij)| (w_j/w_i)] (|z_0|+R)^k.

For each fixed k the bracketed row sum is at most

||B_k||_w=max_(a=1,...,n) sum_(j=1)^n |(B_k)_(aj)| w_j/w_a.

Multiplication by the nonnegative scalar (|z_0|+R)^k preserves that inequality. Summing in k therefore bounds the entire expression for every individual row i by the same scalar sum_k ||B_k||_w (|z_0|+R)^k. Taking the maximum over those rows gives the precise desired inequality:

max_i sum_(j=1)^n sum_(l=0)^4 |(Bt_l)_(ij)| (w_j/w_i) R^l
<= sum_(k=0)^4 ||B_k||_w (|z_0|+R)^k.

The maximum was taken only after the rowwise inequality. No equality between a maximum of a sum and a sum of maxima is asserted. This derivation retains the complex centre through |z_0| and every unit/phase in the original coefficients until the stated triangle inequality. It is an exact finite algebraic estimate, not a numerical experiment.
