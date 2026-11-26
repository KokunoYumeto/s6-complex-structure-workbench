#!/usr/bin/env python3
"""Bounded names in the fully read invariant-Chern cap proof."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02LT", "maps:src:D.2.51", "352c4c99786471c1641a1e99f23d053072bfc2c59a1f3808079f70704836b5b2", "417–428",
           "Read all 958 lines, including the actual mapping-torus homotopies, integral cone, orbit partial sums, all quotient inverses, long-cover component map, boundary image and star markings. Identified the four plain-K formulas with the explicitly defined partial-sum operator through its domain, A_0 K identity and boundary signs. Traced the fibre-cycle Y separately from the later explicitly bound base mapping torus.")

operator_reason = ("The intended operator is the already defined mathcal K:ker R→Z^v, with entries -(sum_{r=0}^k z_{j,r}) for k<l_j-1 and final entry zero. For z=x-sRx (or u-sRu), Rs=I gives Rz=0; IC_local_12 gives A_0 mathcal K z=z. Hence the displayed d_3 and d_4 preimages and the quotient residues use this same map. On each orbit, summing mathcal K(x-sRx) gives sum_i i x_{j,i}, so the weighted scalar identity is unchanged. The repair prints that defined operator consistently; the earlier central fibre K retains its name.")
p.exact("partial-sum-font-command",
        r"\mathcal \mathcal \mathcal \mathcal \mathcal K(x-sRx)",
        r"\mathcal K(x-sRx)", operator_reason)
p.exact("zero-degree-boundary-preimage",
        r"The error is $d_3(0,K(x-sRx))$.",
        r"The error is $d_3(0,\mathcal K(x-sRx))$.", operator_reason)
p.exact("weighted-partial-sum",
        r" c^tK(x-sRx)=\sum_jc_j\sum_{i=0}^{l_j-1}i x_{j,i}.",
        r" c^t\mathcal K(x-sRx)=\sum_jc_j\sum_{i=0}^{l_j-1}i x_{j,i}.", operator_reason)
p.exact("wang-left-quotient-coordinate",
        r"\left(Rx,\left[-c^tK(x-sRx)/g\right]_D\right)",
        r"\left(Rx,\left[-c^t\mathcal K(x-sRx)/g\right]_D\right)", operator_reason)
p.exact("degree-three-boundary-preimage",
        r"The error in $u$ equals $d_4(-K(u-sRu))$; the $y$ error is zero.",
        r"The error in $u$ equals $d_4(-\mathcal K(u-sRu))$; the $y$ error is zero.", operator_reason)

p.exact("free-abelian-component-target",
        r"Cancellation of $q_0$ in this free group gives exactly",
        r"Cancellation of $q_0$ in this free abelian group gives exactly",
        "The stated target is ker d^t⊂Z^rho with addition. Its explicit basis J and inverse kernel coordinates give its commuting free abelian structure. The identity on that basis preserves all three component equations and cancellation by the nonzero integer q_0; adding abelian states the existing law.")

cycle_reason = ("Y_fib=Y is the same integral linear combination of the actual area and two mixed fibre tori, using the fixed Bezout section of IC_local_40. Identity on that cycle and its coefficients preserves its image under Phi, its scalar coordinate theta and the displayed subtraction of theta(delta wedge gamma), which still maps to Psi(w,0). The later Y is explicitly the base mapping torus of N, with its own projection and orbit-coordinate maps; those remain unchanged.")
p.exact("fibre-cycle-definition",
        r"and form that literal combination $Y$",
        r"and form that literal combination $Y_{\rm fib}$", cycle_reason)
p.exact("fibre-cycle-section",
        r" Y-\theta(\delta\wedge\gamma)\longmapsto",
        r" Y_{\rm fib}-\theta(\delta\wedge\gamma)\longmapsto", cycle_reason)

p.finish()
