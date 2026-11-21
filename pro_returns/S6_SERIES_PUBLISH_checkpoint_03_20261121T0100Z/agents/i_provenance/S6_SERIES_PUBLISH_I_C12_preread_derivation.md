# Independent targeted derivation before reading ari:C.1.2's proof

Recorded on 21 November 2026 UTC by GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH/provenance_inventory.

## Prior exposure and input

Only the target statement has been read from the parent's statement-only intake. The parent's assignment disclosed that a full check needs the absence of logarithmic winding, and that the printed proof uses an additional E6 bound. No formula or step from that printed proof has been opened here. The argument below is written before opening it and obtains the required phase control by real Weierstrass segments and positive theta-product factors.

The preceding C.1.1 distribution theorem has already been checked in full. The definitions are those of the frozen Paper I source: the theta variable has periods 1 and τ; ρ=(1+i√3)/2; μ is the lower cusp-selected zero of the Weierstrass function; and

\[
\beta^{\rm part}(\tau)=\frac{6i}{\pi}
\Log\frac{\vartheta_1(\mu(\tau),\tau)}{2\sqrt3\,\eta(\tau)},
\qquad (\beta^{\rm part}+\tau)(\infty)=0.
\]

The two approaches used below are τ=iT, T decreasing to 1, and τ=1/2+iT, T decreasing to √3/2. Near the cusp the chosen logarithm is the same on both: the normalized quotient tends to one uniformly for 0≤Re τ≤1/2 after dividing by its factor exp(πiτ/6).

## 1. The exact norms from endomorphism kernels

On the square lattice, α=1−i has degree two and nonzero kernel point
\(p_i=(1-i)/2\), because \((1-i)p_i=-i\) is a lattice vector. C.1.1 gives
\(N(p_i)=|1-i|=\sqrt2\).

On the hexagonal lattice, ρ²=ρ−1 and α=1+ρ has degree three. Its kernel is
\(\{0,p_\rho,-p_\rho\}\), with \(p_\rho=(2-\rho)/3\), because
\((1+\rho)p_\rho=1\). The two nonzero points have the same norm by evenness, so
\(N(p_\rho)^2=|1+\rho|=\sqrt3\), and consequently
\(N(p_\rho)=3^{1/4}\).

These are the required zero points of the Weierstrass function. In the square case \(ip_i-p_i=i\), whereas scaling gives
\(\wp(ip_i)=i^{-2}\wp(p_i)=-\wp(p_i)\); hence \(\wp(p_i)=0\).
In the hexagonal case \(\rho p_\rho+p_\rho=1\), whereas scaling gives
\(\wp(\rho p_\rho)=\rho^{-2}\wp(p_\rho)\). Evenness and periodicity make its left side \(\wp(p_\rho)\), and \(\rho^{-2}\ne1\), so \(\wp(p_\rho)=0\).

## 2. The lower zero on the rectangular path

Let τ=iT with T>1. The lattice is invariant under conjugation. On
\(z=1/2-ib\), the identities \(\bar z=1-z\), evenness and periodicity show that \(\wp(z)\) is real.

The derivative \(\wp'\) has its only zeros at the three nonzero half-periods: it has a pole of order three at the identity, is odd, and vanishes at those three points, which therefore exhaust its zeros. Thus on the interior of the segment \(0<b<T/2\) the real function \(b\mapsto\wp(1/2-ib)\) has no critical point.

Its endpoint values are

\[
e_1=\frac{\pi^2}{3}(\vartheta_3^4+\vartheta_4^4)>0,
\qquad
e_2=\frac{\pi^2}{3}(\vartheta_2^4-\vartheta_4^4)<0.
\]

Here the theta constants are evaluated at iT. To check the strict second sign without a numerical approximation, θ2(iT) is strictly decreasing in T by its positive defining series, and θ4(iT) is strictly increasing by its positive product
\(\prod_{n\ge1}(1-e^{-2\pi Tn})(1-e^{-\pi T(2n-1)})^2\).
The modular transformation at i gives θ2(i)=θ4(i). Therefore θ2(iT)<θ4(iT) for T>1.

There is consequently one and only one zero on this segment, at b=b(T) in (0,T/2). It varies continuously and, away from the endpoint, analytically. The cusp limit

\[
\wp(1/2-ib,iT)\longrightarrow
\pi^2\operatorname{sech}^2(\pi b)-\frac{\pi^2}{3}
\]

identifies it with the lower cusp-selected zero, where
\(b\to b_\infty=\log(5+2\sqrt6)/(2\pi)\) and \(\cosh(\pi b_\infty)=\sqrt3\).
As T decreases to 1 the zero converges to b=1/2, namely p_i. This last assertion also follows from compactness of the segment, continuity of wp away from its pole, and uniqueness of the zero at the square half-period.

## 3. The lower zero on the rhombic path

Let τ=1/2+iT with T≥√3/2. Conjugation again preserves the lattice, since \(\bar\tau=1-\tau\). Therefore wp(1/2−ib) is real.

For 0<b<T, that segment contains no half-period: an equality
\(2(1/2-ib)=m+n\tau\) would force n=−1 and b=T/2, but then m=3/2, which is not integral. The function has no critical point on the entire open segment. As b tends to T it tends to minus infinity, since \(1/2-iT=1-\tau\) is a lattice point and the approach direction is imaginary.

At b=0 its value is positive throughout this path. Here q=−r with
\(r=e^{-2\pi T}\le e^{-\pi\sqrt3}<1/100\). The Fourier expansion at the half-period gives

\[
\frac{\wp(1/2,\tau)}{\pi^2}
=\frac23+16\sum_{n\ \mathrm{odd}}\frac{nq^n}{1-q^n}
\ge\frac23-16\frac{r}{(1-r)^2}>0.
\]

The last inequality already follows from r<1/100. The elementary bound r<1/100 follows from π√3>5 and the positive Taylor partial sum of e^5 through degree six, which exceeds 100. No E6 estimate is needed here.

There is exactly one zero on 0<b<T. Its cusp limit is the same b∞ as above, so this is the lower cusp-selected branch. At T=√3/2 the point pρ has real part 1/2 and b=T/3 and is a zero by Step 1. Uniqueness therefore identifies the endpoint with pρ, without a lattice-translation ambiguity.

## 4. The theta quotient has a fixed argument on each entire path

Write μ=1/2−ib, so X=exp(2πiμ)=−exp(2πb), a negative real number. The Jacobi product in the period-one variable is

\[
\frac{\vartheta_1(\mu,\tau)}{\eta(\tau)}
=2q^{1/12}\sin(\pi\mu)
\prod_{n\ge1}(1-q^nX)(1-q^nX^{-1}),
\qquad q^{1/12}=\exp(\pi i\tau/6).
\]

The sine is cosh(πb)>0. On the rectangular path q>0, so every product factor is positive. The whole quotient is positive, and its continuously chosen logarithm has imaginary part zero from the cusp to i.

On the rhombic path q=−r. Even-n factors are positive. For odd n the two factors are
\(1-r^n e^{2\pi b}\) and \(1-r^n e^{-2\pi b}\), both positive because 0<b<T≤nT. Hence the quotient has the fixed argument π/12 along this entire path, supplied only by q^(1/12). There is no winding or passage across a zero.

Near either cusp path the quotient divided by
\(2\sqrt3\exp(\pi i\tau/6)\) tends to one. Therefore these fixed arguments are the arguments of the specific logarithm fixed by \((\beta^{\rm part}+\tau)(\infty)=0\), not merely the arguments modulo 2π.

## 5. The four endpoint values and determinant values

The Gaussian conversion is
\(|\vartheta_1(\mu,\tau)/\eta(\tau)|=N(\mu,\tau)\exp(\pi(\operatorname{Im}\mu)^2/T)\).
At i the exponential is exp(π/4). At ρ it is exp(π/(6√3)). Combining Steps 1 and 4 therefore yields exactly

\[
\frac{\vartheta_1(p_i,i)}{\eta(i)}=\sqrt2e^{\pi/4},
\qquad
\frac{\vartheta_1(p_\rho,\rho)}{\eta(\rho)}
=e^{\pi i/12}3^{1/4}e^{\pi/(6\sqrt3)}.
\]

Inserting the now fixed logarithms into β gives

\[
\beta^{\rm part}(z_1)
=-\frac12+i\left(\frac1{\sqrt3}-\frac3{2\pi}\log48\right),
\quad
\beta^{\rm part}(z_2)
=i\left(\frac32-\frac3\pi\log6\right).
\]

Finally, at ρ one has \(6(\operatorname{Im}\mu)^2/T=1/\sqrt3\), and at i it equals 3/2. Subtracting these terms proves precisely
\(D_{\rm part}(z_1)=-3\log48/(2\pi)\) and
\(D_{\rm part}(z_2)=-3\log6/\pi\).

## Result before comparison

The complete target statement, including the exact branches, follows. The phase argument uses unique real zeros on two entire vertical paths and positive product factors; it is not inferred from endpoint norms or from numerical agreement. The next step is to freeze this derivation, run a short newly written exact-arithmetic check of the lattice kernels and the rational inequality used in Step 3, and only then open the printed proof.
