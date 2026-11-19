# A fresh coefficient-atlas attempt: regular coefficients and the cusp correction

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family. Phase: `S6_SERIES_GRIND`. This attempt was made after the target statement and its existing operator proof had been read. It is a new explicit calculation, not another statement-first proof credit and not a solution of `inv:C3.8`.

## 1. Exact map from the original marking

Write the real Betti coordinates in the original order as
`r=(r_gamma,r_u,r_w,r_delta)`. Set

\[
 q_B=(r_u,r_\gamma)^t,\qquad p_B=(r_w,r_\delta)^t,
 \quad T=\begin{pmatrix}\tau&6\mu\\\mu&\beta\end{pmatrix},
 \quad D=\operatorname{diag}(1,6).
\]

The actual coordinate map is
\[
 \zeta=p_B+Tq_B
 =\begin{pmatrix}6\mu&\tau&1&0\\\beta&\mu&0&1\end{pmatrix}r.
\]
Its real inverse on the admissible domain is
\[
 Y=\operatorname{Im}T,quad v=\operatorname{Im}\zeta,
 \quad q_B=Y^{-1}v,\quad p_B=\operatorname{Re}\zeta-
 (\operatorname{Re}T)Y^{-1}v.
\]
Here `det Y=y r-6m^2=y Delta<0`, with `y=Im tau`, `m=Im mu`, `r=Im beta`. These formulas retain the original ordered marking. They are not an identification of a new unspecified period convention.

The fixed real two-form is exactly
\[
 \eta_B=dq_B^tD\wedge dp_B
 =dr_u\wedge dr_w+6\,dr_\gamma\wedge dr_\delta.
\]

## 2. All horizontal coefficients on a regular torus chart

On a simply connected regular base chart, define
\[
 S=DY^{-1}=\frac1{yr-6m^2}
 \begin{pmatrix}r&-6m\\-6m&6y\end{pmatrix},
 \quad \theta=d\zeta-(dT)q_B.
\]
Since `DT` and `DY` are symmetric, `S` is symmetric. Direct differentiation of the inverse coordinate map gives
\[
 \partial q_B=\frac1{2i}Y^{-1}\theta,
 \qquad \bar\partial q_B=-\frac1{2i}Y^{-1}\bar\theta.
\]
With the real function
\[
 \varphi=2\pi v^tDY^{-1}v=2\pi q_B^tDYq_B,
\]
one obtains the exact total-space form
\[
 Q_{\rm sf}=-\frac{i}{2}\theta^t S\wedge\bar\theta
 =-\frac{i}{2\pi}\partial\bar\partial\varphi.
\]
This includes all horizontal terms. For a local coordinate `t` and `K=dT/dt`, its coefficient matrix in `(dt,dzeta_1,dzeta_2)` is
\[
 -\frac i2
 \begin{pmatrix}-Kq_B&I_2\end{pmatrix}^{t}
 S
 \begin{pmatrix}-\bar Kq_B&I_2\end{pmatrix}.
\]
Equivalently, the four terms are the fibre term, the two mixed terms, and
`-(i/2) q_B^t K^t S bar K q_B dt wedge dbar t`. There is no omitted second derivative of `T`.

The same form equals the pullback of `eta_B` by the displayed real inverse. Indeed `theta=dp_B+T dq_B` and `D T=T^t D`; expansion gives the equality. It follows that this real form is de Rham closed. Its restriction to a fibre is precisely the printed invariant form
\[
 \frac{1}{2iy\Delta}
 \bigl(r\,d\zeta_1\wedge d\bar\zeta_1
 -6m\,d\zeta_1\wedge d\bar\zeta_2
 -6m\,d\zeta_2\wedge d\bar\zeta_1
 +6y\,d\zeta_2\wedge d\bar\zeta_2\bigr).
\]

For a lattice translation `(p_B,q_B)->(p_B+a,q_B+b)`, the coordinate map is `zeta->zeta+a+Tb`. Its differential adds `(dT)b`, while `q_B` adds `b`; hence `theta` is unchanged. This proves full coefficient descent, including the base derivatives.

For a linear marked monodromy, `zeta'=R(t)zeta`, `Pi'=R Pi A^{-1}`, and `r'=Ar`. Consequently
`dzeta'-(dPi')r'=R(dzeta-(dPi)r)`. The original two matrices satisfy `A_j^t E A_j=E`, where
\[
 E=\begin{pmatrix}0&0&0&6\\0&0&1&0\\0&-1&0&0\\-6&0&0&0\end{pmatrix}.
\]
Thus the regular form descends through the actual linear monodromies. On either finite root chart the affine action is `r->A_jr+v_j/m_j`; its constant translation also preserves `eta_B`. The form constructed in that root chart is therefore smooth and invariant through its central torus and descends through the free finite quotient. This statement concerns the local root representative. The logarithmic collar translation relating it to the middle representative must still be corrected; equality of the two local forms on that collar is not asserted.

## 3. An explicit holomorphic cocycle on the regular charts

For `lambda=(a,b)` in `Z^2+T Z^2`, use the factor
\[
 A_\lambda(\zeta,t)=
 \exp\bigl(2\pi i b^tD\zeta+\pi i b^tDTb\bigr).
\]
Its two-step cocycle defect in the logarithm is exactly `2pi i b^tD a'`, so the exponential cocycle holds. Its logarithmic differential is the holomorphic one-form
\[
 \alpha_\lambda=b^tD\,d\zeta+
 \tfrac12 b^tD(dT)b.
\]
The same defect is constant, hence these differentials satisfy the exact additive cocycle law. The metric coefficient `exp(varphi)` is compatible with these factors: its logarithm changes by `4pi b^tD v+2pi b^tDYb`, which cancels `log|A_lambda|^2`. Its first Chern form, with curvature `bar partial partial log h`, is the displayed `Q_sf`. This gives an evaluated regular-chart Čech representative as well as its smooth coefficients. It does not yet supply a Čech cocycle on the cusp charts.

## 4. The exact cusp obstruction for this attempted representative

Use the actual cusp coordinates of `mapsI:src:A.1.2`:
\[
 q=z_0z_1z_2,\qquad x_1=z_1,\quad x_2=z_2,
 \quad x_j=e^{2\pi i\zeta_j},
\]
and the exact bounded-unit period decomposition
\[
 \begin{pmatrix}6\mu&\tau\\\beta&\mu\end{pmatrix}
 =s\begin{pmatrix}0&1\\-1&0\end{pmatrix}+C(q),
 \qquad s=\frac{\log q}{2\pi i},
\]
where `C` is holomorphic and bounded at zero. For the positive real path
`z_0=z_1=z_2=epsilon`, let `T_0=-log(q)/(2pi)=-3log(epsilon)/(2pi)`.
Then `y=T_0+O(1)`, `r=-T_0+O(1)`, `m=O(1)`, and
\[
 S_{11}=\frac1{T_0}+O(T_0^{-2}).
\]
At this path the uniformly bounded coordinate tangent
`V=partial_{z_1}-partial_{z_0}` satisfies `dq(V)=0` exactly. Therefore
\[
 \theta_1(V)=\frac1{2\pi i\epsilon},\qquad
 \theta_2(V)=0,\qquad
 Q_{\rm sf}(V,\bar V)=-\frac{iS_{11}}{8\pi^2\epsilon^2}.
\]
Its absolute value is asymptotic to `1/(8pi^2 epsilon^2 T_0)` and diverges. All bounded holomorphic unit terms are retained in the `O(T_0^{-2})` correction. Thus this particular evaluated representative has no smooth extension even at that one triple point. A coordinate-independent smoothness assertion cannot be recovered by changing the bounded period terms.

## 5. A global real-form obstruction, with its exact scope

Suppose a real `(1,1)` form `Q` on the given `X` were `bar partial` closed and had the required fibre Dolbeault class. Reality implies `partial Q=overline{bar partial Q}=0`, so `dQ=0`. The established topology gives `H^2(X,R)=0`; hence `Q=dA` for a real one-form `A`.

Let `i:F->X` be a regular compact fibre. On `F`, the equality of Dolbeault classes gives `i^*Q-eta=bar partial B` for a `(1,0)` form `B`. Since `i^*Q` and `eta` are both `bar partial` closed, Stokes gives
\[
 \int_F(i^*Q)^2=\int_F\eta^2=-12.
\]
On the other hand `i^*Q=d(i^*A)` and
`(i^*Q)^2=d(i^*A wedge i^*Q)`, so the same integral is zero. This contradiction rules out a **real** global representative of the requested class. It does not rule out the established complex Dolbeault representative. Any successful global atlas must contain a nonreal correction whose `partial` differential accounts for this obstruction.

## 6. Remaining exact task

The outstanding cochain must simultaneously:

1. cancel the displayed cusp growth (and the corresponding coefficients on all translated toric charts);
2. preserve `bar partial Q=0` and the fibre class `eta`;
3. obey the full toric period factors and the two original logarithmic collar translations;
4. provide coefficients on the finite root quotients and all double/triple cusp strata.

The regular cocycle above, the finite affine invariance and the real-form obstruction do not construct that cochain. The atlas remains open. No body edit or new theorem is proposed from this partial attempt.
