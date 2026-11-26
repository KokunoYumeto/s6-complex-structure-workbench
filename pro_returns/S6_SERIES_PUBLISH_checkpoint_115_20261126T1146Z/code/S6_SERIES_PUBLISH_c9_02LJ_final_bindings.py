#!/usr/bin/env python3
"""Prepare the bounded 02LJ final-image binding repair; never admit it.

The entire 1395-line statement/proof was read. Complete before/after source
copies stay in scratch tmp. The retained packet contains exact guarded source
fragments, the authored review, an exposed used-only proposal event and actual
preparation output. Canonical TeX, events, defects and derived data are read only.
"""
import csv
from collections import Counter
from datetime import datetime, timezone
import difflib
import re

from S6_SERIES_PUBLISH_c9_backend_notation import Packet, sha
from S6_SERIES_PUBLISH_c9_notation_addendum_io import compose


p = Packet('02LJ', 'maps:src:D.2.42',
           '8e42345d1514a6dbcb262a5fb91234a25b0f49890ff6e11cdbacde20a096a270',
           '486–502', 'Final-image complete proof binding and period transport.')

# Every token operation has a semantic interval read in its entirety. Literal
# products that have no token boundary are included explicitly below.
p.scope('primitive-complement-bezout',
        r'The integer \(\nu\) is the content of \(A-I\).',
        'For height', p.symbols([('x', r'x_u'), ('y', r'y_u')]),
        'x_u,y_u are the identical chosen integers with x_u u_1+y_u u_2=1. The resulting complement v=(-y_u,x_u)^t and its determinant-one inverse are unchanged; only the two integer coordinates are qualified.')
p.scope('generic-period-basis',
        r'integral basis \(H\) replaces', 'Use wedge order',
        p.symbols([('H', r'H_{\rm bas}')]),
        'H_bas is the identical integral basis matrix used as the argument of the full period-coordinate change Pi to Pi H_bas, x to H_bas^{-1}x. Multiplication by H_bas is the unchanged inverse. The later actual cap bases receive their own qualified names.')
p.scope('wedge-section-bezout', 'Use wedge order', 'Set\n',
        compose(p.literals([('ax+by', r'a x_{\wedge}+b y_{\wedge}', 1)]),
                p.symbols([('x', r'x_{\wedge}'), ('y', r'y_{\wedge}')])),
        'x_wedge,y_wedge are the same Bezout integers with a x_wedge+b y_wedge=1. The section s_0=x_wedge e_12-y_wedge e_34, its omega value and every subsequent cylinder preimage remain identical.')

p.scope('rank-one-cap-map-family',
        'At a rank-one multiplicative cap use the basis', 'At the cusp use',
        compose(p.literals([(r'f_1(', r'f^{\rm N}_1(', 1),
                            (r'f_2(', r'f^{\rm N}_2(', 1)]),
                p.symbols([('H', r'H_N'), ('h', r'h_{\rm per}')])),
        'H_N is the same ordered rank-one basis (l,h_per,p_0,w_0). f_1^N and f_2^N are the original coordinate projections with exactly the same output entries. Their physical inputs are H_N^{-1}x and (wedge^2 H_N)^{-1}y; inserting the stated zero entries and applying H_N or wedge^2 H_N is the original right inverse. Every primitive kernel and cylinder preimage is preserved.')
p.exact('site-specialization-binding',
        r'''\item \emph{Cap maps, arbitrary finite parameters, and homology.}

At a rank-one multiplicative cap''',
        r'''\item \emph{Cap maps, arbitrary finite parameters, and homology.}

In the cap formulas, \(A,g,\beta,T\) denote
\(A_i,g_i,\beta_i,T_i\) at the site under discussion, in its fixed physical marking.
At a rank-one multiplicative cap''',
        'This explicitly identifies the cap-formula parameters A,g,beta,T with the already defined indexed matrix/cocycle entries at that cap. The specialization map evaluates the indexed family at the chosen site and retains the same physical marking, so its coordinate entries and all inverse matrices are unchanged.')
p.exact('rank-one-coordinate-binding',
        'constructed in the primitive rank-one construction. The normalized ruled component with\nits two sections identified gives',
        r'''constructed in the primitive rank-one construction. Here \(x\) and \(y\)
denote coordinate columns in \(H_N\) and \(\wedge^2H_N\), respectively.
The normalized ruled component with its two sections identified gives''',
        'This binds the existing map arguments to the ordered input basis already specified. The physical-to-coordinate maps are H_N^{-1} and wedge^2 H_N^{-1}; their inverses are H_N and wedge^2 H_N. No input entry, projection, kernel or section is changed.')
p.scope('cusp-cap-map-family', 'At the cusp use', 'For an original additive cap,',
        compose(p.literals([(r'f_1(', r'f^{\rm C}_1(', 1),
                            (r'f_2(', r'f^{\rm C}_2(', 1)]),
                p.symbols([('H', r'H_C')])),
        'H_C is the same cusp basis (SCe_1,Le_1,SCe_2,Le_2). The maps f_1^C,f_2^C retain the projections (x_2,x_4) and (y_12,y_14-y_23,y_24,y_34). The stated zero insertion followed by wedge^2 H_C remains the section, and both kernel generators and both monodromy-cylinder preimages remain unchanged.')
p.exact('cusp-coordinate-binding',
        r'At the cusp use \(H_C=(SCe_1,Le_1,SCe_2,Le_2)\) of the prescribed-cusp construction. Then',
        r'''At the cusp use \(H_C=(SCe_1,Le_1,SCe_2,Le_2)\) of the prescribed-cusp construction.
Here the input columns are in \(H_C\) and \(\wedge^2H_C\) coordinates. Then''',
        'The same cusp inputs are now explicitly bound to H_C and wedge^2 H_C. Coordinate extraction and reconstruction are inverse because H_C is the unchanged unimodular ordered basis.')
p.scope('original-line-vector-and-shear', 'For an original additive cap,',
        'Zero line multidegree',
        compose(p.symbols([('h', r'h_{\rm line}')]),
                p.literals([(r'\lambda', r'\lambda_{\rm line}', 4)])),
        'h_line=a(A-I)^{-1}g is the same integral original-line vector and lambda_line=-h_line^t J is its same row. S_P and S_P^{-1} retain respectively addition and subtraction of that row, and lambda_line(A-I)+beta=0 is the original shear-cancellation identity.')
p.scope('original-cap-map-family',
        r'Put \(z_Q=b(A-I)^{-1}g\)', 'At a finite cap,',
        p.literals([(r'f_2(y)', r'f^{\rm orig}_2(y)', 1)]),
        'f_2^orig is the identical original-additive specialization in the coordinates after S_P. Its q_vert factors, z_Q entries, Bezout section followed by wedge^2 S_P^{-1}, and fixed basis are preserved. The label distinguishes this already specified map from the two preceding projections.')
p.scope('original-core-generator',
        r'Put \(z_Q=b(A-I)^{-1}g\)', 'At a finite cap,',
        p.literals([('[C]', r'[C_{\rm core}]', 3)]),
        'C_core is the same original core curve whose primitive homology class occurs in the displayed H_2 basis. The elliptic fibre remains q_vert[C_core], and the identical Bezout column followed by wedge^2 S_P^{-1} remains its section. Identity on this primitive class preserves both cap-map outputs and their sections; C retains the later cusp-matrix role.')

p.scope('finite-power-vector', 'At a finite cap,',
        r'\item \emph{Primitive rank-one periods and all scalar isotropy.}',
        p.symbols([('v', r'v_{\rm fin}')]),
        'v_fin=n ell+r delta is the same fixed power vector of the finite affine lift. Its normalized affine translation, norm equality, boundary parametrization and inverse, sector fibre area and norm sweep are all renamed together. This preserves every Thom column and the full central-surface and group relations; the elliptic complement v retains its ordered-basis role.')
p.exact('finite-site-period-vector',
        r'At a finite cap, \(\ell=(-bz_1,-bz_2,0,1)\) is integral and',
        r'''At a finite cap, write \(z_{\rm site}=z_i=(A_i-I)^{-1}g_i\).
Then \(\ell=(-b(z_{\rm site})_1,-b(z_{\rm site})_2,0,1)\) is integral and''',
        'z_site is explicitly the previously defined rational period vector z_i at this additive site. Its two components are the original z_1,z_2 in ell, with identity on the same ordered elliptic basis. No lattice element, gamma coordinate or finite-lift entry changes; the later scalar exponential z is not used as an unbound vector.')
p.scope('finite-coinvariant-column', 'At a finite cap,',
        r'\item \emph{Primitive rank-one periods and all scalar isotropy.}',
        p.literals([(r'\beta_0', r'\beta_{\rm fin}', 11)]),
        'beta_fin is the same finite coinvariant column: delta at II and (0,-1,0,0) at the indicated III cap. Its norm, delta-preimage identity, pairing with ell and all central-surface Bezout coordinates retain their original entries. The later scalar valuation coefficient is separately qualified.')
p.scope('finite-norm-preimage',
        'Integer reduction of $[T-I', 'Its last two inverse rows',
        p.symbols([('y', r'y_{\rm norm}')]),
        'y_norm is the same integer preimage with q_vert beta_fin+(T-I)y_norm=delta. Identity on this lattice column preserves the displayed norm and pairing identities and the inverse coinvariant rows.')
p.scope('affine-translation-vector',
        r'The affine representative is \(R_{\rm aff}',
        'For the holomorphic units',
        compose(p.literals([(r'N_mt', r'N_m t_{\rm aff}', 1)]),
                p.symbols([('t', r't_{\rm aff}'), ('h', r'h_{\rm aff}')]),
                p.literals([(r'\pi=', r'\pi_{\rm fix}=', 1)])),
        't_aff is the original affine translation, h_aff the solution of (I-T)h_aff=t_aff-v_fin/m on the complementary subspace, and pi_fix=N_m/m is the unchanged projector. Translation by h_aff and by -h_aff are exactly inverse and retain scalar commutation. The public mod-two invariant t and the original-line vector are no longer rebound.')
p.scope('holomorphic-affine-section', 'For the holomorphic units',
        'A peripheral period change',
        compose(p.literals([(r'\mathcal Nd=0', r'\mathcal N d_{\rm hol}=0', 1),
                            (r'\mathcal R^jd', r'\mathcal R^j d_{\rm hol}', 1)]),
                p.symbols([('h', r'h_{\rm hol}'), ('d', r'd_{\rm hol}')]),
                p.literals([(r'\sigma', r'\sigma_{\rm root}', 3),
                            (r'\zeta u', r'\zeta_{\rm root}u', 1),
                            (r'A(\sigma_{\rm root}^{-1}u)',
                             r'A_{\rm root}(\sigma_{\rm root}^{-1}u)', 1)])),
        'sigma_root(u)=zeta u is the same root-disc rotation, A_root is the same holomorphic linear part in its action, and d_hol is the same affine difference. The weighted sum defining h_hol and the identity (I-R)h_hol=d_hol preserve every coefficient. Its negative gives the same inverse translation over the whole disc and collar.')
p.exact('holomorphic-operator-inputs',
        r'''For the holomorphic units on the whole good root disc, let
\(\mathcal Rf(u)=A_{\rm root}(\sigma_{\rm root}^{-1}u)f(\sigma_{\rm root}^{-1}u)\), where
\(\sigma_{\rm root}(u)=\zeta_{\rm root}u\) and \(\mathcal R^m=I\). If the two affine terms
differ by \(d_{\rm hol}\) with \(\mathcal N d_{\rm hol}=0\), use''',
        r'''For the holomorphic units on the whole good root disc, write \(A_{\rm root}(u)\)
for the linear part of the retained good-root action, and let
\(\mathcal Rf(u)=A_{\rm root}(\sigma_{\rm root}^{-1}u)f(\sigma_{\rm root}^{-1}u)\), where
\(\sigma_{\rm root}(u)=\zeta_{\rm root}u\) and \(\mathcal R^m=I\).
Put \(\mathcal N=\sum_{j=0}^{m-1}\mathcal R^j\).
For the two affine terms with difference \(d_{\rm hol}\) and
\(\mathcal N d_{\rm hol}=0\), use''',
        'The holomorphic coefficient is explicitly bound to the same retained root-action linear part. The norm is the sum of the same m iterates. The exact identity (I-R)sum_j jR^j=N-mI proves that the unchanged weighted sum solves the displayed affine comparison and has the unchanged subtraction inverse; the original kernel condition and all units are preserved.')
p.scope('finite-central-basis',
        r'For \(A_{\rm fin}m+B_{\rm fin}n=1\), the basis',
        r'Thus \(H_1(F_{\rm fin})\)',
        compose(p.literals([('mz', r'm z_{\rm fin}', 1), ('nz', r'n z_{\rm fin}', 1)]),
                p.symbols([('z', r'z_{\rm fin}')])),
        'z_fin=A_fin ell+B_fin c_0 is the same free central-surface generator. The two displayed inverse integer equations retain all m,n,r,q_vert coefficients and are verified by A_fin m+B_fin n=1. The later exponential elliptic coordinate retains its own name.')
p.scope('fixed-sweep-map', 'A peripheral period change',
        'The opposite sectors give the inverse boundary chains.',
        p.literals([('t(u)', r't_{\rm swp}(u)', 2),
                    (r't(\delta)', r't_{\rm swp}(\delta)', 1),
                    (r't(\ell)', r't_{\rm swp}(\ell)', 1)]),
        't_swp is the same fixed-loop sweep homomorphism used in the stated inverse cycle coordinates. Its shear adds omega(u,lambda)s and the inverse subtracts that term. D_delta=t_swp(delta) and L_ell=t_swp(ell) are the identical two previously named cycle classes, and the full Thom columns keep every entry. The public mod-two invariant t keeps its original scalar role.')
p.scope('finite-determinant-sign',
        r'Hence simple connectivity is precisely',
        r'\item \emph{Primitive rank-one periods and all scalar isotropy.}',
        p.literals([(r'\varepsilon', r'\varepsilon_{\rm det}', 7)]),
        'varepsilon_det=me-n is the same sign plus or minus one. Its two Bezout coefficients, every inverse generator equation and the final cyclic relation are preserved with that same sign. The cusp refinement vector and bordism generator receive separate names.')
p.exact('boundary-meridian-generator',
        r'''relation. The positive normal meridian is \(m\mu-v_{\rm fin}\).''',
        r'''relation. Write \(\mu_{\partial}\) for the positive boundary-base
generator in these mapping-torus coordinates. The positive normal meridian is
\(m\mu_{\partial}-v_{\rm fin}\).''',
        'mu_partial is exactly the old boundary-base generator mu used in the adjacent mapping-torus parametrization. The same m-step base traversal accumulates v_fin and the same subtracting fibre translation closes the normal meridian; both parametrizations and their inverse are unchanged. The theorem’s fundamental-class invariant mu(X) retains its original map.')
p.scope('finite-thom-column-family',
        'Sectors of its meridional disc',
        r'\item \emph{Primitive rank-one periods and all scalar isotropy.}',
        p.literals([('C_1', r'C_{1,\rm Th}'),
                    ('C_2', r'C_{2,\rm Th}'),
                    ('C_3', r'C_{3,\rm Th}')]),
        'C_{j,Th} is the identical j-th finite Thom column in the ordered cycle coordinates (s,D_delta,L_ell). All three displayed columns, the generated integral subgroup, K_0=A_fin C_{2,Th}+B_fin C_{3,Th}, and both reverse column relations carry the same subscripts together. Identity on the three-column domain preserves the full presentation and every integer entry. The scalar subgroups C_2 and C_3 keep their group notation.')

p.scope('rank-one-bezout-coordinates',
        r'At an unselected multiplicative site put',
        r'The chart identification is',
        compose(p.literals([(r'\sigma', r'\sigma_{\rm Bez}', 4),
                            (r'\\y&d_0', r'\\y_L&d_0', 1)]),
                p.symbols([('x', r'x_L'), ('y', r'y_L'), ('h', r'h_{\rm per}'),
                           ('H', r'H_N')])),
        'sigma_Bez,theta_N and x_L,y_L are the same two Bezout pairs. C_S,C_L and both literal inverses retain their entries, with determinant one from n_0 theta_N+A_0 sigma_Bez=1 and d_0 x_L+B_0 y_L=1. h_per is the same first long vector in H_N; its return is h_per+l. The pairing matrix and scalar direction are unchanged.')
p.scope('rank-one-chart-coordinates', 'The chart identification is',
        'The primitive long period identifies successive charts',
        compose(p.literals([('XY', 'X_NY_N', 2), ('Xq', 'X_Nq', 1)]),
                p.symbols([('X', 'X_N'), ('Y', 'Y_N'), ('z', 'z_N')])),
        'z_N is the same exponential coordinate of the primitive rank-one vanishing period l. The chart coordinates X_N=z_N/q^j and Y_N=q^{j+1}/z_N retain the exact inverse z_N=X_N q^j, q=X_N Y_N. The physical elliptic exponential z and the completed space Y keep their earlier meanings; the basis transport below relates this rank-one exponential to Z_N.')
p.scope('rank-one-isotropy-weight', 'On that elliptic curve,',
        r'\item \emph{The prescribed cusp',
        compose(p.literals([(r'\sigma', r'\sigma_{\rm Bez}', 4)]),
                p.symbols([('w', r'w_{\rm norm}')])),
        'The normal character w_norm=(a r_Tate)^{-1}=-sigma_Bez is the identical residue. Both opposite normal characters and the primitive scalar translation retain their signs. The unit, divisibility and nontrivial-translation assertions use the unchanged basis and inverse.')
p.scope('cusp-edge-weight', r'Let \(k=b\kappa\).',
        r'\item \emph{One line, its fan support',
        p.symbols([('k', r'k_{\rm edge}')]),
        'k_edge=b kappa is the same integer cusp-edge weight. The adjacent charts and their inverse, endpoint weights, tangent action and stabilizer order retain every entry. The finite positive k in m=d_i k keeps its original domain and value.')

# Exact physical, rank-one and cusp transport, preserving all period units.
p.scope('physical-real-complex-coordinates', r'With \(Z=U+\Pi_{\rm ph}W\)',
        r'At a rank-one cap use',
        compose(p.literals([('Rv', r'R v_{\rm lin}', 1)]),
                p.symbols([('U', r'U_{\rm ph}'), ('W', r'W_{\rm ph}'),
                           ('Z', r'Z_{\rm ph}'), ('v', r'v_{\rm lin}')])),
        'U_ph,W_ph,Z_ph are the existing physical real and complex coordinates; v_lin is the existing multiplicative line coordinate. The gauge exponent, both deck maps, involution and inverse factors retain every entry. Explicit basis and exponential bindings are added in the next operation.')
p.exact('physical-period-inputs',
        r'With \(Z_{\rm ph}=U_{\rm ph}+\Pi_{\rm ph}W_{\rm ph}\), the invertible gauge',
        r'''Write \(x=SU_{\rm ph}+LW_{\rm ph}\) and
\(Z_{\rm ph}=U_{\rm ph}+\Pi_{\rm ph}W_{\rm ph}\).
These are the real coordinates in the ordered physical short and long bases
and the corresponding normalized complex coordinates. Thus
\(z=\exp(2\pi i(Z_{\rm ph})_1)\) and
\(v_{\rm lin}=\exp(2\pi i(Z_{\rm ph})_2)\), with inverse logarithms
modulo the same marked periods. Put
\(h_1=\exp(2\pi i\tau_E)\), \(h_G=\exp(2\pi i\zeta_G)\) and
\(R=\exp(2\pi i\rho_L)\); these retain the original holomorphic units.
The invertible gauge''',
        'The same physical point is decomposed in the unchanged short/long basis (S,L), with inverse reconstruction SU_ph+LW_ph. The normalized period columns give Z_ph=U_ph+Pi_ph W_ph and the named exponentials. Their inverse is the already specified logarithm modulo the identical marked periods. Exponentiating the two displayed columns of Pi_ph yields exactly h_1,h_G and R in both deck maps; no unit is discarded.')
p.scope('doubled-deck-maps', r'gives the exact period and inversion maps',
        r'The functions $h_1,h_G,R$',
        compose(p.literals([('hF=Fh', r'h_{\mathcal D}F_{\mathcal D}=F_{\mathcal D}h_{\mathcal D}', 1),
                            ('JhJ=h^{-1}', r'J_{\mathcal D}h_{\mathcal D}J_{\mathcal D}=h_{\mathcal D}^{-1}', 1),
                            ('JFJ=F^{-1}', r'J_{\mathcal D}F_{\mathcal D}J_{\mathcal D}=F_{\mathcal D}^{-1}', 1)]),
                p.symbols([('h', r'h_{\mathcal D}'), ('F', r'F_{\mathcal D}'), ('J', r'J_{\mathcal D}')])),
        'h_D,F_D,J_D are the identical two period maps and inversion map on the doubled line D with coordinates (z,v_lin,zeta). Every original line factor and target-coordinate inverse factor is retained. The explicit commutation and conjugation identities are renamed together. The undoubled-line lifts are separately indexed by L, and J in the elliptic symplectic pairing remains its original matrix.')
p.exact('rank-one-period-transport',
        r'''At a rank-one cap use \eqref{maps:eq:MT_local_36}. With
\(\Pi_N=C_S^{-1}\Pi_{\rm ph}C_L\), the Gaussian is''',
        r'''At a rank-one cap use \eqref{maps:eq:MT_local_36} and put
\[
 \begin{aligned}
 U_N&=C_S^{-1}U_{\rm ph},& W_N&=C_L^{-1}W_{\rm ph},\\
 Z_N&=C_S^{-1}Z_{\rm ph},& \Pi_N&=C_S^{-1}\Pi_{\rm ph}C_L.
 \end{aligned}
\]
The inverse is
\((U_{\rm ph},W_{\rm ph},Z_{\rm ph})=(C_SU_N,C_LW_N,C_SZ_N)\),
and \(Z_N=U_N+\Pi_NW_N\). The rank-one chart coordinate is
\(z_N=\exp(2\pi i(Z_N)_1)\). The identity
\(K_N=C_S^tD_{\rm pol}C_L\) gives
\[
 U_N^tK_NW_N=U_{\rm ph}^tD_{\rm pol}W_{\rm ph},\qquad
 K_N^t\Pi_N=C_L^tD_{\rm pol}\Pi_{\rm ph}C_L.
\]
Thus the same Gaussian in these coordinates is''',
        'The normalized short and long bases are SC_S and LC_L. Hence U_N=C_S^{-1}U_ph, W_N=C_L^{-1}W_ph and Z_N=C_S^{-1}Z_ph, with the displayed multiplication inverse. Substitution in K_N=C_S^t D_pol C_L proves both retained gauge terms equal their physical expressions. K_N^t Pi_N is the congruence C_L^t D_pol Pi_ph C_L, so its symmetry follows from the same physical matrix; all full holomorphic period entries are preserved.')
p.scope('rank-one-gauge-coordinates',
        r'Thus the same Gaussian in these coordinates is',
        'For the nonprimitive physical first period',
        compose(p.literals([('W_1', '(W_N)_1', 1),
                            ('K_NW', 'K_NW_N', 1),
                            (r'\Pi_NW', r'\Pi_NW_N', 1),
                            ('K_N^tZ', 'K_N^tZ_N', 1)]),
                p.symbols([('U', r'U_N'), ('W', r'W_N')])),
        'Every rank-one gauge, long factor and around-base comparison now uses the explicitly transported coordinates U_N,W_N,Z_N. Both inverse basis maps above recover the original physical point. The off-diagonal pairing entry is retained and the two added n_per W_N,1 squared terms are unchanged.')
p.exact('rank-one-long-period-argument',
        r'''entry \(M\) remains. Its long factors have exponent
\(-4\pi i h^tK_N^tZ_N-2\pi i h^tK_N^t\Pi_Nh\).
The integer support \(n_{\rm per}j^2\) has difference \(2n_{\rm per}hj+n_{\rm per}h^2\), and''',
        r'''entry \(M\) remains. For a long-period coefficient column
\(\mathbf n_N\in\mathbb Z^2\) in \((h_{\rm per},w_0)\), its long factors have exponent
\(-4\pi i\mathbf n_N^tK_N^tZ_N-2\pi i\mathbf n_N^tK_N^t\Pi_N\mathbf n_N\).
Write \(r_N=(\mathbf n_N)_1\). The first long generator advances the fan index
by one, so the integer support \(n_{\rm per}j^2\) has difference
\(2n_{\rm per}r_Nj+n_{\rm per}r_N^2\) under \(j\mapsto j+r_N\), and''',
        'The old vector h in the long exponential is the coefficient column n_N in the actual long basis (h_per,w_0). The old scalar h in the one-variable support difference is its first coordinate r_N. The coordinate projection n_N to r_N is fixed by h_per mapping to h_per+l and w_0 being fixed; the inverse coefficient map sends n_N to its same two long coefficients. Expanding n_per(j+r_N)^2-n_per j^2 gives the identical support expression. No long unit or pairing entry is removed.')
p.scope('physical-valuation-scalar', 'For the nonprimitive physical first period',
        'At the cusp the symmetric pairing is',
        p.literals([(r'\beta_0', r'\beta_{\rm val}', 3),
                    (r'\sigma', r'\sigma_{\rm Bez}', 1)]),
        'beta_val is the same scalar B_0 multiplying the primitive physical valuation column v_0. Both valuation columns, their linear identity and psi_1 are unchanged. sigma_Bez in the line character is the identical Bezout coefficient already used in the primitive basis. The finite beta_fin column keeps its own lattice role.')
p.exact('cusp-period-transport',
        'At the cusp the symmetric pairing is',
        r'''At the cusp the short and long bases are \(SC,L\). Put
\[
 \begin{aligned}
 U_C&=C^{-1}U_{\rm ph},& W_C&=W_{\rm ph},\\
 Z_C&=C^{-1}Z_{\rm ph},& \Pi_C&=C^{-1}\Pi_{\rm ph}.
 \end{aligned}
\]
The inverse is
\((U_{\rm ph},W_{\rm ph},Z_{\rm ph})=(CU_C,W_C,CZ_C)\),
and \(Z_C=U_C+\Pi_CW_C\). Since \(C^tD_{\rm pol}=D_{\rm pol}C\),
the symmetric pairing is''',
        'The cusp basis is exactly (SC,L). The real/complex coordinate transport and its multiplication inverse are the stated matrices C^{-1} and C, with unchanged long coordinates. Pi_C=C^{-1}Pi_ph is the full normalized cusp period matrix. The given C and D_pol satisfy C^t D_pol=D_pol C entrywise; this makes the following K the same pairing and proves the full gauge transport.')
p.exact('cusp-gaussian-and-character-binding',
        r'''The Gaussian \(\exp\{-2\pi i(U^tKW+W^tK\Pi W)\}\) gives long
factors \(q^{-h^tKh}X^{-2Kh}\) times their unchanged holomorphic
units. The support \(\psi(v)=v^tKv\) on the prescribed unit triangles
has the required difference \(2h^tKv+h^tKh\).
For a triangle slope \(m\), its regular frame is
\(e_m=\chi^{-m}e\) and vector coordinate is
\(\zeta_m=\chi^m\zeta\); the opposite monomials give the inverse.''',
        r'''In particular
\[
 U_C^tKW_C=U_{\rm ph}^tD_{\rm pol}W_{\rm ph},\qquad
 K\Pi_C=D_{\rm pol}\Pi_{\rm ph}.
\]
The Gaussian \(\exp\{-2\pi i(U_C^tKW_C+W_C^tK\Pi_CW_C)\}\)
is therefore the same physical gauge. Define
\(B_C(q)=\Pi_C-(\log q)/(2\pi i)I\) on the cut disc; it retains the
full holomorphic period-unit matrix. Let
\(\mathbf X_C=(X_1,X_2)=(e^{2\pi i(Z_C)_1},e^{2\pi i(Z_C)_2})\),
using the same dense coordinates as the adjacent cusp charts. For
\(\mathbf m\in\mathbb Z^2\) write
\(\mathbf X_C^{\mathbf m}=\exp(2\pi i\mathbf m^tZ_C)\).
For a long-period coefficient \(\mathbf n_C\in\mathbb Z^2\), the long factors are
\[
 q^{-\mathbf n_C^tK\mathbf n_C}\mathbf X_C^{-2K\mathbf n_C}
 \exp(-2\pi i\mathbf n_C^tK B_C(q)\mathbf n_C).
\]
Thus the original holomorphic factors remain present. The support
\(\psi(v)=v^tKv\) on the prescribed unit triangles has difference
\(2\mathbf n_C^tKv+\mathbf n_C^tK\mathbf n_C\) under
\(v\mapsto v+\mathbf n_C\).
Let \(e_{\mathcal D}\) be the reference frame with fibre coordinate \(\zeta\).
For a triangle slope \(\mathbf m_C\), its regular frame is
\(e_{\mathbf m_C}=\mathbf X_C^{-\mathbf m_C}e_{\mathcal D}\) and vector coordinate is
\(\zeta_{\mathbf m_C}=\mathbf X_C^{\mathbf m_C}\zeta\);
the opposite monomials give the inverse.''',
        'K=C^t D_pol and C^t D_pol=D_pol C give K Pi_C=D_pol Pi_ph and equality of the first real gauge term by direct multiplication. Pi_C has return I because its basis is (SC,L); B_C is its unchanged complete holomorphic remainder. Exponentiating Pi_C splits the original long factor into the displayed q power, character monomial and full unit exponential. The coefficient map sends the old long vector h to n_C; v to v+n_C gives exactly the old support difference. X_C is explicitly the exponential of Z_C, with inverse logarithm modulo the same periods; the toric characters and opposite monomials preserve the frame and vector-coordinate inverses. The fixed covector chi=gamma* is retained.')

p.scope('undoubled-physical-gauge', 'The physical Gaussian is',
        'In the cusp coordinates the short refinement is',
        compose(p.symbols([('U', r'U_{\rm ph}'), ('W', r'W_{\rm ph}'),
                           ('v', r'v_{\rm lin}'),
                           ('h', r'h_{\mathcal L}'), ('F', r'F_{\mathcal L}'), ('J', r'J_{\mathcal L}')]),
                p.literals([('Z_1', r'(Z_{\rm ph})_1', 1)])),
        'The undoubled Gaussian uses the same physical coordinates and the identical half exponent. Its three map labels h_L,F_L,J_L index the corresponding lifts to the undoubled line L, with the same factors and target-coordinate inverse factors. The base maps are exactly those of the D lifts, and the stated L tensor square to D identification compares their line factors through the unchanged monomial gauge. Every integral unit exponent is preserved.')
p.scope('cusp-refinement-and-monomial',
        'In the cusp coordinates the short refinement is',
        'At a rank-one site the short refinement is',
        p.literals([(r'\epsilon', r'\epsilon_{\rm ref}', 2),
                    ('X^{L_0}', r'\mathbf X_C^{L_0^t}', 1),
                    ('X^{-L_0}', r'\mathbf X_C^{-L_0^t}', 1)]),
        'epsilon_ref is the identical short refinement column (1,0)^t. The support, integral linear row L_0, scalar phase and characters retain their entries. With the explicit column-character convention, X_C^{L_0^t}=exp(2 pi i L_0 Z_C) is exactly the old dense monomial; its reciprocal is the unchanged inverse. The public classification epsilon remains its scalar indicator.')
p.scope('rank-one-refinement-coordinate',
        'At a rank-one site the short refinement is', r'At \(I_2\)',
        p.literals([(r'\epsilon_N^tZ', r'\epsilon_N^tZ_N', 1)]),
        'The rank-one refinement is evaluated on the explicitly normalized Z_N, whose inverse is C_S Z_N. Its component definition Q(S C_S e_j), support, integral affine comparison and tensor-square map are the same ones.')
p.scope('special-I2-basis', r'At \(I_2\) use the explicit primitive basis',
        r'This completes the equivariant-line construction',
        compose(p.literals([(r'\sigma', r'\sigma_{\rm Bez}', 1),
                            ('p_0', 'p_2', 4),
                            ('h_{\\rm gen}=h+yw_0', r'h_{\rm per}=h_2+y_Lw_0', 1),
                            ('p_{\\rm gen}=p_2', r'p_0=p_2', 1)]),
                p.symbols([('h', r'h_2')])),
        'The explicit I2 specialization keeps l and w_0 but names its changed columns p_2 and h_2=v. The earlier general columns satisfy p_0=p_2+(sigma_Bez-1)l/2 and h_per=h_2+y_L w_0. These are the same two unimodular shears; subtracting the multiples is the inverse. All four explicit short/long matrices, the specialized pairing, Q(p_2), degrees and characters retain their entries.')

p.scope('borel-positive-character', 'Subtract that multiple of the whole-circle base',
        r'\item \emph{Full coprime homotopy',
        p.symbols([('T', r'T_{\rm Bor}')]),
        'T_Bor is the same positive whole-circle base class used in the common subtraction and inverse addition. The monodromy matrices T_i and their selected-site T keep their original geometric roles.')
p.exact('positive-character-binding',
        r'''all fixed curves. Subtract that multiple of the whole-circle base
class \(T_{\rm Bor}\); adding it back is the inverse.''',
        r'''all fixed curves. Put
\(T_{\rm Bor}=c_1(\text{positive weight-one character})\in H^2(BS^1;\mathbb Z)\).
Subtract that multiple of the whole-circle base class \(T_{\rm Bor}\);
adding it back is the inverse.''',
        'The base character is explicitly the same positive weight-one circle character whose reductions are used in the following formulas. Its coefficient subtraction/addition and both finite fixed-curve restrictions are unchanged.')
p.scope('crt-map-family', 'On coefficient groups, let',
        r'\item \emph{The full order-nine detector',
        p.literals([(r'\theta', r'\Theta_{\rm CRT}', 4)]),
        'Theta_CRT is exactly the residue map Z/c to the direct sum of its prime factors. Its inverse remains sum j_p; the simplicial Eilenberg--Mac Lane maps, both homotopy composites, detector tables and refined-coordinate tables preserve every coefficient. The scalar circle parameter theta retains its action role.')
p.exact('three-primary-generator-import',
        r'''Use the coefficient map $e\mapsto e_3$ on $\mathbb Z/3$,
with inverse $e_3\mapsto e$.''',
        r'''Use the coefficient map $e_{\rm EM}\mapsto e_3$ on $\mathbb Z/3$,
with inverse $e_3\mapsto e_{\rm EM}$.''',
        'The imported LF generator is now explicitly named e_EM. The coefficient isomorphism sends that exact generator to e_3, and the printed inverse sends e_3 back to e_EM. Its Eilenberg--Mac Lane map carries gamma_3(e_EM) to gamma_3(e_3), preserving the positive CP3 reduction, coefficient-one detector and natural operation. This coordinates the public import with the root-owned LF packet; the local clutch integer e remains unchanged.')
p.exact('coprime-tor-parameters',
        r'''annihilating powers kills the tensor product, and
\(\operatorname{Tor}(\mathbb Z/p^a,B)=B[p^a]=0\) for \(\varpi\)-primary
\(B\). Direct sums and filtered colimits prove the corresponding''',
        r'''annihilating powers kills the tensor product. For a positive integer
\(n_{\rm Tor}\) and a \(\varpi\)-primary group \(B_{\varpi}\),
\(\operatorname{Tor}(\mathbb Z/p^{n_{\rm Tor}},B_{\varpi})
 =B_{\varpi}[p^{n_{\rm Tor}}]=0\).
Direct sums and filtered colimits prove the corresponding''',
        'n_Tor and B_varpi are the identical formal exponent and group arguments in the printed Tor identity, now explicitly bound over their already used positive-exponent and varpi-primary domains. Identity on both arguments preserves the p-power torsion subgroup, Bezout annihilation and filtered-colimit argument. The marked weight a and the graph matrix B retain their existing roles.')
p.exact('cyclic-resolution-generator',
        r'''The cyclic resolution has differentials \(g-1,N_9\); with trivial
\(\mathbb Z/9\) coefficients they are zero.''',
        r'''Write \(g_9\) for that positive generator of \(C_9\).
The cyclic resolution has differentials \(g_9-1,N_9\), where
\(N_9=\sum_{j=0}^{8}g_9^j\); with trivial
\(\mathbb Z/9\) coefficients they are zero.''',
        'g_9 is the same chosen positive C_9 generator in the cyclic resolution. Identity on the group ring preserves its augmentation differential g_9-1 and the explicitly displayed nine-term norm N_9. The elliptic section cocycle g remains the same site parameter. The resolution, period-two shift, cohomology algebra and positive character are unchanged.')
p.exact('literal-fixed-curve-pullback',
        r'''Pullback verifies the inverse through \(i^*i_*(z)=e z\); the remaining
relative class vanishes after localization.''',
        r'''Here \(i_C:C_f\hookrightarrow X\) and \(i_E:E_3\hookrightarrow X\)
are the fixed-curve inclusions, and \(e_C,e_E\) are their equivariant
normal Euler classes. Pullback verifies the inverse through
\[
 i_C^*i_{C*}(z_C)=e_Cz_C,\qquad
 i_E^*i_{E*}(z_E)=e_Ez_E.
\]
The remaining relative class vanishes after localization.''',
        'The two identities explicitly instantiate the original Thom self-intersection formula for the exact inclusions i_C and i_E already used in the preceding inverse restriction map. Their equivariant normal Euler classes are the same denominators e_C,e_E. Dividing by them after localization and pulling back recovers each input; the disjoint fixed components give zero cross terms. The generic i and e placeholders no longer reuse the earlier CW inclusion and ordinary clutch integer. No self-intersection coefficient or inverse map changes.')
p.scope('edge-localization-and-borel-class',
        r'On \(C_f\), set', r'At \(E_3\), the primitive periods',
        compose(p.literals([('kT', r'k_{\rm edge}T_{\rm Bor}', 1)]),
                p.symbols([('k', r'k_{\rm edge}'), ('T', r'T_{\rm Bor}')])),
        'The same k_edge=b kappa is carried through a_edge, both homogeneous weights, z_C(z_C-k_edge T_Bor), both normal roots, the Euler class and the complete order-nine quotient. The subgroup and character maps are unchanged, so all coefficients and inverse localization maps retain their original values.')
p.scope('restricted-positive-character',
        r'Here $t_3=\rho_3(T)$', r'\item \emph{The other primary cubics.}',
        p.literals([(r'\rho_3(T)', r'\rho_3(T_{\rm Bor})', 1),
                    (r'\sigma\eta', r'\Sigma_{\rm susp}\eta', 1),
                    (r'\sigma(-d_E\eta)', r'\Sigma_{\rm susp}(-d_E\eta)', 1)]),
        't_3 is the same reduction of the positive circle character. Sigma_susp names the same left-interval suspension used in the two displayed pullbacks; the flip, sign, coefficient d_E and slant inverse are unchanged.')
p.exact('suspension-operator-binding',
        r'''collapse the wedge. With the suspension convention of \eqref{maps:eq:third-power-suspension},
\(q_{\rm susp}^*\Sigma_{\rm susp}\eta''',
        r'''collapse the wedge. Write \(\Sigma_{\rm susp}\) for the left-interval suspension of
\eqref{maps:eq:third-power-suspension}, with its stated slant inverse. Then
\(q_{\rm susp}^*\Sigma_{\rm susp}\eta''',
        'Sigma_susp is explicitly bound to the cited positive left cross product, with the unchanged slant-by-interval inverse. The cohomological sign from flipping the two degree-one factors remains minus one; the root rotation and Bezout coefficient keep their separate names.')
p.exact('degree-two-fixed-curve-class',
        r'''therefore zero. On \(C_f\), with \(h=\alpha_2|C_f\), the only
integrating term of \((h+t\tau^2)^3/\tau^4\) is \(t h\).''',
        r'''therefore zero. On \(C_f\), put \(\alpha_{2,C}=\alpha_2|C_f\). The only
integrating term of \((\alpha_{2,C}+t\tau^2)^3/\tau^4\) is \(t\alpha_{2,C}\).''',
        'alpha_2,C is exactly the same restricted degree-two class formerly denoted h. Identity on H^2(C_f;F_2) preserves the cubic expansion, integrating term, degree and resulting mod-two invariant t.')
p.scope('normal-character-and-borel-root',
        r'For \(p=3,5\), let the ordinary roots',
        'Here is the complete conversion to the Tate coordinates.',
        p.literals([(r'\lambda', r'\lambda_{\rm norm}', 4),
                    (r'\rho_p(T)', r'\rho_p(T_{\rm Bor})', 1)]),
        'lambda_norm is the same normal eigenline character, with its opposite -lambda_norm. The expansion of both roots, p1=-2e and localization coefficient remain identical. t_p is the same reduction of T_Bor. The original shear covector lambda_line retains its separate explicitly named row.')
p.scope('tate-character-all-uses',
        'Here is the complete conversion to the Tate coordinates.',
        'For the two-primary projection',
        compose(p.literals([(r'\sigma', r'\sigma_{\rm Bez}', 1)]),
                p.symbols([('w', r'w_{\rm norm}')])),
        'w_norm is the identical Tate normal-character residue already defined at E_p. All weight quotients, degree-zero localization identities, generator rescaling and its inverse, fourteen-row table entries and final equality criterion use the same residue. The formal toric chart coordinate w and the long vector w_0 retain their specified domains.')
p.scope('two-primary-bordism-generators', 'For the two-primary projection',
        'The exact CRT maps give',
        compose(p.literals([(r'\epsilon', r'\epsilon_{2,\rm bord}', 2),
                            (r'\zeta', r'\zeta_{2,\rm bord}', 5)]),
                p.symbols([('A', r'a_{\rm bord}'), ('B', r'b_{\rm bord}')])),
        'epsilon_2,bord and zeta_2,bord are the same two generators of the stated free-lift quotient, with relations epsilon_2,bord=0 and 2 zeta_2,bord=0. The coefficient pair a_bord,b_bord maps to b_bord mod two, with the same inverse class b_bord zeta_2,bord. The positive CP3 reduction and both invariants remain unchanged; the public epsilon indicator and line coordinate zeta retain their own names.')
p.exact('three-primary-bordism-generator',
        r'''\eqref{maps:eq:three-primary-bordism}; its inverse fundamental-class
map is $j\gamma_3(e_3)\mapsto j\zeta$.''',
        r'''\eqref{maps:eq:three-primary-bordism}. Write \(\zeta_{3,\rm bord}\)
for the image of its positive \(\mathbb{CP}^3\) reduction generator
\(\zeta_{\rm bord}\) under the coefficient map \(e_{\rm EM}\mapsto e_3\).
The inverse fundamental-class map is
$j\gamma_3(e_3)\mapsto j\zeta_{3,\rm bord}$.''',
        'zeta_3,bord is explicitly the image of LF’s positive CP3 reduction generator zeta_bord under K(e_EM to e_3,2) on spin bordism. The inverse coefficient map e_3 to e_EM recovers zeta_bord. Naturality sends the fundamental class gamma_3(e_EM) to gamma_3(e_3), so j gamma_3(e_3) to j zeta_3,bord is the same inverse fundamental-class map, with the same zero-kernel conclusion. This coordinates the exact public import with the root-owned LF packet.')
p.scope('fundamental-class-map-name',
        r'Here $\Omega_6^{\rm Spin}(\mathrm{pt})=0$', None,
        p.literals([('(P,h)', r'(P,h_{\rm bord})', 5),
                    (r'h(\zeta_{2,\rm bord})', r'h_{\rm bord}(\zeta_{2,\rm bord})', 1)]),
        'h_bord is the same fundamental-class homomorphism in every occurrence of Zhubr’s pair, including the zero coefficient group, two-primary generator, model values and final injection. It sends [M,f] to f_*[M]. The actual h-cobordism terminology is retained, and none of the deck, translation or period-column objects is rebound.')
p.exact('fundamental-class-map-binding',
        r'''Here $\Omega_6^{\rm Spin}(\mathrm{pt})=0$, by
\ref{maps:src:D.1.11} for coefficient group zero, whose injective
pair $(P,h_{\rm bord})$ has zero target.''',
        r'''Write \(h_{\rm bord}([M,f])=f_*[M]\) for the fundamental-class map
in the cited spin-bordism pair. Here $\Omega_6^{\rm Spin}(\mathrm{pt})=0$, by
\ref{maps:src:D.1.11} for coefficient group zero, whose injective
pair $(P,h_{\rm bord})$ has zero target.''',
        'This explicitly defines the same fundamental-class homomorphism used by the cited classification pair. The pushforward f_*[M] is the unchanged mathematical map; it applies to each displayed coefficient target and preserves all generator values and inverse maps.')
p.scope('realized-finite-vector',
        'All listed types are realized:', 'Within an even sector,',
        p.symbols([('v', r'v_{\rm fin}')]),
        'The realization uses the same finite vector v_fin=n ell+r delta with m=d_i,e=1,n=m-1,r=0. Its division by m is the same affine lift, with the unchanged determinant and freeness assertions.')
p.scope('recognition-coefficient-group',
        'Zhubr Theorem 5, printed p.796,', 'Both the constructed threefolds',
        p.symbols([('G', r'G_{\rm coeff}')]),
        'G_coeff is the identical coefficient-group parameter in the quoted bordism injection and marked H_2 isomorphism. Both target factors and the K(G_coeff,2) source are changed together by identity on that group, preserving the complete recognition map. The elliptic section G retains its original geometric role.')
p.scope('coefficient-generator-family', 'On coefficient groups, let', None,
        p.literals([('e_p', r'e_{p,\rm coef}'),
                    ('e_2', r'e_{2,\rm coef}'),
                    ('e_3', r'e_{3,\rm coef}'),
                    ('e_5', r'e_{5,\rm coef}')]),
        'e_{p,coef} is the identical chosen generator of each cyclic coefficient group Z/p, including the model markings for p=2,3,5. Every j_p injection, positive divided-power generator, two-primary bordism value, connected-sum model value and Phi/Phi^{-1} table entry is changed by identity on that same generator. The LF input map is exactly e_EM to e_{3,coef}, with inverse e_{3,coef} to e_EM, and its induced bordism map transports zeta_bord to zeta_{3,bord}. All integer coefficients and orientations are retained. The physical periods e_1,e_2 and the standard input columns of the cusp basis retain their original coordinate meanings.')


def verify_transport():
    """Exact polynomial identities for the explicitly displayed basis maps."""
    import sympy as sp
    import sys
    print('Preparation runtime:',sys.version.split()[0],'SymPy',sp.__version__)
    a, b, nu, kap = sp.symbols('a b nu kap', nonzero=True)
    tau, zet, rhoL = sp.symbols('tau zet rhoL')
    C = sp.Matrix([[nu, b*kap], [-a*kap, (1-a*b*kap**2)/nu]])
    Ci = sp.Matrix([[(1-a*b*kap**2)/nu, -b*kap], [a*kap, nu]])
    D = sp.diag(a, -b)
    Pph = sp.Matrix([[tau, -b*zet], [a*zet, rhoL]])
    K = C.T*D
    simplify = lambda M: M.applyfunc(sp.simplify)
    assert simplify(C*Ci) == sp.eye(2) == simplify(Ci*C)
    assert simplify(C.T*D-D*C) == sp.zeros(2)
    assert simplify(K-K.T) == sp.zeros(2)
    assert simplify(K*Ci*Pph-D*Pph) == sp.zeros(2)
    u1,u2,w1,w2=sp.symbols('u1 u2 w1 w2')
    Uph=sp.Matrix([u1,u2]); Wph=sp.Matrix([w1,w2])
    assert sp.simplify(((Ci*Uph).T*K*Wph-Uph.T*D*Wph)[0]) == 0
    x,y=sp.symbols('x y'); vv=sp.Matrix([x,y]); cv=C*vv
    psi=lambda r,s: -a*C[1,1]*r*r+2*a*b*kap*r*s+b*nu*s*s+a*r
    assert sp.simplify(psi(cv[0],cv[1])+(vv.T*K*vv)[0]-a*(C*vv)[0]) == 0
    # Arbitrary invertible bases: no period-entry specialization is used.
    s11,s12,s21,s22,l11,l12,l21,l22=sp.symbols('s11 s12 s21 s22 l11 l12 l21 l22')
    CS=sp.Matrix([[s11,s12],[s21,s22]])
    CL=sp.Matrix([[l11,l12],[l21,l22]])
    KN=CS.T*D*CL; PN=CS.inv()*Pph*CL
    assert simplify(KN.T*PN-CL.T*D*Pph*CL)==sp.zeros(2)
    assert sp.simplify(((CS.inv()*Uph).T*KN*(CL.inv()*Wph)-Uph.T*D*Wph)[0])==0
    assert sp.simplify(((CL.inv()*Wph).T*KN.T*PN*(CL.inv()*Wph)-Wph.T*D*Pph*Wph)[0])==0
    n0,A0,sg,d0,B0,yl=sp.symbols('n0 A0 sg d0 B0 yl', nonzero=True)
    th=(1-A0*sg)/n0; xl=(1-B0*yl)/d0
    CS0=sp.Matrix([[n0,sg],[-A0,th]])
    CS0i=sp.Matrix([[th,-sg],[A0,n0]])
    CL0=sp.Matrix([[xl,-B0],[yl,d0]])
    CL0i=sp.Matrix([[d0,B0],[-yl,xl]])
    assert simplify(CS0*CS0i)==sp.eye(2)==simplify(CS0i*CS0)
    assert simplify(CL0*CL0i)==sp.eye(2)==simplify(CL0i*CL0)
    ak,B,sigma,yL=sp.symbols('ak B sigma yL')
    CS2=sp.Matrix([[2,1],[-ak,(1-ak)/2]])
    SS=sp.Matrix([[1,(sigma-1)/2],[0,1]])
    expectedCS=sp.Matrix([[2,sigma],[-ak,(1-ak*sigma)/2]])
    CL2=sp.Matrix([[1,-B],[0,1]])
    SL=sp.Matrix([[1,0],[yL,1]])
    expectedCL=sp.Matrix([[1-B*yL,-B],[yL,1]])
    assert simplify(CS2*SS-expectedCS)==sp.zeros(2)
    assert simplify(CL2*SL-expectedCL)==sp.zeros(2)
    assert SS*sp.Matrix([[1,-(sigma-1)/2],[0,1]])==sp.eye(2)
    assert SL*sp.Matrix([[1,0],[-yL,1]])==sp.eye(2)
    print('Exact transport identities: cusp C/Cinverse, K symmetry, both gauge terms, full physical support pullback, both rank-one gauge terms, literal C_S/C_L inverses under their Bezout identities, and both I2 shears/inverses passed.')


def stage_final():
    root=p.root
    stem='S6_SERIES_PUBLISH_c9_02LJ_final_bindings'
    out=root/'agents'/'continuation9_02LJ_final_bindings'
    tmp=root.parents[1]/'tmp'/'c9_02LJ_final_bindings'
    out.mkdir(exist_ok=True); tmp.mkdir(exist_ok=True)
    back=p.new
    for op in reversed(p.operations):
        assert back.count(op['new'])==1,(op['name'],'reverse guard')
        back=back.replace(op['new'],op['old'],1)
    assert back==p.old
    assert p.old[:p.old.index(r'\end{theorem}')]==p.new[:p.new.index(r'\end{theorem}')]
    tablecounts={}
    for env in ('array','tabular'):
        pat=r'\\begin\{'+env+r'\}.*?\\end\{'+env+r'\}'
        oldtables=re.findall(pat,p.old,re.S)
        newtables=re.findall(pat,p.new,re.S)
        undo=[(r'\Theta_{\rm CRT}',r'\theta'),(r'w_{\rm norm}','w'),
              (r'e_{p,\rm coef}','e_p'),(r'e_{2,\rm coef}','e_2'),
              (r'e_{3,\rm coef}','e_3'),(r'e_{5,\rm coef}','e_5')]
        for newold,oldname in undo:
            newtables=[s.replace(newold,oldname) for s in newtables]
        assert oldtables==newtables,(env,'all table entries and domains')
        tablecounts[env]=len(oldtables)
    for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',
                r'\\(?:[A-Za-z]*ref|cite[A-Za-z]*)\*?(?:\[[^]]*\])?\{[^}]+\}']:
        assert re.findall(pat,p.old)==re.findall(pat,p.new),pat
    assert '\r' not in p.new
    oldlines,newlines=p.old.splitlines(True),p.new.splitlines(True)
    fullnew=p.source[:p.start]+p.new+p.source[p.end:]
    for context in range(2,14):
        groups=list(difflib.SequenceMatcher(a=oldlines,b=newlines,autojunk=False).get_grouped_opcodes(n=context))
        fragments=[]
        for g in groups:
            old=''.join(oldlines[g[0][1]:g[-1][2]])
            new=''.join(newlines[g[0][3]:g[-1][4]])
            fragments.append((old,new))
        if all(p.source.count(o)==1 and fullnew.count(n)==1 for o,n in fragments):
            break
    else: raise AssertionError('unique full-source fragment guards')
    rows=[]
    def substantive(line):
        t=line.strip()
        return len(t)>12 and not re.match(r'\\(?:begin|end)\{',t)
    for i,(old,new) in enumerate(fragments,1):
        relevant=[op for op in p.operations if
                  any(substantive(x) and x in old for x in op['changed_old']) or
                  any(substantive(x) and x in new for x in op['changed_new'])]
        assert relevant,(i,'operation explanation')
        firstline=p.source.count('\n',0,p.source.index(old))+1
        lastline=firstline+len(old.splitlines())-1
        rows.append(dict(change_id=f'III-C9-02LJ-FINAL-BIND-{i:03}',type='D20',
                         statement_id=p.sid,old_location=f'02LJ full statement/proof; frozen source lines {firstline}–{lastline}; exact unique fragment',
                         old_page='candidate05 physical 486–502',new_location='same statement/proof and permanent identifiers',
                         new_page='pending rebuilt image review',old_text=old,new_text=new,
                         reason=' '.join(dict.fromkeys(op['reason'] for op in relevant)),
                         review_status='Full current 1395-line statement/proof read after actual candidate05 images. Complete original/candidate comparison and exact reverse recover the admitted baseline. Root admission and changed-page image reading pending; no independent proof credit.'))
    result=p.source
    for row in rows:
        assert result.count(row['old_text'])==1
        result=result.replace(row['old_text'],row['new_text'],1)
    assert result==fullnew
    for row in reversed(rows):
        assert result.count(row['new_text'])==1
        result=result.replace(row['new_text'],row['old_text'],1)
    assert result==p.source
    assert p.source_path.read_bytes()==p.source_bytes
    (tmp/(stem+'_baseline.tex')).write_text(p.old)
    (tmp/(stem+'_proposed.tex')).write_text(p.new)
    (out/(stem+'.diff')).write_text(''.join(difflib.unified_diff(oldlines,newlines,
                                      fromfile='02LJ admitted baseline',tofile='02LJ final binding proposal',n=5)))
    fields=list(rows[0])
    with (out/(stem+'_defects.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
    with (root/'CHECK_EVENTS.tsv').open(newline='') as f:
        eventfields=next(csv.reader(f,delimiter='\t'))
    stamp=datetime.now(timezone.utc).isoformat()
    event={k:'' for k in eventfields}
    eid='publish:c9:III:02LJ:final-rendered-bindings'
    event.update(statement_id=p.sid,date=stamp[:10],who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; continuation nine',
                 type='used and rechecked in this run',
                 outcome=f'Read the complete current 1395-line statement/proof after actual candidate05 images 486–502, with prior source exposure. Prepared {len(rows)} unique reversible fragments in {len(p.operations)} semantic operations. Bound physical/rank-one/cusp coordinates and full period units; checked the exact basis maps and inverses, both Gaussian pullbacks, support identity and I2 shear comparison. Qualified each observed same-proof named role, retaining map entries, table values, labels and citations. Coordinated the explicit e_EM and zeta_bord imports with the root-owned LF packet. This is exposed source review, with no independent-proof or additional image-reading credit. Root admission and rebuilt changed-page images remain pending.',
                 event_id=eid,phase='publication continuation9',source_file='S6_SERIES_PUBLISH_III.tex',
                 source_row='02LJ complete current statement/proof; candidate05 observed bindings',
                 source_event_type='used and rechecked in this run',evidence_group=eid,
                 publish_input_file='../CLAUDE_READING_LOG_PAPER_III.md',
                 publish_input_row='P15; prompt0.8 complete proof scope; candidate05 observed bindings',
                 date_utc=stamp,where=f'code/{stem}.py; code/{stem}.out; agents/continuation9_02LJ_final_bindings/{stem}_review.md; agents/continuation9_02LJ_final_bindings/{stem}_defects.tsv; agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_c9_candidate05_pages434_567_review.md')
    with (out/(stem+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=eventfields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerow(event)
    occurrence=[]
    for op in p.operations:
        for count,old,new in op['details']:
            occurrence.append(dict(operation=op['name'],count=count,old=old,new=new))
    with (out/(stem+'_occurrences.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['operation','count','old','new'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(occurrence)
    print('02LJ baseline',len(oldlines),sha(p.old),'candidate',len(newlines),sha(p.new))
    print('Semantic operations',len(p.operations),'guarded fragments',len(rows),'unique context',context)
    oldnums=Counter(re.findall(r'\d+',p.old));newnums=Counter(re.findall(r'\d+',p.new))
    print('Decimal-token additions from explicit coordinate/domain/index bindings:',dict(newnums-oldnums))
    print('Decimal-token removals from qualified indices:',dict(oldnums-newnums))
    print('The complete theorem statement is byte-identical; all permanent labels, tags, references and citations are byte-identical sequences.')
    print('All table entries and domains recover the original bytes under the explicit identity name maps:',tablecounts)
    for op in p.operations:
        print(op['name'])
        for count,old,new in op['details']:
            # Keep exact token counts readable; full fragment texts are in TSV/diff.
            print(' ',count,repr(old)[:220],'->',repr(new)[:220])
    print('Full operation and source-fragment reverses passed. Permanent identifiers and canonical source bytes unchanged.')
    print('Observed canonical source SHA-256',sha(p.source))
    print('Proposed used-only event',eid)
    print('Packet',out.relative_to(root),'complete candidates outside checkpoint',tmp)
    assert p.source_path.read_bytes()==p.source_bytes


if __name__=='__main__':
    verify_transport()
    stage_final()
