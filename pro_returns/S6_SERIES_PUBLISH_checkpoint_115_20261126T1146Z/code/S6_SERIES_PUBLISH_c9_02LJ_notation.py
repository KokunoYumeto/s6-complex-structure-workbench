#!/usr/bin/env python3
"""Scoped reversible source proposal for the full mixed-three-primary proof."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02LJ", "maps:src:D.2.42", "253f4b0f52530f18e3d9da65881791e334167a8dc98a0453fd24fdc686c73fef", "484–500",
           "Read all 1,395 lines, fourteen patterns, integral graph/cap maps, all affine parameters, primitive periods, both line constructions, common Borel imports, full primary detectors, CRT maps and recognition. Traced finite Bezout coefficients, sweeps, affine lift, pairing entries, scalar order and the two quotient-map domains through their complete uses.")

affine_reason = ("R_aff=R is the identical affine map x↦Tx+v/m on the same good cover; its inverse is x↦T^{-1}(x-v/m). The later fixed-point iterate is the same map, and the displayed translation conjugacies and their inverses retain all affine parameters. The physical line contraction R and the separately printed holomorphic operator mathcal R keep their original meanings.")
p.exact("affine-representative",
        r"The affine representative is \(R(x)=Tx+v/m\).",
        r"The affine representative is \(R_{\rm aff}(x)=Tx+v/m\).", affine_reason)
p.exact("affine-fixed-point",
        r"\(x+\theta\delta=R^j x\) modulo the lattice.",
        r"\(x+\theta\delta=R_{\rm aff}^{\,j}x\) modulo the lattice.", affine_reason)

p.scope("finite-bezout-pair", r"For \(A_0m+B_0n=1\)", r"\item \emph{Primitive rank-one periods",
        p.literals([("A_0", r"A_{\rm fin}"), ("B_0", r"B_{\rm fin}")]),
        "A_fin=A_0 and B_fin=B_0 are exactly the finite-cap Bezout coefficients A_fin m+B_fin n=1. Identity on this ordered pair preserves the central-surface basis, its inverse, every Thom column combination, both elimination identities and the special choice (epsilon e,-epsilon). The later A_0=a kappa/d_0 and B_0=b kappa/n_0 are the normalized period entries and remain unchanged.")

sweep_reason = ("D_delta=D=t(delta) and L_ell=L=t(ell) are the identical finite boundary sweeps. The coordinate identity on (s,D_delta,L_ell), with inverse identity, preserves every full Thom column and the relations D_delta=-be s, L_ell=0. The later Borel argument imports precisely these same equations. Graph differential D, long period basis L and all their inverse maps remain unchanged.")
p.scope("finite-boundary-sweeps", "Sectors of its meridional disc", r"\item \emph{Primitive rank-one periods",
        p.symbols([("D", r"D_\delta"), ("L", r"L_\ell")]), sweep_reason)
p.exact("borel-sweep-import",
        r"gives \(L=0,D=-be\,s=0\) modulo",
        r"gives \(L_\ell=0,D_\delta=-be\,s=0\) modulo", sweep_reason)

pairing_reason = ("n_per=N=a nu/d_0² and r_per=R=-b d_0²/nu are the same diagonal entries of K_N=(SC_S)^t omega(LC_L). Identity on the two integers and the unchanged primitive basis preserves the pairing, I_p specialization, doubled/undoubled supports, base-return exponent, physical support and finite character. The nodal names K_N,Pi_N and epsilon_N remain; scalar subgroup order and physical R are given their own unchanged domains.")
p.exact("nodal-pairing-entries",
        r"""       =\begin{pmatrix}N&0\\M&R\end{pmatrix},\qquad
 N=\frac{a\nu}{d_0^2},\quad R=-\frac{bd_0^2}{\nu},\qquad""",
        r"""       =\begin{pmatrix}n_{\rm per}&0\\M&r_{\rm per}\end{pmatrix},\qquad
 n_{\rm per}=\frac{a\nu}{d_0^2},\quad r_{\rm per}=-\frac{bd_0^2}{\nu},\qquad""", pairing_reason)
p.exact("ip-pairing-specialization",
        r" d_0=1,\quad n_0=p,\quad N=ap,\quad R=-b/p.",
        r" d_0=1,\quad n_0=p,\quad n_{\rm per}=ap,\quad r_{\rm per}=-b/p.", pairing_reason)
p.exact("doubled-nodal-support",
        r"The integer support \(Nj^2\) has difference \(2Nhj+Nh^2\), and",
        r"The integer support \(n_{\rm per}j^2\) has difference \(2n_{\rm per}hj+n_{\rm per}h^2\), and", pairing_reason)
p.exact("nodal-base-exponent",
        r"add the same \(NW_1^2\)", r"add the same \(n_{\rm per}W_1^2\)", pairing_reason)
p.exact("physical-nodal-support",
        r"                         =-Nj^2+N\alpha_0j.",
        r"                         =-n_{\rm per}j^2+n_{\rm per}\alpha_0j.", pairing_reason)
p.exact("ip-line-character",
        r"is \(-\sigma N(2j+1)=0\pmod p\) for odd \(p\).",
        r"is \(-\sigma n_{\rm per}(2j+1)=0\pmod p\) for odd \(p\).", pairing_reason)
p.exact("undoubled-nodal-support",
        r"\((Nj^2-\mathcal Q(l)j)/2\).", r"\((n_{\rm per}j^2-\mathcal Q(l)j)/2\).", pairing_reason)
p.exact("nonprimitive-undoubled-support",
        r"so \(-N j(j-d_0)/2\) is integral.",
        r"so \(-n_{\rm per}j(j-d_0)/2\) is integral.", pairing_reason)

polarization_reason = ("D_pol=D=diag(a,-b) is the identical two-by-two physical polarization matrix. Identity on the ordered two-dimensional bases preserves its symmetry with Pi_ph, both Gaussian exponents, and K=C^t D_pol. Every reciprocal gauge and period factor is unchanged. The earlier graph differential D retains its rectangular domain and original inverse construction.")
p.exact("physical-polarization",
        r""" D=\operatorname{diag}(a,-b),\quad
 \Pi_{\rm ph}=\begin{pmatrix}\tau_E&-b\zeta_G\\a\zeta_G&\rho_L\end{pmatrix},
 \qquad D\Pi_{\rm ph}=(D\Pi_{\rm ph})^t.""",
        r""" D_{\rm pol}=\operatorname{diag}(a,-b),\quad
 \Pi_{\rm ph}=\begin{pmatrix}\tau_E&-b\zeta_G\\a\zeta_G&\rho_L\end{pmatrix},
 \qquad D_{\rm pol}\Pi_{\rm ph}=(D_{\rm pol}\Pi_{\rm ph})^t.""", polarization_reason)
p.exact("doubled-physical-gaussian",
        r"G_D=\exp\{-2\pi i(U^tDW+W^tD\Pi_{\rm ph}W)\}",
        r"G_D=\exp\{-2\pi i(U^tD_{\rm pol}W+W^tD_{\rm pol}\Pi_{\rm ph}W)\}", polarization_reason)
p.exact("cusp-polarization", r"K=C^tD=", r"K=C^tD_{\rm pol}=", polarization_reason)
p.exact("undoubled-physical-gaussian",
        r"\exp\{\pi i[-U^tDW-W^tD\Pi_{\rm ph}W+Z_1]\}",
        r"\exp\{\pi i[-U^tD_{\rm pol}W-W^tD_{\rm pol}\Pi_{\rm ph}W+Z_1]\}", polarization_reason)

p.scope("scalar-subgroup-order", r"The scalar lift by \(\delta/N\)", "The physical Gaussian is",
        p.symbols([("N", r"N_{\rm sc}")]),
        "N_sc=N is the same positive scalar subgroup order dividing b. The action delta/N_sc, line multiplier, commutator and N_sc-th power are the same maps, with the same negative-translation inverse. This identity keeps the site count N and the nodal entry n_per in their respective domains.")

p.scope("based-cw-retraction", r"homotopy groups thus vanish.", "For three primes apply",
        p.literals([(r"\(q\)", r"\(r_{\rm CW}\)", 1),
                    (r"\(iq\)", r"\(i r_{\rm CW}\)", 1),
                    (r"\(qi=", r"\(r_{\rm CW}i=", 1),
                    (r"\(iq\simeq", r"\(i r_{\rm CW}\simeq", 1)]),
        "r_CW=q is the same based cellular map K_p×K_q→K_p∨K_q. The identity of this map preserves the specified cellular construction, r_CW i=id, and i r_CW homotopic to id relative to the wedge. The coefficient prime q, all primary projections/inclusions and the exact CRT maps remain unchanged.")
p.scope("suspension-collapse", r"Let \(q:BC_3\times S^1", "Naturality and",
        p.literals([(r"\(q:", r"\(q_{\rm susp}:", 1),
                    (r"\(q^*", r"\(q_{\rm susp}^*", 2)]),
        "q_susp=q is the identical map BC_3×S¹→S¹∧BC_3 obtained by the displayed factor flip and wedge collapse. Identity on its source and target preserves both pullback formulas and their sign. This reversible change of name leaves the left-interval suspension and its slant inverse intact; it makes no inverse claim for the collapse map itself. The based CW retraction has its separate name r_CW.")

p.finish()
