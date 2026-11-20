# P1.4: fresh whole-target derivation before the receiving proof

## 0. Input, exposure, and exact meaning of the Hodge bundle

The only target-specific source read before this derivation is `audit_root/packets/P14_statement_and_raw_pencil_08.tex`, whose supplied SHA256 is `3acaa9983ff072c4c6f80c5e95807f7fecc6f442cfa5edf5a15b893c44b21557`. It contains the literal pencil

\[
y^2=x^5+\lambda^3x+\lambda^4
\tag{0.1}
\]

and the expected statement, including the nodal parameter, root orders, and splitting. Thus the expected answer was exposed. No receiving P1.4 proof, prior producer, or earlier P1.4 check record was read or imported.

The derivation below constructs the compact family explicitly, including its smooth models on the two root charts and its nodal fibre on the ordinary base chart. Its Hodge bundle means the pushforward of the **relative dualizing line bundle of this stable family**, with the indicated deck descent on the root orbifold. This is also the canonical extension of the ordinary bundle of holomorphic differentials across the single nodal fibre. The extension at that point is proved explicitly below; an arbitrary extension of the punctured-base vector bundle is not used.

The new certificate is `p14_exact_certificate.py`, with output `p14_exact_certificate.json`. It performs exact polynomial, cyclotomic, and rational-divisor calculations from (0.1), using no prior producer.

## 1. Compactification and the unique nonzero finite singular fibre

For a finite parameter put

\[
f_\lambda(x)=x^5+\lambda^3x+\lambda^4.
\]

The standard odd-degree compactification is the finite double cover of the `x`-line's projective completion with branch section

\[
X^5Z+\lambda^3XZ^5+\lambda^4Z^6
\]

of `O(6)`. Equivalently its two affine charts are

\[
y^2=x^5+\lambda^3x+\lambda^4,
\qquad v^2=u+\lambda^3u^5+\lambda^4u^6,
\]

with `u=1/x`, `v=y/x^3`. At the unique point over infinity, `(u,v)=(0,0)`, the derivative of the right side with respect to `u` is one. This point is smooth for every finite parameter. The double cover is finite flat over the projective line, hence proper and flat over the parameter chart. Away from repeated branch roots it has six simple branch points, including infinity. The double-cover Euler characteristic formula gives `2g-2=2(-2)+6=2`, so its smooth fibres have genus two.

The exact discriminant is

\[
\operatorname{disc}_x f_\lambda
=\lambda^{15}(256+3125\lambda).
\tag{1.1}
\]

Thus the only singular finite fibre with `lambda != 0` is at

\[
\lambda_*=-\frac{256}{3125}.
\]

The equations for a repeated affine root give

\[
5x^4+\lambda^3=0,
\qquad \frac45\lambda^3x+\lambda^4=0,
\]

so its repeated root is

\[
r=-\frac54\lambda_*=\frac{64}{625}.
\]

The complete factorization there is

\[
f_{\lambda_*}(x)=(x-r)^2q(x),
\quad q(x)=x^3+2rx^2+3r^2x+4r^3.
\tag{1.2}
\]

Here `q(r)=10r^3 != 0` and `disc(q)=-200r^6 != 0`. Therefore there is exactly one double root and all three remaining roots are simple. Locally at `(r,0)`, a holomorphic square root of `q` turns the equation into

\[
\bigl(y-(x-r)\sqrt{q(x)}\bigr)
\bigl(y+(x-r)\sqrt{q(x)}\bigr)=0.
\]

The two linear factors have independent differentials, proving that the singularity is an ordinary node. In addition,

\[
\frac{\partial f}{\partial\lambda}(r,\lambda_*)
=\frac14\lambda_*^3\ne0.
\tag{1.3}
\]

Thus the total surface is smooth at the node and the parameter gives a transverse one-parameter smoothing. The normalization is the smooth genus-one curve `z^2=q(x)`, with the two points over `x=r` identified. The cubic in (1.2) is not a square in the function field, so the nodal fibre is irreducible. It is a stable arithmetic-genus-two curve.

## 2. Good reduction at zero: exact model and deck action

Use the root chart and change of fibre coordinates

\[
\lambda=t^8,\qquad x=t^6X,\qquad y=t^{15}Y.
\tag{2.1}
\]

For `t != 0` this is an isomorphism, with inverse `X=t^{-6}x`, `Y=t^{-15}y`. Substitution gives

\[
Y^2=X^5+X+t^2.
\tag{2.2}
\]

Its central fibre `Y^2=X^5+X` is smooth: its polynomial discriminant is 256. In fact the chart discriminant is `256+3125t^8`. The chart at the point over infinity is

\[
V^2=U+U^5+t^2U^6,
\qquad U=1/X,\quad V=Y/X^3,
\]

whose derivative in `U` at `(U,V)=(0,0)` is one. Hence, on a sufficiently small disk, these compact double-cover charts form a proper smooth genus-two family over the entire root disk.

Let `zeta` be a primitive eighth root of unity. The exact deck map preserving the original variables in (2.1) is

\[
\tau_0:(X,Y,t)\longmapsto(\zeta^2X,\zeta Y,\zeta t).
\tag{2.3}
\]

Its transformed equation is `zeta^2` times (2.2), and `t^8`, `t^6X`, `t^{15}Y` are unchanged. On the infinity chart it is

\[
(U,V,t)\longmapsto(\zeta^{-2}U,\zeta^3V,\zeta t),
\]

so it extends to the compact family. The two central holomorphic differentials

\[
\alpha_0=dX/Y,\qquad\beta_0=X\,dX/Y
\]

transform by

\[
\tau_0^*\alpha_0=\zeta\alpha_0,
\qquad\tau_0^*\beta_0=\zeta^3\beta_0.
\tag{2.4}
\]

In particular the action on first cohomology has exact order eight. The fourth power is already the hyperelliptic involution on the central fibre: it fixes `X` and negates `Y`.

## 3. Good reduction at infinity: exact model and deck action

Put `mu=1/lambda` and use

\[
\mu=t^5,\qquad\lambda=t^{-5},\qquad
x=t^{-4}X,\qquad y=t^{-10}Y.
\tag{3.1}
\]

The inverse over the punctured disk is `X=t^4x`, `Y=t^{10}y`. The equation becomes

\[
Y^2=X^5+tX+1.
\tag{3.2}
\]

Its discriminant is `3125+256t^5`, nonzero at zero. The infinity chart is

\[
V^2=U+tU^5+U^6,
\]

and again its derivative in `U` at the point over infinity is one. Thus this is another proper smooth genus-two family over a sufficiently small full root disk.

For a primitive fifth root `xi`, the exact deck map is

\[
\tau_\infty:(X,Y,t)\longmapsto(\xi^4X,Y,\xi t).
\tag{3.3}
\]

It preserves (3.2) and the original `x,y,mu`. On the second chart it is `(U,V,t)->(xi U,xi^3 V,xi t)`. The central forms

\[
\alpha_\infty=dX/Y,\qquad\beta_\infty=X\,dX/Y
\]

have characters

\[
\tau_\infty^*\alpha_\infty=\xi^4\alpha_\infty,
\qquad\tau_\infty^*\beta_\infty=\xi^3\beta_\infty.
\tag{3.4}
\]

The first character has exact order five.

## 4. Minimality of the two ramification orders

The displayed good models prove the existence of good reduction after orders eight and five. Their finite central deck actions also prove minimality.

Here is the precise monodromy comparison. A proper smooth family over a disk admits a smooth fibrewise trivialization obtained by a horizontal distribution and radial parallel transport. The horizontal distribution can be averaged over the finite deck group, so its radial transport is equivariant. In that trivialization the deck map on the central fibre is exactly (2.3) or (3.3). A positively oriented loop on the original parameter disk lifts to a path from `t` to `zeta t` or `xi t`; return to the original marked fibre uses the inverse deck identification. The resulting homology monodromy is therefore conjugate to the inverse of the central deck action. Its order is eight at zero and five at infinity, independently of the inverse convention.

The nontriviality assertions here are detected on the actual holomorphic differential subspaces by (2.4) and (3.4). A nonzero holomorphic differential on a compact smooth curve has a nonzero de Rham class, since its pairing with its complex conjugate has nonzero integral. Thus these primitive-root eigenvalues are genuine first-cohomology eigenvalues, not merely coefficients of formal expressions.

Ramification of order `m` replaces a peripheral monodromy by its `m`th power. Good reduction supplies a proper smooth family on the full disk; its transport around a contractible small loop is isotopic to the identity. Its first-cohomology monodromy is therefore the identity. The actual order-eight and order-five actions give the divisibility requirements

\[
8\mid m\quad\text{at zero},\qquad 5\mid m\quad\text{at infinity}.
\]

Every positive multiple of the displayed orders gives good reduction by pullback of (2.2) or (3.2). Consequently the good-reduction root orders are exactly the positive multiples of eight and five, respectively, and their minima are eight and five.

## 5. Canonical extension of the Hodge bundle across the node

Let `U=P^1\{0,infinity}`. The compact double-cover family over `U` is smooth except for the single nodal fibre in Section 1. Its relative dualizing line can be computed directly, including at that node.

On the affine equation its generator is the relative residue

\[
\frac{dx}{2y}.
\]

This expression denotes the residue generator of the dualizing module of the hypersurface `y^2-f_lambda(x)=0`. The hypersurface adjunction construction defines it also where both fibre derivatives vanish. On the second chart its generator is `du/(2v)`, and the exact transition is

\[
\frac{dx}{2y}=-u\,\frac{du}{2v}.
\tag{5.1}
\]

Absorbing the constant minus sign in the second trivialization identifies this line with the pullback of `O(1)` on the projective `x`-line. This also follows directly from the double-cover algebra

\[
p_*\mathcal O_{\mathcal C}=\mathcal O\oplus\mathcal O(-3).
\]

The transition (5.1) gives

\[
p_*\omega_{\mathcal C/U}
=\mathcal O(1)\oplus\mathcal O(-2).
\tag{5.2}
\]

Taking sections over the projective line, `O(1)` has basis `1,x` on the affine chart, while `O(-2)` has no section. These statements follow from the two-chart Laurent-polynomial calculation over the parameter ring, so they remain valid at the nodal parameter. It follows that

\[
\pi_*\omega_{\mathcal C/U}
=\mathcal O_U\,\omega_1\oplus\mathcal O_U\,\omega_2,
\qquad
\omega_1=dx/y,\quad\omega_2=x\,dx/y.
\tag{5.3}
\]

Thus (5.3) is a holomorphic frame across `lambda_*`, not only away from it.

For an explicit fibrewise check, use the normalization `z^2=q(x)` in (1.2). The pullbacks are

\[
\omega_1=\frac{dx}{(x-r)z},\qquad
\omega_2=r\omega_1+\frac{dx}{z}.
\]

At the two points over `x=r`, the residues of `omega_1` are `1/sqrt(q(r))` and its negative. The differential `dx/z` is the nonzero regular differential of the elliptic normalization. They therefore supply the two independent dualizing differentials of the node, with the prescribed opposite residues. This agrees with the canonical residue construction and shows explicitly why no extra zero, pole, or twist at the nodal base point appears in either Hodge line.

The same construction on the two smooth root charts gives local frames `(alpha_0,beta_0)` and `(alpha_infinity,beta_infinity)`. Gluing their families by the explicit punctured-chart isomorphisms gives the stable family on the root orbifold with orders eight and five. Its relative dualizing pushforward is the Hodge bundle used in the remainder of the proof.

## 6. Exact line divisors and the global splitting

When differentiating along a fibre, the base parameter is constant. Substituting (2.1) gives the exact transition equations

\[
\omega_1=t^{-9}\alpha_0,\qquad
\omega_2=t^{-3}\beta_0.
\tag{6.1}
\]

Substituting (3.1) gives

\[
\omega_1=t^6\alpha_\infty,\qquad
\omega_2=t^2\beta_\infty.
\tag{6.2}
\]

These are diagonal transitions, with the holomorphic frames from Section 5 on the remaining ordinary chart, including the node. They define global line subbundles `L_1,L_2` and an actual bundle isomorphism

\[
L_1\oplus L_2\longrightarrow\mathcal H.
\]

It sends the ordered local line frames to the displayed ordered Hodge frames. Its matrix is the identity on every such chart; the inverse sends a differential to its two coefficients in those frames. The maps are compatible with (6.1)--(6.2) and the deck characters (2.4), (3.4).

On the root orbifold, a coarse divisor coefficient `a/8` at zero means valuation `a` on its order-eight root chart, and a coefficient `b/5` at infinity means valuation `b` on its order-five root chart. Hence the meromorphic sections `omega_1,omega_2` have divisors

\[
\operatorname{div}_{L_1}(\omega_1)
=-\frac98[0]+\frac65[\infty],
\qquad
\operatorname{div}_{L_2}(\omega_2)
=-\frac38[0]+\frac25[\infty].
\tag{6.3}
\]

There are no other divisor terms because (5.3) is a frame over all of `U`.

Define

\[
T=\mathcal O\left(\frac25[\infty]-\frac38[0]\right).
\]

The isomorphism `T -> L_2` sends its canonical meromorphic section to `omega_2`. In the zero root chart the local frame of `T` is `t^3` and maps to `beta_0=t^3 omega_2`; in the infinity chart it is `t^{-2}` and maps to `beta_infinity=t^{-2}omega_2`. Their characters are respectively `zeta^3` and `xi^{-2}=xi^3`, exactly those of the target frames.

There is also an exact isomorphism `T^3 -> L_1`: it sends the cube of that meromorphic section to `omega_1`. On the zero chart it sends the frame `t^9` to `alpha_0`; on the infinity chart it sends `t^{-6}` to `alpha_infinity`. The respective character equalities are

\[
\zeta^9=\zeta,\qquad\xi^{-6}=\xi^4.
\]

These explicit arrows and their inverses identify the line bundles, rather than only their degrees. Therefore

\[
\boxed{\mathcal H=T^3\oplus T}
\]

and `dx/y` is the stated meromorphic generator of the `T^3` line. Finally

\[
\deg T=\frac25-\frac38=\frac{16-15}{40}=\frac1{40}.
\]

## 7. Certificate and status before the freeze

The exact certificate records forty assertions. They include the complete discriminant and nodal factorization, the nonzero smoothing derivative, both good-chart substitutions and discriminants, smoothness of their points over infinity, both deck equations modulo the relevant cyclotomic polynomial, invariance of the original coordinates, the exact orders detected on differentials, the cubic character adapters, and the rational divisor/degree identities.

The proof above supplies the geometric steps that those polynomial identities alone do not assert: compact smooth good models, the central-deck-to-monodromy comparison, minimal ramification, and the canonical relative-dualizing extension across the nodal fibre. It also constructs both directions of the Hodge line-bundle isomorphisms.

No additional target-specific input was required. The full derivation is complete for the canonical Hodge bundle just specified. A receiving statement that uses the term Hodge bundle on the root orbifold without specifying its extension over the nodal point should make this canonical relative-dualizing scope explicit. The receiving proof and previous P1.4 code or records remain unread at this freeze.
