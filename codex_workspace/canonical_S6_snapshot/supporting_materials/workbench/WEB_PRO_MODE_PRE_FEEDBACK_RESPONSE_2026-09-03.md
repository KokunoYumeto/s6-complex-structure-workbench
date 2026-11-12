# Inbound ChatGPT Pro-mode response before local feedback

- Received in this Codex task: 2026-09-03 (Europe/Berlin).
- Temporal status: this response was produced before ChatGPT Pro mode received `WEB_PRO_MODE_FEEDBACK.md`.
- Evidentiary status: inbound source material for independent checking; inclusion is not endorsement.
- Scope correction: the finite-cover calculation below is a valid ancillary
  theorem for an altered cusp family, but it does not answer the requested
  native \(S^{12}/S^{24}\) sphere-carrier problem. The current cover-free
  construction from the unmodified \(T^2\times\mathbb R^2\) quotient is stated
  in [WEB_PRO_MODE_FEEDBACK.md](WEB_PRO_MODE_FEEDBACK.md).

## Verbatim response supplied by the user
Yes. There are three exact constructions, and one of them directly repairs the \\(T^{2}\times\mathbb R^{2}\\) limitation without changing the Euclidean metric:

1\. the universal cover of every fibre is already \\(\mathbb R^{4}\\), but it retains only the periodic field sector when pulled back from the torus;
2\. a monodromy-compatible sequence of finite covers unrolls the two remaining compact directions and converges locally to the full \\(\mathbb R^{4}\\);
3\. doubling the expanding two-dimensional quotient gives another four-dimensional decompactification, but it uses two copies and discards the compact subtorus.

The second construction is the useful one.

The source data used below are the monodromy matrix in Proposition 1, the cusp lattices in Theorem 2, the period matrix in Proposition 9, and the cusp expansion in equation (2.5a) of the supplied [Alpöge–Fable \\(S^6\\) proof-audit archive]\(sandbox:/mnt/data/S6\_Annotated\_Mathematical\_Proof\_Audit\_\_\_Public\_Working\_Edition%20%2822%29%281%29.zip). The calculation does not use the theorem identifying the completed threefold with \\(S^{6}\\).

\## 1. A fixed torus maps from \\(\mathbb R^{4}\\), not onto it

For a regular fibre, let

$$
F\_T=\mathbb R^{4}/\mathsf P\_T\mathbb Z^{4},
$$

where

$$
\mathsf P\_T=
\begin{pmatrix}
6\operatorname{Re}\mu\_T&
\operatorname{Re}\tau\_T&
1&0\\\\
6\operatorname{Im}\mu\_T&
\operatorname{Im}\tau\_T&
0&0\\\\
\operatorname{Re}\beta\_T&
\operatorname{Re}\mu\_T&
0&1\\\\
\operatorname{Im}\beta\_T&
\operatorname{Im}\mu\_T&
0&0
\end{pmatrix}.
$$

There is an exact universal covering morphism

$$
q\_T:\mathbb R^{4}\longrightarrow F\_T,
\qquad
x\longmapsto[x],
$$

with

$$
\ker q\_T=\mathsf P\_T\mathbb Z^{4}.
$$

Equivalently, in complex coordinates \\(\mathbb C^{2}\cong\mathbb R^{4}\\),

$$
q\_T:\mathbb C^{2}\longrightarrow
\mathbb C^{2}/\Pi\_T\Lambda
$$

is holomorphic.

There is no continuous surjection \\(F\_T\to\mathbb R^{4}\\): the image of compact \\(F\_T\\) under a continuous map is compact, whereas \\(\mathbb R^{4}\\) is not. There is also no continuous embedding \\(F\_T\hookrightarrow\mathbb R^{4}\\): invariance of domain would make its image open in \\(\mathbb R^{4}\\), while compactness would make it compact; no nonempty open subset of \\(\mathbb R^{4}\\) is compact.

Thus one fixed compact fibre cannot literally be identified with \\(\mathbb R^{4}\\). The correct operations are covering and decompactification.

\## 2. Why the native cusp stops at \\(T^{2}\times\mathbb R^{2}\\)

The third and fourth columns of \\(\mathsf P\_T\\) are independent of \\(T\\):

$$
\mathsf P\_T\widehat w=
\begin{pmatrix}1\\\0\\\0\\\0\end{pmatrix},
\qquad
\mathsf P\_T\widehat\delta=
\begin{pmatrix}0\\\0\\\1\\\0\end{pmatrix}.
$$

Consequently, every native fibre contains the fixed real subtorus

$$
K\_T=
\frac{
\mathbb R\langle e\_1,e\_3\rangle
}{
\mathbb Z\langle e\_1,e\_3\rangle
}
\cong T^{2},
$$

whose two generating geodesics both have Euclidean length \\(1\\).

In particular,

$$
\operatorname{sys}(F\_T)\leq1,
\qquad
\operatorname{inj}(F\_T)\leq\frac12
$$

for every \\(T\\). This is an exact obstruction to a native pointed limit \\(\mathbb R^{4}\\): the two length-one loops never disappear.

Let

$$
\rho:\mathbb R^{4}\longrightarrow\mathbb R^{2},
\qquad
\rho(x\_1,x\_2,x\_3,x\_4)=(x\_2,x\_4).
$$

The image of the period lattice is

$$
\rho(\mathsf P\_T\mathbb Z^{4})
\=
B\_T\mathbb Z^{2},
$$

where

$$
B\_T=
\begin{pmatrix}
6\operatorname{Im}\mu\_T&
\operatorname{Im}\tau\_T\\\\
\operatorname{Im}\beta\_T&
\operatorname{Im}\mu\_T
\end{pmatrix}.
$$

Therefore \\(\rho\\) descends to

$$
\pi\_T:F\_T\longrightarrow
Q\_T:=\mathbb R^{2}/B\_T\mathbb Z^{2},
\qquad
[x]\longmapsto[(x\_2,x\_4)].
$$

Its kernel is exactly \\(K\_T\\). Indeed, if \\(\pi\_T([x])=0\\), then

$$
(x\_2,x\_4)=
B\_T
\begin{pmatrix}a\\\b\end{pmatrix}
$$

for some \\(a,b\in\mathbb Z\\). Subtracting \\(a\mathsf P\_T\widehat\gamma+
b\mathsf P\_T\widehat u\\) leaves a vector in
\\(\mathbb R\langle e\_1,e\_3\rangle\\), proving \\([x]\in K\_T\\).

Thus there is an exact sequence of real tori

$$
0\longrightarrow K\_T
\longrightarrow F\_T
\xrightarrow{\ \pi\_T\ }
Q\_T
\longrightarrow0.
$$

Along the radial cusp, write

$$
t\_c=e^{-2\pi T},\qquad
\tau\_T=iT+h(t\_c),\qquad
\mu\_T=\mu(t\_c),\qquad
\beta\_T=b(t\_c)-iT-h(t\_c).
$$

Then

$$
B\_T
\=
T
\begin{pmatrix}
0&1\\\\
-1&0
\end{pmatrix}
\+
\begin{pmatrix}
6\operatorname{Im}\mu(t\_c)&
\operatorname{Im}h(t\_c)\\\\
\operatorname{Im}b(t\_c)-\operatorname{Im}h(t\_c)&
\operatorname{Im}\mu(t\_c)
\end{pmatrix}.
$$

The second matrix remains bounded as \\(T\to\infty\\). Therefore \\(Q\_T\\) decompactifies to \\(\mathbb R^{2}\\), while \\(K\_T\\) remains a unit \\(T^{2}\\). This gives the native limit

$$
F\_T\longrightarrow T^{2}\times\mathbb R^{2}.
$$

The cusp monodromy explains this decomposition exactly. In the ordered lattice basis

$$
(\widehat\gamma,\widehat u,\widehat w,\widehat\delta),
$$

the source monodromy is

$$
M\_0=
\begin{pmatrix}
1&0&0&0\\\\
0&1&0&0\\\\
0&1&1&0\\\\
-1&0&0&1
\end{pmatrix}.
$$

Writing \\(M\_0=I+R\\),

$$
R(a,b,c,d)^{\mathsf T}
\=
(0,0,b,-a)^{\mathsf T},
\qquad
R^{2}=0.
$$

Hence

$$
\ker R=\operatorname{im}R
\=
\mathbb Z\langle\widehat w,\widehat\delta\rangle.
$$

These are precisely the two compact lattice directions. The quotient

$$
\overline\Lambda
\=
\Lambda/
\mathbb Z\langle\widehat w,\widehat\delta\rangle
$$

has trivial cusp monodromy, because \\(M\_0-I\\) takes values entirely in the sublattice being divided out.

\## 3. The exact finite-cover unspooling

For an integer \\(N\geq1\\), define

$$
S\_N=\operatorname{diag}(1,1,N,N)
$$

and the index-\\(N^{2}\\) sublattice

$$
\Lambda\_N
\=
\mathbb Z\langle
\widehat\gamma,\widehat u,
N\widehat w,N\widehat\delta
\rangle
\=
S\_N\mathbb Z^{4}.
$$

At a fixed fibre, define

$$
\widetilde F\_{T,N}
\=
\mathbb R^{4}/\mathsf P\_TS\_N\mathbb Z^{4}.
$$

Because

$$
\mathsf P\_TS\_N\mathbb Z^{4}
\subset
\mathsf P\_T\mathbb Z^{4},
$$

the identity map on \\(\mathbb R^{4}\\) descends to a finite holomorphic covering

$$
c\_{T,N}:
\widetilde F\_{T,N}
\longrightarrow
F\_T,
\qquad
[x]\_{\mathsf P\_TS\_N\mathbb Z^{4}}
\longmapsto
[x]\_{\mathsf P\_T\mathbb Z^{4}}.
$$

Its deck group is

$$
\frac{
\mathsf P\_T\mathbb Z^{4}
}{
\mathsf P\_TS\_N\mathbb Z^{4}
}
\cong
\frac{\mathbb Z^{4}}{S\_N\mathbb Z^{4}}
\cong
(\mathbb Z/N\mathbb Z)^{2}.
$$

Therefore

$$
\deg c\_{T,N}=N^{2}.
$$

In particular, \\(N=2\\) gives an exact \*\*four-sheeted cover\*\*:

$$
\widetilde F\_{T,2}\longrightarrow F\_T.
$$

This is the literal four-sheet version of the heuristic.

The two previously unit-length periods become

$$
N e\_1,\qquad N e\_3.
$$

Their lengths are therefore \\(N\\), so taking \\(N\to\infty\\) unrolls precisely the two directions that remained compact in the native cusp.

\## 4. The holonomy is compatible with the unspooling

The fibre cover by itself exists at every regular fibre. To assemble it around the cusp loop, the monodromy must preserve \\(\Lambda\_N\\).

A single cusp loop does not do that:

$$
M\_0\widehat\gamma
\=
\widehat\gamma-\widehat\delta,
\qquad
M\_0\widehat u
\=
\widehat u+\widehat w.
$$

The coefficients of \\(\widehat w,\widehat\delta\\) are not generally divisible by \\(N\\).

Now take the \\(N\\)-fold cyclic cover of the punctured cusp disc,

$$
r\_N:\Delta\_s^\*\longrightarrow\Delta\_{t\_c}^\*,
\qquad
t\_c=s^N.
$$

One loop around \\(s=0\\) winds \\(N\\) times around \\(t\_c=0\\), so the pulled-back monodromy is \\(M\_0^N\\). Since \\(R^{2}=0\\),

$$
M\_0^N=(I+R)^N=I+NR.
$$

Consequently,

$$
M\_0^N\widehat\gamma
\=
\widehat\gamma-N\widehat\delta,
$$

$$
M\_0^N\widehat u
\=
\widehat u+N\widehat w,
$$

$$
M\_0^N(N\widehat w)=N\widehat w,
\qquad
M\_0^N(N\widehat\delta)=N\widehat\delta.
$$

Hence

$$
M\_0^N\Lambda\_N=\Lambda\_N.
$$

More strongly,

$$
S\_N^{-1}M\_0^NS\_N=M\_0.
$$

Thus, in the basis

$$
(\widehat\gamma,\widehat u,
N\widehat w,N\widehat\delta)
$$

of the covered lattice, the monodromy matrix is again exactly \\(M\_0\\). The cover does not erase the cusp holonomy. It balances the \\(N\\)-fold base winding against the \\(N\\)-fold unrolling of each compact fibre cycle.

The corresponding diagram is

$$
\begin{array}{ccc}
\widetilde{\mathcal F}\_N
&\xrightarrow{\ C\_N\ }&
r\_N^\*\mathcal F\\\\[1mm]
\downarrow&&\downarrow\\\\
\Delta\_s^\*&=&\Delta\_s^\* ,
\end{array}
$$

where the fibre of \\(C\_N\\) is \\(c\_{T,N}\\) and its deck group is
\\((\mathbb Z/N\mathbb Z)^2\\).

This is the exact relation between the nontrivial cusp holonomy and the four-sheet heuristic:

$$
\boxed{
\text{twofold base cover}
\+
\text{doubling each of two compact cycles}
\=
\text{four-sheeted fibre cover}.
}
$$

General \\(N\\) gives an \\(N\\)-fold base cover and an \\(N^{2}\\)-sheeted fibre cover.

\## 5. Proof that the covered fibres converge to \\(\mathbb R^{4}\\)

Reorder the real coordinates as

$$
(x\_1,x\_3\\,;\\,x\_2,x\_4).
$$

Define

$$
A\_T=
\begin{pmatrix}
6\operatorname{Re}\mu\_T&
\operatorname{Re}\tau\_T\\\\
\operatorname{Re}\beta\_T&
\operatorname{Re}\mu\_T
\end{pmatrix},
$$

while retaining

$$
B\_T=
\begin{pmatrix}
6\operatorname{Im}\mu\_T&
\operatorname{Im}\tau\_T\\\\
\operatorname{Im}\beta\_T&
\operatorname{Im}\mu\_T
\end{pmatrix}.
$$

Every vector of the covered period lattice has the exact form

$$
\lambda\_{T,N}(n,m)
\=
\begin{pmatrix}
A\_Tn+Nm\\\\
B\_Tn
\end{pmatrix},
\qquad
n,m\in\mathbb Z^{2}.
$$

Let

$$
J=
\begin{pmatrix}0&1\\\\-1&0\end{pmatrix}.
$$

The cusp formula gives

$$
B\_T=TJ+C\_T,
$$

where

$$
C\_T=
\begin{pmatrix}
6\operatorname{Im}\mu(t\_c)&
\operatorname{Im}h(t\_c)\\\\
\operatorname{Im}b(t\_c)-\operatorname{Im}h(t\_c)&
\operatorname{Im}\mu(t\_c)
\end{pmatrix}.
$$

Choose \\(T\_0\\) inside the cusp neighbourhood and put

$$
C=
\sup\_{T\geq T\_0}\\|C\_T\\|\_{\mathrm{op}}<\infty.
$$

Because \\(J\\) is orthogonal,

$$
\begin{aligned}
\\|B\_Tn\\|
&=\\|TJn+C\_Tn\\|\\\\
&\geq T\\|n\\|-\\|C\_T\\|\_{\mathrm{op}}\\|n\\|\\\\
&\geq(T-C)\\|n\\|.
\end{aligned}
$$

Now consider a nonzero lattice vector
\\(\lambda\_{T,N}(n,m)\\).

When \\(n\neq0\\),

$$
\\|\lambda\_{T,N}(n,m)\\|
\geq
\\|B\_Tn\\|
\geq T-C.
$$

When \\(n=0\\), necessarily \\(m\neq0\\), and

$$
\\|\lambda\_{T,N}(0,m)\\|
\=
N\\|m\\|
\geq N.
$$

Therefore the systole satisfies

$$
\boxed{
\operatorname{sys}(\widetilde F\_{T,N})
\geq
\min\\{T-C,N\\}.
}
$$

Hence, for any sequence

$$
T\_j\longrightarrow\infty,
\qquad
N\_j\longrightarrow\infty,
$$

one has

$$
\operatorname{sys}(\widetilde F\_{T\_j,N\_j})
\longrightarrow\infty
$$

and

$$
\operatorname{inj}(\widetilde F\_{T\_j,N\_j})
\=
\frac12
\operatorname{sys}(\widetilde F\_{T\_j,N\_j})
\longrightarrow\infty.
$$

Let

$$
\widetilde q\_{T,N}:
\mathbb R^{4}\longrightarrow\widetilde F\_{T,N},
\qquad
x\longmapsto[x]
$$

be the universal covering map. Its kernel is

$$
\ker\widetilde q\_{T,N}
\=
\mathsf P\_TS\_N\mathbb Z^{4}.
$$

Fix \\(R>0\\). Once

$$
\operatorname{sys}(\widetilde F\_{T,N})>4R,
$$

the restriction

$$
\widetilde q\_{T,N}|\_{B\_R(0)}
$$

is an isometric embedding: if \\(x,y\in B\_R(0)\\) and
\\(\lambda\neq0\\) is a period, then

$$
\\|x-y+\lambda\\|
\geq
\\|\lambda\\|-\\|x-y\\|
\>
4R-2R
\geq
\\|x-y\\|.
$$

Thus the quotient metric agrees exactly with the Euclidean metric throughout the embedded ball.

It follows that

$$
\boxed{
(\widetilde F\_{T\_j,N\_j},[0])
\longrightarrow
(\mathbb R^{4},0)
}
$$

in pointed smooth, pointed Gromov–Hausdorff, and local-isometric senses.

Because the covering map originates in \\(\mathbb C^{2}\\), the same statement is holomorphic:

$$
\boxed{
\widetilde F\_{T\_j,N\_j}
\longrightarrow
\mathbb C^{2}\cong\mathbb R^{4}
}
$$

on every fixed bounded complex coordinate domain.

A completely explicit diagonal sequence is

$$
N=j,\qquad T=j^{2}.
$$

Then

$$
t\_c=e^{-2\pi j^{2}},
\qquad
s=t\_c^{1/j}=e^{-2\pi j},
$$

so both the original cusp coordinate and the coordinate on the \\(j\\)-fold base cover tend to zero, while

$$
\operatorname{sys}(\widetilde F\_{j^{2},j})
\geq j
$$

for sufficiently large \\(j\\).

\## 6. This introduces the missing momentum directions

The covering is not merely a relabelling of the old periodic field theory.

Characters of \\(F\_T\\) are

$$
\chi\_{T,\ell}([x])
\=
\exp\left(
2\pi i
\left\langle
\mathsf P\_T^{-\mathsf T}\ell,x
\right\rangle
\right),
\qquad
\ell\in\mathbb Z^{4}.
$$

Characters of the cover are

$$
\widetilde\chi\_{T,N,k}([x])
\=
\exp\left(
2\pi i
\left\langle
\mathsf P\_T^{-\mathsf T}S\_N^{-1}k,x
\right\rangle
\right),
\qquad
k\in\mathbb Z^{4}.
$$

Pullback under \\(c\_{T,N}\\) gives

$$
c\_{T,N}^{\*}\chi\_{T,\ell}
\=
\widetilde\chi\_{T,N,S\_N\ell}.
$$

Therefore the image of the original field space consists exactly of cover modes satisfying

$$
k\_3\equiv0\pmod N,
\qquad
k\_4\equiv0\pmod N.
$$

The cover contains additional modes with

$$
k\_3\not\equiv0\pmod N
\quad\text{or}\quad
k\_4\not\equiv0\pmod N.
$$

Their momenta occur in fractions of the previous compact-direction momentum:

$$
S\_N^{-1}k
\=
\left(
k\_1,k\_2,\frac{k\_3}{N},\frac{k\_4}{N}
\right).
$$

Thus the finite covers genuinely fill in the two missing momentum continua. The old cusp contributes momentum spacing of order \\(T^{-1}\\) in two directions; the covering contributes spacing of order \\(N^{-1}\\) in the other two.

The covered scalar spectrum is exactly

$$
\operatorname{Spec}\Delta\_{T,N}
\=
\left\\{
4\pi^{2}
\left\\|
\mathsf P\_T^{-\mathsf T}S\_N^{-1}k
\right\\|^{2}:
k\in\mathbb Z^{4}
\right\\}.
$$

For the gauge-fixed Yang–Mills Hessian at the flat connection, the positive nonharmonic spectrum is the same set, with transverse-polarization and Lie-algebra multiplicities:

$$
\operatorname{Spec}^{+}\mathcal M\_{T,N}
\=
\left\\{
4\pi^{2}
\left\\|
\mathsf P\_T^{-\mathsf T}S\_N^{-1}k
\right\\|^{2}:
k\in\mathbb Z^{4}\setminus\\{0\\}
\right\\}.
$$

Consequently, the geometric sequence now has all of the following properties simultaneously:

$$
\dim\_{\mathbb R}\widetilde F\_{T,N}=4,
$$

$$
\operatorname{Vol}(\widetilde F\_{T,N})\longrightarrow\infty,
$$

$$
\operatorname{inj}(\widetilde F\_{T,N})\longrightarrow\infty,
$$

$$
\widetilde F\_{T,N}\longrightarrow\mathbb R^{4},
$$

and

$$
\inf\operatorname{Spec}^{+}\mathcal M\_{T,N}
\longrightarrow0.
$$

This removes the earlier geometric limitation that the operator family lived only in a \\(T^{2}\times\mathbb R^{2}\\) thermodynamic limit.

\## 7. The literal doubling construction also works

The heuristic of obtaining two expanding two-dimensional objects and combining them also has an exact realization.

Recall

$$
Q\_T=\mathbb R^{2}/B\_T\mathbb Z^{2},
\qquad
\pi\_T:F\_T\to Q\_T,
$$

with kernel \\(K\_T\cong T^{2}\\).

Since

$$
B\_T=TJ+C\_T
$$

and \\(C\_T\\) is bounded,

$$
\operatorname{sys}(Q\_T)\geq T-C.
$$

Therefore

$$
Q\_T\longrightarrow\mathbb R^{2}.
$$

Now define

$$
D\_T=Q\_T\times Q\_T
\=
\mathbb R^{4}/
\begin{pmatrix}
B\_T&0\\\\
0&B\_T
\end{pmatrix}
\mathbb Z^{4}.
$$

The exact map from two original fibres is

$$
\Pi\_T:
F\_T\times F\_T
\longrightarrow
D\_T,
\qquad
(x,y)\longmapsto
(\pi\_T(x),\pi\_T(y)).
$$

Its kernel is

$$
\ker\Pi\_T=K\_T\times K\_T.
$$

Moreover,

$$
\operatorname{sys}(D\_T)
\=
\operatorname{sys}(Q\_T)
\geq T-C,
$$

so

$$
\boxed{
D\_T\longrightarrow\mathbb R^{4}.
}
$$

This is a mathematically exact version of “take two copies of the part that becomes \\(\mathbb R^{2}\\).”

Its information loss is also exact: the map discards \\(K\_T\times K\_T\\), four compact real directions. The finite-cover construction above is preferable because it unrolls those directions instead of quotienting them away.

The natural doubled global manifold would be \\(X\times X\\), not \\(S^{12}\\). Indeed,

$$
H\_6(S^{6}\times S^{6};\mathbb Z)
\cong
\mathbb Z\oplus\mathbb Z,
$$

whereas

$$
H\_6(S^{12};\mathbb Z)=0.
$$

Thus \\(S^{6}\times S^{6}\\) and \\(S^{12}\\) are not homotopy equivalent.

\## 8. Wick rotation has to occur after the unspooling

On the native limit

$$
T^{2}\times\mathbb R^{2},
$$

Wick rotation of one noncompact coordinate gives

$$
T^{2}\times\mathbb R^{1,1},
$$

not \\(\mathbb R^{1,3}\\). The two torus identifications are unchanged.

After the finite-cover limit has produced local coordinates on \\(\mathbb R^{4}\\), define

$$
W:\mathbb R^{1,3}\longrightarrow\mathbb C^{4},
\qquad
W(t,x\_1,x\_2,x\_3)
\=
(it,x\_1,x\_2,x\_3).
$$

For the complexified Euclidean bilinear form

$$
dz\_0^{2}+dz\_1^{2}+dz\_2^{2}+dz\_3^{2},
$$

one has

$$
W^{\*}
\left(
dz\_0^{2}+dz\_1^{2}+dz\_2^{2}+dz\_3^{2}
\right)
\=
-dt^{2}+dx\_1^{2}+dx\_2^{2}+dx\_3^{2}.
$$

Thus Wick rotation does give local Minkowski \\(\mathbb R^{1,3}\\), but only after all four quotient periods have been sent to infinity. It does not itself remove any period.

\## 9. Precise consequence

The geometric objection in the previous analysis is now removed:

$$
\boxed{
\text{The Alpöge–Fable cusp admits a monodromy-compatible
finite-cover sequence with pointed limit }\mathbb R^{4}.
}
$$

The exact mechanism is

$$
\boxed{
t\_c=s^N,\qquad
\Lambda\_N=
\langle
\widehat\gamma,\widehat u,
N\widehat w,N\widehat\delta
\rangle,\qquad
S\_N^{-1}M\_0^NS\_N=M\_0.
}
$$

For \\(N=2\\), this is precisely a four-sheeted fibre cover after a twofold cusp-base cover. Sending \\(N\to\infty\\) unspools the two residual torus directions; sending \\(T\to\infty\\) simultaneously unspools the other two.

The resulting family is a genuine Euclidean-\\(\mathbb R^{4}\\) exhaustion, and its scalar, gauge-Hessian, and Gaussian-quantized gaps tend to zero. What remains outside that theorem is the nonlinear reconstructed Yang–Mills Hamiltonian: the finite covers give the correct four-dimensional geometry and full momentum continuum, but the calculation still concerns the flat-connection Hessian and its Gaussian quantization rather than the interacting physical spectrum.

That is a substantially stronger position than the previous \\(T^{2}\times\mathbb R^{2}\\) result.


