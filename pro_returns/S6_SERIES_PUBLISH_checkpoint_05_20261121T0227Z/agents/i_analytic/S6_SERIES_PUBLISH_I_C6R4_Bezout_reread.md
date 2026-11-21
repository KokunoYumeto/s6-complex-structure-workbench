# Coarse duplication height bound

PASS: IA-C-17 uses exactly the original max of coefficient one-norms of F,G and the two Bezout pairs. No product with D is needed after projective gcd cancellation. Reread only, included in the C/D rewrite evidence, not an additional independent check.

Let H=max(|a|,|b|), d=gcd(F(a,b),G(a,b)), and C_j=||A_j||_1+||B_j||_1. Both Bezout identities imply d divides D since gcd(a^7,b^7)=1. Using the coordinate of size H gives |D|H^7 <= C_j H^3 max(|F|,|G|). Thus max(|F|,|G|)/d >= H^4/C_j because |D|/d>=1. The upper bound is <=max(||F||_1,||G||_1)H^4. Taking logs proves the stated bound. Telescoping with hhat=(1/2)lim4^-n h(2^nP) gives logC/(6*4^6).

The constants and their definition match the attached operative compendium proof exactly; full compared text and source hash are in the JSON receipt.
