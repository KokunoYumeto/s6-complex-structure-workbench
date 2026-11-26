#!/usr/bin/env python3
"""Expose the admitted period map and give KL sole homology ownership."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import difflib
import re
import S6_SERIES_PUBLISH_c8_integrate_units as units

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_later'
LATER=ROOT/'agents/continuation8_iii_integration/units/later'
paths={key:LATER/(key+'.tex') for key in ('os49_construction','os49_graph_caps')}
old={key:path.read_text() for key,path in paths.items()}
assert sha256(old['os49_construction'].encode()).hexdigest()=='63791b2110d4a6982a5818280cbb5bd3dfd3d717e6146b70e5c0de569460560e'
assert sha256(old['os49_graph_caps'].encode()).hexdigest()=='bd622ac730f2fed211a3d8ff903b41c9f828190ae2cc9884fd62d29a84cefc2e'
new=dict(old)
rows={key:[] for key in paths}
C,G='os49_construction','os49_graph_caps'

def change(key,before,after,kind,reason,sid):
    assert new[key].count(before)==1,(key,before,new[key].count(before))
    pos=new[key].index(before)
    rows[key].append(dict(type=kind,statement_id=sid,
        old_location=key+'.tex v002 line '+str(new[key][:pos].count('\n')+1),
        old_page='pending final concordance',new_location='same result or explicit bridge placement',
        new_page='pending final build',old_text=before,new_text=after,reason=reason,
        review_status='complete bridge and prior proof read; final exact edit readback pending'))
    new[key]=new[key].replace(before,after)

anchor=r'''\(\ell_0=e_\gamma-e_u=(1,-1,0,0)^t\).
We give the period calculation'''
period=r'''\(\ell_0=e_\gamma-e_u=(1,-1,0,0)^t\).
In the cusp formulas below, \(u=u_h\) is the literal logarithmic
period of \(h\), and \(\gamma=\gamma_g=\Pi(e_\gamma)\) is the
forward suspension period. Their exact relation to the homology
marking is
\[
 \Pi(e_w)=w_Z=(1,0)^t,\quad \Pi(e_\delta)=\delta=(0,1)^t,\quad
 \Pi(e_u)=-u_h+\kappa,\quad
 \kappa=pw_Z+q_\delta\delta,\qquad p,q_\delta\in\mathbb Z.
\]
The gamma column of \(T_C^{-t}\) fixes \(w_Z\); comparison of the
two u increments leaves the displayed integral invariant vector.
Its coefficients are defined at the based regular fibre and
continued as constant integers. In geometric period order
\((\gamma_g,u_h,w_Z,\delta)\), the map and inverse are
\begin{equation}
 F_{p,q}=
 \begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&p&1&0\\0&q_\delta&0&1\end{pmatrix},
 \qquad F_{p,q}^{-1}=F_{p,q}.
 \hypertarget{tag-Q30O}{}\label{os49:eq:based-cusp-period-map}
\end{equation}
For the full unit columns displayed below,
\[
 \Pi(s)=
 \begin{pmatrix}
 -3s+C_1&-2s-U_1+p&1&0\\
 -s+mv+C_2&-s-U_2+q_\delta&0&1
 \end{pmatrix},
 \quad
 \Pi(s+1)=\Pi(s)T_C^{-t}.
\]
The inverse arrow uses \(s-1\) and \(T_C^t\).
In particular the actual finite vector has geometric coordinates
\((n,n,-np,d-nq_\delta)^t\), and its period is
\(n(\gamma_g+u_h-\kappa)+d\delta\). The same \(F_{p,q}\) conjugates
its linear root action and transports its inverse.
We give the period calculation'''
change(C,anchor,period,'D20',
       'Place the already admitted directed-period map at the first cusp use; retain both branch integers, all root characters and the exact inverse instead of identifying e_u with the h period.',
       'night:P3F.27')

ending=r'''The degree \(2mn\) belongs to the full line
clutch.  Its quadratic angular term has zero endpoints and is
independent of \(q\).


\end{proof}'''
ending_new=r'''The degree \(2mn\) belongs to the full line
clutch.  Its quadratic angular term has zero endpoints and is
independent of \(q\).

For the based lift \(u_*=u_h-\kappa=-\Pi(e_u)\), put
\(K_*=K-3\kappa\). Its extending origin is
\(\Omega_{\rm ext,*}=\Omega_{\rm ext}+3nv\kappa\).
The coordinate map and inverse are
\[
 (Z_{\rm ext},V_{\rm ext})\longmapsto
 (r^{3np}Z_{\rm ext},r^{3nq_\delta}V_{\rm ext}),\qquad
 (Z_*,V_*)\longmapsto(r^{-3np}Z_*,r^{-3nq_\delta}V_*).
\]
For \(r\ne0\) these units extend through every cusp chart.
They carry the complete based angular path to
\(n\theta K_*+nm\theta(\theta-1)\delta\), with the same inverse
endpoint arrows. Their q-root difference is zero, so the full
line winding remains \(2mn\).
\end{proof}'''
change(C,ending,ending_new,'D22',
       'Print the admitted unit-frame map carrying the whole angular path to the based period lift, including its inverse and unchanged full root winding.',
       'night:P3F.27')

graph_before=r'''Write \(u_h\) for the logarithmic h-period.  With the forward
gamma and positive delta fixed, the based source marking is
\[
 \Pi(e_w)=w_Z,\quad \Pi(e_u)=-u_h+\kappa_0,\quad
 \kappa_0=pw_Z+q_\delta\delta_V,\qquad p,q_\delta\in\mathbb Z.
\]
The gamma column \(-3w_Z-\delta_V\) fixes the first equation;
the q-increments fix the second up to those two invariant integers.
Set \(u_*=u_h-\kappa_0=-\Pi(e_u)\),
\(H_*=-u_*-\gamma\), \(K_*=3u_*+2\gamma\).'''
graph_after=r'''Use the complete based period map
\eqref{os49:eq:based-cusp-period-map}, and write its retained vector
as \(\kappa_0=pw_Z+q_\delta\delta_V\).
Thus \(u_*=u_h-\kappa_0=-\Pi(e_u)\).
Put \(H_*=-u_*-\gamma\), \(K_*=3u_*+2\gamma\).'''
change(G,graph_before,graph_after,'D11',
       'Give the preceding angular-clutch proof sole ownership of the directed-period derivation; retain here its full root-coordinate shear and its new extensions over the page/compression caps.',
       'night:P3F.31')

bridge=r'''\begin{remark}[The component-supported Type C marking]
\hypertarget{tag-Q30N}{}\label{os49:rem:type-c-marking}
{\normalfont\scriptsize tag Q30N}\par
The source of \eqref{os49:eq:source-cubic} is the source of
\cref{maps:src:D.2.11}: the identity on both Weierstrass charts
carries \(P\) to \(G\), \(Q=3P\) to \(3G\), \(O\) to \(O\), and
\(\mathcal O(P-O)\) to \(M\). The two simple-divisor linearizations
have divisor \(C_0\), so their ratio is a nonzero constant \(c\)
on the compact surface. The scalar map
\(\lambda_{\rm KL}=c^{-1}\lambda\), with inverse
\(\lambda=c\lambda_{\rm KL}\), makes the arrows identical.
The map on the line complement is then the identity.

In the homology order \((\gamma,u,w,\delta)\), the exact change
from the marking of \cref{night:P3F.26} to the index-one Type C
marking of \cref{mapsIII:def:yang-finite-data} is
\[
 G_0=\begin{pmatrix}
 -1&0&0&0\\0&-1&0&0\\0&-1&1&0\\0&0&0&1
 \end{pmatrix},\qquad G_0^{-1}=G_0.
\]
Writing \(A=T_A^{-t}\), \(B=T_B^{-t}\), its products are
\(A_1G_0=G_0A\) and \(A_2G_0=G_0B\).
The period matrix is \(\Pi_Y=\Pi G_0^{-1}\); the map on the
universal \(\mathbb C^2\) and its inverse are the identity.
The actual periods are
\[
 \gamma_Y=-\gamma_g,\qquad u_Y=u_*-w_Z,\qquad
 w_Y=w_Z,\qquad\delta_Y=\delta_V,
\]
where \(u_*=-\Pi(e_u)\) is the based lift in
\eqref{os49:eq:based-cusp-period-map}. Its two branch shifts are
carried by that equation and its inverse.

The rigidified Poincar\'e frame of \cref{maps:src:D.2.12}
has the theta quotient
\(\vartheta(z-\mu)/\vartheta(z)\), whose divisor is \(G-O\)
and whose \(\tau_0\)-multiplier is \(e^{2\pi i\mu}\).
Consequently \(u_*=(\tau_0,\mu)\) and
\(\gamma_g=(-3\mu,\beta_P)\), because the forward arrow covers
\(-3G\). A remaining integral source-period correction would be
fixed by both finite elliptic matrices; the second matrix minus
the identity has determinant one, so this correction is zero.
The line-frame maps are
\(\eta=e^{-2\pi izy_2}\xi\) and
\(\xi=e^{2\pi izy_2}\eta\), with the rigidified lattice
multipliers proved there. Thus
\[
 \Pi_Y=
 \begin{pmatrix}3\mu&\tau&1&0\\\beta&\mu&0&1\end{pmatrix},
 \qquad \tau=\tau_0-1,\quad\beta=-\beta_P .
\]
The cycle change \((w_Z,u_*)\mapsto(w_Z,u_*-w_Z)\) has inverse
\((w_Z,u_Y)\mapsto(w_Z,u_Y+w_Z)\) and determinant one.
The source point \(G\) has value \(\tau_0/3=(\tau+1)/3\)
at \(IV^*\): its negative Abel--Jacobi fixed representative is
\((1/3,0)\) in \((e_u,e_w)=(-u_*,w_Z)\).
Its value at \(II\) is zero. At the cusp both
\(\tau_0-2s\) and \(\mu-s\) are holomorphic, so
\(\mu-\tau/2\) is holomorphic there.

The last two columns of the period equivariance give
\[
 R_1=\begin{pmatrix}-1/\tau&0\\-\mu/\tau&1\end{pmatrix},
 \qquad
 R_2=\begin{pmatrix}1/(\tau+1)&0\\-\mu/(\tau+1)&1\end{pmatrix}.
\]
The first two columns then give
\[
 \begin{aligned}
 \tau\circ g_1&=(\tau-1)/\tau,&
 \mu\circ g_1&=1-\mu/\tau,&
 \beta\circ g_1&=\beta+1-3\mu^2/\tau,\\
 \tau\circ g_2&=-1/(\tau+1),&
 \mu\circ g_2&=\mu/(\tau+1),&
 \beta\circ g_2&=\beta-3\mu^2/(\tau+1).
 \end{aligned}
\]
The finite values and cusp condition therefore identify this
\(\mu\) with \(\mu_C\) by
\cite[Proposition 3.4]{manYang26}; its second affine coordinate
differs from the particular solution by the constant of
\cite[Proposition 3.6]{manYang26}.
At the based fibre, write
\(\beta_P=\Gamma_2+\log\lambda/(2\pi i)\).
The parameter map and inverse are
\[
 c_Y=c_*-\frac{\log\lambda}{2\pi i},\qquad
 \lambda=e^{2\pi i(c_*-c_Y)},\qquad
 c_*=-\Gamma_2-\beta_{C,\mathrm{part}}(z_*).
\]
They use the chosen logarithmic chart; changes of logarithm are
the corresponding integral delta-period changes.
Small \(|\lambda|\) gives the admissible Type C half-plane.

The intermediate \((II,IV^*,I_2)\) marking
in \cref{maps:src:D.2.11} is obtained by the inverse Hurwitz map
\[
 (U,V)\longmapsto(UVU^{-1},U),\qquad
 (M_{II},M_{IV})\longmapsto
 (M_{IV},M_{IV}^{-1}M_{II}M_{IV}).
\]
These specify its based stems from those of \cref{night:P3F.26}.
The lattice map to its period order \((e_1,e_2,\delta,\gamma)\)
and its inverse are
\[
 F_0=\begin{pmatrix}3&2&-1&0\\0&1&0&0\\0&-1&0&1\\1&0&0&0\end{pmatrix},
 \quad
 F_0^{-1}=\begin{pmatrix}0&0&0&1\\0&1&0&0\\-1&2&0&3\\0&1&1&0\end{pmatrix}.
\]
For its displayed \(S\), one has \(S^tF_0=G_0\); these identities
carry the same period columns, rather than changing the source.

For every \(m=3k\), the finite vector map is
\[
 G_0\{n(e_\gamma-e_u)+d e_\delta\}
 =-n(\gamma_Y-u_Y-w_Y)+d\delta_Y .
\]
Thus \((k,n_Y,r_Y)=(k,-n,d)\), with inverse
\((k,n,d)=(k,-n_Y,r_Y)\). The complete coprime domains agree.
In root coordinates the complex point map is the identity, the
real marking map is \(G_0\), and the root coordinate is fixed.
The identities \(A_1G_0=G_0A\) and
\(\Pi_Y(gs)G_0\ell=\Pi(gs)\ell\) carry the affine generator,
its inverse and both logarithmic collar translations exactly.
The positive exterior meridian is fixed; the positive normal
kernel \((\ell,m)\) maps to \((G_0\ell,m)\).

At the cusp the full multiplicative generators become
\(g_Y=g^{-1}\), \(h_Y=h\), with inverse
\(g=g_Y^{-1}\), \(h=h_Y\). Hence their subgroup, all its units
and the scalar are unchanged. Yang's triangles
\(\operatorname{conv}(v,v+e_1,v+e_2)\) and
\(\operatorname{conv}(v+e_1+e_2,v+e_1,v+e_2)\) are the same
negative-diagonal fan used here. The identity on every character
semigroup and its inverse extend across every toric divisor and
node. At \(II\) the source-line quotient is the identical one.
These maps agree on the ordinary overlaps and identify the
completed threefolds with all their specified attaching maps.
\end{remark}

'''
change(C,'\\subsection{Coprime finite caps}\n','\\subsection{Coprime finite caps}\n'+bridge,
       'D12','Insert the complete actual source/period/parameter/root/collar/meridian/fan bridge before the first later use of KL; its full inverse maps establish the overlapping family scope.',
       'os49:rem:type-c-marking')

homology=r'''\begin{equation}
 H_0=H_6=\mathbb Z,\quad H_5=0,\quad
 H_1=H_2=H_3=H_4=\mathbb Z/|n|.
 \hypertarget{tag-Q30D}{}\label{os49:eq:coprime-homology}
\end{equation}'''
statement=r'''For every OS49 cap order $m=3k$ and invariant vector $\ell=n(1,-1,0,0)+d\delta$ with $\gcd(n,m)=1$, the specialization indices are $(m,k,k,m)$ and all four integral Leray differentials are multiplication by $n$. The fundamental group and homology in degrees one through four are $\Z/|n|$. Every $n=\pm1$ member is the standard $S^6$, for every $k$ and $d$.'''
new_statement=r'''For every \(k\in\mathbb Z_{>0}\), \(n,d\in\mathbb Z\), put \(m=3k\) and
\(\ell=n(1,-1,0,0)+d\delta\), with \(\gcd(n,m)=1\).
The finite specialization indices in degrees one through four
are \((m,k,k,m)\), and all four integral Leray differentials
are multiplication by \(+n\) in the marking of
\cref{night:P3F.26}. These caps give a proper holomorphic family
on the punctured parameter disc with \(\lambda=r^m\).
The fundamental group is \(\mathbb Z/|n|\), and
'''+homology+r'''
Every \(n=\pm1\) member is the standard smooth \(S^6\), for all
these \(k\) and \(d\).'''
assert new[C].count(homology)==1
new[C]=new[C].replace(homology,'')
change(C,statement,new_statement,'D13',
       'Place the full retained homology display in the statement and state the separately proved marked indices, signed differentials and actual r-covered holomorphic family.',
       'night:P3F.29')

start=new[C].index('For the fundamental group, the exact reduced boundary kernels kill')
end=new[C].index('\\end{proof}',start)
before=new[C][start:end]
after=r'''Remark~\ref{os49:rem:type-c-marking} identifies this entire
family with \cref{maps:src:D.2.11} by
\((k,n_Y,r_Y)=(k,-n,d)\). Its hypothesis is
\(\gcd(n_Y,3k)=1\), exactly the present hypothesis. Its original
type-\(II\) and index-one toroidal \(I_2\) pieces are the pieces
carried by the displayed root, collar and fan maps. The group
generator maps are \(\gamma\mapsto-\gamma_Y\) and
\(\gamma_Y\mapsto-\gamma\).
That theorem therefore gives the stated fundamental group,
\eqref{os49:eq:coprime-homology} and the smooth sphere conclusion
for \(n=\pm1\). Equivalently, integral duality gives
\[
 H^0=H^6=\mathbb Z,\quad H^1=0,\quad
 H^2=H^3=H^4=H^5=\mathbb Z/|n|.
\]
Together with the complete specialization lattices and the four
signed differentials above, this proves every stated assertion.
'''
change(C,before,after,'D12',
       'Give the earlier KL theorem sole ownership of the overlapping all-3k coprime homology/sphere conclusions after the complete geometric parameter bridge; retain every finite specialization image, signed Leray differential, root/collar inverse and r-family argument.',
       'night:P3F.29')

units.check_permanent_identifiers(old[C],new[C],
    allowed_labels=['os49:eq:based-cusp-period-map','os49:rem:type-c-marking'],
    allowed_targets=['tag-Q30O','tag-Q30N'])
units.check_permanent_identifiers(old[G],new[G])
assert new[C].count('\\begin{proof}')==new[C].count('\\end{proof}')==4
assert new[C].count('\\begin{remark}')==new[C].count('\\end{remark}')==1
for key,path in paths.items():
    table=OUT/('S6_SERIES_PUBLISH_III_'+key+'_publication_defects.tsv')
    with table.open(newline='') as handle:
        reader=csv.DictReader(handle,delimiter='\t')
        fields=reader.fieldnames
        prior=list(reader)
    for row in rows[key]:
        row['change_id']='c8-III-'+key+'-'+str(len(prior)+1).zfill(3)
        prior.append(row)
    path.write_text(new[key])
    with table.open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields,delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(prior)
    (OUT/('S6_SERIES_PUBLISH_III_'+key+'_publication_v003.diff')).write_text(
        ''.join(difflib.unified_diff(old[key].splitlines(True),new[key].splitlines(True),
                                   fromfile=key+'_v002',tofile=key+'_v003')))
print('UTC',datetime.now(timezone.utc).isoformat())
for key in paths:
    print('OUTPUT',key,len(new[key].splitlines()),sha256(new[key].encode()).hexdigest(),
          'NEW_EDITS',len(rows[key]))
print('NEW_IDENTITIES Q30N os49:rem:type-c-marking; Q30O os49:eq:based-cusp-period-map')
print('KL_IS_FULL_COPRIME_HOMOLOGY_OWNER; P29_ALL_MARKED_IMAGES_DIFFERENTIALS_AND_R_FAMILY_RETAINED')
print('ALL_PRIOR_IDENTIFIERS_PRESERVED; NO_SHARED_WRITES; FINAL_WHOLE_READBACK_PENDING')
