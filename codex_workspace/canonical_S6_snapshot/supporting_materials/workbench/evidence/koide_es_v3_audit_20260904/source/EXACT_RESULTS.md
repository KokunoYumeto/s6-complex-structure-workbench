# Exact results in the Koide--Erdos--Straus extension

## 1. Orientation-correct complete divisor channels

For

\[
n\equiv1\pmod4,\qquad R\equiv3\pmod4,\qquad
0<R<n,\qquad \gcd(n,R)=1,
\]

put

\[
a=\frac{n+R}{4},\qquad N=na.
\]

For each \(\delta\mid n^2\), define

\[
\mathscr C_\delta(n,R)=
\{(u,v)>0:uv=a^2,\ R\mid4u+\delta\}.
\]

The source-compatible orientation is

\[
d=Ry-N=\frac{n^2}{\delta}u,
\qquad
e=Rz-N=\delta v.
\]

This gives a bijection

\[
\bigsqcup_{\delta\mid n^2}\mathscr C_\delta(n,R)
\longleftrightarrow
\{(y,z)>0:Ryz=N(y+z)\}.
\]

The exact inverse is

\[
\kappa=\gcd(Ry-N,n^2),\qquad
\delta=\frac{n^2}{\kappa},\qquad
u=\frac{Ry-N}{\kappa},\qquad
v=\frac{Rz-N}{\delta}.
\]

The denominator-exchange involution is

\[
(\delta,u,v)\longmapsto(n^2/\delta,v,u),
\]

and has no fixed state.

## 2. Complete terminal order

With

\[
T_\delta=\frac{4u+\delta}{R},\qquad
\sigma_\delta=
\begin{cases}1&\delta\equiv1\pmod4,\\-1&\delta\equiv3\pmod4,
\end{cases}
\]

set

\[
\ell_2=\sigma_\delta,
\quad
\ell_0=\frac{T_\delta+\sigma_\delta}{4},
\quad
\ell_1=u-\frac{R-3}{4}T_\delta.
\]

Then

\[
12\ell_0-4\ell_1-3\ell_2=\delta,
\]

and

\[
\begin{pmatrix}1&-(R-3)/4\\0&1\end{pmatrix}
\begin{pmatrix}R&-u\\4&-T_\delta\end{pmatrix}
=
\mathsf R_\delta
=
\begin{pmatrix}3&-\ell_1\\4&-T_\delta\end{pmatrix}.
\]

Thus

\[
\det\mathsf R_\delta=-\delta,
\qquad
\operatorname{SNF}(\mathsf R_\delta)=\operatorname{diag}(1,\delta).
\]

Complementary denominator orientations have terminal orders
\(\{\delta,n^2/\delta\}\).

## 3. Exact Fourier channel count

Write

\[
a=\prod_{q^e\parallel a}q^e,
\qquad
u=a\prod_{q^e\parallel a}q^{\beta_q},
\quad -e\le\beta_q\le e.
\]

The channel condition is

\[
\prod q^{\beta_q}\equiv-\delta n^{-1}\pmod R.
\]

For characters of \((\mathbb Z/R\mathbb Z)^\times\),

\[
C_\delta(n,R)
=
\frac1{\varphi(R)}
\sum_\chi
\overline{\chi(-\delta n^{-1})}
\prod_{q^e\parallel a}
\sum_{\beta=-e}^e\chi(q)^\beta.
\]

The unordered total is the corresponding divisor-order sum divided by two.

## 4. Primitive projective and Lorentz morphisms

The unique factor coordinates are

\[
u=r^2s,\qquad a=rst,\qquad v=st^2,
\qquad\gcd(r,t)=1.
\]

The channel condition is exactly

\[
R\mid nr+\delta t.
\]

The projective map is

\[
[r:t]\longmapsto[nr:\delta t],
\]

and the channel is the inverse image of \([1:-1]\).

The shell matrix is obtained from the rank-one matrix

\[
\Gamma=s\begin{pmatrix}r^2&rt\\rt&t^2\end{pmatrix}
\]

by the congruence

\[
\Sigma_{n,\delta}
=M_{n,\delta}\Gamma M_{n,\delta}^{\mathsf T},
\qquad
M_{n,\delta}=\operatorname{diag}(n/\sqrt\delta,\sqrt\delta).
\]

In Lorentz coordinates this is the integral similitude

\[
\rho_{n,\delta}=
\begin{pmatrix}
(n^2/\delta+\delta)/2&0&(n^2/\delta-\delta)/2\\
0&n&0\\
(n^2/\delta-\delta)/2&0&(n^2/\delta+\delta)/2
\end{pmatrix},
\]

with

\[
\rho_{n,\delta}^{\mathsf T}\operatorname{diag}(1,-1,-1)
\rho_{n,\delta}=n^2\operatorname{diag}(1,-1,-1),
\qquad
\det\rho_{n,\delta}=n^3.
\]

Its rapidity is \(\log(n/\delta)\); complementary channels have opposite
rapidities.

## 5. Prime saturation on every primitive ray

For every primitive positive ray \([r:t]\), every modulus \(M\) divisible by
four, and every reduced class \(c\equiv1\pmod4\), an explicit reduced prime
progression is constructed whose sufficiently large primes all have exterior
Erdos--Straus certificates on that exact ray. Its relative density inside the
class \(c\pmod M\) is a positive explicit number
\(\varphi(M)/\varphi(Q)\).

In particular the result applies to all 48 reduced hard classes
\(c\equiv1\pmod{12}\) modulo 840.

## 6. Density one on the single diagonal ray

For \(p\equiv1\pmod4\) prime and any divisor

\[
R\mid\frac{p+1}{2},\qquad R\equiv3\pmod4,
\]

put

\[
s=\frac{p+R}{4},\qquad k=\frac{p+1}{R}.
\]

Then

\[
\frac4p=\frac1s+\frac1{sk}+\frac1{psk}.
\]

For a finite set of primes \(q\equiv3\pmod4\), \(q\nmid M\), the relative
density in a reduced class \(c\pmod M\) of primes detected by at least one
such \(q\) is

\[
1-\prod_q\frac{q-2}{q-1}.
\]

Exhausting the primes \(q\equiv3\pmod4\) makes this density tend to one.
Thus the single Koide ray \([1:1]\) captures relative density one in every
admissible prime progression.

## 7. Exact individual-prime multiplicity on the diagonal ray

Let \(m_p=(p+1)/2\). The number of exterior selector states on \([1:1]\) is

\[
\nu_{\mathrm{diag}}(p)
=
\#\{R\mid m_p:R\equiv3\pmod4\}
=
\frac12\left(\tau(m_p)-\sum_{d\mid m_p}\chi_4(d)\right).
\]

If

\[
m_p=\prod_{q\equiv1(4)}q^{e_q}
    \prod_{r\equiv3(4)}r^{f_r},
\]

then

\[
\nu_{\mathrm{diag}}(p)=\frac12
\left[
\prod_q(e_q+1)\prod_r(f_r+1)
-
\prod_q(e_q+1)\prod_r\epsilon(f_r)
\right],
\]

where \(\epsilon(f)=1\) for even \(f\) and zero for odd \(f\).
Consequently

\[
\nu_{\mathrm{diag}}(p)=0
\Longleftrightarrow
\text{every prime divisor of }(p+1)/2\text{ is }1\pmod4.
\]

At \(p=109\), the two residuals \(R=11,55\) give

\[
\frac4{109}=\frac1{30}+\frac1{300}+\frac1{32700}
            =\frac1{41}+\frac1{82}+\frac1{8938}.
\]

## 8. Universal diagonal divisor identity

For a general divisor channel on \([1:1]\), the exact criterion is

\[
R\mid n+\delta.
\]

With \(k_\delta=(n+\delta)/R\) and \(s=(n+R)/4\),

\[
\frac4n
=
\frac1s+\frac1{s k_\delta}
+
\frac1{s n k_\delta/\delta}.
\]

Under \(\delta\mapsto n^2/\delta\), the final two denominators are exchanged.

## 9. Bezout opening and exact period discriminant

For a primitive ray vector \(\mathbf v=(r,t)^{\mathsf T}\), choose
\(\mathbf w=(x,y)^{\mathsf T}\) with \(ry-tx=1\). Define

\[
A_{\delta,\mathbf w}
=\delta\mathbf v\mathbf v^{\mathsf T}
 -\mathbf w\mathbf w^{\mathsf T}.
\]

Then

\[
\det A_{\delta,\mathbf w}=-\delta.
\]

A centered companion makes \((A_{\delta,\mathbf w})_{11}>0\). The exact raw
period triple

\[
(T_{\rm raw},M_{\rm raw},B_{\rm raw})
=\left(A_{11},A_{12}/\sqrt6,A_{22}\right)
\]

satisfies

\[
T_{\rm raw}B_{\rm raw}-6M_{\rm raw}^2=-\delta,
\qquad
B_{\rm raw}-\frac{6M_{\rm raw}^2}{T_{\rm raw}}
=-\frac\delta{A_{11}}<0.
\]

Thus the opening removes the rank defect and defines a regular ambient period
torus. It does not, by itself, prove membership in the global S6 period map.

## 10. Exact opening--terminal morphism

For the terminal matrix \(\mathsf R_\delta\), the paper gives explicit
matrices \(P_0,Q_0,L_A,R_A\in\operatorname{GL}_2(\mathbb Z)\) such that

\[
\mathsf R_\delta
=P_0^{-1}L_A A_{\delta,\mathbf w}R_AQ_0^{-1}.
\]

This is a coordinate-level integral left--right morphism, not merely a
matching determinant or Smith normal form.

## 11. Defect-one Koide map and exact rational separation

The orthogonal--homothetic map

\[
\mathfrak K_\delta(A)
=
\mathcal F^{-1}\left(
\frac{((A_{11}+A_{22})/2,A_{12},(A_{11}-A_{22})/2)}
     {\sqrt{3\delta}}
\right)
\]

satisfies

\[
Q_K(\mathfrak K_\delta(A))=-\frac13,
\qquad
\Delta(\mathfrak K_\delta(A))=-1.
\]

The extension proves the sharper result

\[
A\in\operatorname{Sym}_2(\mathbb Q),\quad
\det A=-\delta<0
\quad\Longrightarrow\quad
\mathfrak K_\delta(A)\notin\mathbb Q^3.
\]

Hence this exact map is disjoint from the integral defect-one orbit counted in
the Koide counting theorem. A transfer to that orbit requires a different
explicit morphism.

## 12. Exact remaining boundary

The extension proves saturation in the ray direction, including density one on
one ray. Erdős--Straus is the opposite quantifier:

\[
\forall p\quad\exists\text{ a ray and residual certificate for that }p.
\]

A density-zero exceptional prime set is not excluded by the results above.
