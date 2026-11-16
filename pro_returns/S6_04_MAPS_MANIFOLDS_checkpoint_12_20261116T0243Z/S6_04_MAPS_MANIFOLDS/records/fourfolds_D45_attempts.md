# D.2.45: attempts, corrections and exact scope

This record preserves the concrete obstacles encountered while extending D.2.44. The final proof is sections/fourfolds_D2_remaining_even.tex. Root's independent full proof and all exact-code audits passed; D.2.45 is registered and integrated. The older failures below remain as attempt history.

## The regular-torus extension failed for a real reason

The ordinary-disc torus spanned by e1,e2,gamma generates H3 in the original-only semistable cases. It does not remain a generator after a single good-II logarithm. For example, the OS45/II cyclic-eight row with m=6, e=-1, n=-7 and r=0 has a nonunit ordinary-clutch linking coefficient. The completed finite replay retains the actual order of this regular torus and the entire regular-fibre H3 image; neither is silently replaced by the full group. Consequently the even parity of that torus alone cannot decide the refined class in the logarithmic cases.

## Residual twenty is not stably framed integrally

The literal critical cycle has exact order five for all residual-twenty rows. Its full spin lambda is nonzero, so a direct reuse of the globally framed proof of D.2.44 would be false. The retained chains bound five times the literal critical cycle. The new relative-characteristic lemma uses its actual rational linking number and fixes the integer correction by the admissible three-frame before division by two. It does not declare the cycle null, divide a congruence in Z/20, or assume an unspecified localized framing.

## A first finite character detected only the two-primary summand

The first useful core character was chi(delta)=n/d, chi(ell)=-r/d, chi(g)=0, with d=gcd(r,n). It gives an odd pairing on the two-primary part, but can fail to be a full generator at residual twenty. This was a valid partial result, not the final normalization.

The improved character is chi(delta)=1, chi(ell)=-sigma*r, chi(g)=-sigma*r*e, where sigma=n-m*e=±1. It respects m*g=r*delta+n*ell, has primitive kernel with elliptic monodromy B^sigma, and gives the full torsion linking unit sigma/b. Its nonzero fifth-column value is retained in the final exact replay. The older zero-root character is not substituted in that replay.

## A bounded test is not the all-order proof

The final executable tests 158 complete marked Smith problems: fourteen original-only clutch cases and four finite-II patterns at k=1,2,3, r=0,1, e=-1,0,1 and sigma=±1. It separately constructs eleven fixed integral chain certificates. Every monodromy fixes delta and its exact bar correction vanishes. The peripheral delta graph terms sum to zero. The finite delta Thom column plus m times the ordinary column and other filled-cap sweeps has literal fibre component -delta wedge v + m*e*delta wedge gamma, with primitive fibre value b*(n-m*e). Explicit integral monodromy preimages reduce it to that multiple of the chosen fibre generator for every integer parameter. These certificates, rather than extrapolation from 158 tests, establish the unbounded formula.

## Verified local and arithmetic inputs

Original-II differential y^2-x^3 has Jacobian ideal (x^2,y), hence critical multiplicity two. A free good logarithmic quotient has no corrected critical contribution after the full divisorial factor of df is removed. The exact local polynomial checks were independently rerun with exit zero in records/fourfolds_II_local_audit.out.

The full final chain program was independently read and rerun with exit zero in records/fourfolds_extended_critical_audit.out. It retains all actual Tate bases, original-II principal-circle lifts, full normal-column indices, root-loop characters, Smith coefficient vectors and closed-chain independence tests. The separate line/localization certificate passed eighteen patterns on fourteen rows, 1056 exact semicharacter checks, 62 adapted matrices, four symbolic arbitrary-twist finite normal rows and four original-II choices; its output is code/fourfolds_D2_remaining_AH.out.

The proved final values are P=2 for all residual-four rows, P=0 for all residual-eight rows, and P=14 in the primitive fibre coordinate for all residual-twenty rows. The complete fundamental-class invariant is zero. The scope is only the eighteen minimal primitive-Mumford patterns, including all simply connected type-II log orders and twists, without additional regular logs or higher translation weights.
