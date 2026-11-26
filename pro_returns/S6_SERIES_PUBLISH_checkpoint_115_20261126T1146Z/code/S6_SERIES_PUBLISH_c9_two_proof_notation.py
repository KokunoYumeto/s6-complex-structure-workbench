#!/usr/bin/env python3
"""Prepare guarded P15 notation edits in 02LE/02LQ; never mutate canonical TeX."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation9_findings'
s = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_text()
rows = []

def add(suffix, statement, locus, old, new, reason):
    assert old != new
    assert s.count(old) == 1, (suffix, s.count(old))
    assert old.count('\\label{') == new.count('\\label{'), suffix
    rows.append(dict(
        change_id='CLAUDE-III-P15-' + suffix, type='D20',
        statement_id=statement, old_location='Paper III, ' + locus,
        old_page='cp100 source; permanent anchor supplied',
        new_location='Paper III, ' + locus, new_page='pending final build',
        old_text=old, new_text=new, reason=reason,
        review_status='Full definition/statement/proof reread completed; exact notation and all incident formulas checked; canonical admission and final PDF gate pending.'))

add('02LE-COHOMOLOGY-Z', 'maps:src:D.2.38', 'tag02LE, comparison ending in D.MP8',
    r'''For comparison with the marking that evaluates to one on $C_f$, put
$z=(a\nu)^{-1}\alpha_p$. Its homology generator is $g_z=(a\nu)s$,
with inverse coordinate evaluation by $z$. The simultaneous action
conversion gives
\begin{equation}
 z[E_p]=-\frac{w^2}{\nu^2},\qquad
 \langle z^3,[X]_p\rangle=0,\qquad
 \langle z\,\rho_p p_1,[X]_p\rangle
       =-2\left(1-\frac{w^2}{\nu^2}\right).''',
    r'''For comparison with the marking that evaluates to one on $C_f$, put
$z_{\rm coh}=(a\nu)^{-1}\alpha_p$. Its homology generator is
$g_{z_{\rm coh}}=(a\nu)s$, with inverse coordinate evaluation by
$z_{\rm coh}$. The simultaneous action conversion gives
\begin{equation}
 z_{\rm coh}[E_p]=-\frac{w^2}{\nu^2},\qquad
 \langle z_{\rm coh}^3,[X]_p\rangle=0,\qquad
 \langle z_{\rm coh}\,\rho_p p_1,[X]_p\rangle
       =-2\left(1-\frac{w^2}{\nu^2}\right).''',
    'The immediately preceding subgroup automorphism uses z as a group element, and earlier physical charts use z as their multiplicative coordinate. Rename only the normalized degree-two cohomology class z to z_coh and its indexed homology generator accordingly. The exact identification z_coh=z=(a nu)^(-1) alpha_p is invertible by restoring the old symbol; the generator remains (a nu)s, evaluation remains one, and all three D.MP8 pairings and subsequent coefficient conversion remain identical.')

add('02LQ-PERIOD-FUNCTION', 'maps:src:D.2.49', 'tag02LQ, analytic period functions',
    r''' \beta&=(-ql(s)-\epsilon(s)/2+B(s^m),-n/2+\epsilon(s)),
\end{split}
\]
where $\Im\tau>0$, $\tau=\tau(s^m)$, and
$\eta(\zeta s)=-\eta(s)$, $\epsilon(\zeta s)=-\epsilon(s)$.
These functions are obtained from the periods:
$\epsilon=\beta_w+n/2$, $\eta=\ell_z+\tau/2$, and
$B=\beta_z+ql+\epsilon/2$. Substitution is the inverse map.''',
    r''' \beta&=(-ql(s)-\epsilon(s)/2+B_{\rm per}(s^m),-n/2+\epsilon(s)),
\end{split}
\]
where $\Im\tau>0$, $\tau=\tau(s^m)$, and
$\eta(\zeta s)=-\eta(s)$, $\epsilon(\zeta s)=-\epsilon(s)$.
These functions are obtained from the periods:
$\epsilon=\beta_w+n/2$, $\eta=\ell_z+\tau/2$, and
$B_{\rm per}=\beta_z+ql+\epsilon/2$. Substitution is the inverse map.''',
    'The theorem fixes the positive integer B=b_0/4, used again in the final global group calculation. The analytic period remainder is renamed B_per. Pointwise B_per(s^m)=B_old(s^m), with inverse renaming; the displayed extraction and reconstruction of beta are unchanged. Its later conjugacy occurrence is changed in the companion row.')
add('02LQ-PERIOD-CONJUGACY', 'maps:src:D.2.49', 'tag02LQ, comparison with D.SL10',
    r'+\frac{jB}{q}-\frac{N\tau}{2m}-F,',
    r'+\frac{jB_{\rm per}}{q}-\frac{N\tau}{2m}-F,',
    'Propagate B_per into the exact translation difference. The first coordinate changes only its symbol B_old to B_per; all coefficients, norm, conjugacy and inverse are unchanged.')

add('02LQ-LINEAR-MAP', 'maps:src:D.2.49', 'tag02LQ, finite linear part',
    r'''Indeed, in the frame given by $\alpha,\lambda$ the finite linear
part is $L(z,w)=(-z-w,w)$. The period equations give''',
    r'''Indeed, in the frame given by $\alpha,\lambda$ the finite linear
part is $\mathsf L(z,w)=(-z-w,w)$. The period equations give''',
    'Retain L for the marked normal torus of D.SL5 and use mathsf L for the finite linear operator. The exact operator is still the 2x2 matrix with rows (-1,-1),(0,1), whose square is identity. All uses in the conjugacy operator are propagated in the companion row.')
add('02LQ-LINEAR-CONJUGACY', 'maps:src:D.2.49', 'tag02LQ, zero-norm gauge',
    r'''Its norm is zero: its invariant first-coordinate part is killed
by $I+L$, and its anti-invariant part lies in the positive
eigenspace of $L$. In general, for such a difference $b(s)$,
put $Th(s)=L^{-1}h(\zeta s)$ and $c=L^{-1}b$. Then
$h_0=m^{-1}\sum_{a=0}^{m-1}aT^ac$ satisfies
$h_0(\zeta s)-Lh_0(s)=b(s)$.''',
    r'''Its norm is zero: its invariant first-coordinate part is killed
by $I+\mathsf L$, and its anti-invariant part lies in the positive
eigenspace of $\mathsf L$. In general, for such a difference $b(s)$,
put $Th(s)=\mathsf L^{-1}h(\zeta s)$ and $c=\mathsf L^{-1}b$. Then
$h_0=m^{-1}\sum_{a=0}^{m-1}aT^ac$ satisfies
$h_0(\zeta s)-\mathsf Lh_0(s)=b(s)$.''',
    'Propagate the same operator L_old=mathsf L through I+L, its eigenspace, inverse, T, and the coboundary equation. T and h_0 therefore remain exactly the original operators/functions; translation by h_0 and subtraction are the same inverse conjugacies.')

add('02LQ-GRAPH-COORDINATE', 'maps:src:D.2.49', 'tag02LQ, central infinite-chain coordinates',
    r'''On the central infinite chain let its graph coordinate have
vertices $i/q$. The long period changes $(t,w)$ by $(1,-n/2)$.
The map $u=w+(n/2)t$, with inverse $w=u-(n/2)t$, gives
central coordinates $u=x+\tau y$ in which
\[
g(t,x,y)=(-t+j/q,\ x-nt+r/k,\ y+N/m).
\]''',
    r'''On the central infinite chain let its graph coordinate
$\theta_{\rm gr}$ have vertices $i/q$. The long period changes
$(\theta_{\rm gr},w)$ by $(1,-n/2)$.
The map $u=w+(n/2)\theta_{\rm gr}$, with inverse
$w=u-(n/2)\theta_{\rm gr}$, gives central coordinates
$u=x+\tau y$ in which
\[
g(\theta_{\rm gr},x,y)=
(-\theta_{\rm gr}+j/q,\ x-n\theta_{\rm gr}+r/k,\ y+N/m).
\]''',
    'D.SL10 already names the fixed translation vector t. Name the scalar graph coordinate theta_gr explicitly. The coordinate identification is (t_old,x,y)->(theta_gr=t_old,x,y), with identical inverse, so the new displayed g is its conjugate by this identity-valued coordinate naming; the u,w maps and proper-power freeness argument remain unchanged.')

add('02LQ-ABELIAN-GENERATOR', 'maps:src:D.2.49', 'tag02LQ, abelianization after D.SL14',
    r'''For $uN+2kv=1$ put $h=ug+v\ell$. The inverse is
$g=Nh-2vR\eta_0$, $\ell=2kh+2uR\eta_0$.
Hence $H_1(U)=\mathbb Z^2$.''',
    r'''For $uN+2kv=1$ put $h_{\rm ab}=ug+v\ell$. The inverse is
$g=Nh_{\rm ab}-2vR\eta_0$, $\ell=2kh_{\rm ab}+2uR\eta_0$.
Hence $H_1(U)=\mathbb Z^2$, in the ordered basis
$(\eta_0,h_{\rm ab})$.''',
    'Retain h in the theorem example k=2h and name the abelian generator h_ab. The inverse integer equations are unchanged; the existing displayed boundary map has second coordinate 2kb+Nc and therefore uses exactly the explicitly stated basis (eta_0,h_ab). The companion group-generator row states its image under abelianization.')

add('02LQ-GROUP-GENERATOR', 'maps:src:D.2.49', 'tag02LQ, group generator and D.SL17',
    r'''For the remaining parity take $uN+2kv=1$ and
$h=g^u\ell^v$. The exact inverse words are
$g=h^N\lambda^{vR}$ and $\ell=h^{2k}\lambda^{-uR}$.
Thus $\Gamma$ is the mapping-torus group of
$\beta\mapsto-\beta-n\lambda$, $\lambda\mapsto\lambda$.
Its integral Wang injection and literal torus section give
\begin{equation}\hypertarget{tag-024F}{}\label{maps:eq:D.SL17}
H_2(\Gamma)=\mathbb Z F\oplus\mathbb Z/2\,T,\qquad
 F=[\lambda,h],\quad T=[\beta,\lambda].''',
    r'''For the remaining parity take $uN+2kv=1$ and
$h_\Gamma=g^u\ell^v$. The exact inverse words are
$g=h_\Gamma^N\lambda^{vR}$ and
$\ell=h_\Gamma^{2k}\lambda^{-uR}$.
Under abelianization, $h_\Gamma$ maps to
$u[g]+v[\ell]=h_{\rm ab}$ for the same $u,v$.
Thus $\Gamma$ is the mapping-torus group of
$\beta\mapsto-\beta-n\lambda$, $\lambda\mapsto\lambda$.
Its integral Wang injection and literal torus section give
\begin{equation}\hypertarget{tag-024F}{}\label{maps:eq:D.SL17}
H_2(\Gamma)=\mathbb Z F\oplus\mathbb Z/2\,T,\qquad
 F=[\lambda,h_\Gamma],\quad T=[\beta,\lambda].''',
    'Name the actual group word h_Gamma and retain all inverse words. For every Bezout pair (u,v), the canonical abelianization sends g^u ell^v to u[g]+v[ell], exactly h_ab for that pair. No distinction of mathematical scope is asserted without this map. The central extension and torus markings are propagated in the following two rows.')
add('02LQ-GROUP-EXTENSION', 'maps:src:D.2.49', 'tag02LQ, central extension after D.SL17',
    r'''$h$ act by
$\beta\mapsto\beta^{-1}\lambda^{-n}$,
$\lambda\mapsto\lambda F^{-1}$.
This is an automorphism since it sends $T$ to $-T=T$.
The semidirect product realizes both central generators.
It evaluates the two-sector bar prism as
$[\beta,h^2]=-nF+nT$.''',
    r'''$h_\Gamma$ act by
$\beta\mapsto\beta^{-1}\lambda^{-n}$,
$\lambda\mapsto\lambda F^{-1}$.
This is an automorphism since it sends $T$ to $-T=T$.
The semidirect product realizes both central generators.
It evaluates the two-sector bar prism as
$[\beta,h_\Gamma^2]=-nF+nT$.''',
    'Propagate h_Gamma into its central-extension action and two-sector bar prism. The automorphism of beta,lambda,F,T is unchanged, so the extension, its generator realization and the D.SL18 torsion coefficient are unchanged.')
add('02LQ-GROUP-EDGE-PERIODS', 'maps:src:D.2.49', 'tag02LQ, fixed-edge periods before D.SL19',
    r'''Their primitive transverse periods are
$h$ and $(\beta g)^u\ell^v
=\beta h-n(u-1)\lambda/2$.
The inverse solves that last equality for $\beta h$.''',
    r'''Their primitive transverse periods are
$h_\Gamma$ and $(\beta g)^u\ell^v
=\beta h_\Gamma-n(u-1)\lambda/2$.
The inverse solves that last equality for $\beta h_\Gamma$.''',
    'Propagate the same group word through both fixed-edge period expressions and their inverse. The exact torus classes D_0->F,D_1->F-T and all subsequent fibre torsion coordinates are unchanged.')

add('02LQ-INTEGER-LIFT', 'maps:src:D.2.49', 'tag02LQ, reduced-component marking D.SL24',
    r'''In the reduced-component marking,
write $j=j_0+hq$, $0\le j_0<q$. Then $g=\beta^hg_0$,
$R=R_0-hq$, and the exact normal-torus change is
\begin{equation}\hypertarget{tag-024N}{}\label{maps:eq:D.SL24}
D=D_{\rm red},\qquad L=L_{\rm red}-hnw .
\end{equation}
Its inverse adds $hnw$, since
$[\delta\beta]=0$ and $[\beta\ell]=nw$.
At $f=0$ the chosen-centre class for $j$ is
$D_0=D_{0,\rm red}+h\tau_2$.
Thus \eqref{maps:eq:D.SL22}, in the reduced-component conductor marking,
has $L=-RD_{0,\rm red}+h\tau_2$.''',
    r'''In the reduced-component marking,
write $j=j_0+h_{\rm lift}q$, $0\le j_0<q$.
Then $g=\beta^{h_{\rm lift}}g_0$, $R=R_0-h_{\rm lift}q$,
and the exact normal-torus change is
\begin{equation}\hypertarget{tag-024N}{}\label{maps:eq:D.SL24}
D=D_{\rm red},\qquad L=L_{\rm red}-h_{\rm lift}nw .
\end{equation}
Its inverse adds $h_{\rm lift}nw$, since
$[\delta\beta]=0$ and $[\beta\ell]=nw$.
At $f=0$ the chosen-centre class for $j$ is
$D_0=D_{0,\rm red}+h_{\rm lift}\tau_2$.
Thus \eqref{maps:eq:D.SL22}, in the reduced-component conductor marking,
has $L=-RD_{0,\rm red}+h_{\rm lift}\tau_2$.''',
    'Keep the theorem example parameter h in k=2h while naming this arbitrary signed component-lift quotient h_lift=(j-j_0)/q. The identity map on that integer, with inverse restoring h_old, propagates through the group word, R, normal-torus coordinate change, inverse addition and the full order-two correction. Every integer lift and all kernel formulas are retained.')

candidate = s
for row in rows:
    assert candidate.count(row['old_text']) == 1, row['change_id']
    candidate = candidate.replace(row['old_text'], row['new_text'], 1)
restored = candidate
for row in reversed(rows):
    assert restored.count(row['new_text']) == 1, row['change_id']
    restored = restored.replace(row['new_text'], row['old_text'], 1)
assert restored == s
for pattern in [r'\\label\{[^}]+\}', r'\\hypertarget\{[^}]+\}']:
    assert re.findall(pattern, candidate) == re.findall(pattern, s)
# Repeated numeric literals in permanent tag labels remain identical too.
numeric_comparison = candidate.replace(r'$(\eta_0,h_{\rm ab})$', r'$\mathrm{basis}$', 1)
assert re.findall(r'\d+', numeric_comparison) == re.findall(r'\d+', s)
fields = ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
with (OUT / 'S6_SERIES_PUBLISH_c9_two_proof_notation_defects.tsv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
print(f'{len(rows)} guarded P15 rows prepared; reverse substitutions recover the exact source.')
print('All existing numeric literals, permanent labels and permanent targets preserved; only added basis notation repeats eta_0; canonical TeX untouched.')
