"""Write complete corrected proof blocks, preserving the source statement IDs."""
from pathlib import Path

root=Path(__file__).resolve().parents[3]
out=root/'deliverables/work/cdp_audit'
header='''% Full corrected source proof block; not a Paper II manuscript.
% Checker: GPT-6 Astra (OpenAI, ChatGPT Pro mode), effort Pro.
% Date: 17 November 2026 UTC.
'''

def block(name):
    s=(out/'extracted'/name).read_text()
    return s[:s.index(r'\end{proof}')+len(r'\end{proof}')]

s=block('CDP_C2c.tex')
start=s.index('For existence, take the standard')
end=s.index('For rank one every normalization')
replacement=r'''For existence, use the lattice $N=\mathbb Z^2\oplus\mathbb Z$
and the standard triangulation of $\mathbb R^2$ whose triangles are
\[
 [u,u+e_1,u+e_1+e_2],\qquad
 [u,u+e_2,u+e_1+e_2],\qquad u\in\mathbb Z^2.
\]
These are the Delaunay triangles for the positive integral quadratic
form $q(u_1,u_2)=u_1^2-u_1u_2+u_2^2$.
Take the cones over these triangles at height one and all their
faces. They form a fan. Every three-dimensional cone is generated
by a basis of $N$, because its triangle is unimodular. Gluing its
affine toric charts therefore gives a smooth complex threefold
$\mathcal X$ with a holomorphic map to the affine line. On each
maximal chart there are coordinates $x_1,x_2,x_3$ in which the map
is exactly $t=x_1x_2x_3$. The central support is consequently
reduced and has normal crossings. Over $t\ne0$ the fibre is the
common algebraic torus $(\mathbb C^*)^2$.

Let $\Lambda_N=\mathbb Z(Ne_1)\oplus\mathbb Z e_2$.
For $\ell\in\Lambda_N$, the lattice shear
\[
 (u,k)\longmapsto(u+k\ell,k)
\]
preserves the fan and induces an automorphism over the base.
On the punctured torus chart it is
\[
 (z_1,z_2,t)\longmapsto
 (t^{\ell_1}z_1,t^{\ell_2}z_2,t).
\]
Restrict to $|t|<\epsilon<1$. This action is free: away from the
central fibre, a fixed point would imply $t^{\ell_i}=1$ for both
coordinates and hence $\ell=0$; on the central fibre, a fixed
point would require its bounded indexing face of the triangulation
to be invariant under translation by $\ell$, which again forces
$\ell=0$.

Here is also the required analytic properness check. For $t\ne0$,
put $v_i=\log|z_i|/\log|t|$. In the chart of a triangle with
vertices $u_1,u_2,u_3$, write
\[
 v=\sum_{j=1}^3\lambda_j u_j,\qquad
 \lambda_j=\frac{\log|x_j|}{\log|t|},\qquad
 \sum_j\lambda_j=1.
\]
On a compact subset of finitely many charts the $|x_j|$ are
bounded. As $t$ tends to zero, this gives a uniform lower bound
for every $\lambda_j$, and their sum then gives a uniform upper
bound. Thus $v$ remains bounded there. Away from zero the same
conclusion follows from compactness in the torus charts.
Translation by $\ell$ sends $v$ to $v+\ell$. Consequently only
finitely many elements can carry a fixed compact set into itself,
or make two fixed compact sets intersect. On the central fibre
this is also immediate from the finitely many indexing faces.
The action is properly discontinuous, so its quotient is a smooth
complex threefold.

The quotient map to the disc is proper. Indeed, translate any
punctured-fibre point so that $v$ belongs to a fixed compact
fundamental parallelogram for $\Lambda_N$. Only finitely many
triangles meet that parallelogram. Choose one containing $v$;
then all its barycentric coordinates are nonnegative, so
$|x_j|=|t|^{\lambda_j}\le1$. These finitely many closed unit
polydiscs provide compact representatives for every sequence
approaching the central fibre. The central fibre itself has
finitely many toric components modulo $\Lambda_N$, and each is
compact: the star of a vertex is a complete two-dimensional fan.
These facts prove compactness over every closed smaller disc.
For $t\ne0$ the quotient fibre is explicitly
\[
 \mathbb C^*/t^{N\mathbb Z}\ \times\
 \mathbb C^*/t^{\mathbb Z},
\]
a product of elliptic curves. This supplies the actual convergent
analytic degeneration, including its smooth total space and
properness, without inferring analytic convergence from a formal
model. The quadratic form supplies the usual polarization data:
its difference under every lattice translation is an integral
affine function. Thus the construction is the analytic realization
of the polyhedral model described in
\cite[Section~6, especially (6.3)--(6.7)]{Mumford1972}.
That source formulates its construction over a complete discrete
valuation ring; the preceding chart and compactness argument is
the complex-disc comparison used here.

The quotient triangulation has $V=N$ and $F=2N$, as required.
'''
s=s[:start]+replacement+s[end:]
(out/'corrected_C2c_full_proof.tex').write_text(header+s+'\n')

s=block('CDP_E6.tex')
start=s.index('We pass from this formal statement')
end=s.index('The just-proved lifting property',start)
replacement=r'''We pass from the formal assertion to an analytic map and
specify the relative parameter space, including its nilpotents.
Let $H$ be the germ at the graph of $g$ in the absolute Douady
space of $\mathcal Y\times\mathbb P^1$, and let
$\pi:\mathcal R\to H$ be its universal compact flat family.
Douady's existence and finiteness theorems
\cite[Section~9, Theorems~1--2, pp.~83--85]{Douady1966}
apply to this analytic ambient space; its local rings and those
of the parameter space may have nilpotents.

After shrinking $H$, one has
\[
 \pi_*\mathcal O_{\mathcal R}=\mathcal O_H,
\]
compatibly with base change. To check this without assuming a
reduced parameter space, represent $R\pi_*\mathcal O_{\mathcal R}$
near the central point by a finite complex of finite free analytic
modules. On the central fibre the unit spans
$H^0(Y,\mathcal O_Y)=\mathbb C$. Split off this unit in degree
zero. The differential is injective modulo the maximal ideal on
the complementary degree-zero summand; an invertible minor
cancels that summand with its image in degree one. The resulting
complex begins with $\mathcal O_H$ in degree zero and zero
differential from it. This proves the displayed equality and its
base-change assertion on the full analytic germ.

Embed a representative of $(S,0)$ in a polydisc. The coordinate
functions of the map $\mathcal R\to\mathcal Y\to S$ are now
pullbacks of unique holomorphic functions on $H$. They satisfy
the defining equations of $S$, because their pullbacks do and the
unit map just proved is injective. They therefore define a
holomorphic morphism $H\to S$, and the universal subspace lies
scheme-theoretically in
\[
 (\mathcal Y\times_S H)\times\mathbb P^1.
\]
The projection of this subspace to $\mathcal Y\times_S H$ is a
proper morphism between two proper flat families over $H$ and
is an isomorphism at the central point. By the isomorphism-locus
criterion \cite[Section~10.1, Proposition~1, p.~86]{Douady1966},
it is an isomorphism after restricting to an open neighbourhood
of that point. The proof of that criterion uses the finite
direct image, flatness and Nakayama's lemma, and applies to
nonreduced $H$. On this open locus the universal subspace is
the graph of an actual map to $\mathbb P^1$.

The universal property of the absolute Douady space consequently
identifies this open locus with the germ $\mathcal H\to S$ of
relative maps from $\mathcal Y/S$ to
$\mathbb P^1\times S/S$. This is the relative version of
Douady's graph construction
\cite[Section~10.2, Theorem~1, p.~87]{Douady1966}; the argument
above supplies the variation of the compact source explicitly.
'''
s=s[:start]+replacement+s[end:]
(out/'corrected_E6_full_proof.tex').write_text(header+s+'\n')
print('Saved complete C2c and E6 corrected proof blocks')
