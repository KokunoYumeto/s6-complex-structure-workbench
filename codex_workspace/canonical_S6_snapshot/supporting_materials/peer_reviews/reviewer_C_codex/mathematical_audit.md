# Mathematical audit summary

## Updated determination

The complete manuscript is **not presently independently certifiable**. If a binary editorial recommendation is required, reject in the supplied form pending specialist verification. Do not retain the earlier report's automatic-CDP-contradiction rationale.

## CDP

Lemma 10.3's conductor-supported section is locally sound. On a reduced non-normal normal-crossings fibre, an ambient differential can map to torsion in the Kähler differentials, disappear in the torsion-free quotient, and fail to come from the conormal term. This is precisely the case suppressed by the “it is immediate … it suffices” reduction in the printed proof.

Theorem 10.5 coherently applies this to the claimed central fibre using pullback to `dP6`, duality, and top-degree base change. The semidirect-product correction in Section 10 is also correct. These findings establish a credible gap in the published proof, not independently the falsity of the published theorem or the truth of the candidate construction.

Official article: <https://www.cambridge.org/core/journals/compositio-mathematica/article/algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number/CDF2D04CFB35CEE105E10B188D97D68A>

## Complete construction

No concrete theorem-breaking error was found in the period family, toric quotient, logarithmic fillings, gluing, van Kampen presentation, Leray calculation, or Appendix B nearby-cycle argument. This negative finding is not certification. The highest-risk unverified bridges are quotient properness, attaching-map signs, integral specialization lattices, and the Leray transgression.

## Confirmed errors

1. `parts/packet_06_body.tex:434`: Remark 7.28 needs an existential-and-unique quantifier for `ell0`.
2. `parts/packet_10_body.tex:122`: `pi1(N0)=Lambda` must be `pi1(N0)=barLambda`.
3. `parts/packet_09_body.tex:534-544`: Appendix A.3 labels a cohomological Mayer–Vietoris calculation as homology and reverses the homology arrows. Replace `H_k` by `H^k` in that calculation, then use universal coefficients; Appendix B already presents the correct cohomological resolution.

## Exact checks

The supplied harness reruns 22/22 exact assertions successfully with SymPy 1.13.1. Several checks share inputs; they verify displayed terminal algebra only, conditional on the geometric inputs.
