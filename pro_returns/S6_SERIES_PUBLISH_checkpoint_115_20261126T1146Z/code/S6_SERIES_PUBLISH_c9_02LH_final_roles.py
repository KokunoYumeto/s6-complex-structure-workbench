#!/usr/bin/env python3
"""Prepare the complete 02LH role repair and its three literal 02LI imports.

All 1675 baseline theorem/proof lines and each direct caller were read.
This program writes only proposals, its operation map and two used-only associations.
The complete source scopes remain outside the checkpoint in scratch tmp.
It has no canonical admission mode.
"""
from collections import Counter
import csv
from datetime import datetime, timezone
import difflib
import json
import re

from S6_SERIES_PUBLISH_c9_backend_notation import Packet, sha
from S6_SERIES_PUBLISH_c9_notation_addendum_io import compose


p = Packet('02LH', 'maps:src:D.2.40',
           '33cbce358737233c6b0305f7591d42e09bf9f124896ac70ba5fc1ccf6480dd0b',
           '366–379', 'Complete candidate07 proof-role review and literal caller transport.',
           image_reader='the global reader')


# Statement and the repeated finite-affine calculation use the same maps.
for first, last in [
    ('At a finite-good site let', 'At a regular site the first condition'),
    ('with the full weighted matrix $A$.', r'\Needspace{5\baselineskip}\n'),
]:
    # The second endpoint is selected explicitly because the literal backslash-n
    # above is never used as a source search string.
    if first.startswith('with the full'):
        last = '\\Needspace{5\\baselineskip}\n\\emph{Peripheral shears'
    p.scope('finite-projected-coordinates-' + str(len(p.operations)+1), first, last,
        compose(p.literals([('Qv', r'Q_{\rm fin}v'),
                            ('w_1', r'w_{{\rm fin},1}'),
                            ('w_2', r'w_{{\rm fin},2}')]),
                p.symbols([('Q', r'Q_{\rm fin}'), ('w', r'w_{\rm fin}')])),
        'Q_fin is exactly H^{-1}F^{-1}N_h and w_fin=Q_fin v in the fixed-lattice coordinates. H and F retain the same primitive image/basis maps and all freeness gcd entries. Q=bG remains the marked elliptic section; the later cusp quotient and period column have their own names. Identity on Z^2 preserves every finite test and section.')

p.scope('raw-return-angular-entry',
        r'Write $B_i,g_i$', 'With the last site omitted, put',
        p.literals([('c_i', r'c_{i,\rm ret}')]),
        'c_{i,ret} is the same bottom angular entry of the marked return matrix, with the identical Tate/additive formulas and integral ordered-product condition. The root paths c_i in the fundamental-group presentation retain their original names and orientations.')

p.scope('tate-frame-definition', 'At \\(I_\\nu\\), choose',
        'At an additive site,',
        compose(p.literals([('uu^t', r'u_{\rm T}u_{\rm T}^t'),
                            (r'\kappa u', r'\kappa u_{\rm T}')]),
                p.symbols([('u', r'u_{\rm T}'), ('r', r'r_{\rm T}')])),
        'u_T,r_T are the same primitive ordered Tate frame in the marked elliptic lattice at the multiplicative site. Its inclusion into Lambda and inverse elliptic coordinates are unchanged; B_i-I=nu u_T u_T^t J_ell and g_i=kappa u_T retain every entry. The free rank r and the separately chosen Bezout scalars are not rebound.')

p.scope('elliptic-minor-matrices', 'With the last site omitted, put',
        r'\emph{The full fibre quotient',
        p.literals([('U_2', r'\mathsf U_2'), ('U_3', r'\mathsf U_3')]),
        'mathsf U_2 and mathsf U_3 are the identical degree-one elliptic relation matrices. Their adjugate sections R_2,R_3 and every inserted column remain unchanged. This font distinguishes these matrices from the cap family U_d, including its weight-one member.')

p.exact('return-word-formal-operators',
        r'''The ordered product of the returns is the identity. The identities
\[
 (MN-I)x=(M-I)Nx+(N-I)x,\qquad
 (M^{-1}-I)x=-(M-I)M^{-1}x
\]''',
        r'''The ordered product of the returns is the identity. For lattice
automorphisms \(M_{\rm word},N_{\rm word}\) and a lattice vector \(x\), the identities
\[
 \begin{aligned}
 (M_{\rm word}N_{\rm word}-I)x
   &=(M_{\rm word}-I)N_{\rm word}x+(N_{\rm word}-I)x,\\
 (M_{\rm word}^{-1}-I)x
   &=-(M_{\rm word}-I)M_{\rm word}^{-1}x
 \end{aligned}
\]''',
        'M_word,N_word are the same two formal lattice automorphisms in the word expansion, acting on x. Both operator identities and the inverse-word relation are unchanged. N remains the number of sites; M in E(M) retains the physical line-bundle role.')

p.scope('degree-one-bezout-pair', 'For integers \\(u,v\\) with',
        r'Put \(M_d=',
        compose(p.literals([('ua+vd', r'u_g a+v_g d'),
                            ('u z_a', r'u_g z_a'), ('vL_d', r'v_g L_d')]),
                p.symbols([('u', 'u_g'), ('v', 'v_g')])),
        'u_g,v_g are precisely the chosen integers with u_g a+v_g d=g. The same linear combination z_g=u_g z_a+v_g L_d R_1 delta maps to g delta. All section and quotient entries remain unchanged; these scalars are separate from the Tate vectors and finite power vector.')

p.scope('fibre-quotient-bezout-pair', r'Put \(\alpha_{\mathrm f}=',
        'The free functional is',
        compose(p.literals([(r'u\alpha', r'u_f\alpha'),
                            (r'v\beta', r'v_f\beta'),
                            ('v x_', 'v_f x_'), ('u x_', 'u_f x_'),
                            ('n(u e_', 'n(u_f e_'), (r'-v\delta', r'-v_f\delta')]),
                p.symbols([('u', 'u_f'), ('v', 'v_f')])),
        'u_f,v_f are exactly the Bezout scalars for alpha_f=a/g and beta_f=db/g. The quotient rows and inverse representatives retain their entries, and their 2-by-2 matrix has determinant u_f alpha_f+v_f beta_f=1. This is a different chosen pair from u_g,v_g; no equality of those choices is asserted.')

p.scope('exterior-group', r'\emph{The marked graph',
        r'\Needspace{5\baselineskip}',
        p.symbols([('G', r'G_{\rm ext}')]),
        'G_ext is the identical semidirect deck group Lambda rtimes F_{N-1}. Its K(G_ext,1) model, both homology maps, and the period-exponential comparison are unchanged. The section generator G in the natural marked row is retained.')

p.exact('semidirect-input-domains',
        r'''Define the semidirect group
\[
       G_{\rm ext}=\Lambda\rtimes F_{N-1},\qquad
       (x,w)(y,z)=(x+A_wy,wz).
\]''',
        r'''Define the semidirect group
\[
       G_{\rm ext}=\Lambda\rtimes F_{N-1},\qquad
       (x,\mathfrak w)(y,\mathfrak z)
          =(x+A_{\mathfrak w}y,\mathfrak w\mathfrak z),
\]
where \(x,y\in\Lambda\) and \(\mathfrak w,\mathfrak z\in F_{N-1}\).
The linear return \(A_{\mathfrak w}\) is the ordered word action.''',
        'The formal semidirect inputs are now typed explicitly: lattice vectors x,y and words fraktur w,z. The product remains the same ordered semidirect product, with the same inverse obtained by the inverse word and its linear action. The group words no longer share the period or line-coordinate names.')

p.scope('semidirect-involution-words',
        'Use the period exponential and its inverse above.',
        r'Write \(\mathfrak a\)',
        p.literals([('(x,w)', r'(x,\mathfrak w)'),
                    ('(-x,w)', r'(-x,\mathfrak w)'),
                    ('(y,z)', r'(y,\mathfrak z)'),
                    ('A_wy', r'A_{\mathfrak w}y'),
                    ('A_w(-y)', r'A_{\mathfrak w}(-y)'),
                    ('wz)', r'\mathfrak w\mathfrak z)')]),
        'The same formal word coordinates are used in the product and involution identities. Both signs on the lattice inputs and every ordered word are retained. Fibre inversion is still its own inverse and has the same +1/-1 actions on the two filtration terms.')

p.scope('involution-lift-elements', 'For every \\(h\\),',
        'Give \\(C_{d}\\)',
        p.symbols([('h', r'h_{\rm ext}'), ('k', r'k_{\rm gr}'),
                           ('x', r'x_{\rm ext}'), ('t', r't_{\rm fib}'),
                           ('c', r'c_{\rm fib}')]),
        'h_ext is the original H_2 exterior class/lift, k_gr its graph coordinate, x_ext its zero-evaluation correction and t_fib=x_ext+iota x_ext its fibre torsion. c_fib is a fibre summand in the splitting or its torsion ambiguity. The subtraction by c_0 and by the unique odd half, both splitting composites and the additivity argument are unchanged.')

p.exact('homology-lift-domain',
        r'For every \(h_{\rm ext}\), \(h_{\rm ext}+\iota h_{\rm ext}\) lies in \(C_d\), and hence',
        r'For every \(h_{\rm ext}\in H_2(V_d;\mathbb Z)\), \(h_{\rm ext}+\iota h_{\rm ext}\) lies in \(C_d\), and hence',
        'This explicitly binds the argument of the existing involution calculation to its stated exterior homology group. It is the same element in the already displayed exact sequence and uses the same fibre injection.')

p.exact('group-cocycle-formal-inputs',
        r'''Give \(C_{d}\) the trivial $G_{\rm ext}$-action; every \(A_{w}\) acts trivially on this
common coinvariant. The function
\[
 c((x,w),(y,z))=[x\wedge A_wy]\in C_d
\]
is an integral group 2-cocycle. Its coboundary on \((x,w),(y,z),(t,u)\)
is
\[
 [y\wedge A_zt-A_wy\wedge A_wA_zt]=0
\]''',
        r'''Give \(C_{d}\) the trivial $G_{\rm ext}$-action; every \(A_{\mathfrak w}\) acts trivially on this
common coinvariant. For the same semidirect inputs define
\[
 \mathfrak c_{\wedge}((x,\mathfrak w),(y,\mathfrak z))
       =[x\wedge A_{\mathfrak w}y]\in C_d .
\]
This is the integral group 2-cocycle. On the third input
\((z_{\Lambda},\mathfrak v)\), with \(z_{\Lambda}\in\Lambda\)
and \(\mathfrak v\in F_{N-1}\), its coboundary is
\[
 [y\wedge A_{\mathfrak z}z_{\Lambda}
   -A_{\mathfrak w}y\wedge A_{\mathfrak w}A_{\mathfrak z}z_{\Lambda}]=0
\]''',
        'fraktur c_wedge is the same integral 2-cocycle on G_ext, with the original ordered action and wedge. The third formal lattice vector is z_Lambda and its base word is fraktur v. The four coboundary terms reduce to the identical displayed coinvariant relation. The core, roof and Chern objects formerly called c receive their own names.')

p.scope('anti-invariant-class-reading', r'If \(y=s_\iota(k)\)',
        'The edge projection gives',
        p.symbols([('y', r'y_{\rm ext}'), ('k', r'k_{\rm gr}'),
                   ('c', r'c_{\rm fib}')]),
        'y_ext=s_iota(k_gr) is the same anti-invariant exterior class, and c_fib the same fibre summand. Its q_d value and unique half remain zero; the splitting and both inverse-coordinate assignments are unchanged.')

p.scope('fixed-normal-formal-input', 'A literal fixed normal is',
        'When \\(A_i(d)^m=I\\)',
        p.symbols([('u', r'\lambda_{\rm fix}')]),
        'lambda_fix is the fixed lattice vector in the literal commuting-pair torus. Its identity inclusion and J_i insertion preserve the exact normal class and zero fibre/torsion coordinates. This formal fixed-vector input is not the named primitive Tate frame.')

p.exact('fixed-normal-input-domain',
        r'''A literal fixed normal is the commuting pair
\((\lambda_{\rm fix},1),(0,\mathfrak m_i)\).''',
        r'''For \(\lambda_{\rm fix}\in\ker(A_i(d)-I)\), the literal fixed normal is the commuting pair
\((\lambda_{\rm fix},1),(0,\mathfrak m_i)\).''',
        'The displayed fixed-normal argument is explicitly in the fixed lattice already used to define J_i. The torus parametrization and orientation are unchanged.')

# All finite data retain the same site and its original h,m,v.
p.scope('finite-projector-and-coordinates', 'with the full weighted matrix $A$.',
        '\\Needspace{5\\baselineskip}\n\\emph{Peripheral shears',
        compose(p.literals([('QR_\\pi', r'Q_{\rm fin}R_\pi'),
                            ('Fz', r'Fz_{\rm fix}'), ('hz', r'hz_{\rm fix}'),
                            ('Hw', r'Hw_{\rm fin}'), ('jw/m', r'jw_{\rm fin}/m'),
                            ('m=hk', r'm=hk_{\rm fin}')]),
                p.symbols([('P', r'P_{\rm fix}'), ('z', r'z_{\rm fix}'),
                           ('t', r't_{\rm fin}')])),
        'P_fix=N_h/h is the original rational projector onto the fixed plane, z_fix the coordinate column in its primitive fixed basis, k_fin=m/h and t_fin the same gcd of m and w_fin components. All finite-power tests, integer lifts and affine maps retain their entries. P=aG remains the section, and the ring/time/torus parameters receive explicit distinct roles.')

p.scope('finite-affine-translation', 'Every affine lift with this power is included.',
        'For the holomorphic\nroot-disc family',
        compose(p.literals([(r'\tau_y', r'\tau_{y_{\rm aff}}')]),
                p.symbols([('y', r'y_{\rm aff}')])),
        'y_aff is the identical vector (I-A)^{-1}(alpha-v/m) on the moving plane. The displayed conjugacy by translation and its negative inverse retain exactly the same affine displacement and linear return.')

p.scope('finite-core-generator', 'The exact core degree-one presentation is',
        'Free data exist at every position.',
        p.literals([('\\mathbb Zc', r'\mathbb Zc_{\rm core}'),
                    ('mc-v', r'mc_{\rm core}-v')]),
        'c_core is the identical positive root path in the core H_1 presentation. Its lattice displacement, root sheet and relation m c_core-v are unchanged. The full Thom map and its torsion relations retain all five columns; later c_i records the same positive root path at site i.')

p.exact('finite-root-normal-parameters',
        r'''The covering-loop normal torus is the commuting pair computed above. The root normal has parametrization
\([uv/m,e^{2\pi i(u/m+t_{\rm fin})}]\), zero fibre parallelogram
and edge displacement $v$. This proves all five columns.''',
        r'''The covering-loop normal torus is the commuting pair computed above. The root normal has parametrization
\([s_{\rm root}v/m,e^{2\pi i(s_{\rm root}/m+t_{\rm nor})}]\),
where \(s_{\rm root},t_{\rm nor}\) are its two oriented circle parameters.
It has zero fibre parallelogram and edge displacement $v$.
This proves all five columns.''',
        's_root,t_nor are the same two formal circle parameters of the root normal, replacing the old u,t only in this parametrization. The first vector remains the parameter times v/m and the phase the identical parameter/m plus normal angle. Orientation and every Thom coefficient are unchanged; t_fin remains only the finite gcd.')

p.scope('peripheral-fixed-vector-argument', r'\emph{Peripheral shears',
        r'\emph{The period cover',
        p.symbols([('u', r'\lambda_{\rm fix}')]),
        'The peripheral normal argument lambda_fix is the fixed lattice input of t_i. The added wedge, norm transpose identity and subtraction inverse are unchanged. The named Tate vector keeps its own name.')

p.scope('smith-basis-maps', 'Here is an integer implementation with inverse coordinates.',
        r'\emph{The cusp:',
        compose(p.literals([('U(Q_1', r'U_{\rm SNF}(Q_1'),
                            ('S_d)V', r'S_d)V_{\rm SNF}'),
                            ('d_r', r'd_{r_{\rm SNF}}')]),
                p.symbols([('V', r'V_{\rm SNF}')])),
        'U_SNF,V_SNF are the same unimodular left/right Smith matrices for Q_1 wedge^2 S_d, and r_SNF indexes its nonzero diagonal entries. The last columns and inverse rows remain the kernel coordinate maps; the cap family U_d and free rank r keep their original roles.')
p.exact('smith-rank-domain',
        'primitive basis below. Compute the reversible Smith decomposition',
        r'''primitive basis below. Write \(r_{\rm SNF}\) for the number of nonzero
Smith entries and compute the reversible decomposition''',
        'r_SNF is the same rank of Q_1 wedge^2 S_d, explicitly the number of its nonzero Smith entries. The public free rank r of H_1 is unchanged.')

p.exact('nearby-fibre-object',
        r'\quad\text{on }H_2(F_1).',
        r'\quad\text{on }H_2(\mathcal F_1),',
        'mathcal F_1 denotes the same nearby weight-one torus, whose H_2 basis is wedge^2 Lambda. It has the identity marked period identification used by the cover/transfer square; F_i retains the fixed lattice of A_i(d).')
p.exact('nearby-fibre-binding',
        'The same construction on the nearby torus\ngives',
        r'''The same construction on the nearby torus \(\mathcal F_1\)
gives''',
        'This binds the newly font-qualified nearby fibre in the transfer formula to the actual torus already used in the covering-square construction.')

p.scope('cusp-matrix-and-quotient', r'\emph{The cusp:',
        r'\emph{Zero-Chern originals',
        compose(p.literals([('Ce_1', r'C_{\rm cusp}e_1'),
                            ('Ce_2', r'C_{\rm cusp}e_2')]),
                p.symbols([('C', r'C_{\rm cusp}'), ('Q', r'Q_{\rm cusp}')]),
                p.literals([(r'\sigma', r'\sigma_{\rm cusp}'),
                            ('(u,', r'(u_{\rm T},'),
                            ('(r,', r'(r_{\rm T},')])),
        'C_cusp is the identical determinant-one selected-cusp period matrix. Q_cusp and sigma_cusp retain the quotient row (y12,y23-d y14,y24,y34) and its zero-insertion section, with relation-coordinate inverse (y13,y14). The short/long period maps use the same primitive Tate frame u_T,r_T. The finite projector coordinates and the elliptic section Q are not reassigned.')

p.scope('cusp-coefficient-indeterminate',
        r'The normalization complex of Theorem~\ref{maps:src:D.2.34}',
        'The period basis',
        p.symbols([('t', r't_{\rm ring}')]),
        't_ring is the same cyclic coefficient indeterminate of Z[t_ring]/(t_ring^d-1). Its chain identification with the cited t_cyc fixes every indexed component, branch and torus cell. The matrix entries, unit reductions and partial-sum inverse are unchanged; this indeterminate is separate from every geometric time parameter and the final torus class.')

p.exact('cusp-period-coordinate-basis',
        r'''The period basis
\[
 (S_{\mathrm{sh}}C_{\rm cusp}e_1,S_{\mathrm{lg}}e_1,S_{\mathrm{sh}}C_{\rm cusp}e_2,S_{\mathrm{lg}}e_2)
\]
has the inverse \(C_{\rm cusp}^{-1}\) on the short coordinates and the
identity on the long coordinates. The return in it is
\(I+E_{12}+d E_{34}\). In wedge order \(12,13,14,23,24,34\),''',
        r'''Write \(\varepsilon_1^{(2)},\varepsilon_2^{(2)}\) for the standard
coordinate columns of the two short and two long period maps. The ordered basis is
\[
 \begin{aligned}
 \mathsf e_1^{\rm C}&=S_{\mathrm{sh}}C_{\rm cusp}\varepsilon_1^{(2)},&
 \mathsf e_2^{\rm C}&=S_{\mathrm{lg}}\varepsilon_1^{(2)},\\
 \mathsf e_3^{\rm C}&=S_{\mathrm{sh}}C_{\rm cusp}\varepsilon_2^{(2)},&
 \mathsf e_4^{\rm C}&=S_{\mathrm{lg}}\varepsilon_2^{(2)}.
 \end{aligned}
\]
In coordinates relative to \((u_{\rm T},r_{\rm T},\delta,\gamma)\), its map and inverse read
\[
 \begin{gathered}
 \binom{x_u}{x_\delta}=C_{\rm cusp}\binom{x_1^{\rm C}}{x_3^{\rm C}},
 \qquad x_r=x_2^{\rm C},\quad x_\gamma=x_4^{\rm C},\\
 \binom{x_1^{\rm C}}{x_3^{\rm C}}=C_{\rm cusp}^{-1}\binom{x_u}{x_\delta}.
 \end{gathered}
\]
The return in this basis is \(I+E_{12}+d E_{34}\).
Put \(\mathsf e_{jk}^{\rm C}=\mathsf e_j^{\rm C}\wedge\mathsf e_k^{\rm C}\).
The following \(y_{jk}\) are coordinates in its wedge basis, in order
\(12,13,14,23,24,34\):''',
        'The four cusp period vectors are the same ordered columns as before. The short coordinate map is C_cusp and its inverse C_cusp^{-1}; the two long coordinates are fixed. The named wedge columns now explicitly carry this basis, so the later exterior e1,e2 still denote the original elliptic vectors. Both products of the unchanged short matrices are identity, and the induced wedge map preserves the exact return, quotient, section and normal-disc coordinates.')

p.scope('cusp-wedge-coordinate-family', 'the relation image has the primitive basis',
        'For completeness the component-disc map',
        p.literals([('e_{13}', r'\mathsf e_{13}^{\rm C}'),
                    ('e_{14}', r'\mathsf e_{14}^{\rm C}'),
                    ('e_{23}', r'\mathsf e_{23}^{\rm C}'),
                    ('e_{24}', r'\mathsf e_{24}^{\rm C}'),
                    ('e_{12}', r'\mathsf e_{12}^{\rm C}'),
                    ('e_{34}', r'\mathsf e_{34}^{\rm C}'),
                    ('e_2', r'\mathsf e_2^{\rm C}'),
                    ('e_3', r'\mathsf e_3^{\rm C}'),
                    ('e_4', r'\mathsf e_4^{\rm C}')]),
        'Every cusp wedge generator, preimage, quotient-section output and degree-one boundary generator is transported through the explicitly stated cusp basis. All coefficients 1,d and the relation-coordinate inverse are identical. The matrix units E12,E34 remain the coordinate endomorphisms in that basis.')

p.scope('cusp-component-vertices', 'For completeness the component-disc map',
        'In the exterior,',
        p.literals([('v_j', r'v_{j,\rm C}'),
                    ('C_{\\rm cusp} e_2', r'C_{\rm cusp}\varepsilon_2^{(2)}'),
                    ('C_{\\rm cusp}e_2', r'C_{\rm cusp}\varepsilon_2^{(2)}')]),
        'v_{j,C}=j C_cusp epsilon_2 is the same selected-cusp vertex. Its normal ray (v_{j,C},1), every character evaluation and its positive boundary class are unchanged. The standard short-coordinate column is now explicit, and the finite power family v_i retains its original lattice meaning.')

p.exact('toric-normal-character-arguments',
        r'''height-one toric lattice is \((v_{j,\rm C},1)\). A character \((m,k)\)
restricts to the normal disc as a nonzero unit times
\(t^{\langle m,v_{j,\rm C}\rangle+k}\).''',
        r'''height-one toric lattice is \((v_{j,\rm C},1)\). A character
\((m_{\rm ch},k_{\rm ht})\) restricts to the normal disc, with coordinate
\(t_{\rm disc}\), as a nonzero unit times
\(t_{\rm disc}^{\langle m_{\rm ch},v_{j,\rm C}\rangle+k_{\rm ht}}\).''',
        'm_ch is the same short dual-lattice character and k_ht its integer height coefficient. t_disc is its positive normal-disc parameter. The exponent, winding, ray recovery and sign are unchanged; the logarithmic order m, graph coordinate k and coefficient-ring indeterminate have separate roles.')

p.scope('cusp-boundary-coordinate-generators',
        'In the cusp boundary degree-one marking,', 'In the exterior,',
        p.literals([('\\mu+j e_3', r'\mu+j\mathsf e_3^{\rm C}'),
                    ('d e_3=(A_d-I)e_4', r'd\mathsf e_3^{\rm C}=(A_*(d)-I)\mathsf e_4^{\rm C}')]),
        'The cusp component-disc boundaries use the same third cusp-basis period and the same selected return A_*(d). Its relation d e3^C=(A_*(d)-I)e4^C supplies the original monodromy bounding cylinder. This is the earlier coordinate change applied to the whole boundary map, not a new boundary assertion.')

p.exact('relative-disc-coefficient-basis',
        r'''For \(d>1\), an integral basis is
\[
 d(e_1-e_0),\qquad
 e_j-j e_1+(j-1)e_0\quad(2\leq j<d).
\]''',
        r'''Let \(\varepsilon_j^{\rm disc}\) be the coefficient vector of the
\(j\)th positive component disc. For \(d>1\), an integral kernel basis is
\[
 \begin{gathered}
 d(\varepsilon_1^{\rm disc}-\varepsilon_0^{\rm disc}),\\
 \varepsilon_j^{\rm disc}-j\varepsilon_1^{\rm disc}
        +(j-1)\varepsilon_0^{\rm disc}\quad(2\leq j<d).
 \end{gathered}
\]''',
        'epsilon_j^disc denotes the same standard coefficient of the jth relative normal disc. The two kernel conditions and all integer coefficients d,-j,j-1 are unchanged; the original inverse reads x_j for j>=2 and (sum j x_j)/d. These relative-disc coefficients are no longer denoted by the physical period symbols.')

p.scope('cusp-angular-bezout', 'Choose \\(s,t\\) with',
        r'\emph{Zero-Chern originals',
        compose(p.literals([('s c_{22}', r's_{\rm Bez}c_{22}'),
                            ('t g', r't_{\rm Bez}g')]),
                p.symbols([('s', r's_{\rm Bez}'), ('t', r't_{\rm Bez}')])),
        's_Bez,t_Bez are the identical integers solving s_Bez c22+t_Bez g=1. Their disc-difference and g-delta boundary combination still reconstructs exactly delta. The component counts, time slots and free fibre generator retain separately bound names.')

p.exact('flat-line-holonomies',
        r'''Here are the gauges. On the universal cover of a graph
circle with flat holonomy $h$, choose $\ell_h$ with
$e^{\ell_h}=h$ and replace the line coordinate $w$ by
$e^{-s\ell_h}w$. The inverse multiplies by $e^{s\ell_h}$.
For an additional return holonomy $h'$, choose
$e^{\ell_{h'}}=h'$ and use $e^{-s\ell_h-t\ell_{h'}}w$.''',
        r'''Here are the gauges. On the universal cover of a graph
circle with flat holonomy $h_{\rm hol}$, choose $\ell_{\rm hol}$ with
$e^{\ell_{\rm hol}}=h_{\rm hol}$ and replace the line coordinate $w_{\rm line}$ by
$e^{-s_{\rm gau}\ell_{\rm hol}}w_{\rm line}$.
The inverse multiplies by $e^{s_{\rm gau}\ell_{\rm hol}}$.
For an additional return holonomy $h'_{\rm hol}$, choose
$e^{\ell'_{\rm hol}}=h'_{\rm hol}$ and use
$e^{-s_{\rm gau}\ell_{\rm hol}-t_{\rm gau}\ell'_{\rm hol}}w_{\rm line}$.
Here $s_{\rm gau},t_{\rm gau}$ are the two real deck coordinates.''',
        'h_hol,h_hol prime are the same nonzero complex scalar holonomies and ell_hol,ell_hol prime their chosen logarithms. The line coordinate w_line and deck arguments s_gau,t_gau retain the original exponential factors and reciprocal inverses. The finite order h and long period h_N are no longer rebound.')

p.exact('line-endpoint-map-inputs',
        r'''For a line mapping torus with endpoint
\((w,x,1)\sim(u(x)w,t x,0)\), the map
\[
 [w,x,s]\longmapsto[e^{\zeta(s)\log u(x)}w,x,s]
\]''',
        r'''For the line mapping torus, write $T_{\rm base}$ for its base
return and $u_{\rm hol}(x)$ for its nonvanishing endpoint line multiplier
at a plumbing point $x$. Its endpoint is
\((w_{\rm line},x,1)\sim(u_{\rm hol}(x)w_{\rm line},T_{\rm base}x,0)\).
The map
\[
 [w_{\rm line},x,s]\longmapsto
   [e^{\zeta(s)\log u_{\rm hol}(x)}w_{\rm line},x,s]
\]''',
        'T_base is the same base translation in the original endpoint relation, u_hol its same nonvanishing line multiplier, and x its plumbing-point input. The displayed line map and inverse negative exponent are unchanged on that same mapping torus; no new return or trivialization is asserted.')

p.scope('positive-roof-slope', 'On the compact plumbing collar choose',
        'The central fibre is an integral homology retract',
        compose(p.literals([('ct+', r'c_{\rm roof}t+'),
                            ('cr_d', r'c_{\rm roof}r_d'),
                            ('ct\\)', r'c_{\rm roof}t\)')]),
                p.symbols([('c', r'c_{\rm roof}')])),
        'c_roof is the identical positive scalar with c_roof max r_d<1. Both endpoint slopes, the strictly positive derivative, the monotone map f_x and its inverse are preserved. The core root and component Chern map have separate names.')

p.exact('roof-formal-domains',
        r'''Put \(\Phi(s)=\int_0^s\phi(t)\,dt\) and
\[''',
        r'''Put \(\Phi(s)=\int_0^s\phi(t)\,dt\). Here $s$ is the unit-interval
coordinate, and $t$ in the roof map ranges from $0$ to $r_d(x)$:
\[''',
        'The original formal arguments of Phi and f_x are explicitly typed by their intervals and the fixed plumbing point x. The definite integral and roof-coordinate formula remain the same, and f_x inverse remains its stated monotone inverse.')

p.scope('additive-component-count', 'An additive central fibre has',
        'For a multiplicative fibre,',
        p.literals([('\\mathbb Z^{s}', r'\mathbb Z^{s_i}')]),
        's_i is the component count at the current additive site, already defined in the theorem input. This is the same component basis and permutation; only the previously unindexed count is made consistent with that indexed input.')

p.scope('rank-one-tate-inputs-and-bezout', 'At a narrow unselected',
        'In the one-dimensional fan',
        compose(p.literals([("u'=u-", r"u'_N=u_{\rm T}-"),
                            ("u'\\otimes", r"u'_N\otimes"),
                            ("(u',", r"(u'_N,"),
                            ('xr+', r'x_N r_{\rm T}+'),
                            (r'y\gamma', r'y_N\gamma'),
                            ('(r,', r'(r_{\rm T},')]),
                p.symbols([('r', r'r_{\rm T}'), ('x', 'x_N'), ('y', 'y_N'),
                           ('l', 'l_N'), ('h', 'h_N'), ('p', 'p_N'), ('w', 'w_N')]),
                p.literals([('A_d-I', 'A_i(d)-I')])),
        'The narrow basis (l_N,h_N,p_N,w_N) is the same ordered tuple (u_T-(a kappa/nu)delta, x_N r_T+y_N gamma, delta, -(db kappa/r0)r_T+(nu/r0)gamma). x_N,y_N are the same Bezout scalars. Its long inverse matrix and short addition inverse are unchanged, giving return I+r0 E12. These four names retain one period role throughout all subsequent specialization and kernel formulas.')

p.scope('rank-one-specialization-family', 'Its degree-two specialization is explicitly',
        'For non-narrow $P$',
        p.symbols([('l', 'l_N'), ('h', 'h_N'), ('p', 'p_N'), ('w', 'w_N')]),
        'The four degree-two maps and both saturated/unsaturated kernel bases use the identical narrow period basis. The target component sum, residual torus and graph products are unchanged. The same coordinate-reading section and remaining component differences remain the inverse.')

p.scope('residual-node-translation',
        'The remaining\ntranslation has a lift',
        'Constant nonzero multipliers',
        p.literals([(r'\tau', r'\tau_{\rm node}')]),
        'tau_node is the same R^2 lift of the remaining residual-torus node translation. Addition of s tau_node and subtraction are the original inverse maps on the gluing circle. The exact-order-two fibre class later in the proof has its own name.')

p.scope('non-narrow-period-complement', 'For non-narrow $P$',
        'Changing any chosen logarithm',
        compose(p.literals([(r'\nu u-', r'\nu u_{\rm T}-'),
                            ('xu+', r'x_P u_{\rm T}+'),
                            (r'z\delta', r'z_P\delta'),
                            (r'\kappa x+', r'\kappa x_P+'),
                            (r'\nu z=', r'\nu z_P=')]),
                p.symbols([('r', r'r_{\rm T}')])),
        'x_P,z_P are the same short-complement Bezout scalars with a kappa x_P+nu z_P=1. p_0,beta_0 and ell_d retain their exact period columns. The inverse short matrix and subtraction of the long shear preserve the same rank-one map and all four primitive specializations.')

p.scope('logarithm-branch-integer', 'Changing any chosen logarithm',
        r'\emph{Nonzero-Chern originals',
        p.symbols([('k', r'k_{\rm branch}')]),
        'k_branch is the same integer change of a chosen logarithm by 2 pi i times that integer. The elementary period shear and subtraction inverse are unchanged, as are their exterior squares on the specialization maps. It is separate from the logarithmic-cap count k.')

p.scope('component-chern-map-and-index', r'\emph{Nonzero-Chern originals.}',
        'For an additive matrix let',
        compose(p.literals([('C_p', r'C_{p_{\rm Ch}}'),
                            (' c=', r' c_{\rm Ch}='),
                            ('$c$', r'$c_{\rm Ch}$'),
                            (r'\ker c\)', r'\ker c_{\rm Ch}\)'),
                            (r'\(c:', r'\(c_{\rm Ch}:')]),
                p.symbols([('p', r'p_{\rm Ch}'),
                           ('F', r'F_{\rm mult}')]),
                p.literals([('^s', '^{s_i}'), ('^{s-1}', '^{s_i-1}'),
                            ('^{2s-1}', '^{2s_i-1}')])),
        'c_Ch=C_{p_Ch}^*-C_0^* is the identical primitive component Chern homomorphism. p_Ch is the same nonzero multiplicity-one component index and F_mult the same full multiplicity vector. Its kernel basis, inverse coordinates x0 and xj-mu_j x0, section C_{p_Ch}, all free groups and product maps are unchanged. The component count is the indexed input s_i; the core/roof/cocycle c roles and rank-one period p_N are separately named.')

p.scope('additive-gysin-period-vector', 'For an additive matrix let',
        r'\emph{The elliptic image',
        compose(p.literals([('dbz_1', r'db z_{{\rm ell},1}'),
                            ('dbz_2', r'db z_{{\rm ell},2}'),
                            ('az_2', r'a z_{{\rm ell},2}'),
                            ('az_1', r'a z_{{\rm ell},1}'),
                            ('bz', r'b z_{\rm ell}'),
                            ('R_d', r'\mathsf R_d'),
                            (r'\rho', r'\rho_{\rm Gys}'),
                            ('s-2', 's_i-2')]),
                p.symbols([('z', r'z_{\rm ell}'), ('B', 'B_i')])),
        'z_ell=(B_i-I)^{-1}g_i is the same rational vector for the actual indexed additive return. mathsf R_d has the identical last-column shear and subtraction inverse. rho_Gys=q_comp(a z_ell,2,-a z_ell,1,1) is the same primitive covector, with the same v0 section and extra wedge generator. All entries, weight transport and evaluated signs are retained; rho(d) remains the component-orbit count function.')

p.exact('additive-indexed-matrix-binding',
        r'For an additive matrix let \(z_{\rm ell}=(B_i-I)^{-1}g_i\).',
        r'At the additive site use its indexed elliptic return \(B_i\) and put \(z_{\rm ell}=(B_i-I)^{-1}g_i\).',
        'This explicitly identifies the old unindexed additive B with the same B_i from the opening marked-return data, by identity on that elliptic lattice and cocycle. The later full relation matrix is independently named B_rel.')

p.scope('elliptic-image-matrix', r'\emph{The elliptic image',
        r'\emph{All unchanged fixed-normal',
        compose(p.literals([('ER_E', r'E_{\rm ell}R_{\rm ell}'),
                            ('R_E', r'R_{\rm ell}'),
                            ('E_J', r'E_{{\rm ell},J}')]),
                p.symbols([('E', r'E_{\rm ell}')])),
        'E_ell is the same complete two-row elliptic relation matrix, with the same minors, adjugate section R_ell and quotient zero. The integer image preimages in OW7 and every angular-wedge preimage are unchanged. E_log later denotes the actual finite-first space, and E(M) remains the circle bundle of the physical line.')

p.scope('elliptic-vanishing-word-pair', 'Their two selected vanishing words,',
        'Every return fixes',
        p.symbols([('u', r'u_{\rm van}'), ('v', r'v_{\rm van}')]),
        'u_van=(1,1) and v_van=(-4,-1) are the identical two selected vanishing words in the elliptic lattice. Their two literal (B_II-I) preimages, index-three quotient and inclusion into im E_ell are unchanged. They are the same pair imported later into the fundamental-group proof; no Tate or finite-power vector is renamed to these words.')

p.scope('additive-fixed-lattice-and-period', 'At an additive original the fixed lattice is',
        'At a nonzero-Chern multiplicative original,',
        compose(p.literals([('F_d', 'F_{i,d}'),
                            ('dbz_1', r'db z_{{\rm ell},1}'),
                            ('dbz_2', r'db z_{{\rm ell},2}'),
                            ('dbz', r'db z_{\rm ell}')]),
                p.symbols([('z', r'z_{\rm ell}')])),
        'F_{i,d} is the same fixed lattice at this additive site and weight, generated by delta and its primitive return period. z_ell is the identical rational vector (B_i-I)^{-1}g_i, and its denominator gives the same return length. The inverse reads x_delta and x_gamma/g_ret,d; the orbit tube, endpoint unit and normal-disc families are unchanged.')

p.exact('additive-fixed-lattice-input',
        'At an additive original the fixed lattice is',
        r'''At an additive original, put \(z_{\rm ell}=(B_i-I)^{-1}g_i\)
for this site's indexed return and cocycle. Its fixed lattice is''',
        'The z_ell used in the general additive fixed-lattice formula is explicitly evaluated from the same input family (B_i,g_i), also at zero-Chern sites. It agrees with the preceding nonzero-Chern specialization at every site whose component order divides b. The identity is on the original two elliptic coordinates.')

p.scope('multiplicative-geometric-normal-frame',
        'At a nonzero-Chern multiplicative original,',
        'Finally, the Wang sequence',
        compose(p.symbols([('u', r'u_{\rm T}'), ('r', r'r_{\rm T}')]),
                p.literals([('J_iF_d', 'J_iF_{i,d}')])),
        'The geometric normal and its rim use the same primitive Tate vectors u_T,r_T as the local cap model. Subtracting and adding the same rim are unchanged inverse normal maps. J_iF_{i,d} is the same full fixed-lattice image, with the cap site and weight made explicit.')

p.exact('general-fixed-lattice-binder',
        r'''Hence the full global
normal image is
\[
                         (0,J_iF_{i,d}).
\]''',
        r'''Hence the full global
normal image is
\[
                         (0,J_iF_{i,d}),\qquad F_{i,d}=\ker(A_i(d)-I)=F_i.
\]''',
        'The indexed fixed-lattice family is explicitly identified with F_i from the theorem input at the same site and weight. This identity on each fixed lattice keeps the complete normal image, inverse period shear and all torsion coordinates unchanged.')

p.scope('local-return-period-family', r'\emph{Zero-Chern originals',
        r'\emph{Relative normal discs',
        p.literals([(r'\ell_d', r'\ell_{i,d}'),
                    ('g_d', 'g_{i,d}'), ('k_d', 'k_{i,d}'), ('k_1', 'k_{i,1}')]),
        'ell_{i,d} denotes the same primitive long return at cap i and weight d; g_{i,d} is its same return length. k_{i,d} is the same extra Gysin kernel generator at that cap. This makes the site parameter explicit throughout zero-Chern, narrow/non-narrow and additive cap calculations. The identities wedge^2 S_d k_{i,d}=d k_{i,1}, all line-flow products and their inverse coordinates are unchanged.')

p.exact('wang-local-return',
        r''' 0\longrightarrow\operatorname{coker}(\Lambda^2A_d-I)
 \longrightarrow H_2(\partial U_d)
 \longrightarrow\ker(A_d-I)\longrightarrow0.''',
        r''' 0\longrightarrow\operatorname{coker}(\Lambda^2A_i(d)-I)
 \longrightarrow H_2(\partial U_d)
 \longrightarrow\ker(A_i(d)-I)\longrightarrow0.''',
        'The boundary Wang return is explicitly the same A_i(d) at the cap under discussion. Its wedge cokernel, fixed lattice and integral section are unchanged; no separate unindexed A_d is introduced.')

p.scope('component-order-parameter',
        r'\emph{Nonzero-Chern originals.}', None,
        p.symbols([('q', r'q_{\rm comp}')]),
        'q_comp is the identical additive component-group order in divisibility, covector, denominator and Gysin-evaluation formulas. The base-coordinate use in the relative-disc equation is separately bound below. No integer value or allowed cap choice changes.')

p.exact('relative-disc-local-base',
        r'''base equation is \(q_{\rm comp}=t^{\mu_C}\epsilon(t)\), with \(\epsilon\)
nonvanishing.''',
        r'''base equation is \(q_{\rm base}=t_{\rm disc}^{\mu_C}\epsilon_{\rm unit}(t_{\rm disc})\),
where \(t_{\rm disc}\) is the normal-disc coordinate and
\(\epsilon_{\rm unit}\) is nonvanishing.''',
        'q_base is the same local base parameter and t_disc the same positive normal-disc coordinate. epsilon_unit is the identical nonzero local unit; the multiplicity exponent mu_C and winding/meridian map are unchanged. q_comp retains its component-order meaning, and epsilon remains the exterior edge projection.')

p.exact('relative-disc-line-coordinate',
        r'\((2\pi i)^{-1}\int d\log w\), including the marked',
        r'\((2\pi i)^{-1}\int d\log w_{\rm line}\), including the marked',
        'w_line is the same nonvanishing cut line coordinate used in the preceding flat gauges. Its logarithmic winding and all period-transition jumps are unchanged. The fixed rank-one period w_N and finite vector w_fin retain their own names.')

p.scope('full-relation-matrix', r'\emph{The complete relation matrix.}',
        r'\emph{Finite-first attachment',
        p.symbols([('B', r'B_{\rm rel}')]),
        'B_rel is the identical full integral relation matrix in Lambda^2 Lambda direct sum K_d, with every return, Thom, saturated fibre and fixed-normal column retained. Its cokernel mathcal C and torsion T are unchanged. B_i continues to denote the ordered elliptic return family.')

p.scope('finite-first-space', r'\emph{Finite-first attachment',
        r'\emph{The role of oddness.}',
        p.symbols([('E', r'E_{\rm log}')]),
        'E_log is the same space obtained by attaching the logarithmic caps first. Every H_2/H_1 group, relative boundary target, Gamma kernel, splitting and free-rank formula refers to this same space. E_ell remains the relation matrix and E(M) the physical circle bundle.')

p.scope('relative-kernel-coefficients', 'Let ${\\mathsf M_{\\rm disc}}$',
        r'\emph{The full fundamental group',
        compose(p.literals([(r"z'", r'z_{\rm log}')]),
                p.symbols([('z', r'z_{\rm disc}')])),
        'z_disc is the same integer coefficient vector of relative component discs and z_log the unique integer coefficient vector in the injective logarithmic presentation. The equation M_disc z_disc=P_log z_log, projection, uniqueness inverse and subtract-and-glue splitting are unchanged; no rational denominator is discarded.')

p.scope('fundamental-group-vanishing-words',
        'On 170 rows two elliptic words have determinant one.',
        'The return \\(\\chi=',
        compose(p.literals([('u_1', r'u_{{\rm van},1}'),
                            ('u_2', r'u_{{\rm van},2}'),
                            ('v_1', r'v_{{\rm van},1}'),
                            ('v_2', r'v_{{\rm van},2}')]),
                p.symbols([('u', r'u_{\rm van}'), ('v', r'v_{\rm van}')])),
        'u_van,v_van are the same selected elliptic vanishing-word pair, including its determinant-one cases and the two explicitly given OS46 pairs. The adjugate formulas, killed angular coordinates, index-three relation 3 e1=-u_van-v_van and final e2=u_van-e1 are unchanged. The Tate and finite-power vectors are not rebound.')

p.exact('selected-cusp-tate-input',
        r'\(\mathbb Z\langle u,\delta\rangle\) and its origin-disc',
        r'\(\mathbb Z\langle u_{\rm T},\delta\rangle\) and its origin-disc',
        'The cusp kills the same selected primitive Tate direction u_T and physical angular delta. Its inclusion is the original ordered short period map used in C_cusp; the same toric discs bound both generators.')

p.scope('return-character', r'The return \(\chi=',
        'The abelianization matrix has rows',
        p.literals([(r'\chi', r'\chi_{\rm ret}')]),
        'chi_ret=gamma^* is the same return character on every used group relation. The quotient and inverse gamma period, the generator powers and both path-map composites are unchanged. chi(X) remains the Euler characteristic, with its original computed value 2d.')

p.exact('root-exponent-slot',
        r'return exponent, then writes \(\gamma^r c_i^j\).',
        r'return exponent \(n_{\rm ret}\in\mathbb Z\), then writes \(\gamma^{n_{\rm ret}}c_i^j\).',
        'n_ret is the same integer return exponent read after the root-sheet residue. Its domain and group word are explicit; r remains the free abelian rank, and the path inverse is unchanged.')

p.scope('logarithmic-generator-count',
        'The chosen origin lifts have canonical product',
        'The forward map sends',
        p.literals([('c_s', 'c_k')]),
        'The final presentation uses the same k logarithmic root paths already counted in the statement and finite-first construction. Replacing the private count s by k preserves the identical indexed list, product order and every relation; s_i retains the component-count role.')

p.exact('rational-fibre-generator',
        r'''The free coordinate of \(C_{d}\) is
\(\omega'_d=\omega_d/g\). Over the rationals each
logarithmic block gives
\(t_i(u)=\omega'_d(u,v_i)s/m_i\).''',
        r'''The free coordinate of \(C_{d}\) is
\(\omega'_d=\omega_d/g\). Let \(s_{\rm fib}=c_0\otimes1\) be its
rational generator of free coordinate one. For the fixed-lattice input
\(\lambda_{\rm fix}\), each rational logarithmic block gives
\(t_i(\lambda_{\rm fix})=\omega'_d(\lambda_{\rm fix},v_i)s_{\rm fib}/m_i\).''',
        's_fib is explicitly the rational image of the earlier fibre class c_0 of free coordinate one. The fixed-normal coefficient omega_d prime(lambda_fix,v_i)/m_i is unchanged. This is the same rational rank calculation; all integral torsion remains in B_rel.')
p.exact('rational-fibre-relation',
        r' \frac{db}{g}\left(e-\sum_i\mu_i/m_i\right)s=0.',
        r' \frac{db}{g}\left(e-\sum_i\mu_i/m_i\right)s_{\rm fib}=0.',
        'The same rational fibre generator is used in the single delta-sweep relation. Its coefficient and all rank cases are unchanged.')

p.scope('order-two-class-and-lift', r'\emph{The role of oddness.}', None,
        compose(p.literals([(r'\tau', r'\tau_2')]),
                p.symbols([('t', r't_{\rm tor}')])),
        'tau_2 is the identical exact-order-two fibre class e12+delta gamma in the explicitly evaluated even input. t_tor is the same literal delta-normal torus. Its edge, marked value, involution signs and the self-inverse translation by tau_2 are unchanged. The specific a=2,b=1,d=2 input is retained exactly; no claim for the odd-input theorem is extended.')

p.exact('finite-fixed-basis-domain',
        r'At a finite-good site, for a primitive fixed basis \(F\), let',
        r'''At a finite-good site, let \(F:\mathbb Z^2\to\ker(A_i(d)-I)\)
be the isomorphism onto the primitive fixed lattice given by its chosen basis, and put''',
        'F is explicitly the same primitive fixed-basis isomorphism, with its existing inverse on that lattice. This types F^{-1}N_h and leaves the projected image H Z^2, all denominators and finite freeness tests unchanged.')

p.exact('finite-site-return-binding',
        r'For a free logarithm with \(A^m=I\) and invariant $v$, the normal',
        r'''At the logarithmic site $i$, write \(A=A_i(d)\). For its free
logarithm with \(A^m=I\) and invariant $v$, the normal''',
        'The previously unindexed local return A is explicitly the same weighted return A_i(d) on the fixed physical lattice. This input identification is identity on every coordinate; all raw-normal, norm, affine and core formulas below keep that same A.')

p.exact('core-thom-peripheral-map',
        r'       m(0,Jv)-(-v\wedge v,JN_mv)=0.',
        r'       m(0,J_i v)-(-v\wedge v,J_iN_mv)=0.',
        'The map in the core relation is the already defined based peripheral insertion J_i, used in all five preceding Thom columns. Its source is the fixed lattice and its target K_d. This binds the two unindexed J occurrences to that exact insertion; m J_i v=J_i N_m v follows from A_i(d)v=v. No column or coefficient changes.')

# Final complete-scope readback and peer comparison: these are the same
# already chosen groups, columns, returns and Gysin section at every use.
p.scope('based-free-group-family', r'\emph{The marked graph',
        r'\Needspace{5\baselineskip}',
        p.literals([('F_{N-1}', r'\mathfrak F_{N-1}')]),
        'mathfrak F_{N-1} is the same free group on the first N-1 based peripheral words. Its semidirect action and all three typed cocycle inputs use the identical ordered words. The fixed lattice family F_i, including its last index, remains unchanged; the word-for-word map and its inverse identify the free-group presentations.')
p.exact('based-free-group-binding',
        r'''Define the semidirect group
\[
       G_{\rm ext}=\Lambda\rtimes \mathfrak F_{N-1},''',
        r'''Let \(\mathfrak F_{N-1}\) be the free group on the first
\(N-1\) based peripheral words. Define the semidirect group
\[
       G_{\rm ext}=\Lambda\rtimes \mathfrak F_{N-1},''',
        'This gives the exact free-group input at its first use. The generators are the same based peripheral words used by the graph bouquet and J_i; the semidirect return action is unchanged.')
p.scope('original-return-unit-weight-family',
        r'\begin{theorem}[Shared odd factors', None,
        p.literals([(r'\Lambda^2A_i-I', r'\Lambda^2A_i(1)-I'),
                    (r'S_d^{-1}A_iS_d', r'S_d^{-1}A_i(1)S_d'),
                    (r'A_i=\begin{pmatrix}', r'A_i(1)=\begin{pmatrix}'),
                    (r'S_d^{-1}[A_i-I]', r'S_d^{-1}[A_i(1)-I]')]),
        'A_i(1) is the original marked return at weight one, literally the d=1 member of the same A_i(d) family because S_1=I. The original block entries, rational return image, conjugation identity and weight-one comparison all use this same matrix. The theorem homology group A_1 and its Smith coordinates retain their names. No matrix entry or indexed site changes.')
p.exact('original-return-unit-weight-binding',
        r'''unchanged cap its rational span is
\(\operatorname{im}(\Lambda^2A_i(1)-I)\).''',
        r'''unchanged cap its rational span is
\(\operatorname{im}(\Lambda^2A_i(1)-I)\). Here \(A_i(1)\)
is the original marked return, the weight-one member of the same
family \(A_i(d)\), with \(S_1=I\).''',
        'The first unweighted-return use now states its exact input identification. Identity on the physical lattice is the forward and inverse identification at d=1; all later weight transports keep S_d and S_d^{-1}.')
p.exact('first-cusp-coordinate-columns',
        r'''The infinite fan is the original fan in this marking. Its
period subgroup has columns \(C_{\rm cusp}e_1,d C_{\rm cusp}e_2\). It has $d$ normalized''',
        r'''Write \(\varepsilon_1^{(2)},\varepsilon_2^{(2)}\) for the standard
two-coordinate columns used by the short and long period maps.
The infinite fan is the original fan in this marking. Its
period subgroup has columns \(C_{\rm cusp}\varepsilon_1^{(2)},d C_{\rm cusp}\varepsilon_2^{(2)}\). It has $d$ normalized''',
        'The same two coordinate columns are bound before their first occurrence and carried into the four-column cusp basis and component vertices. Multiplication by C_cusp followed by S_sh and its stated inverse preserve the exact period subgroup; the exterior e1,e2 retain their original marked elliptic meaning.')
p.exact('cusp-basis-reuses-bound-columns',
        r'''Write \(\varepsilon_1^{(2)},\varepsilon_2^{(2)}\) for the standard
coordinate columns of the two short and two long period maps. The ordered basis is''',
        'In this marking the ordered basis is',
        'The later basis uses the same already bound two-coordinate columns, without introducing a second basis or changing any displayed period column.')
p.exact('cusp-representative-selected-return',
        r'a period translate changes the ray-character normal-disc map by an image of \(A_d-I\), so',
        r'a period translate changes the ray-character normal-disc map by an image of \(A_*(d)-I\), so',
        'A_*(d) is the same selected-cusp return used by the closing monodromy cylinder d e3^C=(A_*(d)-I)e4^C. The representative-change relation is unchanged in that exact marked basis.')
p.exact('transfer-display-sentence-punctuation',
        r''' \quad\text{on }H_2(\mathcal F_1),
\]
This matrix''',
        r''' \quad\text{on }H_2(\mathcal F_1).
\]
This matrix''',
        'The displayed transfer equation ends its sentence; this punctuation repair changes no map, domain or coefficient.')
p.scope('gysin-section-vector',
        r'Choose an integer \(v_0\)',
        'For a multiplicative original the analogous generator is',
        p.literals([('v_0', r'v_{\rm Gys}')]),
        'v_Gys is the same selected three-coordinate integral section of rho_Gys, and mathsf R_d(v_Gys,0) is its same insertion into Lambda. The inverse section reads rho_Gys and the existing period-shear inverse. The indexed affine power family v_i, including v_0, keeps its original domain and entries.')
p.exact('gysin-section-vector-domain',
        r'Choose an integer \(v_{\rm Gys}\) with \(\rho_{\rm Gys}(v_{\rm Gys})=1\).',
        r'Choose \(v_{\rm Gys}\in\mathbb Z^3\) with \(\rho_{\rm Gys}(v_{\rm Gys})=1\).',
        'This records the three-coordinate domain already specified for rho_Gys, with the identical value one and the same R_d(-,0) inclusion into the physical four-lattice.')
p.scope('component-order-late-pairings', r'\emph{Free ranks',
        r'\emph{The role of oddness.}',
        p.literals([('-db/(gq)', r'-db/(gq_{\rm comp})')]),
        'Both later nonzero-Chern additive pairings use the same component-group order q_comp already defined in the local Gysin construction. The rational values, nonzero detection and enumeration comparison are identical; no multiplicity or kernel is changed.')
p.exact('site-power-coordinate-binding',
        r'''take \(m>0\) divisible by \(h\), and take
\(v\in\ker(A_i(d)-I)\). At a regular site use \(h=1\) and''',
        r'''take \(m>0\) divisible by \(h\), and take
\(v=v_i\in\ker(A_i(d)-I)\). Write \(v_{i,1},\ldots,v_{i,4}\)
for its coordinates in \((e_1,e_2,\delta,\gamma)\); their inverse is
\(v_i=v_{i,1}e_1+v_{i,2}e_2+v_{i,3}\delta+v_{i,4}\gamma\).
At a regular site use \(h=1\) and''',
        'At the chosen site i, v is exactly the affine power v_i. The coordinate extraction uses the fixed physical lattice basis and the displayed linear combination is its inverse. The scalar coordinates are indexed by both site and coordinate, so the global power vectors v_1,...,v_4 retain their own lattice meaning.')
p.scope('site-power-scalar-coordinates',
        r'\begin{theorem}[Shared odd factors', None,
        p.literals([('v_1,v_2,v_3,v_4', 'v_{i,1},v_{i,2},v_{i,3},v_{i,4}')]),
        'All four scalar gcd lists use the exact coordinates of the same selected v=v_i in the fixed ordered physical lattice. The primitive-vector test, fixed-power witness and regular-site test retain every integer and all divisibility conditions.')
p.exact('homology-table-input-slot',
        r'''In particular \(\chi(X)=2d\). These are
\eqref{maps:eq:D.WP8}--\eqref{maps:eq:D.WP9} with the full
integral matrix \eqref{maps:eq:D.OW2}--\eqref{maps:eq:D.OW4}.''',
        r'''In particular \(\chi(X)=2d\). These are
\eqref{maps:eq:D.WP8}--\eqref{maps:eq:D.WP9}, evaluated at
\(A_{1,\rm tor}=A_1\), with the full integral matrix
\eqref{maps:eq:D.OW2}--\eqref{maps:eq:D.OW4}.''',
        'The cited current homology table uses the formal torsion input A_{1,tor}. The present theorem already defines its actual abelianization torsion as A_1, so the input assignment A_{1,tor}=A_1 makes the existing table evaluation literal. The identity on the displayed Smith cyclic coordinates and its inverse preserve every homology group; r,d,L,beta,T and the entire local table remain unchanged.')


CALLER_OLD = r'''The possible multiplicative rim term
$\delta\wedge u_2$ vanishes by the integral unit elliptic
preimages in \eqref{maps:eq:D.OW7}; those preimages are polynomial
in $d$. Hence every cap kernel, with its torsion, is represented
by the stated fibre and fixed-normal columns.
At a narrow zero-Chern multiplicative site, use the integral
period basis $(l,h,p,w)$ in the rank-one part of the proof of
Theorem~\ref{maps:src:D.2.40}, with $r_0=\gcd(d,\nu)$.
Identity on this basis carries the two marked boundary maps
to their common normalization diagram. Both fibre kernels are
$\mathbb Z\langle l\wedge p,l\wedge w\rangle$, and all three
fixed normals bound. In wedge order $12,13,14,23,24,34$, the
four complementary coordinates and their section are
\[
 Q(y)=(y_{12},y_{23},y_{24},y_{34}),\qquad
 \sigma(z)=z_1e_{12}+z_2e_{23}+z_3e_{24}+z_4e_{34}.
\]
The inverse cap coordinates read the first coefficient of the
component sum and the three graph-circle/torus products in that
diagram. Thus $Q\sigma=I$ gives the same complete marked
boundary kernel for these two choices, with every node and line
unit carried by the stated period maps.'''
CALLER_NEW = r'''Write \((u_{\rm T},r_{\rm T})\) for the same ordered primitive
Tate frame in the imported multiplicative cap marking. Identity
on this marked frame fixes \(\delta,\gamma\) and carries the original
cap calculation to these coordinates. The possible rim term, with
its original order, is $\delta\wedge r_{\rm T}$. It vanishes by the integral unit elliptic
preimages in \eqref{maps:eq:D.OW7}; those preimages are polynomial
in $d$. Hence every cap kernel, with its torsion, is represented
by the stated fibre and fixed-normal columns.
At a narrow zero-Chern multiplicative site, use the integral
period basis $(l_N,h_N,p_N,w_N)$ in the rank-one part of the proof of
Theorem~\ref{maps:src:D.2.40}, with $r_0=\gcd(d,\nu)$.
Identity on this basis carries the two marked boundary maps
to their common normalization diagram. Both fibre kernels are
$\mathbb Z\langle l_N\wedge p_N,l_N\wedge w_N\rangle$, and all three
fixed normals bound. Write
\[
 \begin{gathered}
 (\mathsf e_1^{\rm N},\mathsf e_2^{\rm N},
  \mathsf e_3^{\rm N},\mathsf e_4^{\rm N})=(l_N,h_N,p_N,w_N),\\
 \mathsf e_{jk}^{\rm N}=\mathsf e_j^{\rm N}\wedge\mathsf e_k^{\rm N}.
 \end{gathered}
\]
The period map \(\Phi_N:\mathbb Z^4\longrightarrow\Lambda\) sends
\((z_1,z_2,z_3,z_4)\) to \(\sum_j z_j\mathsf e_j^{\rm N}\).
Its inverse, in physical coordinates \((x_u,x_r,x_\delta,x_\gamma)\)
relative to \((u_{\rm T},r_{\rm T},\delta,\gamma)\), is
\[
 \begin{aligned}
 z_1&=x_u,&z_3&=x_\delta+(a\kappa/\nu)x_u,\\
 z_2&=(\nu/r_0)x_r+(db\kappa/r_0)x_\gamma,&
 z_4&=-y_Nx_r+x_Nx_\gamma.
 \end{aligned}
\]
Here \(x_N,y_N\) are the same imported integers with
\((\nu/r_0)x_N+(db\kappa/r_0)y_N=1\). The two composites
are identity by that equation and the displayed short shear.
Use \(\Lambda^2\Phi_N\) to reconstruct wedge vectors and
\(\Lambda^2\Phi_N^{-1}\) to extract their coefficients \(y_{jk}\)
in order \(12,13,14,23,24,34\). The four complementary coordinates
and their section, for \(z\in\mathbb Z^4\), are
\[
 \begin{aligned}
 Q(y)&=(y_{12},y_{23},y_{24},y_{34}),\\
 \sigma(z)&=z_1\mathsf e_{12}^{\rm N}+z_2\mathsf e_{23}^{\rm N}
           +z_3\mathsf e_{24}^{\rm N}+z_4\mathsf e_{34}^{\rm N}.
 \end{aligned}
\]
The inverse cap coordinates read the first coefficient of the
component sum and the three graph-circle/torus products in that
diagram. Thus $Q\sigma=I$ gives the same complete marked
boundary kernel for these two choices, with every node and line
unit carried by the stated period maps.'''

CALLER_CUSP_OLD = r'''For each remaining component use its positive normal disc;
its boundary is $\mu_Cx_i+\rho_C\delta$, where $\mu_C$ is its
multiplicity and $\rho_C$ is the integer winding read from its
marked period and line transitions. Exponentiating the period
logarithm recovers the path. At the selected cusp the $d$
discs have boundaries $x_*+jC_{22}\delta$, $0\le j<d$,
in its actual short-period matrix. Let $M$ contain all these
boundaries. The kernel $\ker\Gamma$ of their map to $H_1(E)$
is computed by the integer equation $Mz=Pz'$.'''
CALLER_CUSP_NEW = r'''For each remaining component use its positive normal disc;
its boundary is $\mu_Cx_i+\rho_C\delta$, where $\mu_C$ is its
multiplicity and $\rho_C$ is the integer winding read from its
marked period and line transitions. Exponentiating the period
logarithm recovers the path. Use the selected-cusp matrix
$C_{\rm cusp}$ of the imported cap construction in its same
short-period marking: its coordinate map is multiplication by
$C_{\rm cusp}$ and its inverse is $C_{\rm cusp}^{-1}$.
Thus $(C_{\rm cusp})_{22}=(1-ab\kappa^2)/n_*$, and the $d$
discs have boundaries $x_*+j(C_{\rm cusp})_{22}\delta$, $0\le j<d$.
Let $M$ contain all these boundaries. The kernel $\ker\Gamma$
of their map to $H_1(E)$ is computed by the integer equation $Mz=Pz'$.'''

CALLER_WORDS_OLD = r'''The nongamma vanishing words are unchanged by $S_d$.
The determinant-one elliptic pairs kill both elliptic generators;
in the two $\mathrm{OS}46/\mathrm{II}$ cases the original
$I_3^*$ discs give $2e_1+\delta$ for $a=1$ and
$e_1+2\delta$ for $a=4$, together with $3e_1=-u-v$.
The selected cusp kills $\delta$. These relations kill the
elliptic lattice in those cases as well.'''
CALLER_WORDS_NEW = r'''The nongamma vanishing words are unchanged by $S_d$.
The determinant-one elliptic pairs kill both elliptic generators.
In the two $\mathrm{OS}46/\mathrm{II}$ cases, use the imported
words $u_{\rm van}=(1,1)$ and $v_{\rm van}=(-4,-1)$ in the
same marked elliptic basis $(e_1,e_2)$. The original $I_3^*$
discs give $2e_1+\delta$ for $a=1$ and $e_1+2\delta$ for $a=4$,
together with $3e_1=-u_{\rm van}-v_{\rm van}$.
The selected cusp kills $\delta$. These relations kill the
elliptic lattice in those cases as well.'''

CALLERS = [
    (CALLER_OLD, CALLER_NEW,
     'The caller imports the identical ordered periods l_N,h_N,p_N,w_N from 02LH and explicitly names their four-column and wedge bases. Phi_N is the original column map, and its displayed inverse is the exact short shear and long Bezout inverse from 02LH; exterior squares reconstruct/extract y_jk. The quotient entries, zero-insertion section, component coordinates and Q sigma=I retain their original values in that basis. The adjoining rim uses the actual original multiplicative identification u_2=r_0 (source28146) with the imported long Tate vector r_T: identity on the marked Tate frame fixes delta and gamma and has the identical inverse. Keeping delta wedge r_T preserves the old delta-first orientation, equal to the negative of the r_T wedge delta generator in the original cap shear. No normal coefficient or kernel changes.'),
    (CALLER_CUSP_OLD, CALLER_CUSP_NEW,
     'The two-dimensional selected-cusp short-period map is exactly C_cusp from 02LH, in the same natural row, fan, primitive Tate/angular marking and positive iterate. Its determinant is one and the inverse is C_cusp^{-1}; its lower-right entry is (1-ab kappa^2)/n_*. Thus the displayed boundary column is the same physical delta-coordinate of the same normal ray. The fibre coinvariant C in this proof keeps its original meaning. All disc columns, Mz=Pz prime, projected kernels and relative splitting entries remain unchanged.'),
    (CALLER_WORDS_OLD, CALLER_WORDS_NEW,
     'The caller now binds the two imported OS46/II vanishing words to their exact columns (1,1) and (-4,-1) in the same physical elliptic basis. Identity on that basis, with the displayed coordinates as inverse, preserves 3e1=-u_van-v_van and both original I3* disc relations. The respective preimages (-2,1) and (5,-4) under the type-II return minus identity are the unchanged 02LH maps. The later count u of unchanged caps retains its counting domain.'),
]


def verify_coordinate_maps():
    """Compare the exact existing matrices and their typed coordinate inverses."""
    import sympy as sp
    from itertools import combinations
    a,b,d,nu,kap,r0,xN,yN=sp.symbols('a b d nu kap r0 xN yN',nonzero=True)
    C=sp.Matrix([[nu,b*kap],[-a*kap,(1-a*b*kap**2)/nu]])
    Ci=sp.Matrix([[(1-a*b*kap**2)/nu,-b*kap],[a*kap,nu]])
    simple=lambda M:M.applyfunc(sp.simplify)
    assert simple(C*Ci)==sp.eye(2)==simple(Ci*C)
    HC=sp.Matrix([[nu,0,b*kap,0],[0,1,0,0],[-a*kap,0,C[1,1],0],[0,0,0,1]])
    HCi=sp.Matrix([[C[1,1],0,-b*kap,0],[0,1,0,0],[a*kap,0,nu,0],[0,0,0,1]])
    assert simple(HC*HCi)==sp.eye(4)==simple(HCi*HC)
    AT=sp.eye(4);AT[0,1]=nu;AT[2,1]=-a*kap;AT[0,3]=d*b*kap;AT[2,3]=d*C[1,1]
    AC=sp.eye(4);AC[0,1]=1;AC[2,3]=d
    assert simple(HCi*AT*HC)==AC
    pairs=list(combinations(range(4),2))
    wedge=lambda A:sp.Matrix([[A.extract(I,J).det() for J in pairs] for I in pairs])
    W=wedge(AC)-sp.eye(6)
    cols=sp.eye(6)
    K=sp.Matrix.hstack(cols[:,1],cols[:,2]+d*cols[:,3])
    assert W*cols[:,3]==K[:,0]
    assert W*(cols[:,4]-d*cols[:,3])==K[:,1]
    Q=sp.Matrix([[1,0,0,0,0,0],[0,0,-d,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
    Sigma=sp.Matrix.hstack(cols[:,0],cols[:,3],cols[:,4],cols[:,5])
    L=sp.Matrix([[0,1,0,0,0,0],[0,0,1,0,0,0]])
    assert Q*Sigma==sp.eye(4) and L*K==sp.eye(2)
    assert K*L+Sigma*Q==sp.eye(6)
    HN=sp.Matrix([[1,0,0,0],[0,xN,0,-d*b*kap/r0],[-a*kap/nu,0,1,0],[0,yN,0,nu/r0]])
    HNi=sp.Matrix([[1,0,0,0],[0,nu/r0,0,d*b*kap/r0],[a*kap/nu,0,1,0],[0,-yN,0,xN]])
    bez=(nu*xN+d*b*kap*yN)/r0
    assert simple(HN*HNi-sp.diag(1,bez,1,bez))==sp.zeros(4)
    assert simple(HNi*HN-sp.diag(1,bez,1,bez))==sp.zeros(4)
    aa,bb,uu,vv=sp.symbols('alpha_f beta_f u_f v_f')
    M=sp.Matrix([[aa,-bb],[vv,uu]]);Mi=sp.Matrix([[uu,bb],[-vv,aa]])
    assert M*Mi==(aa*uu+bb*vv)*sp.eye(2)==Mi*M
    BII=sp.Matrix([[0,1],[-1,-1]])
    assert BII*sp.Matrix([-2,1])==sp.Matrix([1,1])
    assert BII*sp.Matrix([5,-4])==sp.Matrix([-4,-1])
    assert sp.Matrix.hstack(sp.Matrix([1,1]),sp.Matrix([-4,-1])).det()==3
    print('Actual exact coordinate check: cusp C/Cinverse and full 4-column maps, conjugated return, both wedge preimages, Q/Sigma and relation-coordinate inverses; narrow 4-column products equal identity under the unchanged displayed Bezout equation; fibre quotient matrix products; both literal OS46 preimages and index three: passed.')


def stage():
    root=p.root;stem='S6_SERIES_PUBLISH_c9_02LH_final_roles'
    out=root/'agents'/'continuation9_02LH_final_roles'
    tmp=root.parents[1]/'tmp'/'c9_02LH_final_roles'
    out.mkdir(exist_ok=True);tmp.mkdir(exist_ok=True)
    back=p.new
    for op in reversed(p.operations):
        assert back.count(op['new'])==1,(op['name'],'reverse guard')
        back=back.replace(op['new'],op['old'],1)
    assert back==p.old
    fullnew=p.source[:p.start]+p.new+p.source[p.end:]
    li_start=p.source.index(r'\begin{theorem}[Integral homology at every positive weight]')
    li_end=p.source.index(r'\end{proof}',li_start)+len(r'\end{proof}')
    li_old=p.source[li_start:li_end]+'\n'
    li_new=li_old
    for old,new,_ in CALLERS:
        assert fullnew.count(old)==1 and fullnew.count(new)==0
        assert li_new.count(old)==1
        fullnew=fullnew.replace(old,new,1)
        li_new=li_new.replace(old,new,1)
    peer_path=root/'agents'/'continuation9_global_sweep'/'S6_SERIES_PUBLISH_c9_candidate07_02LI_peer_roles.json'
    peer_rows=json.loads(peer_path.read_text())
    peer_ids=[f'CLAUDE-III-P15-C9-C07-02LI-PEER-{i:03}' for i in range(1,5)]
    assert [r['change_id'] for r in peer_rows]==peer_ids
    li_combined=li_new
    for row in peer_rows:
        assert row['source_sha256']==sha(p.source)
        assert row['statement_id']=='maps:src:D.2.41'
        assert li_combined.count(row['old'])==1 and li_combined.count(row['new'])==0
        li_combined=li_combined.replace(row['old'],row['new'],1)
    peer_back=li_combined
    for row in reversed(peer_rows):
        assert peer_back.count(row['new'])==1
        peer_back=peer_back.replace(row['new'],row['old'],1)
    assert peer_back==li_new
    for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',
                    r'\\(?:[A-Za-z]*ref|cite[A-Za-z]*)\*?(?:\[[^]]*\])?\{[^}]+\}']:
        assert re.findall(pattern,p.source)==re.findall(pattern,fullnew),pattern
        assert re.findall(pattern,li_old)==re.findall(pattern,li_combined),(pattern,'coordinated LI')
    assert '\r' not in fullnew
    # Complete literal arrays and matrices retain their entries under these
    # exact identity substitutions; the new coordinate definitions use binomials.
    tablecounts={}
    for env in ('array','tabular','pmatrix'):
        pat=r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}'
        old=re.findall(pat,p.old,re.S);new=re.findall(pat,p.new,re.S)
        for nn,oo in [(r'c_{i,\rm ret}','c_i'),(r't_{\rm ring}','t'),
                      ('x_N','x'),('y_N','y'),('^{s_i}','^s'),
                      ('^{s_i-1}','^{s-1}'),('^{2s_i-1}','^{2s-1}')]:
            new=[s.replace(nn,oo) for s in new]
        assert old==new,(env,'entry recovery')
        tablecounts[env]=len(old)
    oldlines,newlines=p.old.splitlines(True),p.new.splitlines(True)
    for context in range(2,15):
        groups=list(difflib.SequenceMatcher(a=oldlines,b=newlines,autojunk=False).get_grouped_opcodes(n=context))
        fragments=[(''.join(oldlines[g[0][1]:g[-1][2]]),
                    ''.join(newlines[g[0][3]:g[-1][4]])) for g in groups]
        if all(p.source.count(o)==1 and fullnew.count(n)==1 for o,n in fragments):break
    else:raise AssertionError('whole-source unique old/new fragments')
    def substantive(line):
        return len(line.strip())>12 and not re.match(r'\\(?:begin|end)\{',line.strip())
    rows=[]
    for num,(old,new) in enumerate(fragments,1):
        relevant=[op for op in p.operations if any(substantive(t) and t in old for t in op['changed_old'])
                  or any(substantive(t) and t in new for t in op['changed_new'])]
        assert relevant,(num,'reason')
        line=p.source.count('\n',0,p.source.index(old))+1
        rows.append(dict(change_id=f'III-C9-02LH-FINAL-ROLE-{num:03}',type='D20',statement_id=p.sid,
            old_location=f'02LH complete statement/proof; frozen source lines {line}–{line+len(old.splitlines())-1}',
            old_page='candidate07 image triggers366–379 (global reader); this guard compared in the complete source owner',
            new_location='same complete statement/proof and permanent identifiers',
            new_page='pending successor build and actual changed-page reading',old_text=old,new_text=new,
            reason=' '.join(dict.fromkeys(op['reason'] for op in relevant)),
            review_status='Complete 1,675-line baseline and full proposed scope read and compared; exact whole-source reverse. Exposed source review; root admission and changed-page reading pending.'))
    for number,(old,new,reason) in enumerate(CALLERS,1):
        line=p.source.count('\n',0,p.source.index(old))+1
        rows.append(dict(change_id=f'III-C9-02LH-CALLER-02LI-{number:03}',type='D20',statement_id='maps:src:D.2.41',
            old_location=f'02LI complete statement/proof; literal02LH import; frozen source lines {line}–{line+len(old.splitlines())-1}',
            old_page='candidate07 caller source; no new image attribution',
            new_location='same caller paragraph and unchanged marked maps/inverse coordinates',
            new_page='pending successor build and changed-page reading',old_text=old,new_text=new,
            reason=reason,
            review_status='Complete 520-line baseline proof and full proposed caller scope read and compared; exact forward/reverse guard. Coordinated exposed review; root admission and changed-page images pending.'))
    result=p.source
    for row in rows:
        assert result.count(row['old_text'])==1,row['change_id']
        result=result.replace(row['old_text'],row['new_text'],1)
    assert result==fullnew
    for row in reversed(rows):
        assert result.count(row['new_text'])==1,row['change_id']
        result=result.replace(row['new_text'],row['old_text'],1)
    assert result==p.source
    assert p.source_path.read_bytes()==p.source_bytes
    (tmp/(stem+'_baseline.tex')).write_text(p.old)
    (tmp/(stem+'_proposed.tex')).write_text(p.new)
    (tmp/(stem+'_caller_baseline.tex')).write_text(li_old)
    (tmp/(stem+'_caller_proposed.tex')).write_text(li_new)
    (tmp/(stem+'_caller_coordinated_proposed.tex')).write_text(li_combined)
    diff=''.join(difflib.unified_diff(oldlines,newlines,fromfile='02LH frozen baseline',tofile='02LH proposal',n=5))
    diff+=''.join(difflib.unified_diff(li_old.splitlines(True),li_new.splitlines(True),fromfile='02LI full caller baseline',tofile='02LI full caller proposal',n=5))
    (out/(stem+'.diff')).write_text(diff)
    with (out/(stem+'_defects.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
    clauses=[]
    domainpat=r'\\mathbb\s*\{?([A-Z])\}?'
    for row in rows:
        delta=Counter(re.findall(domainpat,row['new_text']))-Counter(re.findall(domainpat,row['old_text']))
        if delta:clauses.append({'change_id':row['change_id'],'added_blackboard_counts':dict(delta)})
    (out/(stem+'.json')).write_text(json.dumps(dict(
        source_sha256=sha(p.source),baseline_scope_sha256=sha(p.old),proposed_scope_sha256=sha(p.new),
        baseline_lines=len(oldlines),proposed_lines=len(newlines),semantic_operations=len(p.operations),
        caller_baseline_sha256=sha(li_old),caller_proposed_sha256=sha(li_new),
        caller_baseline_lines=len(li_old.splitlines()),caller_proposed_lines=len(li_new.splitlines()),
        coordinated_caller_sha256=sha(li_combined),coordinated_caller_lines=len(li_combined.splitlines()),
        coordinated_peer_source=str(peer_path.relative_to(root)),coordinated_peer_change_ids=peer_ids,
        rows=rows,added_domain_clauses=clauses),ensure_ascii=False,indent=2)+'\n')
    occurrence=[]
    for op in p.operations:
        for count,old,new in op['details']:
            occurrence.append(dict(operation=op['name'],count=count,old=old,new=new))
    with (out/(stem+'_occurrences.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['operation','count','old','new'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(occurrence)
    with (root/'CHECK_EVENTS.tsv').open(newline='') as f:fields=next(csv.reader(f,delimiter='\t'))
    now=datetime.now(timezone.utc).isoformat();eid='publish:c9:III:02LH:final-rendered-roles'
    event={k:'' for k in fields}
    event.update(statement_id=p.sid,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine',
        type='used and rechecked in this run',
        outcome=f'Read all 1,675 current 02LH baseline statement/proof lines, the complete {len(newlines)}-line proposal and every direct theorem/equation caller after the global reader reported actual current07 image triggers on pages 366–379. Prior repairs and image findings were exposed. Prepared {len(rows)-len(CALLERS)} complete-proof fragments and three literal 02LI import fragments, with exact inverse coordinate/name maps, cusp and rank-one frame transports, integer quotient/section identities and whole-source reversal. All map coefficients, classification tables, formal owners, labels, tags, references and citations are preserved. This is exposed source review; no independent-proof or additional image-reading credit. Root admission and successor changed-page reading remain pending.',
        event_id=eid,phase='publication continuation9',source_file='S6_SERIES_PUBLISH_III.tex',
        source_row='02LH complete current statement/proof and exact 02LI basis/cusp/vanishing-word imports',
        source_event_type='used and rechecked in this run',evidence_group=eid,
        publish_input_file='../CLAUDE_READING_LOG_PAPER_III.md',
        publish_input_row='P15; prompt0.8 complete proof scope; candidate07 observed bindings',
        date_utc=now,where=f'code/{stem}.py; code/{stem}.out; agents/continuation9_02LH_final_roles/{stem}_review.md; agents/continuation9_02LH_final_roles/{stem}_defects.tsv; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate07_first_range_images.md')
    caller_event=event.copy()
    caller_event.update(statement_id='maps:src:D.2.41',
        event_id='publish:c9:III:02LI:LH-import-transport',
        source_row='02LI complete 520-line current statement/proof; III-C9-02LH-CALLER-02LI-001; III-C9-02LH-CALLER-02LI-002; III-C9-02LH-CALLER-02LI-003; CLAUDE-III-P15-C9-C07-02LI-PEER-001; CLAUDE-III-P15-C9-C07-02LI-PEER-002; CLAUDE-III-P15-C9-C07-02LI-PEER-003; CLAUDE-III-P15-C9-C07-02LI-PEER-004',
        outcome=f'Read the complete 520-line 02LI baseline statement/proof, its complete coordinated {len(li_combined.splitlines())}-line proposal and Q140/Q141, including the unchanged integral cone, P2 inverse, full five-column Thom maps, affine/projector maps, saturated cap kernels, relative splitting, fundamental group and rational comparison. Compared all three edited 02LH imports: narrow periods and typed wedge coordinates with the verified Tate rim, selected-cusp short matrix, and the two OS46/II vanishing words. The coordinated global-reader bar-chain, bar-vector, averaging-projector, selected fixed-coordinate, site-power coordinate and exact imported homology-table slot qualifications are included in the same exposed full-proof comparison. All actual coordinate morphisms and inverses, entries, signs, labels and public conclusions are retained. This association shares the 02LH evidence group; no independent-proof or image-reading credit. Root admission and successor changed-page reading remain pending.',
        where=event['where']+'; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate07_02LI_peer_roles_defects.tsv; agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_candidate07_02LH_peer_review.md; CLAUDE-III-P15-C9-C07-02LI-PEER-001; CLAUDE-III-P15-C9-C07-02LI-PEER-002; CLAUDE-III-P15-C9-C07-02LI-PEER-003; CLAUDE-III-P15-C9-C07-02LI-PEER-004')
    with (out/(stem+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows([event,caller_event])
    print('02LH baseline',len(oldlines),sha(p.old),'candidate',len(newlines),sha(p.new))
    print('Semantic operations',len(p.operations),'LH fragments',len(rows)-len(CALLERS),'caller fragments',len(CALLERS),'total',len(rows),'unique context',context)
    print('02LI complete baseline/proposed lines and hashes',len(li_old.splitlines()),sha(li_old),len(li_new.splitlines()),sha(li_new))
    print('02LI complete coordinated proposal lines/hash',len(li_combined.splitlines()),sha(li_combined),'peer guards',peer_ids)
    print('All literal table/matrix entries recover the baseline under the recorded identity names:',tablecounts)
    print('Explicit added blackboard/domain clauses:',json.dumps(clauses,ensure_ascii=False))
    oldnum=Counter(re.findall(r'\d+',p.old));newnum=Counter(re.findall(r'\d+',p.new))
    print('Decimal token additions from explicit coordinate/domain bindings:',dict(newnum-oldnum))
    print('Decimal token removals from qualified subscripts:',dict(oldnum-newnum))
    for op in p.operations:
        print(op['name'])
        for count,old,new in op['details']:print(' ',count,repr(old)[:200],'->',repr(new)[:200])
    print('All operation reverses, unique whole-source fragment reverses and ordered permanent labels/targets/references/citations passed.')
    print('Canonical source bytes unchanged; no canonical event, defect, count or status writes.')
    print('Observed source SHA256',sha(p.source),'proposed used-only associations',[eid,caller_event['event_id']],'shared evidence group',eid)
    print('Packet',out.relative_to(root),'complete scopes outside checkpoint',tmp)


if __name__=='__main__':
    verify_coordinate_maps()
    stage()



