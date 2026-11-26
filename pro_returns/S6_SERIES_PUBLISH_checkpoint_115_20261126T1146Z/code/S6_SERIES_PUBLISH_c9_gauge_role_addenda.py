#!/usr/bin/env python3
"""Whole-proof role repairs for the already read LB/LE/LF/LJ units.

This prepares exact guarded proposals only. All complete candidates remain
outside the checkpoint; canonical manuscript, defects and events are untouched.
"""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet
from S6_SERIES_PUBLISH_c9_notation_addendum_io import compose, stage

packets = []
p = Packet('02LB', 'maps:src:D.2.35',
           '12a980978b1c7366a1c7667d601e0db54e3422e002d8321a3444f8f42d7cd1b6',
           '435–445', 'Finite Bezout coefficient versus marked valuation coefficient.')
p.numeric_names = [(r'\alpha_0', r'\alpha_{\rm fin}')]
p.scope('finite-bezout-coefficient', r'Choose $\alpha_0m+\eta_0n=1$.',
        'Thus the functional one on $s$',
        p.literals([(r'\alpha_0', r'\alpha_{\rm fin}', 4)]),
        'alpha_fin is the identical integer chosen in alpha_fin m+eta_0 n=1, with inverse name substitution alpha_0=alpha_fin. The full finite kernel columns, their even fibre coefficients and t(ell)=b r_0(alpha_fin+eta_0 e)s therefore retain their exact values. The sector cutting/rejoining maps and the ordinary-cap translation and its inverse are unchanged. Earlier alpha_0 remains the valuation coefficient in H_val=alpha_0 nu_0 and n_per=alpha_0 nu_1; the same integer name is no longer rebound to a separately chosen Bezout coefficient.')
packets.append(p)

p = Packet('02LE', 'maps:src:D.2.38',
           '851d795feb6157a8c8c540224cda68fd3a76e8cdc7b7f057562b638d900ba982',
           '457–473', 'Finite indices, prime coefficients, fixed components and Tate/CRT parameters.')
p.scope('upright-cap-labels', 'Writing $F$ for a finite cap',
        'There are seven order-ten patterns',
        p.literals([('Writing $F$ for a finite cap and $O$ for an original cap,',
                     r'Writing $\mathrm F$ for a finite cap and $\mathrm O$ for an original cap,', 1),
                    (':F&', r':\mathrm F&', 3), (':O&', r':\mathrm O&', 3)]),
        'The upright labels F and O name exactly the same finite and original cap choices in the same six table cells. Identity on the labelled site option gives the comparison in both directions; every numerical entry and all twelve patterns are unchanged. The italic F used for the lifted line return keeps that map and its inverse.')
p.exact('finite-site-product',
        r'residual $c=b/\prod_{F}q_i$ and retain $c=10,14$. These finite',
        r'residual $c=b/\prod_{i\in\mathcal I_{\rm fin}}q_i$, where $\mathcal I_{\rm fin}$'+'\n'
        'is the set of finite additive sites, and retain $c=10,14$. These finite',
        'I_fin is explicitly the same finite additive site set formerly denoted by F in the product. Identity on each site index preserves its vertical index q_i and hence the product and c. The preceding coprimality test, multiplicities and retained input rows are unchanged; the actual line return F retains its own name.')
p.scope('finite-vertical-index', 'The fixed columns are primitive and the finite coinvariant section',
        'The index-one cusp', p.symbols([('q', r'q_{\rm fin}')]),
        'q_fin is the identical finite vertical index, one for II and three for IV. The identity beta_0 to beta_0 sends [delta]=q_fin beta_0, the norm map N_m beta_0=(m/q_fin)delta and the pairing -Omega(beta_0,ell)=b/q_fin to the same values. All three full Thom columns, the two inverse integer substitutions and the final relation (b/q_fin)(n-me)s are preserved. The base-disc coordinate q and prime coefficient parameter now have separate explicit names; no geometric map is changed.')
prime = lambda: compose(p.literals([('_q', r'_{\varpi}')]), p.symbols([('q', r'\varpi')]))
p.scope('prime-character-binding', r'In particular $H^2(X;\mathbb Z)=0$',
        r'\item \emph{One undoubled line on the common piece.}', prime(),
        'varpi ranges over exactly the same primes 2,p as the former q in alpha_q(s)=1. The coefficient identification Z/varpi to Z/q is the identity residue map for each of those two values, with identity inverse. alpha_varpi is the same functional on the marked generator s and every sweep. The finite-site q_i in the unchanged divisibility calculation is preserved.')
p.scope('prime-line-and-fixed-set-maps', 'All these line extensions restrict',
        'At $I_2$, its local', prime(),
        'The same prime parameter varpi=2,p indexes the reduction rho_varpi, alpha_varpi, and the subgroup translation delta/varpi. Identity on the coefficient residues and on C_varpi sends the displayed line restriction to the original one. The primitive quotient sends delta/varpi to (n_0/varpi)p_0 and its subtraction inverse exactly as before; varpi divides n_0 is the same fixed-point criterion. The tensor-square line comparison and all monomial inverse maps are unchanged.')
p.scope('prime-borel-and-coprime-maps', r'For $q=2,p$, $\alpha_q$ has',
        'An automorphism on the odd factor', prime(),
        'For varpi=2,p, the Borel extension U_varpi, subgroup C_varpi, coefficient field F_varpi, reductions rho_varpi, mixed class xi_varpi and space K_varpi=K(Z/varpi,2) are the same indexed objects as before. Identity on each coefficient cyclic group induces the same simplicial Eilenberg--Mac Lane maps and inverse. The pi1 section, common base-character subtraction/addition, full mixed restriction terms, wedge inclusion and CW inverse, and both integer CRT maps are unchanged. Only the common prime-index spelling changes; all numerical exponents and fixed values 2,p remain.')
p.exact('odd-factor-unit',
        r'''An automorphism on the odd factor, multiplication by $r$, lifts
to the unit $p+(1-p)r$ modulo $2p$; its inverse is
$p+(1-p)r^{-1}$.''',
        r'''An automorphism on the odd factor, multiplication by $u_{\rm aut}$, lifts
to the unit $p+(1-p)u_{\rm aut}$ modulo $2p$; its inverse is
$p+(1-p)u_{\rm aut}^{-1}$.''',
        'u_aut is the same unit in Z/p that multiplies the odd coefficient factor. The inverse renaming returns r=u_aut. The idempotents p and 1-p give precisely the same lift to a unit modulo 2p, and multiplying the displayed lift and inverse gives one in both CRT factors. The finite affine integer r and Tate valuation no longer share the automorphism parameter name.')
p.scope('involution-fixed-curve', 'For the involution the normal representation on each fixed curve is',
        'The elliptic term is zero',
        p.literals([('on each fixed curve is', r'on each fixed curve $F_{\rm fix}$ is', 1),
                    (r'\nu_F', r'\nu_{F_{\rm fix}}', 4), ('TF)', r'TF_{\rm fix})', 1),
                    (r'\sum_F', r'\sum_{F_{\rm fix}}', 1),
                    ('i_{F*}', r'i_{F_{\rm fix}*}', 1), ('e_F', r'e_{F_{\rm fix}}', 1)]),
        'F_fix is explicitly the same fixed component of the involution. Identity of its embedding preserves the tangent bundle, the complex rank-two normal representation, both Chern classes, its Euler class and inclusion i_Ffix. The Thom restriction inverse still sums i_Ffix,*(z/e_Ffix) over exactly the same components. Its composition with restriction is the original self-intersection calculation; the line return F retains its separate map.')
p.scope('odd-fixed-curve', 'On a fixed curve for $C_p$, let the ordinary normal roots be',
        'The identity allows unequal ordinary normal degrees.',
        p.literals([('On a fixed curve for $C_p$,', r'On a fixed curve $F_{\rm fix}$ for $C_p$,', 1),
                    ('|F=', r'|F_{\rm fix}=', 1), ('e_F', r'e_{F_{\rm fix}}', 1),
                    ('TF)', r'TF_{\rm fix})', 1)]),
        'The formal component argument F_fix is the same fixed curve of C_p with the same inclusion, tangent root and two normal eigenline roots. Identity on the curve preserves p_1(TX)|F_fix=-2e_Ffix and the displayed expansion of both sides. The subsequent localization pairing, quarter-map and Tate conversion retain all coefficients and markings.')
p.scope('tate-weight-definition', r'At $I_p$, put $r=-\kappa_i$',
        r'Formula \eqref{maps:eq:MP_local_46} gives',
        p.literals([('$r=', r'$r_{\rm Tate}=', 1), ('(ar)', r'(a r_{\rm Tate})', 1)]),
        'r_Tate=-kappa_i is the identical positive-valuation Tate component. The weight w=(a r_Tate)^(-1) is the same inverse residue as before and the following sigma a kappa_i=1 identity still gives w=-sigma. The affine integer r in v=n ell+r delta is preserved as the finite filling parameter; no weight or chosen action changes.')
p.exact('tate-conversion-use',
        r'marking at the unique $I_p$, $r=-\kappa_i$ and $w=(ar)^{-1}$.',
        r'marking at the unique $I_p$, $r_{\rm Tate}=-\kappa_i$ and $w=(a r_{\rm Tate})^{-1}$.',
        'This is the same r_Tate already defined at the unique I_p and the same inverse residue w. The following action conversion z to z^(nu^(-1)), its inverse z to z^nu, and all ordinary and equivariant pairings remain exactly as displayed.')
p.scope('crt-marking-residue', r'Here is the marking that compares \eqref{maps:eq:MP_local_70}',
        r'Both compositions in \eqref{maps:eq:MP_local_71}',
        p.literals([(' k&=', r' k_{\rm CRT}&=', 1), ('=k s', r'=k_{\rm CRT}s', 1),
                    ('$k$', r'$k_{\rm CRT}$', 1), (r'$k\bmod', r'$k_{\rm CRT}\bmod', 1)]),
        'k_CRT is the same residue P_2p-tp modulo 2p, with inverse renaming k=k_CRT. Phi still sends e_2 to p s and e_p to k_CRT s; its inverse still sends n s to (n mod 2)e_2+(P_p^(-1)n mod p)e_p. The even residue and its reduction P_p prove the same two identity composites. The earlier positive multiplicity parameter k in m=d_i k retains its name and value.')
packets.append(p)

p = Packet('02LF', 'maps:src:D.2.39',
           '621d32bf155fe0cf1cd0c414a4a9a221b498c90ff8dab9ef39b18f45b9a0b3be',
           '474–483', 'Roof function, finite affine parameter, Tate valuation and Borel root.')
p.scope('positive-roof-function', 'The contracting quotient is a mapping torus with a positive roof',
        "Translation by the identity-component N\\'eron logarithm",
        p.literals([('r(y)', r'r_{\rm roof}(y)', 3), (r'\max r', r'\max r_{\rm roof}', 1),
                    ('0<k<', r'0<k_{\rm roof}<', 1), ('{k+', r'{k_{\rm roof}+', 1),
                    ('(1-k', r'(1-k_{\rm roof}', 1)]),
        'r_roof(y)=r(y) is the same positive roof function on the same base points, and k_roof is the same chosen positive density constant k. Identity on the interval [0,r_roof(y)] and on that real constant preserves the bump function, integral, matching end derivatives and increasing map f_y. Its original increasing inverse remains unchanged pointwise. The finite affine integer r, positive finite multiplicity k, Tate valuation and root choice retain their own values and domains.')
p.scope('cusp-edge-weight', r'Write $k=b\kappa$.',
        'On an original additive cap, a norm', p.symbols([('k', r'k_{\rm edge}')]),
        'k_edge=b kappa is the same integral scalar weight of the prescribed cusp edge. Identity on the marked short coordinates d_delta=(-b kappa,nu) retains both actual toric-chart maps and inverse transitions. Their weights become (k_edge-nu,nu,-k_edge) and (-nu,nu-k_edge,k_edge), with identical integers. The fixed-point and tangent-weight assertions are the same; this k_edge is kept separate from the positive finite multiplicity k in m=d k.')
p.scope('edge-character-ring', r'Put ${a_{\rm edge}}=a(\nu-k)$',
        r'\item \emph{The coefficient-one detector and spin bordism.}',
        compose(p.literals([('kT', r'k_{\rm edge}T', 3)]), p.symbols([('k', r'k_{\rm edge}')])),
        'The unchanged edge weight k_edge=b kappa is used at both endpoint values of z_C, in z_C(z_C-k_edge T)=0 and in a_edge=a(nu-k_edge). Identity of the equivariant line and its two endpoint characters preserves this ring relation, the restriction of U and the inverse generator change alpha=a_edge u. No equivariant class or degree is changed.')
p.scope('edge-localization-weight', r'The normal roots on $C_0$ are',
        'The action on the elliptic component, in its primitive periods, is',
        p.symbols([('k', r'k_{\rm edge}')]),
        'The normal roots, Euler class and cubic-restriction expression use the same k_edge fixed by the earlier actual chart weights. The identity on those two normal line representations preserves e_C=nu(k_edge-nu)T^2 and the full mod-nine contribution a_edge^3 k_edge^2/(nu(k_edge-nu)). Its denominator and divisibility assertions have identical integer values; the integral and restriction maps are unchanged.')
p.scope('physical-tate-support', r'In physical coordinates let $r=\operatorname{ord}h_G=-\kappa$',
        'The affine term is the same $z^a$ gauge.',
        p.literals([('$r=', r'$r_{\rm Tate}=', 2), ('ab r', r'ab r_{\rm Tate}', 3),
                    ('brv_2', r'b r_{\rm Tate}v_2', 1)]),
        'r_Tate is the same integer ord h_G=-kappa in the nodal and cusp physical period charts. Substitution into the same physical support and both period-difference equations gives exactly their original values. In particular psi_ph(Cv)=-v^tKv+a(nu v_1-b r_Tate v_2) is the identical pullback; C, its inverse, the monomial z^a, the two Gaussian gauges and their reciprocals are unchanged. The affine r in the finite-cap power remains the original independent integer parameter.')
p.exact('borel-cube-root',
        r'$[e,z]\mapsto[er]\in ES^1/C_3$, where $r^3=z$, has inverse',
        r'$[e,z]\mapsto[e r_{\rm root}]\in ES^1/C_3$, where $r_{\rm root}^3=z$, has inverse',
        'r_root is the identical chosen cube root of z used to define the Borel map. Replacing the root by an element of C_3 gives the same target coset, and [et,z]=[e,t^3z] is the unchanged well-definedness relation. The inverse [e] to [e,1] and both quotient composites are the original ones; all period and degree coefficients remain unchanged.')
packets.append(p)

p = Packet('02LJ', 'maps:src:D.2.42',
           '2699be29b381c8b7dfc6e9b1c29cf0a489c5459718739cf62393b0f410fae966',
           '484–500', 'Roof function, affine integer, Tate residue and Borel root after the first retained-role addendum.')
p.scope('positive-roof-function', 'nonnegative bump \\(b_y\\) of integral one on a roof of length',
        'The ends have matching derivatives.',
        p.literals([('r(y)', r'r_{\rm roof}(y)', 2), (r'\max r', r'\max r_{\rm roof}', 1),
                    ('0<k<', r'0<k_{\rm roof}<', 1), ('{k+', r'{k_{\rm roof}+', 1),
                    ('(1-k', r'(1-k_{\rm roof}', 1)]),
        'r_roof is the same positive roof length and k_roof the same chosen positive density constant. Identity on the interval and that real number preserves the density integral, increasing function f_y and its inverse. The following negative Neron translation and reciprocal line gauge are the same maps on the same points. The affine filling parameter r and positive multiplicity k retain their integer ranges and full Thom formulas.')
p.scope('additive-vertical-index', r'Put \(z_Q=b(A-I)^{-1}g\) and \(q=1\)',
        r'\item \emph{Primitive rank-one periods and all scalar isotropy.}',
        compose(p.literals([('qA_{\\rm Bez}', r'q_{\rm vert}A_{\rm Bez}', 1),
                            ('qz_{Q,2}', r'q_{\rm vert}z_{Q,2}', 2),
                            ('qz_{Q,1}', r'q_{\rm vert}z_{Q,1}', 2),
                            ('rq', r'r q_{\rm vert}', 3),
                            ('qrC_1', r'q_{\rm vert}rC_1', 2)]),
                p.symbols([('q', r'q_{\rm vert}')])),
        'q_vert has the same two values: one for type II and two for type III. Identity on this integer for each additive type preserves the original-cap fibre map, its Bezout section and fixed basis, and the finite-cap coinvariant index, norm map and pairing. Every coefficient in the finite central-surface relation, its inverse Bezout basis, the three Thom columns and their inverse elimination is renamed together. The base coordinate q remains the original coordinate in Pi(q) and the toric charts; no comparison between different cap maps is asserted beyond retaining their original integer coefficients.')
p.scope('coprime-prime-parameter', r'power of \(p\). For different primes \(p,q\)',
        'On coefficient groups, let',
        compose(p.literals([('_q', r'_{\varpi}', 3)]), p.symbols([('q', r'\varpi')])),
        'varpi is the same second prime in the coprime argument formerly written q. Identity on Z/varpi carries the Eilenberg--Mac Lane space K_varpi and its coefficient maps to the original K_q. The tensor and Tor annihilator identities, wedge inclusion, cellwise construction of r_CW and both homotopy composites are unchanged. Its new name separates this prime parameter from the marked base coordinate and additive vertical index without weakening the argument.')
p.scope('tate-weight-definition', 'positive-valuation Tate residue is',
        r'This uses \(\sigma a\kappa_i=1\pmod p\).',
        p.literals([(r'\(r=', r'\(r_{\rm Tate}=', 1), ('(ar)', r'(a r_{\rm Tate})', 1)]),
        'r_Tate=-kappa_i is the same positive-valuation Tate residue. The inverse residue w=(a r_Tate)^(-1) and the identity sigma a kappa_i=1 preserve both normal characters and the marked generator. This does not change the finite affine integer r or the already indexed real period r_per.')
p.scope('borel-cube-root', 'There is an explicit Borel identification',
        r'The associated-bundle',
        p.literals([('[e r]', r'[e r_{\rm root}]', 1), ('r^3=z', r'r_{\rm root}^3=z', 1),
                    (r'\(er\)', r'\(e r_{\rm root}\)', 1)]),
        'r_root is the same cube root of z in the Borel identification, including its subsequent coset-independence check. Identity on the root choice preserves the coset [e r_root], and multiplying the root by C_3 gives the same target. The associated-bundle relation, inverse [e] to [e,1], period path and both composites remain unchanged.')
p.exact('tate-conversion-use',
        r'At \(E_p\), \(r=-\kappa_i\) and \(w=(ar)^{-1}=-\sigma\).',
        r'At \(E_p\), \(r_{\rm Tate}=-\kappa_i\) and \(w=(a r_{\rm Tate})^{-1}=-\sigma\).',
        'This uses the identical Tate residue already defined at E_p. The same reciprocal weight is substituted into every displayed Tate-coordinate conversion and all mod-p refined-class expressions; the original marking and its inverse evaluation remain unchanged.')
packets.append(p)

stage(packets, 'S6_SERIES_PUBLISH_c9_gauge_role_addenda',
      'continuation9_gauge_role_addenda', 'retained-gauge-role-readback',
      'Each renamed object is identified by the identity on its original domain or by the same explicit coefficient and coordinate maps; every affected inverse formula is preserved.')
