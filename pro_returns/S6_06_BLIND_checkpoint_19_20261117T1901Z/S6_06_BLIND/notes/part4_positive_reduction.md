# P4.33: normalization cohomology

Status: Proved; independently audited.

```tex
\subsection{Normalization cohomology for the remaining positive cases}

\begin{statement}{P4.33}{Proved}
Let $S$ be an irreducible singular support in Part~4.2, and let
$\rho:T\to N\to S$ be its minimal normalization resolution.
Then $H^2(N,\mathcal O_N)=0$. If
$p=\dim H^0(N,R^1\rho_{N*}\mathcal O_T)$ is the sum of the
geometric genera of the normalization singularities, then
\[
 p=h^1(T,\mathcal O_T)-h^1(N,\mathcal O_N).
\]
In particular a rational resolution forces every normalization
singularity to be rational and gives $\chi(\mathcal O_N)=1$.
For the scheme-theoretic image conductor $C_{\rm sch}$ we have
\[
 \chi(\mathcal O_{C_{\rm sch}})
   =-\chi(\mathcal O_N)=h^1(N,\mathcal O_N)-1.
\]

In the ruled double-horizontal case, with section $H$ of genus
$g\ge1$, a contracted $H$ gives $h^1(N,\mathcal O_N)=0$ and
$p=g$. A noncontracted $H$ gives $p=0$ and
$h^1(N,\mathcal O_N)=g$.
\end{statement}
\begin{proof}
Write $I_S\subset\mathcal O_S$ for the conductor ideal.
Finite duality gives
\[
 \nu_*\omega_N=I_S\otimes\omega_S.
\]
The dualizing line bundle $\omega_S$ is torsion by P4.12.
A nonzero section of a torsion line bundle on a compact
irreducible reduced complex space has no zero: raising it
to a trivializing positive power gives a nonzero holomorphic
function, hence a nonzero constant. Such a section cannot
belong to the proper conductor ideal along the nonempty
conductor. Therefore $H^0(N,\omega_N)=0$. Serre duality
on the compact Cohen--Macaulay normal surface gives
$H^2(N,\mathcal O_N)=0$.

The resolution is birationally ruled or of class VII and
has $H^2(T,\mathcal O_T)=0$, by P4.12 and the classification
already used in P4.26. The low-degree Leray sequence,
using $\rho_{N*}\mathcal O_T=\mathcal O_N$ and the
finite support of $R^1\rho_{N*}\mathcal O_T$, is therefore
\[
 0\longrightarrow H^1(N,\mathcal O_N)
 \longrightarrow H^1(T,\mathcal O_T)
 \longrightarrow H^0(N,R^1\rho_{N*}\mathcal O_T)
 \longrightarrow0.
\]
This proves the formula for $p$. If $T$ is rational,
$h^1(\mathcal O_T)=0$, so $p=0$. Each nonnegative local
geometric genus is zero, giving the asserted rational
singularities and Euler characteristic.

For completeness the conductor Euler identity does not
require rational singularities. Put $L=\nu^*\omega_S$,
and write $I_N=\omega_N\otimes L^{-1}$ for the conductor
on $N$. Serre duality gives $\chi(I_N)=\chi(L)$.
Riemann--Roch on $T$, applied to the torsion line bundle
$\rho_N^*L$, gives
$\chi(\rho_N^*L)=\chi(\mathcal O_T)$.
The projection formula makes
$R^1\rho_{N*}\rho_N^*L=L\otimes R^1\rho_{N*}\mathcal O_T$;
its finite length is still $p$. Leray therefore gives
$\chi(L)=\chi(\mathcal O_N)$.
Consequently the conductor scheme $D_{\rm sch}\subset N$
has $\chi(\mathcal O_{D_{\rm sch}})=0$.
The exact conductor square, together with
$\chi(\mathcal O_S)=0$, proves
$\chi(\mathcal O_{C_{\rm sch}})=-\chi(\mathcal O_N)$.
Since $N$ is compact connected and $H^2(\mathcal O_N)=0$,
the remaining equality follows.

Finally suppose the ruled pole support is $H$ with
rational vertical trees. If $H$ is contracted, the
composition $H\to T\to N$ is constant. Pullback from
$H^1(N,\mathcal O_N)$ to $H^1(H,\mathcal O_H)$ is zero.
But restriction
$H^1(T,\mathcal O_T)\to H^1(H,\mathcal O_H)$ is an
isomorphism: the ruling has section $H$, a
$\mathbb P^1$-bundle has zero first higher direct image
of its structure sheaf, and the actual point blowups
preserve these groups. The Leray injection above
therefore forces $H^1(N,\mathcal O_N)=0$, so $p=g$.
If $H$ is not contracted, every exceptional curve is
vertical. The ruling descends by the normalized-graph
comparison of P4.29. Its Leray calculation gives $p=0$,
and the same exact sequence gives $h^1(\mathcal O_N)=g$.
\end{proof}
```
