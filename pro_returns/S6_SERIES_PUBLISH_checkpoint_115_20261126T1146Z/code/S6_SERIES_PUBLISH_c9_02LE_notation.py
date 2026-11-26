#!/usr/bin/env python3
"""Bounded identity renamings for the complete order-ten/fourteen proof."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02LE", "maps:src:D.2.38", "d0882609c2841a97e9facb16a3e0c2a4a78b4149a253fe02d8df97ac470c7934", "457–473",
           "Read all 1,304 lines and each marked table entry, exterior cylinder map, finite Thom kernel, line gauge, rank-one/cusp extension, fixed set, Borel comparison, coprime homotopy map, invariant and connected-sum marking. Prepared identity names for the cylinder lift, boundary sweeps, scalar order, real long coordinate, holomorphic unit matrix and based CW retraction, with all original inverses retained.")

p.scope("integer-cylinder-lift", "The integral exterior sequence", "For a rank-one site, set",
        p.literals([("R", r"R_{\rm cyl}", 4)]),
        "R_cyl=R is the same integer cylinder-chain lift from the six-dimensional exterior-coordinate lattice to the monodromy-cylinder coefficient lattice. Its defining matrix identity B_2 R_cyl=I_6-s_0 omega and the chain R_cyl v are unchanged, so the existing quotient map and inverse n↦[n s_0] have the identical proof. Physical holomorphic factor R remains unchanged later.")

p.scope("finite-boundary-sweeps", "For completeness retain the full degree-two Thom kernel before", "The index-one cusp has Euler contribution",
        p.symbols([("D", r"D_\delta"), ("L_0", r"L_\ell")]),
        "D_delta=D=t(delta) and L_ell=L_0=t(ell) are the same two exterior sweep classes. Identity on the ordered coordinates (s,D_delta,L_ell), with inverse identity, preserves every C_1,C_2,C_3,K_0 column and the complete finite and ordinary kernel. The quotient substitutions remain D_delta=-be s and L_ell=br(alpha+eta e)s. Later D is the polarization matrix and L_0 is the affine support row; their existing names and maps are retained.")

scalar_reason = ("N_sc=N is the same positive scalar subgroup order dividing b. The action vector is the identical delta/N_sc and the same exponential multiplier defines T_tau, whose inverse is T_{-tau}; its N_sc-th power remains J_delta. Identity on this integer preserves the C_2,C_p,C_{2p} specializations. The earlier site count N in the monodromy-cylinder matrix remains unchanged.")
p.scope("scalar-group-order", "The finite scalar lift is", "Here are the maps identifying this line",
        p.symbols([("N", r"N_{\rm sc}")]), scalar_reason)
p.exact("scalar-holomorphic-action",
        r"(z,e^{2\pi i/N}v,\zeta)", r"(z,e^{2\pi i/N_{\rm sc}}v,\zeta)", scalar_reason)

coordinate_reason = ("v_per=B is the same real long-coordinate column in R². The coordinate identity (U,B)↦(U,v_per) and its inverse preserve x=SU+L v_per, the cusp change x=SCU+L v_per, each complex coordinate Z, every Gaussian exponent and the base-return substitution. All short/long bases, polarization matrices, line factors and reciprocal inverse gauges remain unchanged.")
p.scope("physical-long-coordinate", r"Write $x=SU+LB$", "The further gauge",
        p.literals([("B", r"v_{\rm per}", 6)]), coordinate_reason)
p.exact("cusp-long-coordinate",
        r"Use $x=SCU+LB$, $Z=U+\Pi B$, where",
        r"Use $x=SCU+Lv_{\rm per}$, $Z=U+\Pi v_{\rm per}$, where", coordinate_reason)
p.exact("holomorphic-unit-matrix",
        r"$\Pi=(\log q)/(2\pi i)I+B(q)$",
        r"$\Pi=(\log q)/(2\pi i)I+B_{\rm hol}(q)$",
        "B_hol(q)=B(q) is the same full holomorphic two-by-two unit matrix, fixed entry by entry with the same q dependence. The distinct real coordinate v_per is already given its exact identity map, and every occurrence of the unit function in Pi is retained.")
p.scope("cusp-gaussian-long-coordinate", "The Gaussian\n\n", "The integer vertex support",
        p.literals([("B", r"v_{\rm per}", 6)]), coordinate_reason)
p.scope("nodal-gaussian-long-coordinate", "The Gaussian formula for this basis uses", "The symmetry is",
        p.literals([("B", r"v_{\rm per}", 4)]), coordinate_reason)

p.scope("based-cw-retraction", "over successive skeleta.", "The finite wedge axiom",
        p.literals([(r"$q$", r"$r_{\rm CW}$", 1),
                    (r"$qi=", r"$r_{\rm CW}i=", 1),
                    (r"$iq\simeq", r"$i r_{\rm CW}\simeq", 1),
                    (r"$i,q$", r"$i,r_{\rm CW}$", 1)]),
        "r_CW=q is the same based cellular retraction K_2×K_p→K_2∨K_p. Identity on the chosen cellular map preserves r_CW i=id and i r_CW homotopic to id relative to the wedge; the construction and homotopy scope stay unchanged. Its later use with the coefficient isomorphism theta is renamed as well. The coefficient prime index q=2,p remains unchanged.")

p.finish()
