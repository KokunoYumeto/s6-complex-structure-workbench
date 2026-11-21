from pathlib import Path
import json,datetime
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];ed=Editor('I')
old=block(ed.text,'inv:A1.0')
new=old.replace('In the cyclic covering coordinate\n$s$, the action on $G$ has characters $(1,\\zeta^{-a})$, where',
 'On the normalized root family, the cohomology pullback by the\ncyclic generator has characters $(1,\\zeta^{-a})$, where')
assert old!=new
new+=r'''

\begin{proposition}[The root-to-coarse comparison maps]
\hypertarget{tag-PI10}{}\label{I:root-coarse-comparison}
\StatementRecord{I:root-coarse-comparison}{proved}{PI10}{\cref{inv:D1.1,inv:D1.2,push:src:E.3.1}}
Write $G_B=R^1f_*\mathcal O_X$ and
$G_{\mathcal B}=R^1\bar f_*\mathcal O_X$. Then
\[
 G_B=\rho_*G_{\mathcal B}.
\]
On a root disc $t=s^m$, take a frame $(e_1,e_2)$ in which the
covariant action is $(1,\zeta^a)$, where
$(m,a)=(3,2)$ or $(4,1)$ and $\zeta=e^{-2\pi i/m}$.
The invariant frame is $(e_1,s^ae_2)$, and the adjunction map is
\[
 \rho^*G_B\longrightarrow G_{\mathcal B},
 \qquad (u,v)\longmapsto(u,s^av).
\]
It is the map induced by normalization after the root base change.
The covariant action on cohomology is
$(g^{-1})^*:G_{\mathcal B,s}\to G_{\mathcal B,gs}$;
the pullback $g^*:G_{\mathcal B,gs}\to G_{\mathcal B,s}$ has
the inverse eigenvalues $(1,\zeta^{-a})$.

For the relative logarithmic cotangent bundle of
\cref{I:def:root-bundles}, the evaluation pairing gives
\[
 \mathcal E=\bar f^*(E^\vee),
\]
where $E$ is the vertical root bundle in \cref{inv:D1.2}.
\end{proposition}
\begin{proof}
The factorization $f=\rho\bar f$ and exactness of finite-group
invariants give $R^qf_*\mathcal O_X=
\rho_*R^q\bar f_*\mathcal O_X$.
In the chosen root frame, invariance of $h(s)e_2$ is exactly
$h(\zeta s)=\zeta^a h(s)$. Its convergent series is therefore
$s^aH(s^m)$. This gives both the invariant frame and the displayed
adjunction matrix. The normalization map agrees with this map on
the punctured disc by its marked torus identification, hence on
the whole disc by holomorphic continuation. At $s=0$ its second
component is zero; this specifies the comparison with the
normalized torus fibre while the coarse base-change theorem uses
the full scheme fibre. Inverting the covariant action gives the
displayed pullback eigenvalues.

On an ordinary chart the pairing is
$\langle d\zeta_i,\partial_{\zeta_j}\rangle=\delta_{ij}$.
At the cusp the exponential map sends
$\partial_{\zeta_i}$ to $2\pi i x_i\partial_{x_i}$ and
$d\zeta_i$ modulo the base differential to
$(2\pi i)^{-1}d\log x_i$, preserving that pairing.
On a finite root chart, $dt/t=m\,ds/s$ removes exactly the
base logarithmic direction from the quotient defining
$\mathcal E$. Thus these local perfect pairings agree under
the transition maps and give $\mathcal E=\bar f^*(E^\vee)$.
\end{proof}
'''
ed.replace(old,new,'D20',
 'Specify the exact invariant-pushforward and normalization maps between the coarse and root cohomology bundles, with diagonal matrix (1,s^a), covariant/inverse-pullback characters, and the explicit cotangent/vertical evaluation pairing. This resolves overloaded G and E notation without identifying different base-change maps.',
 'I:root-coarse-comparison')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_coarse_root_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'verification':'Root derived h(zeta*s)=zeta^a*h(s) and diagonal adjunction; topology agent independently confirmed the specified map from its previously checked root charts, expressly without another independent-experiment claim.',
 'maps':['G_B=rho_*G_root by exact invariants.','rho^*G_B to G_root is diag(1,s^a), (m,a)=(3,2),(4,1).','Cohomology covariant map is inverse pullback; actual pullback has inverse eigenvalues.','d-zeta and partial-zeta transport to (2pi i)^-1 dlogx and2pi i x partial-x; evaluation gives relative log cotangent=barf^*E^dual.'],
 'scope':'Explicit map/notation clarification. The normalized torus-fibre map is not claimed invertible at the root centre.'},indent=2)+'\n')
