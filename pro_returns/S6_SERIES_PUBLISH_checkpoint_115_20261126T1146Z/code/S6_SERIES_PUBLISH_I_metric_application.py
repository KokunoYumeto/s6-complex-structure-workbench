from pathlib import Path
import json,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
a=ed.text.index('The expanded source derivation is retained in the proof compendium, Paper~I, label '+r'\nolinkurl{inv:C3.6}.')
b=ed.text.index(r'\begin{proposition}',a)
old=ed.text[a:b]
new=r'''\begin{proof}
Gauduchon's conformal theorem
\cite[Theorem~2, pp.~132--133]{Gauduchon1985} supplies a Gauduchon
metric on the compact complex threefold. Fix any such $\omega_0$.
By \cref{fam:src:A.1.1} and $4S_2=f^*(p_2)$,
$K_X^{\otimes2}\simeq f^*\mathcal O_B(-1)$.
For $\theta=f^*\omega_{FS}$, with
$\int_{\mathbb P^1}\omega_{FS}=1$, this gives
\[
 c_{1,BC}(T_X)=\tfrac12[\theta]_{BC}.
\]
The convention
$\operatorname{Ric}^{\mathrm{Ch}}(\omega)=-i\partial\bar\partial
\log\det(g)$ represents $2\pi c_{1,BC}(T_X)$.
Thus $\pi\theta$ is the prescribed representative of that class.
Theorem~1.3 of \cite[arXiv v2, p.~3; conventions on p.~2]{STW2017}
gives a Gauduchon metric with this Chern--Ricci form and
$[\omega^2]_A=[\omega_0^2]_A$.

The pullback $\theta$ is semipositive and has rank one where
$f$ is a submersion. In particular
$\int_X\theta\wedge\omega_0^2>0$.
Every $\partial\bar\partial$-exact $(1,1)$ form pairs to zero
with the Gauduchon square, by integration by parts.
Consequently $[\theta]_{BC}\ne0$, and a zero Chern--Ricci form
would contradict the displayed Chern-class identity.
\end{proof}

'''
ed.replace(old,new,'D06',
 'Restore the full specialized application of Gauduchon and STW at the cited statement. The supplied short proof was read in full and the exact K-square/Chern normalization and Aeppli preservation agree; the classical PDE proof is cited. The nonzero class follows by the explicit positive Gauduchon pairing.',
 'inv:C3.6')
for label,old in [
 ('inv:A1.0','The expanded source derivation is retained in the proof compendium, Paper~I, label '+r'\nolinkurl{inv:A1.0}.'),
 ('inv:A1.0','The structure-sheaf and cusp statements are due to '+r'\citet[Lemma~9.12 and Proposition~9.13]{AC2026}; we retain the independent root-line derivation. A complete re-derivation is given in \CompendiumRef{I}{app:rederive:inv-A1.0}.'),
 ('inv:C3.1','The Picard and fibre-restriction statement is due to '+r'\citet[Theorem~10.5]{AC2026}. A complete re-derivation is given in \CompendiumRef{I}{app:rederive:inv-C3.1}.')]:
    ed.replace(old,'','D06','Keep the precise primary attribution and operative proof where already printed; remove the obsolete compendium pointer and repeated source narration.',label)
ed.replace('The structure-sheaf input in the precise form used below','Structure-sheaf direct images','D16','Use a mathematical statement title.','inv:A1.0')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_metric_application_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'old_proof_source':'agents/i_analytic/S6_SERIES_PUBLISH_I_initial_four_printed_proofs.json target inv-C3.6',
 'reading':'Complete supplied proof and the initial-four independent comparison read before restoring the application.',
 'exact_maps':['K_X^2=f^*O(-1) gives c1BC(T_X)=theta/2.','Unnormalized Chern–Ricci is 2pi c1BC, hence pi theta.','The positive integral of theta against a Gauduchon square proves nonvanishing under the BC–Aeppli pairing.'],
 'scope':'Used-and-rechecked proof restoration; classical existence results remain precisely cited inputs.'},indent=2)+'\n')
