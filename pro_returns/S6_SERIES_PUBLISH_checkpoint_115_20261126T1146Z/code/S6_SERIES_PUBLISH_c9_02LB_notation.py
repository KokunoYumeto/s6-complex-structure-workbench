#!/usr/bin/env python3
"""Scoped source disposition of the complete order-two proof."""
from S6_SERIES_PUBLISH_c9_backend_notation import Packet

p = Packet("02LB", "maps:src:D.2.35", "1715f11142647695c9e090a58cdd08fba278d81229ed5e15bc4274e0c3b51a5b", "435–445",
           "Read every period, cap, fixed-set, attachment, Borel, surgery and recognition paragraph. Traced the angular minor, real long-coordinate vector, holomorphic unit matrix, two valuation columns, rank-one pairing integer and boundary sweep through their full uses. Prepared identity renamings with the same matrices, line factors, inverse gauges and characteristic evaluations.")

p.scope("angular-unimodular-minor", "The following submatrices $B$", "Since $f$ is primitive",
        p.symbols([("B", r"B_{\rm ang}")]),
        "B_ang=B is the same three-by-three minor in the first three angular coordinates and the same listed column indices. Its entries, determinant signs and right inverse (det B_ang)adj(B_ang) are unchanged. Identity on the three selected source columns and target basis gives both coordinate directions.")

p.exact("free-abelian-kernel",
        "Its kernel is a rank-zero subgroup of a free\ngroup, hence zero.",
        "Its kernel is a rank-zero subgroup of a free abelian\ngroup, hence zero.",
        "The degree-one Mayer–Vietoris source is the explicitly stated direct sum of integral H_1 groups, with addition. The subgroup kernel inherits that commuting law. The identity on every source generator and on the existing boundary matrix preserves the rank-zero argument; abelian states the given group structure.")

coordinate_reason = ("v_per=B is the same real long-coordinate column in R². The coordinate identification (U,B)↦(U,v_per) and its inverse fix both entries; hence x=SU+L v_per, Z=U+Pi v_per, every Gaussian exponent and the base-return substitution are exactly the original maps. The physical short/long bases, polarization, line coordinate and reciprocal inverse gauges are unchanged.")
p.scope("physical-long-coordinate", "In real short/long coordinates", "is an invertible gauge",
        p.literals([("B", r"v_{\rm per}")]), coordinate_reason)
p.exact("holomorphic-period-unit", r"\Pi=(\log q)/(2\pi i)I+B(q)",
        r"\Pi=(\log q)/(2\pi i)I+B_{\rm hol}(q)",
        "B_hol(q)=B(q) is the same full holomorphic two-by-two unit matrix in the period function. It is fixed entry by entry, with identical q dependence. The renamed real long-coordinate column is v_per, and the earlier three-by-three angular minor is B_ang.")
p.scope("cusp-long-coordinate", "For $x=SC_0U+LB$", "The integral Cartier function",
        p.literals([("B", r"v_{\rm per}")]), coordinate_reason)
p.scope("rank-one-long-coordinate", "The common prequantum line has", "This keeps the full off-diagonal",
        p.literals([("B", r"v_{\rm per}")]), coordinate_reason)

p.exact("valuation-columns",
        r"$H=\alpha_0\nu_0$, $F=\beta_0\nu_0$, where",
        r"$H_{\rm val}=\alpha_0\nu_0$, $F_{\rm val}=\beta_0\nu_0$, where",
        "H_val=H and F_val=F are exactly the two valuation columns (n,aj)^t and (-bj,rho)^t, with unchanged alpha_0,beta_0 and primitive nu_0. Their coordinate identity preserves the four following scalar equalities, support and period differences. The four-dimensional period-basis map H and the actual line return F, including its later F h^(bj/2) comparison and inverse, retain their existing meanings.")

p.scope("rank-one-pairing-integer", "The common prequantum line has", r"\item \emph{The actual fixed curves",
        p.literals([("N", r"n_{\rm per}")]),
        "n_per=N=Omega(l,h) is the same integer first entry of the rank-one pairing K_1. Every node support, parity identity, equality n_per=k and support comparison uses the identical integer. The earlier number N of base holes is retained in its Mayer–Vietoris count.")

p.scope("finite-boundary-sweep", r"\item \emph{The integral attachment", r"\item \emph{The global equivariant comparison",
        p.symbols([("D", r"D_\delta")]),
        "D_delta=D=t(delta) is the same fixed-normal boundary sweep in the additive exterior H_2 coordinates. The identity on s,D_delta and the other sweep fixes every finite/ordinary Thom column; eliminating it still gives D_delta=-be s, with that same inverse substitution. The polarization matrix D=diag(a,-b) keeps its existing name, and every integer coefficient is preserved.")

p.finish()
