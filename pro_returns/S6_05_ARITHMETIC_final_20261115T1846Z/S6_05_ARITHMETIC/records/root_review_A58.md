# Root review of the completed sharp-arc oscillation theorem

Reviewed on 15 November 2026 after checkpoint 03 by the root AI agent. This is not human review. The full written proof of A.5.8 has been reread after the two independent track audits. The final source SHA256 is recorded below.

The source functional is used only in the reflection-even subspace; odd target periods vanish. The manuscript now states this choice explicitly. The normalized derivative of the exact outgoing Fermi resolvent supplies both the source phase and its positive principal amplitude. The line density has the scalar resolvent-jump normalization t/(pi i), leading to cos(tr)/(pi sqrt(cosh r)); no extra factor two is introduced by reflecting the positive spectral window.

Every inverse spectral power is Taylor-expanded about T before the even Paley–Wiener reconstruction. Spectral source errors are discarded before unfolding. After integrating in the spectral parameter, both the exact kernel and every retained cover term have the same finite propagation support; their difference therefore does too. Low-frequency control follows from the nonzero gamma connection coefficient and the Volterra kernel estimate |sin(t(v-r))/t|<=v-r. Uniform orbit packing and the source amplitude make the remaining finite-propagation image sum integrable over the whole source lift. The constant mode is rapidly small after evaluating the even entire window at i/2. The previously proved gap removes other imaginary parameters.

The endpoint substitution gives the exact measure a/(2D^(3/2)E^(1/2))dv and the stated BV density. Its denominator has size |N1| in every infinite tail. The source boost makes c_m geometric; the O(Y) reduced-axis count suffices to sum c/N2^2. Bounded-height tails and their possible endpoint jumps are summable too. Coefficient derivatives have the exponential decay required to cancel the v-coordinate singularity. No spacing of the dense endpoint phase values is used.

At every remaining stationary point, the transformed integral normal forces cosh(ell)=3|zprime|. The chosen window isolates ell=acosh(3), and the Hessian is positive for ell, negative for the actual phase. Integral t forces t=0 at that value. The two geometric stationary axes have normals (4,0,+/-1), positive cyclic multiplicities and the same stationary phase. The explicit unit contribution is rhohat(0)/(4*2^(1/4)*sqrt(pi)). The endpoint equality would contradict Q(sqrt(2)) intersect Q(sqrt(3))=Q. Consequently the coefficient C_star is strictly positive and the O(T^-1) remainder is lower order.

The asymptotic implies infinitely many nonzero complete-eigenspace contractions. The positive smoothed almost-periodic argument A.5.6 then gives both signs for the sharp count; the O(log X) wall correction and Y=3X+O(X^-1) change do not affect their square-root scale. This theorem settles the nonvanishing and Omega portions of A.5. It does not assert a square-root upper bound or a named conjectural implication.

Verdict: PASS.

Source: sections/A_nonvanishing.tex
SHA256: 00250b7c2a9122f1b8cf3c101130c9594c632c73f54912450ae7c98ca8d22300
Review time: 2026-11-15T18:00:56.550997+00:00
