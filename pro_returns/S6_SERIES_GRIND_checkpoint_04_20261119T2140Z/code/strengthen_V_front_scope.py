"""State the exact scope of the receiving period/classification results."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];p=R/'frontmatter/frontmatter_V.tex';s=p.read_text()
a=s.index('The genus-two pencil\n');b=s.index('\\textit{Mechanism.}',a)
c=r'''The pencil $y^2=x^5+\lambda^3x+\lambda^4$ has one nodal
fibre away from $0,\infty$, at $\lambda_*=-256/3125$.
Its good root charts have orders eight and five, and on that root
curve its Hodge bundle is
\[
 \mathcal H=T^3\oplus T,\qquad
 T=\OO((2/5)[\infty]-(3/8)[0]),\qquad \deg T=1/40.
\]
The meromorphic differential $dx/y$ generates $\ell_0=T^3$.
In the full rank-four de Rham bundle, projection of
$\ell_0\wedge\mathcal H_{\rm dR}$ to
$\bigwedge^2\mathcal H_{\rm dR}/\mathbb C\omega$
is a rank-three bundle $P$.  Its holomorphic lift to the specified
rank-six extension is $(\sigma_b+\xi\alpha e)(P)$, with the
normalization of $e,\alpha,\sigma_b$ in \cref{night:P1.15}.
It is transverse to its conjugate on the completed base exactly
for the parameters $\xi\in\mathcal U$ of Theorem~E.
The actual exterior-square and lift maps descend the finite root
orders to five and four; the cusp has period
$Z(q)=(\log q/(2\pi i))I_3+C(q)$ with $C$ holomorphic at zero
(\cref{night:P1.4,night:P1.5,maps:src:F.3.5,maps:src:F.3.6,night:P1.18}).

'''
s=s[:a]+c+s[b:]
a=s.index('Every supplied rank-six integral datum');b=s.index('\\textit{Mechanism.}',a)
c=r'''Let $k\in\{2,3\}$ and $\Lambda=\mathbb Z^6$.
Consider ordered integral tuples $(M_1,\ldots,M_k,M_0)$ with each
$M_i$ of finite order and having a nonzero fixed vector, with
$M_0=(M_1\cdots M_k)^{-1}$, and with
$N=M_0-I$ satisfying $N^2=0$, rank three, and
$\operatorname{im}N=\ker N$ as integral sublattices of $\Lambda$.
Every such tuple has a computable canonical representative and an
explicit simultaneous unimodular conjugator; equality of the
representatives is equivalent to simultaneous integral conjugacy.
For input entry height $H$, the finite stopping bound is
$(2H+1)^{36(k+1)}$ candidates before the proved rejection filters.
The ordered sector with both finite linear orders two has exactly
56 classes.  Each has free affine lifts of actual order four,
and every free affine filling of this sector has nontrivial
fundamental group.

Specify the actual free affine actions
$\tau_i(x)=M_ix+v_i/m_i$, with $v_i\in\Lambda$ and actual
order $m_i$, an integral translation clutch $\kappa\in\Lambda$,
and a primitive Kuhn cusp marking.  The algorithms compute the
full fundamental group and every integral homology group of the
resulting marked gluing for every such input.  Their constructive
parametrization and finite tests identify exactly the inputs with
$\pi_1=1$ and $H_2=H_3=0$; there is no fixed bound on the
orders, twists or lattice indices (\cref{maps:src:F.2.39}).

On $B^*=\mathbb P^1\setminus\{p_0,\ldots,p_k\}$ with $k\ge1$,
every representation $\rho:\pi_1(B^*)\to GL^+(6,\mathbb R)$
whose $p_0$ monodromy satisfies $(M_0-I)^2=0$ and
$\operatorname{rank}(M_0-I)=3$ has a holomorphic period family
transverse to its conjugate everywhere on $B^*$. In the marking
$M_0=\left(\begin{smallmatrix}I&I\\0&I\end{smallmatrix}\right)$,
its cusp period is
\[
 Z(t)=\frac{\log t}{2\pi i}I_3+C(t),\qquad C\text{ holomorphic at }0,
\]
with any prescribed finite jet of $C$ at zero. An integral primitive
cusp admits an integral marking. The other $p_i$ remain punctures
in this assertion (\cref{maps:src:F.3.11}).

For a polarized algebraic abelian-surface family with toric-rank-two
cusp, the construction that takes a fibrewise degree-zero line bundle
and quotients its punctured bundle by a lifted translation cannot
have $b_1=b_2=0$ with the stipulated rank-three square-zero Kuhn
cusp; this holds for both proportional and nonproportional source
sections. The filtration and Euler-parity proof is
\cref{maps:src:F.3.4}.

'''
s=s[:a]+c+s[b:]
s=s.replace('enclose all12911 leaves of the closed covers above','enclose all 1600 leaves of the closed covers above').replace('proof, items1--7','proof, items 1--7')
s=s.replace(r'full statements: \SeriesRef{maps:src:F.2.39}, \SeriesRef{maps:src:F.3.11}.',r'full statements: \SeriesRef{maps:src:F.2.39}, \SeriesRef{maps:src:F.3.11}, \SeriesRef{maps:src:F.3.4}.')
p.write_text(s)
p=R/'frontmatter/frontmatter_V_map.json';d=json.loads(p.read_text())
for m in d['main_theorems']:
 if m['letter']=='F' and 'maps:src:F.3.4' not in m['body_labels']:m['body_labels'].append('maps:src:F.3.4')
 if m['letter']=='C' and 'night:P1.18' not in m['body_labels']:m['body_labels'].append('night:P1.18')
 for st in m['steps']:
  st['claim_tex']=st['claim_tex'].replace('all12911','all 1600').replace('items1--7','items 1--7')
p.write_text(json.dumps(d,indent=2))
print('Updated exact V.C/V.F hypotheses and V.E certificate count; no mathematical assertion beyond receiving statements.')
