# Independent targeted derivation before reading ari:C.1.1's proof

Recorded on 21 November 2026 UTC by GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH/provenance_inventory.

## Read scope before this derivation

I read only the target statement supplied in `work/records/S6_SERIES_PUBLISH_I_root_statement_intake.json`, and the definitions immediately preceding it in the frozen Paper I source. I have not opened the target's printed proof. Earlier provenance work exposed its citation in C.4.2, which uses the local expansion at the origin to fix a distribution constant. That exposure is recorded here; I do not claim ignorance of the statement's intended use. The source was also parsed mechanically for labels and references, without displaying the target proof.

The definitions are

\[
U_\tau(z)=\log N(z,\tau)
=\log\left|\frac{\vartheta_1(z,\tau)}{\eta(\tau)}\right|
-\frac{\pi(\operatorname{Im}z)^2}{T},\qquad T=\operatorname{Im}\tau,
\]

with theta variable of periods \(1,\tau\), and
\(U_\Lambda(z)=U_\tau(z/\omega)\) for
\(\Lambda=\omega(\mathbb Z+\tau\mathbb Z)\).

The target asserts the exact isogeny distribution identity, with no additive constant, and its resulting discriminant-scaled product over the nonzero kernel.

## Derivation

### 1. The constant normalization is zero mean

Put \(q=e^{2\pi i\tau}\) and \(z=x+s\tau\), with \(0<s<1\). The theta/eta product is

\[
\frac{\vartheta_1(z,\tau)}{\eta(\tau)}
=2q^{1/12}\sin(\pi z)
\prod_{n\ge1}(1-q^n e^{2\pi iz})(1-q^n e^{-2\pi iz}).
\]

For every coefficient \(a\) of modulus less than one,
\(\int_0^1\log|1-ae^{2\pi ix}|\,dx=0\): expand the holomorphic logarithm into its absolutely convergent power series and integrate each nonconstant Fourier mode. The factors above have moduli controlled by
\(e^{-2\pi T(n+s)}\), \(e^{-2\pi T(n-s)}\), and \(e^{-2\pi Ts}\); all are less than one. Also
\(\log|2\sin(\pi z)|=\pi Ts+\log|1-e^{2\pi iz}|\).
Termwise integration is justified on every closed substrip \(\epsilon\le s\le1-\epsilon\) by uniform product convergence. At the two ends the sole singularities are logarithmic and locally integrable. Therefore

\[
\int_0^1 U_\tau(x+s\tau)\,dx
=-\frac{\pi T}{6}+\pi Ts-\pi Ts^2
=-\pi T B_2(s).
\]

Since \(\int_0^1B_2(s)\,ds=0\), the integral of \(U_\tau\) against normalized Haar measure is zero. Scaling by \(\omega\) gives the same conclusion for every \(\Lambda\).

### 2. Pullback and kernel sum have the same distributional Laplacian

Write \(A\) and \(A'\) for the Euclidean areas of fundamental parallelograms of \(\Lambda\) and \(\Lambda'\). The logarithm of theta is harmonic off its simple zeros, and
\(\Delta\log|z|=2\pi\delta_0\). The Gaussian term has Laplacian \(-2\pi/A\) after lattice scaling. Thus, on \(\mathbb C/\Lambda\),

\[
\Delta U_\Lambda=2\pi\delta_0-\frac{2\pi}{A}.
\]

The index relation is
\(d=|\alpha|^2A/A'\).
The function \(U_{\Lambda'}(\alpha z)\) has a simple logarithmic singularity at each point of
\(K=\alpha^{-1}\Lambda'/\Lambda\), so its Laplacian is

\[
2\pi\sum_{v\in K}\delta_v-\frac{2\pi|\alpha|^2}{A'}
=2\pi\sum_{v\in K}\delta_v-\frac{2\pi d}{A}.
\]

The same formula holds for
\(\sum_{v\in K}U_\Lambda(z+v)\), because \(-K=K\).
Their difference consequently extends to a distributionally harmonic function on the compact torus, and hence is constant. Its mean is zero: translations preserve Haar measure, and the finite surjective group homomorphism \(z\mapsto\alpha z\) pushes normalized Haar measure to normalized Haar measure. Therefore the constant is zero:

\[
U_{\Lambda'}(\alpha z)=\sum_{v\in K}U_\Lambda(z+v).
\]

The cancellation holds at each logarithmic singularity. Both sides are locally integrable, so the equality has the stated distributional and locally integrable meaning there, as well as its ordinary pointwise meaning away from the kernel.

### 3. The origin coefficient is exactly the twelfth root of the Weierstrass discriminant

Differentiating the product in Step 1 at zero gives
\(\vartheta'_1(0,\tau)=2\pi\eta(\tau)^3\) in the period-one theta variable. Hence

\[
N_\Lambda(z)
=\frac{2\pi|\eta(\tau)|^2}{|\omega|}\,|z|
\bigl(1+O(|z|^2)\bigr).
\]

The lattice Weierstrass normalization is

\[
g_2(\Lambda)=\frac{4\pi^4}{3\omega^4}E_4(\tau),\qquad
g_3(\Lambda)=\frac{8\pi^6}{27\omega^6}E_6(\tau).
\]

Using \(E_4^3-E_6^2=1728\eta^{24}\), the scale is

\[
g_2^3-27g_3^2
=\frac{64\pi^{12}}{27\omega^{12}}\,1728\eta^{24}
=\left(\frac{2\pi}{\omega}\right)^{12}\eta^{24}.
\]

Thus
\(U_\Lambda(z)=\log|z|+\frac1{12}\log|\Delta_\Lambda|+O(|z|^2)\).
The coefficient is \(1/12\); the theta derivative is taken in the period-one variable, which supplies the factor \(2\pi\).

### 4. Taking the limit at the identity proves the kernel product

In the distribution identity let \(z\to0\), subtract the \(v=0\) term and use Step 3. All other terms are continuous because their kernel points are nonzero on the torus. This yields

\[
\sum_{0\ne v\in K}U_\Lambda(v)
=\log|\alpha|+\frac1{12}\log\left|
\frac{\Delta_{\Lambda'}}{\Delta_\Lambda}\right|.
\]

Exponentiation gives exactly the asserted product. For an endomorphism of the same elliptic curve the discriminant ratio is one. For degree one the empty product also checks the scaling: \(\Lambda'=\alpha\Lambda\) implies
\(\Delta_{\Lambda'}=\alpha^{-12}\Delta_\Lambda\), making the right-hand side one.

## Result before comparison

The statement follows with the specified normalization, sign, complex absolute value and discriminant scale. No numerical computation is required in this argument. This file is to be frozen before opening the printed proof; subsequent comparison belongs in a separate record.
